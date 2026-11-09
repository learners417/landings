"""Las 6 herramientas de /para-empezar, con la piel de la Edición Libres (9 nov 2026).
Cada una: su palabra (la de los reels), su estación del camino, su libro y su video.
El botón abre la puerta de las herramientas (base.js): nombre y correo, y después la herramienta.
El texto es el aprobado; los títulos pasan a título y subtítulo, como en un libro."""
import pathlib

P = pathlib.Path('/home/claude/eco/pages')

LIBRO = {
    'lago': ('Lo que el lago te enseña', 'Estación 1 del camino, días 1 a 7', 'El lago: tu reset',
             'Su logro: tu reset hecho y tu precio nuevo sellado.', 'tapas/lago-chica.webp', 240, 360, '--c:var(--lago)'),
    'montana': ('Lo que la montaña te enseña', 'Estación 2 del camino, días 8 a 14', 'La montaña: tu programa',
                'Su logro: tu oferta sellada, con su enlace de pago, y tu preventa enviada.', 'tapas/montana-chica.webp', 240, 360, '--c:var(--montana)'),
    'rio': ('Lo que el río te enseña', 'Estación 4 del camino, días 57 a 70', 'El río: tu propia app',
            'Su logro: tu app andando y horas de tu semana recuperadas.', 'tapas/rio-chica.webp', 240, 360, '--c:var(--rio)'),
}

CSS = """
@media (min-width:1000px){ .pliego>.verso{order:-1;display:flex;flex-direction:column;justify-content:center} }
/* el video: una lámina con la foto de Javo; entra al tocarla */
.video{position:relative;margin:0}
.video>button,.video iframe{display:block;width:100%;aspect-ratio:16/10;border:0;padding:0;border-radius:4px}
.video>button{position:relative;cursor:pointer;background:var(--papel-2);padding:9px;box-shadow:0 0 0 1px var(--linea),var(--sombra);text-align:left;font:inherit;color:var(--tinta)}
.video>button img{width:100%;height:100%;object-fit:cover;object-position:center 22%;border-radius:2px;background:var(--papel-3)}
.video .play{position:absolute;left:50%;top:50%;width:76px;height:76px;margin:-38px 0 0 -38px;border-radius:50%;background:var(--tinta);display:grid;place-items:center;box-shadow:inset 0 0 0 4px var(--tinta),inset 0 0 0 5px var(--oro),0 18px 30px -16px rgba(20,18,16,.8);transition:transform .35s var(--e)}
.video .play::before{content:"";margin-left:6px;border-style:solid;border-width:11px 0 11px 18px;border-color:transparent transparent transparent var(--papel-2)}
.video>button:hover .play,.video>button:focus-visible .play{transform:scale(1.06)}
.video figcaption{display:flex;justify-content:space-between;gap:12px;margin-top:12px;font-size:17px}
.video figcaption b{font-family:var(--f-titulo);font-size:23px;font-weight:600;line-height:1.15}
.video figcaption span{flex:none;color:var(--tinta-2);font-size:16px;padding-top:4px}
.palabra{display:inline-block;margin-top:2px;font-weight:600;letter-spacing:.12em}
.estacion-x{display:grid;grid-template-columns:96px 1fr;gap:22px;align-items:start;text-decoration:none;color:inherit;padding:24px 0;border-block:1px solid var(--linea)}
.estacion-x img{width:96px;border-radius:2px 4px 4px 2px;box-shadow:10px 14px 24px -14px rgba(20,18,16,.6)}
.estacion-x .ol-serie{margin:0}
.estacion-x b{display:block;font-family:var(--f-titulo);font-size:32px;font-weight:600;line-height:1.05;margin-top:6px}
.estacion-x p{margin-top:8px;font-size:18px;color:var(--tinta-2)}
.estacion-x .link{display:inline-block;margin-top:12px;color:var(--tinta)}
@media (min-width:760px){ .estacion-x{grid-template-columns:130px 1fr;gap:32px} .estacion-x img{width:130px} }
.dentro .t{font-family:var(--f-titulo);font-size:23px;font-weight:600}
.nota-c{margin-top:22px;font-size:18px;color:var(--tinta-2)}
.nota-c b{color:var(--tinta);font-weight:600}
"""

