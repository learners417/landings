"""Carrusel «La calculadora» de Experiencias Patagónicas (4:5, 8 tarjetas).

Historia: el sueño de 20 lugares a US$ 3.000 → la cuenta de verdad → tres errores →
la calculadora express → las fechas → «Comentá CALCULADORA».
Los números salen de la misma fórmula de la calculadora de /retiros-2027 (costos de referencia
de Experiencias Patagónicas para Bariloche 2027: Premium US$ 330 por persona y por noche).
Una línea de cordillera corre de la primera tarjeta a la última.

    python3 anuncios/carrusel_calculadora.py
"""
import math, pathlib, random
from playwright.sync_api import sync_playwright
from build_anuncios import CSS as BASE, foto, tilde

SALIDA = pathlib.Path('/home/claude/entregas/marzo/carrusel-calculadora')
W, H, N = 1080, 1350, 8

# ── la cuenta, con la fórmula de la página ──
def cuenta(per, pre, noches=4, nivel=330):
    pro = per * noches * nivel
    fij = 1600 + 200 * noches
    imp = .08 * (pro + fij)
    pres = pro + fij + imp
    hon = max(1800, .12 * pres)
    costo = pres + hon
    return dict(ven=per * pre, pro=pro, fij=fij, imp=imp, hon=hon, costo=costo, que=per * pre - costo,
                pct=round((per * pre - costo) / (per * pre) * 100), eq=math.ceil(costo / pre))

C = cuenta(20, 3000)
def m(n):
    return 'US$ ' + f'{round(n):,}'.replace(',', '.')
assert (m(C['ven']), m(C['pro']), m(C['fij']), m(C['imp']), m(C['hon']), m(C['que']), C['pct'], C['eq']) == \
       ('US$ 60.000', 'US$ 26.400', 'US$ 2.400', 'US$ 2.304', 'US$ 3.732', 'US$ 25.164', 42, 12), C
assert round(C['pro']) + round(C['fij']) + round(C['imp']) + round(C['hon']) + round(C['que']) == 60000

# ── la cordillera que cruza las 8 tarjetas ──
random.seed(7)
pts, x = [], 0
while x <= W * N + 60:
    pts.append((x, random.choice([1262, 1274, 1286, 1250, 1294, 1240, 1280])))
    x += random.choice([70, 90, 110, 130])
