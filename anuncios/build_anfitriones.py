"""Anuncios de Anfitriones del Sur (piel «Lago»): 3 imágenes (feed 4:5 e historia 9:16)
y 3 carruseles de 6 tarjetas (1:1). Usa cuadros reales de Ailu: la salida queda fuera del repo
hasta que ella la apruebe.

    python3 build_anfitriones.py
"""
import pathlib, shutil
from playwright.sync_api import sync_playwright

RAIZ = pathlib.Path(__file__).resolve().parent
FOTOS = pathlib.Path('/home/claude/anfitriones/fotos')   # Unsplash + cuadros de Ailu (descifrados de la rama ailu-fotos)
SALIDA = pathlib.Path('/home/claude/anfitriones/salida')  # fuera del repo hasta que Ailu apruebe
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
.capa{position:absolute;inset:0;background-size:cover;background-position:var(--pos,center)}
.velo{position:absolute;inset:0;background:rgba(9,30,35,var(--v,.58))}
.sobre{position:absolute;inset:0;display:flex;flex-direction:column;padding:var(--pad,64px);color:#FFFDF9}
.foto{flex:none;width:100%;background-size:cover;background-position:var(--pos,center)}
.panel{flex:1;display:flex;flex-direction:column;padding:var(--pad,56px 64px)}
.banda{background:#123A42;color:#E9F0EE}
.ojo{display:flex;align-items:center;gap:16px;font:800 27px/1.1 'Manrope';letter-spacing:.13em;text-transform:uppercase;color:#9A3E25}
.ojo::before{content:"";flex:none;width:46px;height:1px;background:#C9B27E}
.lago .ojo,.banda .ojo,.sobre .ojo{color:#C9B27E}
.t{font-family:'Fraunces',serif;font-variation-settings:"SOFT" 100,"opsz" 144;font-weight:400;letter-spacing:-.028em;line-height:1.0;text-wrap:balance}
.t em{font-style:italic;font-weight:350;color:#9A3E25}
.lago .t em,.banda .t em,.sobre .t em{color:#C9B27E}
.p{font:600 34px/1.38 'Manrope';color:#4F5B57;text-wrap:pretty}
.lago .p,.banda .p{color:#B7CBC8}
.sobre .p{color:#E9F0EE}
.pie{margin-top:auto;display:flex;align-items:flex-end;justify-content:space-between;gap:24px;border-top:1px solid #C9B27E;padding-top:24px}
.fechas{font:700 31px/1.25 'Manrope'}
.fechas span{display:block;font:600 27px/1.3 'Manrope';color:#4F5B57}
.lago .fechas span,.banda .fechas span{color:#B7CBC8}
.sobre .fechas span{color:#DCE8E6}
.firma{font-family:'Fraunces',serif;font-variation-settings:"SOFT" 100,"opsz" 144;font-size:32px;line-height:1.05;text-align:right;color:#123A42}
.lago .firma,.banda .firma,.sobre .firma{color:#FFFDF9}
.folio{position:absolute;top:44px;right:52px;z-index:5;font:700 26px/1 'Manrope';letter-spacing:.08em;color:#FFFDF9;background:rgba(18,58,66,.62);padding:10px 14px;border-radius:999px}
.folio.claro{background:none;color:#4F5B57;padding:0;top:56px;right:64px}
.lago .folio.claro{color:#B7CBC8}
.sig{font:700 30px/1 'Manrope';color:#C9B27E;letter-spacing:.02em}
.cifra{font-family:'Fraunces',serif;font-variation-settings:"SOFT" 100,"opsz" 144;font-weight:330;letter-spacing:-.045em;line-height:.9;font-variant-numeric:lining-nums tabular-nums;white-space:nowrap}
.chip{border:1px solid #C9B27E;border-radius:999px;padding:16px 26px;font:700 32px/1 'Manrope'}
.lago .chip{color:#E9F0EE}
/* ticket */
.ticket{background:#FFFDF9;border-radius:22px 22px 0 0;padding:34px 40px 46px;box-shadow:0 30px 60px -40px rgba(18,58,66,.6);
  -webkit-mask:radial-gradient(14px at 50% 100%,#0000 98%,#000) 0 0/32px 100% repeat-x;}
.ticket .cab{font:800 27px/1.1 'Manrope';letter-spacing:.13em;text-transform:uppercase;color:#4F5B57;padding-bottom:20px;border-bottom:2px dashed rgba(29,36,34,.22)}
.ticket .r{display:flex;justify-content:space-between;align-items:baseline;gap:24px;font:600 34px/1.3 'Manrope';padding:18px 0;font-variant-numeric:tabular-nums}
.ticket .r b{font-weight:800}
.ticket .rojo{color:#B4432F}
.ticket .tot{border-top:2px dashed rgba(29,36,34,.22);margin-top:6px;padding-top:22px}
/* chat */
.burbuja{max-width:780px;padding:26px 30px 18px;border-radius:30px;font:600 34px/1.36 'Manrope';box-shadow:0 18px 40px -26px rgba(0,0,0,.6)}
.burbuja small{display:block;text-align:right;font:700 26px/1 'Manrope';opacity:.6;margin-top:10px}
.entra{background:#FFFDF9;color:#1D2422;border-bottom-left-radius:8px;align-self:flex-start}
.sale{background:#DCE8E6;color:#123A42;border-bottom-right-radius:8px;align-self:flex-end}
.quien{font:800 26px/1 'Manrope';letter-spacing:.1em;text-transform:uppercase;color:#C9B27E;margin:0 8px 12px;align-self:flex-end}
.pastilla{align-self:flex-end;display:flex;align-items:center;gap:14px;background:#36603F;color:#FFFDF9;border-radius:999px;padding:14px 26px 14px 16px;font:800 30px/1 'Manrope'}
.tilde{flex:none;width:var(--d,52px);height:var(--d,52px);border-radius:50%;background:#36603F;display:grid;place-items:center}
.pastilla .tilde{background:#FFFDF9}
.tilde svg{width:56%;height:56%}
.casas{display:grid;grid-template-columns:repeat(5,1fr);gap:20px 24px}
.casas svg{width:100%;height:auto}
.inst{display:grid;grid-template-columns:1fr 1fr;gap:34px 34px;margin-top:44px}
.inst div{display:flex;gap:18px;align-items:flex-start;border-top:1px solid rgba(201,178,126,.6);padding-top:20px}
.inst svg{flex:none;width:46px;height:46px;color:#C9B27E}
.inst p{font:700 36px/1.25 'Manrope';color:#E9F0EE}
.inst div{padding-top:26px}
"""
CSS = CSS.replace('GRANO', GRANO)

def foto(n):
    return (FOTOS / n).as_uri()

def bg(n, pos='center'):
    return f"background-image:url('{foto(n)}');--pos:{pos}"

def tilde(d=52, color='#FBF8F2'):
    return (f'<span class="tilde" style="--d:{d}px"><svg viewBox="0 0 24 24" fill="none" stroke="{color}" stroke-width="3" '
            'stroke-linecap="round" stroke-linejoin="round"><path d="m5 12.5 4.5 4.5L19 7.5"/></svg></span>')

def pie(arriba='10 lugares de Fundador', abajo='Instalación sin costo · andando en 7 días'):
    return f'<div class="pie"><p class="fechas">{arriba}<span>{abajo}</span></p><p class="firma">Anfitriones<br>del Sur</p></div>'

CASA = '<svg viewBox="0 0 64 56" fill="{f}" stroke="{s}" stroke-width="2.5" stroke-linejoin="round"><path d="M6 26 32 5l26 21v26H6z"/><path d="M26 52V36h12v16" fill="none"/></svg>'
def casas(llenas, total=10, color_lleno='#36603F', borde='#9A3E25'):
    return '<div class="casas">' + ''.join(CASA.format(f=color_lleno if i < llenas else 'none', s=color_lleno if i < llenas else borde) for i in range(total)) + '</div>'

ICONOS = {
    'web': '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6"><circle cx="12" cy="12" r="9"/><path d="M3 12h18M12 3c2.8 3 2.8 15 0 18M12 3c-2.8 3-2.8 15 0 18"/></svg>',
    'chat': '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linejoin="round"><path d="M4 5h16v11H9l-5 4z"/><path d="M8 9.5h8M8 12.5h5"/></svg>',
    'mapa': '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6"><path d="M12 21s-7-6.2-7-11.5A7 7 0 0 1 19 9.5C19 14.8 12 21 12 21z"/><circle cx="12" cy="9.5" r="2.5"/></svg>',
    'base': '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6"><circle cx="9" cy="8" r="3.2"/><path d="M3 20c.5-3.6 3-5.5 6-5.5s5.5 1.9 6 5.5"/><circle cx="17" cy="9" r="2.4"/><path d="M16 14.6c2.6.2 4.4 2 4.8 5.4"/></svg>',
    'sobre': '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linejoin="round"><rect x="3" y="5.5" width="18" height="13" rx="2"/><path d="m4 7 8 6 8-6"/></svg>',
    'reporte': '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round"><path d="M4 20h16M7 16v-5M12 16V6M17 16v-8"/></svg>',
}

AILU_HABLA = 'cuadro-29.jpg'      # sonriendo, a cámara
AILU_PECHO = 'cuadro-22.jpg'      # mano en el pecho
AILU_GESTO = 'cuadro-16.jpg'      # explicando
NOCHE = 'photo-1782226796423-8d72656a332c.jpg'
NIEVE = 'photo-1510798831971-661eb04b3739.jpg'
MANANA = 'photo-1692199037113-ff28ad03f703.jpg'
GRUPO = 'photo-1599341301512-ca6d7a851fba.jpg'

P = {}

# ═══════════════ IMAGEN 1 · Booking también ═══════════════
def ticket(ancho=820):
    return f"""<div class="ticket" style="width:{ancho}px">
  <p class="cab">Cabaña para 4 · enero</p>
  <p class="r"><span>31 noches × US$ 90</span><b>US$ 2.790</b></p>
  <p class="r rojo"><span>Comisión de la plataforma, 15 %</span><b>−US$ 418,50</b></p>
  <p class="r tot"><span>Te quedó en casa</span><b>US$ 2.371,50</b></p>
</div>"""
P['imagen-1-booking-tambien-feed'] = (1080, 1350, 'papel', f"""<div class="col"><div class="panel" style="--pad:70px 64px 56px">
  <p class="ojo">Cabañas, apart y posadas de Bariloche</p>
  <h1 class="t" style="font-size:118px;margin-top:34px">Llenaste la cabaña en enero. <em>Booking también.</em></h1>
  <div style="margin-top:46px">{ticket(900)}</div>
  <p class="p" style="margin-top:34px">Del huésped que vuelve, que la comisión quede en tu casa.</p>
  {pie()}
</div></div>""")
P['imagen-1-booking-tambien-historia'] = (1080, 1920, 'papel', f"""<div class="col"><div class="panel" style="--pad:250px 64px 370px">
  <p class="ojo">Cabañas, apart y posadas de Bariloche</p>
  <h1 class="t" style="font-size:124px;margin-top:34px">Llenaste la cabaña en enero. <em>Booking también.</em></h1>
  <div style="margin-top:50px">{ticket(940)}</div>
  <p class="p" style="margin-top:36px">Del huésped que vuelve, que la comisión quede en tu casa.</p>
  {pie()}
</div></div>""")

# ═══════════════ IMAGEN 2 · 02:14 ═══════════════
def charla(esc=1.0):
    return f"""<div style="display:flex;flex-direction:column;gap:18px;margin-top:{int(36*esc)}px">
  <p class="burbuja entra">Olá! Vocês têm cabana para 4 pessoas de 12 a 16 de julho?<small>02:14</small></p>
  <p class="quien">Tu asistente</p>
  <p class="burbuja sale" style="margin-top:-6px">Olá! Sim, temos a cabana para 4. Reservando direto, o café da manhã está incluído.<small>02:14</small></p>
  <p class="pastilla">{tilde(44,'#36603F')}Seña cobrada · 02:21</p>
</div>"""
P['imagen-2-dos-catorce-feed'] = (1080, 1350, '', f"""<div class="capa" style="{bg(NOCHE,'50% 50%')}"></div><div class="velo" style="--v:.66"></div>
<div class="sobre" style="--pad:62px 64px 56px">
  <p class="ojo">Julio · una familia de São Paulo</p>
  <p class="cifra" style="font-size:190px;color:#C9B27E;margin-top:18px">02:14</p>
  {charla()}
  <h1 class="t" style="font-size:78px;margin-top:auto">Vos seguías durmiendo. <em>La reserva entró directa.</em></h1>
  <div class="pie" style="margin-top:28px">{'<p class="fechas">Tu WhatsApp con asistente<span>Contesta en el idioma del huésped, a cualquier hora</span></p>'}<p class="firma">Anfitriones<br>del Sur</p></div>
</div>""")
P['imagen-2-dos-catorce-historia'] = (1080, 1920, '', f"""<div class="capa" style="{bg(NOCHE,'50% 50%')}"></div><div class="velo" style="--v:.66"></div>
<div class="sobre" style="--pad:250px 64px 370px">
  <p class="ojo">Julio · una familia de São Paulo</p>
  <p class="cifra" style="font-size:210px;color:#C9B27E;margin-top:18px">02:14</p>
  {charla(1.3)}
  <h1 class="t" style="font-size:84px;margin-top:auto">Vos seguías durmiendo. <em>La reserva entró directa.</em></h1>
  <div class="pie" style="margin-top:28px"><p class="fechas">Tu WhatsApp con asistente<span>Contesta en el idioma del huésped</span></p><p class="firma">Anfitriones<br>del Sur</p></div>
</div>""")

# ═══════════════ IMAGEN 3 · Ailu ═══════════════
P['imagen-3-ailu-feed'] = (1080, 1350, '', f"""<div class="col">
<div class="foto" style="height:760px;{bg('ailu-29-feed.jpg','50% 50%')}"></div>
<div class="panel" style="--pad:44px 64px 54px">
  <p class="t" style="font-size:72px;font-style:italic;font-weight:360;color:#123A42">«Lo que ganás con tu casa tiene que quedar en tu casa.»</p>
  <p class="p" style="margin-top:22px;font-size:32px"><b style="color:#1D2422">Ailu,</b> de las cocinas de Bariloche. Te instalo las reservas directas en 7 días.</p>
  {pie()}
</div></div>""")
P['imagen-3-ailu-historia'] = (1080, 1920, '', f"""<div class="col">
<div class="foto" style="height:1060px;{bg('ailu-29-historia.jpg','50% 50%')}"></div>
<div class="panel" style="--pad:48px 64px 370px">
  <p class="t" style="font-size:74px;font-style:italic;font-weight:360;color:#123A42">«Lo que ganás con tu casa tiene que quedar en tu casa.»</p>
  {pie('Ailu · 10 lugares de Fundador')}
</div></div>""")

# ═══════════════ CARRUSEL 1 · La cuenta de Booking ═══════════════
P['carrusel-1-cuenta-1'] = (1080, 1080, '', f"""<p class="folio">01 / 06</p><div class="col">
<div class="foto" style="height:640px;{bg('ailu-16-carrusel.jpg','50% 50%')}"></div>
<div class="panel banda" style="--pad:40px 64px 44px">
  <p class="ojo">Ailu · Anfitriones del Sur</p>
  <h1 class="t" style="font-size:78px;margin-top:20px">¿Cuánto le pagaste a Booking <em>este año?</em></h1>
  <div style="margin-top:auto;display:flex;justify-content:space-between;align-items:flex-end"><p class="p" style="font-size:31px">Hice la cuenta de una cabaña de Bariloche.</p><p class="sig">Deslizá →</p></div>
</div></div>""")
P['carrusel-1-cuenta-2'] = (1080, 1080, 'papel', """<p class="folio claro">02 / 06</p><div class="col"><div class="panel" style="--pad:84px 72px 70px">
  <p class="ojo">Una cabaña de Bariloche</p>
  <div style="display:flex;flex-wrap:wrap;gap:16px;margin-top:40px"><span class="chip">10 reservas por mes</span><span class="chip">3 noches cada una</span><span class="chip">US$ 90 la noche</span></div>
  <p class="p" style="margin-top:28px">Todo por Booking. Es el ejemplo que muestra la calculadora de la página.</p>
  <div style="margin-top:auto;border-top:1px solid #C9B27E;padding-top:28px"><p class="p">En un año, 120 reservas:</p>
  <p class="cifra" style="font-size:200px;margin-top:16px;color:#123A42">US$ 32.400</p></div>
</div></div>""")
P['carrusel-1-cuenta-3'] = (1080, 1080, 'papel', """<p class="folio claro">03 / 06</p><div class="col"><div class="panel" style="--pad:84px 72px 70px">
  <p class="ojo">Lo que le dejó a Booking</p>
  <p class="cifra" style="font-size:250px;margin-top:auto;color:#B4432F">US$ 4.860</p>
  <h1 class="t" style="font-size:74px;margin-top:34px">El 15 % de todo el año. <em>Incluso de los que ya lo conocían.</em></h1>
</div></div>""")
P['carrusel-1-cuenta-4'] = (1080, 1080, 'papel', f"""<p class="folio claro">04 / 06</p><div class="col"><div class="panel" style="--pad:84px 72px 70px">
  <p class="ojo">De cada 10 reservas</p>
  <h1 class="t" style="font-size:92px;margin-top:30px">3 ya te conocían.</h1>
  <div style="margin-top:auto">{casas(3)}</div>
  <p class="p" style="margin-top:30px">Huéspedes que vuelven y recomendados que te buscan por tu nombre. Igual reservan por Booking.</p>
</div></div>""")
P['carrusel-1-cuenta-5'] = (1080, 1080, 'lago', """<p class="folio claro">05 / 06</p><div class="col"><div class="panel" style="--pad:84px 72px 70px">
  <p class="ojo">Si esos 3 vuelven directo</p>
  <p class="cifra" style="font-size:250px;margin-top:auto;color:#C9B27E">US$ 1.458</p>
  <h1 class="t" style="font-size:66px;margin-top:30px">de comisión que dejás de pagar. <em>Como Fundador pagás la mitad, y solo si entra la reserva.</em></h1>
</div></div>""")
P['carrusel-1-cuenta-6'] = (1080, 1080, '', f"""<p class="folio claro">06 / 06</p><div class="col"><div class="panel" style="--pad:84px 72px 64px">
  <p class="ojo">Anfitriones del Sur</p>
  <h1 class="t" style="font-size:104px;margin-top:38px">Hacé la cuenta <em>con tus números.</em></h1>
  <p class="p" style="margin-top:30px;max-width:900px">Está en la página. O hablá 15 minutos con Ailu: vemos tu número y si tu casa entra como Fundador.</p>
  {pie()}
</div></div>""")

# ═══════════════ CARRUSEL 2 · Una noche de julio ═══════════════
P['carrusel-2-julio-1'] = (1080, 1080, '', f"""<p class="folio">01 / 06</p><div class="col">
<div class="foto" style="height:660px;{bg(NIEVE,'50% 46%')}"></div>
<div class="panel banda" style="--pad:40px 64px 44px">
  <p class="ojo">Julio · 02:14</p>
  <h1 class="t" style="font-size:80px;margin-top:20px">Una familia de São Paulo <em>quiere tu cabaña.</em></h1>
  <div style="margin-top:auto;display:flex;justify-content:space-between;align-items:flex-end"><p class="p" style="font-size:31px">¿Quién le contesta?</p><p class="sig">Deslizá →</p></div>
</div></div>""")
ESCENAS = [
    ('02', '<p class="burbuja entra" style="font-size:44px;max-width:900px">Olá! Vocês têm cabana para 4 pessoas de 12 a 16 de julho?<small>02:14</small></p>',
     '02:14', 'Te escriben en portugués, <em>a la hora que sea.</em>'),
    ('03', '<p class="quien">Tu asistente</p><p class="burbuja sale" style="font-size:42px;max-width:900px">Olá! Sim, temos a cabana para 4. Reservando direto, o café da manhã está incluído.<small>02:14</small></p>',
     '02:14', 'Tu asistente contesta en su idioma, <em>al instante.</em>'),
    ('04', f'<p class="quien">Tu asistente</p><p class="burbuja sale" style="font-size:42px;max-width:900px">Para confirmar, é só pagar o sinal neste link.<small>02:15</small></p><p class="pastilla" style="margin-top:22px;font-size:34px">{tilde(48,"#36603F")}Seña cobrada · 02:21</p>',
     '02:21', 'La seña entra sola. <em>Vos seguís durmiendo.</em>'),
]
for n, chat, hora, texto in ESCENAS:
    P[f'carrusel-2-julio-{int(n)}'] = (1080, 1080, '', f"""<div class="capa" style="{bg(NOCHE,'50% 50%')}"></div><div class="velo" style="--v:.68"></div>
<p class="folio claro" style="color:#DCE8E6">{n} / 06</p>
<div class="sobre" style="--pad:120px 64px 60px">
  <div style="display:flex;flex-direction:column">{chat}</div>
  <div style="margin-top:auto;border-top:1px solid rgba(201,178,126,.75);padding-top:24px">
    <p class="ojo">{hora}</p><h1 class="t" style="font-size:66px;margin-top:16px">{texto}</h1></div>
</div>""")
P['carrusel-2-julio-5'] = (1080, 1080, '', f"""<p class="folio">05 / 06</p><div class="col">
<div class="foto" style="height:600px;{bg(MANANA,'50% 40%')}"></div>
<div class="panel banda" style="--pad:40px 64px 44px">
  <p class="ojo">08:30</p>
  <h1 class="t" style="font-size:76px;margin-top:18px">Te levantás con la reserva hecha. <em>Directa, sin Booking.</em></h1>
  <p class="pastilla" style="margin-top:auto;align-self:flex-start;font-size:30px">{tilde(42,'#36603F')}4 noches · seña cobrada</p>
</div></div>""")
P['carrusel-2-julio-6'] = (1080, 1080, '', f"""<p class="folio">06 / 06</p><div class="col">
<div class="foto" style="height:620px;{bg('ailu-22-carrusel.jpg','50% 50%')}"></div>
<div class="panel" style="--pad:32px 64px 40px">
  <p class="ojo">Ailu · Anfitriones del Sur</p>
  <h1 class="t" style="font-size:72px;margin-top:16px">Te lo instalamos en 7 días. <em>De tu parte, veinte minutos.</em></h1>
  {pie('Hablá 15 minutos con Ailu', '10 lugares de Fundador · instalación sin costo')}
</div></div>""")

# ═══════════════ CARRUSEL 3 · Tu mejor huésped ═══════════════
P['carrusel-3-huesped-1'] = (1080, 1080, '', f"""<p class="folio">01 / 06</p><div class="col">
<div class="foto" style="height:580px;{bg('ailu-29-carrusel.jpg','50% 50%')}"></div>
<div class="panel banda" style="--pad:40px 64px 44px">
  <h1 class="t" style="font-size:74px">Tu mejor huésped vuelve todos los años. <em>Y todos los años pagás comisión.</em></h1>
  <div style="margin-top:auto;display:flex;justify-content:space-between;align-items:flex-end"><p class="p" style="font-size:30px">Ailu · Anfitriones del Sur</p><p class="sig">Deslizá →</p></div>
</div></div>""")
P['carrusel-3-huesped-2'] = (1080, 1080, 'papel', """<p class="folio claro">02 / 06</p><div class="col"><div class="panel" style="--pad:84px 72px 70px">
  <p class="ojo">Seguís en Booking</p>
  <h1 class="t" style="font-size:112px;margin-top:40px">Booking te lo trae la primera vez. <em>La segunda, que vuelva directo a vos.</em></h1>
  <p class="p" style="margin-top:auto">Esto es para los que ya vinieron y para los que te recomiendan.</p>
</div></div>""")
INST = [('web', 'Tu web de reservas, en 3 idiomas'), ('chat', 'Tu WhatsApp con asistente, las 24 horas'), ('mapa', 'Tu ficha de Google, ordenada'),
        ('base', 'Tu base de huéspedes, tuya siempre'), ('sobre', 'Mensajes automáticos antes y después'), ('reporte', 'Tu reporte del mes')]
P['carrusel-3-huesped-3'] = (1080, 1080, 'lago', f"""<p class="folio claro">03 / 06</p><div class="col"><div class="panel" style="--pad:84px 72px 70px">
  <p class="ojo">Lo que te instalamos en 7 días</p>
  <div class="inst">{''.join(f'<div>{ICONOS[i]}<p>{t}</p></div>' for i, t in INST)}</div>
  <p class="p" style="margin-top:auto">De tu parte, veinte minutos: tus fotos, tus tarifas y los accesos.</p>
</div></div>""")
P['carrusel-3-huesped-4'] = (1080, 1080, 'papel', """<p class="folio claro">04 / 06</p><div class="col"><div class="panel" style="--pad:84px 72px 70px">
  <p class="ojo">Fundadores · 10 lugares</p>
  <p class="cifra" style="font-size:330px;margin-top:auto;color:#123A42">7,5 %</p>
  <h1 class="t" style="font-size:70px;margin-top:26px">en lugar del 15 % de Booking, <em>y solo si entra la reserva.</em></h1>
  <div style="display:flex;gap:14px;margin-top:30px"><span class="chip">Instalación sin costo</span><span class="chip">Andando en 7 días</span></div>
</div></div>""")
P['carrusel-3-huesped-5'] = (1080, 1080, '', f"""<p class="folio">05 / 06</p><div class="col">
<div class="foto" style="height:540px;{bg(GRUPO,'50% 60%')}"></div>
<div class="panel banda" style="--pad:40px 64px 46px">
  <p class="ojo">¿Y la temporada baja?</p>
  <h1 class="t" style="font-size:80px;margin-top:18px">Te mandamos grupos, <em>de abril a junio.</em></h1>
  <p class="p" style="margin-top:auto;font-size:31px">Experiencias Patagónicas trae retiros y equipos de empresa a Bariloche. Las casas de la red tienen prioridad.</p>
</div></div>""")
P['carrusel-3-huesped-6'] = (1080, 1080, '', f"""<p class="folio claro">06 / 06</p><div class="col"><div class="panel" style="--pad:84px 72px 64px">
  <p class="ojo">10 lugares de Fundador</p>
  <div style="margin-top:40px;width:760px">{casas(0)}</div>
  <h1 class="t" style="font-size:98px;margin-top:44px">Hablá 15 minutos <em>con Ailu.</em></h1>
  <p class="p" style="margin-top:22px">Vemos tu número de Booking y si tu casa entra.</p>
  {pie('Reservas directas en Bariloche', 'Instalación sin costo · andando en 7 días')}
</div></div>""")


def armar():
    if SALIDA.exists():
        shutil.rmtree(SALIDA)
    SALIDA.mkdir()
    avisos = 0
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
            avisos += bool(info)
            print(nombre, f'{w}x{h}', info or 'ok')
            pg.close()
        b.close()
    print('piezas:', len(P), '· con avisos:', avisos)

if __name__ == '__main__':
    armar()
