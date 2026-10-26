# Herramientas de preparación de datos

Scripts en Python 3 que generan `models/` y `data/` a partir de BodyParts3D. Se ejecutan todos desde esta carpeta.
Dependencias: `numpy`, `trimesh`, `fast-simplification` y [gltfpack](https://github.com/zeux/meshoptimizer) (`npm install gltfpack`).

Datos de entrada: el repositorio https://github.com/Kevin-Mattheus-Moerman/BodyParts3D clonado aquí como `BodyParts3D/`. Hace falta su carpeta `assets/BodyParts3D_data`, con `stl/` y `parts_list_e.txt`.

| Orden | Script | Entrada → salida |
|---|---|---|
| — | `anat_a.py`, `anat_b.py`, `anat_c.py` | Fichas en español: sistemas, esqueleto y piel (a), músculos (b) y resto de órganos (c). Los importan los demás scripts |
| 0 | `00_lista_piezas.py` | `parts_list_e.txt` + `stl/` → `stlnames.txt` (identificador y nombre en inglés de cada malla) |
| 1 | `01_sistemas.py` | `stlnames.txt` + fichas → `fidsys.json` (sistema de cada malla). Se detiene si alguna malla no tiene ficha |
| 2 | `02_mallas.py 50` | `stl/` + `fidsys.json` → `simp/*.npz` (≈3,3 millones de triángulos; el 50 es el factor de detalle) |
| 3 | `03_exportar.py` | `simp/` + `stlnames.txt` + fichas → `site/models/*.glb` y `site/anatomia.json` |
| 4 | `04_base64.py site/models` | `*.glb` → `*.txt` (base64), el formato que se empaqueta en `models/*.js` |

He comprobado que los pasos 0 y 1 reproducen exactamente los archivos usados para el visor publicado.
