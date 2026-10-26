# -*- coding: utf-8 -*-
# Parte C: sistema nervioso, sentidos, cardiovascular, respiratorio, digestivo, urinario, reproductor, endocrino, linfático.
from anat_a import C, add
FULL = {}  # claves por nombre inglés completo (estructuras impares cuyo nombre incluye right/left)
def addf(full, n, s, g, d, f=None):
    FULL[full] = {"n": n, "s": s, "g": g, "d": d, "f": f or []}

# ============================ ENCÉFALO
G = "Encéfalo: corteza cerebral"
GYR = "Circunvolución de la corteza cerebral (sustancia gris). "
add("superior frontal gyrus", "Circunvolución frontal superior", "ner", G, GYR+"Contiene el área motora suplementaria y participa en funciones ejecutivas, autoconciencia y memoria de trabajo.", [["Lóbulo", "Frontal"]])
add("middle frontal gyrus", "Circunvolución frontal media", "ner", G, GYR+"Incluye el campo ocular frontal (movimientos oculares voluntarios) y parte de la corteza prefrontal dorsolateral (planificación, memoria de trabajo).", [["Lóbulo", "Frontal"]])
add("orbital gyri straight gyrus", "Circunvoluciones orbitarias y recta", "ner", G, GYR+"Superficie inferior del lóbulo frontal, sobre el techo de las órbitas. Corteza orbitofrontal: toma de decisiones, valoración de recompensas y control de la conducta social. El surco olfatorio separa la circunvolución recta de las orbitarias.", [["Lóbulo", "Frontal"]])
add("precentral gyrus", "Circunvolución precentral", "ner", G, GYR+"Corteza motora primaria (área 4 de Brodmann): origina las órdenes motoras voluntarias del lado opuesto del cuerpo, con una representación somatotópica (homúnculo motor).", [["Lóbulo", "Frontal"], ["Área", "M1 · Brodmann 4"]])
add("postcentral gyrus", "Circunvolución poscentral", "ner", G, GYR+"Corteza somatosensorial primaria (áreas 3, 1 y 2): recibe tacto, dolor, temperatura y propiocepción del lado opuesto del cuerpo (homúnculo sensitivo).", [["Lóbulo", "Parietal"], ["Área", "S1 · Brodmann 3-1-2"]])
add("superior parietal lobule precuneus", "Lobulillo parietal superior y precúneo", "ner", G, GYR+"Integra información visual y somatosensorial para orientar el cuerpo en el espacio y guiar los movimientos. El precúneo, en la cara medial, participa en la memoria episódica y la autoconciencia.", [["Lóbulo", "Parietal"]])
add("supramarginal gyrus", "Circunvolución supramarginal", "ner", G, GYR+"Rodea el extremo del surco lateral. Interviene en la percepción espacial, la praxis y, en el hemisferio dominante, en el procesamiento fonológico del lenguaje.", [["Lóbulo", "Parietal (inferior)"], ["Área", "Brodmann 40"]])
add("angular gyrus", "Circunvolución angular", "ner", G, GYR+"Rodea el extremo del surco temporal superior. En el hemisferio dominante es clave para la lectura, la escritura y el cálculo.", [["Lóbulo", "Parietal (inferior)"], ["Área", "Brodmann 39"]])
add("anterior part of superior temporal gyrus", "Circunvolución temporal superior (parte anterior)", "ner", G, GYR+"Su cara superior contiene la corteza auditiva primaria (circunvoluciones transversas de Heschl).", [["Lóbulo", "Temporal"]])
add("posterior part of superior temporal gyrus", "Circunvolución temporal superior (parte posterior)", "ner", G, GYR+"En el hemisferio dominante contiene el área de Wernicke, esencial para la comprensión del lenguaje.", [["Lóbulo", "Temporal"], ["Área", "Wernicke · Brodmann 22"]])
add("middle temporal gyrus", "Circunvolución temporal media", "ner", G, GYR+"Participa en el reconocimiento de palabras y significados, y en la percepción del movimiento visual (área MT/V5 en su parte posterior).", [["Lóbulo", "Temporal"]])
add("inferior temporal gyrus", "Circunvolución temporal inferior", "ner", G, GYR+"Forma parte de la vía visual ventral («qué»): reconocimiento de objetos y formas.", [["Lóbulo", "Temporal"]])
add("fusiform gyrus", "Circunvolución fusiforme (occipitotemporal lateral)", "ner", G, GYR+"En la cara inferior del hemisferio. Contiene el área fusiforme de las caras y el área de la forma visual de las palabras.", [["Lóbulo", "Temporal / occipital"]])
add("parahippocampal gyrus", "Circunvolución parahipocampal", "ner", G, GYR+"Forma parte del sistema límbico. Su parte anterior (corteza entorrinal y uncus) es la principal vía de entrada al hipocampo; esencial para la memoria y la orientación espacial.", [["Lóbulo", "Límbico / temporal"]])
add("cingulate gyrus", "Circunvolución del cíngulo", "ner", G, GYR+"Rodea el cuerpo calloso en la cara medial del hemisferio. Parte del sistema límbico: emociones, motivación, atención, dolor y control de errores.", [["Lóbulo", "Límbico"]])
add("accessory short gyrus", "Circunvolución corta accesoria de la ínsula", "ner", G, GYR+"Pequeña circunvolución de la parte anterior de la ínsula.", [["Lóbulo", "Insular"]])
add("insula", "Ínsula", "ner", G, "Lóbulo de la corteza cerebral oculto en el fondo del surco lateral, cubierto por los opérculos frontal, parietal y temporal. Procesa el gusto, la interocepción (sensaciones viscerales), el dolor y la conciencia emocional.", [["Lóbulo", "Insular"]])
add("occipital lobe", "Lóbulo occipital", "ner", G, "Lóbulo posterior del hemisferio cerebral. Contiene la corteza visual primaria (V1, área 17 de Brodmann) alrededor del surco calcarino y las áreas visuales de asociación.", [["Función", "Visión"], ["Área", "V1 · Brodmann 17"]])
add("white matter structure of cerebral hemisphere", "Sustancia blanca de los hemisferios cerebrales", "ner", "Encéfalo: sustancia blanca",
    "Masa de axones mielinizados situada bajo la corteza. Contiene fibras de asociación (unen áreas del mismo hemisferio), comisurales (unen ambos hemisferios) y de proyección (unen la corteza con estructuras inferiores).")
