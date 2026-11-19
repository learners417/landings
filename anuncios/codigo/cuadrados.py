# Arma las tarjetas cuadradas (1080x1080) de los carruseles v8 a partir de las 4:5.
# Uso: python3 build_sq.py [nombre ...]
import sys, os
import numpy as np
from PIL import Image, ImageDraw

SRC = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'v8')
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'out')
os.makedirs(OUT, exist_ok=True)
W = H = 1080


def load(n):
    return Image.open(os.path.join(SRC, n + '.png')).convert('RGB')


def remove_rows(im, cuts):
    """Quita filas [a, b) de la imagen (todo el ancho)."""
    arr = np.asarray(im)
    keep = np.ones(arr.shape[0], bool)
    for a, b in cuts:
        keep[a:b] = False
    return Image.fromarray(arr[keep].copy())


def map_y(y, cuts):
    """Dónde queda la fila y después de quitar los cortes."""
    return y - sum(min(max(y - a, 0), b - a) for a, b in cuts)


def bgcolor(im, box=(0, 0, 60, 60)):
    a = np.asarray(im.crop(box)).reshape(-1, 3).astype(float)
    return tuple(int(round(v)) for v in a.mean(0))


def fit_flat(im, bg, y0, y1, x0=90, x1=1000, top=64, bottom=64, left=96, smax=1.0, center_x=False):
    """Recorta el contenido [x0,x1)x[y0,y1), lo escala para que entre en el cuadrado
    con los márgenes dados y lo pega sobre el color de fondo."""
    content = im.crop((x0, y0, x1, y1))
    ch = y1 - y0
    s = min(smax, (H - top - bottom) / ch)
    if s != 1.0:
        content = content.resize((round((x1 - x0) * s), round(ch * s)), Image.LANCZOS)
    canvas = Image.new('RGB', (W, H), bg)
    used = content.size[1]
    ytop = top + ((H - top - bottom) - used) // 2
    if center_x:
        xdst = (W - content.size[0]) // 2
    else:
        xdst = round(left + (x0 - 96) * s)
    canvas.paste(content, (xdst, ytop))
    return canvas, s, ytop, xdst


def save(im, name):
    assert im.size == (W, H), (name, im.size)
    im.save(os.path.join(OUT, name + '.png'))
    print('ok', name, im.size)


# ---------------------------------------------------------------- 4 personas (f-4, h-4, a-3)
SEPS = [596, 735, 873, 1012, 1150]
SEP_COLOR = (129, 144, 148)


def cuatro(name):
    im = load(name)
    bg = bgcolor(im)
    arr = np.asarray(im).copy()
    for y in SEPS:                       # se borran y se vuelven a trazar a todo el ancho
        arr[y, :] = bg
    im = Image.fromarray(arr)
    title_end = 225 if name == 'f-4' else 242
    cuts = []
    if title_end < 242:                  # título -> bajada: 24 px
        cuts.append((title_end + 1 + 24, 266))
    cuts.append((380, 404))              # bajada -> «4 personas»: de 64 a 40
    for c in [(600, 606), (660, 666), (722, 727),
              (740, 746), (807, 811), (860, 865),
              (878, 884), (937, 943), (1000, 1004),
              (1016, 1022), (1076, 1082), (1138, 1142)]:
        cuts.append(c)                   # aire dentro de cada ítem
    cuts.append((1165, 1182))            # último separador -> «Y atender…»: de 61 a 44
    im2 = remove_rows(im, cuts)
    y0, y1 = 86, map_y(1276, cuts)
    out, s, ytop, xdst = fit_flat(im2, bg, y0, y1, x0=90, x1=1000, top=58, bottom=58)
    d = ImageDraw.Draw(out)
    for y in SEPS:
        yo = round(ytop + (map_y(y, cuts) - y0) * s)
        d.line([(96, yo), (983, yo)], fill=SEP_COLOR, width=1)
    print(name, 'escala', round(s, 3))
    save(out, name)


# ---------------------------------------------------------------- a-2 (agenda hasta mayo)
def a2():
    im = load('a-2')
    bg = bgcolor(im)
    cuts = [
        (410, 424),            # «Lo lograste.» -> meses: de 54 a 40
        (590, 640),            # dos franjas de las barras (25 px cada una)
        (770, 878),            # barras -> separador: de 158 a 50
        (918, 928),            # separador -> pregunta: de 44 a 34
        (1092, 1106),          # pregunta -> respuesta: de 44 a 30
    ]
    im2 = remove_rows(im, cuts)
    out, s, *_ = fit_flat(im2, bg, 108, map_y(1244, cuts), x0=90, x1=1000, top=62, bottom=66)
    print('a-2 escala', round(s, 3))
    save(out, 'a-2')


