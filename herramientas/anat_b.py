# -*- coding: utf-8 -*-
# Parte B: sistema muscular. Datos: origen, inserción, acción, inervación.
from anat_a import C, add, ORD

def M(key, n, g, o, i, a, inv, d=""):
    f = [["Origen", o], ["Inserción", i], ["Acción", a], ["Inervación", inv]]
    desc = d or f"Músculo esquelético. {a[0].upper()+a[1:]}."
    add(key, n, "mus", g, desc, f)

# ============================ CABEZA: mímica (todos inervados por el nervio facial, VII)
G = "Cabeza: músculos de la expresión facial"
VII = "Nervio facial (VII)"
M("frontalis", "Músculo frontal (vientre frontal del occipitofrontal)", G, "Aponeurosis epicraneal", "Piel de la ceja y la frente", "Eleva las cejas y arruga la frente horizontalmente", VII + ", ramos temporales")
M("occipitalis", "Músculo occipital (vientre occipital del occipitofrontal)", G, "Línea nucal suprema del occipital y mastoides", "Aponeurosis epicraneal", "Tracciona el cuero cabelludo hacia atrás", VII + ", ramo auricular posterior")
M("temporoparietalis", "Músculo temporoparietal", G, "Fascia temporal por encima del pabellón auricular", "Borde lateral de la aponeurosis epicraneal", "Tensa el cuero cabelludo y eleva el pabellón auricular", VII + ", ramos temporales")
add("aponeurosis of epicranius", "Aponeurosis epicraneal (galea aponeurótica)", "mus", G,
    "Lámina tendinosa resistente que cubre la bóveda craneal y une los vientres frontal y occipital del músculo occipitofrontal. Está firmemente unida a la piel del cuero cabelludo.",
    [["Tipo", "Tejido conectivo denso (aponeurosis)"]])
M("orbital part of orbicularis oculi", "Músculo orbicular del ojo — porción orbitaria", G, "Parte nasal del hueso frontal, apófisis frontal del maxilar y ligamento palpebral medial", "Fibras circulares que rodean la órbita y vuelven a su origen", "Cierra los párpados con fuerza (guiño forzado)", VII + ", ramos temporales y cigomáticos")
M("palpebral part of orbicularis oculi", "Músculo orbicular del ojo — porción palpebral", G, "Ligamento palpebral medial", "Rafe palpebral lateral", "Cierra los párpados suavemente (parpadeo y sueño)", VII + ", ramos temporales y cigomáticos")
M("corrugator supercilii", "Músculo corrugador superciliar", G, "Extremo medial del arco superciliar", "Piel de la mitad de la ceja", "Tracciona la ceja hacia abajo y adentro (fruncir el ceño)", VII + ", ramos temporales")
M("procerus", "Músculo prócer", G, "Fascia del hueso nasal y cartílago nasal lateral", "Piel entre las cejas", "Desciende el extremo medial de las cejas y produce arrugas transversales en la raíz nasal", VII)
M("nasalis", "Músculo nasal", G, "Maxilar, por encima de los incisivos y canino", "Aponeurosis del dorso nasal y cartílago alar", "Comprime la narina (porción transversa) o la dilata (porción alar)", VII + ", ramos bucales")
M("depressor septi nasi", "Músculo depresor del tabique nasal", G, "Fosa incisiva del maxilar", "Tabique móvil de la nariz", "Tracciona el tabique hacia abajo y dilata la narina", VII + ", ramos bucales")
M("levator labii superioris alaeque nasi", "Músculo elevador del labio superior y del ala de la nariz", G, "Apófisis frontal del maxilar", "Cartílago alar y labio superior", "Eleva el labio superior y dilata la narina", VII + ", ramos cigomáticos y bucales")
M("levator labii superioris", "Músculo elevador del labio superior", G, "Borde infraorbitario del maxilar", "Piel del labio superior", "Eleva y everte el labio superior", VII + ", ramos cigomáticos y bucales")
M("zygomaticus major", "Músculo cigomático mayor", G, "Cara lateral del hueso cigomático", "Ángulo de la boca (modíolo)", "Tracciona el ángulo de la boca hacia arriba y atrás (sonrisa)", VII + ", ramos cigomáticos")
M("zygomaticus minor", "Músculo cigomático menor", G, "Cara anterior del hueso cigomático", "Labio superior", "Eleva el labio superior", VII + ", ramos cigomáticos")
M("levator anguli oris", "Músculo elevador del ángulo de la boca", G, "Fosa canina del maxilar", "Ángulo de la boca", "Eleva el ángulo de la boca", VII + ", ramos bucales")
M("risorius", "Músculo risorio", G, "Fascia parotídea y maseterina", "Ángulo de la boca", "Tracciona lateralmente el ángulo de la boca", VII + ", ramos bucales")
M("depressor anguli oris", "Músculo depresor del ángulo de la boca", G, "Línea oblicua de la mandíbula", "Ángulo de la boca", "Desciende el ángulo de la boca (expresión de tristeza)", VII + ", ramos mandibulares")
M("depressor labii inferioris", "Músculo depresor del labio inferior", G, "Línea oblicua de la mandíbula", "Piel del labio inferior", "Desciende y everte el labio inferior", VII + ", ramo marginal de la mandíbula")
M("mentalis", "Músculo mentoniano (borla del mentón)", G, "Fosa incisiva de la mandíbula", "Piel del mentón", "Eleva y protruye el labio inferior; arruga la piel del mentón", VII + ", ramo marginal de la mandíbula")
M("orbicularis oris", "Músculo orbicular de la boca", G, "Fibras de los músculos vecinos y maxilar y mandíbula cerca de la línea media", "Piel y mucosa de los labios", "Cierra y protruye los labios (silbar, besar)", VII + ", ramos bucales y mandibulares")
M("buccinator", "Músculo buccinador", G, "Apófisis alveolares del maxilar y la mandíbula y rafe pterigomandibular", "Ángulo de la boca y orbicular de la boca", "Comprime la mejilla contra los dientes; mantiene el alimento entre las arcadas y permite soplar", VII + ", ramos bucales")
M("platysma", "Músculo platisma (cutáneo del cuello)", G, "Fascia de la parte superior del tórax (pectoral mayor y deltoides)", "Borde inferior de la mandíbula y piel de la parte inferior de la cara", "Tensa la piel del cuello y desciende el labio inferior y la mandíbula", VII + ", ramo cervical")

# ============================ CABEZA: masticadores (nervio mandibular, V3)
G = "Cabeza: músculos de la masticación"
V3 = "Nervio mandibular (V3), rama del trigémino"
M("superficial part of masseter", "Músculo masetero — porción superficial", G, "Borde inferior de los dos tercios anteriores del arco cigomático", "Ángulo y cara lateral de la rama de la mandíbula", "Eleva la mandíbula (cierre de la boca) y colabora en la protrusión", V3 + ", nervio maseterino", "Porción superficial, la más voluminosa, del masetero, uno de los músculos más potentes del cuerpo en relación con su tamaño.")
M("deep part of masseter", "Músculo masetero — porción profunda", G, "Cara medial del arco cigomático", "Cara lateral de la rama y apófisis coronoides de la mandíbula", "Eleva la mandíbula y colabora en su retrusión", V3 + ", nervio maseterino")
M("temporalis", "Músculo temporal", G, "Fosa temporal y fascia temporal", "Apófisis coronoides y borde anterior de la rama de la mandíbula", "Eleva la mandíbula; sus fibras posteriores la retraen", V3 + ", nervios temporales profundos")
M("medial pterygoid", "Músculo pterigoideo medial", G, "Fosa pterigoidea (cara medial de la lámina lateral de la apófisis pterigoides)", "Cara medial del ángulo de la mandíbula", "Eleva la mandíbula y, junto con el pterigoideo lateral, produce movimientos de lateralidad", V3)
M("upper head of lateral pterygoid", "Músculo pterigoideo lateral — cabeza superior", G, "Cara infratemporal del ala mayor del esfenoides", "Cápsula y disco de la articulación temporomandibular", "Estabiliza el disco articular durante el cierre de la boca", V3)
M("lower head of lateral pterygoid", "Músculo pterigoideo lateral — cabeza inferior", G, "Cara lateral de la lámina lateral de la apófisis pterigoides", "Fóvea pterigoidea del cuello del cóndilo mandibular", "Protruye la mandíbula e inicia la apertura de la boca; lateralidad", V3)

