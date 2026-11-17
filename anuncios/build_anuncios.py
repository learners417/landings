"""Anuncios de imagen de Experiencias Patagónicas · campaña MARZO (piel «Lago»).

Arma 2 anuncios (feed 4:5 e historia 9:16) y un carrusel de 6 tarjetas (1:1) con las fotos de
anuncios/fotos/ y las fuentes locales. Salida: anuncios/salida/*.png

    python3 anuncios/build_anuncios.py
"""
import pathlib
from playwright.sync_api import sync_playwright

RAIZ = pathlib.Path(__file__).resolve().parent
FOTOS = RAIZ / 'fotos'
SALIDA = RAIZ / 'salida'
F = '/home/claude/fonts/node_modules/'

FUENTES = ''
for w in (400, 500, 600, 700, 800):
    FUENTES += "@font-face{font-family:'Manrope';font-weight:%d;src:url('file://%s@fontsource/manrope/files/manrope-latin-%d-normal.woff2')}" % (w, F, w)
FUENTES += "@font-face{font-family:'Fraunces';font-weight:100 900;font-style:normal;src:url('file://%s@fontsource-variable/fraunces/files/fraunces-latin-full-normal.woff2')}" % F
FUENTES += "@font-face{font-family:'Fraunces';font-weight:100 900;font-style:italic;src:url('file://%s@fontsource-variable/fraunces/files/fraunces-latin-full-italic.woff2')}" % F

CSS = FUENTES + """
*{box-sizing:border-box;margin:0;padding:0}
html,body{width:var(--w);height:var(--h);overflow:hidden}
body{background:#F4EFE6;color:#1D2422;font-family:'Manrope',sans-serif;-webkit-font-smoothing:antialiased;display:flex;flex-direction:column}
.foto{flex:none;width:100%;height:var(--foto);background-size:cover;background-position:var(--pos,center)}
.panel{flex:1;display:flex;flex-direction:column;padding:var(--pad,64px)}
.marca{display:flex;align-items:center;gap:16px;font:800 28px/1 'Manrope';letter-spacing:.12em;text-transform:uppercase;color:#9A3E25}
.marca::before{content:"";width:44px;height:1px;background:#C9B27E}
.t{font-family:'Fraunces',serif;font-variation-settings:"SOFT" 100,"opsz" 144;font-weight:400;letter-spacing:-.025em;line-height:1.02;text-wrap:balance}
.t em{font-style:italic;font-weight:360;color:#9A3E25}
.pie{margin-top:auto;display:flex;align-items:flex-end;justify-content:space-between;gap:24px;border-top:1px solid #C9B27E;padding-top:26px}
.fechas{font:700 32px/1.25 'Manrope';letter-spacing:-.01em}
.fechas span{display:block;font:600 28px/1.3 'Manrope';color:#4F5B57;letter-spacing:0}
.firma{font-family:'Fraunces',serif;font-variation-settings:"SOFT" 100,"opsz" 144;font-size:32px;line-height:1.05;text-align:right;color:#123A42}
.cuenta{margin-top:30px}
.fila{display:flex;align-items:baseline;gap:18px;font:600 36px/1.2 'Manrope';padding:13px 0;border-bottom:1px solid rgba(29,36,34,.14)}
.fila .p{flex:1;border-bottom:2px dotted rgba(29,36,34,.28);transform:translateY(-8px)}
.fila b{font-family:'Fraunces',serif;font-style:italic;font-weight:400;font-size:44px;line-height:.8;color:#9A3E25}
.fila.total{border-bottom:0;border-top:1px solid #C9B27E;margin-top:8px;font-weight:800}
.oscuro{background:#123A42;color:#E9F0EE}
.oscuro .marca{color:#C9B27E}
.oscuro .t em{color:#C9B27E}
.oscuro .pie{border-color:rgba(201,178,126,.7)}
.oscuro .fechas span{color:#B7CBC8}
.oscuro .firma{color:#E9F0EE}
.banda{background:#123A42;color:#E9F0EE}
.banda .marca{color:#C9B27E}
.banda .t em{color:#C9B27E}
.bajada{font:600 34px/1.4 'Manrope';color:#4F5B57;margin-top:26px;max-width:900px}
.sig{position:absolute;right:56px;bottom:52px;font:700 30px/1 'Manrope';color:#C9B27E}
"""

