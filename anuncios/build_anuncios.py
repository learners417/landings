"""Anuncios de imagen de Experiencias Patagónicas · campaña MARZO (piel «Lago»).

3 anuncios de imagen (feed 4:5 y historia 9:16) y 3 carruseles de 6 tarjetas (1:1),
con las fotos de anuncios/fotos/ y las fuentes locales. Salida: anuncios/salida/*.png

    python3 anuncios/build_anuncios.py
"""
import pathlib, shutil
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

GRANO = ("data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='240' height='240'>"
         "<filter id='n'><feTurbulence type='fractalNoise' baseFrequency='.85' numOctaves='2' stitchTiles='stitch'/>"
         "<feColorMatrix values='0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 .55 0'/></filter>"
         "<rect width='100%25' height='100%25' filter='url(%23n)'/></svg>")

CSS = FUENTES + """
*{box-sizing:border-box;margin:0;padding:0}
html,body{width:var(--w);height:var(--h);overflow:hidden}
body{position:relative;font-family:'Manrope',sans-serif;-webkit-font-smoothing:antialiased;color:#1D2422;background:#F4EFE6}
body::after{content:"";position:absolute;inset:0;background-image:url("GRANO");opacity:.10;mix-blend-mode:multiply;pointer-events:none;z-index:9}
body.lago{background:#123A42;color:#E9F0EE}
body.lago::after{opacity:.16;mix-blend-mode:soft-light}
body.papel{background:#FBF8F2}
.col{position:absolute;inset:0;display:flex;flex-direction:column}
.foto{flex:none;width:100%;background-size:cover;background-position:var(--pos,center)}
.marco{flex:none;margin:var(--m,48px 48px 0);border-radius:28px;background-size:cover;background-position:var(--pos,center)}
.panel{flex:1;display:flex;flex-direction:column;padding:var(--pad,56px 64px)}
.banda{background:#123A42;color:#E9F0EE}
.ojo{display:flex;align-items:center;gap:16px;font:800 27px/1.1 'Manrope';letter-spacing:.13em;text-transform:uppercase;color:#9A3E25}
.ojo::before{content:"";flex:none;width:46px;height:1px;background:#C9B27E}
.lago .ojo,.banda .ojo{color:#C9B27E}
.t{font-family:'Fraunces',serif;font-variation-settings:"SOFT" 100,"opsz" 144;font-weight:400;letter-spacing:-.028em;line-height:1.0;text-wrap:balance}
.t em{font-style:italic;font-weight:350;color:#9A3E25}
.lago .t em,.banda .t em{color:#C9B27E}
.p{font:600 34px/1.38 'Manrope';color:#4F5B57;text-wrap:pretty}
.lago .p,.banda .p{color:#B7CBC8}
.pie{margin-top:auto;display:flex;align-items:flex-end;justify-content:space-between;gap:24px;border-top:1px solid #C9B27E;padding-top:24px}
.fechas{font:700 31px/1.25 'Manrope'}
.fechas span{display:block;font:600 27px/1.3 'Manrope';color:#4F5B57}
.lago .fechas span,.banda .fechas span{color:#B7CBC8}
.firma{font-family:'Fraunces',serif;font-variation-settings:"SOFT" 100,"opsz" 144;font-size:31px;line-height:1.05;text-align:right;color:#123A42}
.lago .firma,.banda .firma{color:#E9F0EE}
.folio{position:absolute;top:44px;right:52px;z-index:5;font:700 26px/1 'Manrope';letter-spacing:.08em;color:#FFFDF9;background:rgba(18,58,66,.62);padding:10px 14px;border-radius:999px}
.folio.claro{background:none;color:#4F5B57;padding:0;top:56px;right:64px}
.lago .folio.claro{color:#B7CBC8}
.sig{font:700 30px/1 'Manrope';color:#C9B27E;letter-spacing:.02em}
.cifra{font-family:'Fraunces',serif;font-variation-settings:"SOFT" 100,"opsz" 144;font-weight:330;letter-spacing:-.045em;line-height:.9;font-variant-numeric:lining-nums tabular-nums;white-space:nowrap}
.fila{display:flex;align-items:center;gap:18px;font:600 35px/1.2 'Manrope';padding:14px 0;border-bottom:1px solid rgba(29,36,34,.14)}
.fila .pt{flex:1;border-bottom:2px dotted rgba(29,36,34,.26);transform:translateY(8px)}
.fila b{font-family:'Fraunces',serif;font-style:italic;font-weight:400;font-size:46px;line-height:.8;color:#9A3E25}
.fila.total{border-bottom:0;border-top:1px solid #C9B27E;margin-top:8px;font-weight:800}
.tach{position:relative;font:600 31px/1.25 'Manrope';color:#4F5B57;padding:9px 0;width:max-content;max-width:100%}
.tach::after{content:"";position:absolute;left:-4px;right:-4px;top:54%;height:3px;background:#B4432F;transform:rotate(-1.2deg);border-radius:2px}
.tilde{flex:none;width:var(--d,72px);height:var(--d,72px);border-radius:50%;background:#36603F;display:grid;place-items:center}
.tilde svg{width:52%;height:52%}
.puntos{display:grid;grid-template-columns:repeat(7,1fr);gap:22px;width:100%}
.punto{aspect-ratio:1;border-radius:50%;border:3px solid #9A3E25}
.punto.cubre{background:#123A42;border-color:#123A42}
.punto.tuyo{background:#36603F;border-color:#36603F;display:grid;place-items:center}
.punto.tuyo .tilde{width:100%;height:100%;background:none}
.chip{border:1px solid #C9B27E;border-radius:999px;padding:16px 26px;font:700 32px/1 'Manrope'}
"""
CSS = CSS.replace('GRANO', GRANO)

