"""El test de las 6 piezas de Experiencias Patagónicas: el post y el carrusel (4:5).

Un solo mensaje: lo que vive la mentora en su propio retiro, y lo que no vive.
Fotos reales de los eventos de Ailu: viven fuera del repo (/home/claude/ep-reales), sus PNG no se suben.

    python3 anuncios/test_seis.py            # post y carrusel
    python3 anuncios/test_seis.py post       # uno
"""
import pathlib, sys
from playwright.sync_api import sync_playwright
from build_anuncios import FUENTES

FOTOS = pathlib.Path('/home/claude/ep-reales')
SALIDA = pathlib.Path('/home/claude/entregas/test')
W, H = 1080, 1350

CSS = FUENTES + """
*{margin:0;padding:0;box-sizing:border-box}
html,body{width:%dpx;height:%dpx;background:#0D1B1F}
.c{position:relative;width:%dpx;height:%dpx;overflow:hidden;color:#FFFDF9;font-family:'Manrope',sans-serif}
.foto{position:absolute;inset:0;background-size:cover;filter:saturate(.92) contrast(1.02)}
.velo{position:absolute;inset:0}
.abajo .velo{background:linear-gradient(180deg,rgba(9,22,26,.5) 0%%,rgba(9,22,26,0) 17%%,rgba(9,22,26,0) 44%%,rgba(9,22,26,.78) 100%%)}
.arriba .velo{background:linear-gradient(180deg,rgba(9,22,26,.62) 0%%,rgba(9,22,26,.18) 46%%,rgba(9,22,26,0) 62%%)}
.marca{position:absolute;top:60px;left:72px;right:72px;display:flex;justify-content:space-between;align-items:center;
  font:700 26px/1 'Manrope';letter-spacing:.2em;text-transform:uppercase;color:rgba(255,253,249,.9)}
.marca i{flex:1;height:1px;background:rgba(201,178,126,.75);margin-left:26px}
.texto{position:absolute;left:72px;right:72px}
.abajo .texto{bottom:96px}
.arriba .texto{top:150px}
h1{font-family:'Fraunces',serif;font-variation-settings:"SOFT" 100,"opsz" 144;font-weight:370;font-size:86px;line-height:1.04;letter-spacing:-.012em;text-wrap:balance}
h1 em{font-style:italic;color:#E7D3A1}
.gran h1{font-size:104px}
.no{margin-top:34px;font:600 40px/1.25 'Manrope';color:rgba(255,253,249,.82);
  text-decoration:line-through;text-decoration-color:#E0705E;text-decoration-thickness:4px;text-wrap:balance}
.bajada{margin-top:30px;font:600 42px/1.28 'Manrope';color:rgba(255,253,249,.94);text-wrap:balance}
.pill{display:inline-flex;align-items:center;gap:14px;margin-top:40px;background:#FFFDF9;color:#14262A;border-radius:999px;padding:22px 34px;font:800 34px/1 'Manrope'}
.pill svg{width:30px;height:30px}
.firma{margin-top:30px;font:700 28px/1.3 'Manrope';letter-spacing:.14em;text-transform:uppercase;color:#E7D3A1}
""" % (W, H, W, H)

FLECHA = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12h14M13 6l6 6-6 6"/></svg>'


def tarjeta(foto, pos, cuerpo, donde='abajo', clase='', marca=True):
    m = '<div class="marca">Experiencias Patagónicas<i></i></div>' if marca else ''
    return (f'<div class="c {donde} {clase}"><div class="foto" style="background-image:url(\'{(FOTOS / foto).as_uri()}\');background-position:{pos}"></div>'
            f'<div class="velo"></div>{m}<div class="texto">{cuerpo}</div></div>')


def escena(foto, pos, vive, no):
    return tarjeta(foto, pos, f'<h1>{vive}</h1><p class="no">{no}</p>')


CIERRE = ('<h1>Vos traés a tu comunidad. <em>Del resto me encargo yo.</em></h1>'
          '<p class="bajada">Con el presupuesto cerrado antes de que vendas el primer lugar.</p>'
          f'<span class="pill">Agendá 30 minutos con Ailu {FLECHA}</span>')

PIEZAS = {
    'post': [
        tarjeta('14-diseno-sin-titulo-03.jpg', '50% 62%',
                '<h1>Así se siente tu propio retiro <em>cuando está todo resuelto.</em></h1>'
                '<p class="bajada">Vos traés a tu comunidad. Del resto me encargo yo.</p>'
                '<p class="firma">Ailu · Retiros en Bariloche</p>', donde='arriba'),
    ],
    'carrusel': [
        tarjeta('08-agape-22.jpg', '58% 50%',
                '<h1>Lo que vas a vivir en tu propio retiro. <em>Y lo que no.</em></h1>'
                f'<span class="pill">Deslizá {FLECHA}</span>', clase='gran'),
        escena('06-5.jpg', '30% 50%', 'Llegás a la sala y el café ya está servido.',
               'Ir a buscar las medialunas a las siete'),
        escena('02-mar08825.jpg', '62% 50%', 'Das tu sesión con la sala armada y el lago de fondo.',
               'Pelearte con el proyector mientras entran'),
        escena('03-7.jpg', '50% 50%', 'A la tarde salen al lago. Vos también.',
               'Quedarte en el hotel coordinando la combi'),
        escena('09-diseno-sin-titulo-1.jpg', '50% 60%', 'A la noche te sentás a la mesa con ellos.',
               'Rearmar el menú del celíaco a último momento'),
        escena('14-diseno-sin-titulo-01.jpg', '50% 30%', 'Y en algún momento, vos también mirás el lago.',
               'Contestar cuarenta chats de proveedores'),
        escena('07-agape-11.jpg', '50% 62%', 'El último día te llevás el abrazo de tu grupo.',
               'Volver a tu casa sin haberlo disfrutado'),
        tarjeta('01-mar04096.jpg', '50% 18%', CIERRE),
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
            fuera = pg.evaluate("""() => [...document.querySelectorAll('.texto, .texto *')].filter(e => {
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
