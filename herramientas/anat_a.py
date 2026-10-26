# -*- coding: utf-8 -*-
# Contenido anatómico en español (Terminología Anatómica). Parte A: sistemas, piel, esqueleto.
C = {}   # concept key (base English name, sides stripped) -> dict

def add(key, n, s, g, d, f=None):
    C[key] = {"n": n, "s": s, "g": g, "d": d, "f": f or []}

SYSTEMS = [
  # key, nombre, color, capa (profundidad para "pelar"), descripción
  ("teg", "Tegumentario", "#d9a287", 0, "Piel y anexos cutáneos (pelo). Es el órgano más extenso del cuerpo: protege frente a agresiones físicas, químicas y microbianas, regula la temperatura y alberga receptores sensitivos."),
  ("mus", "Muscular", "#b8404a", 1, "Músculos esqueléticos, tendones, aponeurosis y ligamentos asociados. Producen movimiento, mantienen la postura y generan calor. En el cuerpo humano hay más de 600 músculos esqueléticos."),
  ("esq", "Esquelético", "#e8dcc4", 2, "Huesos, cartílagos y discos intervertebrales. El esqueleto adulto tiene unos 206 huesos: sostiene el cuerpo, protege órganos, sirve de palanca a los músculos, almacena calcio y fósforo y aloja la médula ósea hematopoyética."),
  ("ner", "Nervioso y sentidos", "#e3c16f", 3, "Encéfalo, vías ópticas, sistema ventricular y órganos de los sentidos. Integra la información sensitiva y coordina las respuestas del organismo."),
  ("car", "Cardiovascular", "#c8283a", 3, "Corazón y grandes vasos. El corazón bombea unos 5 litros de sangre por minuto en reposo a través de la circulación sistémica y la pulmonar."),
  ("res", "Respiratorio", "#e58f9c", 3, "Vías aéreas y pulmones. Permiten el intercambio de oxígeno y dióxido de carbono entre el aire y la sangre."),
  ("dig", "Digestivo", "#c98a4b", 3, "Tubo digestivo desde la boca hasta el ano y glándulas anejas (hígado, vesícula biliar, páncreas). Digiere los alimentos y absorbe nutrientes y agua."),
  ("uri", "Urinario", "#d6b24a", 3, "Riñones, uréteres, vejiga y uretra. Filtra la sangre, regula el equilibrio hidroelectrolítico y ácido-base y elimina desechos en la orina."),
  ("rep", "Reproductor masculino", "#6f8fc7", 3, "Testículos, vías espermáticas, glándulas anejas y pene. El modelo de origen (BodyParts3D) corresponde a un varón adulto."),
  ("end", "Endocrino", "#8e6bbf", 3, "Glándulas que vierten hormonas a la sangre. En este modelo: hipófisis, glándula pineal y glándulas suprarrenales."),
  ("lin", "Linfático e inmunitario", "#6aa36f", 3, "Órganos linfoides: bazo y timo. Participan en la defensa inmunitaria y, el bazo, en el filtrado de la sangre."),
]

# ---------------------------------------------------------------- TEGUMENTARIO
add("skin", "Piel", "teg", "Piel",
    "Órgano que recubre toda la superficie corporal (≈1,8 m² y ≈4 kg en el adulto). Consta de epidermis (epitelio plano estratificado queratinizado), dermis (tejido conectivo con vasos, nervios, folículos pilosos y glándulas) y se apoya en la hipodermis o tejido subcutáneo.",
    [["Funciones", "Barrera protectora, termorregulación, sensibilidad, síntesis de vitamina D"], ["Capas", "Epidermis · dermis · (hipodermis)"]])
add("set of head hairs", "Cabello", "teg", "Anexos cutáneos",
    "Conjunto de pelos terminales del cuero cabelludo. Cada pelo nace de un folículo piloso de la dermis; está formado por queratina dura y crece aproximadamente 1 cm al mes.",
    [["Tejido", "Queratina (anexo epidérmico)"], ["Función", "Protección frente a radiación solar y aislamiento térmico"]])
