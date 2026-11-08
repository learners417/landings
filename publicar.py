"""Arma site/: lo que Vercel publica. Cada página queda con el nombre de su ruta en GHL
(tuclinica.digital/phr → site/phr.html), y Vercel la sirve en /phr."""
import pathlib, shutil
ECO = pathlib.Path(__file__).resolve().parent
DIST, FIJAS, SITE = ECO / 'dist', ECO / 'fijas', ECO / 'site'
RUTA = {'agenda.html': 'instala-tu-clinica', 'preparacion.html': 'preparacion',
        'recursos.html': 'recursos-gratuitos', 'gracias.html': 'gracias'}
TAMBIEN = {'recursos.html': ['para-empezar']}   # /para-empezar (nombre del Mapa, 8 nov 2026); /recursos-gratuitos sigue andando
FUERA = {'piel-generador.html'}          # la capa del generador se pega aparte, no es una página
if SITE.exists(): shutil.rmtree(SITE)
SITE.mkdir()
n = 0
# dist/: lo que arma build.py desde pages/ · fijas/: la agenda y la preparación (se editan directo)
fijas = {f.name for f in FIJAS.glob('*.html')}
for f in sorted(list(DIST.glob('*.html')) + list(FIJAS.glob('*.html'))):
    if f.name in FUERA or (f.parent == DIST and f.name in fijas): continue
    shutil.copy(f, SITE / f'{RUTA.get(f.name, f.stem)}.html'); n += 1
    for otra in TAMBIEN.get(f.name, []):           # la misma página con otra ruta de GHL
        shutil.copy(f, SITE / f'{otra}.html'); n += 1
(SITE / 'index.html').write_text('<!DOCTYPE html><html lang="es"><head><meta charset="UTF-8"><meta name="robots" content="noindex">'
    '<meta http-equiv="refresh" content="0;url=https://tuclinica.digital/inicio"><title>Javo Katz</title></head><body></body></html>\n')
print(n, 'páginas en site/')