def foto(pid):
    return (FOTOS / f'{pid}.jpg').as_uri()

PIE = """<div class="pie"><p class="fechas">22 feb · 8 mar · 15 mar<span>{nota}</span></p>
<p class="firma">Experiencias<br>Patagónicas</p></div>"""

def pagina(w, h, cuerpo, clase=''):
    return f"""<!doctype html><html><head><meta charset="utf-8"><style>{CSS}</style></head>
<body class="{clase}" style="--w:{w}px;--h:{h}px;position:relative">{cuerpo}</body></html>"""

PIEZAS = {}

# ── Anuncio 1 · Llenaste tu programa ─────────────────────────────────
A1_FOTO = 'photo-1551845728-6820a30c64e2'
PIEZAS['A1-feed'] = (1080, 1350, f"""
<div class="foto" style="--foto:680px;--pos:50% 40%;background-image:url('{foto(A1_FOTO)}')"></div>
<div class="panel" style="--pad:58px 64px 56px">
  <p class="marca">Retiros llave en mano · Bariloche</p>
  <h1 class="t" style="font-size:80px;margin-top:26px">Llenaste tu programa este año. <em>Cerralo con tu grupo en la Patagonia.</em></h1>
  <p class="bajada">Vos das tu contenido. El lugar, la mesa y los traslados los ponemos nosotras.</p>
  {PIE.format(nota='Quedan 3 semanas antes de abril')}
</div>""")
PIEZAS['A1-historia'] = (1080, 1920, f"""
<div class="foto" style="--foto:900px;--pos:50% 40%;background-image:url('{foto(A1_FOTO)}')"></div>
<div class="panel" style="--pad:64px 64px 380px">
  <p class="marca">Retiros llave en mano · Bariloche</p>
  <h1 class="t" style="font-size:88px;margin-top:30px">Llenaste tu programa este año. <em>Cerralo con tu grupo en la Patagonia.</em></h1>
  <p class="bajada">Vos das tu contenido. El lugar, la mesa y los traslados los ponemos nosotras.</p>
  {PIE.format(nota='Quedan 3 semanas antes de abril')}
</div>""")

# ── Anuncio 2 · Antes de reservar la casa ───────────────────────────
A2_FOTO = 'photo-1562050344-f7ad946cee35'
CUENTA = """<div class="cuenta">
  <p class="fila">Cuántas personas vienen<span class="p"></span><b>?</b></p>
  <p class="fila">A cuánto lo vendés<span class="p"></span><b>?</b></p>
  <p class="fila">Cuántas noches<span class="p"></span><b>?</b></p>
  <p class="fila total">Cuánto te queda<span class="p"></span><b>?</b></p>
</div>"""
PIEZAS['A2-feed'] = (1080, 1350, f"""
<div class="foto" style="--foto:470px;--pos:50% 55%;background-image:url('{foto(A2_FOTO)}')"></div>
<div class="panel" style="--pad:52px 64px 56px">
  <p class="marca">Tu retiro en Bariloche</p>
  <h1 class="t" style="font-size:84px;margin-top:22px">Antes de reservar la casa, <em>hacé esta cuenta.</em></h1>
  {CUENTA}
  {PIE.format(nota='La calculadora está en la página')}
</div>""")
PIEZAS['A2-historia'] = (1080, 1920, f"""
<div class="foto" style="--foto:600px;--pos:50% 55%;background-image:url('{foto(A2_FOTO)}')"></div>
<div class="panel" style="--pad:60px 64px 380px">
  <p class="marca">Tu retiro en Bariloche</p>
  <h1 class="t" style="font-size:88px;margin-top:26px">Antes de reservar la casa, <em>hacé esta cuenta.</em></h1>
  {CUENTA}
  {PIE.format(nota='La calculadora está en la página')}
</div>""")