def foto(pid):
    return (FOTOS / f'{pid}.jpg').as_uri()

def bg(pid, pos='center'):
    return f"background-image:url('{foto(pid)}');--pos:{pos}"

def tilde(d=72):
    return (f'<span class="tilde" style="--d:{d}px"><svg viewBox="0 0 24 24" fill="none" stroke="#FBF8F2" stroke-width="3" '
            'stroke-linecap="round" stroke-linejoin="round"><path d="m5 12.5 4.5 4.5L19 7.5"/></svg></span>')

def pie(nota, fechas='22 feb · 8 mar · 15 mar'):
    return f'<div class="pie"><p class="fechas">{fechas}<span>{nota}</span></p><p class="firma">Experiencias<br>Patagónicas</p></div>'

P = {}   # nombre -> (ancho, alto, clase del body, html)

# ═══════════════ ANUNCIOS DE IMAGEN ═══════════════
# 1 · Llenaste tu programa  (foto enmarcada, estilo revista)
F1 = 'photo-1551845728-6820a30c64e2'
P['imagen-1-llenaste-feed'] = (1080, 1350, '', f"""<div class="col">
<div class="marco" style="height:700px;{bg(F1,'50% 38%')}"></div>
<div class="panel" style="--pad:46px 64px 54px">
  <p class="ojo">Retiros llave en mano · Bariloche</p>
  <h1 class="t" style="font-size:82px;margin-top:24px">Llenaste tu programa este año. <em>Cerralo con tu grupo en la Patagonia.</em></h1>
  {pie('Quedan 3 semanas antes de abril')}
</div></div>""")
P['imagen-1-llenaste-historia'] = (1080, 1920, '', f"""<div class="col">
<div class="marco" style="--m:48px 48px 0;height:900px;{bg(F1,'50% 38%')}"></div>
<div class="panel" style="--pad:52px 64px 370px">
  <p class="ojo">Retiros llave en mano · Bariloche</p>
  <h1 class="t" style="font-size:90px;margin-top:28px">Llenaste tu programa este año. <em>Cerralo con tu grupo en la Patagonia.</em></h1>
  <p class="p" style="margin-top:26px">Vos das tu contenido. El lugar, la mesa y los traslados los ponemos nosotras.</p>
  {pie('Quedan 3 semanas antes de abril')}
</div></div>""")

