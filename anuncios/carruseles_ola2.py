"""Segunda ola: diez carruseles de Experiencias Patagónicas (4:5, 7 tarjetas), con la piel de
«La calculadora» y de las temporadas. Ninguno repite ángulo con los ocho de la primera ola.

  ticket      el precio de cada lugar decide lo que te queda          TICKET
  mastermind  con 10 personas te queda más que con 20                 MASTERMIND
  equipo      encuentros de empresa                                   EQUIPO
  panel       REFUGIO: vender y cobrar en cuotas                      PANEL
  vuelos      tu comunidad vive en seis países                        VUELOS
  programa    los cuatro días, hora por hora                          PROGRAMA
  anual       el primer retiro vende el segundo                       ANUAL
  primero     tenés comunidad y nunca organizaste un retiro           PRIMERO
  socio       16 lugares, vendiendo 8                                 SOCIO
  mensaje     el mensaje para tu comunidad antes de señar             MENSAJE

Datos y textos: página /retiros-2027 (programa de ejemplo, formatos, preguntas, honorario).
Números: misma fórmula de la calculadora de la página (cuenta() en carrusel_calculadora.py).
Fechas: verano 22 feb, 8 y 15 mar · otoño (abril) en la llamada · invierno 5 jul, 16 y 23 ago,
13 sep. Mayo y junio no se ofrecen.

    python3 anuncios/carruseles_ola2.py            # los diez
    python3 anuncios/carruseles_ola2.py socio      # uno
"""
import sys
from build_anuncios import tilde
from carrusel_calculadora import cuenta, m, LOGO, LOGO_SVG, PERSONA
from carruseles_temporada import (CSS as TEMP, ICO, ft, full, sub, hitos, tick_lista, comentario, DESLIZA,
                                  armar as _armar, ENTREGAS)
import carruseles_temporada as T

# ── los números, con la fórmula de la página ──
A, B = cuenta(16, 2200), cuenta(16, 3500)                     # ticket
RET, MM = cuenta(20, 3000), cuenta(10, 5000, 3, 520)          # mastermind
P14 = cuenta(14, 3000)                                        # panel
S16 = cuenta(16, 3000)                                        # socio y mensaje
assert (m(A['que']), A['pct'], A['eq'], m(B['que']), B['pct'], B['eq'], m(A['costo'])) == \
       ('US$ 6.750', 19, 13, 'US$ 27.550', 49, 9, 'US$ 28.450')
assert (m(RET['que']), m(MM['que']), MM['eq']) == ('US$ 25.164', 'US$ 28.469', 5)
assert (m(P14['que']), P14['pct'], P14['eq'], m(42000 * .65)) == ('US$ 16.744', 40, 9, 'US$ 27.300')
assert (m(S16['que']), m(S16['que'] / 2), S16['eq'], m(S16['costo'])) == ('US$ 19.550', 'US$ 9.775', 10, 'US$ 28.450')
# el precio «como un viaje»: producción por persona + un poco más = 2.200
POR = 16 * 4 * 330 / 16, (2400 + A['imp'] + A['hon']) / 16
assert round(POR[0]) + round(POR[1]) + 422 == 2200, POR

ICO.update({
    'web': '<rect x="3" y="4.5" width="18" height="15" rx="2.5"/><path d="M3 9h18"/>',
    'cuotas': '<rect x="2.5" y="6" width="19" height="13" rx="2.5"/><path d="M2.5 10.5h19M6.5 15h4"/>',
    'cel': '<rect x="7" y="2.5" width="10" height="19" rx="2.5"/><path d="M11 18.5h2"/>',
    'lista': '<path d="M9 6.5h11M9 12h11M9 17.5h11"/><circle cx="4.5" cy="6.5" r="1"/><circle cx="4.5" cy="12" r="1"/><circle cx="4.5" cy="17.5" r="1"/>',
    'dos': '<circle cx="8.5" cy="8.5" r="3.2"/><circle cx="16.2" cy="9.6" r="2.6"/><path d="M3 19.5c.9-3 3-4.7 5.5-4.7s4.6 1.7 5.5 4.7M15 14.8c.4-.1.8-.2 1.2-.2 2.2 0 4 1.5 4.8 4.4"/>',
    'casa': '<path d="M3.5 11 12 4l8.5 7"/><path d="M6 9.5V20h12V9.5"/><path d="M10 20v-5h4v5"/>',
    'reloj': '<circle cx="12" cy="12" r="8.5"/><path d="M12 7.5V12l3 2"/>',
})
from carruseles_temporada import ico