# ── Anuncio 3 · Carrusel «Día uno» (1:1) ─────────────────────────────
TARJETAS = [
    ('photo-1647476685001-8510e5591ec3', '50% 50%', 'Día 1 · 15:00', 'Tu grupo aterriza en Bariloche. <em>Nadie busca un taxi.</em>'),
    ('photo-1571787207812-77254da636a6', '50% 45%', 'Día 1 · 19:30', 'Una casa frente al lago, <em>solo para ustedes.</em>'),
    ('photo-1599341301512-ca6d7a851fba', '50% 60%', 'Día 2 · 10:00', 'Vos das tu contenido. <em>Del resto nos ocupamos nosotras.</em>'),
    ('photo-1579541183120-dbb2ab2aa3c5', '50% 62%', 'Día 3 · 18:40', 'Velero privado por el Nahuel Huapi, <em>con el sol bajando.</em>'),
    ('photo-1778694277039-5cbf0b9a1fcf', '50% 50%', 'Día 4 · 21:00', 'La última cena. <em>Mesa larga, fuego y cocina de autor.</em>'),
]
for i, (pid, pos, ojo, texto) in enumerate(TARJETAS, 1):
    flecha = '<p class="sig">Deslizá →</p>' if i == 1 else ''
    PIEZAS[f'A3-tarjeta-{i}'] = (1080, 1080, f"""
<div class="foto" style="--foto:640px;--pos:{pos};background-image:url('{foto(pid)}')"></div>
<div class="panel banda" style="--pad:50px 64px 56px">
  <p class="marca">{ojo}</p>
  <h1 class="t" style="font-size:70px;margin-top:24px;max-width:940px">{texto}</h1>
</div>{flecha}""")
PIEZAS['A3-tarjeta-6'] = (1080, 1080, f"""
<div class="panel" style="--pad:84px 72px 64px">
  <p class="marca">Experiencias Patagónicas</p>
  <h1 class="t" style="font-size:96px;margin-top:40px">Tu retiro en la Patagonia, <em>llave en mano.</em></h1>
  <p style="font:600 36px/1.35 'Manrope';margin-top:36px;color:#B7CBC8;max-width:820px">Para quien ya tiene un grupo que le paga. Elegí tu horario de 30 minutos y lo armamos con tus números.</p>
  {PIE.format(nota='Quedan 3 semanas antes de abril')}
</div>""")

def armar():
    SALIDA.mkdir(exist_ok=True)
    with sync_playwright() as p:
        b = p.chromium.launch()
        for nombre, (w, h, cuerpo) in PIEZAS.items():
            clase = 'oscuro' if nombre == 'A3-tarjeta-6' else ''
            pg = b.new_page(viewport={'width': w, 'height': h}, device_scale_factor=1)
            html = SALIDA / f'_{nombre}.html'
            html.write_text(pagina(w, h, cuerpo, clase), encoding='utf-8')
            pg.goto(html.as_uri())
            pg.evaluate('document.fonts.ready')
            pg.wait_for_timeout(250)
            # control: nada se sale del lienzo y nada queda debajo de 26 px
            info = pg.evaluate("""()=>{const o=[];document.querySelectorAll('body *').forEach(e=>{const r=e.getBoundingClientRect();if(r.width&&(r.right>innerWidth+1||r.bottom>innerHeight+1))o.push('sale '+e.className+' '+Math.round(r.bottom));const t=[...e.childNodes].some(n=>n.nodeType==3&&n.textContent.trim());if(t&&parseFloat(getComputedStyle(e).fontSize)<26)o.push('chica '+e.className)});return o}""")
            pg.screenshot(path=str(SALIDA / f'{nombre}.png'))
            html.unlink()
            print(nombre, w, 'x', h, info or 'ok')
            pg.close()
        b.close()

if __name__ == '__main__':
    armar()