# 2 · Antes de reservar la casa, hacé esta cuenta
F2 = 'photo-1562050344-f7ad946cee35'
CUENTA = """<div style="margin-top:28px">
  <p class="fila">Cuántas personas vienen<span class="pt"></span><b>?</b></p>
  <p class="fila">A cuánto lo vendés<span class="pt"></span><b>?</b></p>
  <p class="fila">Cuántas noches<span class="pt"></span><b>?</b></p>
  <p class="fila total">Cuánto te queda<span class="pt"></span><b>?</b></p>
</div>"""
P['imagen-2-cuenta-feed'] = (1080, 1350, 'papel', f"""<div class="col">
<div class="foto" style="height:450px;{bg(F2,'50% 55%')}"></div>
<div class="panel" style="--pad:50px 64px 54px">
  <p class="ojo">Tu retiro en Bariloche</p>
  <h1 class="t" style="font-size:84px;margin-top:22px">Antes de reservar la casa, <em>hacé esta cuenta.</em></h1>
  {CUENTA}
  {pie('La calculadora está en la página')}
</div></div>""")
P['imagen-2-cuenta-historia'] = (1080, 1920, 'papel', f"""<div class="col">
<div class="foto" style="height:600px;{bg(F2,'50% 55%')}"></div>
<div class="panel" style="--pad:58px 64px 370px">
  <p class="ojo">Tu retiro en Bariloche</p>
  <h1 class="t" style="font-size:90px;margin-top:26px">Antes de reservar la casa, <em>hacé esta cuenta.</em></h1>
  {CUENTA}
  {pie('La calculadora está en la página')}
</div></div>""")

# 3 · Doce proveedores. Una sola persona.
F3 = 'photo-1598162480222-b2c3d92548d5'
DOCE = ['El hotel o el lodge', 'La cocina de 4 días', 'Los traslados', 'El velero y la lancha',
        'El guía de montaña', 'La sala y el sonido', 'El fotógrafo', 'El plan B si llueve',
        'El seguro de cada salida', 'El pago a cada uno', 'Los horarios del día', 'El imprevisto de las 23 h']
def lista():
    bloques = ''.join('<div>' + ''.join(f'<p class="tach">{x}</p>' for x in DOCE[i*6:(i+1)*6]) + '</div>' for i in range(2))
    return f'<div style="display:grid;grid-template-columns:1fr 1fr;column-gap:36px;margin-top:24px">{bloques}</div>'
AILU = f"""<div style="display:flex;align-items:center;gap:24px;margin-top:28px;padding-top:26px;border-top:1px solid #C9B27E">
  {tilde(72)}<p><span class="t" style="font-size:60px;display:block">Ailu</span>
  <span class="p" style="font-size:30px;display:block;margin-top:6px">Contesta, decide y está en el evento.</span></p></div>"""
P['imagen-3-doce-feed'] = (1080, 1350, '', f"""<div class="col">
<div class="foto" style="height:290px;{bg(F3,'50% 42%')}"></div>
<div class="panel" style="--pad:42px 64px 48px">
  <p class="ojo">Cuando tu retiro lo armás solo</p>
  <h1 class="t" style="font-size:80px;margin-top:20px">Doce proveedores. <em>Una sola persona.</em></h1>
  {lista()}
  {AILU}
  {pie('Retiros llave en mano en Bariloche')}
</div></div>""")
P['imagen-3-doce-historia'] = (1080, 1920, '', f"""<div class="col">
<div class="foto" style="height:420px;{bg(F3,'50% 42%')}"></div>
<div class="panel" style="--pad:52px 64px 370px">
  <p class="ojo">Cuando tu retiro lo armás solo</p>
  <h1 class="t" style="font-size:88px;margin-top:22px">Doce proveedores. <em>Una sola persona.</em></h1>
  {lista()}
  {AILU}
  {pie('Retiros llave en mano en Bariloche')}
</div></div>""")

