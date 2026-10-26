"""Paso 1 (humano): asigna cada malla a su sistema (según las fichas de anat_*.py) -> fidsys.json,
que meshes.py usa para dar más detalle a órganos y huesos que a músculos y piel."""
import re, json
import anat_a, anat_b, anat_c  # noqa: anat_b y anat_c completan el diccionario de anat_a al importarse
C, FULL = anat_a.C, anat_c.FULL
out = {}
for line in open('stlnames.txt', encoding='utf-8').read().split('\n'):
    fid, en = line.split('\t')
    if en in FULL: s = FULL[en]['s']
    else:
        b = re.sub(r'\s+', ' ', re.sub(r'\b(right|left)\b ?', '', en).strip())
        s = C[b]['s']          # falla si una malla no tiene ficha: así no se cuela ninguna sin revisar
    out[fid] = s
json.dump(out, open('fidsys.json', 'w'))
print(len(out), 'mallas asignadas')