add("set of eyebrows", "Cejas", "teg", "Anexos cutáneos",
    "Pelos gruesos situados sobre el borde supraorbitario. Desvían el sudor y el agua lejos de los ojos y participan en la expresión facial.")
add("set of pubic hairs", "Vello púbico", "teg", "Anexos cutáneos",
    "Pelo terminal de la región púbica, que aparece en la pubertad por acción de los andrógenos. Es un carácter sexual secundario.")

# ---------------------------------------------------------------- ESQUELETO: cráneo
G_CR = "Cráneo"
add("frontal bone", "Hueso frontal", "esq", G_CR,
    "Hueso impar que forma la frente, el techo de las órbitas y la parte anterior de la bóveda craneal. Contiene los senos frontales.",
    [["Tipo", "Hueso plano"], ["Articula con", "Parietales, esfenoides, etmoides, nasales, maxilares, lagrimales y cigomáticos"]])
add("parietal bone", "Hueso parietal", "esq", G_CR,
    "Hueso par, cuadrilátero, que forma la mayor parte del techo y las paredes laterales del cráneo. Los dos parietales se unen en la sutura sagital.",
    [["Tipo", "Hueso plano"], ["Suturas", "Coronal, sagital, lambdoidea y escamosa"]])
add("occipital bone", "Hueso occipital", "esq", G_CR,
    "Hueso impar de la parte posterior e inferior del cráneo. Presenta el agujero magno, por donde el encéfalo se continúa con la médula espinal, y los cóndilos que articulan con el atlas.",
    [["Tipo", "Hueso plano"], ["Articula con", "Parietales, temporales, esfenoides y atlas (C1)"]])
add("temporal bone", "Hueso temporal", "esq", G_CR,
    "Hueso par de la pared lateral y la base del cráneo. Aloja el oído medio e interno en su porción petrosa y articula con la mandíbula en la articulación temporomandibular.",
    [["Partes", "Escama, porción petrosa, porción timpánica, apófisis estiloides y mastoides"]])
add("sphenoid bone", "Hueso esfenoides", "esq", G_CR,
    "Hueso impar en forma de mariposa situado en el centro de la base del cráneo. Su silla turca aloja la hipófisis y articula con todos los demás huesos del neurocráneo.",
    [["Partes", "Cuerpo, alas mayores, alas menores y apófisis pterigoides"]])
add("ethmoid", "Hueso etmoides", "esq", G_CR,
    "Hueso impar y ligero situado entre las órbitas. Forma parte del techo y las paredes de las fosas nasales; su lámina cribosa deja pasar los filetes del nervio olfatorio.",
    [["Partes", "Lámina cribosa, lámina perpendicular y laberintos etmoidales"]])
add("maxilla", "Maxilar", "esq", G_CR,
    "Hueso par que forma la mandíbula superior, parte del paladar duro, el suelo de la órbita y la pared lateral de las fosas nasales. Aloja los dientes superiores y el seno maxilar.",
    [["Tipo", "Hueso neumático"], ["Contiene", "Seno maxilar y alvéolos dentarios superiores"]])
add("mandible", "Mandíbula", "esq", G_CR,
    "Único hueso móvil del cráneo y el más fuerte de la cara. Aloja los dientes inferiores y articula con los temporales en las articulaciones temporomandibulares.",
    [["Partes", "Cuerpo, ramas, apófisis coronoides y cóndilos"], ["Articulación", "Temporomandibular (bicondílea)"]])
add("zygomatic bone", "Hueso cigomático", "esq", G_CR,
    "Hueso par que forma el pómulo y parte de la pared lateral de la órbita. Con la apófisis cigomática del temporal forma el arco cigomático.")
add("nasal bone", "Hueso nasal", "esq", G_CR,
    "Hueso par, pequeño y alargado, que forma el dorso óseo de la nariz.")
add("lacrimal bone", "Hueso lagrimal", "esq", G_CR,
    "Hueso par, el más pequeño de la cara, en la pared medial de la órbita. Contiene la fosa del saco lagrimal.")
add("palatine bone", "Hueso palatino", "esq", G_CR,
    "Hueso par en forma de L que forma la parte posterior del paladar duro y parte de la pared lateral de las fosas nasales.")