HEAD = """<!DOCTYPE html>
<html lang="es" data-theme="light">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<title>@@TITLE@@ · Javo Katz</title>
<meta name="description" content="@@DESC@@">
<meta name="theme-color" content="#F4EEE3">
<meta property="og:type" content="website">
<meta property="og:title" content="@@TITLE@@">
<meta property="og:description" content="@@DESC@@">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,500;0,600;1,500;1,600&family=Literata:ital,opsz,wght@0,7..72,400..600;1,7..72,400..500&display=swap">
<style>/*EDICION_CSS*/</style>
<style>""" + CSS + """</style>
</head>
<body data-pagina="@@SLUG@@" data-pagos="" data-palabra="@@PALABRA@@" data-libro-titulo="@@TITLE@@">
"""

# el video entra al tocarlo; el clic a la herramienta queda medido
JS = """
<script>
(function(){
  var pag=document.body.getAttribute('data-pagina');
  document.querySelectorAll('[data-yt]').forEach(function(v){
    var b=v.querySelector('button'); if(!b) return;
    b.addEventListener('click',function(){
      b.outerHTML='<iframe src="https://www.youtube-nocookie.com/embed/'+v.getAttribute('data-yt')+'?autoplay=1&rel=0&playsinline=1" title="'+(v.getAttribute('data-titulo')||'Video')+'" allow="autoplay; encrypted-media; picture-in-picture; fullscreen" allowfullscreen></iframe>';
      if(window.pxc) pxc('VerVideo',{content_name:pag});
    });
  });
  document.querySelectorAll('[data-link="comunidad"]').forEach(function(a){
    a.addEventListener('click',function(){ if(window.pxc) pxc('IrComunidad',{content_name:pag}); });
  });
})();
</script>
"""

DENTRO = [('Calculadora de tu hora real', '2 minutos'), ('Los 5 mensajes de reactivación', 'listos para enviar'),
          ('Checklist de automatización', '12 procesos'), ('Tu protocolo, paso a paso', 'resultado, tiempo y método'),
          ('Guía de precios', 'por especialidad'), ('Neuro-Escáner IA', 'tu patrón con el precio')]


def lideres(filas, clase='lideres'):
    return f'<ul class="{clase}">' + ''.join(
        f'<li><span class="fila"><span class="t">{a}</span><span class="pg"></span><span class="d">{b}</span></span></li>' for a, b in filas) + '</ul>'


def capitulo(n, cid, titulo, dato, h2, bajada, cuerpo, ancho=False):
    b = f'\n   <p class="bajada">{bajada}</p>' if bajada else ''
    return f"""
<section class="cap" id="{cid}" data-capitulo="{titulo}" data-dato="{dato}">
 <div class="cap-in">
  <header class="cap-cab">
   <span class="cap-n">{n}</span>
   <h2>{h2}</h2>{b}
  </header>
  <div class="{'ancho' if ancho else 'cuerpo'}">
{cuerpo}
  </div>
 </div>
</section>
"""


def cuentas(filas, total, nota=''):
    n = f'\n   <p class="nota-c">{nota}</p>' if nota else ''
    return ('   <div class="oferta" style="max-width:none"><p class="ol-serie">Un ejemplo</p>' +
            lideres(filas + [(f'<b>{total[0]}</b>', f'<b style="font-family:var(--f-titulo);font-size:34px;color:var(--oro-texto)">{total[1]}</b>')]) +
            '</div>' + n)


def secuencia(pasos, nota=''):
    li = ''.join(f'<li><span class="sn">{lab}<b>{n}</b></span><div><h3>{t}</h3><p>{p}</p></div></li>' for n, lab, t, p in pasos)
    n = f'\n   <p class="nota-c">{nota}</p>' if nota else ''
    return f'   <ol class="secuencia">{li}</ol>{n}'


