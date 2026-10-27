// Textos de la interfaz por idioma. Para añadir un idioma:
//  1. añade su código a LANGS y a LANG_NAMES, y un bloque en STR (lo que falte se toma del español);
//  2. crea data/anatomia.<código>.js con las fichas traducidas (ver CONTRIBUTING.md).
export const LANGS = ['es', 'en'];
export const LANG_NAMES = {es: 'Español', en: 'English'};

export function detectLang(){
  const q = new URLSearchParams(location.search).get('lang');
  if (LANGS.includes(q)) return q;
  try { const s = localStorage.getItem('lang'); if (LANGS.includes(s)) return s; } catch (e) {}
  const nav = (navigator.languages || [navigator.language || 'es']).map(l => l.slice(0, 2).toLowerCase());
  return nav.find(l => LANGS.includes(l)) || 'en';
}

export const STR = {
  es: {
    title: 'Anatomía en capas',
    metaDesc: 'Atlas 3D interactivo del cuerpo humano (BodyParts3D) con capas y fichas en español.',
    brand: 'Anatomía <em>en capas</em>',
    langLabel: 'Idioma',
    views: 'Vistas', front: 'Anterior', back: 'Posterior', right: 'Lateral dcho.', left: 'Lateral izq.', top: 'Superior',
    spin: 'Girar', reset: 'Restablecer',
    panelLayers: 'Capas y sistemas', panelCard: 'Ficha de la estructura',
    tabs: 'Paneles', tabModel: 'Modelo', tabLayers: 'Capas', tabCard: 'Ficha',
    searchPh: 'Buscar estructura (p. ej. «fémur», «hígado»)', search: 'Buscar estructura',
    peel: 'Pelar capas', peelAll: 'Todo', peelSkin: 'Sin piel', peelMuscle: 'Sin músculo', peelViscera: 'Vísceras',
    loading: 'Cargando modelo anatómico…',
    credit: 'Modelo 3D: <a href="https://lifesciencedb.jp/bp3d/" target="_blank" rel="noopener">BodyParts3D</a> © DBCLS · <a href="https://creativecommons.org/licenses/by-sa/2.1/jp/deed.es" target="_blank" rel="noopener">CC BY-SA 2.1 JP</a> · adaptación CC BY-SA 4.0 · simplificado para web · uso educativo, no clínico',
    sideD: 'Lado derecho', sideI: 'Lado izquierdo', sideDs: 'dcho.', sideIs: 'izq.',
    stats: (n, c, s) => `${n} estructuras · ${c} fichas · ${s} sistemas · varón adulto`,
    systemReady: (name, d, total) => `Sistema ${name.toLowerCase()} listo (${d}/${total})`,
    modelDone: 'Modelo completo',
    errSystem: name => `No se pudo cargar el sistema ${name}.`,
    errData: msg => `Error al cargar los datos: ${msg}`,
    toggleSys: name => `Mostrar u ocultar ${name}`, showGroup: name => `Mostrar ${name}`,
    opacity: 'Opacidad', noResults: 'Sin resultados',
    howTo: 'Cómo usarlo', selectAny: 'Selecciona cualquier estructura del cuerpo',
    how1: 'Arrastra para girar, rueda o pellizca para acercar y clic derecho para desplazar.',
    how2: 'Haz clic en un órgano, hueso o músculo para ver su nombre y su ficha.',
    how3: 'Usa <b>Pelar capas</b> o el ojo de cada sistema para retirar tejidos; ajusta su opacidad para ver a través.',
    how4: 'Atajos: <kbd>Esc</kbd> deseleccionar · <kbd>F</kbd> enfocar · <kbd>H</kbd> ocultar · <kbd>I</kbd> aislar',
    systemsIncluded: 'Sistemas incluidos',
    aboutTitle: 'Acerca del modelo y su rigor',
    about: `<p>La geometría procede de <a href="https://lifesciencedb.jp/bp3d/" target="_blank" rel="noopener">BodyParts3D</a> (Database Center for Life Science, Japón), un atlas construido a partir de imágenes de resonancia magnética de un varón adulto y etiquetado con los identificadores de la <i>Foundational Model of Anatomy</i> (FMA). Cada malla conserva su identificador original, visible en la ficha.</p>
        <p>Para que funcione en el navegador, las mallas se han simplificado (≈26 millones → ≈3,3 millones de triángulos) sin alterar su posición ni su forma general. La nomenclatura sigue la Terminología Anatómica en español.</p>
        <p><b>Estructuras que el modelo de origen no incluye:</b></p>
        <ul><li>Médula espinal y nervios periféricos (solo el nervio y la vía ópticos).</li><li>Glándula tiroides, lengua, glándulas salivales, faringe y laringe (salvo el cartílago tiroides).</li><li>Ganglios y vasos linfáticos; la mayoría de arterias y venas de los miembros y de la cabeza.</li><li>Terceros molares, meninges y algunas circunvoluciones cerebrales.</li><li>Anatomía femenina: el modelo es de un único individuo varón, por lo que hay variación anatómica normal entre personas.</li></ul>
        <p>Licencia: los datos se distribuyen bajo <a href="https://creativecommons.org/licenses/by-sa/2.1/jp/deed.es" target="_blank" rel="noopener">CC BY-SA 2.1 Japón</a>; las mallas derivadas y las fichas de este visor se comparten bajo <a href="https://creativecommons.org/licenses/by-sa/4.0/deed.es" target="_blank" rel="noopener">CC BY-SA 4.0</a>, y el código bajo licencia MIT.</p>
        <p><b>Uso educativo, no clínico.</b> Este atlas es un material de estudio: no sirve para diagnóstico ni para decisiones médicas, y sus fichas no han sido revisadas por especialistas.</p>`,
    focus: 'Enfocar', isolate: 'Aislar', showAll: 'Ver todo', hide: 'Ocultar',
    dimRest: 'Atenuar el resto del cuerpo',
    source: (id, en) => `Fuente: BodyParts3D · ${id}<br>Término original: ${en}`,
  },
  en: {
    title: 'Layered Anatomy',
    metaDesc: 'Interactive 3D atlas of the human body (BodyParts3D) with layers and anatomical cards.',
    brand: 'Layered <em>anatomy</em>',
    langLabel: 'Language',
    views: 'Views', front: 'Anterior', back: 'Posterior', right: 'Right lateral', left: 'Left lateral', top: 'Superior',
    spin: 'Rotate', reset: 'Reset',
    panelLayers: 'Layers and systems', panelCard: 'Structure card',
    tabs: 'Panels', tabModel: 'Model', tabLayers: 'Layers', tabCard: 'Card',
    searchPh: 'Search structure (e.g. "femur", "liver")', search: 'Search structure',
    peel: 'Peel layers', peelAll: 'All', peelSkin: 'No skin', peelMuscle: 'No muscle', peelViscera: 'Viscera',
    loading: 'Loading anatomical model…',
    credit: '3D model: <a href="https://lifesciencedb.jp/bp3d/" target="_blank" rel="noopener">BodyParts3D</a> © DBCLS · <a href="https://creativecommons.org/licenses/by-sa/2.1/jp/deed.en" target="_blank" rel="noopener">CC BY-SA 2.1 JP</a> · adaptation CC BY-SA 4.0 · simplified for the web · educational use, not clinical',
    sideD: 'Right side', sideI: 'Left side', sideDs: 'R', sideIs: 'L',
    stats: (n, c, s) => `${n} structures · ${c} cards · ${s} systems · adult male`,
    systemReady: (name, d, total) => `${name} system ready (${d}/${total})`,
    modelDone: 'Model complete',
    errSystem: name => `Could not load the ${name} system.`,
    errData: msg => `Error loading data: ${msg}`,
    toggleSys: name => `Show or hide ${name}`, showGroup: name => `Show ${name}`,
    opacity: 'Opacity', noResults: 'No results',
    howTo: 'How to use it', selectAny: 'Select any structure of the body',
    how1: 'Drag to rotate, scroll or pinch to zoom, and right-click to pan.',
    how2: 'Click an organ, bone or muscle to see its name and its card.',
    how3: 'Use <b>Peel layers</b> or the eye on each system to remove tissues; adjust opacity to see through.',
    how4: 'Shortcuts: <kbd>Esc</kbd> deselect · <kbd>F</kbd> focus · <kbd>H</kbd> hide · <kbd>I</kbd> isolate',
    systemsIncluded: 'Systems included',
    aboutTitle: 'About the model and its rigor',
    about: `<p>The geometry comes from <a href="https://lifesciencedb.jp/bp3d/" target="_blank" rel="noopener">BodyParts3D</a> (Database Center for Life Science, Japan), an atlas built from magnetic resonance images of an adult male and labelled with <i>Foundational Model of Anatomy</i> (FMA) identifiers. Each mesh keeps its original identifier, shown on its card.</p>
        <p>To run in the browser, the meshes were simplified (≈26 million → ≈3.3 million triangles) without altering their position or overall shape. Nomenclature follows the Terminologia Anatomica. The cards were written in Spanish; the English cards are a translation that has not been reviewed by specialists.</p>
        <p><b>Structures the source model does not include:</b></p>
        <ul><li>Spinal cord and peripheral nerves (only the optic nerve and pathway).</li><li>Thyroid gland, tongue, salivary glands, pharynx and larynx (except the thyroid cartilage).</li><li>Lymph nodes and lymphatic vessels; most arteries and veins of the limbs and head.</li><li>Third molars, meninges and some cerebral gyri.</li><li>Female anatomy: the model is a single male individual, so normal anatomical variation between people applies.</li></ul>
        <p>License: the data are distributed under <a href="https://creativecommons.org/licenses/by-sa/2.1/jp/deed.en" target="_blank" rel="noopener">CC BY-SA 2.1 Japan</a>; the derived meshes and the cards of this viewer are shared under <a href="https://creativecommons.org/licenses/by-sa/4.0/deed.en" target="_blank" rel="noopener">CC BY-SA 4.0</a>, and the code under the MIT license.</p>
        <p><b>Educational use, not clinical.</b> This atlas is study material: it is not for diagnosis or medical decisions, and its cards have not been reviewed by specialists.</p>`,
    focus: 'Focus', isolate: 'Isolate', showAll: 'Show all', hide: 'Hide',
    dimRest: 'Dim the rest of the body',
    source: (id, en) => `Source: BodyParts3D · ${id}<br>Original term: ${en}`,
  },
};