add("inferior nasal concha", "Cornete nasal inferior", "esq", G_CR,
    "Hueso par, curvo, en la pared lateral de la fosa nasal. Aumenta la superficie de la mucosa que calienta y humedece el aire inspirado.")
add("vomer", "Vómer", "esq", G_CR,
    "Hueso impar y plano que forma la parte posteroinferior del tabique nasal.")
add("hyoid bone", "Hueso hioides", "esq", "Cuello",
    "Hueso en forma de U situado en el cuello a nivel de C3. Es el único hueso que no articula con ningún otro: está suspendido por músculos y ligamentos y sirve de anclaje a la lengua.",
    [["Partes", "Cuerpo, astas mayores y astas menores"]])

# ---------------------------------------------------------------- ESQUELETO: columna
G_CV = "Columna vertebral"
add("atlas", "Atlas (C1)", "esq", G_CV,
    "Primera vértebra cervical. Carece de cuerpo y de apófisis espinosa: es un anillo con dos masas laterales que sostienen el cráneo. La articulación atlantooccipital permite la flexión y extensión de la cabeza («decir sí»).",
    [["Articula con", "Occipital y axis"]])
add("axis", "Axis (C2)", "esq", G_CV,
    "Segunda vértebra cervical. Su diente (apófisis odontoides) actúa como pivote alrededor del cual gira el atlas: la articulación atlantoaxial permite la rotación de la cabeza («decir no»).")
CERV = "Vértebra cervical típica: cuerpo pequeño, agujeros transversos por donde asciende la arteria vertebral (C1–C6) y apófisis espinosa corta, bífida en C3–C6."
C7 = "Vértebra prominente: su apófisis espinosa larga y no bífida es fácilmente palpable en la base del cuello y sirve de referencia clínica."
TORA = "Vértebra torácica: presenta fositas costales en el cuerpo y en las apófisis transversas para articular con las costillas, y una apófisis espinosa larga dirigida hacia abajo."
LUMB = "Vértebra lumbar: la de mayor tamaño, con cuerpo reniforme y robusto adaptado a soportar el peso del tronco. Sus apófisis espinosas son cortas y horizontales."
ORD = ["first","second","third","fourth","fifth","sixth","seventh","eighth","ninth","tenth","eleventh","twelfth"]
ORD_ES = ["primera","segunda","tercera","cuarta","quinta","sexta","séptima","octava","novena","décima","undécima","duodécima"]
ORD_ES_M = ["primer","segundo","tercer","cuarto","quinto","sexto","séptimo","octavo","noveno","décimo","undécimo","duodécimo"]
for i in range(2,7):
    add(f"{ORD[i]} cervical vertebra", f"Vértebra C{i+1}", "esq", G_CV, (C7 if i==6 else CERV))
for i in range(12):
    extra = ""
    if i==0: extra=" Articula con la primera costilla y con parte de la segunda."
    if i>=10: extra=" Sus fositas costales son completas y únicas; ya no articula con las apófisis transversas."
    add(f"{ORD[i]} thoracic vertebra", f"Vértebra T{i+1}", "esq", G_CV, TORA+extra)
for i in range(5):
    extra = " Articula con el sacro en la articulación lumbosacra; el disco L5–S1 es uno de los más afectados por hernias." if i==4 else ""
    add(f"{ORD[i]} lumbar vertebra", f"Vértebra L{i+1}", "esq", G_CV, LUMB+extra)
add("sacrum", "Sacro", "esq", G_CV,
    "Hueso triangular formado por la fusión de las cinco vértebras sacras. Se encaja entre los dos coxales en las articulaciones sacroilíacas y transmite el peso del tronco a la pelvis.",
    [["Formado por", "Fusión de S1–S5"], ["Articula con", "L5, coxales y cóccix"]])
DISC = "Disco intervertebral: fibrocartílago formado por un anillo fibroso periférico y un núcleo pulposo gelatinoso central. Amortigua cargas y permite pequeños movimientos entre vértebras."
def disc_name(lbl): return f"Disco intervertebral {lbl}"
add("intervertebral disk of axis", disc_name("C2–C3"), "esq", G_CV, DISC)
for i in range(2,7):
    add(f"intervertebral disk of {ORD[i]} cervical vertebra", disc_name(f"C{i+1}–C{i+2}" if i<6 else "C7–T1"), "esq", G_CV, DISC)