for k in (len(pts) // 5, len(pts) // 2, 4 * len(pts) // 5):   # tres cumbres
    pts[k] = (pts[k][0], 1214)
RUTA = 'M' + ' L'.join(f'{a},{b}' for a, b in pts)

def cordillera(i, color='#C9B27E'):
    return (f'<svg class="cord" viewBox="{i * W} 0 {W} {H}" preserveAspectRatio="none">'
            f'<path d="{RUTA}" fill="none" stroke="{color}" stroke-width="2.4" stroke-linejoin="round"/></svg>')

CSS = BASE + """
.cord{position:absolute;inset:0;width:100%;height:100%;z-index:1;pointer-events:none}
.cap{position:absolute;inset:0;z-index:2;display:flex;flex-direction:column;padding:56px 76px 150px}
.marca{display:flex;align-items:center;gap:12px;color:#1D2422}
.marca svg{width:46px;height:46px;color:#9A3E25;flex:none}
.marca span{font-family:'Fraunces',serif;font-variation-settings:"SOFT" 100,"opsz" 72;font-weight:440;font-size:28px;letter-spacing:-.015em}
.lago .marca{color:#E9F0EE}.lago .marca svg{color:#C9B27E}
.ft{position:relative;overflow:hidden;background:#1B4B54;flex:none}
.ft i{position:absolute;inset:0;background-size:cover;background-position:var(--pos,center);filter:saturate(.86) contrast(1.03)}
.ft::after{content:"";position:absolute;inset:0;background:#123A42;mix-blend-mode:soft-light;opacity:.3}
.ft.calida::after{background:#B9714C;opacity:.22}
.arco{border-radius:999px 999px 34px 34px}
.circ{border-radius:50%}
.estadio{border-radius:999px}
.t em{font-style:italic}
.ojo{font-size:27px}
.nota{background:#FFFDF9;border-radius:30px;padding:30px 36px 32px;box-shadow:0 40px 70px -36px rgba(18,58,66,.55)}
.nota .l{font:700 30px/1.3 'Manrope';color:#4F5B57;font-variant-numeric:tabular-nums}
.ticket{background:#FFFDF9;color:#1D2422;border-radius:26px 26px 0 0;padding:30px 40px 50px;
  -webkit-mask:radial-gradient(14px at 50% 100%,#0000 98%,#000) 0 0/32px 100% repeat-x}
.ticket .r{display:flex;justify-content:space-between;align-items:baseline;gap:24px;font:600 34px/1.25 'Manrope';padding:23px 0;font-variant-numeric:tabular-nums}
.ticket .r b{font-weight:800;white-space:nowrap}
.ticket .r small{display:block;font:600 28px/1.3 'Manrope';color:#4F5B57}
.ticket .rojo b{color:#B4432F}
.ticket .tot{border-top:2px dashed rgba(29,36,34,.25);margin-top:8px;padding-top:20px;align-items:flex-end}
.paso{display:flex;align-items:center;gap:34px}
.paso .n{font-family:'Fraunces',serif;font-style:italic;font-weight:350;font-size:44px;color:#9A3E25;margin-right:-14px}
.lugares{display:grid;grid-template-columns:repeat(10,1fr);gap:14px}
.lugares .punto{aspect-ratio:1;border-radius:50%;background:#123A42;border:0}
.lugares .punto.tuyo{background:#36603F;display:grid;place-items:center}
.lugares .punto.tuyo .tilde{width:100%;height:100%;background:none}
.prov{display:flex;flex-wrap:wrap;gap:16px 12px}
.prov span{position:relative;border:1.5px solid rgba(29,36,34,.22);border-radius:999px;padding:15px 24px;font:600 33px/1 'Manrope';color:#4F5B57}
.prov span::after{content:"";position:absolute;left:14px;right:14px;top:50%;height:3px;background:#B4432F;border-radius:2px}
.cel{width:520px;height:850px;border-radius:70px;background:#0B2328;padding:16px;box-shadow:0 50px 90px -40px rgba(0,0,0,.7)}
.pant{width:100%;height:100%;border-radius:56px;background:#FBF8F2;color:#1D2422;padding:50px 34px 28px;display:flex;flex-direction:column;gap:20px;overflow:hidden}
.pant .lab{display:flex;justify-content:space-between;font:700 28px/1.2 'Manrope'}
.pant .lab b{font-weight:800;color:#123A42}
.riel{position:relative;height:10px;border-radius:10px;background:#E4DED2;margin-top:18px}
.riel i{position:absolute;left:0;top:0;bottom:0;border-radius:10px;background:#9A3E25}
.riel s{position:absolute;top:50%;width:34px;height:34px;border-radius:50%;background:#FFFDF9;border:3px solid #9A3E25;transform:translate(-50%,-50%)}
.chips{display:flex;gap:10px;margin-top:14px}
.chips span{flex:1;text-align:center;border:1.5px solid rgba(29,36,34,.22);border-radius:999px;padding:12px 0;font:700 27px/1 'Manrope'}
.chips .si{background:#123A42;border-color:#123A42;color:#FFFDF9}
.res{margin-top:auto;background:#123A42;color:#E9F0EE;border-radius:34px;padding:26px 28px 28px}
.res .et{font:800 26px/1.2 'Manrope';letter-spacing:.1em;text-transform:uppercase;color:#C9B27E}
.res .cifra{font-size:86px;color:#FFFDF9;margin-top:14px}
.res small{display:block;font:600 27px/1.3 'Manrope';color:#B7CBC8;margin-top:12px}
.guia{display:flex;flex-direction:column}
.guia p{display:flex;gap:18px;align-items:baseline;font:600 32px/1.25 'Manrope';color:#E9F0EE}
.guia p b{font-family:'Fraunces',serif;font-style:italic;font-weight:350;font-size:50px;color:#C9B27E;line-height:.8;flex:none;width:34px}
.fecha{position:relative;flex:1;height:560px}
.fecha .ft{position:absolute;inset:0}
.fecha .d{position:absolute;left:0;right:0;bottom:26px;z-index:3;text-align:center;color:#FFFDF9}
.fecha .d .cifra{font-size:150px;text-shadow:0 6px 30px rgba(0,0,0,.35)}
.fecha .d .mes{font:800 30px/1 'Manrope';letter-spacing:.16em;text-transform:uppercase;margin-top:8px}
.coment{background:#FFFDF9;color:#1D2422;border-radius:32px;padding:26px 30px;display:flex;gap:20px;align-items:flex-start;box-shadow:0 40px 70px -36px rgba(0,0,0,.6)}
.coment .av{flex:none;width:72px;height:72px;border-radius:50%;display:grid;place-items:center}
.coment .quien{font:800 27px/1.2 'Manrope'}
.coment .dice{font:600 32px/1.3 'Manrope';margin-top:6px}
.sig{font-size:31px}
"""

LOGO_SVG = ('<svg viewBox="0 0 64 64" aria-hidden="true"><path d="M4 52 22 22l10 14 8-10 20 26z" fill="none" '
            'stroke="currentColor" stroke-width="3.4" stroke-linejoin="round"/><path d="M32 36 38 28" fill="none" '
            'stroke="currentColor" stroke-width="3.4" stroke-linecap="round"/></svg>')
LOGO = f'<div class="marca">{LOGO_SVG}<span>Experiencias Patagónicas</span></div>'
PERSONA = ('<svg viewBox="0 0 24 24" width="40" height="40" fill="none" stroke="#4F5B57" stroke-width="1.8" stroke-linecap="round">'
           '<circle cx="12" cy="8.5" r="4"/><path d="M4.5 20c1.4-3.6 4.2-5.4 7.5-5.4s6.1 1.8 7.5 5.4"/></svg>')

def ft(pid, clase='', estilo='', pos='center'):
    return f'<div class="ft {clase}" style="{estilo}"><i style="background-image:url(\'{foto(pid)}\');--pos:{pos}"></i></div>'

T = []   # (clase del body, html)

# 1 · El sueño
T.append(('', f"""{LOGO}
<div style="position:relative;height:680px;margin-top:30px">
  {ft('photo-1778694277039-5cbf0b9a1fcf', 'arco calida', 'position:absolute;right:0;top:0;width:640px;height:680px', '60% 50%')}
  <div class="nota" style="position:absolute;left:0;bottom:36px;width:560px">
    <p class="l">20 lugares</p><p class="l">× US$ 3.000</p>
    <p class="cifra" style="font-size:112px;color:#123A42;margin-top:16px;padding-top:18px;border-top:2px dashed rgba(29,36,34,.22)">US$ 60.000</p>
  </div>
</div>
<h1 class="t" style="font-size:96px;margin-top:40px;text-wrap:wrap">Esa es la cuenta que hacés.<br><em>Lo que te queda es otra.</em></h1>
<p class="sig" style="margin-top:auto;text-align:right;color:#9A3E25">Deslizá →</p>"""))

# 2 · Cómo empieza
PASOS = [('photo-1647476685001-8510e5591ec3', '50% 50%', 'Elegís Bariloche y cuatro noches.'),
         ('photo-1758797316165-986ec92e7ad2', '40% 50%', 'Ponés US$ 3.000 y multiplicás por 20.'),
         ('photo-1686670576866-8c9ec4a7fc87', '50% 60%', 'Reservás el lodge y salís a vender.')]
FILAS = ''.join(f'<div class="paso">{ft(p, "circ", "width:190px;height:190px", pos)}<p class="n">{k}</p>'
                f'<p class="t" style="font-size:52px;line-height:1.08">{txt}</p></div>' for k, (p, pos, txt) in enumerate(PASOS, 1))
T.append(('papel', f"""{LOGO}
<p class="ojo" style="margin-top:56px">Así empieza</p>
<h1 class="t" style="font-size:90px;margin-top:20px">Tu comunidad te pide <em>verse en persona.</em></h1>
<div style="display:flex;flex-direction:column;gap:30px;margin-top:46px">{FILAS}</div>
<p class="t" style="font-size:54px;margin-top:auto;color:#9A3E25;font-style:italic;font-weight:350">Y el número real lo ves cuando ya volviste a casa.</p>"""))

# 3 · Error 1: la cuenta de verdad
T.append(('lago', f"""{LOGO}
<p class="ojo" style="margin-top:50px">Error 1</p>
<h1 class="t" style="font-size:84px;margin-top:20px;color:#FFFDF9">Contar lo que vendés <em>como lo que ganás.</em></h1>
<div class="ticket" style="margin-top:40px">
  <div class="r"><span>Lo que vendés<small>20 lugares a US$ 3.000</small></span><b>{m(C['ven'])}</b></div>
  <div class="r rojo"><span>Alojamiento, cocina, traslados y salidas</span><b>−{m(C['pro'])}</b></div>
  <div class="r rojo"><span>Sala, fotos y detalles</span><b>−{m(C['fij'])}</b></div>
  <div class="r rojo"><span>Imprevistos, 8 %</span><b>−{m(C['imp'])}</b></div>
  <div class="r rojo"><span>Producción llave en mano, 12 %</span><b>−{m(C['hon'])}</b></div>
  <div class="r tot"><span style="font-weight:800">Te queda a vos<small>el {C['pct']} % de lo que vendés</small></span>
    <b class="cifra" style="font-size:108px;color:#36603F;font-weight:330">{m(C['que'])}</b></div>
</div>"""))

# 4 · Error 2: el número de equilibrio
LUG = ''.join('<span class="punto"></span>' if i < C['eq'] else '<span class="punto tuyo">' + tilde(10) + '</span>' for i in range(20))
T.append(('', f"""{LOGO}
<p class="ojo" style="margin-top:50px">Error 2</p>
<h1 class="t" style="font-size:80px;margin-top:18px">Reservar el lodge <em>sin saber tu número.</em></h1>
<div style="display:flex;align-items:flex-end;gap:30px;margin-top:40px">
  <p class="cifra" style="font-size:360px;color:#123A42;line-height:.78">{C['eq']}</p>
  <p class="t" style="font-size:54px;line-height:1.05;padding-bottom:6px">lugares pagan <em>todo el retiro.</em></p>
</div>
<div class="lugares" style="margin-top:56px">{LUG}</div>
<div style="display:grid;grid-template-columns:12fr 8fr;gap:14px;margin-top:18px">
  <p style="font:800 28px/1.25 Manrope;padding-top:12px;border-top:3px solid #123A42">Del 1 al 12: cubren todo</p>
  <p style="font:800 28px/1.25 Manrope;padding-top:12px;border-top:3px solid #36603F;color:#36603F">Del 13 al 20: tuyos</p></div>
<p class="p" style="margin-top:auto;font-size:35px">Con ese número fijás tu fecha límite de inscripción, y el lodge se reserva con cancelación sin cargo hasta 45 días antes.</p>"""))

# 5 · Error 3: armarlo por tu cuenta
PROV = ['El lodge', 'La cocina', 'Los traslados', 'El velero', 'El guía', 'La sala', 'El fotógrafo', 'El plan B',
        'Los seguros', 'Los pagos', 'Los horarios', 'El imprevisto de las 23 h']
T.append(('papel', f"""{LOGO}
<p class="ojo" style="margin-top:50px">Error 3</p>
<h1 class="t" style="font-size:88px;margin-top:18px">Armarlo <em>por tu cuenta.</em></h1>
{ft('photo-1562050344-f7ad946cee35', 'estadio calida', 'height:250px;margin-top:34px', '50% 55%')}
<p class="p" style="margin-top:34px;font-size:32px;color:#1D2422;font-weight:700">Doce proveedores y cuarenta horas de llamadas:</p>
<div class="prov" style="margin-top:20px">{''.join(f'<span>{p}</span>' for p in PROV)}</div>
<div style="display:flex;align-items:center;gap:22px;margin-top:auto">{tilde(70)}
  <p class="t" style="font-size:50px;line-height:1.05">Con nosotras, <em>una sola persona: Ailu.</em></p></div>"""))

# 6 · La calculadora express
CEL = f"""<div class="cel"><div class="pant">
  <p style="font:800 26px/1 Manrope;letter-spacing:.12em;text-transform:uppercase;color:#9A3E25">Calculadora express</p>
  <div><p class="lab">Personas <b>20</b></p><div class="riel"><i style="width:58%"></i><s style="left:58%"></s></div></div>
  <div><p class="lab">Precio por persona <b>US$ 3.000</b></p><div class="riel"><i style="width:40%"></i><s style="left:40%"></s></div></div>
  <div><p class="lab">Noches</p><div class="chips"><span>3</span><span class="si">4</span><span>5</span></div></div>
  <div><p class="lab">Nivel</p><div class="chips"><span class="si">Premium</span><span>Lujo</span></div></div>
  <div class="res"><p class="et">Te queda a vos</p><p class="cifra">{m(C['que'])}</p><small>El {C['pct']} %. Con {C['eq']} lugares cubriste todo.</small></div>
</div></div>"""
T.append(('lago', f"""{LOGO}
<p class="ojo" style="margin-top:50px">La calculadora express</p>
<h1 class="t" style="font-size:78px;margin-top:18px;color:#FFFDF9">Cuatro datos <em>y ves lo que te queda.</em></h1>
<div style="display:flex;gap:36px;margin-top:40px;align-items:flex-start">
  <div class="guia" style="flex:1;padding-top:140px;gap:62px">
    <p><b>1</b>Cuántas personas</p><p><b>2</b>A cuánto</p><p><b>3</b>Cuántas noches</p><p><b>4</b>Qué nivel</p>
    <p style="margin-top:60px"><b style="font-style:normal">=</b>Lo que te queda, antes de vender el primer lugar</p>
  </div>
  {CEL}
</div>"""))

# 7 · Las fechas
FECHAS = [('photo-1579541183120-dbb2ab2aa3c5', '50% 60%', '22', 'feb'),
          ('photo-1598162480222-b2c3d92548d5', '42% 50%', '8', 'mar'),
          ('photo-1780345021264-950c42e368f2', '50% 50%', '15', 'mar')]
TILES = ''.join(f'<div class="fecha">{ft(p, "arco", "", pos)}<div class="d"><p class="cifra">{d}</p><p class="mes">{mes}</p></div></div>'
                for p, pos, d, mes in FECHAS)
T.append(('', f"""{LOGO}
<p class="ojo" style="margin-top:50px">Antes de abril</p>
<h1 class="t" style="font-size:92px;margin-top:18px">Quedan <em>tres fechas.</em></h1>
<div style="display:flex;gap:22px;margin-top:40px">{TILES}</div>
<p class="p" style="margin-top:36px;font-size:33px">Cuando una se toma con seña, se tacha. Ailu produce todo en Bariloche y está en el retiro, de la llegada a la despedida.</p>"""))

# 8 · Comentá CALCULADORA
T.append(('lago', f"""{LOGO}
<div style="position:relative;height:560px;margin-top:34px">
  {ft('photo-1782226796423-8d72656a332c', 'arco calida', 'position:absolute;right:0;top:0;width:560px;height:560px', '40% 50%')}
  <div style="position:absolute;left:0;top:150px;width:560px;display:flex;flex-direction:column;gap:18px">
    <div class="coment"><span class="av" style="background:#E9F0EE">{PERSONA}</span>
      <div><p class="quien">Vos</p><p class="dice" style="font-weight:800;font-size:38px;letter-spacing:.04em">CALCULADORA</p></div></div>
    <div class="coment" style="margin-left:60px"><span class="av" style="background:#123A42;color:#C9B27E">{LOGO_SVG.replace('<svg', '<svg width="40" height="40"')}</span>
      <div><p class="quien">Experiencias Patagónicas</p><p class="dice">Te la mandamos por mensaje.</p></div></div>
  </div>
</div>
<h1 class="t" style="font-size:104px;margin-top:44px;color:#FFFDF9">Comentá <em>CALCULADORA.</em></h1>
<p class="p" style="margin-top:24px;font-size:34px">Te mandamos la calculadora express. Hacés tu cuenta con tus números y, si te cierra, armamos tu retiro en una llamada de 30 minutos.</p>"""))


def armar():
    SALIDA.mkdir(parents=True, exist_ok=True)
    with sync_playwright() as p:
        b = p.chromium.launch()
        for i, (clase, cuerpo) in enumerate(T):
            nombre = f'carrusel-calculadora-{i + 1}'
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