G = "Encéfalo: sustancia blanca"
add("corpus callosum", "Cuerpo calloso", "ner", G, "La mayor comisura del encéfalo: unos 200 millones de axones que conectan los dos hemisferios cerebrales y permiten compartir información entre ellos.", [["Partes", "Pico, rodilla, tronco y esplenio"]])
add("anterior commissure", "Comisura anterior", "ner", G, "Haz de fibras que cruza la línea media delante del fórnix; conecta los lóbulos temporales y estructuras olfatorias de ambos hemisferios.")
add("posterior commissure", "Comisura posterior", "ner", G, "Haz de fibras que cruza la línea media por encima del acueducto cerebral; participa en el reflejo pupilar consensual a la luz.")
add("anterior limb of internal capsule", "Cápsula interna — brazo anterior", "ner", G, "Lámina de sustancia blanca entre el núcleo caudado y el núcleo lenticular. Contiene fibras entre el tálamo y la corteza frontal y fibras frontopontinas.")
add("fornix of forebrain", "Fórnix (trígono cerebral)", "ner", G, "Haz arqueado de fibras que es la principal vía de salida del hipocampo; termina sobre todo en los cuerpos mamilares. Participa en los circuitos de la memoria (circuito de Papez).")
add("commissure of fornix of forebrain", "Comisura del fórnix", "ner", G, "Fibras que cruzan entre los pilares posteriores de ambos fórnix, conectando los dos hipocampos.")
add("stria terminalis", "Estría terminal", "ner", G, "Haz de fibras que discurre junto al núcleo caudado y conecta la amígdala con el hipotálamo y el área septal.")
add("stria medullaris of thalamus", "Estría medular del tálamo", "ner", G, "Haz de fibras en la cara medial del tálamo que lleva información del área septal a los núcleos de la habénula.")
add("lamina terminalis", "Lámina terminal", "ner", G, "Delgada lámina que forma la pared anterior del tercer ventrículo. Contiene el órgano vasculoso, sensible a la osmolaridad de la sangre (sed).")
add("septum pellucidum", "Septo pelúcido", "ner", G, "Doble lámina delgada que separa las astas anteriores de los ventrículos laterales, entre el cuerpo calloso y el fórnix.")
G = "Encéfalo: núcleos profundos"
add("caudate nucleus", "Núcleo caudado", "ner", G, "Núcleo de sustancia gris en forma de C que sigue la pared del ventrículo lateral. Con el putamen forma el estriado: planificación del movimiento, aprendizaje y motivación.", [["Grupo", "Ganglios basales"]])
add("putamen", "Putamen", "ner", G, "Parte lateral del núcleo lenticular. Con el caudado forma el estriado, que recibe la información de la corteza y regula el movimiento. Afectado en la enfermedad de Parkinson por la pérdida de dopamina.", [["Grupo", "Ganglios basales"]])
add("globus pallidus", "Globo pálido", "ner", G, "Parte medial del núcleo lenticular. Es la principal salida de los ganglios basales hacia el tálamo; su función es inhibidora.", [["Grupo", "Ganglios basales"]])
add("thalamus", "Tálamo", "ner", G, "Masa ovoide de sustancia gris a cada lado del tercer ventrículo. Es la gran estación de relevo: casi toda la información sensitiva (excepto el olfato) pasa por él antes de llegar a la corteza. También regula la vigilia y la atención.", [["Grupo", "Diencéfalo"]])
add("hypothalamus, nsn", "Hipotálamo", "ner", G, "Región del diencéfalo bajo el tálamo. Controla el sistema nervioso autónomo y la hipófisis, y regula la temperatura, el hambre, la sed, el sueño y los ritmos circadianos.", [["Grupo", "Diencéfalo"], ["Peso", "≈4 g"]])
add("tuber cinereum", "Túber cinereum", "ner", G, "Eminencia de sustancia gris en la base del hipotálamo, entre el quiasma óptico y los cuerpos mamilares; de ella parte el tallo de la hipófisis.", [["Grupo", "Diencéfalo"]])
add("mammillary body", "Cuerpo mamilar", "ner", G, "Par de pequeñas eminencias redondeadas en la base del hipotálamo. Reciben el fórnix y forman parte del circuito de la memoria; se lesionan en el síndrome de Wernicke-Korsakoff.", [["Grupo", "Diencéfalo"]])
add("habenula", "Habénula", "ner", G, "Pequeño núcleo del epitálamo, junto a la glándula pineal. Participa en la respuesta a la recompensa negativa y la aversión.", [["Grupo", "Epitálamo"]])
add("lateral geniculate body", "Cuerpo geniculado lateral", "ner", G, "Núcleo del tálamo que recibe el tracto óptico y envía la radiación óptica a la corteza visual. Es el relevo de la vía visual.", [["Grupo", "Metatálamo"]])
add("medial geniculate body", "Cuerpo geniculado medial", "ner", G, "Núcleo del tálamo relevo de la vía auditiva: recibe fibras del colículo inferior y proyecta a la corteza auditiva.", [["Grupo", "Metatálamo"]])
add("hippocampus", "Hipocampo", "ner", G, "Estructura curvada del lóbulo temporal medial, en el suelo del asta temporal del ventrículo lateral. Esencial para formar nuevos recuerdos declarativos y para la memoria espacial; de las primeras regiones afectadas en la enfermedad de Alzheimer.", [["Grupo", "Sistema límbico"]])
add("amygdala", "Amígdala (cuerpo amigdalino)", "ner", G, "Conjunto de núcleos en forma de almendra en la parte anterior del lóbulo temporal. Procesa las emociones, en especial el miedo, y asigna valor emocional a los recuerdos.", [["Grupo", "Sistema límbico"]])
G = "Encéfalo: tronco del encéfalo y cerebelo"
add("midbrain, nsn", "Mesencéfalo", "ner", G, "Porción superior del tronco del encéfalo. Contiene la sustancia negra, el núcleo rojo y los núcleos de los nervios III y IV; interviene en los movimientos oculares y el control motor.", [["Nervios craneales", "III (oculomotor) y IV (troclear)"]])
add("peduncle of midbrain", "Pedúnculo cerebral", "ner", G, "Columna anterior del mesencéfalo formada por la base del pedúnculo, que contiene las fibras corticoespinales y corticonucleares descendentes.")
add("interpeduncular fossa", "Fosa interpeduncular", "ner", G, "Depresión entre los dos pedúnculos cerebrales, en la cara anterior del mesencéfalo, por donde emerge el nervio oculomotor (III).")
add("superior colliculus", "Colículo superior", "ner", G, "Eminencia del techo del mesencéfalo que coordina los movimientos de los ojos y la cabeza hacia estímulos visuales (reflejos visuales).", [["Vía", "Visual"]])
add("inferior colliculus", "Colículo inferior", "ner", G, "Eminencia del techo del mesencéfalo que es un relevo obligado de la vía auditiva y participa en la localización de los sonidos.", [["Vía", "Auditiva"]])
add("brachium of superior colliculus", "Brazo del colículo superior", "ner", G, "Haz de fibras que une el tracto óptico y el cuerpo geniculado lateral con el colículo superior.")
add("brachium of inferior colliculus", "Brazo del colículo inferior", "ner", G, "Haz de fibras que une el colículo inferior con el cuerpo geniculado medial (vía auditiva).")
add("pons", "Puente (protuberancia)", "ner", G, "Porción media del tronco del encéfalo. Conecta la corteza con el cerebelo y contiene centros respiratorios y los núcleos de los nervios V, VI, VII y VIII.", [["Nervios craneales", "V, VI, VII y VIII"]])
add("medulla oblongata", "Bulbo raquídeo", "ner", G, "Porción inferior del tronco del encéfalo, que se continúa con la médula espinal en el agujero magno. Alberga centros vitales cardiovasculares y respiratorios y los núcleos de los nervios IX a XII; en él se decusan las pirámides.", [["Nervios craneales", "IX, X, XI y XII"]])
add("cerebellum", "Cerebelo", "ner", G, "Órgano situado en la fosa craneal posterior, detrás del tronco del encéfalo. Coordina el movimiento, el equilibrio y el tono muscular, y participa en el aprendizaje motor. Contiene más neuronas que el resto del encéfalo.", [["Peso", "≈150 g"], ["Partes", "Vermis y dos hemisferios"]])
G = "Encéfalo: sistema ventricular"
add("lateral ventricle", "Ventrículo lateral", "ner", G, "Cavidad en forma de C dentro de cada hemisferio, llena de líquido cefalorraquídeo. Se comunica con el tercer ventrículo por el agujero interventricular.", [["Partes", "Asta frontal, cuerpo, atrio, asta occipital y asta temporal"]])
add("third ventricle", "Tercer ventrículo", "ner", G, "Cavidad estrecha y medial entre los dos tálamos, llena de líquido cefalorraquídeo. Comunica con los laterales y, por el acueducto, con el cuarto ventrículo.")
add("cerebral aqueduct", "Acueducto del mesencéfalo (de Silvio)", "ner", G, "Conducto estrecho del mesencéfalo que une el tercer y el cuarto ventrículo. Su obstrucción es una causa frecuente de hidrocefalia.")
add("fourth ventricle", "Cuarto ventrículo", "ner", G, "Cavidad romboidal entre el tronco del encéfalo y el cerebelo. Sus aberturas (media y laterales) vierten el líquido cefalorraquídeo al espacio subaracnoideo.")
add("interventricular foramen", "Agujero interventricular (de Monro)", "ner", G, "Orificio que comunica cada ventrículo lateral con el tercer ventrículo.")
add("central canal of spinal cord", "Conducto central de la médula espinal", "ner", G, "Conducto estrecho, continuación del cuarto ventrículo, que recorre el centro de la médula espinal. (En este modelo la médula espinal en sí no está representada).")
add("choroid plexus of cerebral hemisphere", "Plexo coroideo del ventrículo lateral", "ner", G, "Red de capilares recubierta de epitelio ependimario que produce el líquido cefalorraquídeo (≈500 ml/día).")
G = "Vía óptica"
add("optic nerve", "Nervio óptico (II)", "ner", G, "Segundo par craneal. Formado por ≈1,2 millones de axones de las células ganglionares de la retina; lleva la información visual desde el ojo hasta el quiasma óptico.", [["Tipo", "Nervio craneal sensorial"]])
add("optic chiasm", "Quiasma óptico", "ner", G, "Estructura en forma de X donde se cruzan las fibras de las mitades nasales de ambas retinas. Está justo encima de la hipófisis, por lo que los tumores hipofisarios pueden alterar el campo visual (hemianopsia bitemporal).")
add("optic tract", "Tracto óptico", "ner", G, "Continuación de la vía óptica desde el quiasma hasta el cuerpo geniculado lateral. Cada tracto lleva la información del hemicampo visual opuesto.")
G = "Órganos de los sentidos"
add("eyeball", "Globos oculares", "ner", G, "Órgano de la visión, esférico, de ≈24 mm de diámetro. Tiene tres capas: fibrosa (esclera y córnea), vascular (coroides, cuerpo ciliar e iris) e interna (retina). El cristalino y la córnea enfocan la luz en la retina.", [["Diámetro", "≈24 mm"], ["Capas", "Fibrosa · vascular (úvea) · retina"]])
add("ear", "Orejas (pabellones auriculares)", "ner", G, "Parte visible del oído externo, formada por cartílago elástico cubierto de piel (salvo el lóbulo). Capta y dirige las ondas sonoras hacia el conducto auditivo externo.", [["Tejido", "Cartílago elástico"]])