CSS = TEMP + """
.ft2{color:#FFFDF9}
.par{display:flex;gap:22px}
.par>div{flex:1;border-radius:40px;padding:40px 36px 38px;display:flex;flex-direction:column;min-height:760px}
.par .a{background:#EAE2D3}
.par .b{background:#123A42;color:#E9F0EE}
.par .et{font:800 27px/1.2 'Manrope';letter-spacing:.12em;text-transform:uppercase;color:#9A3E25}
.par .b .et{color:#C9B27E}
.par .pre{font-family:'Fraunces',serif;font-variation-settings:"SOFT" 100,"opsz" 144;font-weight:330;font-size:150px;line-height:1;letter-spacing:-.04em;margin-top:26px}
.par .b .pre{color:#FFFDF9}
.par .u{font:700 28px/1.2 'Manrope';color:#4F5B57;margin-top:10px}
.par .b .u{color:#B7CBC8}
.par .k{margin-top:auto;border-top:2px dashed rgba(29,36,34,.25);padding-top:24px;font:800 27px/1.2 'Manrope';letter-spacing:.1em;text-transform:uppercase}
.par .b .k{border-color:rgba(233,240,238,.3);color:#C9B27E}
.par .v{font-family:'Fraunces',serif;font-weight:330;font-size:78px;line-height:1;letter-spacing:-.03em;margin-top:14px;white-space:nowrap}
.par .a .v{color:#9A3E25}.par .b .v{color:#FFFDF9}
.par .s{font:700 29px/1.2 'Manrope';margin-top:10px;color:#4F5B57}
.par .b .s{color:#B7CBC8}
.bloque{border-radius:40px;padding:44px 46px;display:flex;flex-direction:column;gap:14px}
.bloque .et{font:800 27px/1.2 'Manrope';letter-spacing:.12em;text-transform:uppercase}
.bloque p.d{font:600 38px/1.28 'Manrope'}
.mas{font-family:'Fraunces',serif;font-weight:300;font-size:110px;line-height:.8;text-align:center;color:#9A3E25;margin:14px 0}
.rango{position:relative;height:14px;border-radius:14px;background:#123A42;margin:104px 40px 84px}
.rango s{position:absolute;top:50%;width:46px;height:46px;border-radius:50%;background:#C9B27E;border:5px solid #F4EFE6;transform:translate(-50%,-50%)}
.rango .lab{position:absolute;top:34px;font:800 29px/1 'Manrope';white-space:nowrap;transform:translateX(-50%)}
.rango .arriba{top:-66px;color:#9A3E25}
.mesa{position:relative;height:560px}
.mesa .tabla{position:absolute;left:170px;right:20px;top:180px;height:180px;border-radius:90px;background:#123A42;display:grid;place-items:center}
.mesa .asiento{position:absolute;width:124px;height:124px;border-radius:50%;background:#FFFDF9;border:2px solid rgba(29,36,34,.18);display:grid;place-items:center;box-shadow:0 18px 30px -20px rgba(18,58,66,.5)}
.mesa .vos{background:#C9B27E;border:0;font:800 32px/1 'Manrope';color:#123A42}
.mesa .asiento svg{width:52px;height:52px}
.fmt{display:flex;flex-direction:column;gap:18px;border-radius:36px;padding:32px 38px 30px}
.fmt .cab{display:flex;justify-content:space-between;align-items:baseline}
.fmt .cab b{font-family:'Fraunces',serif;font-weight:400;font-size:66px;letter-spacing:-.02em}
.fmt .cab span{font:600 29px/1.2 'Manrope';color:#4F5B57}
.fmt .pts{display:flex;flex-wrap:wrap;gap:9px}
.fmt .pts i{width:34px;height:34px;border-radius:50%;background:#123A42}
.fmt .pie2{display:flex;justify-content:space-between;align-items:baseline;border-top:1px solid rgba(29,36,34,.16);padding-top:16px}
.fmt .pie2 span{font:800 27px/1.2 'Manrope';letter-spacing:.1em;text-transform:uppercase;color:#4F5B57}
.fmt .pie2 b{font-family:'Fraunces',serif;font-weight:330;font-size:80px;letter-spacing:-.03em}
.fmt.b{background:#123A42;color:#E9F0EE}
.fmt.b .cab b,.fmt.b .pie2 b{color:#FFFDF9}
.fmt.b .cab span,.fmt.b .pie2 span{color:#B7CBC8}
.fmt.b .pts i{background:#C9B27E}
.fmt.b .pie2{border-color:rgba(233,240,238,.2)}
.cal .r{display:flex;gap:28px;align-items:baseline;padding:28px 0;border-bottom:1px solid rgba(29,36,34,.14)}
.cal .r:last-child{border:0}
.cal .r .cuando{width:180px;flex:none;color:#9A3E25}
.cal .r .t{font-size:54px;line-height:1.08}
.lago .cal .r{border-color:rgba(233,240,238,.16)}.lago .cal .r .cuando{color:#C9B27E}.lago .cal .r .t{color:#FFFDF9}
.claro .linea::before{background:#C9B27E}
.claro .hito::before{background:#FBF8F2}
.claro .hito .h{color:#9A3E25}
.claro .hito .q{color:#1D2422}
.tit-dia{display:flex;align-items:flex-end;gap:26px}
.tit-dia .cifra{font-size:200px;line-height:.76;color:#C9B27E}
.apretado .hito{padding:17px 0}.apretado .hito::before{top:37px}
.claro .tit-dia .cifra{color:#9A3E25}
.tit-dia h1{font-size:96px;padding-bottom:6px}
.split{display:flex;gap:22px}
.split>div{flex:1;border-radius:40px;padding:34px 34px 30px}
.split .et{font:800 27px/1.2 'Manrope';letter-spacing:.12em;text-transform:uppercase}
.split p.i{font:600 34px/1.28 'Manrope';padding:16px 0;border-bottom:1px solid rgba(29,36,34,.12)}
.split p.i:last-child{border:0}
.ed{position:relative;display:flex;justify-content:space-between}
.ed::before{content:"";position:absolute;left:120px;right:120px;top:120px;border-top:3px dashed #C9B27E}
.ed .anio{font-size:76px}
.ed>div{position:relative;width:240px;text-align:center}
.ed .anio{font-family:'Fraunces',serif;font-weight:380;font-size:68px;letter-spacing:-.03em;margin-top:22px}
.ed .n{font:800 27px/1.2 'Manrope';letter-spacing:.12em;text-transform:uppercase;color:#9A3E25;margin-top:6px}
.num3 .r{display:flex;gap:30px;align-items:flex-start;padding:26px 0;border-bottom:1px solid rgba(29,36,34,.14)}
.num3 .r:last-child{border:0}
.num3 .r b{font-family:'Fraunces',serif;font-style:italic;font-weight:330;font-size:120px;line-height:.8;color:#9A3E25;width:80px;flex:none}
.num3 .r p{font:600 44px/1.25 'Manrope'}
.num3 .r{padding:28px 0}
.veinte{display:grid;grid-template-columns:repeat(10,1fr);gap:14px}
.veinte i{aspect-ratio:1;border-radius:50%;border:2px solid rgba(29,36,34,.25);display:grid;place-items:center;font:800 26px/1 'Manrope';font-style:normal;color:#4F5B57}
.veinte i.ok{background:#123A42;border-color:#123A42;color:#FBF8F2}
.veinte i.top{background:#36603F;border-color:#36603F;color:#FBF8F2}
.venn{position:relative;height:540px}
.venn .c{position:absolute;top:0;width:540px;height:540px;border-radius:50%;display:flex;flex-direction:column;justify-content:center}
.venn .c1{left:0;border:3px solid #123A42;background:rgba(18,58,66,.06);padding-left:84px}
.venn .c2{right:0;border:3px solid #9A3E25;background:rgba(154,62,37,.05);align-items:flex-end;padding-right:84px;text-align:right}
.venn .c .cifra{font-size:190px;line-height:.85}
.venn .c1 .cifra{color:#123A42}.venn .c2 .cifra{color:#9A3E25}
.venn .c p{font:800 29px/1.25 'Manrope';letter-spacing:.06em;text-transform:uppercase;margin-top:14px;max-width:220px}
.venn .centro{position:absolute;left:50%;top:50%;transform:translate(-50%,-50%);z-index:2}
.burbuja{position:relative;background:#FFFDF9;border-radius:36px 36px 36px 10px;padding:36px 40px 30px;box-shadow:0 40px 70px -36px rgba(18,58,66,.5)}
.burbuja p{font:600 41px/1.36 'Manrope';color:#1D2422}
.burbuja p+p{margin-top:18px}
.burbuja .hora{font:700 26px/1 'Manrope';color:#4F5B57;text-align:right;margin-top:16px}
.mapa{position:relative;height:640px}
.mapa svg{position:absolute;inset:0;width:100%;height:100%}
.mapa .ciudad{position:absolute;left:0;width:340px;height:76px;border-radius:999px;background:rgba(233,240,238,.1);border:1.5px solid rgba(233,240,238,.25);display:flex;align-items:center;padding:0 28px;font:700 30px/1 'Manrope';color:#FFFDF9}
.mapa .pin{position:absolute;right:0;top:190px;width:250px;height:250px;border-radius:50%;background:#C9B27E;color:#123A42;display:flex;flex-direction:column;align-items:center;justify-content:center;text-align:center}
.mapa .pin b{font-family:'Fraunces',serif;font-weight:400;font-size:52px;letter-spacing:-.02em}
.mapa .pin span{font:800 26px/1.2 'Manrope';letter-spacing:.12em;text-transform:uppercase;margin-top:6px}
.idioma{display:flex;justify-content:space-between}
.idioma>div{text-align:center;width:270px}
.idioma .cir{width:250px;height:250px;margin:0 auto;border-radius:50%;background:#123A42;color:#C9B27E;display:grid;place-items:center;font-family:'Fraunces',serif;font-weight:380;font-size:100px;letter-spacing:-.02em}
.idioma p{font:700 32px/1.2 'Manrope';margin-top:20px}
.lp{display:flex;justify-content:space-between;align-items:center;padding:21px 0;border-bottom:1px solid #E4DED2;font:700 32px/1.2 'Manrope'}
.lp:last-child{border:0}
.est{border-radius:999px;padding:9px 16px;font:800 26px/1 'Manrope';white-space:nowrap}
.est.ok{background:#36603F;color:#FBF8F2}.est.cu{background:#E9DFC9;color:#5E4E26}
.est.se{background:#123A42;color:#FBF8F2}.est.li{border:2px dashed #9AA5A1;color:#4F5B57;padding:7px 14px}
.lago .razon p{color:#E9F0EE}.lago .razon p b{color:#FFFDF9}
.lago .razon{border-color:rgba(233,240,238,.16)}
.big2{display:flex;align-items:flex-end;gap:26px}
.big2 .cifra{line-height:.78}
"""
T.CSS = CSS          # armar() de temporadas lee T.CSS