def pagina(slug, palabra, estacion, title, desc, h1, sub, lead, video, poster, minutos, cta, caps, cierre, ejemplos=False):
    lib = LIBRO[estacion]
    s = HEAD.replace('@@TITLE@@', title).replace('@@DESC@@', desc).replace('@@SLUG@@', slug).replace('@@PALABRA@@', palabra)
    n = len(caps)
    caps_html = ''.join(capitulo(i + 1, *c) for i, c in enumerate(caps))
    est = capitulo(n + 1, 'estacion', 'Tu estación del camino', lib[2].split(': ')[0], 'Esta herramienta es parte de un libro.', '', f"""   <a class="estacion-x" data-link="cap" data-hash="{estacion}" href="#" style="{lib[7]}">
    <img data-img="{lib[4]}" alt="{lib[0]}" width="{lib[5]}" height="{lib[6]}" loading="lazy">
    <div><p class="ol-serie">{lib[1]}</p><b>{lib[2]}</b><p>{lib[3]} Sigue con el primer capítulo de <i>{lib[0]}</i>, aquí mismo y sin costo.</p><span class="link">Leer el primer capítulo</span></div>
   </a>""")
    dentro = capitulo(n + 2, 'dentro', 'Lo que hay adentro', 'seis herramientas', 'Seis herramientas, sin costo.',
                      'Profesionales que atienden 1 a 1 y construyen su consulta con sistemas. Al dejar tu correo, entras a todas:',
                      '   ' + lideres(DENTRO, 'lideres dentro') +
                      f'\n   <div class="acciones"><a class="btn" data-link="comunidad" href="#">{cta}</a></div>')
    s += f"""
<header class="top"><div class="top-in">
  <a class="marca" data-link="inicio" href="#">Javo Katz</a>
  <p class="rotulo" aria-hidden="true"></p>
  <div class="top-der">
   <button type="button" class="btn-indice" data-indice><i></i>Índice</button>
   <a class="btn" data-link="comunidad" href="#">{cta}</a>
  </div>
</div></header>

<main>
<section class="portadilla" data-barra-desde>
 <div class="wrap">
  <div class="pliego">
   <div class="recto">
    <p class="serie">Para empezar · sin costo</p>
    <h1>{h1}</h1>
    <span class="filete"></span>
    <p class="subtitulo">{sub}</p>
    <p class="bajada">{lead}</p>
    <div class="acciones">
     <a class="btn" data-link="comunidad" href="#">{cta}</a>
    </div>
    <p class="aval"><img data-foto data-ancho="160" alt="" width="52" height="52" data-quita-si-falla><span>Javo Katz. Acompaño a profesionales que atienden 1 a 1: <b>más de 50</b>, en Latinoamérica, España y EE. UU.</span></p>
   </div>
   <div class="verso">
    <figure class="video" data-yt="{video}" data-titulo="{title}">
     <button type="button" aria-label="Ver el video: {poster}"><img data-foto data-ancho="1100" alt="" width="1100" height="688"><span class="play" aria-hidden="true"></span></button>
     <figcaption><b>{poster}</b><span>{minutos} minutos</span></figcaption>
    </figure>
   </div>
  </div>
 </div>
</section>
{caps_html}{est}{dentro}</main>

<footer class="colofon">
 <div class="wrap">
  <p class="cierre">{cierre}</p>
  <div class="acciones"><a class="btn" data-link="comunidad" href="#">{cta}</a></div>
  <p class="micro" style="margin-top:22px">¿Prefieres que lo instalemos juntos? <a class="link" data-link="agenda" href="#">Agenda tu diagnóstico</a></p>
  <div class="lomitos" aria-hidden="true"><i style="--c:#F2EFE7;height:84%"></i><i style="--c:#2B4E68;height:90%"></i><i style="--c:#904932;height:90%"></i><i style="--c:#B48B3F;height:90%"></i><i style="--c:#2F7A80;height:90%"></i><i style="--c:#294637;height:90%"></i><i style="--c:#F5EFE5;height:100%"></i><i style="--c:#E6E1D5;height:100%"></i></div>
  <nav aria-label="Más de Javo Katz"><a data-link="inicio" href="#">Inicio</a><a data-link="recursos" href="#">Las seis herramientas</a><a data-link="libros" href="#">Los libros</a><a data-link="capitulo" href="#">Los primeros capítulos</a><a data-link="camino" href="#">El camino</a><a data-link="agenda" href="#">Mentoría e instalación</a></nav>
  <p class="nota-final">Compuesto en Cormorant Garamond y Literata. Escrito en Bariloche, Patagonia.</p>
  <p class="legal">Javo Katz · Tu Clínica Digital.{' Los números de esta página son un ejemplo para hacer la cuenta.' if ejemplos else ''} Este sitio no forma parte de Meta ni está avalado por Meta.</p>
 </div>
</footer>

<div class="barra"><a class="btn" data-link="comunidad" href="#">{cta}</a></div>

<script>/*EDICION_JS*/</script>"""
    s += JS + "</body>\n</html>\n"
    (P / f'{slug}.html').write_text(s)