# ============================ ENDOCRINO
add("pituitary gland", "Hipófisis", "end", "Glándulas endocrinas", "Glándula de ≈0,5 g alojada en la silla turca del esfenoides y unida al hipotálamo por el tallo hipofisario. Regula a otras glándulas: la adenohipófisis secreta GH, TSH, ACTH, FSH, LH y prolactina; la neurohipófisis libera oxitocina y ADH.", [["Peso", "≈0,5 g"], ["Lóbulos", "Adenohipófisis y neurohipófisis"]])
add("pineal body", "Glándula pineal (epífisis)", "end", "Glándulas endocrinas", "Pequeña glándula del epitálamo, en forma de piña, situada tras el tercer ventrículo. Secreta melatonina durante la oscuridad y regula los ritmos circadianos.", [["Hormona", "Melatonina"]])
add("adrenal gland", "Glándula suprarrenal", "end", "Glándulas endocrinas", "Glándula situada sobre el polo superior de cada riñón. La corteza produce cortisol, aldosterona y andrógenos; la médula, adrenalina y noradrenalina.", [["Peso", "≈4–5 g"], ["Partes", "Corteza (glomerular, fascicular, reticular) y médula"]])

# ============================ LINFÁTICO
add("spleen", "Bazo", "lin", "Órganos linfoides", "Órgano linfoide situado en el hipocondrio izquierdo, bajo las costillas 9–11. Su pulpa roja filtra la sangre y elimina hematíes envejecidos; su pulpa blanca genera respuestas inmunitarias frente a patógenos de la sangre.", [["Peso", "≈150 g"], ["Localización", "Hipocondrio izquierdo"]])
add("lobe of thymus", "Lóbulo del timo", "lin", "Órganos linfoides", "Órgano linfoide primario del mediastino anterior, formado por dos lóbulos. En él maduran los linfocitos T. Es grande en la infancia y se sustituye progresivamente por grasa en el adulto (involución).", [["Función", "Maduración de linfocitos T"]])

