import os, sys, numpy as np, trimesh, fast_simplification, json
from concurrent.futures import ProcessPoolExecutor
D = 'BodyParts3D/assets/BodyParts3D_data/stl/'
OUT = 'simp/'
os.makedirs(OUT, exist_ok=True)
K = float(sys.argv[1]) if len(sys.argv) > 1 else 40.0
EXP = 0.40
SPECIAL = {'FMA7163': 110000}  # piel
FS = json.load(open('fidsys.json'))
KS = {'mus':1.0,'esq':1.5,'teg':1.0}

def target(n, fid):
    if fid in SPECIAL: return SPECIAL[fid]
    k = K * KS.get(FS.get(fid), 2.6)
    return int(min(n, max(800, k * n ** EXP)))

def work(f):
    fid = f[:-4]
    m = trimesh.load(D + f, process=True)
    v = np.asarray(m.vertices, dtype=np.float32); fc = np.asarray(m.faces, dtype=np.int32)
    n = len(fc); t = target(n, fid)
    if t < n:
        v, fc = fast_simplification.simplify(v, fc, target_reduction=1 - t / n, agg=5)
    # Z-up (mm, anterior -Y) -> Y-up (m, anterior +Z): (X, Z, -Y)
    v = np.stack([v[:, 0], v[:, 2], -v[:, 1]], 1) / 1000.0
    np.savez(OUT + fid + '.npz', v=v.astype(np.float32), f=fc.astype(np.uint32))
    return fid, n, len(fc)

if __name__ == '__main__':
    files = sorted(x for x in os.listdir(D) if x.endswith('.stl'))
    if '--estimate' in sys.argv:
        import struct
        tot = 0
        for f in files:
            with open(D + f, 'rb') as fh:
                fh.seek(80); n = struct.unpack('<I', fh.read(4))[0]
            tot += target(n, f[:-4])
        print('K', K, 'estimated tris', tot); sys.exit()
    stats = {}
    with ProcessPoolExecutor(os.cpu_count()) as ex:
        for fid, n, t in ex.map(work, files, chunksize=4):
            stats[fid] = [n, t]
    json.dump(stats, open('simp_stats.json', 'w'))
    print('done', sum(s[1] for s in stats.values()))