# ============================ CUELLO
G = "Cuello"
M("sternocleidomastoid", "Músculo esternocleidomastoideo", G, "Manubrio del esternón (cabeza esternal) y tercio medial de la clavícula (cabeza clavicular)", "Apófisis mastoides del temporal y línea nucal superior", "Unilateral: inclina la cabeza hacia su lado y la gira hacia el contrario. Bilateral: flexiona el cuello; músculo inspiratorio accesorio", "Nervio accesorio (XI) y ramos de C2–C3")
M("sternohyoid", "Músculo esternohioideo", G + " (infrahioideos)", "Manubrio del esternón y extremo medial de la clavícula", "Cuerpo del hueso hioides", "Desciende el hioides tras la deglución", "Asa cervical (C1–C3)")
M("sternothyroid", "Músculo esternotiroideo", G + " (infrahioideos)", "Cara posterior del manubrio del esternón", "Línea oblicua del cartílago tiroides", "Desciende la laringe", "Asa cervical (C1–C3)")
M("thyrohyoid", "Músculo tirohioideo", G + " (infrahioideos)", "Línea oblicua del cartílago tiroides", "Cuerpo y asta mayor del hioides", "Desciende el hioides o eleva la laringe si el hioides está fijo", "C1 a través del nervio hipogloso (XII)")
M("omohyoid", "Músculo omohioideo", G + " (infrahioideos)", "Borde superior de la escápula (vientre inferior)", "Cuerpo del hioides (vientre superior)", "Desciende y fija el hioides", "Asa cervical (C1–C3)", "Músculo digástrico con un tendón intermedio unido a la clavícula por una expansión fascial. Desciende y fija el hioides.")
M("anterior belly of digastric", "Músculo digástrico — vientre anterior", G + " (suprahioideos)", "Fosa digástrica de la mandíbula", "Tendón intermedio, fijado al hioides", "Desciende la mandíbula y eleva el hioides", "Nervio milohioideo (de V3)")
M("posterior belly of digastric", "Músculo digástrico — vientre posterior", G + " (suprahioideos)", "Escotadura mastoidea del temporal", "Tendón intermedio, fijado al hioides", "Eleva y retrae el hioides durante la deglución", VII)
add("intermediate tendon", "Tendón intermedio del digástrico", "mus", G + " (suprahioideos)",
    "Tendón que une los vientres anterior y posterior del digástrico. Atraviesa el estilohioideo y se fija al hioides mediante un asa fibrosa.")
M("stylohyoid", "Músculo estilohioideo", G + " (suprahioideos)", "Apófisis estiloides del temporal", "Cuerpo del hioides", "Eleva y retrae el hioides", VII)
M("mylohyoid", "Músculo milohioideo", G + " (suprahioideos)", "Línea milohioidea de la mandíbula", "Rafe medio y cuerpo del hioides", "Forma el suelo de la boca; eleva el hioides y la lengua al deglutir", "Nervio milohioideo (de V3)")
M("geniohyoid", "Músculo geniohioideo", G + " (suprahioideos)", "Espina mentoniana inferior de la mandíbula", "Cuerpo del hioides", "Tracciona el hioides hacia delante y arriba; desciende la mandíbula", "C1 a través del nervio hipogloso (XII)")
M("scalenus anterior", "Músculo escaleno anterior", G + " (escalenos)", "Tubérculos anteriores de las apófisis transversas de C3–C6", "Tubérculo del escaleno de la primera costilla", "Eleva la primera costilla (inspiración forzada); inclina el cuello", "Ramos anteriores de C4–C6", "Músculo profundo del cuello. La arteria subclavia pasa por detrás y la vena subclavia por delante de él.")
M("scalenus medius", "Músculo escaleno medio", G + " (escalenos)", "Tubérculos posteriores de las apófisis transversas de C2–C7", "Cara superior de la primera costilla", "Eleva la primera costilla; inclina el cuello", "Ramos anteriores de C3–C8")
M("scalenus posterior", "Músculo escaleno posterior", G + " (escalenos)", "Tubérculos posteriores de las apófisis transversas de C4–C6", "Cara externa de la segunda costilla", "Eleva la segunda costilla; inclina el cuello", "Ramos anteriores de C6–C8")
M("longus capitis", "Músculo largo de la cabeza", G + " (prevertebrales)", "Tubérculos anteriores de las apófisis transversas de C3–C6", "Porción basilar del occipital", "Flexiona la cabeza", "Ramos anteriores de C1–C3")
M("superior oblique part of longus colli", "Músculo largo del cuello — porción oblicua superior", G + " (prevertebrales)", "Tubérculos anteriores de las apófisis transversas de C3–C5", "Tubérculo anterior del atlas", "Flexiona el cuello", "Ramos anteriores de C2–C6")
M("vertical intermediate part of longus colli", "Músculo largo del cuello — porción vertical", G + " (prevertebrales)", "Cuerpos vertebrales de C5–T3", "Cuerpos vertebrales de C2–C4", "Flexiona el cuello", "Ramos anteriores de C2–C6")
M("inferior oblique part of longus colli", "Músculo largo del cuello — porción oblicua inferior", G + " (prevertebrales)", "Cuerpos vertebrales de T1–T3", "Tubérculos anteriores de las apófisis transversas de C5–C6", "Flexiona e inclina el cuello", "Ramos anteriores de C2–C6")
M("rectus capitis anterior", "Músculo recto anterior de la cabeza", G + " (prevertebrales)", "Masa lateral del atlas", "Porción basilar del occipital", "Flexiona la cabeza en la articulación atlantooccipital", "Ramos anteriores de C1–C2")
M("rectus capitis lateralis", "Músculo recto lateral de la cabeza", G + " (prevertebrales)", "Apófisis transversa del atlas", "Apófisis yugular del occipital", "Inclina lateralmente la cabeza", "Ramos anteriores de C1–C2")

# ============================ DORSO
G = "Dorso: músculos suboccipitales"
SUBOC = "Nervio suboccipital (ramo posterior de C1)"
M("rectus capitis posterior major", "Músculo recto posterior mayor de la cabeza", G, "Apófisis espinosa del axis", "Parte lateral de la línea nucal inferior", "Extiende la cabeza y la gira hacia su lado", SUBOC)
M("rectus capitis posterior minor", "Músculo recto posterior menor de la cabeza", G, "Tubérculo posterior del atlas", "Parte medial de la línea nucal inferior", "Extiende la cabeza", SUBOC)
M("obliquus capitis superior", "Músculo oblicuo superior de la cabeza", G, "Apófisis transversa del atlas", "Occipital, entre las líneas nucales superior e inferior", "Extiende e inclina lateralmente la cabeza", SUBOC)
M("obliquus capitis inferior", "Músculo oblicuo inferior de la cabeza", G, "Apófisis espinosa del axis", "Apófisis transversa del atlas", "Gira el atlas (y la cabeza) hacia su lado", SUBOC)

G = "Dorso: músculos superficiales"
M("descending part of trapezius", "Músculo trapecio — porción descendente", G, "Línea nucal superior, protuberancia occipital externa y ligamento nucal", "Tercio lateral de la clavícula", "Eleva la escápula (encoger los hombros) y la rota hacia arriba", "Nervio accesorio (XI); sensibilidad propioceptiva de C3–C4", "Porción superior del trapecio, gran músculo plano y triangular de la nuca y la espalda.")
M("transverse part of trapezius", "Músculo trapecio — porción transversa", G, "Apófisis espinosas de C7–T3", "Acromion y espina de la escápula", "Retrae la escápula (aproximación a la columna)", "Nervio accesorio (XI)")
M("ascending part of trapezius", "Músculo trapecio — porción ascendente", G, "Apófisis espinosas de T4–T12", "Tubérculo de la espina de la escápula", "Desciende la escápula y colabora en su rotación hacia arriba", "Nervio accesorio (XI)")
M("latissimus dorsi", "Músculo dorsal ancho", G, "Apófisis espinosas de T7–L5 (fascia toracolumbar), cresta ilíaca y costillas 9–12", "Surco intertubercular del húmero", "Extiende, aduce y rota medialmente el húmero (trepar, remar)", "Nervio toracodorsal (C6–C8)", "El músculo más ancho del cuerpo. Extiende, aduce y rota medialmente el brazo.")
M("rhomboid major", "Músculo romboides mayor", G, "Apófisis espinosas de T2–T5", "Borde medial de la escápula, por debajo de la espina", "Retrae y eleva la escápula; la fija a la pared torácica", "Nervio dorsal de la escápula (C4–C5)")
M("rhomboid minor", "Músculo romboides menor", G, "Ligamento nucal y apófisis espinosas de C7–T1", "Borde medial de la escápula, a la altura de la espina", "Retrae y eleva la escápula", "Nervio dorsal de la escápula (C4–C5)")
M("levator scapulae", "Músculo elevador de la escápula", G, "Apófisis transversas de C1–C4", "Ángulo superior de la escápula", "Eleva la escápula e inclina el cuello", "Nervio dorsal de la escápula (C5) y ramos de C3–C4")
M("serratus posterior superior", "Músculo serrato posterior superior", G + " (intermedios)", "Ligamento nucal y apófisis espinosas de C7–T3", "Costillas 2–5", "Eleva las costillas (se le atribuye función inspiratoria)", "Nervios intercostales T2–T5")
M("serratus posterior inferior", "Músculo serrato posterior inferior", G + " (intermedios)", "Apófisis espinosas de T11–L2", "Costillas 9–12", "Desciende las costillas inferiores", "Nervios intercostales T9–T11 y subcostal")

