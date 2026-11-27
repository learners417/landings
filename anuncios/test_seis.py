"""El test de las 6 piezas de Experiencias Patagónicas: el post y el carrusel (4:5).

Un solo mensaje: lo que vive la mentora en su propio retiro, y lo que no vive.
Fotos reales de los eventos de Ailu: viven fuera del repo (/home/claude/ep-reales), sus PNG no se suben.

    python3 anuncios/test_seis.py            # post y carrusel
    python3 anuncios/test_seis.py post       # uno
"""
import pathlib, sys
from playwright.sync_api import sync_playwright

FOTOS = pathlib.Path('/home/claude/ep-reales')
SALIDA = pathlib.Path('/home/claude/entregas/test')
W, H = 1080, 1350

MF = '/home/claude/fonts/node_modules/@fontsource/montserrat/files/'
MONT = ''.join("@font-face{font-family:'Montserrat';font-weight:%d;src:url('file://%smontserrat-latin-%d-normal.woff2')}" % (w, MF, w) for w in (200, 300, 400, 500))
GRANO = "url(\"data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='240' height='240'><filter id='g'><feTurbulence type='fractalNoise' baseFrequency='.85' numOctaves='2' stitchTiles='stitch'/><feColorMatrix values='0 0 0 0 .5 0 0 0 0 .5 0 0 0 0 .5 0 0 0 .55 0'/></filter><rect width='100%%' height='100%%' filter='url(%%23g)'/></svg>\")"

CSS = MONT + """
*{margin:0;padding:0;box-sizing:border-box}
html,body{width:%dpx;height:%dpx;background:#14181A}
.c{position:relative;width:%dpx;height:%dpx;overflow:hidden;color:#F4F1EA;font-family:'Montserrat',sans-serif;-webkit-font-smoothing:antialiased}
.foto{position:absolute;inset:0;background-size:cover;filter:saturate(.9) contrast(1.02)}
.velo{position:absolute;inset:0}
.abajo .velo{background:linear-gradient(180deg,rgba(12,16,18,.22) 0%%,rgba(12,16,18,0) 14%%,rgba(12,16,18,0) 46%%,rgba(12,16,18,.74) 100%%)}
.arriba .velo{background:linear-gradient(180deg,rgba(12,16,18,.6) 0%%,rgba(12,16,18,.2) 40%%,rgba(12,16,18,0) 58%%)}
.grano{position:absolute;inset:0;background-image:%s;opacity:.16;mix-blend-mode:overlay;pointer-events:none}
.logo{position:absolute;top:64px;right:68px;width:84px;opacity:.92}
.texto{position:absolute;left:76px;right:76px}
.abajo .texto{bottom:100px}
.arriba .texto{top:170px}
h1{font-weight:300;font-size:76px;line-height:1.1;letter-spacing:-.02em;text-wrap:balance}
h1 b{font-weight:300;color:#BFE0E6}
.gran h1{font-size:84px}
.gran .texto{right:400px}
.no{margin-top:34px;font:400 38px/1.3 'Montserrat';color:rgba(244,241,234,.8);
  text-decoration:line-through;text-decoration-color:#E0705E;text-decoration-thickness:3px;text-wrap:balance}
.bajada{margin-top:30px;font:400 40px/1.3 'Montserrat';color:rgba(244,241,234,.94);text-wrap:balance}
.firma{margin-top:34px;font:500 26px/1 'Montserrat';letter-spacing:.32em;text-transform:uppercase;color:rgba(244,241,234,.86)}
.pill{display:inline-flex;align-items:center;gap:14px;margin-top:42px;background:#F4F1EA;color:#1F1A21;border-radius:999px;padding:22px 34px;font:500 32px/1 'Montserrat'}
.pill svg{width:28px;height:28px}
.desliza{position:absolute;right:68px;bottom:100px;display:flex;align-items:center;gap:16px;font:500 28px/1 'Montserrat';letter-spacing:.28em;text-transform:uppercase;color:#F4F1EA;
  border:1.5px solid rgba(244,241,234,.75);border-radius:999px;padding:20px 26px 20px 32px}
.desliza svg{width:30px;height:30px}
""" % (W, H, W, H, GRANO)

FLECHA = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12h14M13 6l6 6-6 6"/></svg>'


