"""Carrusel 2 «La cuenta», versión con fotos y la piel de la marca (logo, fotos con la misma luz,
subtítulo de la película, botón de la página). Salida: /home/claude/entregas/marzo/carruseles/

    python3 anuncios/cuenta_v2.py
"""
import pathlib
from playwright.sync_api import sync_playwright
from build_anuncios import CSS as BASE, foto, tilde

SALIDA = pathlib.Path('/home/claude/entregas/marzo/carruseles')

CSS = BASE + """
.ft{position:relative;overflow:hidden;border-radius:30px;background:#1B4B54;flex:none}
.ft i{position:absolute;inset:0;background-size:cover;background-position:var(--pos,center);filter:saturate(.86) contrast(1.03)}
.ft::after{content:"";position:absolute;inset:0;background:#123A42;mix-blend-mode:soft-light;opacity:.32}
.ft.calida::after{background:#B9714C;opacity:.24}
.ft.full{position:absolute;inset:0;border-radius:0}
.ft.full::before{content:"";position:absolute;inset:0;z-index:1;background:linear-gradient(180deg,rgba(10,30,34,.5) 0%,rgba(10,30,34,0) 24%,rgba(10,30,34,0) 50%,rgba(10,30,34,.35) 100%)}
.barra{position:absolute;top:40px;left:48px;right:48px;z-index:6;display:flex;align-items:center;justify-content:space-between}
.marca{display:flex;align-items:center;gap:14px;color:#1D2422}
.marca svg{width:54px;height:54px;color:#9A3E25;flex:none}
.marca span{font-family:'Fraunces',serif;font-variation-settings:"SOFT" 100,"opsz" 72;font-weight:440;font-size:32px;letter-spacing:-.015em}
.osc .marca{color:#FFFDF9}.osc .marca svg{color:#C9B27E}
.num{font:700 26px/1 'Manrope';letter-spacing:.08em;color:#4F5B57}
.osc .num{color:#FFFDF9;background:rgba(18,58,66,.62);padding:11px 15px;border-radius:999px}
.sub{position:absolute;left:44px;right:44px;bottom:44px;z-index:4;background:rgba(18,58,66,.93);border-radius:30px;padding:44px 50px 46px;color:#E9F0EE}
.sub .t{color:#FFFDF9}
.sub .t em{color:#C9B27E}
.cuando{font:800 27px/1.2 'Manrope';letter-spacing:.12em;text-transform:uppercase;color:#C9B27E}
.pastilla{display:inline-flex;align-items:center;background:#FFFDF9;color:#1D2422;border-radius:999px;padding:15px 26px;font:800 30px/1 'Manrope';box-shadow:0 14px 30px -18px rgba(0,0,0,.6)}
.boton{display:inline-flex;align-items:center;gap:14px;background:#9A3E25;color:#FFFDF9;border-radius:999px;padding:0 38px;height:84px;font:700 32px/1 'Manrope';box-shadow:0 14px 30px -18px rgba(154,62,37,.75)}
.lista p{display:flex;align-items:flex-start;gap:20px;font:600 38px/1.22 'Manrope';padding:31px 0;border-bottom:1px solid rgba(29,36,34,.14)}
.lista p:first-child{padding-top:6px}
.lista .tilde{margin-top:-2px}
.lugares{display:grid;grid-template-columns:repeat(14,1fr);gap:11px}
.lugares .punto{border-width:0}
.tramo{display:grid;grid-template-columns:9fr 5fr;gap:22px;margin-top:20px}
.tramo p{font:800 28px/1.25 'Manrope';padding-top:14px;border-top:3px solid #123A42}
.tramo p+p{border-color:#36603F;color:#36603F}
"""

LOGO = ('<div class="marca"><svg viewBox="0 0 64 64" aria-hidden="true"><path d="M4 52 22 22l10 14 8-10 20 26z" fill="none" '
        'stroke="currentColor" stroke-width="3.4" stroke-linejoin="round"/><path d="M32 36 38 28" fill="none" stroke="currentColor" '
        'stroke-width="3.4" stroke-linecap="round"/></svg><span>Experiencias Patagónicas</span></div>')