G = "Dorso: músculos profundos (erectores de la columna)"
RP = "Ramos posteriores de los nervios espinales"
M("splenius capitis", "Músculo esplenio de la cabeza", G, "Ligamento nucal y apófisis espinosas de C7–T3", "Apófisis mastoides y tercio lateral de la línea nucal superior", "Extiende la cabeza; unilateralmente la gira hacia su lado", RP + " cervicales medios")
M("splenius cervicis", "Músculo esplenio del cuello", G, "Apófisis espinosas de T3–T6", "Apófisis transversas de C1–C3", "Extiende el cuello y lo gira hacia su lado", RP + " cervicales inferiores")
M("iliocostalis lumborum", "Músculo iliocostal lumbar", G, "Cresta ilíaca, sacro y fascia toracolumbar", "Ángulos de las costillas 6–12", "Extiende e inclina lateralmente la columna", RP)
M("iliocostalis thoracis", "Músculo iliocostal torácico", G, "Ángulos de las costillas 7–12", "Ángulos de las costillas 1–6 y apófisis transversa de C7", "Extiende e inclina lateralmente la columna", RP)
M("iliocostalis cervicis", "Músculo iliocostal cervical", G, "Ángulos de las costillas 3–6", "Apófisis transversas de C4–C6", "Extiende e inclina lateralmente el cuello", RP)
M("longissimus thoracis", "Músculo longísimo torácico", G, "Sacro, apófisis espinosas lumbares y apófisis transversas lumbares", "Apófisis transversas torácicas y costillas 2–12", "Extiende e inclina lateralmente la columna", RP)
M("longissimus cervicis", "Músculo longísimo cervical", G, "Apófisis transversas de T1–T5", "Apófisis transversas de C2–C6", "Extiende e inclina lateralmente el cuello", RP)
M("longissimus capitis", "Músculo longísimo de la cabeza", G, "Apófisis transversas de T1–T5 y articulares de C4–C7", "Apófisis mastoides", "Extiende la cabeza y la gira hacia su lado", RP)
M("spinalis thoracis", "Músculo espinoso torácico", G, "Apófisis espinosas de T11–L2", "Apófisis espinosas de T1–T8", "Extiende la columna torácica", RP)
M("spinalis cervicis", "Músculo espinoso cervical", G, "Ligamento nucal y apófisis espinosas de C7–T2", "Apófisis espinosa del axis", "Extiende el cuello", RP)
M("semispinalis thoracis", "Músculo semiespinoso torácico", G + " (transversoespinosos)", "Apófisis transversas de T6–T10", "Apófisis espinosas de C6–T4", "Extiende la columna y la gira hacia el lado contrario", RP)
M("semispinalis cervicis", "Músculo semiespinoso del cuello", G + " (transversoespinosos)", "Apófisis transversas de T1–T6", "Apófisis espinosas de C2–C5", "Extiende el cuello y lo gira hacia el lado contrario", RP)
M("semispinalis capitis", "Músculo semiespinoso de la cabeza", G + " (transversoespinosos)", "Apófisis transversas de C7–T6 y articulares de C4–C6", "Occipital, entre las líneas nucales", "Principal extensor de la cabeza", RP)
M("multifidus", "Músculo multífido", G + " (transversoespinosos)", "Sacro, espinas ilíacas y apófisis transversas/mamilares de L5 a C4", "Apófisis espinosas situadas 2–4 niveles por encima", "Estabiliza los segmentos vertebrales; extiende y rota la columna", RP, "Músculo profundo formado por fascículos cortos. Es un estabilizador segmentario clave de la columna lumbar.")
M("cervical rotator", "Músculos rotadores cervicales", G + " (transversoespinosos)", "Apófisis transversas de las vértebras cervicales", "Lámina o apófisis espinosa de la vértebra 1–2 niveles superior", "Estabilizan y rotan la columna; función propioceptiva", RP)
M("thoracic rotator", "Músculos rotadores torácicos", G + " (transversoespinosos)", "Apófisis transversas de las vértebras torácicas", "Lámina o apófisis espinosa de la vértebra 1–2 niveles superior", "Estabilizan y rotan la columna; función propioceptiva", RP)
M("lumbar rotator", "Músculos rotadores lumbares", G + " (transversoespinosos)", "Apófisis mamilares de las vértebras lumbares", "Lámina o apófisis espinosa de la vértebra superior", "Estabilizan y rotan la columna; función propioceptiva", RP)
M("set of interspinales cervicis", "Músculos interespinosos cervicales", G + " (segmentarios)", "Apófisis espinosa de una vértebra cervical", "Apófisis espinosa de la vértebra superior", "Extienden el cuello y lo estabilizan", RP)
M("set of interspinales thoracis", "Músculos interespinosos torácicos", G + " (segmentarios)", "Apófisis espinosas torácicas (inconstantes, en los extremos de la región)", "Apófisis espinosa de la vértebra superior", "Extienden y estabilizan la columna", RP)
M("set of interspinales lumborum", "Músculos interespinosos lumbares", G + " (segmentarios)", "Apófisis espinosa de una vértebra lumbar", "Apófisis espinosa de la vértebra superior", "Extienden y estabilizan la columna lumbar", RP)
M("set of anterior cervical intertransversarii", "Músculos intertransversos anteriores del cuello", G + " (segmentarios)", "Tubérculo anterior de una apófisis transversa cervical", "Tubérculo anterior de la apófisis transversa superior", "Inclinación lateral y estabilización del cuello", "Ramos anteriores de los nervios cervicales")
M("set of posterior cervical intertransversarii", "Músculos intertransversos posteriores del cuello", G + " (segmentarios)", "Tubérculo posterior de una apófisis transversa cervical", "Tubérculo posterior de la apófisis transversa superior", "Inclinación lateral y estabilización del cuello", RP)
M("set of lateral lumbar intertransversarius muscles", "Músculos intertransversos laterales lumbares", G + " (segmentarios)", "Apófisis transversa (costal) lumbar", "Apófisis transversa superior", "Inclinación lateral de la columna lumbar", "Ramos anteriores de los nervios lumbares")
M("set of medial lumbar intertransversarius muscles", "Músculos intertransversos mediales lumbares", G + " (segmentarios)", "Apófisis accesoria lumbar", "Apófisis mamilar de la vértebra superior", "Inclinación lateral y estabilización lumbar", RP)
M("set of levatores costarum longi", "Músculos elevadores largos de las costillas", G + " (segmentarios)", "Apófisis transversas de T7–T10", "Costilla situada dos niveles por debajo", "Elevan las costillas; inclinan la columna", RP + " de C8–T11")
M("set of levatores costarum breves", "Músculos elevadores cortos de las costillas", G + " (segmentarios)", "Apófisis transversas de C7–T11", "Costilla inmediatamente inferior, entre tubérculo y ángulo", "Elevan las costillas; inclinan la columna", RP + " de C8–T11")