def h(texto, tam=88, color=None, mt=18, extra=''):
    c = f';color:{color}' if color else ''
    return f'<h1 class="t" style="font-size:{tam}px;margin-top:{mt}px{c}{extra}">{texto}</h1>'

def ojo(t, mt=50):
    return f'<p class="ojo" style="margin-top:{mt}px">{t}</p>'

def p(t, tam=34, color=None, mt='auto', peso=600, extra=''):
    c = f';color:{color}' if color else ''
    return f'<p class="p" style="margin-top:{mt};font-size:{tam}px;font-weight:{peso}{c}{extra}">{t}</p>'

def razones(lista, ultima_sin_borde=True):
    out = ''
    for i, (k, t) in enumerate(lista):
        sb = ';border:0' if ultima_sin_borde and i == len(lista) - 1 else ''
        out += f'<div class="razon" style="{sb}">{ico(k)}<p>{t}</p></div>'
    return out

def puntos(total, pagan, cols=8):
    return (f'<div class="lugares" style="grid-template-columns:repeat({cols},1fr)">' +
            ''.join('<span class="punto"></span>' if i < pagan else '<span class="punto tuyo">' + tilde(10) + '</span>'
                    for i in range(total)) + '</div>')

def notif(quien, hora, msg, color='#123A42', icono='persona'):
    return (f'<div class="notif"><span class="ic" style="background:{color}"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" '
            f'stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round">{ICO[icono] if icono in ICO else ""}</svg></span>'
            f'<div style="flex:1"><p class="cab">{quien}<span>{hora}</span></p><p class="msg">{msg}</p></div></div>')
ICO['persona'] = '<circle cx="12" cy="8.5" r="4"/><path d="M4.5 20c1.4-3.6 4.2-5.4 7.5-5.4s6.1 1.8 7.5 5.4"/>'

CAL = """<div class="cal">
  <div class="r"><p class="cuando">Verano</p><p class="t">22 feb · 8 y 15 mar</p></div>
  <div class="r"><p class="cuando">Otoño</p><p class="t">Abril, en la llamada</p></div>
  <div class="r"><p class="cuando">Nieve</p><p class="t">5 jul · 16 y 23 ago · 13 sep</p></div>
</div>"""

def estaciones(color_txt='#4F5B57'):
    return f"""<div class="fila" style="gap:22px">
  <div class="estacion">{ft('photo-1780345021264-950c42e368f2', 'arco', 'height:440px', '45% 50%')}<h3>Verano</h3><p style="color:{color_txt}">22 feb<br>8 y 15 mar</p></div>
  <div class="estacion">{ft('photo-1763477893101-70d85f5c3414', 'arco', 'height:440px', '50% 55%')}<h3>Otoño</h3><p style="color:{color_txt}">Abril,<br>en la llamada</p></div>
  <div class="estacion">{ft('photo-1505322266409-1c77f8b33a8a', 'arco', 'height:440px', '50% 50%')}<h3>Nieve</h3><p style="color:{color_txt}">5 jul · 16 y 23 ago<br>13 sep</p></div>
</div>"""

def cel(cuerpo, ancho=520, alto=820, extra=''):
    return f'<div class="cel" style="width:{ancho}px;height:{alto}px;{extra}"><div class="pant">{cuerpo}</div></div>'

C = {}

# ───────────────────────── 12 · TICKET ─────────────────────────
C['ticket'] = (13, [
    ('lago', full('photo-1589837391857-2ce9dd7e868a', '50% 50%'), f"""{LOGO}
{sub('Mismo lodge · mismo lago · 16 personas', f'Uno se queda con {m(A["que"])}.<br><em>El otro, con {m(B["que"])}.</em>', 76, DESLIZA)}"""),
    ('papel', '', f"""{LOGO}
{ojo('La única diferencia')}
{h('El precio <em>de cada lugar.</em>', 96)}
<div class="par" style="margin-top:44px">
  <div class="a"><p class="et">Retiro A</p><p class="pre">2.200</p><p class="u">US$ por persona</p>
    <p class="k">Te queda</p><p class="v">{m(A['que'])}</p><p class="s">El {A['pct']} % de lo vendido</p></div>
  <div class="b"><p class="et">Retiro B</p><p class="pre">3.500</p><p class="u">US$ por persona</p>
    <p class="k">Te queda</p><p class="v">{m(B['que'])}</p><p class="s">El {B['pct']} % de lo vendido</p></div>
</div>
{p(f'Los dos pagan lo mismo de producción: {m(A["costo"])}.', 34, '#1D2422', 'auto', 700)}"""),
    ('lago', '', f"""{LOGO}
{ojo('El error')}
{h('Ponerle precio <em>como si fuera un viaje.</em>', 88, '#FFFDF9')}
<div class="ticket" style="margin-top:44px">
  <div class="r"><span>Alojamiento, cocina, traslados y salidas</span><b>US$ {round(POR[0]):,}</b></div>
  <div class="r"><span>Sala, fotos, imprevistos y producción</span><b>US$ {round(POR[1])}</b></div>
  <div class="r"><span>Un poco más</span><b>US$ 422</b></div>
  <div class="r tot"><span style="font-weight:800">Precio por persona</span><b class="cifra" style="font-size:100px;font-weight:330">US$ 2.200</b></div>
</div>
<p class="t" style="font-size:66px;margin-top:auto;color:#FFFDF9;padding-bottom:6px">Así, tu contenido <em>va de regalo.</em></p>""".replace('US$ 1,320', 'US$ 1.320')),
    ('', '', f"""{LOGO}
{ojo('La cuenta que sí')}
{h('Tu programa <em>más el viaje.</em>', 96)}
<div class="bloque" style="background:#123A42;color:#E9F0EE;margin-top:40px"><p class="et" style="color:#C9B27E">Tu programa</p>
  <p class="d">Tus sesiones, tu método y cuatro días cerca tuyo.</p></div>
<p class="mas">+</p>
<div class="bloque" style="background:#FFFDF9"><p class="et" style="color:#9A3E25">El viaje</p>
  <p class="d">Lodge frente al lago, cocina de autor, traslados y velero.</p></div>
<div class="rango"><span class="lab arriba" style="left:50%">US$ 3.500</span><s style="left:50%"></s>
  <span class="lab" style="left:0;transform:none;margin-left:-40px">US$ 2.000</span><span class="lab" style="right:0;left:auto;transform:none;margin-right:-40px">US$ 5.000</span></div>
{p('Los retiros de este nivel van de US$ 2.000 a 5.000 por persona.', 33, '#1D2422', 'auto', 700)}"""),
    ('lago', full('photo-1598284444079-ab715eed2b88', '50% 50%'), f"""{LOGO}
{sub('Lo que compra tu grupo', 'Lo que compra tu grupo es estar <em>cuatro días con vos.</em>', 80)}"""),
    ('papel', '', f"""{LOGO}
{ojo('Y tu número')}
{h(f'Con US$ 3.500, <em>{B["eq"]} lugares pagan todo.</em>', 90)}
<div class="big2" style="margin-top:36px"><p class="cifra" style="font-size:300px;color:#123A42">{B['eq']}</p>
  <p class="t" style="font-size:52px;padding-bottom:8px">de 16 cubren <em>la producción completa.</em></p></div>
<div style="margin-top:44px">{puntos(16, B['eq'])}</div>
{p(f'A US$ 2.200 necesitás {A["eq"]} de los 16.', 36, '#1D2422', '34px', 700)}
{p('Calculadora de Experiencias Patagónicas: 16 personas, 4 noches, nivel Premium.', 27)}"""),
    comentario('TICKET', 'Te mandamos la calculadora para probar tu precio.', 'photo-1589837391857-2ce9dd7e868a', '50% 50%', 'lago',
               'Movés el precio y ves cuánto te queda. Si te cierra, Ailu arma tus números reales en 30 minutos.'),
])

