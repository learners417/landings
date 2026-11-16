"""Revisión local de las páginas de Experiencias Patagónicas: capturas en celular y escritorio,
errores de script y letra menor a 16 px. Sin red: las fuentes salen de /home/claude/fonts y las fotos
se reemplazan por un degradé (la revisión es de forma, no de fotos).

    python3 ep/qa.py site/retiros.html site/anfitriones.html
"""
import sys, os, io, pathlib
from playwright.sync_api import sync_playwright

F = '/home/claude/fonts/node_modules/'
CSS = ''
for w in (400, 500, 600, 700, 800):
    CSS += "@font-face{font-family:'Manrope';font-weight:%d;src:url('file://%s@fontsource/manrope/files/manrope-latin-%d-normal.woff2')}" % (w, F, w)
CSS += "@font-face{font-family:'Fraunces';font-weight:100 900;font-style:normal;src:url('file://%s@fontsource-variable/fraunces/files/fraunces-latin-full-normal.woff2')}" % F
CSS += "@font-face{font-family:'Fraunces';font-weight:100 900;font-style:italic;src:url('file://%s@fontsource-variable/fraunces/files/fraunces-latin-full-italic.woff2')}" % F

def foto():
    from PIL import Image, ImageDraw
    im = Image.new('RGB', (800, 600)); d = ImageDraw.Draw(im)
    for y in range(600):
        t = y / 600
        d.line([(0, y), (800, y)], fill=(int(40 + 80 * t), int(80 + 40 * t), int(90 + 20 * t)))
    b = io.BytesIO(); im.save(b, 'JPEG', quality=70); return b.getvalue()
JPG = foto()

CHICO = """(()=>{const r=[];document.querySelectorAll('body *').forEach(e=>{const t=[...e.childNodes].some(n=>n.nodeType==3&&n.textContent.trim());if(!t)return;const cs=getComputedStyle(e);if(cs.display=='none'||cs.visibility=='hidden')return;if(e.closest('[hidden],.escena:not(.activa)'))return;const s=parseFloat(cs.fontSize);if(s<16)r.push(e.tagName+'.'+e.className+' '+s+'px «'+e.textContent.trim().slice(0,40)+'»')});return [...new Set(r)].slice(0,30)})()"""
ANCHO = """(()=>{const w=document.documentElement.clientWidth;const r=[];document.querySelectorAll('body *').forEach(e=>{const b=e.getBoundingClientRect();if(b.right>w+1&&getComputedStyle(e).position!='fixed'&&!e.closest('.pestanas,.pelicula'))r.push(e.tagName+'.'+e.className+' '+Math.round(b.right))});return r.slice(0,12)})()"""

def ruta(r):
    u = r.request.url
    if u.startswith('file:') or u.startswith('data:'): return r.continue_()
    if 'images.unsplash.com' in u: return r.fulfill(status=200, content_type='image/jpeg', body=JPG)
    if 'fonts.googleapis.com' in u: return r.fulfill(status=200, content_type='text/css', body=CSS)
    return r.abort()

salida = pathlib.Path('/tmp/qa'); salida.mkdir(exist_ok=True)
with sync_playwright() as p:
    b = p.chromium.launch()
    for f in sys.argv[1:]:
        for ancho, alto in ((390, 844), (1440, 900)):
            pg = b.new_page(viewport={'width': ancho, 'height': alto}); errs = []
            pg.on('pageerror', lambda e: errs.append(str(e)[:160]))
            pg.route('**/*', ruta)
            pg.goto('file://' + os.path.abspath(f)); pg.wait_for_timeout(1200)
            pg.evaluate("document.querySelectorAll('.rv').forEach(e=>e.classList.add('in'));document.querySelectorAll('.tachados').forEach(e=>e.classList.add('tachar'))")
            pg.wait_for_timeout(900)
            nombre = f'{pathlib.Path(f).stem}-{ancho}'
            pg.screenshot(path=str(salida / f'{nombre}.png'), full_page=True)
            print('==', nombre, 'errores:', errs, '| chica:', pg.evaluate(CHICO), '| se sale:', pg.evaluate(ANCHO))
            pg.close()
    b.close()
