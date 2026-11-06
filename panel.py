"""El panel de montaje: una página para pegar todo en GHL sin abrir archivos.
Cada página va como archivo propio del artifact (paginas/<ruta>.html), con el píxel
apagado para la vista previa; «Copiar código» devuelve el código exacto de producción."""
import json, pathlib, re, shutil

ECO = pathlib.Path('/home/claude/eco')
DIST = ECO / 'dist'
OUT = ECO / 'panel'
MARK = '<script>window.fbq=function(){};window._fbq=window.fbq;</script>'

LIBROS = [('sanadores', 'Sanadores Libres'), ('lago', 'Lo que el lago te enseña'), ('montana', 'Lo que la montaña te enseña'),
          ('viento', 'Lo que el viento te enseña'), ('rio', 'Lo que el río te enseña'), ('bosque', 'Lo que el bosque te enseña'),
          ('heroe', 'Héroe descapado'), ('libertades', 'Las 7 libertades fundamentales')]

FILAS = [
  # tab, ruta, archivo, tipo, nombre, nota
  ('hoy', 'preparacion', 'preparacion.html', 'nueva', 'La preparación, después de agendar',
   'Hoy esta ruta muestra «página no encontrada», y es a donde llega quien agenda.'),
  ('hoy', 'instala-tu-clinica', 'agenda.html', 'reemplaza', 'La agenda de la campaña',
   'Lleva tu nombre, letra de 16, el sello legible, la marca en una línea y «diagnóstico». Si la portada de tuclinica.digital muestra esta misma agenda, pega el código también ahí.'),

  ('reemplazar', 'recursos-gratuitos', 'recursos.html', 'reemplaza', 'Los recursos',
   'Quedan 6 herramientas: /modelodenegocio y /guiadeprecios eran la misma página.'),
  ('reemplazar', 'libros', 'libros.html', 'reemplaza', 'Los libros', ''),
  ('reemplazar', 'el-numero', 'el-numero.html', 'reemplaza', 'El Número', 'Hoy muestra la versión anterior.'),
  ('reemplazar', 'app-745191', 'app-745191.html', 'reemplaza', 'Tu app a medida', 'Hoy muestra «Las dos apps».'),
  ('reemplazar', 'gracias', 'gracias.html', 'reemplaza', 'Gracias, después de pagar',
   'Mientras no estén los PDF, el botón de descarga abre tu WhatsApp.'),
  ('reemplazar', 'generador-pp', 'piel-generador.html', 'capa', 'El generador',
   'Deja el código que ya tiene. Suma un segundo bloque de Código personalizado debajo y pega esta capa.'),
  ('reemplazar', 'phr', 'phr.html', 'reemplaza', 'Tu hora real',
   'Mismo video y misma comunidad. Cambia también el título: hoy dice «Agenda llena. Cuenta vacía».'),
  ('reemplazar', 'generador-caja', 'generador-caja.html', 'reemplaza', 'Los 5 mensajes',
   'Mismo video y misma comunidad. Cambia también el título: hoy dice «pacientes».'),
  ('reemplazar', 'automatizar', 'automatizar.html', 'reemplaza', 'El checklist de automatización', 'Mismo video y misma comunidad.'),
  ('reemplazar', 'creatuprotocolo', 'creatuprotocolo.html', 'reemplaza', 'Tu protocolo', 'Mismo video y misma comunidad.'),
  ('reemplazar', 'modelodenegocio', 'modelodenegocio.html', 'reemplaza', 'Tu precio', 'La misma página que /guiadeprecios.'),
  ('reemplazar', 'guiadeprecios', 'guiadeprecios.html', 'reemplaza', 'Tu precio', 'La misma página que /modelodenegocio.'),
  ('reemplazar', 'impostor', 'impostor.html', 'reemplaza', 'Tu patrón', 'Mismo video y misma comunidad.'),

  ('nuevas', 'inicio', 'inicio.html', 'nueva', 'Tu inicio: el universo', 'Es el link de tu bio personal.'),
  ('nuevas', 'app', 'app.html', 'nueva', 'La app', ''),
  ('nuevas', 'capitulos', 'capitulos.html', 'nueva', 'Los primeros capítulos', ''),
] + [
  ('nuevas', f'capitulo-{k}', f'capitulo-{k}.html', 'nueva', f'Capítulo · {n}', '') for k, n in LIBROS
] + [
  ('nuevas', 'lo-que-el-sur-te-ensena', 'lo-que-el-sur-te-ensena.html', 'nueva', 'La colección del sur', ''),
  ('nuevas', 'heroe-descapado', 'heroe-descapado.html', 'nueva', 'Héroe descapado', 'Lista de espera por WhatsApp.'),
  ('nuevas', 'materias-pendientes', 'materias-pendientes.html', 'nueva', 'Materias pendientes', 'Lista de espera por WhatsApp.'),
  ('nuevas', 'intangibles', 'intangibles.html', 'nueva', 'Intangibles', 'Lista de espera por WhatsApp.'),
  ('nuevas', 'clinica-del-lider', 'clinica-del-lider.html', 'nueva', 'La Clínica del Líder',
   'Mientras no estén los links de pago, cada botón abre tu WhatsApp con la elección escrita.'),
]

def meta(s, pat):
    m = re.search(pat, s, re.I | re.S)
    return re.sub(r'\s+', ' ', m.group(1)).strip() if m else ''

if OUT.exists():
    shutil.rmtree(OUT)
(OUT / 'paginas').mkdir(parents=True)

datos = []
for tab, ruta, archivo, tipo, nombre, nota in FILAS:
    s = (DIST / archivo).read_text()
    titulo = meta(s, r'<title>(.*?)</title>')
    desc = meta(s, r'<meta name="description" content="(.*?)"')
    m = re.search(r'<head[^>]*>', s, re.I)
    prev = s[:m.end()] + MARK + s[m.end():] if m else MARK + s
    destino = f'{ruta}.html'
    (OUT / 'paginas' / destino).write_text(prev)
    datos.append(dict(tab=tab, ruta='/' + ruta, archivo=destino, tipo=tipo, nombre=nombre, nota=nota,
                      titulo=titulo, desc=desc, kb=round(len(s.encode()) / 1024)))

html = (ECO / 'panel-plantilla.html').read_text()
seguro = lambda o: json.dumps(o, ensure_ascii=False).replace('</', '<\\/')
html = html.replace('/*DATOS*/[]', seguro(datos)).replace('/*MARK*/""', seguro(MARK))
(OUT / 'index.html').write_text(html)
print(len(datos), 'páginas ·', sum(d['kb'] for d in datos), 'KB')
