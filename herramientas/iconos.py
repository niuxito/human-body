"""Genera los iconos y la imagen para compartir en estilo pixel art (la línea visual de alexisparron.com).
Uso (desde esta carpeta):  python3 iconos.py ..
Salida en la carpeta indicada: favicon.svg, favicon.ico, apple-touch-icon.png, icon-192.png, icon-512.png, og-image.png.
Dependencia: Pillow."""
import struct, sys, io
from PIL import Image, ImageDraw

BG, PAPER, YELLOW, GREY = '#252525', '#f5f3ee', '#f2ca50', '#b9b6ae'
# Figura 5×5: Y = amarillo (cabeza y órgano), W = papel
FIGURE = ['..Y..',
          'WWWWW',
          '.WYW.',
          '.W.W.',
          '.W.W.']
COLOR = {'W': PAPER, 'Y': YELLOW}

def layout(size, fill=None):
    """Lado de celda y hueco enteros para que la figura quede nítida y centrada en `size` px."""
    fill = fill or (0.9 if size <= 48 else 0.82)
    best = None
    for c in range(size, 0, -1):
        g = max(1, round(c / 2)) if size > 20 else 1
        w = 5 * c + 4 * g
        if w <= size * fill:
            if (size - w) % 2 == 0: return c, g, (size - w) // 2
            best = best or (c, g, (size - w) // 2)
    return best

def figure(d, c, g, ox, oy):
    for r, row in enumerate(FIGURE):
        for k, ch in enumerate(row):
            if ch in COLOR:
                x, y = ox + k * (c + g), oy + r * (c + g)
                d.rectangle([x, y, x + c - 1, y + c - 1], fill=COLOR[ch])

def icon(size):
    im = Image.new('RGB', (size, size), BG); c, g, o = layout(size)
    figure(ImageDraw.Draw(im), c, g, o, o); return im

def png_bytes(im):
    b = io.BytesIO(); im.save(b, 'PNG', optimize=True); return b.getvalue()

def ico(sizes):
    """ICO con una imagen PNG nítida por tamaño (sin reescalar)."""
    imgs = [png_bytes(icon(s)) for s in sizes]
    head = struct.pack('<HHH', 0, 1, len(sizes)); off = 6 + 16 * len(sizes); ent = b''
    for s, data in zip(sizes, imgs):
        ent += struct.pack('<BBBBHHII', s, s, 0, 0, 1, 32, len(data), off); off += len(data)
    return head + ent + b''.join(imgs)

def svg():
    cells = {'W': [], 'Y': []}
    for r, row in enumerate(FIGURE):
        for k, ch in enumerate(row):
            if ch in cells: cells[ch].append(f'M{6 + k * 12} {6 + r * 12}h8v8h-8z')
    return ('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64"><rect width="64" height="64" rx="8" fill="%s"/>'
            '<g fill="%s"><path d="%s"/></g><g fill="%s"><path d="%s"/></g></svg>\n'
            % (BG, PAPER, ''.join(cells['W']), YELLOW, ''.join(cells['Y'])))

# Fuente pixel 5×7 mínima (solo lo necesario para la imagen para compartir)
G = {
'A':['.###.','#...#','#...#','#####','#...#','#...#','#...#'], 'B':['####.','#...#','#...#','####.','#...#','#...#','####.'],
'C':['.####','#....','#....','#....','#....','#....','.####'], 'D':['####.','#...#','#...#','#...#','#...#','#...#','####.'],
'E':['#####','#....','#....','####.','#....','#....','#####'], 'G':['.####','#....','#....','#.###','#...#','#...#','.####'],
'H':['#...#','#...#','#...#','#####','#...#','#...#','#...#'], 'I':['#####','..#..','..#..','..#..','..#..','..#..','#####'],
'L':['#....','#....','#....','#....','#....','#....','#####'], 'M':['#...#','##.##','#.#.#','#.#.#','#...#','#...#','#...#'],
'N':['#...#','##..#','#.#.#','#..##','#...#','#...#','#...#'], 'O':['.###.','#...#','#...#','#...#','#...#','#...#','.###.'],
'P':['####.','#...#','#...#','####.','#....','#....','#....'], 'R':['####.','#...#','#...#','####.','#.#..','#..#.','#...#'],
'S':['.####','#....','#....','.###.','....#','....#','####.'], 'T':['#####','..#..','..#..','..#..','..#..','..#..','..#..'],
'U':['#...#','#...#','#...#','#...#','#...#','#...#','.###.'], 'X':['#...#','#...#','.#.#.','..#..','.#.#.','#...#','#...#'],
'Y':['#...#','#...#','.#.#.','..#..','..#..','..#..','..#..'], 'W':['#...#','#...#','#...#','#.#.#','#.#.#','##.##','#...#'],
'3':['####.','....#','....#','.###.','....#','....#','####.'], '.':['.....','.....','.....','.....','.....','.....','..#..'],
'-':['.....','.....','.....','.###.','.....','.....','.....'], ' ':['.....']*7,
}

def text(d, s, x, y, scale, color):
    for ch in s:
        for r, row in enumerate(G[ch]):
            for k, v in enumerate(row):
                if v == '#': d.rectangle([x + k * scale, y + r * scale, x + (k + 1) * scale - 1, y + (r + 1) * scale - 1], fill=color)
        x += 6 * scale

def og():
    im = Image.new('RGB', (1200, 630), BG); d = ImageDraw.Draw(im)
    text(d, 'ATLAS 3D DEL CUERPO HUMANO', 90, 120, 4, YELLOW)
    text(d, 'ANATOMIA', 90, 190, 12, PAPER)
    text(d, 'EN CAPAS', 90, 310, 12, PAPER)
    text(d, 'LAYERED HUMAN ANATOMY', 90, 460, 4, GREY)
    text(d, 'ANATOMIA.ALEXISPARRON.COM', 90, 510, 4, GREY)
    figure(d, 48, 24, 774, 147)
    return im

if __name__ == '__main__':
    out = (sys.argv[1] if len(sys.argv) > 1 else '..').rstrip('/') + '/'
    open(out + 'favicon.svg', 'w').write(svg())
    open(out + 'favicon.ico', 'wb').write(ico([16, 32, 48]))
    for name, s in [('apple-touch-icon.png', 180), ('icon-192.png', 192), ('icon-512.png', 512)]:
        open(out + name, 'wb').write(png_bytes(icon(s)))
    open(out + 'og-image.png', 'wb').write(png_bytes(og()))
    print('Generados en', out)