# ============================ CARDIOVASCULAR: corazón
G = "Corazón"
add("wall of heart", "Corazón (pared)", "car", G, "Órgano muscular hueco del tamaño de un puño, situado en el mediastino medio. Tiene cuatro cavidades (dos aurículas y dos ventrículos). Su pared consta de endocardio, miocardio y epicardio. Late unas 100 000 veces al día.",
    [["Peso", "≈300 g"], ["Capas", "Endocardio · miocardio · epicardio"], ["Gasto cardíaco", "≈5 L/min en reposo"]])
add("tricuspid valve", "Válvula tricúspide", "car", G, "Válvula auriculoventricular derecha, con tres valvas. Impide el reflujo de sangre del ventrículo derecho a la aurícula derecha durante la sístole.", [["Valvas", "Anterior, posterior y septal"]])
add("mitral valve", "Válvula mitral (bicúspide)", "car", G, "Válvula auriculoventricular izquierda, con dos valvas. Impide el reflujo de sangre del ventrículo izquierdo a la aurícula izquierda durante la sístole.", [["Valvas", "Anterior y posterior"]])
add("pulmonary valve", "Válvula pulmonar", "car", G, "Válvula semilunar de tres valvas situada entre el ventrículo derecho y el tronco pulmonar. Impide el reflujo hacia el ventrículo durante la diástole.")
for k,n in [("anterior papillary muscle of ventricle","Músculo papilar anterior del ventrículo derecho"),("posterior papillary muscle of ventricle","Músculo papilar posterior"),("septal papillary muscle of ventricle","Músculo papilar septal del ventrículo derecho"),("papillary muscle of ventricle, nsn","Músculo papilar del ventrículo izquierdo")]:
    add(k, n, "car", G, "Proyección cónica del miocardio ventricular unida a las valvas por las cuerdas tendinosas. Al contraerse en la sístole impide que las valvas auriculoventriculares se evaginen hacia la aurícula.")