for i in range(12):
    add(f"intervertebral disk of {ORD[i]} thoracic vertebra", disc_name(f"T{i+1}–T{i+2}" if i<11 else "T12–L1"), "esq", G_CV, DISC)
for i in range(5):
    add(f"intervertebral disk of {ORD[i]} lumbar vertebra", disc_name(f"L{i+1}–L{i+2}" if i<4 else "L5–S1"), "esq", G_CV, DISC)

# ---------------------------------------------------------------- ESQUELETO: tórax
G_TX = "Caja torácica"
for i in range(12):
    if i<7: tipo = "Costilla verdadera (vertebroesternal): se une directamente al esternón mediante su propio cartílago costal."
    elif i<10: tipo = "Costilla falsa (vertebrocondral): su cartílago se une al de la costilla superior, formando el arco costal."
    else: tipo = "Costilla flotante: su extremo anterior termina libre en la musculatura de la pared abdominal."
    extra = ""
    if i==0: extra=" Es la más corta, ancha y plana; por su cara superior cruzan la arteria y la vena subclavias."
    add(f"{ORD[i]} rib", f"{ORD_ES_M[i].capitalize()} costilla".replace("Primer costilla","Primera costilla").replace("Tercer costilla","Tercera costilla"), "esq", G_TX, tipo+extra,
        [["Nº", f"{i+1}.ª de 12 pares"]])
# nombres correctos en femenino
for i in range(12):
    C[f"{ORD[i]} rib"]["n"] = f"{ORD_ES[i].capitalize()} costilla"
for i in range(7):
    add(f"{ORD[i]} costal cartilage", f"{ORD_ES_M[i].capitalize()} cartílago costal", "esq", G_TX,
        "Cartílago hialino que une el extremo anterior de la costilla al esternón. Su elasticidad permite la expansión de la caja torácica en la respiración.")
add("costal cartilage", "Cartílagos costales (8.º–10.º)", "esq", G_TX,
    "Cartílagos hialinos de las costillas falsas. Se unen entre sí y al séptimo cartílago formando el reborde o arco costal.")
add("manubrium", "Manubrio del esternón", "esq", G_TX,
    "Parte superior del esternón. Articula con las clavículas y con el primer cartílago costal; su unión con el cuerpo forma el ángulo esternal (de Louis), a la altura de la segunda costilla.")
add("body of sternum", "Cuerpo del esternón", "esq", G_TX,
    "Porción central y más larga del esternón. En sus bordes laterales articulan los cartílagos costales 2.º a 7.º.")
add("xiphoid process", "Apófisis xifoides", "esq", G_TX,
    "Extremo inferior, pequeño, del esternón. Es cartilaginosa en el joven y se osifica con la edad; en ella se inserta la línea alba.")

# ---------------------------------------------------------------- ESQUELETO: miembro superior
G_MS = "Miembro superior"
add("clavicle", "Clavícula", "esq", G_MS,
    "Hueso largo en forma de S itálica que une el miembro superior al tronco. Articula medialmente con el esternón y lateralmente con el acromion de la escápula. Es el hueso que se fractura con más frecuencia.",
    [["Articulaciones", "Esternoclavicular y acromioclavicular"]])
add("scapula", "Escápula (omóplato)", "esq", G_MS,
    "Hueso plano y triangular de la parte posterior del tórax. Su cavidad glenoidea articula con la cabeza del húmero formando el hombro; la espina termina en el acromion.",
    [["Relieves", "Espina, acromion, apófisis coracoides, cavidad glenoidea"]])
add("humerus", "Húmero", "esq", G_MS,
    "Hueso largo del brazo. Su cabeza articula con la escápula (hombro) y su extremo distal con el radio y el cúbito (codo). El nervio radial discurre por su surco en la diáfisis.",
    [["Tipo", "Hueso largo"], ["Articulaciones", "Glenohumeral y del codo"]])