# ============================ TÓRAX
G = "Tórax"
M("clavicular part of pectoralis major", "Músculo pectoral mayor — porción clavicular", G, "Mitad medial de la clavícula", "Cresta del tubérculo mayor del húmero", "Flexiona el brazo y lo aduce y rota medialmente", "Nervio pectoral lateral (C5–C7)", "Porción superior del pectoral mayor, gran músculo en abanico de la pared anterior del tórax.")
M("sternocostal part of pectoralis major", "Músculo pectoral mayor — porción esternocostal", G, "Cara anterior del esternón y cartílagos costales 1–6", "Cresta del tubérculo mayor del húmero", "Aduce y rota medialmente el brazo; lo extiende desde la flexión", "Nervios pectorales lateral y medial (C5–T1)")
M("abdominal part of pectoralis major", "Músculo pectoral mayor — porción abdominal", G, "Hoja anterior de la vaina del recto del abdomen", "Cresta del tubérculo mayor del húmero", "Aduce y desciende el brazo", "Nervio pectoral medial (C8–T1)")
M("pectoralis minor", "Músculo pectoral menor", G, "Costillas 3–5", "Apófisis coracoides de la escápula", "Desciende y protruye la escápula; eleva las costillas si la escápula está fija", "Nervio pectoral medial (C8–T1)")
M("subclavius", "Músculo subclavio", G, "Unión de la primera costilla con su cartílago", "Cara inferior del tercio medio de la clavícula", "Fija y desciende la clavícula", "Nervio subclavio (C5–C6)")
M("serratus anterior", "Músculo serrato anterior", G, "Caras externas de las costillas 1–8 (o 9)", "Borde medial de la escápula (cara costal)", "Protruye la escápula y la rota hacia arriba; la mantiene pegada al tórax", "Nervio torácico largo (C5–C7)", "Su parálisis produce la «escápula alada». Protruye y rota la escápula.")
M("external intercostal muscle", "Músculos intercostales externos", G, "Borde inferior de la costilla superior", "Borde superior de la costilla inferior (fibras hacia abajo y adelante)", "Elevan las costillas en la inspiración", "Nervios intercostales (T1–T11)")
M("internal intercostal muscle", "Músculos intercostales internos", G, "Borde superior de la costilla inferior", "Borde inferior de la costilla superior (fibras perpendiculares a las externas)", "Descienden las costillas en la espiración forzada", "Nervios intercostales (T1–T11)")
M("innermost intercostal muscle", "Músculos intercostales íntimos", G, "Cara interna de la costilla inferior", "Cara interna de la costilla superior", "Actúan con los intercostales internos", "Nervios intercostales (T1–T11)")
M("transversus thoracis", "Músculo transverso del tórax", G, "Cara posterior del esternón y apófisis xifoides", "Cara interna de los cartílagos costales 2–6", "Desciende los cartílagos costales (espiración)", "Nervios intercostales T2–T6")
M("diaphragm", "Diafragma", G, "Apófisis xifoides, cartílagos costales 7–12 y vértebras L1–L3 (pilares)", "Centro tendinoso", "Principal músculo de la inspiración: al contraerse desciende y aumenta el volumen torácico", "Nervio frénico (C3–C5)",
  "Tabique musculotendinoso en forma de cúpula que separa el tórax del abdomen. Es el principal músculo respiratorio; lo atraviesan la vena cava inferior (T8), el esófago (T10) y la aorta (T12).")

# ============================ ABDOMEN
G = "Abdomen"
M("rectus abdominis", "Músculo recto del abdomen", G, "Cresta del pubis y sínfisis del pubis", "Cartílagos costales 5–7 y apófisis xifoides", "Flexiona el tronco y comprime las vísceras abdominales", "Nervios toracoabdominales T7–T11 y subcostal (T12)", "Músculo largo y aplanado envuelto por la vaina de los rectos; sus intersecciones tendinosas dan el aspecto de «tableta». Flexiona el tronco.")
M("pyramidalis", "Músculo piramidal del abdomen", G, "Cuerpo del pubis", "Línea alba", "Tensa la línea alba", "Nervio subcostal (T12)", "Pequeño músculo triangular, inconstante (falta en ≈20 % de las personas), situado delante del recto del abdomen.")
M("external oblique", "Músculo oblicuo externo del abdomen", G, "Caras externas de las costillas 5–12", "Línea alba, tubérculo del pubis y mitad anterior de la cresta ilíaca", "Flexiona y gira el tronco hacia el lado contrario; comprime el abdomen", "Nervios toracoabdominales T7–T11 y subcostal", "El más superficial y grande de los músculos anchos del abdomen; su borde inferior forma el ligamento inguinal.")
M("internal oblique", "Músculo oblicuo interno del abdomen", G, "Fascia toracolumbar, cresta ilíaca y dos tercios laterales del ligamento inguinal", "Costillas 10–12, línea alba y pubis (tendón conjunto)", "Flexiona y gira el tronco hacia su mismo lado; comprime el abdomen", "Nervios toracoabdominales, iliohipogástrico e ilioinguinal (T7–L1)")
M("transversus abdominis", "Músculo transverso del abdomen", G, "Cartílagos costales 7–12, fascia toracolumbar, cresta ilíaca y ligamento inguinal", "Línea alba, cresta del pubis y línea pectínea", "Comprime el contenido abdominal y estabiliza la columna lumbar", "Nervios toracoabdominales, iliohipogástrico e ilioinguinal (T7–L1)")
M("quadratus lumborum", "Músculo cuadrado lumbar", G + " (pared posterior)", "Ligamento iliolumbar y cresta ilíaca", "Duodécima costilla y apófisis transversas de L1–L4", "Inclina lateralmente el tronco y fija la duodécima costilla en la inspiración", "Ramos anteriores de T12–L4")
add("linea alba", "Línea alba", "mus", G,
    "Rafe fibroso de la línea media anterior del abdomen, desde la apófisis xifoides hasta la sínfisis del pubis, formado por el entrecruzamiento de las aponeurosis de los músculos anchos del abdomen. Contiene el ombligo.",
    [["Tipo", "Tejido conectivo denso"]])
add("inguinal ligament", "Ligamento inguinal", "mus", G,
    "Banda fibrosa que se extiende desde la espina ilíaca anterosuperior hasta el tubérculo del pubis. Es el borde inferior, engrosado, de la aponeurosis del oblicuo externo y marca el límite entre abdomen y muslo.",
    [["Inserciones", "Espina ilíaca anterosuperior → tubérculo del pubis"]])

# ============================ PELVIS / PERINÉ
G = "Pelvis: suelo pélvico"
M("pubococcygeus", "Músculo pubococcígeo", G + " (elevador del ano)", "Cuerpo del pubis y arco tendinoso del elevador del ano", "Cóccix y ligamento anococcígeo", "Sostiene las vísceras pélvicas y resiste aumentos de presión abdominal", "Nervio del elevador del ano (S4) y ramos del pudendo", "Parte del músculo elevador del ano, principal componente del diafragma pélvico.")
M("puborectalis", "Músculo puborrectal", G + " (elevador del ano)", "Cuerpo del pubis", "Forma un asa en U alrededor de la unión anorrectal", "Mantiene el ángulo anorrectal; esencial para la continencia fecal", "Nervio del elevador del ano (S4) y pudendo")
M("iliococcygeus", "Músculo iliococcígeo", G + " (elevador del ano)", "Arco tendinoso del elevador del ano y espina isquiática", "Cóccix y ligamento anococcígeo", "Sostiene las vísceras pélvicas", "Nervio del elevador del ano (S4)")
add("tendinous arch of levator ani", "Arco tendinoso del músculo elevador del ano", "mus", G,
    "Engrosamiento de la fascia del obturador interno que se extiende del pubis a la espina isquiática y da origen a parte del músculo elevador del ano.")
M("coccygeus", "Músculo coccígeo (isquiococcígeo)", G, "Espina isquiática", "Bordes laterales del cóccix y del sacro inferior", "Sostiene las vísceras pélvicas y flexiona el cóccix", "Ramos de S3–S4")
M("external anal sphincter", "Músculo esfínter externo del ano", G, "Rodea el conducto anal (fibras de piel perianal, cuerpo perineal y ligamento anococcígeo)", "Cuerpo perineal y ligamento anococcígeo", "Cierre voluntario del ano (continencia)", "Nervios rectales inferiores (del pudendo, S2–S4)", "Anillo de músculo esquelético bajo control voluntario que cierra el conducto anal.")