def barra(n):
    return f'<div class="barra">{LOGO}<p class="num">{n:02d} / 06</p></div>'

def ft(pid, pos='center', clase='', estilo=''):
    return f'<div class="ft {clase}" style="{estilo}"><i style="background-image:url(\'{foto(pid)}\');--pos:{pos}"></i></div>'

Q = {}

# 1 · Portada: la cena del grupo, la pregunta en el subtítulo de la película
Q['carrusel-2-cuenta-1'] = ('osc', f"""{ft('photo-1778694277039-5cbf0b9a1fcf', '62% 50%', 'full calida')}{barra(1)}
<div class="sub">
  <p class="cuando">Tu retiro en Bariloche</p>
  <h1 class="t" style="font-size:84px;margin-top:20px">¿Cuánto te queda de un retiro de cuatro días <em>en la Patagonia?</em></h1>
  <div style="display:flex;justify-content:space-between;align-items:center;margin-top:30px;padding-top:24px;border-top:1px solid rgba(201,178,126,.55)">
    <p class="p" style="font-size:32px;color:#DCE8E6">Hicimos la cuenta.</p><p class="sig">Deslizá →</p></div>
</div>""")

# 2 · Lo que vendés: el lodge frente al lago, con los datos del ejemplo
Q['carrusel-2-cuenta-2'] = ('papel', f"""{barra(2)}
<div class="col" style="padding:124px 48px 0">
  <div style="position:relative">
    {ft('photo-1571787207812-77254da636a6', '50% 46%', '', 'height:560px')}
    <div style="position:absolute;left:28px;right:28px;bottom:28px;z-index:3;display:flex;flex-wrap:wrap;gap:12px">
      <span class="pastilla">14 personas</span><span class="pastilla">4 noches</span><span class="pastilla">US$ 2.900 cada una</span></div>
  </div>
  <div class="panel" style="--pad:34px 16px 52px">
    <p class="p" style="font-size:33px">Lodge boutique frente al lago y cocina de autor.</p>
    <div style="margin-top:auto;border-top:1px solid #C9B27E;padding-top:24px;display:flex;align-items:flex-end;justify-content:space-between;gap:20px">
      <p class="p" style="font-size:34px;color:#1D2422;font-weight:800;padding-bottom:14px">Lo que<br>vendés</p>
      <p class="cifra" style="font-size:176px;color:#123A42">US$ 40.600</p></div>
  </div>
</div>""")

# 3 · Lo que cuesta producirlo todo: la mesa puesta al costado
COSTOS = ['Alojamiento, cocina, traslados y salidas', 'Sala, fotos y detalles', 'Imprevistos, 8 %', 'Nuestro honorario']
LISTA = ''.join(f'<p>{tilde(50)}<span>{c}</span></p>' for c in COSTOS)
Q['carrusel-2-cuenta-3'] = ('papel', f"""{barra(3)}
<div class="col" style="padding:124px 48px 0">
  <div style="display:flex;gap:44px;height:612px">
    {ft('photo-1562050344-f7ad946cee35', '30% 50%', 'calida', 'width:356px;height:100%')}
    <div style="flex:1;display:flex;flex-direction:column;padding-right:16px">
      <p class="ojo" style="font-size:26px">Todo producido</p>
      <div class="lista" style="margin-top:22px">{LISTA}</div>
    </div>
  </div>
  <div class="panel" style="--pad:0 16px 50px;justify-content:flex-end">
    <div style="border-top:1px solid #C9B27E;padding-top:20px;display:flex;align-items:flex-end;justify-content:space-between;gap:20px">
      <p class="p" style="font-size:34px;color:#1D2422;font-weight:800;padding-bottom:12px">Lo que<br>cuesta todo</p>
      <p class="cifra" style="font-size:150px;color:#9A3E25">−US$ 25.256</p></div>
  </div>
</div>""")