add("radius", "Radio", "esq", G_MS,
    "Hueso lateral del antebrazo (del lado del pulgar). Gira alrededor del cúbito en la pronación y supinación. Su extremo distal forma la mayor parte de la articulación de la muñeca.",
    [["Tipo", "Hueso largo"]])
add("ulna", "Cúbito (ulna)", "esq", G_MS,
    "Hueso medial del antebrazo. Su olécranon forma la punta del codo y su escotadura troclear articula con el húmero.",
    [["Tipo", "Hueso largo"]])
CARPO = "Hueso corto del carpo. Los ocho huesos del carpo se disponen en dos filas y forman el esqueleto de la muñeca."
add("scaphoid", "Escafoides", "esq", "Mano: carpo", CARPO+" El escafoides (fila proximal) es el que se fractura con más frecuencia; su vascularización retrógrada favorece la necrosis tras la fractura.")
add("lunate", "Semilunar", "esq", "Mano: carpo", CARPO+" Fila proximal; es el hueso del carpo que se luxa con más frecuencia.")
add("triquetral", "Piramidal", "esq", "Mano: carpo", CARPO+" Fila proximal; articula con el pisiforme en su cara palmar.")
add("pisiform", "Pisiforme", "esq", "Mano: carpo", CARPO+" Fila proximal; es un hueso sesamoideo dentro del tendón del flexor cubital del carpo.")
add("trapezium", "Trapecio", "esq", "Mano: carpo", CARPO+" Fila distal; articula en silla de montar con el primer metacarpiano, lo que permite la oposición del pulgar.")
add("trapezoid", "Trapezoide", "esq", "Mano: carpo", CARPO+" Fila distal; el más pequeño de la fila, articula con el segundo metacarpiano.")
add("capitate", "Hueso grande (capitado)", "esq", "Mano: carpo", CARPO+" Fila distal; es el mayor hueso del carpo y articula con el tercer metacarpiano.")
add("hamate", "Ganchoso", "esq", "Mano: carpo", CARPO+" Fila distal; su gancho delimita el canal de Guyon, por donde pasan el nervio y la arteria cubitales.")
MC = "Hueso largo de la palma de la mano. Su base articula con el carpo y su cabeza con la falange proximal (nudillo)."
for i,dd in enumerate(["del pulgar; el más corto y robusto, con gran movilidad", "del índice; el más largo", "del dedo medio; presenta la apófisis estiloides en su base", "del anular", "del meñique"]):
    add(f"{ORD[i]} metacarpal bone", f"{ORD_ES_M[i].capitalize()} metacarpiano", "esq", "Mano: metacarpo", MC+f" Metacarpiano {dd}.")
DEDOS = {"thumb":"pulgar","index finger":"índice","middle finger":"dedo medio","ring finger":"anular","little finger":"meñique"}
for en,es in DEDOS.items():
    for ph,phes,txt in [("proximal","proximal","Articula con la cabeza del metacarpiano (articulación metacarpofalángica)."),("middle","media","Situada entre las falanges proximal y distal; el pulgar carece de ella."),("distal","distal","Porción terminal del dedo; su tuberosidad sostiene el pulpejo y la uña.")]:
        if en=="thumb" and ph=="middle": continue
        add(f"{ph} phalanx of {en}", f"Falange {phes} del {es}".replace("del dedo medio","del dedo medio"), "esq", "Mano: falanges",
            f"Hueso largo en miniatura de los dedos de la mano. {txt}")

# ---------------------------------------------------------------- ESQUELETO: miembro inferior
G_MI = "Miembro inferior"
add("hip bone", "Hueso coxal", "esq", "Pelvis",
    "Hueso par formado por la fusión del ilion, el isquion y el pubis, que convergen en el acetábulo, donde se aloja la cabeza del fémur. Con el sacro y el cóccix forma la pelvis ósea.",
    [["Partes", "Ilion, isquion y pubis"], ["Articulaciones", "Sacroilíaca, sínfisis del pubis y coxofemoral"]])
