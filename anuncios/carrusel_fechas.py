"""Carrusel «Antes de las fiestas» de Experiencias Patagónicas (4:5, 8 tarjetas), misma piel que
«La calculadora» y «Plan B».

Historia: tu retiro de marzo se vende antes de las fiestas → elegiste el 15 de marzo y parece que
sobra tiempo → la cuenta regresiva (la fecha límite es 45 días antes, cuando el lodge deja de
cancelarse sin cargo) → el error de empezar en enero (2 lugares por semana contra 4) → cada fecha
con su fecha límite → arrancar es una llamada → del 13 al 20 son tuyos → «Comentá MARZO».
Los 12 lugares de equilibrio y los US$ 25.164 salen de la calculadora (20 personas, US$ 3.000,
4 noches, Premium). Las fiestas se cuentan del 21 de diciembre al 6 de enero.

    python3 anuncios/carrusel_fechas.py
"""
import pathlib, random
from datetime import date, timedelta
from playwright.sync_api import sync_playwright
from carrusel_calculadora import CSS as BASE, LOGO, LOGO_SVG, PERSONA, ft, W, H, N, C, m
from carrusel_planb import CSS as PB

SALIDA = pathlib.Path('/home/claude/entregas/marzo/carrusel-antes-de-las-fiestas')
MESES = ['ene', 'feb', 'mar', 'abr', 'may', 'jun', 'jul', 'ago', 'sep', 'oct', 'nov', 'dic']
def f(d):
    return f'{d.day} {MESES[d.month - 1]}'

FECHAS = [date(2027, 2, 22), date(2027, 3, 8), date(2027, 3, 15)]
LIM = [x - timedelta(days=45) for x in FECHAS]
assert [f(x) for x in LIM] == ['8 ene', '22 ene', '29 ene']
# semanas de venta para el 15 de marzo, sin las fiestas (21 dic al 6 ene)
DIC = (date(2026, 12, 20) - date(2026, 12, 1)).days + 1        # 20 días
ENE = (LIM[2] - date(2027, 1, 7)).days + 1                      # 23 días
assert round((DIC + ENE) / 7) == 6 and round(ENE / 7) == 3
assert C['eq'] == 12 and C['eq'] / 6 == 2 and C['eq'] / 3 == 4

random.seed(41)
pts, x = [], 0
while x <= W * N + 60:
    pts.append((x, random.choice([1256, 1268, 1282, 1248, 1292, 1240, 1276])))
    x += random.choice([70, 90, 110, 130])
