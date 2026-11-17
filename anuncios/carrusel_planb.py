"""Carrusel «Plan B» de Experiencias Patagónicas (4:5, 8 tarjetas), misma piel que «La calculadora».

Historia: día 3, 13:40, el viento suspende el velero → lo que pasa si lo armaste por tu cuenta →
el error → el mismo día con el plan B escrito → el plan B de cada día → lo que se lleva tu grupo →
las fechas → «Comentá PLAN B». El programa y los planes B salen de /retiros-2027.

    python3 anuncios/carrusel_planb.py
"""
import pathlib, random
from playwright.sync_api import sync_playwright
from carrusel_calculadora import CSS as BASE, LOGO, LOGO_SVG, PERSONA, ft, W, H, N

SALIDA = pathlib.Path('/home/claude/entregas/marzo/carrusel-plan-b')

random.seed(23)
pts, x = [], 0
while x <= W * N + 60:
    pts.append((x, random.choice([1258, 1270, 1284, 1246, 1292, 1240, 1278])))
    x += random.choice([70, 90, 110, 130])
for k in (len(pts) // 6, len(pts) // 2 + 3, 5 * len(pts) // 6):
    pts[k] = (pts[k][0], 1210)
RUTA = 'M' + ' L'.join(f'{a},{b}' for a, b in pts)

def cordillera(i):
    return (f'<svg class="cord" viewBox="{i * W} 0 {W} {H}" preserveAspectRatio="none">'
            f'<path d="{RUTA}" fill="none" stroke="#C9B27E" stroke-width="2.4" stroke-linejoin="round"/></svg>')

CSS = BASE + """
.notif{background:#FFFDF9;color:#1D2422;border-radius:30px;padding:22px 26px 24px;display:flex;gap:20px;align-items:flex-start;box-shadow:0 30px 60px -36px rgba(18,58,66,.6)}
.notif .ic{flex:none;width:66px;height:66px;border-radius:20px;display:grid;place-items:center;color:#FBF8F2}
.notif .ic svg{width:38px;height:38px}
.notif .cab{display:flex;justify-content:space-between;gap:16px;font:800 27px/1.2 'Manrope'}
.notif .cab span{font-weight:600;color:#4F5B57;white-space:nowrap}
.notif .msg{font:600 33px/1.3 'Manrope';margin-top:6px}
.linea{position:relative;padding-left:58px}
.linea::before{content:"";position:absolute;left:15px;top:30px;bottom:30px;width:2px;background:#C9B27E}
.hito{position:relative;display:flex;align-items:baseline;gap:26px;padding:24px 0}
.hito::before{content:"";position:absolute;left:-54px;top:44px;width:24px;height:24px;border-radius:50%;background:#123A42;border:3px solid #C9B27E}
.hito .h{font-family:'Fraunces',serif;font-variation-settings:"SOFT" 100,"opsz" 144;font-weight:360;font-size:60px;letter-spacing:-.03em;color:#C9B27E;flex:none;width:170px;font-variant-numeric:lining-nums tabular-nums}
.hito .q{font:600 37px/1.3 'Manrope';color:#E9F0EE}
.hito.corte .q{color:#B7CBC8;text-decoration:line-through;text-decoration-color:#B4432F;text-decoration-thickness:3px}
.hito.ok::before{background:#36603F;border-color:#36603F}
.dia{display:flex;gap:28px;align-items:center}
.dia .que{flex:1}
.dia .et{font:800 26px/1.2 'Manrope';letter-spacing:.12em;text-transform:uppercase;color:#9A3E25}
.dia .si{font:600 35px/1.28 'Manrope';margin-top:8px;color:#1D2422}
.dia .si b{font-weight:800}
.pildora{position:relative;height:236px;border-radius:999px;overflow:hidden}
.pildora .ft{position:absolute;inset:0}
.pildora .rot{position:absolute;inset:0;z-index:3;display:flex;align-items:center;justify-content:space-between;padding:0 64px;color:#FFFDF9}
.pildora .rot .cifra{font-size:140px;text-shadow:0 6px 30px rgba(0,0,0,.35)}
.pildora .rot .mes{font:800 32px/1.2 'Manrope';letter-spacing:.12em;text-transform:uppercase;text-shadow:0 2px 16px rgba(0,0,0,.4)}
.pildora::before{content:"";position:absolute;inset:0;z-index:2;background:rgba(10,30,34,.28)}
"""

ICO = {
    'velero': '<path d="M12 3v14M12 4.5 19 15h-7z"/><path d="M3 18h18l-2.5 3h-13z"/>',
    'combi': '<rect x="2" y="7" width="15" height="9" rx="2"/><path d="M17 10h2.6l1.9 3v3H17"/><circle cx="7" cy="17.5" r="1.8"/><circle cx="17" cy="17.5" r="1.8"/>',
    'casa': '<path d="M3.5 11 12 4l8.5 7v9h-17z"/><path d="M10 20v-5h4v5"/>',
    'chat': '<path d="M4 5h16v11H9.5L5 20v-4H4z"/>',
}
def ico(n, fondo):
    return (f'<span class="ic" style="background:{fondo}"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" '
            f'stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round">{ICO[n]}</svg></span>')

def notif(n, fondo, quien, cuando, msg, estilo=''):
    return (f'<div class="notif" style="{estilo}">{ico(n, fondo)}<div style="flex:1"><p class="cab">{quien}<span>{cuando}</span></p>'
            f'<p class="msg">{msg}</p></div></div>')

T = []

# 1 · 13:40
T.append(('lago', f"""{LOGO}
<div style="position:relative;height:680px;margin-top:30px">
  {ft('photo-1579541183120-dbb2ab2aa3c5', 'arco', 'position:absolute;right:0;top:0;width:540px;height:680px', '50% 62%')}
  <p class="cifra" style="position:absolute;left:0;top:60px;font-size:200px;color:#C9B27E">13:40</p>
  {notif('velero', '#123A42', 'Velero', 'ahora', 'Navegación suspendida por viento. Hoy no salimos.', 'position:absolute;left:0;bottom:60px;width:620px')}
</div>
<h1 class="t" style="font-size:96px;margin-top:44px;color:#FFFDF9;text-wrap:wrap">Día 3 de tu retiro.<br><em>Veinte personas te miran.</em></h1>
<p class="sig" style="margin-top:auto;text-align:right">Deslizá →</p>"""))

# 2 · El celular, si lo armaste por tu cuenta
T.append(('', f"""{LOGO}
<p class="ojo" style="margin-top:50px">Si lo armaste por tu cuenta</p>
<h1 class="t" style="font-size:80px;margin-top:18px">Tu celular <em>a las 13:41.</em></h1>
<div style="display:flex;flex-direction:column;gap:22px;margin-top:44px">
  {notif('velero', '#123A42', 'Velero', 'ahora', '¿Lo pasamos para mañana? La seña no se devuelve.')}
  {notif('combi', '#9A3E25', 'Traslados', 'ahora', 'La combi ya salió para el puerto. ¿La volvemos?', 'margin-left:30px')}
  {notif('casa', '#36603F', 'Lodge', 'hace 1 min', 'La sala está ocupada hasta las 18.', 'margin-left:60px')}
  {notif('chat', '#4F5B57', 'Grupo del retiro · 20', '12 mensajes', '¿Al final qué hacemos?', 'margin-left:90px')}
</div>
<p class="t" style="font-size:54px;margin-top:auto;color:#9A3E25;font-style:italic;font-weight:350">Y tu grupo, esperando en el lobby.</p>"""))

# 3 · El error
T.append(('papel', f"""{LOGO}
<p class="ojo" style="margin-top:50px">El error que más cuesta</p>
<h1 class="t" style="font-size:84px;margin-top:18px">Pensar el plan B <em>cuando ya pasó.</em></h1>
{ft('photo-1643494555111-df0141d84a62', 'estadio', 'height:360px;margin-top:40px', '50% 45%')}
<p class="p" style="margin-top:38px;font-size:36px;color:#1D2422">En la Patagonia el clima cambia en una hora. El viento, la lluvia y la nieve son parte del programa.</p>
<div style="margin-top:auto;border-top:1px solid #C9B27E;padding-top:28px">
  <p class="t" style="font-size:54px;line-height:1.05;padding-bottom:8px">Tu grupo no recuerda el viento. <em>Recuerda cómo se resolvió.</em></p></div>"""))

# 4 · El mismo día, con el plan B escrito
HITOS = [('corte', '13:40', 'Velero por el Nahuel Huapi'), ('', '13:45', 'Ailu activa el plan B del día 3'),
         ('ok', '14:00', 'Circuito Chico en traslado privado'), ('ok', '16:30', 'Té en el mirador'),
         ('ok', '19:00', 'Fuego en la playa del lodge, como estaba')]
LIN = ''.join(f'<div class="hito {c}"><span class="h">{h}</span><span class="q">{q}</span></div>' for c, h, q in HITOS)
T.append(('lago', f"""{LOGO}
<p class="ojo" style="margin-top:50px">Con el plan B escrito</p>
<h1 class="t" style="font-size:84px;margin-top:18px;color:#FFFDF9">El mismo día 3, <em>sin una llamada.</em></h1>
<div class="linea" style="margin-top:44px">{LIN}</div>
<p class="t" style="font-size:56px;margin-top:auto;color:#FFFDF9;line-height:1.05;padding-bottom:8px">Vos seguís con tu grupo. <em>Del resto se ocupa Ailu.</em></p>"""))

# 5 · El plan B de cada día
DIAS = [('photo-1647476685001-8510e5591ec3', '50% 50%', 'Día 1 · Llegada', 'Si el vuelo se demora,', 'el traslado espera tu vuelo.'),
        ('photo-1758797316165-986ec92e7ad2', '40% 50%', 'Día 2 · Adentro', 'Si llueve,', 'la caminata pasa a la tarde y la sesión sigue en la sala.'),
        ('photo-1579541183120-dbb2ab2aa3c5', '50% 60%', 'Día 3 · Afuera', 'Si hay viento,', 'Circuito Chico en lugar del velero.'),
        ('photo-1510798831971-661eb04b3739', '50% 50%', 'Día 4 · Cierre', 'Si nieva en la ruta,', 'los traslados salen antes.')]
FILAS = ''.join(f'<div class="dia">{ft(p, "arco", "width:156px;height:192px", pos)}<div class="que"><p class="et">{d}</p>'
                f'<p class="si"><b>{a}</b> {b}</p></div></div>' for p, pos, d, a, b in DIAS)
T.append(('', f"""{LOGO}
<p class="ojo" style="margin-top:50px">Antes de que llegues</p>
<h1 class="t" style="font-size:80px;margin-top:18px">Cada día tiene <em>su plan B.</em></h1>
<div style="display:flex;flex-direction:column;gap:26px;margin-top:40px">{FILAS}</div>"""))

# 6 · Lo que se lleva tu grupo
T.append(('papel', f"""{LOGO}
{ft('photo-1551845728-6820a30c64e2', 'arco', 'height:660px;margin-top:30px', '50% 40%')}
<h1 class="t" style="font-size:86px;margin-top:40px">Tu grupo no se entera del cambio. <em>Se acuerda del lago.</em></h1>
<p class="p" style="margin-top:auto;font-size:33px">Vos das tu contenido. Ailu está en el retiro, de la llegada a la despedida.</p>"""))

# 7 · Las fechas
FECHAS = [('photo-1780345021264-950c42e368f2', '50% 50%', '22', 'Febrero'),
          ('photo-1692199037113-ff28ad03f703', '50% 55%', '8', 'Marzo'),
          ('photo-1598162480222-b2c3d92548d5', '42% 60%', '15', 'Marzo')]
PIL = ''.join(f'<div class="pildora">{ft(p, "", "", pos)}<div class="rot"><p class="cifra">{d}</p><p class="mes">{mes} · 4 noches</p></div></div>'
              for p, pos, d, mes in FECHAS)
T.append(('lago', f"""{LOGO}
<p class="ojo" style="margin-top:50px">Antes de abril</p>
<h1 class="t" style="font-size:88px;margin-top:18px;color:#FFFDF9">Quedan <em>tres fechas.</em></h1>
<div style="display:flex;flex-direction:column;gap:24px;margin-top:44px">{PIL}</div>
<p class="p" style="margin-top:auto;font-size:34px">Cuando una se toma con seña, se tacha.</p>"""))

# 8 · Comentá PLAN B
T.append(('', f"""{LOGO}
<div style="position:relative;height:560px;margin-top:34px">
  {ft('photo-1692199037113-ff28ad03f703', 'arco', 'position:absolute;right:0;top:0;width:540px;height:560px', '50% 55%')}
  <div style="position:absolute;left:0;top:150px;width:580px;display:flex;flex-direction:column;gap:18px">
    <div class="coment"><span class="av" style="background:#E9F0EE">{PERSONA}</span>
      <div><p class="quien">Vos</p><p class="dice" style="font-weight:800;font-size:38px;letter-spacing:.04em">PLAN B</p></div></div>
    <div class="coment" style="margin-left:60px"><span class="av" style="background:#123A42;color:#C9B27E">{LOGO_SVG.replace('<svg', '<svg width="40" height="40"')}</span>
      <div><p class="quien">Experiencias Patagónicas</p><p class="dice">Te mandamos el programa de los 4 días.</p></div></div>
  </div>
</div>
<h1 class="t" style="font-size:110px;margin-top:44px">Comentá <em>PLAN B.</em></h1>
<p class="p" style="margin-top:24px;font-size:34px">Te mandamos el programa de los cuatro días y cómo se arma el plan B de cada uno. Si te cierra, armamos tu retiro en 30 minutos.</p>"""))


def armar():
    SALIDA.mkdir(parents=True, exist_ok=True)
    with sync_playwright() as p:
        b = p.chromium.launch()
        for i, (clase, cuerpo) in enumerate(T):
            nombre = f'carrusel-plan-b-{i + 1}'
            pg = b.new_page(viewport={'width': W, 'height': H}, device_scale_factor=1)
            html = SALIDA / f'_{nombre}.html'
            html.write_text(f'<!doctype html><html><head><meta charset="utf-8"><style>{CSS}</style></head>'
                            f'<body class="{clase}" style="--w:{W}px;--h:{H}px">{cordillera(i)}<div class="cap">{cuerpo}</div></body></html>',
                            encoding='utf-8')
            pg.goto(html.as_uri())
            pg.evaluate('document.fonts.ready')
            pg.wait_for_timeout(400)
            info = pg.evaluate("""()=>{const o=[];const cap=document.querySelector('.cap');const lim=innerHeight-150+1;
              cap.querySelectorAll('*').forEach(e=>{const r=e.getBoundingClientRect();
              if(r.width&&(r.right>innerWidth+1||r.bottom>lim))o.push('sale '+e.tagName+'.'+e.className+' '+Math.round(r.right)+'x'+Math.round(r.bottom));
              const t=[...e.childNodes].some(n=>n.nodeType==3&&n.textContent.trim());
              if(t&&parseFloat(getComputedStyle(e).fontSize)<26)o.push('chica '+e.className+' '+e.textContent.slice(0,20))});return o.slice(0,6)}""")
            pg.screenshot(path=str(SALIDA / f'{nombre}.png'))
            html.unlink()
            print(nombre, info or 'ok')
            pg.close()
        b.close()

if __name__ == '__main__':
    armar()