add("femur", "Fémur", "esq", G_MI,
    "Hueso del muslo; es el más largo, pesado y resistente del cuerpo (≈1/4 de la estatura). Su cabeza articula con el acetábulo y sus cóndilos con la tibia y la rótula.",
    [["Tipo", "Hueso largo"], ["Articulaciones", "Cadera y rodilla"]])
add("patella", "Rótula", "esq", G_MI,
    "Hueso sesamoideo más grande del cuerpo, incluido en el tendón del cuádriceps. Protege la rodilla y aumenta el brazo de palanca del cuádriceps en la extensión.",
    [["Tipo", "Hueso sesamoideo"]])
add("tibia", "Tibia", "esq", G_MI,
    "Hueso medial y principal de la pierna, que soporta el peso corporal. Su borde anterior es subcutáneo y su extremo distal forma el maléolo medial.",
    [["Tipo", "Hueso largo"], ["Articulaciones", "Rodilla, tibioperonea y tobillo"]])
add("fibula", "Peroné (fíbula)", "esq", G_MI,
    "Hueso lateral y delgado de la pierna. Apenas soporta peso, pero da inserción a músculos y su extremo distal forma el maléolo lateral, que estabiliza el tobillo.",
    [["Tipo", "Hueso largo"]])
TARSO = "Hueso corto del tarso. Los siete huesos del tarso forman el esqueleto posterior del pie."
add("talus", "Astrágalo (talus)", "esq", "Pie: tarso", TARSO+" Transmite el peso de la tibia al resto del pie; no tiene inserciones musculares y está cubierto en gran parte por cartílago articular.")
add("calcaneus", "Calcáneo", "esq", "Pie: tarso", TARSO+" Es el mayor hueso del pie y forma el talón; en su tuberosidad se inserta el tendón calcáneo (de Aquiles).")
add("navicular bone of foot", "Navicular (escafoides tarsiano)", "esq", "Pie: tarso", TARSO+" Situado en el lado medial, entre el astrágalo y los tres cuneiformes; es la clave del arco longitudinal medial.")
add("cuboid bone", "Cuboides", "esq", "Pie: tarso", TARSO+" Situado en el borde lateral del pie; por su surco discurre el tendón del fibular largo.")
add("medial cuneiform bone", "Cuneiforme medial", "esq", "Pie: tarso", TARSO+" El mayor de los tres cuneiformes; articula con el primer metatarsiano.")
add("intermediate cuneiform bone", "Cuneiforme intermedio", "esq", "Pie: tarso", TARSO+" El más pequeño de los cuneiformes; articula con el segundo metatarsiano.")
add("lateral cuneiform bone", "Cuneiforme lateral", "esq", "Pie: tarso", TARSO+" Articula con el tercer metatarsiano y con el cuboides.")
MT = "Hueso largo del antepié. Su base articula con el tarso y su cabeza con la falange proximal; las cabezas metatarsianas apoyan en el suelo durante la marcha."
for i,dd in enumerate(["el más corto y grueso; soporta la mayor carga", "el más largo; frecuente en fracturas por estrés", "", "", "su tuberosidad recibe el tendón del fibular corto"]):
    add(f"{ORD[i]} metatarsal bone", f"{ORD_ES_M[i].capitalize()} metatarsiano", "esq", "Pie: metatarso", MT+(f" Es {dd}." if dd else ""))
TOES = {"big toe":"dedo gordo (hallux)","second toe":"segundo dedo","third toe":"tercer dedo","fourth toe":"cuarto dedo","little toe":"quinto dedo"}
for en,es in TOES.items():
    for ph,phes in [("proximal","proximal"),("middle","media"),("distal","distal")]:
        if en=="big toe" and ph=="middle": continue
        add(f"{ph} phalanx of {en}", f"Falange {phes} del {es}", "esq", "Pie: falanges",
            "Hueso de los dedos del pie. Son más cortas que las de la mano; el dedo gordo tiene solo dos falanges.")
add("sesamoid bone of foot", "Huesos sesamoideos del pie", "esq", "Pie: metatarso",
    "Pequeños huesos incluidos en los tendones del flexor corto del dedo gordo, bajo la cabeza del primer metatarsiano. Protegen el tendón y mejoran su palanca.")