addf("posterior papillary muscle of left ventricle", "Músculo papilar posterior del ventrículo izquierdo", "car", G, "Proyección del miocardio ventricular izquierdo unida por cuerdas tendinosas a las valvas de la mitral. Impide su prolapso durante la sístole.")
addf("posterior papillary muscle of right ventricle", "Músculo papilar posterior del ventrículo derecho", "car", G, "Proyección del miocardio ventricular derecho unida por cuerdas tendinosas a la válvula tricúspide. Impide su prolapso durante la sístole.")
G = "Corazón: arterias coronarias"
CORO = " Las arterias coronarias irrigan el propio miocardio; su obstrucción produce isquemia e infarto."
addf("stem of left coronary artery", "Tronco de la arteria coronaria izquierda", "car", G, "Nace del seno aórtico izquierdo y, tras un corto trayecto (≈1 cm), se divide en la rama interventricular anterior y la circunfleja."+CORO)
addf("anterior interventricular branch of left coronary artery, nsn", "Rama interventricular anterior (descendente anterior)", "car", G, "Rama de la coronaria izquierda que desciende por el surco interventricular anterior. Irriga la cara anterior de ambos ventrículos y los 2/3 anteriores del tabique."+CORO)
addf("circumflex branch of left coronary artery", "Rama circunfleja de la coronaria izquierda", "car", G, "Recorre el surco coronario izquierdo hacia la cara posterior del corazón e irriga la aurícula y la pared lateral del ventrículo izquierdo."+CORO)
addf("trunk of right coronary artery", "Arteria coronaria derecha", "car", G, "Nace del seno aórtico derecho y recorre el surco coronario derecho. Irriga la aurícula y el ventrículo derechos y, en la mayoría de las personas, los nodos sinusal y auriculoventricular."+CORO)
addf("marginal branch of right coronary artery", "Rama marginal derecha", "car", G, "Rama de la coronaria derecha que desciende por el borde derecho (agudo) del corazón e irriga el ventrículo derecho."+CORO)
addf("posterior interventricular branch of right coronary artery, nsn", "Rama interventricular posterior (descendente posterior)", "car", G, "Desciende por el surco interventricular posterior e irriga el tercio posterior del tabique y la cara inferior de los ventrículos. Nace de la coronaria derecha en ≈80 % de las personas (dominancia derecha)."+CORO)
addf("right posterolateral branch of right coronary artery", "Rama posterolateral derecha", "car", G, "Rama terminal de la coronaria derecha que irriga la cara posterolateral del ventrículo izquierdo."+CORO)
addf("set of interventricular septal branches of right coronary artery", "Ramas septales de la coronaria derecha", "car", G, "Pequeñas ramas que penetran en el tercio posterior del tabique interventricular."+CORO)
addf("set of interventricular septal branches of left coronary artery", "Ramas septales de la coronaria izquierda", "car", G, "Ramas de la interventricular anterior que penetran en los 2/3 anteriores del tabique interventricular, donde discurre el sistema de conducción."+CORO)
G = "Corazón: venas cardíacas"
add("coronary sinus", "Seno coronario", "car", G, "Vena ancha situada en el surco coronario posterior que recoge la mayor parte de la sangre venosa del corazón y desemboca en la aurícula derecha.")
add("great cardiac vein", "Vena cardíaca magna", "car", G, "Asciende por el surco interventricular anterior junto a la rama interventricular anterior y desemboca en el seno coronario.")
add("middle cardiac vein", "Vena cardíaca media", "car", G, "Discurre por el surco interventricular posterior y desemboca en el seno coronario.")
add("set of anterior cardiac veins", "Venas cardíacas anteriores", "car", G, "Pequeñas venas de la cara anterior del ventrículo derecho que desembocan directamente en la aurícula derecha.")
addf("set of posterior veins of left ventricle", "Venas posteriores del ventrículo izquierdo", "car", G, "Drenan la cara diafragmática del ventrículo izquierdo en el seno coronario.")
G = "Grandes arterias"
add("ascending aorta", "Aorta ascendente", "car", G, "Primer tramo de la aorta, desde la válvula aórtica hasta el arco (≈5 cm). De su raíz nacen las arterias coronarias.", [["Diámetro", "≈3 cm"]])
add("arch of aorta", "Arco (cayado) de la aorta", "car", G, "Porción curva de la aorta sobre el bronquio principal izquierdo. De él nacen el tronco braquiocefálico, la carótida común izquierda y la subclavia izquierda.")
add("descending aorta", "Aorta descendente", "car", G, "Continúa el arco aórtico: la porción torácica desciende junto a la columna, atraviesa el diafragma (T12) y como aorta abdominal se bifurca en las ilíacas comunes a nivel de L4.")
add("brachiocephalic artery, nsn", "Tronco braquiocefálico", "car", G, "Primera y mayor rama del arco aórtico. Se divide tras la articulación esternoclavicular derecha en la carótida común y la subclavia derechas.")
add("common carotid artery", "Arteria carótida común", "car", G, "Asciende por el cuello y a la altura del borde superior del cartílago tiroides (C4) se divide en carótida externa (cara y cuello) e interna (encéfalo y ojo). En su bifurcación está el seno carotídeo, sensor de presión arterial.")
add("subclavian artery", "Arteria subclavia", "car", G, "Arteria principal del miembro superior. Pasa entre los escalenos anterior y medio sobre la primera costilla y se continúa como arteria axilar. Da la arteria vertebral, que irriga el encéfalo posterior.")
add("celiac artery", "Tronco celíaco", "car", G+" (abdominales)", "Primera rama visceral de la aorta abdominal (T12). Se divide en las arterias gástrica izquierda, esplénica y hepática común: irriga estómago, hígado, bazo, páncreas y duodeno.")
addf("left gastric artery", "Arteria gástrica izquierda", "car", G+" (abdominales)", "Rama del tronco celíaco que recorre la curvatura menor del estómago y da ramas esofágicas.")
add("common hepatic artery", "Arteria hepática común", "car", G+" (abdominales)", "Rama del tronco celíaco que irriga hígado, vesícula, estómago (curvatura menor y mayor), duodeno y páncreas.")
add("splenic artery", "Arteria esplénica", "car", G+" (abdominales)", "La rama más gruesa del tronco celíaco; recorre tortuosamente el borde superior del páncreas hasta el bazo.")
add("superior mesenteric artery", "Arteria mesentérica superior", "car", G+" (abdominales)", "Nace de la aorta a nivel de L1 e irriga el intestino delgado (desde la segunda porción del duodeno), el ciego, el colon ascendente y los 2/3 del transverso.")
add("inferior mesenteric artery", "Arteria mesentérica inferior", "car", G+" (abdominales)", "Nace de la aorta a nivel de L3 e irriga el tercio distal del colon transverso, el colon descendente, el sigma y el recto superior.")
add("renal artery", "Arteria renal", "car", G+" (abdominales)", "Nace de la aorta a nivel de L1–L2. Los riñones reciben ≈20 % del gasto cardíaco. La derecha es más larga y pasa por detrás de la vena cava inferior.")
add("common iliac artery", "Arteria ilíaca común", "car", G+" (pelvis)", "Rama terminal de la aorta (L4). Se divide frente a la articulación sacroilíaca en ilíaca externa e interna.")
add("external iliac artery", "Arteria ilíaca externa", "car", G+" (pelvis)", "Recorre el borde de la pelvis y, al pasar bajo el ligamento inguinal, se convierte en la arteria femoral, principal arteria del miembro inferior.")
add("internal iliac artery", "Arteria ilíaca interna", "car", G+" (pelvis)", "Irriga las vísceras pélvicas, el periné, la región glútea y la parte medial del muslo.")
add("pulmonary artery", "Arterias pulmonares (tronco pulmonar)", "car", G, "Llevan sangre pobre en oxígeno desde el ventrículo derecho a los pulmones. El tronco pulmonar se divide en arterias pulmonares derecha e izquierda bajo el arco aórtico. Son las únicas arterias del adulto que transportan sangre desoxigenada.")
G = "Grandes venas"
add("superior vena cava", "Vena cava superior", "car", G, "Formada por la unión de las dos venas braquiocefálicas. Recoge la sangre de cabeza, cuello, miembros superiores y tórax y desemboca en la aurícula derecha.", [["Longitud", "≈7 cm"]])
add("inferior vena cava", "Vena cava inferior", "car", G, "La vena más grande del cuerpo. Se forma a nivel de L5 por la unión de las ilíacas comunes, asciende a la derecha de la aorta, atraviesa el diafragma (T8) y desemboca en la aurícula derecha.")
add("brachiocephalic vein", "Vena braquiocefálica", "car", G, "Formada por la unión de la yugular interna y la subclavia detrás de la articulación esternoclavicular. La izquierda es más larga y cruza por delante de las ramas del arco aórtico.")
add("internal jugular vein", "Vena yugular interna", "car", G, "Recoge la sangre del encéfalo, la cara y el cuello. Nace en el agujero yugular y desciende en la vaina carotídea junto a la carótida y el nervio vago.")
add("subclavian vein", "Vena subclavia", "car", G, "Continúa la vena axilar. Pasa por delante del escaleno anterior, sobre la primera costilla, y se une a la yugular interna. Es una vía habitual de acceso venoso central.")
add("pulmonary vein", "Venas pulmonares", "car", G, "Normalmente cuatro (dos por pulmón). Llevan sangre oxigenada desde los pulmones a la aurícula izquierda. Son las únicas venas del adulto que transportan sangre oxigenada.")
add("splenic vein", "Vena esplénica", "car", G+" (sistema porta)", "Drena el bazo y parte del páncreas y el estómago; tras recibir la mesentérica inferior se une a la mesentérica superior detrás del cuello del páncreas para formar la vena porta.")
add("superior mesenteric vein", "Vena mesentérica superior", "car", G+" (sistema porta)", "Drena el intestino delgado, el ciego y el colon ascendente y transverso. Con la vena esplénica forma la vena porta, que lleva los nutrientes absorbidos al hígado.")
add("renal vein", "Vena renal", "car", G, "Drena el riñón en la vena cava inferior. La izquierda es más larga y cruza por delante de la aorta, bajo la arteria mesentérica superior.")
add("common iliac vein", "Vena ilíaca común", "car", G+" (pelvis)", "Formada por la unión de las ilíacas externa e interna. Ambas se unen a nivel de L5 para formar la vena cava inferior.")
add("external iliac vein", "Vena ilíaca externa", "car", G+" (pelvis)", "Continuación de la vena femoral por encima del ligamento inguinal; drena el miembro inferior.")
add("internal iliac vein", "Vena ilíaca interna", "car", G+" (pelvis)", "Drena las vísceras pélvicas, el periné y la región glútea.")