# ============================ MIEMBRO SUPERIOR: hombro
G = "Miembro superior: hombro"
M("clavicular part of deltoid", "Músculo deltoides — porción clavicular (anterior)", G, "Tercio lateral de la clavícula", "Tuberosidad deltoidea del húmero", "Flexiona y rota medialmente el brazo", "Nervio axilar (C5–C6)", "Porción anterior del deltoides, músculo que da forma redondeada al hombro.")
M("acromial part of deltoid", "Músculo deltoides — porción acromial (media)", G, "Borde lateral del acromion", "Tuberosidad deltoidea del húmero", "Abduce el brazo (de 15° a 90°, tras el inicio por el supraespinoso)", "Nervio axilar (C5–C6)")
M("spinal part of deltoid", "Músculo deltoides — porción espinal (posterior)", G, "Espina de la escápula", "Tuberosidad deltoidea del húmero", "Extiende y rota lateralmente el brazo", "Nervio axilar (C5–C6)")
M("supraspinatus", "Músculo supraespinoso", G + " (manguito rotador)", "Fosa supraespinosa de la escápula", "Carilla superior del tubérculo mayor del húmero", "Inicia la abducción del brazo y estabiliza la cabeza humeral", "Nervio supraescapular (C5–C6)", "Forma parte del manguito de los rotadores; su tendón es el que se lesiona con más frecuencia en el hombro.")
M("infraspinatus muscle", "Músculo infraespinoso", G + " (manguito rotador)", "Fosa infraespinosa de la escápula", "Carilla media del tubérculo mayor del húmero", "Rota lateralmente el brazo y estabiliza el hombro", "Nervio supraescapular (C5–C6)")
M("teres minor", "Músculo redondo menor", G + " (manguito rotador)", "Borde lateral de la escápula", "Carilla inferior del tubérculo mayor del húmero", "Rota lateralmente el brazo y estabiliza el hombro", "Nervio axilar (C5–C6)")
M("subscapularis", "Músculo subescapular", G + " (manguito rotador)", "Fosa subescapular (cara anterior de la escápula)", "Tubérculo menor del húmero", "Rota medialmente el brazo y estabiliza el hombro", "Nervios subescapulares superior e inferior (C5–C6)")
M("teres major", "Músculo redondo mayor", G, "Ángulo inferior de la escápula (cara posterior)", "Cresta del tubérculo menor del húmero", "Aduce, extiende y rota medialmente el brazo", "Nervio subescapular inferior (C5–C6)")

# ============================ MIEMBRO SUPERIOR: brazo
G = "Miembro superior: brazo"
MUSC = "Nervio musculocutáneo (C5–C6)"
M("long head of biceps brachii", "Músculo bíceps braquial — cabeza larga", G, "Tubérculo supraglenoideo de la escápula (tendón intraarticular)", "Tuberosidad del radio y aponeurosis bicipital", "Supina el antebrazo y flexiona el codo; colabora en la flexión del hombro", MUSC, "Cabeza lateral del bíceps braquial. Su tendón atraviesa la articulación del hombro por el surco intertubercular.")
M("short head of biceps brachii", "Músculo bíceps braquial — cabeza corta", G, "Apófisis coracoides de la escápula", "Tuberosidad del radio y aponeurosis bicipital", "Supinador potente del antebrazo y flexor del codo", MUSC)
M("coracobrachialis", "Músculo coracobraquial", G, "Apófisis coracoides de la escápula", "Tercio medio de la cara medial del húmero", "Flexiona y aduce el brazo", MUSC)
M("brachialis", "Músculo braquial", G, "Mitad distal de la cara anterior del húmero", "Apófisis coronoides y tuberosidad del cúbito", "Flexor principal del codo en cualquier posición del antebrazo", MUSC + " y ramo del nervio radial")
RAD = "Nervio radial (C6–C8)"
M("long head of triceps brachii", "Músculo tríceps braquial — cabeza larga", G, "Tubérculo infraglenoideo de la escápula", "Olécranon del cúbito", "Extiende el codo; extiende y aduce el brazo", RAD, "Cabeza del tríceps braquial, único músculo del compartimento posterior del brazo y principal extensor del codo.")
M("lateral head of triceps brachii", "Músculo tríceps braquial — cabeza lateral", G, "Cara posterior del húmero, por encima del surco del nervio radial", "Olécranon del cúbito", "Extiende el codo", RAD)
M("medial head of triceps brachii", "Músculo tríceps braquial — cabeza medial", G, "Cara posterior del húmero, por debajo del surco del nervio radial", "Olécranon del cúbito", "Extiende el codo", RAD)
M("anconeus", "Músculo ancóneo", G, "Epicóndilo lateral del húmero", "Cara lateral del olécranon", "Colabora en la extensión del codo y estabiliza la articulación", RAD)

# ============================ MIEMBRO SUPERIOR: antebrazo
G = "Miembro superior: antebrazo (anterior)"
MED = "Nervio mediano (C6–C8)"
M("humeral head of pronator teres", "Músculo pronador redondo — cabeza humeral", G, "Epicóndilo medial del húmero", "Cara lateral del radio (tercio medio)", "Prona el antebrazo y flexiona el codo", MED)
M("ulnar head of pronator teres", "Músculo pronador redondo — cabeza cubital", G, "Apófisis coronoides del cúbito", "Cara lateral del radio (tercio medio)", "Prona el antebrazo", MED, "Cabeza profunda del pronador redondo; entre ambas cabezas pasa el nervio mediano.")
M("flexor carpi radialis", "Músculo flexor radial del carpo", G, "Epicóndilo medial del húmero", "Base del segundo metacarpiano", "Flexiona y abduce la muñeca", MED)
M("palmaris longus", "Músculo palmar largo", G, "Epicóndilo medial del húmero", "Retináculo flexor y aponeurosis palmar", "Flexiona la muñeca y tensa la aponeurosis palmar", MED, "Músculo inconstante (ausente en ≈15 % de las personas); su tendón se usa con frecuencia como injerto.")
M("humeral head of flexor carpi ulnaris", "Músculo flexor cubital del carpo — cabeza humeral", G, "Epicóndilo medial del húmero", "Pisiforme, gancho del ganchoso y quinto metacarpiano", "Flexiona y aduce la muñeca", "Nervio cubital (C7–T1)")
M("ulnar head of flexor carpi ulnaris", "Músculo flexor cubital del carpo — cabeza cubital", G, "Olécranon y borde posterior del cúbito", "Pisiforme, gancho del ganchoso y quinto metacarpiano", "Flexiona y aduce la muñeca", "Nervio cubital (C7–T1)")
M("humeroulnar head of flexor digitorum superficialis", "Músculo flexor superficial de los dedos — cabeza humerocubital", G, "Epicóndilo medial del húmero y apófisis coronoides del cúbito", "Falanges medias de los dedos 2.º–5.º", "Flexiona las articulaciones interfalángicas proximales y la muñeca", MED)
M("radial head of flexor digitorum superficialis", "Músculo flexor superficial de los dedos — cabeza radial", G, "Borde anterior del radio", "Falanges medias de los dedos 2.º–5.º", "Flexiona las articulaciones interfalángicas proximales", MED)
M("flexor digitorum profundus", "Músculo flexor profundo de los dedos", G, "Caras anterior y medial del cúbito y membrana interósea", "Bases de las falanges distales de los dedos 2.º–5.º", "Único flexor de las articulaciones interfalángicas distales", "Nervio mediano (interóseo anterior; dedos 2–3) y nervio cubital (dedos 4–5)")
M("flexor pollicis longus", "Músculo flexor largo del pulgar", G, "Cara anterior del radio y membrana interósea", "Base de la falange distal del pulgar", "Flexiona el pulgar", "Nervio interóseo anterior (del mediano)")
M("pronator quadratus", "Músculo pronador cuadrado", G, "Cuarto distal de la cara anterior del cúbito", "Cuarto distal de la cara anterior del radio", "Principal pronador del antebrazo", "Nervio interóseo anterior (del mediano)")
G = "Miembro superior: antebrazo (posterior)"
M("brachioradialis", "Músculo braquiorradial", G, "Cresta supracondílea lateral del húmero", "Base de la apófisis estiloides del radio", "Flexiona el codo, sobre todo en semipronación", RAD)
M("extensor carpi radialis longus", "Músculo extensor radial largo del carpo", G, "Cresta supracondílea lateral del húmero", "Base del segundo metacarpiano (dorso)", "Extiende y abduce la muñeca", RAD)
M("extensor carpi radialis brevis", "Músculo extensor radial corto del carpo", G, "Epicóndilo lateral del húmero", "Base del tercer metacarpiano (dorso)", "Extiende y abduce la muñeca", "Nervio radial (ramo profundo)", "Su tendón de origen es el más afectado en la epicondilitis lateral («codo de tenista»).")
M("extensor digitorum", "Músculo extensor de los dedos", G, "Epicóndilo lateral del húmero", "Expansiones extensoras de los dedos 2.º–5.º", "Extiende los dedos y la muñeca", "Nervio interóseo posterior (del radial)")
M("extensor digiti minimi", "Músculo extensor del meñique", G, "Epicóndilo lateral del húmero", "Expansión extensora del quinto dedo", "Extiende el meñique", "Nervio interóseo posterior (del radial)")
M("humeral head of extensor carpi ulnaris", "Músculo extensor cubital del carpo — cabeza humeral", G, "Epicóndilo lateral del húmero", "Base del quinto metacarpiano", "Extiende y aduce la muñeca", "Nervio interóseo posterior (del radial)")
M("ulnar head of extensor carpi ulnaris", "Músculo extensor cubital del carpo — cabeza cubital", G, "Borde posterior del cúbito", "Base del quinto metacarpiano", "Extiende y aduce la muñeca", "Nervio interóseo posterior (del radial)")
M("supinator", "Músculo supinador", G, "Epicóndilo lateral, ligamentos colateral radial y anular y cresta del supinador del cúbito", "Tercio proximal del radio (caras lateral, posterior y anterior)", "Supina el antebrazo", "Nervio radial (ramo profundo)")
M("abductor pollicis longus", "Músculo abductor largo del pulgar", G, "Caras posteriores del cúbito y del radio y membrana interósea", "Base del primer metacarpiano", "Abduce y extiende el pulgar", "Nervio interóseo posterior (del radial)")
M("extensor pollicis brevis", "Músculo extensor corto del pulgar", G, "Cara posterior del radio y membrana interósea", "Base de la falange proximal del pulgar", "Extiende el pulgar en la articulación metacarpofalángica", "Nervio interóseo posterior (del radial)")
M("extensor pollicis longus", "Músculo extensor largo del pulgar", G, "Cara posterior del cúbito y membrana interósea", "Base de la falange distal del pulgar", "Extiende todas las articulaciones del pulgar", "Nervio interóseo posterior (del radial)")
M("extensor indicis", "Músculo extensor del índice", G, "Cara posterior del cúbito y membrana interósea", "Expansión extensora del índice", "Extiende el índice (señalar)", "Nervio interóseo posterior (del radial)")
add("interosseous membrane of forearm", "Membrana interósea del antebrazo", "mus", "Miembro superior: antebrazo (posterior)",
    "Lámina fibrosa que une los bordes interóseos del radio y el cúbito. Transmite fuerzas del radio al cúbito y da origen a músculos profundos del antebrazo.",
    [["Tipo", "Sindesmosis (articulación fibrosa)"]])