# ───────────────────────── 13 · MASTERMIND ─────────────────────────
ASIENTOS = ''.join(f'<span class="asiento" style="left:{x - 62}px;top:{y}px">{PERSONA}</span>'
                   for y in (34, 402) for x in (260, 410, 560, 710, 860))
C['mastermind'] = (17, [
    ('lago', full('photo-1568635795040-a4b24136201f', '50% 50%'), f"""{LOGO}
{sub('Mastermind en Bariloche', 'Con 10 personas<br><em>te queda más que con 20.</em>', 86, DESLIZA)}"""),
    ('papel', '', f"""{LOGO}
{ojo('La cuenta')}
{h('Dos formatos,<br><em>la misma semana.</em>', 88)}
<div class="fmt" style="background:#EAE2D3;margin-top:40px">
  <div class="cab"><b>Retiro</b><span>4 noches · Premium</span></div>
  <div class="pts">{'<i></i>' * 20}</div>
  <div class="pie2"><span>20 × US$ 3.000 · te queda</span><b>{m(RET['que'])}</b></div></div>
<div class="fmt b" style="margin-top:28px">
  <div class="cab"><b>Mastermind</b><span>3 noches · Lujo</span></div>
  <div class="pts">{'<i></i>' * 10}</div>
  <div class="pie2"><span>10 × US$ 5.000 · te queda</span><b>{m(MM['que'])}</b></div></div>
{p('Con la calculadora de la página: Premium US$ 330 y Lujo US$ 520 por persona y por noche, todo incluido.', 27)}"""),
    ('', '', f"""{LOGO}
{ojo('El formato')}
{h('Diez lugares <em>en tu mesa.</em>', 100)}
<div class="mesa" style="margin-top:60px">
  <div class="tabla"><p class="t" style="font-size:68px;color:#FFFDF9"><em style="color:#C9B27E">10</em> lugares</p></div>
  {ASIENTOS}
  <span class="asiento vos" style="left:20px;top:208px">Vos</span>
</div>
{p('Un grupo chico que paga alto por estar en la misma mesa que vos: de 6 a 14 personas, 3 o 4 días.', 38, '#1D2422')}"""),
    ('lago', full('photo-1686670576866-8c9ec4a7fc87', '50% 50%'), f"""{LOGO}
{sub('Nivel Lujo', 'Los mejores hoteles de Bariloche <em>y todo privado.</em>', 82)}"""),
    ('lago', '', f"""{LOGO}
{ojo('Por qué rinde')}
{h('Menos lugares, <em>más cerca tuyo.</em>', 96, '#FFFDF9')}
{ft('photo-1762245273803-60affd991e19', 'estadio calida', 'height:280px;margin-top:40px', '50% 55%')}
<div style="margin-top:16px">{razones([('lista', f'<b>Con {MM["eq"]} lugares vendidos,</b> cubriste todo.'), ('casa', '<b>Un lodge</b> para ustedes y nadie más.'), ('reloj', '<b>Cada persona</b> tiene tu tiempo, los tres días.')])}</div>"""),
    ('papel', '', f"""{LOGO}
{ojo('Fechas 2027')}
{h('Una semana, <em>diez personas.</em>', 100)}
<div style="margin-top:40px">{CAL}</div>
{ft('photo-1777265163251-68d680068d0c', 'estadio', 'height:240px;margin-top:auto', '50% 60%')}
{p('Un grupo por semana. Cuando una fecha se reserva con la seña, se cierra.', 32, '#1D2422', '26px', 700)}"""),
    comentario('MASTERMIND', 'Te mandamos la calculadora con el nivel Lujo.', 'photo-1777265163251-68d680068d0c', '50% 50%', 'lago',
               'Ponés 10 personas y tu precio, y ves lo que te queda antes de vender el primer lugar.'),
])

# ───────────────────────── 14 · EQUIPO ─────────────────────────
FORMATOS = [('photo-1763110806287-ce3c9b382309', '50% 50%', 'El arranque del año del equipo de liderazgo'),
            ('photo-1789681128477-aff6b6b8b23f', '50% 50%', 'Un offsite de estrategia'),
            ('photo-1579541183120-dbb2ab2aa3c5', '50% 60%', 'El viaje de los mejores del equipo')]
C['equipo'] = (23, [
    ('lago', full('photo-1775642103903-cc8170403d78', '50% 50%'), f"""{LOGO}
{sub('Encuentros de empresa', 'El arranque del año de tu equipo, <em>frente a la cordillera.</em>', 80, DESLIZA)}"""),
    ('papel', '', f"""{LOGO}
{ojo('Para quién')}
{h('Tres encuentros <em>que producimos.</em>', 96)}
<div style="display:flex;flex-direction:column;gap:28px;margin-top:44px">""" + ''.join(
        f'<div class="paso">{ft(ph, "circ", "width:200px;height:200px", pos)}<p class="t" style="font-size:58px;line-height:1.06">{tx}</p></div>'
        for ph, pos, tx in FORMATOS) + f"""</div>
<div style="margin-top:auto"><span class="pill" style="background:#123A42;color:#FBF8F2;font-size:34px;padding:22px 34px">15 a 60 personas · 2 a 4 días</span></div>"""),
    ('lago', '', f"""{LOGO}
{ojo('Un ejemplo de dos días')}
{h('Dos días afuera, <em>todo resuelto.</em>', 92, '#FFFDF9')}
<div style="margin-top:34px">{hitos([('', 'Día 1', 'Traslado del aeropuerto y almuerzo frente al lago'), ('', '15:00', 'Sesión de estrategia en una sala con vista'), ('', '20:30', 'Cena de autor, una mesa para todos'), ('ok', 'Día 2', 'Sesión de la mañana y velero por el Nahuel Huapi'), ('ok', '17:00', 'Traslados con el horario de cada vuelo')], 170)}</div>"""),
    ('lago', full('photo-1777265163251-68d680068d0c', '50% 50%'), f"""{LOGO}
{sub('Día 1 · 20:30', 'Cocina de autor y una mesa larga <em>para todo el equipo.</em>', 78)}"""),
    ('', '', f"""{LOGO}
{ojo('Lo que pide una empresa')}
{h('Todo en orden, <em>con su factura.</em>', 96)}
{ft('photo-1571787207812-77254da636a6', 'estadio', 'height:330px;margin-top:38px', '50% 60%')}
<div style="margin-top:18px">{tick_lista(['Cada proveedor factura directo', 'Un solo pago, si lo necesitás', 'Sala con sonido y café', 'El plan B de cada día'])}</div>
{p('Para el pago único, una agencia aliada arma el paquete.', 31, '#1D2422', 'auto', 700)}"""),
    ('lago', '', f"""{LOGO}
{ojo('El tamaño')}
{h('Del equipo de liderazgo <em>a toda la empresa.</em>', 86, '#FFFDF9')}
<div class="big2" style="margin-top:54px"><p class="cifra" style="font-size:250px;color:#C9B27E">15–60</p><p class="t" style="font-size:60px;color:#FFFDF9;padding-bottom:8px">personas</p></div>
<div style="border-top:1px solid rgba(201,178,126,.5);margin-top:44px;padding-top:34px" class="big2">
  <p class="cifra" style="font-size:160px;color:#FFFDF9">2–4</p><p class="t" style="font-size:60px;color:#FFFDF9;padding-bottom:6px">días</p></div>
{ft('photo-1763110806287-ce3c9b382309', 'estadio', 'height:250px;margin-top:auto', '50% 50%')}"""),
    comentario('EQUIPO', 'Ailu te escribe para ver la fecha y el equipo.', 'photo-1775642103903-cc8170403d78', '50% 50%', 'papel',
               'Le contás cuántos son y qué tienen que salir decidiendo. En 48 horas tenés tu propuesta.'),
])