def tarjeta(foto, pos, cuerpo, donde='abajo', clase='', extra=''):
    logo = f'<img class="logo" src="{(FOTOS / "logo-esquina.png").as_uri()}" alt="">'
    return (f'<div class="c {donde} {clase}"><div class="foto" style="background-image:url(\'{(FOTOS / foto).as_uri()}\');background-position:{pos}"></div>'
            f'<div class="velo"></div><div class="grano"></div>{logo}<div class="texto">{cuerpo}</div>{extra}</div>')


def escena(foto, pos, vive, no):
    return tarjeta(foto, pos, f'<h1>{vive}</h1><p class="no">{no}</p>')


CIERRE = ('<h1>Vos traés a tu comunidad. <b>Del resto me encargo yo.</b></h1>'
          '<p class="bajada">Con el presupuesto cerrado antes de que vendas el primer lugar.</p>'
          f'<span class="pill">Agendá 30 minutos con Ailu {FLECHA}</span>')

PIEZAS = {
    'post': [
        tarjeta('13-thumbnail.jpg', '50% 30%',
                '<h1>Así se siente tu propio retiro <b>cuando está todo resuelto.</b></h1>'
                '<p class="bajada">Vos traés a tu comunidad. Del resto me encargo yo.</p>'
                '<p class="firma">Ailu · Bariloche</p>', donde='arriba'),
    ],
    'carrusel': [
        tarjeta('08-agape-22.jpg', '58% 50%',
                '<h1>Lo que vas a vivir en tu propio retiro. <b>Y lo que no.</b></h1>', clase='gran',
                extra=f'<div class="desliza">Deslizá {FLECHA}</div>'),
        escena('06-5.jpg', '30% 50%', 'Llegás a la sala y el café ya está servido.',
               'Ir a buscar las medialunas a las siete'),
        escena('02-mar08825.jpg', '62% 50%', 'Das tu sesión con la sala armada y el lago de fondo.',
               'Pelearte con el proyector mientras entran'),
        escena('03-7.jpg', '50% 50%', 'A la tarde salen al lago. Vos también.',
               'Quedarte en el hotel coordinando la combi'),
        escena('09-diseno-sin-titulo-1.jpg', '50% 60%', 'A la noche te sentás a la mesa con ellos.',
               'Rearmar el menú del celíaco a último momento'),
        escena('11-diseno-sin-titulo-3.jpg', '50% 45%', 'Y después de cenar, el fuego.',
               'Contestar cuarenta chats de proveedores'),
        escena('07-agape-11.jpg', '50% 62%', 'El último día te llevás el abrazo de tu grupo.',
               'Volver a tu casa sin haberlo disfrutado'),
        tarjeta('17-mar04001.jpg', '55% 30%', CIERRE),
    ],
}


def render(nombre):
    out = SALIDA / nombre
    out.mkdir(parents=True, exist_ok=True)
    with sync_playwright() as p:
        b = p.chromium.launch()
        pg = b.new_page(viewport={'width': W, 'height': H})
        for k, html in enumerate(PIEZAS[nombre], 1):
            tmp = out / '_tmp.html'
            tmp.write_text(f'<html><head><meta charset="utf-8"><style>{CSS}</style></head><body>{html}</body></html>')
            pg.goto(tmp.as_uri())
            pg.evaluate('document.fonts.ready')
            pg.wait_for_timeout(500)
            # Control: nada se sale del cuadro y ninguna letra baja de 26 px.
            fuera = pg.evaluate("""() => [...document.querySelectorAll('.texto, .texto *, .desliza')].filter(e => {
                const r = e.getBoundingClientRect(); return r.bottom > %d - 40 || r.right > %d - 40 || r.top < 40; }).map(e => e.className || e.tagName)""" % (H, W))
            chica = pg.evaluate("""() => [...document.querySelectorAll('.c *')].filter(e => e.childNodes.length && [...e.childNodes].some(n => n.nodeType === 3 && n.textContent.trim()))
                .map(e => parseFloat(getComputedStyle(e).fontSize)).filter(s => s < 26)""")
            assert not fuera, (nombre, k, fuera)
            assert not chica, (nombre, k, chica)
            pg.screenshot(path=str(out / f'{nombre}-{k}.png'))
        b.close()
    (out / '_tmp.html').unlink()
    print(nombre, len(PIEZAS[nombre]), '→', out)


if __name__ == '__main__':
    for n in (sys.argv[1:] or PIEZAS):
        render(n)