add("flexor retinaculum of wrist", "Retináculo flexor de la muñeca", "mus", "Miembro superior: mano",
    "Banda fibrosa que cruza la cara palmar del carpo y convierte el surco carpiano en el túnel del carpo, por donde pasan el nervio mediano y los tendones flexores. Su compresión causa el síndrome del túnel carpiano.")

# ============================ MIEMBRO SUPERIOR: mano
G = "Miembro superior: mano"
M("abductor pollicis brevis", "Músculo abductor corto del pulgar", G + " (eminencia tenar)", "Retináculo flexor, escafoides y trapecio", "Base de la falange proximal del pulgar (lado radial)", "Abduce el pulgar", "Nervio mediano (ramo recurrente)")
M("opponens pollicis", "Músculo oponente del pulgar", G + " (eminencia tenar)", "Retináculo flexor y trapecio", "Borde lateral del primer metacarpiano", "Opone el pulgar (lo lleva hacia la palma a encontrarse con los demás dedos)", "Nervio mediano (ramo recurrente)")
M("superficial head of flexor pollicis brevis", "Músculo flexor corto del pulgar — cabeza superficial", G + " (eminencia tenar)", "Retináculo flexor y trapecio", "Base de la falange proximal del pulgar", "Flexiona el pulgar en la articulación metacarpofalángica", "Nervio mediano (ramo recurrente)")
M("deep head of flexor pollicis brevis", "Músculo flexor corto del pulgar — cabeza profunda", G + " (eminencia tenar)", "Trapezoide y hueso grande", "Base de la falange proximal del pulgar", "Flexiona el pulgar", "Nervio cubital (ramo profundo)")
M("oblique head of adductor pollicis", "Músculo aductor del pulgar — cabeza oblicua", G, "Bases de los metacarpianos 2.º–3.º y hueso grande", "Base de la falange proximal del pulgar (lado cubital)", "Aduce el pulgar", "Nervio cubital (ramo profundo)")
M("transverse head of adductor pollicis", "Músculo aductor del pulgar — cabeza transversa", G, "Cara palmar del tercer metacarpiano", "Base de la falange proximal del pulgar (lado cubital)", "Aduce el pulgar (pinza lateral)", "Nervio cubital (ramo profundo)")
M("abductor digiti minimi of hand", "Músculo abductor del meñique (mano)", G + " (eminencia hipotenar)", "Pisiforme", "Base de la falange proximal del quinto dedo", "Abduce el meñique", "Nervio cubital (ramo profundo)")
M("flexor digiti minimi brevis of hand", "Músculo flexor corto del meñique (mano)", G + " (eminencia hipotenar)", "Gancho del ganchoso y retináculo flexor", "Base de la falange proximal del quinto dedo", "Flexiona el meñique", "Nervio cubital (ramo profundo)")
M("opponens digiti minimi of hand", "Músculo oponente del meñique (mano)", G + " (eminencia hipotenar)", "Gancho del ganchoso y retináculo flexor", "Borde medial del quinto metacarpiano", "Lleva el quinto metacarpiano hacia delante (oposición)", "Nervio cubital (ramo profundo)")
M("set of lumbricals of hand", "Músculos lumbricales de la mano", G, "Tendones del flexor profundo de los dedos", "Expansiones extensoras de los dedos 2.º–5.º (lado radial)", "Flexionan las metacarpofalángicas y extienden las interfalángicas", "Nervio mediano (1.º–2.º) y cubital (3.º–4.º)")
M("set of palmar interossei of hand", "Músculos interóseos palmares", G, "Caras palmares de los metacarpianos 2.º, 4.º y 5.º", "Expansiones extensoras y falanges proximales de esos dedos", "Aducen los dedos hacia el eje del dedo medio (PAD)", "Nervio cubital (ramo profundo)")
M("set of dorsal interossei of hand", "Músculos interóseos dorsales de la mano", G, "Caras adyacentes de los cinco metacarpianos (cabezas dobles)", "Falanges proximales y expansiones extensoras de los dedos 2.º–4.º", "Abducen los dedos respecto al eje del dedo medio (DAB)", "Nervio cubital (ramo profundo)")

# ============================ MIEMBRO INFERIOR: cadera / glúteo
G = "Miembro inferior: cadera y región glútea"
M("psoas major", "Músculo psoas mayor", G, "Cuerpos y apófisis transversas de T12–L5 y discos intervertebrales", "Trocánter menor del fémur (con el ilíaco)", "Flexiona el muslo en la cadera; flexiona el tronco", "Ramos anteriores de L1–L3", "Músculo largo de la pared abdominal posterior; con el ilíaco forma el iliopsoas, el flexor más potente de la cadera.")
M("iliacus", "Músculo ilíaco", G, "Fosa ilíaca", "Trocánter menor del fémur (con el psoas)", "Flexiona el muslo en la cadera", "Nervio femoral (L2–L3)")
M("gluteus maximus", "Músculo glúteo mayor", G, "Cara posterior del ilion, sacro, cóccix y ligamento sacrotuberoso", "Tracto iliotibial y tuberosidad glútea del fémur", "Extensor potente de la cadera (levantarse, subir escaleras); rotación lateral", "Nervio glúteo inferior (L5–S2)", "El músculo más voluminoso del cuerpo. Extiende la cadera y la rota lateralmente.")
M("gluteus medius", "Músculo glúteo medio", G, "Cara externa del ilion, entre las líneas glúteas anterior y posterior", "Cara lateral del trocánter mayor", "Abduce y rota medialmente el muslo; estabiliza la pelvis al caminar", "Nervio glúteo superior (L4–S1)", "Su debilidad produce el signo de Trendelenburg (caída de la pelvis del lado contrario al apoyar).")
M("gluteus minimus", "Músculo glúteo menor", G, "Cara externa del ilion, entre las líneas glúteas anterior e inferior", "Cara anterior del trocánter mayor", "Abduce y rota medialmente el muslo; estabiliza la pelvis", "Nervio glúteo superior (L4–S1)")
M("tensor fasciae latae", "Músculo tensor de la fascia lata", G, "Espina ilíaca anterosuperior", "Tracto iliotibial", "Abduce, flexiona y rota medialmente el muslo; estabiliza la rodilla en extensión", "Nervio glúteo superior (L4–S1)")
add("iliotibial tract", "Tracto iliotibial", "mus", G,
    "Engrosamiento lateral de la fascia lata que se extiende desde la cresta ilíaca hasta el cóndilo lateral de la tibia (tubérculo de Gerdy). Recibe al tensor de la fascia lata y al glúteo mayor y estabiliza la cadera y la rodilla.")