# ============================ RESPIRATORIO
G = "Vías respiratorias"
add("set of nasal cartilages", "Cartílagos nasales", "res", G, "Cartílagos hialinos que forman el esqueleto de la parte móvil de la nariz: cartílagos alares mayores, laterales y del tabique.")
add("thyroid cartilage", "Cartílago tiroides", "res", G, "El mayor cartílago de la laringe. Sus dos láminas se unen por delante formando la prominencia laríngea («nuez»), más marcada en el varón. Protege las cuerdas vocales, que se fijan a su cara interna.", [["Tejido", "Cartílago hialino"], ["Nivel", "C4–C5"]])
add("trachea", "Tráquea", "res", G, "Tubo de ≈10–12 cm que va de la laringe (C6) a la carina (T4–T5), donde se divide en los dos bronquios principales. Lo sostienen 16–20 anillos de cartílago hialino en forma de C, abiertos por detrás.", [["Longitud", "≈10–12 cm"], ["Diámetro", "≈2 cm"]])
add("bronchus", "Bronquios", "res", G, "Árbol bronquial: los bronquios principales se dividen en lobulares y segmentarios. El principal derecho es más corto, ancho y vertical, por lo que los cuerpos extraños aspirados suelen ir a la derecha.")
G = "Pulmones"
PUL = " Los pulmones contienen ≈300–500 millones de alvéolos, con una superficie de intercambio de ≈70 m²."
addf("upper lobe of right lung", "Lóbulo superior del pulmón derecho", "res", G, "Lóbulo apical del pulmón derecho, separado del medio por la fisura horizontal. Tiene tres segmentos: apical, posterior y anterior."+PUL, [["Pulmón derecho", "3 lóbulos, 10 segmentos"]])
addf("middle lobe of lung", "Lóbulo medio del pulmón derecho", "res", G, "Lóbulo exclusivo del pulmón derecho, limitado por las fisuras horizontal y oblicua. Tiene dos segmentos: lateral y medial."+PUL)
addf("lower lobe of right lung", "Lóbulo inferior del pulmón derecho", "res", G, "Lóbulo basal y posterior del pulmón derecho, bajo la fisura oblicua. Tiene cinco segmentos (superior y cuatro basales)."+PUL)
addf("upper lobe of left lung", "Lóbulo superior del pulmón izquierdo", "res", G, "Lóbulo superior del pulmón izquierdo. Incluye la língula, equivalente al lóbulo medio derecho, y la escotadura cardíaca que deja espacio al corazón."+PUL, [["Pulmón izquierdo", "2 lóbulos, 8–10 segmentos"]])
addf("lower lobe of left lung", "Lóbulo inferior del pulmón izquierdo", "res", G, "Lóbulo situado bajo la fisura oblicua del pulmón izquierdo; forma la mayor parte de la cara diafragmática y posterior."+PUL)

