"""Tarjetas para compartir (og:image, 1200 x 630) con la piel Paisaje vivo.
Aprobadas por Javo el 17 nov 2026 (muestra: inicio, libros y capitulo-lago).

Una vez:   cd og && npm i @fontsource/manrope@5 @fontsource/literata@5
Armar:     python3 og/tarjeta.py            (todas, en imgs/og/)
           python3 og/tarjeta.py imgs/og libros phr   (solo esas)
Después: subir a main y, si la imagen es nueva, cargar su URL en el panel SEO de GHL
(Imágenes): https://cdn.jsdelivr.net/gh/learners417/landings@main/imgs/og/<clave>.jpg
"""
import sys, os, html, pathlib, tempfile
from playwright.sync_api import sync_playwright
from PIL import Image

AQUI = pathlib.Path(__file__).resolve().parent
REPO = AQUI.parent
FUENTES = AQUI / 'node_modules/@fontsource'
RECORTES = pathlib.Path(tempfile.mkdtemp(prefix='og-'))
# las ilustraciones de La Cima y del mastermind salen de las tapas (sin el título ni la firma)
for _k, _caja in {'montana': (0, 280, 480, 650), 'bosque': (0, 300, 480, 650)}.items():
    Image.open(REPO / f'imgs/tapas/{_k}-grande.webp').convert('RGB').crop(_caja).save(RECORTES / f'{_k}.png')

COL = {
    'lago': '#2B4E68', 'lago2': '#213D52', 'montana': '#904932', 'viento': '#B48B3F', 'rio': '#46979E',
    'bosque': '#294637', 'sanadores': '#3F5450', 'tinta': '#23201D', 'papel': '#F4EEE3', 'papel2': '#E6DCCB',
    'cima': '#9C4F35', 'raices': '#2C4D3D',
}

def uri(p):
    return pathlib.Path(p).as_uri()

def img(rel):
    return uri(REPO / rel)

def telefono(dia):
    return f'<div class="tel"><img src="{img("imgs/app/" + dia + ".webp")}" alt=""></div>'

def tapas(*claves):
    caps = ''.join(f'<img class="tapa t{i}" src="{img("imgs/tapas/" + c + "-grande.webp")}" alt="">' for i, c in enumerate(claves))
    return f'<div class="tapas n{len(claves)}">{caps}</div>'

def sur():
    fila = lambda ks: ''.join(f'<img src="{img("imgs/tapas/" + k + "-grande.webp")}" alt="">' for k in ks)
    return f'<div class="sur"><div>{fila(("lago", "montana", "viento"))}</div><div>{fila(("rio", "bosque"))}</div></div>'

def obra():
    return f'<div class="obra"><img src="{img("imgs/img/obra.webp")}" alt=""></div>'

def numeral(n, txt):
    return f'<div class="num"><b>{n}</b><span>{html.escape(txt)}</span></div>'

def cita(txt):
    return f'<div class="cita">{html.escape(txt)}</div>'

def lomos_grandes():
    return '<div class="grandes">' + ''.join(f'<i style="background:{COL[k]}"></i>' for k in ('lago', 'montana', 'viento', 'rio', 'bosque')) + '</div>'

def recorte(k):
    return f'<div class="rec"><img src="{uri(RECORTES / (k + ".png"))}" alt=""></div>'

LIBRO = {'sanadores': 'Sanadores Libres', 'lago': 'Lo que el lago te enseña', 'montana': 'Lo que la montaña te enseña',
         'viento': 'Lo que el viento te enseña', 'rio': 'Lo que el río te enseña', 'bosque': 'Lo que el bosque te enseña',
         'heroe': 'Héroe descapado', 'libertades': 'Las 7 libertades fundamentales'}

T = {}
def t(clave, titulo, bajada, color, objeto, marca=None):
    T[clave] = dict(titulo=titulo, bajada=bajada, color=color, objeto=objeto, marca=marca)