# ───────────────────────── 15 · PANEL (REFUGIO) ─────────────────────────
PANT1 = f"""<p style="font:800 26px/1 Manrope;letter-spacing:.12em;text-transform:uppercase;color:#9A3E25">Retiro de marzo</p>
<div class="big2" style="margin-top:10px"><p class="cifra" style="font-size:150px;color:#123A42">14</p><p style="font:700 30px/1.2 Manrope;padding-bottom:10px">de 16<br>lugares</p></div>
<div class="lugares" style="grid-template-columns:repeat(8,1fr);gap:12px">{''.join('<span class="punto tuyo">' + tilde(10) + '</span>' for _ in range(14))}<span class="punto" style="background:#E4DED2"></span><span class="punto" style="background:#E4DED2"></span></div>
<div class="res"><p class="et">Cobrado</p><p class="cifra" style="font-size:80px">{m(42000 * .65)}</p><small>El 65 % de lo vendido</small></div>"""
LISTA = [('Marina', 'ok', 'Pagado'), ('Diego', 'cu', '2 de 3 cuotas'), ('Paula', 'ok', 'Pagado'), ('Camila', 'se', 'Seña'),
         ('Lucas', 'cu', '1 de 3 cuotas'), ('Lugar 15', 'li', 'Libre'), ('Lugar 16', 'li', 'Libre')]
PANT2 = ('<p style="font:800 26px/1 Manrope;letter-spacing:.12em;text-transform:uppercase;color:#9A3E25">Panel de ejemplo</p>'
         '<p class="t" style="font-size:50px;margin-top:4px">Tus lugares</p><div>' +
         ''.join(f'<div class="lp"><span>{n}</span><span class="est {c}">{e}</span></div>' for n, c, e in LISTA) + '</div>')
C['panel'] = (31, [
    ('lago', '', f"""{LOGO}
{ojo('Tu panel')}
{h('Así se ve tu retiro <em>vendido antes de viajar.</em>', 80, '#FFFDF9')}
<div style="position:relative;height:740px;margin-top:36px">
  {ft('photo-1575393476573-6cdacd2e8c88', 'arco', 'position:absolute;right:0;top:40px;width:480px;height:700px', '50% 50%')}
  {cel(PANT1, 470, 740, 'position:absolute;left:0;top:0')}
</div>"""),
    ('', '', f"""{LOGO}
{ojo('Sin panel')}
{h('Vender 16 lugares <em>por mensajes.</em>', 92)}
<div style="display:flex;flex-direction:column;gap:16px;margin-top:40px">
  {notif('Marina', '22:41', '¿Puedo pagar en cuotas?')}
  {notif('Diego', '23:05', 'Te transferí, ¿te llegó?', '#9A3E25')}
  {notif('Paula', '08:12', '¿Me pasás el link de nuevo?', '#36603F')}
  {notif('Camila', '09:30', '¿Quedan lugares?', '#5E4E26')}
</div>
<p class="t" style="font-size:58px;margin-top:auto;padding-bottom:6px">Y una planilla para saber <em>quién pagó qué.</em></p>"""),
    ('lago', '', f"""{LOGO}
{ojo('Con la seña')}
{h('Te damos REFUGIO, <em>tu panel para vender.</em>', 92, '#FFFDF9')}
<div style="margin-top:40px">{razones([('web', '<b>La página de tu retiro,</b> para tu comunidad.'), ('cuotas', '<b>Los cobros en cuotas</b> de cada lugar.'), ('cel', '<b>La app</b> de cada participante.'), ('lista', '<b>El seguimiento de cada lugar,</b> a la vista.')])}</div>
{ft('photo-1647347040491-c38db922e0e1', 'estadio', 'height:220px;margin-top:auto', '50% 60%')}"""),
    ('papel', '', f"""{LOGO}
{ojo('En tu teléfono')}
<div style="display:flex;gap:40px;margin-top:30px;align-items:flex-start">
  {cel(PANT2, 540, 900)}
  <div style="flex:1;padding-top:30px"><h1 class="t" style="font-size:80px">Cada lugar, <em>a la vista.</em></h1>
    <p class="p" style="font-size:33px;margin-top:30px;color:#1D2422;font-weight:700">Quién pagó, quién va en cuotas y qué lugares quedan.</p></div>
</div>"""),
    ('lago', full('photo-1617548437735-92d875423353', '50% 50%'), f"""{LOGO}
{sub('Al cierre', 'Lo que te queda, <em>con todo pagado.</em>', 80,
     f'<div class="big2" style="margin-top:22px;padding-top:22px;border-top:1px solid rgba(201,178,126,.5)"><p class="cifra" style="font-size:110px;color:#C9B27E">{m(P14["que"])}</p></div>'
     f'<p class="p" style="font-size:31px;margin-top:16px;color:#DCE8E6">14 lugares a US$ 3.000. Con {P14["eq"]} cubriste todo.</p>')}"""),
    ('papel', '', f"""{LOGO}
{ojo('Fechas 2027')}
{h('Elegí tu semana <em>y abrí la venta.</em>', 96)}
<div style="margin-top:44px">{estaciones()}</div>
{p('Con la seña, la fecha es tuya y tu panel queda listo para vender.', 33, '#1D2422', 'auto', 700)}"""),
    comentario('PANEL', 'Te mandamos la página con el panel y la calculadora.', 'photo-1575393476573-6cdacd2e8c88', '50% 50%', 'lago',
               'Ves cómo se vende tu retiro y hacés tu cuenta. Si te cierra, Ailu arma tu fecha en 30 minutos.'),
])

# ───────────────────────── 16 · VUELOS ─────────────────────────
CIUDADES = ['Ciudad de México', 'Bogotá', 'Lima', 'São Paulo', 'Madrid', 'Buenos Aires']
LINEAS = ''.join(f'<path d="M340 {38 + k * 108} C 520 {38 + k * 108}, 520 315, 678 315" fill="none" stroke="#C9B27E" stroke-width="2.4" stroke-dasharray="2 10" stroke-linecap="round"/>'
                 for k in range(6))
MAPA = (f'<div class="mapa"><svg viewBox="0 0 928 640">{LINEAS}</svg>' +
        ''.join(f'<span class="ciudad" style="top:{k * 108}px">{c}</span>' for k, c in enumerate(CIUDADES)) +
        '<div class="pin"><b>Bariloche</b><span>Tu retiro</span></div></div>')
