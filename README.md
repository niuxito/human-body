# Anatomía en capas

Atlas 3D interactivo del cuerpo humano para uso educativo. Incluye 934 estructuras anatómicas en 11 sistemas, con capas que se pueden activar y desactivar, opacidad por sistema, búsqueda y una ficha en español de cada estructura.

## Cómo usarlo

1. Descomprime el zip.
2. Abre `index.html` con doble clic en cualquier navegador moderno (Chrome, Firefox, Edge, Safari).

Funciona sin conexión y sin instalar nada. Las tipografías van incluidas en `fonts/` (Newsreader e IBM Plex, licencia SIL OFL 1.1), así que no se contacta con ningún servidor externo.

Para modificar el visor, edita `src/visor.js` y regenera `app.js`:

```
npm install
npm run build
```

Para publicarlo en la web basta con subir la carpeta tal cual a cualquier alojamiento estático (GitHub Pages, Netlify, el servidor del centro…).

## Contenido del paquete

| Archivo | Qué es |
|---|---|
| `index.html` | Página del visor (estructura y estilos) |
| `src/visor.js` | **Código fuente** del visor (JavaScript legible, módulo ES) |
| `app.js` | El mismo código empaquetado con three.js, sin minificar (generado) |
| `package.json` | Dependencias y comando para regenerar `app.js` |
| `herramientas/` | Scripts que prepararon las mallas y las fichas (ver `herramientas/LEEME.md`) |
| `fonts/` | Tipografías en local con sus licencias OFL |
| `data/anatomia.js` | Fichas, nombres y organización por sistemas |
| `models/*.js` | Mallas 3D (glTF binario comprimido con meshoptimizer, en base64) |
| `LICENSE` | Licencia MIT del código (copia de `LICENSE-codigo.txt`, para que GitHub la detecte) |
| `LICENSE-codigo.txt` | Licencia MIT del código |
| `LICENSE-contenido.md` | Licencia de las mallas y los textos |
| `LICENSE-three.js.txt` | Licencia MIT de three.js |
| `LICENSE-meshoptimizer.txt` | Licencia MIT de meshoptimizer |

## Fuente de los datos y créditos

Las mallas 3D derivan de **BodyParts3D**, © The Database Center for Life Science (DBCLS), Japón, distribuidas bajo licencia [CC BY-SA 2.1 Japón](https://creativecommons.org/licenses/by-sa/2.1/jp/).
Fuente: https://lifesciencedb.jp/bp3d/ (copia usada: https://github.com/Kevin-Mattheus-Moerman/BodyParts3D).

**Cambios realizados sobre las mallas originales:** simplificación de unos 26 millones a 3,3 millones de triángulos; cambio de ejes y de unidades (de mm a m); compresión con meshoptimizer; asignación de colores y agrupación por sistemas.

Las fichas descriptivas en español son obra original de este proyecto.

## Licencias

- **Código** (`index.html`, `src/`, `herramientas/` y `app.js`, salvo three.js): MIT. Ver `LICENSE-codigo.txt`.
- **Mallas y fichas** (`models/`, `data/`): CC BY-SA 4.0, obligatorio porque las mallas derivan de BodyParts3D (CC BY-SA). Ver `LICENSE-contenido.md`.
- **Bibliotecas incluidas en `app.js`:** three.js y meshoptimizer, ambas MIT (ver sus ficheros `LICENSE-*`).

## Limitaciones

Modelo de un único varón adulto. No incluye médula espinal, nervios periféricos, glándula tiroides, lengua, laringe (salvo el cartílago tiroides), vasos linfáticos ni la mayoría de los vasos de los miembros. Las fichas no han sido revisadas por especialistas: conviene que un docente las revise antes de usarlas en clase.

## Autoría

Visor y fichas: Alexis Parrón, 2026. Desarrollado con ayuda de Claude (Anthropic).

Biblioteca 3D: [three.js](https://threejs.org) (MIT).

Descompresión y compresión de mallas: [meshoptimizer](https://github.com/zeux/meshoptimizer) (MIT, © Arseny Kapoulkine). Su decodificador va incluido en `app.js` y las mallas se comprimieron con gltfpack. Ver `LICENSE-meshoptimizer.txt`.
