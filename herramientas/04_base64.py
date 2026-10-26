"""Paso 4 (humano): GLB comprimidos -> texto base64 (models/*.txt), el formato que publica el visor.
El empaquetado final los convierte en models/*.js para que funcionen sin servidor."""
import base64, glob, sys
for f in glob.glob((sys.argv[1] if len(sys.argv) > 1 else 'site/models') + '/*.glb'):
    open(f[:-4] + '.txt', 'wb').write(base64.b64encode(open(f, 'rb').read())); print(f)