# ── 1 · HORA REAL (HORA) ────────────────────────────────────────────
pagina('phr', 'HORA', 'lago', 'Tu hora real',
  'Cuánto te queda por cada hora que de verdad trabajas, y las 3 palancas que mueven ese número.',
  'Cuánto vale tu hora real.', 'Lo que te queda por cada hora que de verdad trabajas.',
  'Cobras por sesión, y tu semana también tiene WhatsApp, gestión y traslados. <b>Ese número decide cuánto vale cada hora de tu vida que le das a tu trabajo.</b>',
  'WyVK5WFTosA', 'Calcula tu hora real conmigo', 11, 'Calcular mi hora real',
  [('cuenta', 'Tres números, dos minutos', '17 USD', 'Tres números, dos minutos.', 'Así se hace la cuenta. En la herramienta la haces con los tuyos.',
    cuentas([('Lo que facturas en el mes', '5.000 USD'), ('Gastos fijos: consultorio, plataformas y formación', '− 900 USD'),
             ('Lo que te queda', '4.100 USD'), ('Horas reales del mes: sesiones, WhatsApp y gestión (55 por semana)', '236 h')],
            ('Tu hora real', '17 USD'), 'Este número depende de cómo está armada tu semana. <b>Tiene 3 palancas.</b>')),
   ('palancas', 'Las 3 palancas', 'lo que mueve tu número', 'Lo que mueve tu número.', '',
    secuencia([('1', 'Palanca', 'Menos horas de gestión', 'Lo que no necesita tu formación lo hace un sistema: confirmaciones, recordatorios y respuestas.'),
               ('2', 'Palanca', 'Más valor por consultante', 'Un programa con principio, final y resultado, en lugar de sesiones sueltas.'),
               ('3', 'Palanca', 'Menos consultantes, mejor acompañados', 'Más ingreso por hora, menos horas y más presencia en cada consulta.')]))],
  'Calcula tu número.', ejemplos=True)

# ── 2 · REACTIVACIÓN (CAJA) ─────────────────────────────────────────
pagina('generador-caja', 'CAJA', 'montana', 'Los consultantes que ya tienes',
  'Antes de invertir en publicidad, mira tu base. Los 5 mensajes exactos para volver a hablarles esta semana.',
  'Los consultantes que ya tienes valen más.', 'Antes de buscar personas nuevas, mira las que ya confiaron en ti.',
  'Personas que ya conocen tu trabajo y a las que nadie volvió a invitar. <b>Los 5 mensajes exactos para hablarles esta semana.</b>',
  'qzioGaxuD_U', 'Los 5 mensajes, uno por uno', 10, 'Quiero los 5 mensajes',
  [('cuenta', 'El ingreso que ya tienes cerca', '2.250 USD', 'El ingreso que ya tienes cerca.', '',
    cuentas([('Personas que atendiste alguna vez', '100'), ('Si vuelve el 15 %', '15'), ('Inversión en publicidad', '0 USD')],
            ('A 150 USD cada una', '2.250 USD'))),
   ('por-que', 'Por qué no volvieron', 'les faltó una invitación', 'Les faltó una invitación.', '',
    secuencia([('1', 'Razón', 'Faltó un próximo paso claro', 'La consulta terminó bien y nadie dijo qué seguía. La vida hizo el resto.'),
               ('2', 'Razón', 'Volver sin explicar les cuesta', 'Para no explicar la ausencia, esperan. Un mensaje tuyo que no la menciona les abre la puerta.'),
               ('3', 'Razón', 'Tu mensaje les da permiso', 'Cuando escribes tú primero, sienten alivio: pueden volver sin explicar nada.')],
              'Los 5 mensajes son una secuencia de 10 días, con el texto exacto. Cada uno cumple una función.'))],
  'Escríbeles esta semana.', ejemplos=True)

