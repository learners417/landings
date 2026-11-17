"""Cinco carruseles más de Experiencias Patagónicas (4:5), con la misma piel que «La calculadora»,
«Plan B» y «Antes de las fiestas»: Nieve, Febrero, Abril, Ailu y Javo.

Fechas (página /retiros-2027): verano 22 feb, 8 y 15 mar · otoño (abril) en la llamada ·
invierno 5 jul, 16 y 23 ago, 13 sep. Mayo y junio no se ofrecen.
Las fotos de Ailu y Javo viven fuera del repo (/home/claude/ailu-privadas): sus PNG no se suben.

    python3 anuncios/carruseles_temporada.py            # los cinco
    python3 anuncios/carruseles_temporada.py nieve      # uno
"""
import pathlib, random, sys
from playwright.sync_api import sync_playwright
from build_anuncios import foto, tilde
from carrusel_calculadora import CSS as BASE, LOGO, LOGO_SVG, PERSONA, W, H, N
from carrusel_planb import CSS as PB

PRIV = pathlib.Path('/home/claude/ailu-privadas')
ENTREGAS = pathlib.Path('/home/claude/entregas/marzo')

def src(p):
    """Foto de Unsplash por id, o privada por ruta relativa a ailu-privadas."""
    return foto(p) if p.startswith('photo-') else (PRIV / p).as_uri()

def ft(p, clase='', estilo='', pos='center'):
    return f'<div class="ft {clase}" style="{estilo}"><i style="background-image:url(\'{src(p)}\');--pos:{pos}"></i></div>'

def full(p, pos='center', pano=None):
    extra = '' if pano is None else f'width:{2 * W}px;right:auto;left:{-pano * W}px;'
    return f'<div class="full"><i style="{extra}background-image:url(\'{src(p)}\');--pos:{pos}"></i></div>'