for k in (len(pts) // 4, 3 * len(pts) // 5, 7 * len(pts) // 8):
    pts[k] = (pts[k][0], 1212)
RUTA = 'M' + ' L'.join(f'{a},{b}' for a, b in pts)

def cordillera(i):
    return (f'<svg class="cord" viewBox="{i * W} 0 {W} {H}" preserveAspectRatio="none">'
            f'<path d="{RUTA}" fill="none" stroke="#C9B27E" stroke-width="2.4" stroke-linejoin="round"/></svg>')

CSS = PB + """
.evento{background:#FFFDF9;color:#1D2422;border-radius:30px;padding:20px 24px;display:flex;gap:22px;align-items:center;box-shadow:0 34px 64px -36px rgba(18,58,66,.6)}
.evento .cal{flex:none;width:104px;border-radius:22px;overflow:hidden;text-align:center;background:#F4EFE6}
.evento .cal p{font:800 26px/1 'Manrope';letter-spacing:.12em;text-transform:uppercase;color:#FFFDF9;background:#123A42;padding:9px 0}
.evento .cal b{display:block;font-family:'Fraunces',serif;font-weight:380;font-size:62px;line-height:1;padding:8px 0 10px;color:#123A42}
.evento.rojo .cal p{background:#B4432F}
.evento .tit{font:800 31px/1.2 'Manrope'}
.evento .sub{font:600 28px/1.3 'Manrope';color:#4F5B57;margin-top:4px}
.meses{display:grid;grid-template-columns:repeat(4,1fr);gap:14px}
.mes{position:relative;border-radius:999px;border:2px solid rgba(29,36,34,.18);padding:26px 0 24px;text-align:center}
.mes .n{font:800 28px/1 'Manrope';letter-spacing:.14em;text-transform:uppercase;color:#4F5B57}
.mes .c{font-family:'Fraunces',serif;font-weight:380;font-size:64px;line-height:1;margin-top:10px;color:#1D2422}
.mes.lim{border-color:#B4432F;background:#B4432F}.mes.lim .n,.mes.lim .c{color:#FFFDF9}
.mes.fin{border-color:#36603F;background:#36603F}.mes.fin .n,.mes.fin .c{color:#FFFDF9}
.mes.fiesta{background:repeating-linear-gradient(135deg,rgba(29,36,34,.06) 0 10px,transparent 10px 20px)}
.ritmo{border-radius:34px;padding:26px 32px 28px}
.ritmo .cab{display:flex;justify-content:space-between;align-items:baseline}
.ritmo .cab p{font:800 30px/1.2 'Manrope'}
.ritmo .cab .cifra{font-size:84px}
.sem{display:flex;gap:12px;margin-top:22px;align-items:flex-end;height:250px}
.sem div{flex:1;display:flex;flex-direction:column-reverse;gap:6px;align-items:center;border-bottom:2px solid rgba(29,36,34,.2);padding-bottom:10px}
.sem i{width:40px;height:40px;border-radius:50%}
.ritmo .pie2{font:600 30px/1.3 'Manrope';margin-top:16px}
.tile{position:relative;flex:1;height:600px}
.tile .ft{position:absolute;inset:0}
.tile .d{position:absolute;left:0;right:0;top:130px;z-index:3;text-align:center;color:#FFFDF9}
.tile .d .cifra{font-size:140px;text-shadow:0 6px 30px rgba(0,0,0,.35)}
.tile .d .mm{font:800 30px/1 'Manrope';letter-spacing:.16em;text-transform:uppercase;margin-top:26px;text-shadow:0 2px 16px rgba(0,0,0,.4)}
.tile .lim{position:absolute;left:14px;right:14px;bottom:16px;z-index:3;background:#FFFDF9;border-radius:999px;padding:14px 0;text-align:center;font:800 28px/1.15 'Manrope';color:#B4432F}
"""

def evento(cls, mes, dia, tit, sub, estilo=''):
    return (f'<div class="evento {cls}" style="{estilo}"><div class="cal"><p>{mes}</p><b>{dia}</b></div>'
            f'<div><p class="tit">{tit}</p><p class="sub">{sub}</p></div></div>')

T = []

# 1 · El gancho
T.append(('', f"""{LOGO}
<div style="position:relative;height:660px;margin-top:30px">
  {ft('photo-1780345021264-950c42e368f2', 'arco', 'position:absolute;right:0;top:0;width:620px;height:660px', '50% 50%')}
  <div style="position:absolute;left:0;bottom:40px;width:600px;display:flex;flex-direction:column;gap:16px">
    {evento('', 'mar', '15', 'Llega tu grupo', 'Bariloche · 4 noches')}
    {evento('rojo', 'ene', '29', 'Fecha límite', '12 lugares vendidos', 'margin-left:44px')}
  </div>
</div>
<h1 class="t" style="font-size:96px;margin-top:40px;text-wrap:wrap">Tu retiro de marzo<br><em>se vende antes de las fiestas.</em></h1>
<p class="sig" style="margin-top:auto;text-align:right;color:#9A3E25">Deslizá →</p>"""))

# 2 · Parece que sobra tiempo
T.append(('papel', f"""{LOGO}
<p class="ojo" style="margin-top:50px">Así empieza</p>
<h1 class="t" style="font-size:88px;margin-top:18px">Elegís el 15 de marzo. <em>Parece que sobra tiempo.</em></h1>
<div class="meses" style="margin-top:56px">
  <div class="mes"><p class="n">Dic</p><p class="c">1</p></div>
  <div class="mes lim"><p class="n">Ene</p><p class="c">29</p></div>
  <div class="mes"><p class="n">Feb</p><p class="c">·</p></div>
  <div class="mes fin"><p class="n">Mar</p><p class="c">15</p></div>
</div>
<div style="display:grid;grid-template-columns:1fr 1fr;gap:14px;margin-top:20px">
  <p style="font:800 30px/1.25 Manrope;color:#B4432F;padding-top:12px;border-top:3px solid #B4432F">29 de enero: tu fecha límite</p>
  <p style="font:800 30px/1.25 Manrope;color:#36603F;padding-top:12px;border-top:3px solid #36603F;text-align:right">15 de marzo: el retiro</p></div>
{ft('photo-1643494555111-df0141d84a62', 'estadio', 'height:300px;margin-top:40px', '50% 45%')}
<p class="t" style="font-size:56px;margin-top:auto;line-height:1.06;padding-bottom:8px">Tu retiro no se juega en marzo. <em>Se juega el 29 de enero.</em></p>"""))

# 3 · La cuenta regresiva
HITOS = [('ok', '15 mar', 'Llega tu grupo a Bariloche'),
         ('', '29 ene', 'Fecha límite: tus 12 lugares vendidos. Hasta 45 días antes, el lodge se cancela sin cargo'),
         ('corte', '21 dic', 'Las fiestas y las vacaciones, hasta el 6 de enero'),
         ('', '1 dic', 'Empezás a vender')]
LIN = ''.join(f'<div class="hito {c}"><span class="h" style="width:180px">{h}</span><span class="q">{q}</span></div>' for c, h, q in HITOS)
T.append(('lago', f"""{LOGO}
<p class="ojo" style="margin-top:50px">La cuenta regresiva</p>
<h1 class="t" style="font-size:84px;margin-top:18px;color:#FFFDF9">De marzo <em>para atrás.</em></h1>
<div class="linea" style="margin-top:40px">{LIN}</div>
<p class="t" style="font-size:56px;margin-top:auto;color:#FFFDF9;line-height:1.06;padding-bottom:8px">Sin las fiestas, <em>te quedan seis semanas de venta.</em></p>"""))

# 4 · El error: empezar en enero
def ritmo(fondo, color, titulo, semanas, por, txt, tinta='#1D2422'):
    cols = ''.join('<div>' + ''.join(f'<i style="background:{color}"></i>' for _ in range(por)) + '</div>' for _ in range(semanas))
    return (f'<div class="ritmo" style="background:{fondo};color:{tinta}"><div class="cab"><p>{titulo}</p>'
            f'<p class="cifra" style="color:{color}">{por} <span style="font-size:40px;font-family:Manrope;font-weight:800;letter-spacing:0">por semana</span></p></div>'
            f'<div class="sem" style="height:{30 + por * 46}px">{cols}</div><p class="pie2">{txt}</p></div>')
T.append(('', f"""{LOGO}
<p class="ojo" style="margin-top:50px">El error que más cuesta</p>
<h1 class="t" style="font-size:84px;margin-top:18px">Empezar a vender <em>en enero.</em></h1>
<div style="display:flex;flex-direction:column;gap:18px;margin-top:32px">
  {ritmo('#FFFDF9', '#36603F', 'Desde diciembre', 6, 2, 'Seis semanas para tus 12 lugares.')}
  {ritmo('#FFFDF9', '#B4432F', 'Desde enero', 3, 4, 'Tres semanas, con tu comunidad volviendo de vacaciones.')}
</div>"""))

# 5 · Cada fecha con su fecha límite
FOTOS = [('photo-1579541183120-dbb2ab2aa3c5', '50% 60%'), ('photo-1598162480222-b2c3d92548d5', '42% 55%'),
         ('photo-1692199037113-ff28ad03f703', '50% 55%')]
TILES = ''.join(f'<div class="tile">{ft(p, "arco", "", pos)}<div class="d"><p class="cifra">{x.day}</p><p class="mm">{MESES[x.month - 1]}</p></div>'
                f'<p class="lim">Vendé antes<br>del {f(l)}</p></div>' for (p, pos), x, l in zip(FOTOS, FECHAS, LIM))
T.append(('papel', f"""{LOGO}
<p class="ojo" style="margin-top:50px">Las fechas antes de abril</p>
<h1 class="t" style="font-size:84px;margin-top:18px">Cada fecha tiene <em>su fecha límite.</em></h1>
<div style="display:flex;gap:20px;margin-top:40px">{TILES}</div>
<p class="p" style="margin-top:auto;font-size:34px;color:#1D2422">Para el 22 de febrero, enero ya no alcanza. Y cuando una fecha se toma con seña, se tacha.</p>"""))

# 6 · Arrancar es una llamada
PASOS = [('photo-1647476685001-8510e5591ec3', '50% 50%', 'Hablás 30 minutos con Ailu:', 'tu grupo, tu fecha y tus números.'),
         ('photo-1784871258457-3a4b0c4de37f', '50% 50%', 'En 48 horas, tu propuesta:', 'lugar, programa y presupuesto cerrado.'),
         ('photo-1782226796423-8d72656a332c', '40% 50%', 'Reservás con la seña', 'y salís a vender con tu panel.')]
FIL = ''.join(f'<div class="paso">{ft(p, "circ", "width:196px;height:196px", pos)}<p class="n" style="color:#C9B27E">{k}</p>'
              f'<p style="font:600 36px/1.3 Manrope;color:#E9F0EE"><b style="font-weight:800;color:#FFFDF9">{a}</b> {b}</p></div>'
              for k, (p, pos, a, b) in enumerate(PASOS, 1))
T.append(('lago', f"""{LOGO}
<p class="ojo" style="margin-top:50px">Esta semana</p>
<h1 class="t" style="font-size:84px;margin-top:18px;color:#FFFDF9">Arrancar es <em>una llamada.</em></h1>
<div style="display:flex;flex-direction:column;gap:34px;margin-top:46px">{FIL}</div>
<p class="t" style="font-size:56px;margin-top:auto;color:#FFFDF9;line-height:1.06;padding-bottom:8px">Desde la seña, <em>la fecha es tuya.</em></p>"""))

# 7 · Del 13 al 20, tuyos
LUG = ''.join('<span class="punto"></span>' if i < C['eq'] else '<span class="punto tuyo">' + '</span>' for i in range(20))
T.append(('', f"""{LOGO}
{ft('photo-1758797316165-986ec92e7ad2', 'arco', 'height:560px;margin-top:30px', '45% 50%')}
<h1 class="t" style="font-size:80px;margin-top:40px">Llegás al 29 de enero con 12 lugares. <em>Del 13 al 20 son tuyos.</em></h1>
<div class="lugares" style="margin-top:auto">{LUG}</div>
<p class="p" style="margin-top:20px;font-size:32px;color:#1D2422">Con los 20 lugares, te quedan {m(C['que'])}.</p>"""))

# 8 · Comentá MARZO
T.append(('lago', f"""{LOGO}
<div style="position:relative;height:560px;margin-top:34px">
  {ft('photo-1598162480222-b2c3d92548d5', 'arco', 'position:absolute;right:0;top:0;width:540px;height:560px', '42% 55%')}
  <div style="position:absolute;left:0;top:150px;width:580px;display:flex;flex-direction:column;gap:18px">
    <div class="coment"><span class="av" style="background:#E9F0EE">{PERSONA}</span>
      <div><p class="quien">Vos</p><p class="dice" style="font-weight:800;font-size:38px;letter-spacing:.04em">MARZO</p></div></div>
    <div class="coment" style="margin-left:60px"><span class="av" style="background:#123A42;color:#C9B27E">{LOGO_SVG.replace('<svg', '<svg width="40" height="40"')}</span>
      <div><p class="quien">Experiencias Patagónicas</p><p class="dice">Te mandamos las fechas y la calculadora.</p></div></div>
  </div>
</div>
<h1 class="t" style="font-size:110px;margin-top:44px;color:#FFFDF9">Comentá <em>MARZO.</em></h1>
<p class="p" style="margin-top:24px;font-size:34px">Elegís tu fecha, ves tu fecha límite y hacés tu cuenta. Si te cierra, arrancás esta semana.</p>"""))


def armar():
    SALIDA.mkdir(parents=True, exist_ok=True)
    with sync_playwright() as p:
        b = p.chromium.launch()
        for i, (clase, cuerpo) in enumerate(T):
            nombre = f'carrusel-antes-de-las-fiestas-{i + 1}'
            pg = b.new_page(viewport={'width': W, 'height': H}, device_scale_factor=1)
            html = SALIDA / f'_{nombre}.html'
            html.write_text(f'<!doctype html><html><head><meta charset="utf-8"><style>{CSS}</style></head>'
                            f'<body class="{clase}" style="--w:{W}px;--h:{H}px">{cordillera(i)}<div class="cap">{cuerpo}</div></body></html>',
                            encoding='utf-8')
            pg.goto(html.as_uri())
            pg.evaluate('document.fonts.ready')
            pg.wait_for_timeout(400)
            info = pg.evaluate("""()=>{const o=[];const cap=document.querySelector('.cap');const lim=innerHeight-150+4;
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