t('inicio', 'Ganas bien.\nEl problema es lo que te cuesta ganarlo.', 'En 90 días, tu programa y el sistema que lo vende.', 'lago', telefono('dia88'))
t('para-empezar', 'Empieza hoy, con tus números.', 'Seis herramientas con resultado en minutos.', 'lago', telefono('dia1'))
t('preparacion', 'Espera: te falta un paso.', 'Mira este video antes de tu diagnóstico.', 'montana', telefono('dia10'))
t('herramienta', 'Tus herramientas.', 'Tu precio, tus mensajes, tu protocolo y tu hora real.', 'lago', telefono('dia5'))
t('phr', 'Cuánto vale tu hora real.', 'Lo que te queda por cada hora que de verdad trabajas.', 'lago', telefono('dia5'))
t('generador-caja', 'Los consultantes que ya tienes valen más.', 'Los 5 mensajes para volver a hablarles esta semana.', 'viento', telefono('dia30'))
t('automatizar', 'Un consultorio que funciona aunque tú pares.', 'Qué herramienta resuelve cada hora de gestión.', 'rio', telefono('dia38'))
t('creatuprotocolo', 'Vende el resultado.', 'Las 3 cosas que tiene un protocolo que se vende.', 'lago', telefono('dia4'))
t('guiadeprecios', 'Un precio sano es parte del cuidado.', 'Lo que sostiene tu precio y los 3 pasos para subirlo.', 'lago', telefono('dia5'))
t('impostor', 'Es un meme, y se cambia.', '«¿Quién soy yo para cobrar esto?» Los 3 patrones y tu primer movimiento.', 'lago', telefono('dia3'))
t('libros', 'Los 8 libros de Javo Katz', 'Y los primeros cinco días de mi app.', 'papel2', obra())
t('capitulos', '¿Por cuál libro empiezas?', 'El primer capítulo de cada libro, para leer aquí mismo.', 'papel2', obra())
for k in ('sanadores', 'lago', 'montana', 'viento', 'rio', 'bosque', 'libertades'):
    t('capitulo-' + k, LIBRO[k], 'Lee el primer capítulo, aquí mismo.', 'papel2', tapas(k))
t('capitulo-heroe', 'Héroe descapado', 'Lee la apertura, aquí mismo.', 'papel2', tapas('heroe'))
t('lo-que-el-sur-te-ensena', 'Lo que el sur te enseña.', 'Cinco paisajes de la Patagonia. 33 lecciones en cada uno.', 'papel2', sur())
t('heroe-descapado', 'Héroe descapado.', '84 días para salir del agotamiento sin parar tu negocio.', 'papel2', tapas('heroe'))
t('materias-pendientes', 'Materias pendientes.', 'Lo que la escuela no te enseñó a propósito.', 'montana', numeral('7', 'materias, un libro por materia'))
t('intangibles', 'Intangibles.', 'Los grandes maestros, llevados al día a día de quien emprende.', 'bosque', cita('Lo que no se toca pero te toca.'))
t('clinica-del-lider', 'Rinde más.\nVive mejor.', 'Una clínica digital para dueños y directores.', 'lago2', numeral('12', 'semanas, con tu equipo detrás'), marca='Javo Katz')
t('camino', '90 días.\nDel lago al bosque.', 'Cinco estaciones. En cada una instalas un sistema.', 'papel2', lomos_grandes())
t('la-cima', '4 días en Bariloche.', 'Del 17 al 20 de diciembre. Las cinco estaciones, en persona.', 'cima', recorte('montana'))
t('mastermind', 'A la mesa con los más comprometidos.', 'Una mesa chica, por invitación.', 'raices', recorte('bosque'))
t('prensa', 'Javo Katz.', 'Mentor, autor de ocho libros y fundador de Tu Clínica Digital.', 'papel2', obra())
for clave, nombre, libro in (('libro-umbral', 'El umbral', 'sanadores'), ('libro-audio', 'Regrabar', 'sanadores'),
                             ('libro-lago', 'La orilla', 'lago'), ('libro-montana', 'La ruta', 'montana'),
                             ('libro-viento', 'Planear', 'viento'), ('libro-rio', 'El cauce', 'rio'),
                             ('libro-bosque', 'Los anillos', 'bosque')):
    t(clave, nombre, 'La meditación de ' + LIBRO[libro] + '.', 'papel2', tapas(libro))