def ruta(seed):
    random.seed(seed)
    pts, x = [], 0
    while x <= W * N + 60:
        pts.append((x, random.choice([1258, 1270, 1284, 1246, 1292, 1240, 1278])))
        x += random.choice([70, 90, 110, 130])
    for k in (len(pts) // 5, len(pts) // 2 + 2, 4 * len(pts) // 5):
        pts[k] = (pts[k][0], 1210)
    return 'M' + ' L'.join(f'{a},{b}' for a, b in pts)

CSS = PB + """
.full{position:absolute;inset:0;z-index:0;overflow:hidden}
.full i{position:absolute;inset:0;background-size:cover;background-position:var(--pos,center);filter:saturate(.88) contrast(1.03)}
.full::after{content:"";position:absolute;inset:0;background:linear-gradient(180deg,rgba(10,30,34,.55) 0%,rgba(10,30,34,0) 20%,rgba(10,30,34,0) 52%,rgba(10,30,34,.5) 100%)}
.sub{position:absolute;left:44px;right:44px;bottom:150px;z-index:3;background:rgba(18,58,66,.93);border-radius:32px;padding:40px 48px 44px;color:#E9F0EE}
.sub .t{color:#FFFDF9}.sub .t em{color:#C9B27E}
.cuando{font:800 27px/1.2 'Manrope';letter-spacing:.12em;text-transform:uppercase;color:#C9B27E}
.pill{display:inline-flex;align-items:center;gap:12px;background:rgba(255,253,249,.95);color:#1D2422;border-radius:999px;padding:16px 26px;font:800 29px/1 'Manrope';box-shadow:0 20px 40px -24px rgba(0,0,0,.6)}
.lista2 p{display:flex;align-items:center;gap:22px;font:600 35px/1.25 'Manrope';padding:18px 0;border-bottom:1px solid rgba(29,36,34,.14)}
.lago .lista2 p{color:#E9F0EE;border-color:rgba(233,240,238,.16)}
.fila{display:flex;gap:16px}
.t4{position:relative;flex:1;height:560px}
.t4 .ft{position:absolute;inset:0}
.t4 .d{position:absolute;left:0;right:0;top:150px;z-index:3;text-align:center;color:#FFFDF9}
.t4 .d .cifra{font-size:116px;text-shadow:0 6px 30px rgba(0,0,0,.4)}
.t4 .d .mm{font:800 28px/1 'Manrope';letter-spacing:.16em;text-transform:uppercase;margin-top:22px;text-shadow:0 2px 16px rgba(0,0,0,.45)}
.razon{display:flex;gap:24px;align-items:center;padding:20px 0;border-bottom:1px solid rgba(29,36,34,.14)}
.razon .ico{flex:none;width:84px;height:84px;border-radius:50%;background:#123A42;color:#C9B27E;display:grid;place-items:center}
.lago .razon .ico{background:rgba(233,240,238,.1)}
.razon .ico svg{width:44px;height:44px}
.razon p{font:600 35px/1.25 'Manrope'}
.razon p b{font-weight:800}
.semana{flex:1;border-radius:999px;border:2px solid rgba(233,240,238,.3);padding:26px 0;text-align:center}
.semana p{font:800 27px/1 'Manrope';letter-spacing:.12em;text-transform:uppercase;color:#B7CBC8}
.semana b{display:block;font-family:'Fraunces',serif;font-weight:380;font-size:78px;line-height:1;color:#FFFDF9;margin-top:10px}
.estacion{flex:1;display:flex;flex-direction:column}
.estacion .ft{height:500px}
.estacion h3{font-family:'Fraunces',serif;font-weight:400;font-size:52px;margin-top:22px;letter-spacing:-.02em}
.estacion p{font:600 30px/1.3 'Manrope';color:#4F5B57;margin-top:8px}
.cita{font-family:'Fraunces',serif;font-variation-settings:"SOFT" 100,"opsz" 144;font-weight:360;font-style:italic;font-size:58px;line-height:1.12;letter-spacing:-.02em}
"""

ICO = {
    'sol': '<circle cx="12" cy="12" r="4.2"/><path d="M12 2.5v2.2M12 19.3v2.2M2.5 12h2.2M19.3 12h2.2M5.3 5.3l1.6 1.6M17.1 17.1l1.6 1.6M5.3 18.7l1.6-1.6M17.1 6.9l1.6-1.6"/>',
    'ola': '<path d="M2.5 9.5c2.2 0 2.2-1.6 4.4-1.6s2.2 1.6 4.4 1.6 2.2-1.6 4.4-1.6 2.2 1.6 4.4 1.6"/><path d="M2.5 15c2.2 0 2.2-1.6 4.4-1.6s2.2 1.6 4.4 1.6 2.2-1.6 4.4-1.6 2.2 1.6 4.4 1.6"/>',
    'monte': '<path d="M2.5 19.5 9 8.5l3.6 6 2.6-4 6.3 9z"/>',
    'hoja': '<path d="M5 19c0-8 5-13 14-14-.5 9-6 14-14 14z"/><path d="M5 19 13 11"/>',
    'fuego': '<path d="M12 21c-3.6 0-6-2.4-6-5.6 0-3.4 2.6-5 3.6-8.4 1.6 1.2 2.4 2.8 2.4 4.4 1-.6 1.8-1.8 2-3 1.8 1.6 4 4 4 7 0 3.2-2.4 5.6-6 5.6z"/>',
    'luz': '<path d="M4 18h16"/><path d="M6.5 18a5.5 5.5 0 0 1 11 0"/><path d="M12 6.5V9M5.6 9.6l1.6 1.6M18.4 9.6l-1.6 1.6"/>',
    'tren': '<path d="M3 17h18M5 17V9l4-3h6l4 3v8"/><path d="M9 12h6"/>',
    'copo': '<path d="M12 3v18M4.2 7.5l15.6 9M4.2 16.5l15.6-9"/><path d="M9.5 4.5 12 6l2.5-1.5M9.5 19.5 12 18l2.5 1.5"/>',
}
def ico(n):
    return (f'<span class="ico"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" '
            f'stroke-linecap="round" stroke-linejoin="round">{ICO[n]}</svg></span>')

def comentario(palabra, respuesta, foto_arco, pos='50% 50%', fondo='lago', cuerpo=''):
    color = '#FFFDF9' if fondo == 'lago' else '#1D2422'
    return (fondo, '', f"""{LOGO}
<div style="position:relative;height:560px;margin-top:34px">
  {ft(foto_arco, 'arco', 'position:absolute;right:0;top:0;width:540px;height:560px', pos)}
  <div style="position:absolute;left:0;top:150px;width:590px;display:flex;flex-direction:column;gap:18px">
    <div class="coment"><span class="av" style="background:#E9F0EE">{PERSONA}</span>
      <div><p class="quien">Vos</p><p class="dice" style="font-weight:800;font-size:38px;letter-spacing:.04em">{palabra}</p></div></div>
    <div class="coment" style="margin-left:60px"><span class="av" style="background:#123A42;color:#C9B27E">{LOGO_SVG.replace('<svg', '<svg width="40" height="40"')}</span>
      <div><p class="quien">Experiencias Patagónicas</p><p class="dice">{respuesta}</p></div></div>
  </div>
</div>
<h1 class="t" style="font-size:110px;margin-top:44px;color:{color}">Comentá <em>{palabra}.</em></h1>
<p class="p" style="margin-top:24px;font-size:34px">{cuerpo}</p>""")

def sub(cuando, titulo, tam=78, extra=''):
    return (f'<div class="sub"><p class="cuando">{cuando}</p>'
            f'<h1 class="t" style="font-size:{tam}px;margin-top:18px;text-wrap:wrap">{titulo}</h1>{extra}</div>')

DESLIZA = ('<div style="display:flex;justify-content:flex-end;margin-top:26px;padding-top:22px;border-top:1px solid rgba(201,178,126,.5)">'
           '<p class="sig">Deslizá →</p></div>')

def hitos(lista, ancho=170):
    return '<div class="linea">' + ''.join(
        f'<div class="hito {c}"><span class="h" style="width:{ancho}px">{h}</span><span class="q">{q}</span></div>' for c, h, q in lista) + '</div>'

def tick_lista(items):
    return '<div class="lista2">' + ''.join(f'<p>{tilde(48)}<span>{x}</span></p>' for x in items) + '</div>'

C = {}

# ───────────────────────── 1 · NIEVE ─────────────────────────
C['nieve'] = (11, [
    ('lago', full('photo-1510798831971-661eb04b3739', '50% 40%'), f"""{LOGO}
<div style="margin-top:56px"><span class="pill">{tilde(34)} Afuera nieva. Adentro, fuego.</span></div>
{sub('Julio en Bariloche', 'El retiro que tu grupo va a contar <em>toda la vida.</em>', 84, DESLIZA)}"""),
    ('papel', '', f"""{LOGO}
<p class="ojo" style="margin-top:50px">Tu próximo retiro</p>
<h1 class="t" style="font-size:86px;margin-top:18px">Un retiro de verano se parece a otro. <em>Uno con nieve, no.</em></h1>
{ft('photo-1505322266409-1c77f8b33a8a', 'arco', 'height:500px;margin-top:40px', '50% 55%')}
<p class="p" style="margin-top:auto;font-size:35px;color:#1D2422">Abren la ventana y el bosque está blanco. Esa foto vende tu próxima edición.</p>"""),
    ('lago', '', f"""{LOGO}
<p class="ojo" style="margin-top:50px">Día 2 · Adentro</p>
<h1 class="t" style="font-size:84px;margin-top:18px;color:#FFFDF9">Un día de retiro <em>en la nieve.</em></h1>
<div style="margin-top:36px">{hitos([('', '08:30', 'Desayuno frente al ventanal'), ('', '10:00', 'Tu sesión, con la estufa encendida'), ('', '13:00', 'Almuerzo largo de cocina patagónica'), ('ok', '15:30', 'Caminata con raquetas por el bosque'), ('ok', '18:00', 'Chocolate caliente y fuego'), ('ok', '21:00', 'Cena de autor')])}</div>"""),
    ('', '', f"""{LOGO}
<p class="ojo" style="margin-top:50px">La pregunta de siempre</p>
<div style="display:flex;gap:30px;align-items:center;margin-top:18px">
  <h1 class="t" style="font-size:90px;flex:1">¿Y si nieva <em>demasiado?</em></h1>
  {ft('photo-1708604010245-59d0c22cf9e9', 'circ', 'width:280px;height:280px', '60% 50%')}
</div>
<div style="margin-top:40px">
  <div class="razon">{ico('tren')}<p><b>Los traslados salen antes</b> y llegan con tiempo.</p></div>
  <div class="razon">{ico('copo')}<p><b>La salida cambia</b> de horario o de lugar.</p></div>
  <div class="razon" style="border:0">{ico('fuego')}<p><b>El fuego sigue</b> y la sesión, también.</p></div>
</div>
<p class="t" style="font-size:56px;margin-top:auto;line-height:1.06;padding-bottom:8px">El plan B de invierno <em>está escrito antes de que llegues.</em></p>"""),
    ('lago', full('photo-1675612380153-e800ffa0aa09', '50% 50%'), f"""{LOGO}
{sub('Para tu comunidad', 'Si tu grupo viene de Brasil, México o Colombia, <em>puede ser la primera vez que ve nevar.</em>', 66)}"""),
    ('papel', '', f"""{LOGO}
<p class="ojo" style="margin-top:50px">Llave en mano</p>
<h1 class="t" style="font-size:84px;margin-top:18px">Todo producido, <em>vos solo llegás.</em></h1>
{ft('photo-1607712617949-8c993d290809', 'estadio', 'height:250px;margin-top:34px', '50% 50%')}
<div style="margin-top:20px">{tick_lista(['Lodge con estufa y vista', 'Cocina de autor los cuatro días', 'Traslados y salidas en la nieve', 'Sala para tus sesiones y plan B'])}</div>
<p class="p" style="margin-top:auto;font-size:33px;color:#1D2422;font-weight:700">Y Ailu en el retiro, de la llegada a la despedida.</p>"""),
    ('lago', '', f"""{LOGO}
<p class="ojo" style="margin-top:50px">Julio a septiembre</p>
<h1 class="t" style="font-size:90px;margin-top:18px;color:#FFFDF9">Cuatro semanas <em>de nieve.</em></h1>
<div class="fila" style="margin-top:40px">""" + ''.join(
        f'<div class="t4">{ft(p, "arco", "", pos)}<div class="d"><p class="cifra">{d}</p><p class="mm">{m}</p></div></div>'
        for p, pos, d, m in [('photo-1505322266409-1c77f8b33a8a', '50% 50%', '5', 'jul'), ('photo-1510798831971-661eb04b3739', '50% 45%', '16', 'ago'),
                             ('photo-1675612380153-e800ffa0aa09', '45% 50%', '23', 'ago'), ('photo-1708604010245-59d0c22cf9e9', '70% 50%', '13', 'sep')]) + """</div>
<p class="p" style="margin-top:auto;font-size:34px">Cuando una se toma con seña, se tacha.</p>"""),
    comentario('NIEVE', 'Te mandamos las fechas de invierno y la calculadora.', 'photo-1510798831971-661eb04b3739', '50% 45%', 'papel',
               'Hacés tu cuenta y, si te cierra, Ailu arma tu retiro de invierno en una llamada de 30 minutos.'),
])

# ───────────────────────── 2 · FEBRERO ─────────────────────────
PANO = 'photo-1780345021264-950c42e368f2'
C['febrero'] = (29, [
    ('lago', full(PANO, '30% 50%', 0), f"""{LOGO}
{sub('Verano 2027', 'Arrancá el año con tu grupo <em>frente al lago.</em>', 86, DESLIZA)}"""),
    ('lago', full(PANO, '30% 50%', 1), f"""{LOGO}
<div class="sub"><p class="cuando">Febrero</p>
  <div style="display:flex;align-items:flex-end;gap:30px;margin-top:10px">
    <p class="cifra" style="font-size:250px;color:#C9B27E;line-height:.8">22</p>
    <h1 class="t" style="font-size:60px;padding-bottom:10px">Febrero tiene <em>una sola semana.</em></h1></div></div>"""),
    ('papel', '', f"""{LOGO}
<p class="ojo" style="margin-top:50px">Por qué febrero</p>
<h1 class="t" style="font-size:88px;margin-top:18px">Febrero, <em>el verano entero.</em></h1>
{ft('photo-1551845728-6820a30c64e2', 'arco', 'height:440px;margin-top:36px', '50% 40%')}
<div style="margin-top:20px">
  <div class="razon">{ico('sol')}<p><b>Días largos:</b> la luz dura hasta tarde.</p></div>
  <div class="razon">{ico('ola')}<p><b>El lago,</b> para navegar y nadar.</p></div>
  <div class="razon" style="border:0">{ico('monte')}<p><b>Las cumbres</b> a la vista.</p></div>
</div>"""),
    ('lago', '', f"""{LOGO}
<p class="ojo" style="margin-top:50px">Lo que pocos ven</p>
<h1 class="t" style="font-size:84px;margin-top:18px;color:#FFFDF9">Lo que tu grupo decide en febrero, <em>lo trabaja con vos todo el año.</em></h1>
{ft('photo-1599341301512-ca6d7a851fba', 'arco', 'height:460px;margin-top:44px', '50% 60%')}
<p class="p" style="margin-top:auto;font-size:38px">Un retiro en febrero es el arranque de tu programa del año.</p>"""),
    ('lago', '', f"""{LOGO}
<p class="ojo" style="margin-top:50px">La cuenta regresiva</p>
<h1 class="t" style="font-size:86px;margin-top:18px;color:#FFFDF9">De hoy <em>al 22 de febrero.</em></h1>
<div style="margin-top:36px">{hitos([('', 'Hoy', 'Hablás 30 minutos con Ailu'), ('', '48 h', 'Tenés tu propuesta: lugar, programa y presupuesto'), ('', 'Seña', 'La fecha es tuya y salís a vender'), ('', '8 ene', 'Fecha límite: tus 12 lugares'), ('ok', '22 feb', 'Llega tu grupo')], 160)}</div>
<p class="t" style="font-size:58px;margin-top:auto;color:#FFFDF9;line-height:1.06;padding-bottom:8px">Desde el 8 de enero, <em>solo te ocupás de llegar.</em></p>"""),
    ('lago', full('photo-1579541183120-dbb2ab2aa3c5', '50% 60%'), f"""{LOGO}
{sub('Día 3 · Afuera', 'Velero privado por el Nahuel Huapi, <em>con el sol bajando.</em>', 80)}"""),
    ('papel', '', f"""{LOGO}
<p class="ojo" style="margin-top:50px">Verano 2027</p>
<h1 class="t" style="font-size:88px;margin-top:18px">Febrero o <em>marzo.</em></h1>
<div class="fila" style="margin-top:40px;align-items:flex-end">
  <div class="t4" style="flex:1.5;height:640px">{ft('photo-1780345021264-950c42e368f2', 'arco', '', '45% 50%')}<div class="d" style="top:180px"><p class="cifra" style="font-size:170px">22</p><p class="mm">febrero</p></div></div>
  <div class="t4" style="height:500px">{ft('photo-1598162480222-b2c3d92548d5', 'arco', '', '42% 55%')}<div class="d"><p class="cifra">8</p><p class="mm">mar</p></div></div>
  <div class="t4" style="height:500px">{ft('photo-1692199037113-ff28ad03f703', 'arco', '', '50% 55%')}<div class="d"><p class="cifra">15</p><p class="mm">mar</p></div></div>
</div>
<p class="p" style="margin-top:auto;font-size:34px;color:#1D2422">La del 22 de febrero es la única del mes. Cuando se toma con seña, se tacha.</p>"""),
    comentario('FEBRERO', 'Te mandamos el programa y la calculadora.', 'photo-1551845728-6820a30c64e2', '50% 40%', 'lago',
               'Hacés tu cuenta con tus números y, si te cierra, la semana del 22 es tuya con la seña.'),
])

# ───────────────────────── 3 · ABRIL ─────────────────────────
C['abril'] = (53, [
    ('lago', full('photo-1768847074569-32311434f343', '50% 45%'), f"""{LOGO}
{sub('Lo que no está en la página', 'Hay un mes para retiros <em>que no publicamos.</em>', 88, DESLIZA)}"""),
    ('papel', '', f"""{LOGO}
<p class="ojo" style="margin-top:50px">El mes</p>
<h1 class="t" style="font-size:96px;margin-top:18px">Abril. <em>El otoño en la Patagonia.</em></h1>
{ft('photo-1763477893101-70d85f5c3414', 'arco', 'height:520px;margin-top:40px', '50% 55%')}
<p class="p" style="margin-top:auto;font-size:35px;color:#1D2422">Las lengas y los ñires se ponen rojos y dorados, y el bosque cambia de color.</p>"""),
    ('lago', '', f"""{LOGO}
<p class="ojo" style="margin-top:50px">Lo que cambia</p>
<h1 class="t" style="font-size:90px;margin-top:18px;color:#FFFDF9">Abril <em>se vive distinto.</em></h1>
{ft('photo-1768777406446-643fc73cabc0', 'estadio', 'height:300px;margin-top:40px', '50% 50%')}
<div style="margin-top:20px">{''.join(f'<div class="razon" style="border-color:rgba(233,240,238,.16){";border:0" if i == 2 else ""}">{ico(k)}<p style="color:#E9F0EE">{t}</p></div>' for i, (k, t) in enumerate([('hoja', '<b style="color:#FFFDF9">Terminó la temporada alta:</b> senderos y miradores más tranquilos.'), ('fuego', '<b style="color:#FFFDF9">Vuelve el fuego</b> a la noche.'), ('luz', '<b style="color:#FFFDF9">La luz de la tarde</b> se pone dorada.')]))}</div>"""),
    ('lago', full('photo-1761897190222-d222d88851c9', '50% 55%'), f"""{LOGO}
{sub('Día 2 · Adentro', 'Tu sesión, con el bosque <em>de fondo.</em>', 86)}"""),
    ('lago', '', f"""{LOGO}
<p class="ojo" style="margin-top:50px">Por qué no está en la página</p>
<h1 class="t" style="font-size:84px;margin-top:18px;color:#FFFDF9">Abril se arma <em>a medida, en la llamada.</em></h1>
<p class="p" style="margin-top:30px;font-size:35px">La semana, el lodge y el programa, para tu grupo.</p>
<div class="fila" style="margin-top:44px">{''.join(f'<div class="semana"><p>Semana</p><b>{n}</b></div>' for n in range(1, 5))}</div>
{ft('photo-1763477893101-70d85f5c3414', 'estadio', 'height:300px;margin-top:40px', '50% 60%')}
<p class="t" style="font-size:62px;margin-top:auto;color:#FFFDF9;line-height:1.05;padding-bottom:8px">Un grupo por semana. <em>Abril tiene cuatro.</em></p>"""),
    ('papel', '', f"""{LOGO}
<p class="ojo" style="margin-top:50px">Llave en mano</p>
<h1 class="t" style="font-size:84px;margin-top:18px">Todo producido, <em>vos solo llegás.</em></h1>
{ft('photo-1784871258457-3a4b0c4de37f', 'estadio', 'height:250px;margin-top:34px', '50% 50%')}
<div style="margin-top:20px">{tick_lista(['Lodge frente al lago', 'Cocina de autor los cuatro días', 'Traslados y salidas por el bosque', 'Sala para tus sesiones y plan B'])}</div>
<p class="p" style="margin-top:auto;font-size:33px;color:#1D2422;font-weight:700">Y Ailu en el retiro, de la llegada a la despedida.</p>"""),
    ('lago', full('photo-1768777406446-643fc73cabc0', '50% 50%'), f"""{LOGO}
{sub('Abril en Bariloche', 'Primeras nieves en las cumbres <em>y dorado abajo.</em>', 86)}"""),
    comentario('ABRIL', 'Ailu te escribe para ver tu semana.', 'photo-1768847074569-32311434f343', '50% 45%', 'papel',
               'Le contás tu grupo y te propone la semana de abril que mejor le queda.'),
])

# ───────────────────────── 4 · AILU ─────────────────────────
A1, A2, A3 = 'video-equipo/cuadro-16.jpg', 'video-equipo/cuadro-22.jpg', 'video-equipo/cuadro-07.jpg'
C['ailu'] = (71, [
    ('lago', full(A1, '50% 30%'), f"""{LOGO}
{sub('Experiencias Patagónicas', 'Ella es la persona que atiende tu retiro <em>a las 11 de la noche.</em>', 78, DESLIZA)}"""),
    ('papel', '', f"""{LOGO}
<p class="ojo" style="margin-top:50px">Quién lo produce</p>
<div style="display:flex;gap:34px;align-items:center;margin-top:24px">
  {ft(A2, 'circ', 'width:340px;height:340px', '50% 33%')}
  <h1 class="t" style="font-size:110px;flex:1">Soy <em>Ailu.</em></h1>
</div>
<p class="cita" style="margin-top:50px;font-size:68px">«Vengo de las cocinas de Bariloche, de Madurado, Alma del Lago y El Nido del Cóndor.»</p>
<p class="p" style="margin-top:auto;font-size:35px;color:#1D2422">Hace más de cuatro años produzco experiencias en la Patagonia.</p>"""),
    ('lago', '', f"""{LOGO}
<p class="ojo" style="margin-top:50px">Por eso</p>
<h1 class="t" style="font-size:90px;margin-top:18px;color:#FFFDF9">Sabe a quién llamar <em>para cada cosa.</em></h1>
{ft('photo-1562050344-f7ad946cee35', 'estadio calida', 'height:300px;margin-top:40px', '50% 55%')}
<div style="margin-top:20px">{tick_lista(['El lodge y la cocina', 'Los traslados y el velero', 'El guía, la sala y el fotógrafo'])}</div>"""),
    ('', '', f"""{LOGO}
<p class="ojo" style="margin-top:50px">Su regla</p>
<div style="display:flex;align-items:flex-end;gap:30px;margin-top:40px">
  <p class="cifra" style="font-size:380px;color:#123A42;line-height:.78">1</p>
  <h1 class="t" style="font-size:72px;line-height:1.02;padding-bottom:10px">retiro <em>por semana.</em></h1>
</div>
<p class="cita" style="margin-top:60px;color:#9A3E25">Cada grupo la tiene entera, de la llegada a la despedida.</p>
{ft('photo-1758797316165-986ec92e7ad2', 'estadio', 'height:240px;margin-top:auto', '45% 50%')}"""),
    ('lago', full(A3, '50% 30%'), f"""{LOGO}
{sub('La mesa', 'Cocina de autor en cada comida, <em>con el menú de cada persona resuelto.</em>', 70)}"""),
    ('papel', '', f"""{LOGO}
<p class="ojo" style="margin-top:50px">Con nosotras</p>
<h1 class="t" style="font-size:86px;margin-top:18px">Hablás con Ailu, <em>y Ailu habla con todos.</em></h1>
<div style="margin-top:36px">{tick_lista(['Elige el lodge y arma la mesa', 'Coordina traslados y salidas', 'Escribe el plan B de cada día', 'Está en el retiro, todos los días'])}</div>"""),
    ('lago', '', f"""{LOGO}
<p class="ojo" style="margin-top:50px">El primer paso</p>
<h1 class="t" style="font-size:90px;margin-top:18px;color:#FFFDF9">La llamada de 30 minutos <em>es con ella.</em></h1>
<div style="display:flex;gap:34px;align-items:center;margin-top:50px">
  {ft(A2, 'circ', 'width:300px;height:300px', '50% 33%')}
  <p class="p" style="font-size:38px;flex:1">Le contás tu grupo y tu fecha. En 48 horas tenés tu propuesta, con tus números.</p>
</div>
<div style="margin-top:auto;border-top:1px solid #C9B27E;padding-top:24px"><p class="cuando">Verano · otoño · nieve</p><p class="t" style="font-size:50px;color:#FFFDF9;margin-top:12px;line-height:1.1">22 feb · 8 y 15 mar · abril<br>5 jul · 16 y 23 ago · 13 sep</p></div>"""),
    comentario('AILU', 'Hola, soy Ailu. Te escribo por mensaje.', A1, '50% 30%', 'papel',
               'Te escribe ella para conocer a tu grupo y ver qué fecha te queda mejor.'),
])

# ───────────────────────── 5 · JAVO ─────────────────────────
J1, J2 = 'foto-3.jpg', 'foto-2.jpg'
C['javo'] = (97, [
    ('lago', full(J1, '50% 36%'), f"""{LOGO}
{sub('Javo Katz · mentor', 'Mi primer programa de cinco cifras <em>incluía venir a Bariloche.</em>', 76, DESLIZA)}"""),
    ('papel', '', f"""{LOGO}
<p class="ojo" style="margin-top:50px">Quién te habla</p>
<h1 class="t" style="font-size:80px;margin-top:18px">Acompaño a profesionales que atienden uno a uno <em>a vender programas de alto valor.</em></h1>
{ft('photo-1778694277039-5cbf0b9a1fcf', 'arco calida', 'height:420px;margin-top:40px', '60% 50%')}
<p class="p" style="margin-top:auto;font-size:34px;color:#1D2422">Lo que más disfruto es el encuentro en persona con los más comprometidos.</p>"""),
    ('lago', '', f"""{LOGO}
<p class="ojo" style="margin-top:50px">Lo que aprendí</p>
<h1 class="t" style="font-size:96px;margin-top:18px;color:#FFFDF9">Un curso se compara con otro. <em>Un viaje con tu mentor, no.</em></h1>
{ft('photo-1578592391689-0e3d1a1b52b9', 'estadio', 'height:330px;margin-top:auto', '50% 55%')}"""),
    ('', '', f"""{LOGO}
<p class="ojo" style="margin-top:50px">Por eso</p>
<h1 class="t" style="font-size:88px;margin-top:18px">Mi programa más alto <em>incluye Bariloche.</em></h1>
<p class="p" style="margin-top:28px;font-size:35px;color:#1D2422">Se llama La Cima: días en la Patagonia para trabajar, grabar y estar en la naturaleza.</p>
{ft('photo-1598162480222-b2c3d92548d5', 'arco', 'height:640px;margin-top:auto', '42% 55%')}"""),
    ('lago', full(A1, '50% 30%'), f"""{LOGO}
{sub('¿Quién lo produce?', 'Yo pongo el contenido. <em>Ailu, todo lo demás.</em>', 82,
     '<p class="p" style="font-size:33px;margin-top:20px;color:#DCE8E6">El lodge, la mesa, los traslados y el plan B de cada día.</p>')}"""),
    ('papel', '', f"""{LOGO}
<p class="ojo" style="margin-top:50px">Tu año en Bariloche</p>
<h1 class="t" style="font-size:84px;margin-top:18px">Elegí la temporada <em>de tu grupo.</em></h1>
<div class="fila" style="margin-top:44px;gap:22px">
  <div class="estacion">{ft('photo-1780345021264-950c42e368f2', 'arco', '', '45% 50%')}<h3>Verano</h3><p>22 feb<br>8 y 15 mar</p></div>
  <div class="estacion">{ft('photo-1763477893101-70d85f5c3414', 'arco', '', '50% 55%')}<h3>Otoño</h3><p>Abril,<br>en la llamada</p></div>
  <div class="estacion">{ft('photo-1505322266409-1c77f8b33a8a', 'arco', '', '50% 50%')}<h3>Nieve</h3><p>5 jul · 16 y 23 ago<br>13 sep</p></div>
</div>"""),
    comentario('VIAJE', 'Te mandamos las fechas del año y la calculadora.', J1, '50% 36%', 'lago',
               'Hacés tu cuenta y, si te cierra, Ailu arma el viaje de tu programa en una llamada de 30 minutos.'),
])


def armar(nombre, seed, tarjetas):
    salida = ENTREGAS / f'carrusel-{nombre}'
    salida.mkdir(parents=True, exist_ok=True)
    ruta_ = ruta(seed)
    with sync_playwright() as p:
        b = p.chromium.launch()
        for i, (clase, fondo, cuerpo) in enumerate(tarjetas):
            archivo = f'carrusel-{nombre}-{i + 1}'
            pg = b.new_page(viewport={'width': W, 'height': H}, device_scale_factor=1)
            html = salida / f'_{archivo}.html'
            cord = (f'<svg class="cord" viewBox="{i * W} 0 {W} {H}" preserveAspectRatio="none">'
                    f'<path d="{ruta_}" fill="none" stroke="#C9B27E" stroke-width="2.4" stroke-linejoin="round"/></svg>')
            html.write_text(f'<!doctype html><html><head><meta charset="utf-8"><style>{CSS}</style></head>'
                            f'<body class="{clase}" style="--w:{W}px;--h:{H}px">{fondo}{cord}<div class="cap">{cuerpo}</div></body></html>',
                            encoding='utf-8')
            pg.goto(html.as_uri())
            pg.evaluate('document.fonts.ready')
            pg.wait_for_timeout(500)
            info = pg.evaluate("""()=>{const o=[];const cap=document.querySelector('.cap');const lim=innerHeight-150+4;
              cap.querySelectorAll('*').forEach(e=>{const r=e.getBoundingClientRect();
              if(r.width&&!e.closest('.sub')&&(r.right>innerWidth+1||r.bottom>lim))o.push('sale '+e.tagName+'.'+e.className+' '+Math.round(r.right)+'x'+Math.round(r.bottom));
              const s=document.querySelector('.sub');if(s){const q=s.getBoundingClientRect();if(q.top<200)o.push('sub alta '+Math.round(q.top))}
              const t=[...e.childNodes].some(n=>n.nodeType==3&&n.textContent.trim());
              if(t&&parseFloat(getComputedStyle(e).fontSize)<26)o.push('chica '+e.className+' '+e.textContent.slice(0,20))});return [...new Set(o)].slice(0,6)}""")
            pg.screenshot(path=str(salida / f'{archivo}.png'))
            html.unlink()
            print(archivo, info or 'ok')
            pg.close()
        b.close()

if __name__ == '__main__':
    elegidos = sys.argv[1:] or list(C)
    for n in elegidos:
        seed, tarjetas = C[n]
        armar(n, seed, tarjetas)