# ═══════════════ CARRUSEL 1 · Día uno ═══════════════
DIAS = [
    ('photo-1647476685001-8510e5591ec3', '50% 50%', 'Día 1 · 15:00', 'Tu grupo aterriza en Bariloche. <em>Nadie busca un taxi.</em>'),
    ('photo-1571787207812-77254da636a6', '50% 45%', 'Día 1 · 19:30', 'Una casa frente al lago, <em>solo para ustedes.</em>'),
    ('photo-1599341301512-ca6d7a851fba', '50% 60%', 'Día 2 · 10:00', 'Vos das tu contenido. <em>Del resto nos ocupamos nosotras.</em>'),
    ('photo-1579541183120-dbb2ab2aa3c5', '50% 62%', 'Día 3 · 18:40', 'Velero privado por el Nahuel Huapi, <em>con el sol bajando.</em>'),
    ('photo-1778694277039-5cbf0b9a1fcf', '50% 50%', 'Día 4 · 21:00', 'La última cena. <em>Mesa larga, fuego y cocina de autor.</em>'),
]
for i, (pid, pos, ojo, texto) in enumerate(DIAS, 1):
    sig = '<p class="sig" style="margin-top:auto;text-align:right">Deslizá →</p>' if i == 1 else ''
    P[f'carrusel-1-dia-uno-{i}'] = (1080, 1080, '', f"""<p class="folio">{i:02d} / 06</p><div class="col">
<div class="foto" style="height:620px;{bg(pid,pos)}"></div>
<div class="panel banda" style="--pad:46px 64px 48px">
  <p class="ojo">{ojo}</p>
  <h1 class="t" style="font-size:76px;margin-top:22px;max-width:950px">{texto}</h1>{sig}
</div></div>""")
P['carrusel-1-dia-uno-6'] = (1080, 1080, 'lago', f"""<p class="folio claro">06 / 06</p><div class="col"><div class="panel" style="--pad:84px 72px 64px">
  <p class="ojo">Experiencias Patagónicas</p>
  <h1 class="t" style="font-size:100px;margin-top:40px">Tu retiro en la Patagonia, <em>llave en mano.</em></h1>
  <p class="p" style="margin-top:34px;max-width:860px">Para quien ya tiene un grupo que le paga. Elegí tu horario de 30 minutos y lo armamos con tus números.</p>
  {pie('Quedan 3 semanas antes de abril')}
</div></div>""")

# ═══════════════ CARRUSEL 2 · La cuenta ═══════════════
P['carrusel-2-cuenta-1'] = (1080, 1080, 'lago', """<p class="folio claro">01 / 06</p><div class="col"><div class="panel" style="--pad:84px 72px 70px">
  <p class="ojo">Tu retiro en Bariloche</p>
  <h1 class="t" style="font-size:114px;margin-top:44px">¿Cuánto te queda de un retiro de cuatro días <em>en la Patagonia?</em></h1>
  <div style="margin-top:auto;display:flex;justify-content:space-between;align-items:flex-end;border-top:1px solid rgba(201,178,126,.7);padding-top:26px">
    <p class="p" style="font-size:32px">Hicimos la cuenta.</p><p class="sig">Deslizá →</p></div>
</div></div>""")
P['carrusel-2-cuenta-2'] = (1080, 1080, 'papel', """<p class="folio claro">02 / 06</p><div class="col"><div class="panel" style="--pad:84px 72px 70px">
  <p class="ojo">Un ejemplo de la calculadora</p>
  <div style="display:flex;flex-wrap:wrap;gap:16px;margin-top:40px">
    <span class="chip">14 personas</span><span class="chip">4 noches</span><span class="chip">US$ 2.900 cada una</span></div>
  <p class="p" style="margin-top:30px;max-width:880px">Nivel premium: lodge boutique frente al lago y cocina de autor.</p>
  <div style="margin-top:auto;border-top:1px solid #C9B27E;padding-top:30px">
    <p class="p" style="font-size:34px">Lo que vendés</p>
    <p class="cifra" style="font-size:190px;margin-top:18px;color:#123A42">US$ 40.600</p></div>
</div></div>""")
COSTOS = ['Alojamiento, cocina, traslados y salidas', 'Sala, fotos y detalles', 'Imprevistos, 8 %', 'Nuestro honorario']
FILAS = ''.join(f'<p class="fila" style="font-size:40px;padding:22px 0">{tilde(52)}<span>{c}</span></p>' for c in COSTOS)
P['carrusel-2-cuenta-3'] = (1080, 1080, 'papel', f"""<p class="folio claro">03 / 06</p><div class="col"><div class="panel" style="--pad:84px 72px 70px">
  <p class="ojo">Todo el retiro, producido</p>
  <div style="margin-top:34px">{FILAS}</div>
  <div style="margin-top:auto;display:flex;justify-content:space-between;align-items:baseline;border-top:1px solid #C9B27E;padding-top:24px">
    <p class="p" style="font-size:34px;color:#1D2422;font-weight:800">Todo junto</p>
    <p class="cifra" style="font-size:120px;color:#9A3E25">−US$ 25.256</p></div>
</div></div>""")
P['carrusel-2-cuenta-4'] = (1080, 1080, 'lago', """<p class="folio claro">04 / 06</p><div class="col"><div class="panel" style="--pad:84px 72px 70px">
  <p class="ojo">Te queda a vos</p>
  <p class="cifra" style="font-size:224px;margin-top:auto;color:#C9B27E">US$ 15.344</p>
  <p class="t" style="font-size:66px;margin-top:34px">El 38 % de lo que vendés, <em>con todo pagado.</em></p>
</div></div>""")
PUNTOS = ''.join('<span class="punto cubre"></span>' if i < 9 else '<span class="punto tuyo">' + tilde(10) + '</span>' for i in range(14))
P['carrusel-2-cuenta-5'] = (1080, 1080, 'papel', f"""<p class="folio claro">05 / 06</p><div class="col"><div class="panel" style="--pad:84px 72px 70px">
  <p class="ojo">El punto de equilibrio</p>
  <h1 class="t" style="font-size:86px;margin-top:30px">Con 9 lugares vendidos, <em>ya cubriste todo.</em></h1>
  <div class="puntos" style="margin-top:auto">{PUNTOS}</div>
  <p class="p" style="margin-top:30px">Los primeros 9 cubren todo. Desde el lugar 10, cada lugar que vendés te queda a vos.</p>
</div></div>""")
P['carrusel-2-cuenta-6'] = (1080, 1080, '', f"""<p class="folio claro">06 / 06</p><div class="col"><div class="panel" style="--pad:84px 72px 64px">
  <p class="ojo">Experiencias Patagónicas</p>
  <h1 class="t" style="font-size:100px;margin-top:40px">Hacé la cuenta <em>con tus números.</em></h1>
  <p class="p" style="margin-top:32px;max-width:880px">La calculadora está en la página. Si te cierra, elegí tu horario de 30 minutos y armamos el tuyo.</p>
  {pie('Quedan 3 semanas antes de abril')}
</div></div>""")

