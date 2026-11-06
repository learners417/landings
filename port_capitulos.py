"""Pasa los primeros capítulos de libros.tuclinica.digital a páginas de GHL.
Fuente: /home/claude/zipsrc/paginas-libros/capitulo (el texto de los libros no se toca).
Salida: pages/capitulos.html y pages/capitulo-<libro>.html, listas para build.py."""
import re, pathlib
from PIL import Image

Z = pathlib.Path('/home/claude/zipsrc/paginas-libros')
E = pathlib.Path('/home/claude/eco')
LIBROS = ['lago', 'montana', 'viento', 'rio', 'bosque', 'sanadores', 'heroe', 'libertades']
lector_css = (Z / 'a/lector.css').read_text()
lector_js = (Z / 'a/lector.js').read_text()

# tapas grandes para el lector (se ven a 250 px: 480 px alcanza en pantallas retina)
for k in LIBROS:
    out = E / f'imgs/tapas/{k}-grande.webp'
    if not out.exists():
        im = Image.open(Z / f'a/tapas/{k}.webp').convert('RGB')
        im = im.resize((480, round(im.size[1] * 480 / im.size[0])), Image.LANCZOS)
        im.save(out, 'WEBP', quality=72, method=6)

def link(m):
    ruta, hash_ = m.group(1), m.group(2) or ''
    if ruta.startswith('libros/'):
        return f'data-link="libros"' + (f' data-hash="{hash_}"' if hash_ else '') + ' href="#"'
    if ruta.startswith('el-numero/'):
        return 'data-link="numero" href="#"'
    if ruta == 'capitulo/index.html':
        return 'data-link="capitulo" href="#"'
    c = re.match(r'capitulo/(\w+)/index\.html', ruta)
    if c:
        return f'data-link="cap" data-hash="{c.group(1)}" href="#"'
    raise SystemExit('link sin traducir: ' + ruta)

def portar(src, dst):
    s = src.read_text()
    s = re.sub(r'\s*<link rel="icon"[^>]*>', '', s)
    s = re.sub(r'\s*<meta property="og:image"[^>]*>', '', s)
    s = re.sub(r'<link rel="stylesheet" href="(\.\./)+a/base\.css">', '<style>/*BASE_CSS*/</style>', s)
    s = re.sub(r'<link rel="stylesheet" href="(\.\./)+a/lector\.css">', lambda m: '<style>\n' + lector_css + '\n</style>', s)
    s = re.sub(r'<script src="(\.\./)+a/config\.js"></script>\s*', '', s)
    s = re.sub(r'<script src="(\.\./)+a/base\.js"></script>', '<script>/*BASE_JS*/</script>', s)
    s = re.sub(r'<script src="(\.\./)+a/lector\.js"></script>', lambda m: '<script>\n' + lector_js + '\n</script>', s)
    # tapas: van dentro de la página
    s = re.sub(r'src="(?:\.\./)+a/tapas/(\w+)\.webp"', r'data-img="tapas/\1-grande.webp"', s)
    s = re.sub(r'src="(?:\.\./)+a/tapas/(\w+)-chica\.webp"', r'data-img="tapas/\1-chica.webp"', s)
    # links entre páginas: por la configuración
    s = re.sub(r'href="(?:\.\./)+([\w/.-]+?)(#\w+)?"', lambda m: link(m) if not m.group(1).startswith('http') else m.group(0), s)
    # la palabra del reel lleva a la página del libro en GHL
    s = s.replace("if(k)location.replace(k+'/index.html'+(p?'?p='+encodeURIComponent(p):''));",
                  "if(k)location.replace(((window.TCD&&TCD.cap)||'/capitulo-')+k+(p?'?p='+encodeURIComponent(p):''));")
    s = s.replace('/capitulo?p=MADERA → /capitulo/bosque?p=MADERA', '/capitulos?p=MADERA → /capitulo-bosque?p=MADERA')
    assert '../' not in s, (dst, re.findall(r'.{30}\.\./.{30}', s)[:3])
    assert '/*BASE_CSS*/' in s and '/*BASE_JS*/' in s, dst
    (E / 'pages' / dst).write_text(s)
    print(dst, len(s))

portar(Z / 'capitulo/index.html', 'capitulos.html')
for k in LIBROS:
    portar(Z / f'capitulo/{k}/index.html', f'capitulo-{k}.html')