C['vuelos'] = (37, [
    ('lago', full('photo-1735497783787-df488ef67ad1', '88% 50%'), f"""{LOGO}
{sub('Tu comunidad, en un solo lugar', 'México, Bogotá, Madrid, São Paulo.<br><em>Todos aterrizan en Bariloche.</em>', 70, DESLIZA)}"""),
    ('lago', '', f"""{LOGO}
{ojo('Lo que te preocupa')}
{h('Tu comunidad vive <em>en seis países.</em>', 92, '#FFFDF9')}
<div style="margin-top:44px">{MAPA}</div>"""),
    ('papel', '', f"""{LOGO}
{ojo('Día 1 · 15:00')}
{h('Los buscamos por el aeropuerto, <em>con un cartel con el nombre de tu retiro.</em>', 74)}
{ft('photo-1527509675366-a7962560b0f0', 'arco', 'height:580px;margin-top:40px', '50% 62%')}
{p('Cada traslado sale con el horario de vuelo de cada uno, de ida y de vuelta.', 34, '#1D2422')}"""),
    ('', '', f"""{LOGO}
{ojo('En su idioma')}
{h('El programa en español, <em>portugués o inglés.</em>', 92)}
<div class="idioma" style="margin-top:60px">
  <div><span class="cir">ES</span><p>Español</p></div>
  <div><span class="cir">PT</span><p>Português</p></div>
  <div><span class="cir">EN</span><p>English</p></div>
</div>
{p('Producimos para grupos de Argentina, del resto de Latinoamérica, de España y de Brasil.', 35, '#1D2422', '50px')}
{ft('photo-1647476685001-8510e5591ec3', 'estadio', 'height:250px;margin-top:auto', '50% 50%')}"""),
    ('lago', full('photo-1598162461164-5cb059c382c6', '50% 55%'), f"""{LOGO}
{sub('Día 1 · 17:00', 'Té en la galería frente al lago. <em>Cada uno se acomoda a su ritmo.</em>', 74)}"""),
    ('lago', '', f"""{LOGO}
{ojo('De su ciudad a tu retiro')}
{h('Una llegada, <em>paso a paso.</em>', 96, '#FFFDF9')}
<div style="margin-top:36px">{hitos([('', 'Vuelo', 'Desde su ciudad hasta Buenos Aires'), ('', 'Vuelo', 'Directo de Buenos Aires a Bariloche'), ('ok', '15:00', 'Los esperamos con el cartel de tu retiro'), ('ok', '17:00', 'Té frente al lago, en el lodge')], 170)}</div>
{p('Del aeropuerto a la puerta y de vuelta, con el horario de cada uno.', 34, None, '30px')}
{ft('photo-1575819474446-a1acbd0652cf', 'estadio', 'height:200px;margin-top:auto', '50% 60%')}"""),
    comentario('VUELOS', 'Te mandamos las fechas y la calculadora.', 'photo-1527509675366-a7962560b0f0', '50% 62%', 'papel',
               'Elegís la semana que le queda bien a tu comunidad y Ailu arma la llegada de cada uno.'),
])

# ───────────────────────── 17 · PROGRAMA ─────────────────────────
def dia(n, nombre, foto, pos, lista, fondo, alto=330):
    clase = 'lago' if fondo == 'lago' else 'papel claro'
    color = '#FFFDF9' if fondo == 'lago' else None
    return (clase, '', f"""{LOGO}
<div class="tit-dia" style="margin-top:50px"><p class="cifra">{n}</p>{h(nombre, 96, color, 0, ';padding-bottom:4px')}</div>
{ft(foto, 'estadio', f'height:{alto}px;margin-top:36px', pos)}
<div class="apretado" style="margin-top:18px">{hitos(lista, 160)}</div>""")

C['programa'] = (41, [
    ('lago', full('photo-1779690182143-903faa4abf61', '50% 50%'), f"""{LOGO}
{sub('Programa de ejemplo · 4 días', 'Así son los cuatro días, <em>hora por hora.</em>', 90, DESLIZA)}"""),
    dia(1, 'Llegada', 'photo-1647347040491-c38db922e0e1', '50% 50%',
        [('', '15:00', 'Los buscamos por el aeropuerto'), ('', '17:00', 'Té en la galería frente al lago'), ('ok', '20:30', 'Cena de apertura y ronda de intenciones, guiada por vos')], 'lago', 430),
    dia(2, 'Adentro', 'photo-1526779259212-939e64788e3c', '50% 50%',
        [('', '07:30', 'Práctica en silencio junto al agua'), ('ok', '10:00', 'Tu primera sesión, en una sala con vista'), ('', '13:00', 'Almuerzo largo de cocina patagónica'), ('', '16:00', 'Caminata al mirador, a paso tranquilo'), ('', '21:00', 'Cena sin teléfonos')], 'papel', 230),
    dia(3, 'Afuera', 'photo-1579541183120-dbb2ab2aa3c5', '50% 62%',
        [('ok', '09:00', 'Tu segunda sesión'), ('', '14:00', 'Velero privado por el Nahuel Huapi'), ('', '19:00', 'Fuego en la playa del lodge'), ('', '21:30', 'Cena de autor con vinos de la Patagonia')], 'lago', 370),
    dia(4, 'Cierre', 'photo-1569435998017-abb5d562dedf', '50% 50%',
        [('ok', '09:30', 'Sesión de cierre: lo que cada uno se lleva'), ('', '12:30', 'Almuerzo de despedida'), ('', '15:00', 'Traslados al aeropuerto, con el horario de cada vuelo')], 'papel', 360),
    ('', '', f"""{LOGO}
{ojo('Quién hace qué')}
{h('Tu contenido manda, <em>el lugar lo acompaña.</em>', 92)}
<div class="split" style="margin-top:44px">
  <div style="background:#123A42;color:#E9F0EE"><p class="et" style="color:#C9B27E">Vos</p>
    <p class="i" style="border-color:rgba(233,240,238,.16)">La ronda de intenciones</p><p class="i" style="border-color:rgba(233,240,238,.16)">Tus tres sesiones</p><p class="i">Lo que cada uno se lleva</p></div>
  <div style="background:#FFFDF9"><p class="et" style="color:#9A3E25">Nosotras</p>
    <p class="i">Lodge, mesa y traslados</p><p class="i">Velero, mirador y fuego</p><p class="i">El plan B de cada día</p></div>
</div>
{ft('photo-1686670576866-8c9ec4a7fc87', 'estadio', 'height:200px;margin-top:auto', '50% 55%')}
{p('Un programa de ejemplo. El tuyo se arma con vos en la llamada.', 33, '#1D2422', '24px', 700)}"""),
    comentario('PROGRAMA', 'Te mandamos el programa y la calculadora.', 'photo-1779690182143-903faa4abf61', '50% 50%', 'papel',
               'Lo ajustás a tu contenido en una llamada de 30 minutos con Ailu.'),
])

