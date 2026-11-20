"""Arma las páginas de «La decisión» de Roberto Páez (ropaez.com).

Fuente: roberto/<pagina>.html + roberto/roberto.css + roberto/roberto.js (la piel «Kensho», compartida).
Salida: fijas/<pagina>.html y site/<pagina>.html, cada una entera en un archivo (el nombre es la ruta).
En GHL (subcuenta Roberto Paez, embudo «Método Kensho»), cada paso lleva
    solo la línea del cargador (ghl-linea.html): la ruta decide el archivo.
y la ruta pública es /<pagina> (por ejemplo /la-decision).

    python3 roberto/build.py
"""
import pathlib, re, json, html as H
from iconos import IC

R = pathlib.Path(__file__).resolve().parent
RAIZ = R.parent
PAGINAS = ['la-decision', 'la-decision-sesion', 'la-decision-gracias', 'la-decision-capitulo-1', 'la-decision-hoy', 'la-decision-revision']
IMG = 'https://cdn.jsdelivr.net/gh/learners417/landings@main/imgs/roberto/'
LOGO = 'https://cdn.jsdelivr.net/gh/learners417/landings@main/imgs/roberto/logo-kensho.png'

def icono(k, color='#060828'):
    return (f'<svg viewBox="0 0 24 24" fill="none" stroke="{color}" color="{color}" stroke-width="1.4" '
            f'stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{IC[k]}</svg>')

DECISIONES = [
    ("ascenso", "Te ascendieron", "Y el cargo nuevo pide otra forma de liderar."),
    ("puesto", "Aceptar o no el puesto", "Otra empresa, otra área u otro país."),
    ("mudanza", "Mudarte o quedarte", "Otra ciudad, otro país, otra vida en casa."),
    ("renuncia", "Renunciar", "Cerrar un ciclo que ya dio lo suyo."),
    ("ancla", "Quedarte", "Y que sea una elección, con un plan."),
    ("viaje", "Un traslado", "Lo que gana tu carrera y lo que pide tu casa."),
    ("ia", "La IA en tu rol", "Tu trabajo cambia y eliges hacia dónde ir."),
    ("emprender", "Emprender lo tuyo", "De la empresa a tu propio proyecto."),
    ("vinculo", "Una desvinculación", "Elegir el paso siguiente con calma."),
    ("etapa", "La etapa que sigue", "Un directorio, la consultoría, enseñar."),
]
VIDEOS = [  # testimonios en video de la biblioteca de medios de Roberto (verticales), sin nombres en la página
    ("689c8248df61c285288130ef", "testimonio-juan-carlos.mp4"),
    ("6aa2221bb00694184700c35f", "walter-mendoza-1.mp4"),
    ("6928ab0a362bfe65e0b99f14", "maria-viteli.mp4"),
]
CAPITULO = [
    ("observa", "Tu escena de las 3:17", "Y lo que Roberto vio en 30 años sobre lo que te trajo hasta aquí."),
    ("escribe", "Tu línea de origen", "Los hitos de tu vida que te trajeron a esta decisión."),
    ("mochila", "La mochila", "Lo que llevas a lo que sigue y lo que ya cumplió su tarea."),
    ("carta", "Una carta", "A la forma de trabajar que te trajo hasta aquí: gracias, y hasta aquí."),
    ("cuidate", "Tu termómetro de entrada", "Cinco números para medir dónde empiezas."),
]

def puntos(n):
    return ''.join('<i></i>' for _ in range(n))

def bloques(src):
    src = src.replace('{{LOGO}}', LOGO)
    src = re.sub(r'\{\{IMG:([\w.-]+)\}\}', lambda m: IMG + m.group(1), src)
    src = re.sub(r'\{\{PUNTOS:(\d+)\}\}', lambda m: puntos(int(m.group(1))), src)
    src = src.replace('{{DECISIONES}}', ''.join(
        f'<div><span class="disco">{icono(k)}</span><span><h3>{H.escape(t)}</h3><p>{H.escape(d)}</p></span></div>' for k, t, d in DECISIONES))
    play = ('<svg viewBox="0 0 40 40" aria-hidden="true"><circle cx="20" cy="20" r="19" fill="#F6F4EE"/>'
            '<path d="M16 13l12 7-12 7z" fill="#060828"/></svg>')
    src = src.replace('{{VIDEOS}}', ''.join(
        f'<div class="video" data-video="{i + 1}"><video preload="none" playsinline '
        f'poster="https://files.leadconnectorhq.com/file/thumbnail/{fid}/thumbnail.jpg" '
        f'src="https://files.leadconnectorhq.com/file/{fid}/{nombre}"></video>'
        f'<button type="button" aria-label="Ver el testimonio {i + 1}"><span>{play}Ver el video</span></button></div>'
        for i, (fid, nombre) in enumerate(VIDEOS)))
    src = src.replace('{{CAPITULO}}', ''.join(
        f'<li><span class="disco">{icono(k)}</span><span><h3>{H.escape(t)}</h3><p>{H.escape(d)}</p></span></li>' for k, t, d in CAPITULO))
    if '{{DIAS_JSON}}' in src:   # los 42 días del libro, con su página (sale de dias.json, que arma el libro)
        dias = json.loads((R / 'dias.json').read_text())
        src = src.replace('{{DIAS_JSON}}', json.dumps([{k: d[k] for k in ('k', 'tipo', 'texto', 'pag', 'semana', 'titulo', 'pregunta')} for d in dias], ensure_ascii=False))
        src = src.replace('{{ICONOS_JSON}}', json.dumps({k: IC[k] for k in {d['k'] for d in dias}}, ensure_ascii=False))
    return src

def sin_comentarios(css):
    return re.sub(r'/\*.*?\*/', '', css, flags=re.S)

css = sin_comentarios((R / 'roberto.css').read_text()).strip()
js = (R / 'roberto.js').read_text().strip()
for p in PAGINAS:
    src = (R / f'{p}.html').read_text()
    assert '/*KX_CSS*/' in src, p   # la revisión no lleva roberto.js: sin píxel
    out = bloques(src).replace('/*KX_CSS*/', css).replace('/*KX_JS*/', js)
    assert '{{' not in out, (p, re.findall(r'\{\{[^}]*\}\}', out)[:3])
    for carpeta in ('fijas', 'site'):
        (RAIZ / carpeta / f'{p}.html').write_text(out)
    print(p, len(out) // 1024, 'KB')