# ═══════════════ CARRUSEL 3 · Cómo se arma ═══════════════
P['carrusel-3-pasos-1'] = (1080, 1080, '', f"""<p class="folio">01 / 06</p><div class="col">
<div class="foto" style="height:640px;{bg('photo-1578592391689-0e3d1a1b52b9','50% 40%')}"></div>
<div class="panel banda" style="--pad:46px 64px 48px">
  <p class="ojo">Tu retiro en Bariloche</p>
  <h1 class="t" style="font-size:92px;margin-top:22px">Llave en mano, <em>en tres pasos.</em></h1>
  <p class="sig" style="margin-top:auto;text-align:right">Deslizá →</p>
</div></div>""")
PASOS = [
    ('photo-1692199037113-ff28ad03f703', '50% 55%', '1', 'Hablamos 30 minutos.', 'Tu grupo, tu fecha y lo que querés que se lleven. Salís de la llamada con un número.'),
    ('photo-1643494555111-df0141d84a62', '50% 50%', '2', 'Tu propuesta en 48 horas.', 'Lugar, programa y presupuesto cerrado, con lo que te queda a vos y tu punto de equilibrio.'),
    ('photo-1782226796423-8d72656a332c', '50% 50%', '3', 'Reservás con la seña.', 'La fecha es tuya. Te damos tu panel para vender y nos ocupamos de cada proveedor.'),
]
for i, (pid, pos, n, tit, txt) in enumerate(PASOS, 2):
    P[f'carrusel-3-pasos-{i}'] = (1080, 1080, 'lago', f"""<p class="folio" style="top:70px;right:72px">{i:02d} / 06</p><div class="col">
<div class="marco" style="--m:48px 48px 0;height:520px;{bg(pid,pos)}"></div>
<div class="panel" style="--pad:40px 64px 56px;flex-direction:row;gap:40px;align-items:flex-start">
  <p class="cifra" style="font-size:300px;color:#C9B27E;line-height:.78;flex:none">{n}</p>
  <div><h1 class="t" style="font-size:80px">{tit}</h1>
  <p class="p" style="margin-top:24px;font-size:36px">{txt}</p></div>
</div></div>""")
P['carrusel-3-pasos-5'] = (1080, 1080, 'papel', """<p class="folio claro">05 / 06</p><div class="col"><div class="panel" style="--pad:84px 72px 70px">
  <p class="ojo">Quién lo produce</p>
  <p class="t" style="font-size:94px;margin-top:40px;font-style:italic;font-weight:350;color:#123A42">«Tu grupo vive Bariloche como lo vivimos los que estamos acá.»</p>
  <div style="margin-top:auto;border-top:1px solid #C9B27E;padding-top:26px">
    <p class="t" style="font-size:54px">Ailu</p>
    <p class="p" style="font-size:31px;margin-top:10px">Viene de las cocinas de Bariloche: Madurado, Alma del Lago y El Nido del Cóndor. Hace más de cuatro años que produce experiencias en la Patagonia, y está en cada evento.</p></div>
</div></div>""")
FECHAS = [('22', 'feb'), ('8', 'mar'), ('15', 'mar')]
TILES = ''.join(f'<div style="border:1px solid rgba(201,178,126,.75);border-radius:26px;padding:26px 22px 22px;text-align:center"><p class="cifra" style="font-size:184px;color:#C9B27E">{d}</p><p style="font:800 30px/1 Manrope;letter-spacing:.14em;text-transform:uppercase;margin-top:14px">{m}</p></div>' for d, m in FECHAS)
P['carrusel-3-pasos-6'] = (1080, 1080, 'lago', f"""<p class="folio claro">06 / 06</p><div class="col"><div class="panel" style="--pad:84px 72px 64px">
  <p class="ojo">Las fechas antes de abril</p>
  <div style="display:grid;grid-template-columns:repeat(3,1fr);gap:22px;margin-top:40px">{TILES}</div>
  <p class="p" style="margin-top:34px">Cuando una se toma con seña, se tacha. En invierno: 5 de julio, 16 y 23 de agosto y 13 de septiembre.</p>
  <div class="pie"><p class="fechas" style="color:#E9F0EE">Elegí tu horario de 30 minutos<span>experienciaspatagonicas.com</span></p><p class="firma">Experiencias<br>Patagónicas</p></div>
</div></div>""")