# ============================ DIGESTIVO
G = "Boca y dientes"
add("labial part of mouth, nsn", "Labios", "dig", G, "Pliegues musculomembranosos que rodean el orificio bucal, formados por el músculo orbicular de la boca cubierto por piel y mucosa. Su zona roja (bermellón) tiene un epitelio fino muy vascularizado.")
add("gingiva of upper jaw", "Encía superior", "dig", G, "Mucosa fibrosa que cubre las apófisis alveolares del maxilar y rodea el cuello de los dientes.")
add("gingiva of lower jaw", "Encía inferior", "dig", G, "Mucosa fibrosa que cubre la porción alveolar de la mandíbula y rodea el cuello de los dientes.")
DT = " Los dientes forman parte del sistema digestivo (cavidad oral). El adulto tiene 32 dientes permanentes; en este modelo faltan los terceros molares (muelas del juicio). Están formados por esmalte, dentina, pulpa y cemento."
def tooth(key, n, d): add(key, n, "dig", "Boca y dientes", d+DT)
tooth("upper central secondary incisor tooth", "Incisivo central superior", "Diente con corona en forma de pala y una sola raíz; corta los alimentos.")
tooth("upper lateral secondary incisor tooth", "Incisivo lateral superior", "Diente cortante, más pequeño que el central, con una sola raíz.")
tooth("lower central secondary incisor tooth", "Incisivo central inferior", "El diente más pequeño de la dentición permanente; corona cortante y una sola raíz.")
tooth("lower lateral secondary incisor tooth", "Incisivo lateral inferior", "Diente cortante con una sola raíz, algo mayor que el central inferior.")
tooth("upper secondary canine tooth", "Canino superior", "Diente con cúspide puntiaguda que desgarra el alimento. Tiene la raíz más larga de la dentición.")
tooth("lower secondary canine tooth", "Canino inferior", "Diente con cúspide puntiaguda que desgarra el alimento; una sola raíz larga.")
tooth("upper first secondary premolar tooth", "Primer premolar superior", "Diente con dos cúspides que tritura el alimento; suele tener dos raíces.")
tooth("upper second secondary premolar tooth", "Segundo premolar superior", "Diente con dos cúspides que tritura el alimento; suele tener una raíz.")
tooth("lower first secondary premolar tooth", "Primer premolar inferior", "Premolar con una cúspide vestibular dominante y una lingual pequeña; una raíz.")
tooth("lower second secondary premolar tooth", "Segundo premolar inferior", "Premolar con dos o tres cúspides; una raíz.")
tooth("upper first secondary molar tooth", "Primer molar superior", "Molar grande con cuatro cúspides y tres raíces; muele el alimento. Erupciona hacia los 6 años.")
tooth("upper second secondary molar tooth", "Segundo molar superior", "Molar con tres o cuatro cúspides y tres raíces. Erupciona hacia los 12 años.")
tooth("lower first secondary molar tooth", "Primer molar inferior", "Molar con cinco cúspides y dos raíces (mesial y distal). Erupciona hacia los 6 años.")
tooth("lower second secondary molar tooth", "Segundo molar inferior", "Molar con cuatro cúspides y dos raíces. Erupciona hacia los 12 años.")
G = "Tubo digestivo"
add("esophagus", "Esófago", "dig", G, "Tubo muscular de ≈25 cm que lleva el bolo alimenticio de la faringe al estómago mediante ondas peristálticas. Atraviesa el diafragma a nivel de T10. Su tercio superior tiene músculo estriado y los inferiores, liso.", [["Longitud", "≈25 cm"]])
add("stomach", "Estómago", "dig", G, "Dilatación del tubo digestivo en forma de J situada en el epigastrio e hipocondrio izquierdo. Almacena el alimento y lo digiere parcialmente con ácido clorhídrico y pepsina, transformándolo en quimo.", [["Capacidad", "≈1–1,5 L (hasta 2–3 L)"], ["Partes", "Cardias, fundus, cuerpo, antro y píloro"]])
add("duodenum", "Duodeno", "dig", G, "Primera porción del intestino delgado (≈25 cm), en forma de C alrededor de la cabeza del páncreas. En su segunda porción desembocan el colédoco y el conducto pancreático (ampolla de Vater).", [["Longitud", "≈25 cm"]])
add("jejunum", "Yeyuno", "dig", G, "Segunda porción del intestino delgado (≈2/5 proximales del yeyunoíleon). Tiene pliegues circulares altos y abundantes y es el principal lugar de absorción de nutrientes.", [["Longitud", "≈2,5 m"]])
add("ileum", "Íleon", "dig", G, "Porción final del intestino delgado (≈3/5 distales). Absorbe vitamina B12 y sales biliares y contiene placas de Peyer (tejido linfoide). Desemboca en el ciego por la válvula ileocecal.", [["Longitud", "≈3,5 m"]])
add("appendix", "Apéndice vermiforme", "dig", G, "Divertículo ciego y estrecho (≈8 cm) que nace del ciego. Rico en tejido linfoide. Su inflamación (apendicitis) es la urgencia quirúrgica abdominal más frecuente.", [["Longitud", "≈6–10 cm"]])
add("colon, nsn", "Colon", "dig", G, "Parte del intestino grueso entre el ciego y el recto: ascendente, transverso, descendente y sigmoide. Absorbe agua y electrolitos y forma las heces. Presenta haustras, tenias y apéndices omentales.", [["Longitud", "≈1,5 m"]])
add("free taenia", "Tenia libre del colon", "dig", G, "Una de las tres cintas longitudinales de músculo liso del colon; es visible en la cara anterior del colon ascendente y descendente.")
add("mesocolic taenia", "Tenia mesocólica", "dig", G, "Tenia del colon situada en la línea de fijación del mesocolon.")
add("omental taenia", "Tenia omental", "dig", G, "Tenia del colon a la que se une el omento mayor en el colon transverso.")
add("rectum", "Recto", "dig", G, "Porción final del intestino grueso (≈12–15 cm), entre el colon sigmoide (S3) y el conducto anal. Almacena temporalmente las heces.", [["Longitud", "≈12–15 cm"]])
G = "Glándulas anejas"
add("liver", "Hígado", "dig", G, "La glándula más grande del cuerpo (≈1,5 kg), situada en el hipocondrio derecho bajo el diafragma. Produce bilis, metaboliza nutrientes y fármacos, sintetiza proteínas plasmáticas y almacena glucógeno. Recibe sangre de la arteria hepática y de la vena porta.", [["Peso", "≈1,4–1,6 kg"], ["Irrigación", "25 % arterial, 75 % portal"]])
add("gallbladder", "Vesícula biliar", "dig", G, "Saco en forma de pera bajo el hígado que almacena y concentra la bilis (≈30–50 ml). La vacía en el duodeno tras las comidas grasas por acción de la colecistocinina.", [["Capacidad", "≈30–50 ml"]])
add("pancreas, nsn", "Páncreas", "dig", G, "Glándula alargada retroperitoneal detrás del estómago. Su porción exocrina segrega enzimas digestivas al duodeno; sus islotes de Langerhans (endocrinos) producen insulina y glucagón.", [["Peso", "≈80–100 g"], ["Partes", "Cabeza, cuello, cuerpo y cola"]])
add("pancreatic duct", "Conducto pancreático (de Wirsung)", "dig", G, "Recorre el páncreas de la cola a la cabeza y se une al colédoco en la ampolla hepatopancreática, que desemboca en la papila duodenal mayor.")