M("piriformis", "Músculo piriforme", G + " (rotadores laterales)", "Cara anterior del sacro", "Borde superior del trocánter mayor", "Rota lateralmente el muslo extendido; lo abduce en flexión", "Nervio del piriforme (S1–S2)", "Referencia clave de la región glútea: el nervio ciático suele salir de la pelvis por debajo de él.")
M("gemellus superior", "Músculo gemelo superior (de la cadera)", G + " (rotadores laterales)", "Espina isquiática", "Trocánter mayor (con el tendón del obturador interno)", "Rota lateralmente el muslo", "Nervio del obturador interno (L5–S1)")
M("gemellus inferior", "Músculo gemelo inferior (de la cadera)", G + " (rotadores laterales)", "Tuberosidad isquiática", "Trocánter mayor (con el tendón del obturador interno)", "Rota lateralmente el muslo", "Nervio del cuadrado femoral (L5–S1)")
M("obturator internus", "Músculo obturador interno", G + " (rotadores laterales)", "Cara interna de la membrana obturatriz y huesos que la rodean", "Cara medial del trocánter mayor", "Rota lateralmente el muslo y estabiliza la cadera", "Nervio del obturador interno (L5–S1)")
M("obturator externus", "Músculo obturador externo", G + " (rotadores laterales)", "Cara externa de la membrana obturatriz", "Fosa trocantérea del fémur", "Rota lateralmente el muslo", "Nervio obturador (L3–L4)")
M("quadratus femoris", "Músculo cuadrado femoral", G + " (rotadores laterales)", "Tuberosidad isquiática", "Cresta intertrocantérea del fémur", "Rota lateralmente el muslo", "Nervio del cuadrado femoral (L5–S1)")

# ============================ MUSLO
G = "Miembro inferior: muslo (anterior)"
FEM = "Nervio femoral (L2–L4)"
M("sartorius", "Músculo sartorio", G, "Espina ilíaca anterosuperior", "Cara medial de la parte superior de la tibia (pata de ganso)", "Flexiona, abduce y rota lateralmente la cadera; flexiona la rodilla (posición de sastre)", FEM, "El músculo más largo del cuerpo. Cruza el muslo en diagonal y actúa sobre cadera y rodilla.")
M("rectus femoris", "Músculo recto femoral", G + " (cuádriceps)", "Espina ilíaca anteroinferior y borde superior del acetábulo", "Tuberosidad de la tibia por el tendón rotuliano", "Extiende la rodilla y flexiona la cadera", FEM, "Única cabeza del cuádriceps que cruza la cadera. Extiende la rodilla y flexiona la cadera.")
M("vastus lateralis", "Músculo vasto lateral", G + " (cuádriceps)", "Trocánter mayor y labio lateral de la línea áspera", "Tuberosidad de la tibia por el tendón rotuliano", "Extiende la rodilla", FEM, "La cabeza más voluminosa del cuádriceps.")
M("vastus medialis", "Músculo vasto medial", G + " (cuádriceps)", "Línea intertrocantérea y labio medial de la línea áspera", "Tuberosidad de la tibia por el tendón rotuliano", "Extiende la rodilla; sus fibras oblicuas estabilizan la rótula", FEM)
M("vastus intermedius", "Músculo vasto intermedio", G + " (cuádriceps)", "Caras anterior y lateral de la diáfisis del fémur", "Tuberosidad de la tibia por el tendón rotuliano", "Extiende la rodilla", FEM)
G = "Miembro inferior: muslo (medial)"
OBT = "Nervio obturador (L2–L4)"
M("pectineus", "Músculo pectíneo", G, "Línea pectínea del pubis", "Línea pectínea del fémur", "Aduce y flexiona el muslo", "Nervio femoral (a veces también obturador)")
M("adductor longus", "Músculo aductor largo", G, "Cuerpo del pubis, por debajo de la cresta", "Tercio medio de la línea áspera", "Aduce el muslo", OBT)
M("adductor brevis", "Músculo aductor corto", G, "Cuerpo y rama inferior del pubis", "Parte proximal de la línea áspera", "Aduce el muslo", OBT)
M("adductor magnus", "Músculo aductor mayor", G, "Rama isquiopubiana y tuberosidad isquiática", "Línea áspera y tubérculo del aductor del fémur", "Aduce el muslo; su porción isquiática extiende la cadera", OBT + " y porción tibial del ciático", "El más grande de los aductores; entre sus inserciones deja el hiato aductor por donde pasan los vasos femorales hacia la fosa poplítea.")
M("adductor minimus", "Músculo aductor mínimo", G, "Rama inferior del pubis", "Parte proximal de la línea áspera", "Aduce y rota lateralmente el muslo", OBT, "Porción superior, a menudo separada, del aductor mayor.")
M("gracilis", "Músculo grácil", G, "Cuerpo y rama inferior del pubis", "Cara medial de la parte superior de la tibia (pata de ganso)", "Aduce el muslo y flexiona la rodilla", OBT)
G = "Miembro inferior: muslo (posterior, isquiotibiales)"
M("long head of biceps femoris", "Músculo bíceps femoral — cabeza larga", G, "Tuberosidad isquiática", "Cabeza del peroné", "Flexiona la rodilla y extiende la cadera; rota lateralmente la pierna", "Nervio ciático, porción tibial (L5–S2)")
M("short head of biceps femoris", "Músculo bíceps femoral — cabeza corta", G, "Labio lateral de la línea áspera", "Cabeza del peroné", "Flexiona la rodilla y rota lateralmente la pierna", "Nervio ciático, porción fibular común (L5–S2)")
M("semitendinosus", "Músculo semitendinoso", G, "Tuberosidad isquiática", "Cara medial de la parte superior de la tibia (pata de ganso)", "Flexiona la rodilla, extiende la cadera y rota medialmente la pierna", "Nervio ciático, porción tibial (L5–S2)")
M("semimembranosus", "Músculo semimembranoso", G, "Tuberosidad isquiática", "Cóndilo medial de la tibia (cara posterior)", "Flexiona la rodilla, extiende la cadera y rota medialmente la pierna", "Nervio ciático, porción tibial (L5–S2)")

# ============================ PIERNA
G = "Miembro inferior: pierna (anterior)"
FP = "Nervio fibular profundo (L4–L5)"
M("tibialis anterior", "Músculo tibial anterior", G, "Cóndilo lateral y mitad superior de la cara lateral de la tibia", "Cuneiforme medial y base del primer metatarsiano", "Flexión dorsal e inversión del pie", FP, "Su parálisis provoca el «pie caído». Flexiona dorsalmente e invierte el pie.")
M("extensor hallucis longus", "Músculo extensor largo del dedo gordo", G, "Cara medial del peroné y membrana interósea", "Base de la falange distal del dedo gordo", "Extiende el dedo gordo y flexiona dorsalmente el pie", FP)
M("extensor digitorum longus", "Músculo extensor largo de los dedos", G, "Cóndilo lateral de la tibia, peroné y membrana interósea", "Falanges media y distal de los dedos 2.º–5.º", "Extiende los dedos y flexiona dorsalmente el pie", FP)
M("fibularis tertius", "Músculo fibular tercero", G, "Tercio distal del peroné", "Base del quinto metatarsiano (dorso)", "Flexión dorsal y eversión del pie", FP)
G = "Miembro inferior: pierna (lateral)"
M("fibularis longus", "Músculo fibular largo (peroneo largo)", G, "Cabeza y dos tercios superiores de la cara lateral del peroné", "Base del primer metatarsiano y cuneiforme medial (cruzando la planta)", "Evierte el pie, colabora en la flexión plantar y sostiene el arco transversal", "Nervio fibular superficial (L5–S1)")
M("fibularis brevis", "Músculo fibular corto (peroneo corto)", G, "Dos tercios inferiores de la cara lateral del peroné", "Tuberosidad del quinto metatarsiano", "Evierte el pie", "Nervio fibular superficial (L5–S1)")
G = "Miembro inferior: pierna (posterior)"
TIB = "Nervio tibial (S1–S2)"
M("medial head of gastrocnemius", "Músculo gastrocnemio — cabeza medial", G + " (tríceps sural)", "Cara poplítea del fémur, por encima del cóndilo medial", "Tuberosidad del calcáneo por el tendón calcáneo", "Flexión plantar del pie y flexión de la rodilla", TIB, "Cabeza medial de los «gemelos», que forman el relieve de la pantorrilla.")
M("lateral head of gastrocnemius", "Músculo gastrocnemio — cabeza lateral", G + " (tríceps sural)", "Cara lateral del cóndilo lateral del fémur", "Tuberosidad del calcáneo por el tendón calcáneo", "Flexión plantar del pie y flexión de la rodilla", TIB)
M("soleus", "Músculo sóleo", G + " (tríceps sural)", "Cabeza y cara posterior del peroné y línea del sóleo de la tibia", "Tuberosidad del calcáneo por el tendón calcáneo", "Flexión plantar del pie; clave en la bipedestación", TIB, "Músculo ancho y plano bajo el gastrocnemio. Su contracción impulsa la sangre venosa hacia el corazón («bomba muscular»).")
add("calcaneal tendon", "Tendón calcáneo (de Aquiles)", "mus", G + " (tríceps sural)",
    "Tendón común del gastrocnemio y el sóleo, el más grueso y resistente del cuerpo. Se inserta en la tuberosidad del calcáneo y transmite la fuerza de la flexión plantar.",
    [["Longitud", "≈15 cm"], ["Clínica", "Rotura por esfuerzo; reflejo aquíleo (S1)"]])