def armar():
    if SALIDA.exists():
        shutil.rmtree(SALIDA)
    SALIDA.mkdir()
    problemas = 0
    with sync_playwright() as p:
        b = p.chromium.launch()
        for nombre, (w, h, clase, cuerpo) in P.items():
            pg = b.new_page(viewport={'width': w, 'height': h}, device_scale_factor=1)
            html = SALIDA / f'_{nombre}.html'
            html.write_text(f'<!doctype html><html><head><meta charset="utf-8"><style>{CSS}</style></head>'
                            f'<body class="{clase}" style="--w:{w}px;--h:{h}px">{cuerpo}</body></html>', encoding='utf-8')
            pg.goto(html.as_uri())
            pg.evaluate('document.fonts.ready')
            pg.wait_for_timeout(300)
            info = pg.evaluate("""()=>{const o=[];document.querySelectorAll('body *').forEach(e=>{const r=e.getBoundingClientRect();
              if(r.width&&(r.right>innerWidth+1||r.bottom>innerHeight+1))o.push('sale '+e.tagName+'.'+e.className+' '+Math.round(r.right)+'x'+Math.round(r.bottom));
              const t=[...e.childNodes].some(n=>n.nodeType==3&&n.textContent.trim());
              if(t&&parseFloat(getComputedStyle(e).fontSize)<26)o.push('chica '+e.className)});return o}""")
            pg.screenshot(path=str(SALIDA / f'{nombre}.png'))
            html.unlink()
            problemas += bool(info)
            print(nombre, f'{w}x{h}', info or 'ok')
            pg.close()
        b.close()
    print('piezas:', len(P), '· con avisos:', problemas)

if __name__ == '__main__':
    armar()