# ── 3 · AUTOMATIZAR (SISTEMA) ───────────────────────────────────────
pagina('automatizar', 'SISTEMA', 'rio', 'Un consultorio que funciona aunque tú pares',
  'Las horas que van a la gestión, qué herramienta resuelve cada una y en qué orden, en 4 semanas.',
  'Un consultorio que funciona aunque tú pares.', 'Qué herramienta resuelve cada tarea, y en qué orden.',
  'Las horas que hoy van a confirmar turnos, responder lo mismo y cobrar. <b>Cuatro semanas, una herramienta por semana.</b>',
  'THjdk3TJVek', 'Las 4 semanas, en orden', 12, 'Quiero el checklist',
  [('procesos', 'Lo que hoy lleva tu tiempo', '5 procesos', 'Lo que hoy lleva tu tiempo.', '',
    secuencia([('1', 'Proceso', 'Confirmar turnos', 'Mensaje por mensaje, todos los días.'),
               ('2', 'Proceso', 'Responder consultas nuevas', 'Precio, horarios y modalidad: la misma respuesta, muchas veces por semana.'),
               ('3', 'Proceso', 'Recordar la consulta', 'Con un recordatorio a tiempo, más personas llegan a su turno.'),
               ('4', 'Proceso', 'Acompañar después de la consulta', 'Con seguimiento, más personas terminan su proceso.'),
               ('5', 'Proceso', 'Cobrar', 'Pedir, esperar y confirmar cada transferencia.')],
              'Nada de esto necesita tu formación. <b>Necesita un proceso.</b>')),
   ('orden', 'El orden que funciona', '4 semanas', 'Semana a semana.', '',
    secuencia([('1', 'Semana', 'WhatsApp Business', 'Mensajes automáticos y respuestas rápidas. Lo primero, y lo más simple.'),
               ('2', 'Semana', 'Tu agenda online', 'Cargas tu calendario y compartes el enlace: cada persona elige su horario.'),
               ('3', 'Semana', 'Tu secuencia de seguimiento', 'Confirmación, recordatorio y seguimiento después de la consulta, solos.'),
               ('4', 'Semana', 'Palabras clave en Instagram', 'Si ya publicas, cada palabra clave abre una conversación sola.')],
              'Sin saber de tecnología: el checklist de los 12 procesos, con la herramienta para cada uno.'))],
  'Empieza esta semana.')

# ── 4 · PROTOCOLO (PROTOCOLO) ───────────────────────────────────────
pagina('creatuprotocolo', 'PROTOCOLO', 'montana', 'Vende el resultado',
  'Tu consultante quiere el resultado que tus sesiones le dan. Las 3 cosas que tiene un protocolo que se vende.',
  'Vende el resultado.', 'La sesión tiene techo. El resultado, no.',
  'Tu consultante quiere el resultado que tus sesiones le dan. <b>Cuando vendes el resultado, cambia todo, también el precio.</b>',
  '-Ex9XtRZV4g', 'Arma tu protocolo conmigo', 13, 'Crear mi protocolo',
  [('dos-formas', 'Dos formas de vender lo mismo', '50 o 1.000 USD', 'Dos formas de vender lo mismo.', '',
    '   <div class="oferta" style="max-width:none">' + lideres([('Vendes sesiones: cada semana se decide de nuevo', '50 USD por sesión'),
                                                              ('Vendes un programa: la persona se compromete con su proceso', '1.000 USD por el resultado')]) + '</div>'),
   ('componentes', 'Los 3 componentes', 'resultado, tiempo y método', 'Un protocolo tiene 3 cosas.', '',
    secuencia([('1', 'Parte', 'Un resultado concreto', '«Recuperar tu energía en 8 semanas», en lugar de «mejorar tu alimentación». Específico y medible.'),
               ('2', 'Parte', 'Un tiempo definido', 'Un principio y un final: la persona sabe cuánto dura y qué va a lograr.'),
               ('3', 'Parte', 'Un método con nombre', 'Tus sesiones ordenadas en un camino con pasos. Pasa a ser «tu proceso».')])),
   ('cambia', 'Qué cambia', 'tres cosas a la vez', 'Tres cosas a la vez.', '',
    secuencia([('A', 'Cambia', 'Tu consultante se compromete', 'Con un principio, un final y un resultado, la persona se involucra distinto.'),
               ('B', 'Cambia', 'Tú planificas mejor', 'Sabes cuántas sesiones, en qué orden y hacia dónde.'),
               ('C', 'Cambia', 'Cobras por valor', 'El precio habla del resultado. Ahí crece tu ticket.')]))],
  'Arma tu protocolo.', ejemplos=True)