M("plantaris", "Músculo plantar", G, "Línea supracondílea lateral del fémur", "Tuberosidad del calcáneo (medial al tendón calcáneo)", "Débil flexión plantar y de la rodilla", TIB, "Músculo pequeño con un tendón muy largo y fino; inconstante.")
M("popliteus", "Músculo poplíteo", G, "Cóndilo lateral del fémur y menisco lateral", "Cara posterior de la tibia, por encima de la línea del sóleo", "«Desbloquea» la rodilla extendida rotando el fémur lateralmente", TIB)
M("tibialis posterior", "Músculo tibial posterior", G, "Membrana interósea y caras posteriores de tibia y peroné", "Tuberosidad del navicular, cuneiformes, cuboides y bases de metatarsianos 2–4", "Inversión y flexión plantar del pie; sostiene el arco longitudinal medial", TIB)
M("flexor digitorum longus", "Músculo flexor largo de los dedos", G, "Cara posterior de la tibia", "Bases de las falanges distales de los dedos 2.º–5.º", "Flexiona los dedos 2.º–5.º y colabora en la flexión plantar", TIB)
M("flexor hallucis longus", "Músculo flexor largo del dedo gordo", G, "Dos tercios inferiores de la cara posterior del peroné", "Base de la falange distal del dedo gordo", "Flexiona el dedo gordo (despegue en la marcha)", TIB)
add("interosseous membrane of leg", "Membrana interósea de la pierna", "mus", G,
    "Lámina fibrosa que une los bordes interóseos de la tibia y el peroné. Separa los compartimentos anterior y posterior de la pierna y da origen a músculos.")

# ============================ PIE
G = "Miembro inferior: pie"
PM = "Nervio plantar medial (S2–S3)"; PL = "Nervio plantar lateral (S2–S3)"
M("extensor digitorum brevis", "Músculo extensor corto de los dedos", G + " (dorso)", "Cara superolateral del calcáneo", "Tendones del extensor largo de los dedos 2.º–4.º", "Extiende los dedos 2.º–4.º", FP)
M("extensor hallucis brevis", "Músculo extensor corto del dedo gordo", G + " (dorso)", "Cara superolateral del calcáneo", "Base de la falange proximal del dedo gordo", "Extiende el dedo gordo", FP)
M("abductor hallucis", "Músculo abductor del dedo gordo", G + " (planta, 1.ª capa)", "Tuberosidad del calcáneo (proceso medial)", "Base de la falange proximal del dedo gordo (medial)", "Abduce y flexiona el dedo gordo; sostiene el arco medial", PM)
M("flexor digitorum brevis", "Músculo flexor corto de los dedos", G + " (planta, 1.ª capa)", "Tuberosidad del calcáneo y aponeurosis plantar", "Falanges medias de los dedos 2.º–5.º", "Flexiona los dedos 2.º–5.º", PM)
M("abductor digiti minimi of foot", "Músculo abductor del quinto dedo (pie)", G + " (planta, 1.ª capa)", "Tuberosidad del calcáneo", "Base de la falange proximal del quinto dedo", "Abduce y flexiona el quinto dedo", PL)
M("flexor accessorius", "Músculo cuadrado plantar (flexor accesorio)", G + " (planta, 2.ª capa)", "Caras medial y lateral del calcáneo", "Borde lateral del tendón del flexor largo de los dedos", "Corrige la tracción oblicua del flexor largo de los dedos", PL)
for i in range(4):
    inv = PM if i==0 else PL
    M(f"{ORD[i]} lumbrical of foot", f"{['Primer','Segundo','Tercer','Cuarto'][i]} músculo lumbrical del pie", G + " (planta, 2.ª capa)", "Tendones del flexor largo de los dedos", f"Expansión extensora del {['segundo','tercer','cuarto','quinto'][i]} dedo", "Flexiona la metatarsofalángica y extiende las interfalángicas", inv)
M("medial head of flexor hallucis brevis", "Músculo flexor corto del dedo gordo — cabeza medial", G + " (planta, 3.ª capa)", "Cuboides y cuneiforme lateral", "Base de la falange proximal del dedo gordo (lado medial)", "Flexiona el dedo gordo en la metatarsofalángica", PM)
M("lateral head of flexor hallucis brevis", "Músculo flexor corto del dedo gordo — cabeza lateral", G + " (planta, 3.ª capa)", "Cuboides y cuneiforme lateral", "Base de la falange proximal del dedo gordo (lado lateral)", "Flexiona el dedo gordo en la metatarsofalángica", PM)
M("oblique head of adductor hallucis", "Músculo aductor del dedo gordo — cabeza oblicua", G + " (planta, 3.ª capa)", "Bases de los metatarsianos 2.º–4.º", "Base de la falange proximal del dedo gordo (lado lateral)", "Aduce el dedo gordo; sostiene el arco transversal", PL)
M("transverse head of adductor hallucis", "Músculo aductor del dedo gordo — cabeza transversa", G + " (planta, 3.ª capa)", "Ligamentos plantares de las metatarsofalángicas 3.ª–5.ª", "Base de la falange proximal del dedo gordo (lado lateral)", "Aduce el dedo gordo; sostiene el arco transversal", PL)
M("flexor digiti minimi brevis of foot", "Músculo flexor corto del quinto dedo (pie)", G + " (planta, 3.ª capa)", "Base del quinto metatarsiano", "Base de la falange proximal del quinto dedo", "Flexiona el quinto dedo", PL)
M("opponens digiti minimi of foot", "Músculo oponente del quinto dedo (pie)", G + " (planta, 3.ª capa)", "Vaina del fibular largo y base del quinto metatarsiano", "Borde lateral del quinto metatarsiano", "Tracciona el quinto metatarsiano (inconstante)", PL)
for i in range(3):
    M(f"{ORD[i]} plantar interosseous of foot", f"{['Primer','Segundo','Tercer'][i]} músculo interóseo plantar", G + " (planta, 4.ª capa)", f"Cara medial del {['tercer','cuarto','quinto'][i]} metatarsiano", f"Base de la falange proximal del {['tercer','cuarto','quinto'][i]} dedo (lado medial)", "Aduce el dedo hacia el eje del segundo dedo", PL)
M("set of dorsal interossei of foot", "Músculos interóseos dorsales del pie", G + " (planta, 4.ª capa)", "Caras adyacentes de los metatarsianos (cabezas dobles)", "Falanges proximales de los dedos 2.º–4.º", "Abducen los dedos respecto al eje del segundo dedo", PL)
add("long plantar ligament", "Ligamento plantar largo", "mus", G,
    "El ligamento más largo de la planta del pie: va de la cara plantar del calcáneo al cuboides y a las bases de los metatarsianos 2.º–5.º. Mantiene el arco longitudinal lateral.")