# ---------------------------------------------------------------- s-5 (Entonces pruebas lo de siempre)
def mountain_f5(im, bg):
    """La montaña de abajo sin el texto encima (la punta se vuelve a dibujar)."""
    arr = np.asarray(im).astype(np.float64).copy()
    snow = arr[1100:1104, 520:560].reshape(-1, 3).mean(0)
    apex_x, apex_y, slope = 540.1, 1057.1, 1.767
    ss = 4                                   # supermuestreo para bordes suaves
    for y in range(1036, 1105):
        for x in range(380, 700):
            inside = 0
            for sy in range(ss):
                yy = y + (sy + 0.5) / ss
                half = (yy - apex_y) * slope
                for sx in range(ss):
                    xx = x + (sx + 0.5) / ss
                    if half > 0 and abs(xx - apex_x) <= half:
                        inside += 1
            f = inside / (ss * ss)
            arr[y, x] = f * snow + (1 - f) * np.array(bg)
        # fuera de la ventana de la punta, la fila es fondo
        arr[y, :380] = bg
        arr[y, 700:] = bg
    return Image.fromarray(arr.round().clip(0, 255).astype(np.uint8))



def text_only_f5(im, bg):
    """Filas del texto que pisan la punta: el texto queda sobre el fondo, sin la montaña."""
    arr = np.asarray(im).astype(np.float64).copy()
    snow = arr[1100:1104, 520:560].reshape(-1, 3).mean(0)
    txt = np.array([243.0, 236.0, 223.0])
    bgv = np.array(bg, float)
    apex_x, apex_y, slope = 540.1, 1057.1, 1.767
    for y in range(1036, 1105):
        for x in range(380, 720):
            half = (y + 0.5 - apex_y) * slope
            under = snow if (half > 0 and abs(x + 0.5 - apex_x) <= half) else bgv
            p = arr[y, x]
            den = txt[2] - under[2]
            al = 0.0 if abs(den) < 1 else min(1.0, max(0.0, (p[2] - under[2]) / den))
            arr[y, x] = al * txt + (1 - al) * bgv
    return Image.fromarray(arr.round().clip(0, 255).astype(np.uint8))

def s5():
    im = load('f-5')
    bg = bgcolor(im)
    clean = mountain_f5(im, bg)
    foot = clean.crop((0, 1040, 1080, 1336))          # punta con aire + la tierra (recortada abajo)
    texto_cuts = [(170, 186), (650, 716), (770, 778)]  # aire: «Entonces»->lista, lista->separador, separador->«Cada uno»
    t = remove_rows(text_only_f5(im, bg), texto_cuts)
    ty0, ty1 = 106, map_y(1099, texto_cuts)
    text = t.crop((90, ty0, 1000, ty1))
    top, gap = 62, 34
    foot_h = 190
    avail = H - top - gap - foot_h
    s = min(1.0, avail / text.size[1])
    text = text.resize((round(text.size[0] * s), round(text.size[1] * s)), Image.LANCZOS)
    canvas = Image.new('RGB', (W, H), bg)
    canvas.paste(text, (round(96 + (90 - 96) * s), top))
    foot = foot.resize((W, foot_h), Image.LANCZOS)     # la montaña, más baja (mismo ancho)
    canvas.paste(foot, (0, H - foot_h))
    print('s-5 escala texto', round(s, 3), 'montaña', round(foot_h / 296, 3))
    save(canvas, 's-5')


# ---------------------------------------------------------------- s-6 (los 5 sistemas)
def s6(center=True):
    im = load('f-6')
    bg = bgcolor(im)
    cuts = [(300, 311), (1010, 1038), (1160, 1167)]
    im2 = remove_rows(im, cuts)
    out, s, *_ = fit_flat(im2, bg, 70, map_y(1290, cuts), x0=86, x1=994, top=56, bottom=56, center_x=center)
    print('s-6 escala', round(s, 3))
    save(out, 's-6')


# ---------------------------------------------------------------- s-8 (video y agenda)
def s8():
    im = load('f-8')
    bg = bgcolor(im)
    arr = np.asarray(im).copy()
    # «acá abajo.» pasa al final de la primera línea
    aca = im.crop((90, 1200, 300, 1250))
    line1_right = 812
    arr[1196:1350, :] = bg                 # se borra «acá abajo.» y la montaña
    im = Image.fromarray(arr)
    space = 13
    im.paste(aca, (line1_right + space - 6, 1153 - (1206 - 1200) - 0))
    cuts = [(1010, 1035)]                  # tarjeta de agenda -> «Me quedan…»: de 75 a 50
    im2 = remove_rows(im, cuts)
    out, s, *_ = fit_flat(im2, bg, 74, map_y(1196, cuts), x0=86, x1=1040, top=56, bottom=60, left=150)
    print('s-8 escala', round(s, 3))
    save(out, 's-8')