CSS = """
@font-face{font-family:M;src:url(%(m8)s) format('woff2');font-weight:800}
@font-face{font-family:M;src:url(%(m7)s) format('woff2');font-weight:700}
@font-face{font-family:L;src:url(%(l4)s) format('woff2');font-weight:400}
@font-face{font-family:L;src:url(%(l4i)s) format('woff2');font-weight:400;font-style:italic}
*{box-sizing:border-box;margin:0}
html,body{width:1200px;height:630px;overflow:hidden;background:%(papel)s}
.c{position:relative;width:1200px;height:630px;padding:62px 0 62px 68px;display:flex;gap:56px}
.izq{flex:1;display:flex;flex-direction:column;min-width:0}
.marca{display:flex;align-items:center;gap:16px;font:800 34px/1 M;color:%(tinta)s;letter-spacing:-.01em}
.lomos{display:inline-flex;gap:5px;height:40px}
.lomos i{width:10px;border-radius:3px}
h1{margin-top:auto;font:800 74px/1.03 M;letter-spacing:-.028em;color:%(tinta)s;text-wrap:balance}
p{margin-top:26px;font:400 36px/1.3 L;color:#5A534C;text-wrap:balance}
.hilo{width:120px;height:1px;background:#A8875A;margin-top:34px}
.der{position:relative;flex:none;width:452px;height:630px;margin:-62px 0;padding:62px 62px 62px 0}
.panel{position:relative;width:100%%;height:100%%;border-radius:32px;overflow:hidden;background:var(--c)}
.tel{position:absolute;left:50%%;bottom:-150px;transform:translateX(-50%%);width:268px;padding:10px;border-radius:44px;background:%(tinta)s;box-shadow:0 24px 48px rgba(0,0,0,.28)}
.tel img{display:block;width:100%%;border-radius:34px}
.tapas{position:absolute;inset:0;display:flex;align-items:center;justify-content:center}
.tapa{position:absolute;border-radius:6px;box-shadow:0 22px 44px rgba(0,0,0,.32)}
.n1 .t0{height:392px}
.obra{position:absolute;inset:34px 30px;display:flex;align-items:center;justify-content:center}
.obra img{max-width:100%%;max-height:100%%;filter:drop-shadow(0 14px 22px rgba(0,0,0,.18))}
.sur{position:absolute;inset:0;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:16px}
.sur div{display:flex;gap:14px}
.sur img{height:178px;border-radius:5px;box-shadow:0 14px 26px rgba(0,0,0,.24)}
.num{position:absolute;inset:0;display:flex;flex-direction:column;align-items:center;justify-content:center;color:%(papel)s;text-align:center;padding:0 40px}
.num b{font:800 230px/.9 M;letter-spacing:-.04em}
.num span{margin-top:26px;padding-top:24px;border-top:1px solid #A8875A;font:400 34px/1.25 L;text-wrap:balance}
.cita{position:absolute;inset:0;display:flex;align-items:center;justify-content:center;padding:0 46px;color:%(papel)s;font:italic 400 52px/1.2 L;text-align:center;text-wrap:balance}
.grandes{position:absolute;inset:0;display:flex;align-items:center;justify-content:center;gap:18px}
.grandes i{width:46px;height:330px;border-radius:12px}
.rec img{position:absolute;left:50%%;bottom:0;height:100%%;transform:translateX(-50%%)}
"""

AJUSTE = """document.fonts.ready.then(function(){var h=document.querySelector('h1'),m=document.querySelector('.marca'),t=74;
while(t>50&&h.getBoundingClientRect().top-m.getBoundingClientRect().bottom<56){t-=2;h.style.fontSize=t+'px'}
document.body.setAttribute('data-listo',t)})"""

def pagina(t):
    m = FUENTES / 'manrope/files'
    l = FUENTES / 'literata/files'
    css = CSS % dict(
        m8=uri(m / 'manrope-latin-800-normal.woff2'), m7=uri(m / 'manrope-latin-700-normal.woff2'),
        l4=uri(l / 'literata-latin-400-normal.woff2'), l4i=uri(l / 'literata-latin-400-italic.woff2'),
        papel=COL['papel'], tinta=COL['tinta'])
    if t['marca']:
        marca = html.escape(t['marca'])
    else:
        lomos = ''.join(f'<i style="background:{COL[k]}"></i>' for k in ('lago', 'montana', 'viento', 'rio', 'bosque'))
        marca = f'<span class="lomos">{lomos}</span>Tu Clínica Digital'
    titulo = html.escape(t['titulo']).replace('\n', '<br>')
    return f"""<!doctype html><html lang="es"><head><meta charset="utf-8"><style>{css}</style></head>
<body><div class="c"><div class="izq">
<div class="marca">{marca}</div>
<h1>{titulo}</h1>
<p>{html.escape(t['bajada'])}</p>
<div class="hilo"></div>
</div><div class="der"><div class="panel" style="--c:{COL[t['color']]}">{t['objeto']}</div></div></div><script>{AJUSTE}</script></body></html>"""

def main():
    salida = pathlib.Path(sys.argv[1]) if len(sys.argv) > 1 else REPO / 'imgs/og'
    salida.mkdir(parents=True, exist_ok=True)
    claves = sys.argv[2:] or list(T)
    tmp = pathlib.Path(tempfile.mkdtemp(prefix='og-html-'))
    with sync_playwright() as p:
        b = p.chromium.launch()
        pg = b.new_page(viewport={'width': 1200, 'height': 630}, device_scale_factor=1)
        for k in claves:
            f = tmp / f'{k}.html'
            f.write_text(pagina(T[k]), encoding='utf-8')
            pg.goto(f.as_uri()); pg.wait_for_selector('body[data-listo]'); pg.wait_for_timeout(150)
            png = tmp / f'{k}.png'
            pg.screenshot(path=str(png))
            Image.open(png).convert('RGB').save(salida / f'{k}.jpg', quality=86, optimize=True, progressive=True)
            print(k, os.path.getsize(salida / f'{k}.jpg') // 1024, 'KB', 'título', pg.evaluate("document.body.dataset.listo"))
        b.close()

if __name__ == '__main__':
    main()