# ── 5 · PRECIO (PRECIO) · /modelodenegocio redirige aquí ────────────
pagina('guiadeprecios', 'PRECIO', 'lago', 'Un precio sano',
  'Lo que sostiene tu precio y los 3 pasos para subirlo con método.',
  'Un precio sano es parte del cuidado.', 'Así se calcula, y así se sube.',
  'Un precio sano te deja energía para sostener a quien acompañas. <b>La guía de precios por especialidad, paso a paso.</b>',
  'wD5V5MAJPO4', 'Tu precio, paso a paso', 11, 'Ver la guía de precios',
  [('sostiene', 'Lo que sostiene tu precio', '4 cosas', 'Tu precio cubre 4 cosas.', '',
    secuencia([('1', 'Cubre', 'La hora de sesión', 'La única que se ve, y la que casi todos cuentan.'),
               ('2', 'Cubre', 'Tu formación', 'Años de estudio, cursos y supervisión, presentes en cada decisión.'),
               ('3', 'Cubre', 'La gestión invisible', 'WhatsApp, notas, coordinación y seguimiento: horas reales.'),
               ('4', 'Cubre', 'Tu sostenibilidad', 'Descanso, ahorro y futuro, para seguir acompañando por años.')])),
   ('pasos', 'Los 3 pasos', 'con método', 'Cómo subir tu precio con método.', '',
    secuencia([('1', 'Paso', 'Parte del valor', 'Del resultado que das, más que del costo de tu hora.'),
               ('2', 'Paso', 'Estrénalo con quien llega', 'El precio nuevo arranca con las personas que empiezan desde hoy.'),
               ('3', 'Paso', 'Dilo una vez', 'Con calma, y espera la respuesta.')]))],
  'Pon tu precio.')

# ── 6 · CREENCIAS (IMPOSTOR · ESCÁNER) ──────────────────────────────
pagina('impostor', 'IMPOSTOR', 'lago', 'Es un meme, y se cambia',
  '«¿Quién soy yo para cobrar esto?» Esa frase se aprende. Los 3 patrones y el primer movimiento para cambiarla.',
  'Es un meme, y se cambia.', '«¿Quién soy yo para cobrar esto?»',
  'Esa frase la aprendiste: en la facultad, en los pasillos, en el ambiente. <b>Y lo que se aprende, se cambia.</b>',
  '3JPGgF4cjDw', 'Tu patrón, y cómo cambiarlo', 14, 'Hacer el Neuro-Escáner IA',
  [('patrones', 'Los 3 patrones', 'cuál opera en ti', 'Cuál opera en ti.', '',
    secuencia([('A', 'Patrón', 'Ofreces descuento antes de que te lo pidan', 'La persona lee duda donde había valor.'),
               ('B', 'Patrón', 'Explicas tu precio con tu currículum', 'El precio se presenta con calma. Tu formación ya está en tu trabajo.'),
               ('C', 'Patrón', 'Das de más para compensar', 'Sumas tiempo y seguimientos sin cobrarlos: más horas por el mismo ingreso.')],
              'El Neuro-Escáner IA identifica cuál pesa más en ti y el primer movimiento para cambiarlo.')),
   ('movimiento', 'El primer movimiento', 'tres pasos', 'Tres pasos concretos.', '',
    secuencia([('1', 'Paso', 'Identifica tu patrón', 'Con el Neuro-Escáner IA, sin costo.'),
               ('2', 'Paso', 'Cobra el precio correcto una vez', 'A una persona nueva, al precio que corresponde. Su «sí» te enseña más que cualquier teoría.'),
               ('3', 'Paso', 'Repítelo', 'El segundo es más fácil. El décimo, natural.')]))],
  'Identifica tu patrón.')

print('ok')
