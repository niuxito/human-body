// Anatomía en capas — código fuente del visor (módulo ES).
// Se empaqueta en app.js con:  npm install && npm run build
// Datos: window.ANAT_DATA (data/anatomia.js) y window.ANAT_MODELS (models/*.js).
import * as THREE from 'three';
import { OrbitControls } from 'three/addons/controls/OrbitControls.js';
import { GLTFLoader } from 'three/addons/loaders/GLTFLoader.js';
import { MeshoptDecoder } from 'three/addons/libs/meshopt_decoder.module.js';
import { RoomEnvironment } from 'three/addons/environments/RoomEnvironment.js';

const $ = s => document.querySelector(s);
const esc = s => String(s).replace(/[&<>"]/g, c => ({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]));
const norm = s => s.normalize('NFD').replace(/[\u0300-\u036f]/g,'').toLowerCase();
const SIDE = {D:'Lado derecho', I:'Lado izquierdo', '':''};
const SIDE_SHORT = {D:'dcho.', I:'izq.', '':''};

// ---------------------------------------------------------------- escena
const stage = $('#stage');
const renderer = new THREE.WebGLRenderer({antialias:true, alpha:true, powerPreference:'high-performance'});
renderer.setPixelRatio(Math.min(devicePixelRatio, 2));
renderer.setSize(innerWidth, innerHeight);
renderer.toneMapping = THREE.ACESFilmicToneMapping;
renderer.toneMappingExposure = 1.05;
stage.appendChild(renderer.domElement);
const scene = new THREE.Scene();
const pmrem = new THREE.PMREMGenerator(renderer);
scene.environment = pmrem.fromScene(new RoomEnvironment(), 0.04).texture;
scene.environmentIntensity = 0.55;
const camera = new THREE.PerspectiveCamera(32, innerWidth/innerHeight, 0.01, 50);
const key = new THREE.DirectionalLight(0xfff4e6, 1.6); key.position.set(1.5, 3, 2.5); scene.add(key);
const rim = new THREE.DirectionalLight(0x9fd0ff, 1.1); rim.position.set(-2, 1.5, -2.5); scene.add(rim);
scene.add(new THREE.HemisphereLight(0xdfe9f2, 0x1a1410, 0.35));

const controls = new OrbitControls(camera, renderer.domElement);
controls.enableDamping = true; controls.dampingFactor = 0.08;
controls.minDistance = 0.12; controls.maxDistance = 7;
controls.zoomToCursor = true;

const root = new THREE.Group();
root.position.set(-0.0006, 0.0135, -0.0965);   // pies en y=0, cuerpo centrado
scene.add(root);

// suelo: disco de sombra suave + regla de estatura
(function floor(){
  const c = document.createElement('canvas'); c.width = c.height = 256;
  const g = c.getContext('2d'); const gr = g.createRadialGradient(128,128,0,128,128,128);
  gr.addColorStop(0,'rgba(0,0,0,.55)'); gr.addColorStop(.6,'rgba(0,0,0,.18)'); gr.addColorStop(1,'rgba(0,0,0,0)');
  g.fillStyle = gr; g.fillRect(0,0,256,256);
  const m = new THREE.Mesh(new THREE.PlaneGeometry(1.4,1.0), new THREE.MeshBasicMaterial({map:new THREE.CanvasTexture(c), transparent:true, depthWrite:false}));
  m.rotation.x = -Math.PI/2; m.position.y = 0.001; scene.add(m);
  const ring = new THREE.Mesh(new THREE.RingGeometry(0.62,0.623,128), new THREE.MeshBasicMaterial({color:0x6f8392, transparent:true, opacity:.35, side:THREE.DoubleSide}));
  ring.rotation.x = -Math.PI/2; ring.position.y = 0.002; scene.add(ring);
  // regla vertical 0–170 cm
  const ruler = new THREE.Group(); ruler.position.set(0.42, 0, -0.12);
  const pts = [new THREE.Vector3(0,0,0), new THREE.Vector3(0,1.7,0)];
  for (let cm=0; cm<=170; cm+=5){ const w = cm%50===0 ? 0.04 : (cm%10===0 ? 0.022 : 0.011); pts.push(new THREE.Vector3(0,cm/100,0), new THREE.Vector3(-w,cm/100,0)); }
  ruler.add(new THREE.LineSegments(new THREE.BufferGeometry().setFromPoints(pts), new THREE.LineBasicMaterial({color:0x8fa3b1, transparent:true, opacity:.55})));
  const txt = (t, y, big) => { const cv = document.createElement('canvas'); cv.width=256; cv.height=64; const x = cv.getContext('2d');
    x.font = `${big?500:400} 34px "IBM Plex Mono", monospace`; x.fillStyle = big ? '#f2c46d' : '#9fb1bd'; x.textBaseline='middle'; x.fillText(t, 6, 32);
    const s = new THREE.Sprite(new THREE.SpriteMaterial({map:new THREE.CanvasTexture(cv), transparent:true, depthWrite:false})); s.scale.set(0.16,0.04,1); s.position.set(0.09, y, 0); ruler.add(s); };
  [0,50,100,150].forEach(v => txt(v+' cm', v/100));
  txt('≈166 cm', 1.655, true);
  const top = new THREE.LineSegments(new THREE.BufferGeometry().setFromPoints([new THREE.Vector3(-0.3,1.655,0), new THREE.Vector3(0.0,1.655,0)]), new THREE.LineDashedMaterial({color:0xf2c46d, dashSize:.012, gapSize:.01, transparent:true, opacity:.6}));
  top.computeLineDistances(); ruler.add(top);
  scene.add(ruler);
  window.__ruler = ruler;
})();

// ---------------------------------------------------------------- estado
let DATA, SYS = {}, CONC, PARTS = {};  // PARTS[id] = {p, c, mesh}
const matCache = new Map();
const sysState = {};   // k -> {on, op}
const hiddenGroups = new Set();
const hiddenParts = new Set();
let isolated = null;   // Set de ids o null
let selected = null, anchorLocal = null, focusMode = false;

function glassify(mat){
  mat.userData.glass = {value: 0};
  mat.onBeforeCompile = sh => {
    sh.uniforms.uGlass = mat.userData.glass;
    sh.fragmentShader = 'uniform float uGlass;\n' + sh.fragmentShader.replace('#include <opaque_fragment>',
      `#include <opaque_fragment>
       float fres = pow(1.0 - abs(dot(normalize(normal), normalize(vViewPosition))), 2.2);
       gl_FragColor.a = mix(gl_FragColor.a, clamp(gl_FragColor.a * 0.55 + fres * 0.75 * sqrt(gl_FragColor.a), 0.0, 1.0), uGlass);
       gl_FragColor.rgb += uGlass * fres * 0.18 * vec3(0.75, 0.88, 1.0);`);
  };
}
function materialFor(sysk, col){
  const k = sysk + '|' + col;
  if (matCache.has(k)) return matCache.get(k);
  const rough = {esq:.62, teg:.55, mus:.48, car:.38, dig:.42, ner:.55, res:.5}[sysk] ?? .45;
  const m = new THREE.MeshPhysicalMaterial({color:new THREE.Color(col), roughness:rough, metalness:0,
    clearcoat: ['car','dig','uri','res','lin','end','rep'].includes(sysk) ? .35 : (sysk==='mus' ? .15 : 0), clearcoatRoughness:.4,
    sheen: sysk==='mus' ? .4 : 0, sheenColor:new THREE.Color('#ff9a8a'), sheenRoughness:.6, side:THREE.FrontSide});
  m.userData.sys = sysk; glassify(m);
  matCache.set(k, m); return m;
}
const hlMat = new THREE.MeshPhysicalMaterial({color:0xf2c46d, emissive:0xf2a13d, emissiveIntensity:.35, roughness:.35, clearcoat:.5});
// silueta visible a través de otras estructuras
const ghostMat = new THREE.MeshBasicMaterial({color:0xf2c46d, transparent:true, opacity:.22, depthTest:false, depthWrite:false});
const ghost = new THREE.Mesh(new THREE.BufferGeometry(), ghostMat); ghost.renderOrder = 999; ghost.visible = false;

function applyOpacity(){
  for (const m of matCache.values()){
    let op = sysState[m.userData.sys].op;
    if (focusMode && selected) op *= 0.12;
    m.opacity = op; const tr = op < 0.999;
    if (m.transparent !== tr){ m.transparent = tr; m.needsUpdate = true; }
    m.depthWrite = !tr; m.userData.glass.value = tr ? 1 : 0;
  }
}
function isVisible(id){
  const P = PARTS[id]; const c = CONC[P.p.c];
  if (isolated) return isolated.has(id);
  return sysState[c.s].on && !hiddenGroups.has(c.s + '|' + c.g) && !hiddenParts.has(id);
}
function applyVisibility(){
  for (const id in PARTS){ const P = PARTS[id]; if (P.mesh) P.mesh.visible = isVisible(id); }
  refreshListStates();
}

// ---------------------------------------------------------------- carga de datos
const loader = new GLTFLoader(); loader.setMeshoptDecoder(MeshoptDecoder);
const ORDER = ['teg','mus','esq','ner','car','res','dig','uri','rep','end','lin'];
const progress = {};
async function boot(){
  DATA = window.ANAT_DATA;
  CONC = DATA.concepts;
  DATA.systems.forEach(s => { SYS[s.k] = s; sysState[s.k] = {on:true, op: s.k==='teg' ? 0.28 : 1}; });
  DATA.parts.forEach(p => PARTS[p.id] = {p, mesh:null});
  const nConc = new Set(DATA.parts.map(p=>p.c)).size;
  $('#stats').textContent = `${DATA.parts.length} estructuras · ${nConc} fichas · ${DATA.systems.length} sistemas · varón adulto`;
  buildSystemsUI(); renderInfo(); applyOpacity();
  const total = Object.values(DATA.files).reduce((a,f)=>a+f.bytes,0);
  const upd = () => { const got = Object.values(progress).reduce((a,b)=>a+b,0); const pct = Math.min(100, Math.round(got/total*100));
    $('#lbar').style.width = pct+'%'; $('#lpct').textContent = pct+' %'; };
  let done = 0;
  // las mallas se publican como GLB codificado en base64 (.txt)
  // versión autónoma: las mallas vienen en models/*.js como GLB codificado en base64
  async function fetchModel(sk){
    const txt = (window.ANAT_MODELS || {})[sk]; if (!txt) throw new Error('falta models/' + sk + '.js');
    const bin = Uint8Array.from(atob(txt), c => c.charCodeAt(0));
    progress[sk] = DATA.files[sk].bytes; upd();
    return bin.buffer;
  }
  await Promise.all(ORDER.map(async sk => {
    try {
      const buf = await fetchModel(sk);
      const gltf = await loader.parseAsync(buf, '');
      gltf.scene.traverse(o => {
        if (!o.isMesh) return;
        const id = PARTS[o.name] ? o.name : (o.parent && PARTS[o.parent.name] ? o.parent.name : null);
        if (!id) return; const P = PARTS[id];
        if (!o.geometry.attributes.normal) o.geometry.computeVertexNormals();
        o.material = materialFor(sk, P.p.col);
        o.userData.id = id; P.mesh = o;
        o.visible = isVisible(id);
      });
      root.add(gltf.scene);
      progress[sk] = DATA.files[sk].bytes; upd();
      done++; $('#ltxt').textContent = `Sistema ${SYS[sk].n.toLowerCase()} listo (${done}/${ORDER.length})`;
    } catch (err) { $('#err').hidden = false; $('#err').textContent = 'No se pudo cargar el sistema ' + SYS[sk].n + '.'; console.error(err); }
  }));
  applyOpacity();
  $('#ltxt').textContent = 'Modelo completo'; setTimeout(()=>$('#loader').classList.add('done'), 700);
}

// ---------------------------------------------------------------- UI: sistemas
const EYE = '<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><path d="M2 12s3.6-7 10-7 10 7 10 7-3.6 7-10 7S2 12 2 12Z"/><circle cx="12" cy="12" r="3"/></svg>';
const EYE_OFF = '<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><path d="M3 3l18 18M10.6 5.1A10 10 0 0 1 12 5c6.4 0 10 7 10 7a17 17 0 0 1-3.2 4M6.2 6.3C3.6 8 2 12 2 12s3.6 7 10 7a9.6 9.6 0 0 0 4.3-1"/></svg>';
const CHEV = '<svg class="chev" width="10" height="10" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3"><path d="m9 6 6 6-6 6"/></svg>';
function buildSystemsUI(){
  const box = $('#systems'); box.innerHTML = '';
  for (const s of DATA.systems){
    const parts = DATA.parts.filter(p => CONC[p.c].s === s.k);
    const groups = {};
    parts.forEach(p => (groups[CONC[p.c].g] ||= []).push(p));
    const el = document.createElement('div'); el.className = 'sys'; el.dataset.sys = s.k;
    el.innerHTML = `<div class="sysrow"><span class="sw" style="background:${s.c}"></span>
      <button class="sysname" aria-expanded="false">${CHEV}${esc(s.n)}</button>
      <span class="count">${parts.length}</span>
      <button class="eye" aria-pressed="true" aria-label="Mostrar u ocultar ${esc(s.n)}">${EYE}</button></div>
      <div class="oprow"><label for="op-${s.k}">Opacidad</label><input type="range" id="op-${s.k}" min="0" max="100" value="${Math.round(sysState[s.k].op*100)}" style="--c:${s.c}"><output>${Math.round(sysState[s.k].op*100)} %</output></div>
      <div class="groups"></div>`;
    const gbox = el.querySelector('.groups');
    Object.keys(groups).sort((a,b)=>a.localeCompare(b,'es')).forEach(g => {
      const gid = s.k + '|' + g;
      const ge = document.createElement('div'); ge.className = 'grp';
      ge.innerHTML = `<div class="grow"><input type="checkbox" checked aria-label="Mostrar ${esc(g)}"><button>${esc(g)}</button><span class="count">${groups[g].length}</span></div><div class="plist"></div>`;
      ge.querySelector('input').addEventListener('change', e => { e.target.checked ? hiddenGroups.delete(gid) : hiddenGroups.add(gid); exitIsolate(); applyVisibility(); });
      ge.querySelector('button').addEventListener('click', () => {
        const pl = ge.querySelector('.plist');
        if (!pl.childElementCount){
          groups[g].sort((a,b)=> CONC[a.c].n.localeCompare(CONC[b.c].n,'es') || a.sd.localeCompare(b.sd)).forEach(p => pl.appendChild(partButton(p)));
          refreshListStates();
        }
        ge.classList.toggle('open');
      });
      gbox.appendChild(ge);
    });
    el.querySelector('.sysname').addEventListener('click', e => { el.classList.toggle('open'); e.currentTarget.setAttribute('aria-expanded', el.classList.contains('open')); });
    el.querySelector('.eye').addEventListener('click', () => { setSys(s.k, !sysState[s.k].on); markPeel(-1); });
    const r = el.querySelector('input[type=range]');
    const paint = () => r.style.setProperty('--p', r.value + '%');
    paint();
    r.addEventListener('input', () => { sysState[s.k].op = r.value/100; r.nextElementSibling.textContent = r.value + ' %'; paint(); applyOpacity(); });
    box.appendChild(el);
  }
}
function partButton(p){
  const b = document.createElement('button'); b.className = 'pitem'; b.dataset.id = p.id;
  b.innerHTML = `<span class="dot" style="background:${p.col}"></span><span>${esc(CONC[p.c].n)}</span><span class="sd">${SIDE_SHORT[p.sd]}</span>`;
  b.addEventListener('click', () => { select(p.id, null, true); showTab('right'); });
  return b;
}
function refreshListStates(){
  document.querySelectorAll('.pitem').forEach(b => { b.classList.toggle('sel', b.dataset.id === selected); b.classList.toggle('hid', !isVisible(b.dataset.id)); });
  document.querySelectorAll('.sys').forEach(el => { const on = sysState[el.dataset.sys].on; el.classList.toggle('off', !on);
    const e = el.querySelector('.eye'); e.setAttribute('aria-pressed', on); e.innerHTML = on ? EYE : EYE_OFF; });
}
function setSys(k, on){ sysState[k].on = on; exitIsolate(); applyVisibility(); }
function markPeel(n){ document.querySelectorAll('[data-peel]').forEach(b => b.setAttribute('aria-pressed', String(+b.dataset.peel === n))); }
document.querySelectorAll('[data-peel]').forEach(b => b.addEventListener('click', () => {
  const lvl = +b.dataset.peel;
  DATA.systems.forEach(s => sysState[s.k].on = s.layer >= lvl);
  if (lvl === 3) DATA.systems.forEach(s => { if (s.k === 'esq') sysState[s.k].on = false; });
  if (lvl >= 1 && selected && !isVisible(selected)) deselect();
  exitIsolate(); applyVisibility(); markPeel(lvl);
}));

// ---------------------------------------------------------------- búsqueda
$('#q').addEventListener('input', e => {
  const q = norm(e.target.value.trim()); const box = $('#results');
  if (q.length < 2){ box.hidden = true; $('#systems').hidden = false; return; }
  const words = q.split(/\s+/);
  const hits = DATA.parts.filter(p => { const h = norm(CONC[p.c].n + ' ' + p.en + ' ' + CONC[p.c].g); return words.every(w => h.includes(w)); })
    .sort((a,b) => norm(CONC[a.c].n).indexOf(words[0]) - norm(CONC[b.c].n).indexOf(words[0]) || CONC[a.c].n.length - CONC[b.c].n.length).slice(0, 40);
  box.innerHTML = hits.length ? '' : '<div class="eyebrow" style="padding:10px 8px">Sin resultados</div>';
  hits.forEach(p => box.appendChild(partButton(p)));
  box.hidden = false; $('#systems').hidden = true; refreshListStates();
});

// ---------------------------------------------------------------- ficha
function renderInfo(){
  const box = $('#info');
  if (!selected){
    box.innerHTML = `<div class="empty" style="display:flex;flex-direction:column;gap:14px">
      <div class="eyebrow">Cómo usarlo</div>
      <h2>Selecciona cualquier estructura del cuerpo</h2>
      <ul class="howto">
        <li><span>①</span><span>Arrastra para girar, rueda o pellizca para acercar y clic derecho para desplazar.</span></li>
        <li><span>②</span><span>Haz clic en un órgano, hueso o músculo para ver su nombre y su ficha.</span></li>
        <li><span>③</span><span>Usa <b>Pelar capas</b> o el ojo de cada sistema para retirar tejidos; ajusta su opacidad para ver a través.</span></li>
        <li><span>④</span><span>Atajos: <kbd>Esc</kbd> deseleccionar · <kbd>F</kbd> enfocar · <kbd>H</kbd> ocultar · <kbd>I</kbd> aislar</span></li>
      </ul>
      <div class="eyebrow" style="margin-top:6px">Sistemas incluidos</div>
      <div class="syslist">${DATA.systems.map(s => `<div><span class="sw" style="background:${s.c}"></span><span><b>${esc(s.n)}.</b> ${esc(s.d)}</span></div>`).join('')}</div>
      <details class="about"><summary>Acerca del modelo y su rigor</summary>
        <p>La geometría procede de <a href="https://lifesciencedb.jp/bp3d/" target="_blank" rel="noopener">BodyParts3D</a> (Database Center for Life Science, Japón), un atlas construido a partir de imágenes de resonancia magnética de un varón adulto y etiquetado con los identificadores de la <i>Foundational Model of Anatomy</i> (FMA). Cada malla conserva su identificador original, visible en la ficha.</p>
        <p>Para que funcione en el navegador, las mallas se han simplificado (≈26 millones → ≈3,3 millones de triángulos) sin alterar su posición ni su forma general. La nomenclatura sigue la Terminología Anatómica en español.</p>
        <p><b>Estructuras que el modelo de origen no incluye:</b></p>
        <ul><li>Médula espinal y nervios periféricos (solo el nervio y la vía ópticos).</li><li>Glándula tiroides, lengua, glándulas salivales, faringe y laringe (salvo el cartílago tiroides).</li><li>Ganglios y vasos linfáticos; la mayoría de arterias y venas de los miembros y de la cabeza.</li><li>Terceros molares, meninges y algunas circunvoluciones cerebrales.</li><li>Anatomía femenina: el modelo es de un único individuo varón, por lo que hay variación anatómica normal entre personas.</li></ul>
        <p>Licencia: los datos se distribuyen bajo <a href="https://creativecommons.org/licenses/by-sa/2.1/jp/deed.es" target="_blank" rel="noopener">CC BY-SA 2.1 Japón</a>; las mallas derivadas y las fichas de este visor se comparten bajo <a href="https://creativecommons.org/licenses/by-sa/4.0/deed.es" target="_blank" rel="noopener">CC BY-SA 4.0</a>, y el código bajo licencia MIT.</p>
        <p><b>Uso educativo, no clínico.</b> Este atlas es un material de estudio: no sirve para diagnóstico ni para decisiones médicas, y sus fichas no han sido revisadas por especialistas.</p>
      </details></div>`;
    return;
  }
  const P = PARTS[selected], c = CONC[P.p.c], s = SYS[c.s];
  box.innerHTML = `<div class="tags"><span class="tag"><span class="sw" style="background:${s.c}"></span>${esc(s.n)}</span>${P.p.sd ? `<span class="tag">${SIDE[P.p.sd]}</span>` : ''}</div>
    <h2>${esc(c.n)}</h2>
    <div class="grpname">${esc(c.g)}</div>
    <div class="actions"><button class="btn primary" data-act="focus">Enfocar</button><button class="btn" data-act="iso">${isolated ? 'Ver todo' : 'Aislar'}</button><button class="btn" data-act="hide">Ocultar</button></div>
    <p class="desc">${esc(c.d)}</p>
    ${c.f.length ? `<dl class="facts">${c.f.map(([k,v]) => `<div><dt>${esc(k)}</dt><dd>${esc(v)}</dd></div>`).join('')}</dl>` : ''}
    <label style="display:flex;gap:8px;align-items:center;font-size:12.5px;color:var(--mut);cursor:pointer"><input type="checkbox" id="focusmode" ${focusMode?'checked':''} style="accent-color:var(--acc)"> Atenuar el resto del cuerpo</label>
    <div class="src">Fuente: BodyParts3D · ${esc(selected)}<br>Término original: ${esc(P.p.en)}</div>`;
  box.querySelectorAll('[data-act]').forEach(b => b.addEventListener('click', () => ({focus:focusSel, iso:toggleIsolate, hide:hideSel})[b.dataset.act]()));
  box.querySelector('#focusmode').addEventListener('change', e => { focusMode = e.target.checked; applyOpacity(); });
}

// ---------------------------------------------------------------- selección
function select(id, hitPoint, fly){
  const P = PARTS[id]; if (!P || !P.mesh) return;
  if (selected && PARTS[selected].mesh) PARTS[selected].mesh.material = materialFor(CONC[PARTS[selected].p.c].s, PARTS[selected].p.col);
  selected = id;
  const c = CONC[P.p.c];
  // asegurar visibilidad
  if (!isVisible(id)){ if (isolated) isolated.add(id); sysState[c.s].on = true; hiddenParts.delete(id); hiddenGroups.delete(c.s+'|'+c.g); applyVisibility(); }
  P.mesh.material = hlMat;
  ghost.geometry = P.mesh.geometry; P.mesh.add(ghost); ghost.visible = true;
  if (hitPoint) anchorLocal = P.mesh.worldToLocal(hitPoint.clone());
  else { P.mesh.geometry.computeBoundingBox(); anchorLocal = P.mesh.geometry.boundingBox.getCenter(new THREE.Vector3()); }
  $('#label .ln').textContent = c.n;
  $('#label .ls').textContent = [SYS[c.s].n, SIDE[P.p.sd]].filter(Boolean).join(' · ');
  renderInfo(); refreshListStates(); applyOpacity();
  if (fly){ focusMode = true; applyOpacity(); renderInfo(); focusSel(); }
}
function deselect(){
  if (!selected) return;
  const P = PARTS[selected]; if (P.mesh) P.mesh.material = materialFor(CONC[P.p.c].s, P.p.col);
  ghost.removeFromParent(); ghost.visible = false; focusMode = false;
  selected = null; anchorLocal = null; renderInfo(); refreshListStates(); applyOpacity();
}
function focusSel(){
  if (!selected) return;
  const box = new THREE.Box3().setFromObject(PARTS[selected].mesh);
  const ctr = box.getCenter(new THREE.Vector3()); const size = box.getSize(new THREE.Vector3()).length();
  const dir = camera.position.clone().sub(controls.target).normalize();
  const dist = Math.max(0.5, size * 2.8);
  flyTo(ctr.clone().add(dir.multiplyScalar(dist)), ctr);
}
function hideSel(){ if (!selected) return; const id = selected; if (isolated) isolated.delete(id); else hiddenParts.add(id); deselect(); applyVisibility(); }
function toggleIsolate(){
  if (isolated){ exitIsolate(); applyVisibility(); renderInfo(); return; }
  if (!selected) return;
  const c = PARTS[selected].p.c;
  isolated = new Set(DATA.parts.filter(p => p.c === c).map(p => p.id));   // incluye ambos lados
  applyVisibility(); renderInfo(); focusSel();
}
function exitIsolate(){ isolated = null; }

// ---------------------------------------------------------------- cámara
let fly = null;
function flyTo(pos, target, ms = 750){
  fly = {p0:camera.position.clone(), t0:controls.target.clone(), p1:pos, t1:target, s:performance.now(), ms: matchMedia('(prefers-reduced-motion: reduce)').matches ? 1 : ms};
}
const VIEWS = {front:[0,0.95,3.3], back:[0,0.95,-3.3], right:[-3.3,0.95,0], left:[3.3,0.95,0], top:[0,4.2,0.35]};
function setView(v){ const t = new THREE.Vector3(0, v==='top'?0.9:0.88, 0); flyTo(new THREE.Vector3(...VIEWS[v]), t); }
document.querySelectorAll('[data-view]').forEach(b => b.addEventListener('click', () => setView(b.dataset.view)));
camera.position.set(0.9, 1.15, 3.1); controls.target.set(0, 0.9, 0); controls.update();
$('#spin').addEventListener('click', e => { controls.autoRotate = !controls.autoRotate; controls.autoRotateSpeed = 1.2; e.currentTarget.setAttribute('aria-pressed', controls.autoRotate); });
$('#reset').addEventListener('click', () => {
  hiddenGroups.clear(); hiddenParts.clear(); isolated = null; focusMode = false;
  DATA.systems.forEach(s => { sysState[s.k] = {on:true, op: s.k==='teg' ? .28 : 1}; });
  document.querySelectorAll('.sys').forEach(el => { const r = el.querySelector('input[type=range]'); r.value = Math.round(sysState[el.dataset.sys].op*100); r.nextElementSibling.textContent = r.value + ' %'; r.style.setProperty('--p', r.value+'%'); });
  document.querySelectorAll('.grow input').forEach(i => i.checked = true);
  markPeel(0); deselect(); applyVisibility(); applyOpacity(); setView('front');
});

// ---------------------------------------------------------------- picking
const ray = new THREE.Raycaster(); const ndc = new THREE.Vector2();
function pick(x, y){
  const r = renderer.domElement.getBoundingClientRect();
  ndc.set((x - r.left)/r.width*2-1, -(y - r.top)/r.height*2+1);
  ray.setFromCamera(ndc, camera);
  const objs = []; for (const id in PARTS){ const m = PARTS[id].mesh; if (m && m.visible) objs.push(m); }
  const hits = ray.intersectObjects(objs, false);
  // ignorar capas muy transparentes (< 15 %) para poder «atravesarlas»
  // capas semitransparentes (p. ej. la piel en modo fantasma) solo se seleccionan si no hay nada opaco detrás
  const ok = (h, min) => h.object.material === hlMat || h.object.material.opacity >= min;
  return hits.find(h => ok(h, 0.6)) || hits.find(h => ok(h, 0.15)) || null;
}
let down = null, hoverPending = false, lastMove = null;
renderer.domElement.addEventListener('pointerdown', e => { down = {x:e.clientX, y:e.clientY}; });
renderer.domElement.addEventListener('pointerup', e => {
  if (!down) return; const d = Math.hypot(e.clientX-down.x, e.clientY-down.y); down = null;
  if (d > 5) return;
  const h = pick(e.clientX, e.clientY);
  if (h) { select(h.object.userData.id, h.point, false); if (innerWidth <= 900) showTab('right'); }
  else deselect();
});
renderer.domElement.addEventListener('pointermove', e => { if (e.pointerType !== 'mouse') return; lastMove = e; if (!hoverPending){ hoverPending = true; requestAnimationFrame(doHover); } });
renderer.domElement.addEventListener('pointerleave', () => { $('#tip').style.transform = 'translate(-9999px,0)'; });
function doHover(){
  hoverPending = false; const e = lastMove; const tip = $('#tip');
  if (!e || e.buttons || !DATA) { tip.style.transform = 'translate(-9999px,0)'; return; }
  const h = pick(e.clientX, e.clientY);
  if (!h){ tip.style.transform = 'translate(-9999px,0)'; renderer.domElement.style.cursor = ''; return; }
  const P = PARTS[h.object.userData.id];
  tip.innerHTML = esc(CONC[P.p.c].n) + (P.p.sd ? `<i>${SIDE_SHORT[P.p.sd]}</i>` : '');
  tip.style.transform = `translate(${e.clientX+14}px, ${e.clientY+14}px)`;
  renderer.domElement.style.cursor = 'pointer';
}
addEventListener('keydown', e => {
  if (e.target.matches('input')) return;
  if (e.key === 'Escape') deselect();
  else if (e.key === 'f' || e.key === 'F') focusSel();
  else if (e.key === 'h' || e.key === 'H') hideSel();
  else if (e.key === 'i' || e.key === 'I') toggleIsolate();
});

// ---------------------------------------------------------------- pestañas móvil
function showTab(t){
  if (innerWidth > 900) return;
  ['left','right'].forEach(k => $('#'+k).classList.toggle('show', k === t));
  document.querySelectorAll('[data-tab]').forEach(b => b.setAttribute('aria-pressed', String(b.dataset.tab === t)));
  fitView();
}
// en móvil, encaja el cuerpo en la zona libre entre la cabecera y el panel inferior
function fitView(){
  const W = innerWidth, H = innerHeight;
  if (W > 900){ camera.clearViewOffset(); camera.zoom = 1; camera.updateProjectionMatrix(); return; }
  const topH = document.querySelector('.top').getBoundingClientRect().bottom + 6;
  const pan = document.querySelector('.panel.show');
  const botH = pan ? H - pan.getBoundingClientRect().top + 8 : 64;
  const free = Math.max(120, H - topH - botH);
  camera.zoom = Math.min(1, free / H * 1.08);
  camera.setViewOffset(W, H, 0, (botH - topH) / 2, W, H);
  camera.updateProjectionMatrix();
}
document.querySelectorAll('[data-tab]').forEach(b => b.addEventListener('click', () => showTab(b.dataset.tab)));
function layout(){
  if (innerWidth > 900){ $('#left').classList.add('show'); $('#right').classList.add('show'); }
  else if (!document.querySelector('[data-tab][aria-pressed="true"]')) showTab('left');
  else showTab(document.querySelector('[data-tab][aria-pressed="true"]').dataset.tab);
}
layout(); fitView();

// ---------------------------------------------------------------- bucle
addEventListener('resize', () => { renderer.setSize(innerWidth, innerHeight); camera.aspect = innerWidth/innerHeight; camera.updateProjectionMatrix(); layout(); fitView(); });
const v3 = new THREE.Vector3(), T0 = performance.now();
function tick(){
  requestAnimationFrame(tick);
  const t = (performance.now() - T0) / 1000;
  if (fly){ let k = Math.min(1, (performance.now()-fly.s)/fly.ms); k = k<.5 ? 4*k*k*k : 1-Math.pow(-2*k+2,3)/2;
    camera.position.lerpVectors(fly.p0, fly.p1, k); controls.target.lerpVectors(fly.t0, fly.t1, k); if (k >= 1) fly = null; }
  controls.update();
  hlMat.emissiveIntensity = 0.28 + 0.14 * Math.sin(t * 3.2); ghostMat.opacity = 0.16 + 0.08 * Math.sin(t * 3.2);
  renderer.render(scene, camera);
  // etiqueta
  const lab = $('#label'), line = $('#lline'), dot = $('#ldot');
  if (selected && anchorLocal && PARTS[selected].mesh.visible){
    v3.copy(anchorLocal); PARTS[selected].mesh.localToWorld(v3); v3.project(camera);
    const x = (v3.x*.5+.5)*innerWidth, y = (-v3.y*.5+.5)*innerHeight;
    if (v3.z < 1){
      const w = lab.offsetWidth, hgt = lab.offsetHeight;
      const leftSide = x > innerWidth*0.5;
      let lx = leftSide ? x - 70 - w : x + 70, ly = y - 70 - hgt/2;
      const minX = innerWidth > 900 ? 362 : 12, maxX = innerWidth > 900 ? innerWidth - 392 : innerWidth - 12;
      lx = Math.max(minX, Math.min(maxX - w, lx)); ly = Math.max(90, Math.min(innerHeight - hgt - 70, ly));
      lab.style.transform = `translate(${lx}px, ${ly}px)`;
      const ax = leftSide ? lx + w : lx, ay = ly + hgt/2;
      line.setAttribute('x1', x); line.setAttribute('y1', y); line.setAttribute('x2', ax); line.setAttribute('y2', ay);
      dot.setAttribute('cx', x); dot.setAttribute('cy', y);
    }
  } else { lab.style.transform = 'translate(-9999px,0)'; line.setAttribute('x1',-99); line.setAttribute('x2',-99); line.setAttribute('y1',-99); line.setAttribute('y2',-99); dot.setAttribute('cx',-99); }
}
tick();
boot().catch(err => { $('#err').hidden = false; $('#err').textContent = 'Error al cargar los datos: ' + err.message; console.error(err); });
