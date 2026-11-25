"""Arma las páginas de Experiencias Patagónicas (/retiros-2027 y /anfitriones).

Fuente: ep/<pagina>.html + ep/ep.css + ep/ep.js (la piel «Lago», compartida).
Salida: fijas/<pagina>.html y site/<pagina>.html, cada una entera en un archivo (así la monta el cargador).
Las fotos se escriben U(photo-id,ancho) y salen con su srcset de Unsplash.
Las fotos propias de Ailu se escriben F(carpeta/archivo,ancho) y salen del CDN de imágenes de su GHL.

    python3 ep/build.py
"""
import pathlib, re

EP = pathlib.Path(__file__).resolve().parent
RAIZ = EP.parent
PAGINAS = ['retiros', 'retiros-preparacion', 'anfitriones']


def url(pid, w, h=None):
    u = f'https://images.unsplash.com/{pid}?auto=format&fit=crop&q=72&w={w}'
    return u + (f'&h={h}' if h else '')


def fotos(html):
    def cambio(m):
        pid, w = m.group(1), int(m.group(2))
        chica = max(480, w // 2)
        return f'src="{url(pid, w)}" srcset="{url(pid, chica)} {chica}w, {url(pid, w)} {w}w"'
    html = re.sub(r'src="U\((photo-[a-z0-9-]+),(\d+)\)"', cambio, html)
    return re.sub(r'src="F\(([A-Za-z0-9]+/[A-Za-z0-9._-]+),(\d+)\)"', propia, html)


def ghl(archivo, w):
    """Fotos propias de Ailu, subidas a su GHL: salen achicadas y en webp por el CDN de imágenes de GHL."""
    return f'https://images.leadconnectorhq.com/image/f_webp/q_80/r_{w}/u_https://files.leadconnectorhq.com/file/{archivo}'


def propia(m):
    archivo, w = m.group(1), int(m.group(2))
    chica = max(480, w // 2)
    return f'src="{ghl(archivo, w)}" srcset="{ghl(archivo, chica)} {chica}w, {ghl(archivo, w)} {w}w"'


def sin_comentarios(css):
    return re.sub(r'/\*.*?\*/', '', css, flags=re.S)


css = sin_comentarios((EP / 'ep.css').read_text())
js = (EP / 'ep.js').read_text()
for p in PAGINAS:
    src = (EP / f'{p}.html').read_text()
    assert '/*EP_CSS*/' in src and '/*EP_JS*/' in src, p
    out = fotos(src.replace('/*EP_CSS*/', css.strip()).replace('/*EP_JS*/', js.strip()))
    assert 'U(photo' not in out and 'src="F(' not in out, p
    for carpeta in ('fijas', 'site'):
        (RAIZ / carpeta / f'{p}.html').write_text(out)
    print(p, len(out) // 1024, 'KB')
