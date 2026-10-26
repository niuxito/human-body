# -*- coding: utf-8 -*-
import re, json, os, subprocess, numpy as np, trimesh
import anat_a, anat_b, anat_c
C, FULL, SYSTEMS = anat_a.C, anat_c.FULL, anat_a.SYSTEMS
SIMP = 'simp/'
OUT = 'site/'
os.makedirs(OUT + 'models', exist_ok=True)

rows = [l.split('\t') for l in open('stlnames.txt').read().split('\n')]

# ---------- colores por estructura (realistas, diferenciados)
def color_for(key, en, sysk):
    e = en
    if sysk == 'teg':
        if 'hair' in e: return '#3b2a22' if 'eyebrow' in e or 'head' in e else '#4a3528'
        return '#d9a58c'
    if sysk == 'mus':
        if any(w in e for w in ['tendon', 'aponeurosis', 'linea alba', 'ligament', 'tract', 'retinaculum', 'membrane', 'tendinous arch']):
            return '#e6dccb'
        return '#a8363f'
    if sysk == 'esq':
        if 'disk' in e: return '#9fc3c9'
        if 'cartilage' in e: return '#b9d3d6'
        return '#e9dfc8'
    if sysk == 'car':
        if 'pulmonary artery' in e: return '#3e63b5'
        if 'pulmonary vein' in e: return '#c42a3a'
        if 'vein' in e or 'vena' in e or 'sinus' in e: return '#3e63b5'
        if 'valve' in e: return '#efe3c8'
        if 'papillary' in e: return '#a8323c'
        if 'wall of heart' in e: return '#9e2f35'
        return '#c42a3a'
    if sysk == 'ner':
        if 'eyeball' in e: return '#f1ede6'
        if e == 'ear': return '#d9a58c'
        if 'ventricle' in e or 'aqueduct' in e or 'canal' in e or 'foramen' in e: return '#4fa8d8'
        if 'choroid' in e: return '#c9557a'
        if any(w in e for w in ['optic']): return '#e8c45e'
        if any(w in e for w in ['white matter', 'callosum', 'commissure', 'capsule', 'fornix', 'stria', 'brachium', 'lamina terminalis', 'septum']): return '#f0e7d8'
        if any(w in e for w in ['caudate', 'putamen', 'pallidus', 'thalamus', 'amygdala', 'hippocampus', 'geniculate', 'habenula', 'mammillary', 'hypothalamus', 'tuber']): return '#c98f86'
        if any(w in e for w in ['pons', 'medulla', 'midbrain', 'peduncle', 'colliculus', 'interpeduncular']): return '#d7b19b'
        if 'cerebellum' in e: return '#d49a8e'
        return '#e2b3a4'  # corteza
    if sysk == 'res':
        if 'lung' in e:
            return '#e8a3ab' if 'upper' in e else ('#dd8f99' if 'lower' in e else '#f0b3b9')
        if 'cartilage' in e: return '#b9d3d6'
        return '#dcc9b8'
    if sysk == 'dig':
        if 'tooth' in e: return '#f4efe2'
        if 'gingiva' in e: return '#d9837f'
        if 'labial' in e: return '#c9736c'
        if 'liver' in e: return '#7e3026'
        if 'gallbladder' in e: return '#5c8a3c'
        if 'pancrea' in e: return '#e3b56a'
        if 'taenia' in e: return '#b86b5c'
        if 'stomach' in e: return '#d98876'
        if 'esophagus' in e: return '#cf8a78'
        if 'colon' in e or 'rectum' in e or 'appendix' in e: return '#c9967a'
        return '#e0a08a'  # intestino delgado
    if sysk == 'uri':
        if 'kidney' in e: return '#8c3b2e'
        if 'bladder' in e: return '#d9b45a'
        return '#e0c26a'
    if sysk == 'rep':
        if 'testis' in e: return '#d9a0a8'
        if 'prostate' in e: return '#b87a8a'
        if 'corpus' in e or 'glans' in e: return '#c98a86'
        return '#7f9fd0'
    if sysk == 'end':
        return '#9b7bc9'
    if sysk == 'lin':
        return '#6b2c48' if 'spleen' in e else '#c9a09a'
    return '#cccccc'

concepts = {}
parts = []
for fid, en in rows:
    side = ''
    if en in FULL:
        key = 'F:' + en; c = FULL[en]
    else:
        b = re.sub(r'\b(right|left)\b ?', '', en).strip(); b = re.sub(r'\s+', ' ', b)
        key = b; c = C[b]
        if re.search(r'\bright\b', en): side = 'D'
        elif re.search(r'\bleft\b', en): side = 'I'
    concepts.setdefault(key, c)
    parts.append({'id': fid, 'k': key, 'sd': side, 'en': en, 's': c['s'], 'col': color_for(key, en, c['s'])})

# índice compacto de conceptos
ckeys = sorted(concepts)
cidx = {k: i for i, k in enumerate(ckeys)}
data = {
    'systems': [{'k': k, 'n': n, 'c': col, 'layer': L, 'd': d} for k, n, col, L, d in SYSTEMS],
    'concepts': [{'n': concepts[k]['n'], 's': concepts[k]['s'], 'g': concepts[k]['g'], 'd': concepts[k]['d'], 'f': concepts[k]['f']} for k in ckeys],
    'parts': [{'id': p['id'], 'c': cidx[p['k']], 'sd': p['sd'], 'en': p['en'], 'col': p['col']} for p in parts],
}

# ---------- GLB por sistema
from collections import defaultdict
bysys = defaultdict(list)
for p in parts: bysys[p['s']].append(p)
sizes = {}
tris = {}
for sysk, plist in bysys.items():
    scene = trimesh.Scene()
    nt = 0
    for p in plist:
        z = np.load(SIMP + p['id'] + '.npz')
        m = trimesh.Trimesh(z['v'], z['f'], process=False)
        nt += len(z['f'])
        scene.add_geometry(m, node_name=p['id'], geom_name=p['id'])
    raw = f'raw_{sysk}.glb'
    scene.export(raw)
    out = OUT + f'models/{sysk}.glb'
    r = subprocess.run(['node_modules/.bin/gltfpack', '-i', raw, '-o', out, '-cc', '-kn', '-vn', '10'], capture_output=True, text=True)
    if r.returncode: print(r.stdout, r.stderr)
    sizes[sysk] = os.path.getsize(out); tris[sysk] = nt
    print(sysk, len(plist), nt, round(sizes[sysk] / 1e6, 2), 'MB')
data['files'] = {k: {'bytes': sizes[k], 'tris': tris[k]} for k in sizes}
json.dump(data, open(OUT + 'anatomia.json', 'w', encoding='utf-8'), ensure_ascii=False, separators=(',', ':'))
print('total MB', round(sum(sizes.values()) / 1e6, 2), 'json KB', os.path.getsize(OUT + 'anatomia.json') // 1024)