# ───────────────────────── 18 · ANUAL ─────────────────────────
C['anual'] = (43, [
    ('lago', full('photo-1601118964938-228a89955311', '50% 40%'), f"""{LOGO}
{sub('Día 4 · 21:00 · La última cena', '«¿Cuándo es <em>el próximo?»</em>', 112, DESLIZA)}"""),
    ('papel', '', f"""{LOGO}
{ojo('Lo que pasa esa noche')}
{h('Tu primer retiro <em>vende el segundo.</em>', 100)}
{ft('photo-1598162461164-5cb059c382c6', 'arco', 'height:540px;margin-top:40px', '50% 28%')}
{p('La pregunta llega en la última cena. Si ya elegiste la fecha del año que viene, la respuesta es un lugar reservado.', 34, '#1D2422')}"""),
    ('lago', '', f"""{LOGO}
{ojo('Lo que te llevás')}
{h('Todo lo que necesitás <em>para la próxima convocatoria.</em>', 86, '#FFFDF9')}
{ft('photo-1758272960374-343f5eb7fdcd', 'estadio', 'height:340px;margin-top:40px', '50% 55%')}
<div style="margin-top:20px">{tick_lista(['Las fotos del retiro, de un fotógrafo', 'Los testimonios de tu grupo, frente al lago', 'Los nombres de quienes quieren volver'])}</div>
<p class="t" style="font-size:56px;margin-top:auto;color:#FFFDF9;padding-bottom:6px">Con eso convocás <em>la segunda edición.</em></p>"""),
    ('', '', f"""{LOGO}
{ojo('Una fecha fija')}
{h('Una vez es un viaje. <em>Todos los años, es tu evento.</em>', 90)}
<div class="ed" style="margin-top:60px">
  <div>{ft('photo-1780345021264-950c42e368f2', 'circ', 'width:240px;height:240px', '45% 50%')}<p class="anio">2027</p><p class="n">Edición 1</p></div>
  <div>{ft('photo-1617548437735-92d875423353', 'circ', 'width:240px;height:240px', '50% 50%')}<p class="anio">2028</p><p class="n">Edición 2</p></div>
  <div>{ft('photo-1589837391857-2ce9dd7e868a', 'circ', 'width:240px;height:240px', '50% 50%')}<p class="anio">2029</p><p class="n">Edición 3</p></div>
</div>
{p('La misma semana cada año: tu comunidad la agenda con tiempo.', 35, '#1D2422', '44px', 700)}
{ft('photo-1643494555111-df0141d84a62', 'estadio', 'height:230px;margin-top:auto', '50% 55%')}"""),
    ('lago', full('photo-1758272960374-343f5eb7fdcd', '50% 50%'), f"""{LOGO}
{sub('Día 3 · 19:00', 'Las fotos de esta noche <em>convocan a la próxima edición.</em>', 76)}"""),
    ('papel', '', f"""{LOGO}
{ojo('Tu primera edición')}
{h('Elegí la semana <em>que se vuelve tuya.</em>', 96)}
<div style="margin-top:44px">{estaciones()}</div>
{p('Un grupo por semana. Cuando una fecha se reserva con la seña, se cierra.', 33, '#1D2422', 'auto', 700)}"""),
    comentario('ANUAL', 'Te mandamos las fechas 2027 y la calculadora.', 'photo-1601118964938-228a89955311', '50% 40%', 'lago',
               'Elegís la semana de tu primera edición y la convertís en la fecha fija de tu comunidad.'),
])

# ───────────────────────── 19 · PRIMERO ─────────────────────────
VEINTE = ''.join(f'<i class="{"top" if k >= 12 else "ok" if k >= 8 else ""}">{k}</i>' for k in range(1, 21))
PASOS3 = [('photo-1506377711776-dbdc2f3c20d9', '50% 40%', 'Hablamos 30 minutos', 'Salís con un número.'),
          ('photo-1784871258457-3a4b0c4de37f', '50% 50%', 'Tu propuesta en 48 horas', 'Lugar, programa y presupuesto cerrado.'),
          ('photo-1589837391857-2ce9dd7e868a', '50% 50%', 'Reservás con la seña', 'La fecha es tuya y salís a vender.')]
C['primero'] = (47, [
    ('lago', '', f"""{LOGO}
{ft('photo-1787174777308-435461789cc0', 'arco', 'height:620px;margin-top:36px', '55% 92%')}
<p class="cuando" style="margin-top:40px">Tu primer retiro</p>
{h('Tenés comunidad.<br><em>Nunca organizaste un retiro.</em>', 92, '#FFFDF9', 14)}
<p class="sig" style="margin-top:auto;text-align:right;color:#C9B27E">Deslizá →</p>"""),
    ('papel', '', f"""{LOGO}
{ojo('Lo que necesitás')}
{h('Para tu primer retiro <em>alcanzan tres respuestas.</em>', 88)}
<div class="num3" style="margin-top:40px">
  <div class="r"><b>1</b><p>Cuántas personas te siguen hoy y cuántas ya te pagan.</p></div>
  <div class="r"><b>2</b><p>La fecha que tenés en la cabeza.</p></div>
  <div class="r"><b>3</b><p>Lo que querés que tu grupo se lleve.</p></div>
</div>
{ft('photo-1551845728-6820a30c64e2', 'estadio', 'height:170px;margin-top:auto', '50% 40%')}
{p('Con eso, en 30 minutos salís con un número y una fecha posible.', 34, '#1D2422', '26px', 700)}"""),
    ('lago', '', f"""{LOGO}
{ojo('Todo lo demás')}
{h('Lo que no es tu contenido, <em>lo producimos nosotras.</em>', 88, '#FFFDF9')}
<div class="fila" style="margin-top:44px;gap:22px">
  <div class="estacion">{ft('photo-1607712617949-8c993d290809', 'arco', 'height:470px', '50% 50%')}<h3 style="color:#FFFDF9">El lugar</h3><p style="color:#B7CBC8">Un lodge solo para tu grupo</p></div>
  <div class="estacion">{ft('photo-1562050344-f7ad946cee35', 'arco', 'height:470px', '50% 55%')}<h3 style="color:#FFFDF9">La mesa</h3><p style="color:#B7CBC8">Cocina de autor en cada comida</p></div>
  <div class="estacion">{ft('photo-1579541183120-dbb2ab2aa3c5', 'arco', 'height:470px', '50% 60%')}<h3 style="color:#FFFDF9">Afuera</h3><p style="color:#B7CBC8">Velero, termas y cabalgata</p></div>
</div>"""),
    ('', '', f"""{LOGO}
{ojo('Cuántas personas')}
{h('Desde 8. <em>Anda muy bien entre 12 y 20.</em>', 92)}
<div class="veinte" style="margin-top:60px">{VEINTE}</div>
<div style="display:grid;grid-template-columns:7fr 4fr 9fr;gap:14px;margin-top:20px">
  <span></span>
  <p style="font:800 27px/1.25 Manrope;padding-top:12px;border-top:3px solid #123A42">Desde 8</p>
  <p style="font:800 27px/1.25 Manrope;padding-top:12px;border-top:3px solid #36603F;color:#36603F">De 12 a 20, el ideal</p></div>
{p('Un mastermind anda entre 6 y 14. Una empresa puede venir con 60.', 35, '#1D2422', '50px', 700)}
{ft('photo-1599341301512-ca6d7a851fba', 'estadio', 'height:250px;margin-top:auto', '50% 60%')}"""),
    ('lago', '', f"""{LOGO}
{ojo('Cómo empieza')}
{h('De la llamada a tu fecha, <em>en tres pasos.</em>', 88, '#FFFDF9')}
<div style="display:flex;flex-direction:column;gap:40px;margin-top:50px">""" + ''.join(
        f'<div class="paso">{ft(ph, "circ", "width:230px;height:230px", pos)}<p class="n" style="color:#C9B27E;font-size:60px">{k}</p>'
        f'<div><p class="t" style="font-size:56px;line-height:1.06;color:#FFFDF9">{a}</p><p class="p" style="font-size:31px;margin-top:8px">{b}</p></div></div>'
        for k, (ph, pos, a, b) in enumerate(PASOS3, 1)) + '</div>'),
    ('lago', full('photo-1766391606466-13175820b0e9', '50% 50%'), f"""{LOGO}
{sub('Día 2 · 07:30', 'Vos guiás. <em>Del resto nos ocupamos nosotras.</em>', 86)}"""),
    comentario('PRIMERO', 'Te mandamos las fechas y la calculadora.', 'photo-1787174777308-435461789cc0', '58% 60%', 'papel',
               'Llevás tus tres respuestas a la llamada con Ailu y salís con un número y una fecha posible.'),
])