# 4 · Lo que te queda: el festejo frente al lago
Q['carrusel-2-cuenta-4'] = ('osc', f"""{ft('photo-1551845728-6820a30c64e2', '50% 50%', 'full')}{barra(4)}
<div class="sub" style="padding:40px 50px 44px">
  <p class="cuando">Te queda a vos</p>
  <p class="cifra" style="font-size:196px;color:#C9B27E;margin-top:22px">US$ 15.344</p>
  <p class="t" style="font-size:56px;margin-top:22px">El 38 % de lo que vendés, <em>con todo pagado.</em></p>
</div>""")

# 5 · El punto de equilibrio: el grupo frente al agua, y los 14 lugares
LUG = ''.join('<span class="punto cubre"></span>' if i < 9 else '<span class="punto tuyo">' + tilde(10) + '</span>' for i in range(14))
Q['carrusel-2-cuenta-5'] = ('papel', f"""{barra(5)}
<div class="col" style="padding:124px 48px 0">
  {ft('photo-1599341301512-ca6d7a851fba', '50% 62%', '', 'height:500px')}
  <div class="panel" style="--pad:34px 16px 50px">
    <h1 class="t" style="font-size:76px">Con 9 lugares vendidos, <em>ya cubriste todo.</em></h1>
    <div style="margin-top:auto">
      <div class="lugares">{LUG}</div>
      <div class="tramo"><p>Del 1 al 9: cubren el retiro</p><p>Del 10 al 14: tuyos</p></div>
    </div>
  </div>
</div>""")

# 6 · Cierre: la cabaña encendida, el botón de la página
Q['carrusel-2-cuenta-6'] = ('osc', f"""{ft('photo-1782226796423-8d72656a332c', '40% 50%', 'full calida')}{barra(6)}
<div class="sub">
  <h1 class="t" style="font-size:88px">Hacé la cuenta <em>con tus números.</em></h1>
  <p class="p" style="font-size:33px;margin-top:22px;color:#DCE8E6">Está la calculadora en la página. Si te cierra, elegí tu horario de 30 minutos y armamos el tuyo.</p>
  <div style="display:flex;align-items:center;justify-content:space-between;gap:24px;margin-top:32px">
    <span class="boton">Hacé tu cuenta →</span>
    <p class="fechas" style="text-align:right;color:#FFFDF9">22 feb · 8 mar · 15 mar<span style="color:#B7CBC8">Antes de abril</span></p></div>
</div>""")


def armar():
    SALIDA.mkdir(parents=True, exist_ok=True)
    with sync_playwright() as p:
        b = p.chromium.launch()
        for nombre, (clase, cuerpo) in Q.items():
            pg = b.new_page(viewport={'width': 1080, 'height': 1080}, device_scale_factor=1)
            html = SALIDA / f'_{nombre}.html'
            html.write_text(f'<!doctype html><html><head><meta charset="utf-8"><style>{CSS}</style></head>'
                            f'<body class="{clase}" style="--w:1080px;--h:1080px">{cuerpo}</body></html>', encoding='utf-8')
            pg.goto(html.as_uri())
            pg.evaluate('document.fonts.ready')
            pg.wait_for_timeout(400)
            info = pg.evaluate("""()=>{const o=[];document.querySelectorAll('body *').forEach(e=>{const r=e.getBoundingClientRect();
              if(r.width&&(r.right>innerWidth+1||r.bottom>innerHeight+1))o.push('sale '+e.tagName+'.'+e.className+' '+Math.round(r.right)+'x'+Math.round(r.bottom));
              const t=[...e.childNodes].some(n=>n.nodeType==3&&n.textContent.trim());
              if(t&&parseFloat(getComputedStyle(e).fontSize)<26)o.push('chica '+e.className);
              if(t&&e.scrollWidth>e.clientWidth+1&&getComputedStyle(e).whiteSpace=='nowrap')o.push('corta '+e.className)});return o}""")
            pg.screenshot(path=str(SALIDA / f'{nombre}.png'))
            html.unlink()
            print(nombre, info or 'ok')
            pg.close()
        b.close()

if __name__ == '__main__':
    armar()