# ---------------------------------------------------------------- celulares
def f1():
    im = load('f-1')
    cuts = [(0, 34), (392, 446), (566, 592), (652, 670), (844, 862), (896, 904),
            (994, 1006), (1084, 1096), (1100, 1180), (1342, 1350)]
    out = remove_rows(im, cuts)
    save(out, 'f-1')


def remove_rows_strips(im, strips):
    """Cortes distintos por franja vertical (cada franja pierde la misma cantidad de filas)."""
    parts = []
    for x0, x1, cuts in strips:
        parts.append(np.asarray(remove_rows(im.crop((x0, 0, x1, im.size[1])), cuts)))
    hs = {p.shape[0] for p in parts}
    assert len(hs) == 1, hs
    return Image.fromarray(np.concatenate(parts, axis=1))


def f2():
    im = load('f-2')
    # el celular pierde el «Hoy»; la franja de la derecha pierde fondo liso más arriba,
    # así la sombra diagonal queda entera
    save(remove_rows_strips(im, [
        (0, 942, [(0, 45), (362, 452), (1215, 1350)]),
        (942, W, [(0, 45), (200, 290), (1215, 1350)]),
    ]), 'f-2')


def f3():
    im = load('f-3')
    cuts = [(0, 222), (606, 616), (962, 1000)]
    save(remove_rows(im, cuts), 'f-3')


def h1():
    im = load('h-1')
    bg = bgcolor(im, (0, 300, 120, 400))
    arr = np.asarray(im).copy()
    circ = arr[86:190, 24:128].copy()
    arr[86:190, 24:128] = bg               # la luna se borra y se vuelve a poner después
    im = Image.fromarray(arr)
    cuts = [(0, 30), (156, 180), (308, 402), (848, 930), (994, 1008), (1324, 1350)]
    out = remove_rows(im, cuts)
    out.paste(Image.fromarray(circ), (24, map_y(86, cuts)))
    save(out, 'h-1')


def h2():
    im = load('h-2')
    cuts = [(0, 180), (270, 272), (469, 471), (547, 549), (745, 747), (823, 825),
            (1004, 1016), (1282, 1350)]
    save(remove_rows(im, cuts), 'h-2')


def h3():
    im = load('h-3')
    phone = im.crop((0, 125, W, 1010))                 # sin la barra de «Iván»
    band = im.crop((0, 1010, W, 1350))
    band = remove_rows(band, [(4, 18), (321, 340)])     # aire de la franja crema
    ph_h = H - band.size[1]
    k = ph_h / phone.size[1]
    ph = phone.resize((round(W * k), ph_h), Image.LANCZOS)
    canvas = Image.new('RGB', (W, H))
    xo = (W - ph.size[0]) // 2
    canvas.paste(ph, (xo, 0))
    a = np.asarray(canvas).copy()
    a[:ph_h, :xo] = a[:ph_h, xo:xo + 1]                 # el fondo se estira a los costados
    a[:ph_h, xo + ph.size[0]:] = a[:ph_h, xo + ph.size[0] - 1:xo + ph.size[0]]
    canvas = Image.fromarray(a)
    canvas.paste(band, (0, ph_h))
    print('h-3 escala celular', round(k, 3))
    save(canvas, 'h-3')


# ---------------------------------------------------------------- fotos
def a1():
    im = load('a-1')
    save(im.crop((0, 35, W, 35 + H)), 'a-1')


def s7():
    im = load('f-7')
    bg = bgcolor(im)
    photo = im.crop((90, 68, 990, 766))                 # el arco con la foto (abajo se corta)
    rest = im.crop((90, 915, 990, 1296))                # «Soy Javo Katz.», texto y libros
    k = 0.9
    photo = photo.resize((round(photo.size[0] * k), round(photo.size[1] * k)), Image.LANCZOS)
    rest = rest.resize((round(rest.size[0] * k), round(rest.size[1] * k)), Image.LANCZOS)
    top, gap = 34, 30
    canvas = Image.new('RGB', (W, H), bg)
    x = (W - photo.size[0]) // 2
    canvas.paste(photo, (x, top))
    canvas.paste(rest, (x, top + photo.size[1] + gap))
    print('s-7 alto usado', top + photo.size[1] + gap + rest.size[1])
    save(canvas, 's-7')


TODOS = {
    'f-1': f1, 'f-2': f2, 'f-3': f3, 'f-4': lambda: cuatro('f-4'),
    'h-1': h1, 'h-2': h2, 'h-3': h3, 'h-4': lambda: cuatro('h-4'),
    'a-1': a1, 'a-2': a2, 'a-3': lambda: cuatro('a-3'),
    's-5': s5, 's-6': s6, 's-7': s7, 's-8': s8,
}

if __name__ == '__main__':
    for n in sys.argv[1:] or list(TODOS):
        TODOS[n]()