# ============================ URINARIO
G = "Sistema urinario"
add("kidney", "Riñón", "uri", G, "Órgano retroperitoneal en forma de judía (≈11 cm) situado entre T12 y L3; el derecho está algo más bajo por el hígado. Filtra ≈180 L de plasma al día mediante ≈1 millón de nefronas y produce 1–2 L de orina. También secreta renina y eritropoyetina.", [["Tamaño", "≈11 × 6 × 3 cm"], ["Peso", "≈150 g"], ["Unidad funcional", "Nefrona"]])
add("ureter", "Uréter", "uri", G, "Conducto muscular de ≈25 cm que transporta la orina desde la pelvis renal hasta la vejiga mediante peristaltismo. Tiene tres estrecheces donde pueden detenerse los cálculos.", [["Longitud", "≈25–30 cm"]])
add("urinary bladder", "Vejiga urinaria", "uri", G, "Órgano muscular hueco situado en la pelvis, tras la sínfisis del pubis. Almacena la orina; su pared (músculo detrusor) se contrae en la micción.", [["Capacidad", "≈400–600 ml"]])
add("urethra", "Uretra", "uri", G, "Conducto que lleva la orina desde la vejiga al exterior. En el varón (≈20 cm) es también la vía del semen y tiene porciones prostática, membranosa y esponjosa.", [["Longitud (varón)", "≈18–20 cm"]])

# ============================ REPRODUCTOR MASCULINO
G = "Sistema reproductor masculino"
add("testis", "Testículo", "rep", G, "Gónada masculina, ovoide (≈4–5 cm), alojada en el escroto. Sus túbulos seminíferos producen espermatozoides y las células de Leydig, testosterona.", [["Tamaño", "≈4–5 × 2,5 cm"], ["Hormona", "Testosterona"]])
add("epididymis", "Epidídimo", "rep", G, "Conducto muy enrollado (≈6 m desplegado) adosado al borde posterior del testículo, donde los espermatozoides maduran y se almacenan.")
add("deferent duct", "Conducto deferente", "rep", G, "Conducto muscular de ≈45 cm que lleva los espermatozoides desde el epidídimo, por el conducto inguinal y la pelvis, hasta el conducto eyaculador.", [["Longitud", "≈45 cm"]])
add("seminal vesicle", "Vesícula seminal", "rep", G, "Glándula tubular situada tras la vejiga. Aporta ≈60–70 % del volumen del semen, un líquido rico en fructosa que nutre a los espermatozoides.")
add("prostate", "Próstata", "rep", G, "Glándula del tamaño de una nuez bajo la vejiga, atravesada por la uretra. Produce ≈20–30 % del semen. Su crecimiento con la edad (hiperplasia benigna) puede dificultar la micción.", [["Peso", "≈20 g"]])
add("corpus cavernosum of penis", "Cuerpos cavernosos del pene", "rep", G, "Dos cilindros de tejido eréctil en la cara dorsal del pene. Al llenarse de sangre producen la erección.")
add("corpus spongiosum of penis, nsn", "Cuerpo esponjoso del pene", "rep", G, "Cilindro de tejido eréctil en la cara ventral del pene que rodea la uretra esponjosa y termina en el glande.")
add("glans penis", "Glande", "rep", G, "Extremo distal expandido del cuerpo esponjoso; contiene el orificio externo de la uretra y abundantes terminaciones sensitivas.")