# ───────────────────────── 20 · SOCIO ─────────────────────────
C['socio'] = (53, [
    ('lago', '', f"""{LOGO}
{ft('photo-1783713463607-0e762c7a293a', 'arco', 'height:640px;margin-top:36px', '45% 90%')}
<p class="cuando" style="margin-top:40px">Retiro con dos anfitriones</p>
{h('Un retiro de 16 lugares,<br><em>vendiendo 8.</em>', 96, '#FFFDF9', 14)}
<p class="sig" style="margin-top:auto;text-align:right;color:#C9B27E">Deslizá →</p>"""),
    ('papel', '', f"""{LOGO}
{ojo('La idea')}
{h('Hacelo con un colega <em>que admirás.</em>', 96)}
<div class="venn" style="margin-top:44px">
  <div class="c c1"><p class="cifra">8</p><p>Tu comunidad</p></div>
  <div class="c c2"><p class="cifra">8</p><p>La de tu colega</p></div>
  <span class="pill centro" style="background:#123A42;color:#FBF8F2">16 lugares</span>
</div>
{p('Cada uno vende 8 lugares a su propia comunidad.', 35, '#1D2422', 'auto', 700)}"""),
    ('lago', '', f"""{LOGO}
{ojo('La cuenta de a dos')}
{h('16 lugares, <em>dos anfitriones.</em>', 96, '#FFFDF9')}
<div class="ticket" style="margin-top:44px">
  <div class="r"><span>Lo que venden<small>16 lugares a US$ 3.000</small></span><b>{m(S16['ven'])}</b></div>
  <div class="r rojo"><span>Producción completa, con honorario</span><b>−{m(S16['costo'])}</b></div>
  <div class="r tot"><span style="font-weight:800">Para cada uno<small>De {m(S16['que'])} en total</small></span>
    <b class="cifra" style="font-size:104px;color:#36603F;font-weight:330">{m(S16['que'] / 2)}</b></div>
</div>
<p class="t" style="font-size:62px;margin-top:auto;color:#FFFDF9;padding-bottom:6px">Con {S16['eq']} lugares cubren todo: <em>{S16['eq'] // 2} cada uno.</em></p>"""),
    ('', '', f"""{LOGO}
{ojo('Por qué funciona')}
{h('Dos voces, <em>un solo retiro.</em>', 100)}
{ft('photo-1674150447993-b2b12155bdf1', 'estadio', 'height:380px;margin-top:40px', '50% 62%')}
<div style="margin-top:16px">{razones([('dos', '<b>Dos comunidades</b> que se conocen entre sí.'), ('lista', '<b>Las sesiones se reparten:</b> cada uno da lo suyo.'), ('casa', '<b>Cada uno vende la mitad</b> de los lugares.')])}</div>"""),
    ('lago', full('photo-1758797316165-986ec92e7ad2', '50% 50%'), f"""{LOGO}
{sub('En el retiro', 'Tu comunidad y la de tu colega, <em>en la misma ronda.</em>', 80)}"""),
    ('papel', '', f"""{LOGO}
{ojo('Antes de salir a vender')}
{h('Cuatro acuerdos <em>de entrada.</em>', 100)}
<div style="margin-top:44px">{tick_lista(['Cuántos lugares vende cada uno', 'Quién da cada sesión', 'Cómo reparten lo que queda', 'Una sola persona para producir: Ailu'])}</div>
{ft('photo-1758272960374-343f5eb7fdcd', 'estadio', 'height:250px;margin-top:auto', '50% 55%')}"""),
    comentario('SOCIO', 'Te mandamos la calculadora para la cuenta de a dos.', 'photo-1783713463607-0e762c7a293a', '42% 50%', 'lago',
               'Ponen los lugares de los dos y dividen lo que queda. Si les cierra, arman la fecha con Ailu.'),
])

# ───────────────────────── 21 · MENSAJE ─────────────────────────
C['mensaje'] = (59, [
    ('lago', full('photo-1506377711776-dbdc2f3c20d9', '50% 40%'), f"""{LOGO}
{sub('Antes de señar una fecha', 'Mandá este mensaje <em>a tu comunidad.</em>', 92, DESLIZA)}"""),
    ('papel', '', f"""{LOGO}
{ojo('Copialo tal cual')}
{h('Tres líneas <em>para tu lista de difusión.</em>', 88)}
<div class="burbuja" style="margin-top:44px">
  <p>Estoy armando un retiro de 4 días en Bariloche, frente al lago, para 16 personas.</p>
  <p>Antes de abrir la inscripción quiero saber quién viene.</p>
  <p>Si te interesa, respondeme <b>YO VOY</b> y te paso la fecha y el precio primero.</p>
  <p class="hora">19:00</p>
</div>
{p('Cambiá los números por los tuyos y mandalo.', 34, '#1D2422', 'auto', 700)}"""),
    ('lago', '', f"""{LOGO}
{ojo('Lo que vuelve')}
{h('Contá <em>los «yo voy».</em>', 104, '#FFFDF9')}
<div style="display:flex;flex-direction:column;gap:16px;margin-top:44px">
  {notif('Laura', '19:02', 'Yo voy')}
  {notif('Andrés', '19:10', 'YO VOY. ¿Qué fecha es?', '#9A3E25')}
  {notif('Sofía', '19:24', 'Yo voy, ¿se puede en cuotas?', '#36603F')}
  {notif('Martín', '20:01', 'Yo voy, y le aviso a mi socio', '#5E4E26')}
</div>
<p class="t" style="font-size:58px;margin-top:auto;color:#FFFDF9;padding-bottom:6px">Cada respuesta va a tu lista, <em>en orden de llegada.</em></p>"""),
    ('', '', f"""{LOGO}
{ojo('Tu número')}
{h('Si llegan a tu punto de equilibrio, <em>tenés retiro.</em>', 88)}
<div class="big2" style="margin-top:36px"><p class="cifra" style="font-size:300px;color:#123A42">{S16['eq']}</p>
  <p class="t" style="font-size:50px;padding-bottom:8px">«yo voy» con 16 lugares <em>a US$ 3.000.</em></p></div>
<div style="margin-top:44px">{puntos(16, S16['eq'])}</div>
{p('Tu punto de equilibrio está en la calculadora: son los lugares que pagan todo.', 33, '#1D2422')}"""),
    ('lago', full('photo-1670899460364-ebc917bac09a', '50% 42%'), f"""{LOGO}
{sub('Por qué funciona', 'Tu comunidad te dice que sí <em>antes de que pongas un dólar.</em>', 78)}"""),
    ('lago', '', f"""{LOGO}
{ojo('Y después')}
{h('Tres pasos <em>con tus «yo voy».</em>', 96, '#FFFDF9')}
<div style="margin-top:40px">{hitos([('', '1', 'Hacés tu cuenta en la calculadora'), ('', '2', 'Hablás 30 minutos con Ailu'), ('ok', '3', 'Señás la fecha y avisás primero a tus «yo voy»')], 70)}</div>
{ft('photo-1766391606466-13175820b0e9', 'estadio', 'height:250px;margin-top:auto', '50% 50%')}"""),
    comentario('MENSAJE', 'Te mandamos el mensaje para copiar y la calculadora.', 'photo-1506377711776-dbdc2f3c20d9', '50% 40%', 'papel',
               'Lo mandás a tu comunidad y, con las respuestas, sabés si tu retiro se llena.'),
])


if __name__ == '__main__':
    elegidos = sys.argv[1:] or list(C)
    for n in elegidos:
        seed, tarjetas = C[n]
        _armar(n, seed, tarjetas)
