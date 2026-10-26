"""Paso 0 (humano): lista de mallas de BodyParts3D con su nombre en inglés -> stlnames.txt
Entrada: carpeta con los STL de BodyParts3D y parts_list_e.txt (ambos en el repositorio
https://github.com/Kevin-Mattheus-Moerman/BodyParts3D, carpeta assets/BodyParts3D_data)."""
import os, sys
BP = sys.argv[1] if len(sys.argv) > 1 else 'BodyParts3D/assets/BodyParts3D_data'
names = {}
for line in open(os.path.join(BP, 'parts_list_e.txt'), encoding='utf-8', errors='replace'):
    p = line.rstrip('\n').split('\t')
    if len(p) >= 2: names[p[0]] = p[1]
ids = sorted(f[:-4] for f in os.listdir(os.path.join(BP, 'stl')) if f.endswith('.stl'))
open('stlnames.txt', 'w', encoding='utf-8').write('\n'.join(f'{i}\t{names.get(i, "?")}' for i in ids))
print(len(ids), 'mallas;', sum(1 for i in ids if i not in names), 'sin nombre')
