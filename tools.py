"""Las 6 landings de herramientas (llevan a la comunidad de Skool), con la piel y el estándar.
Mismo video y misma herramienta que las páginas viejas; el texto, reescrito al estándar
(sin «gratis», sin «pacientes», sin cifras sin fuente, sin señales de falta de dinero).
El video carga solo al tocarlo (la página pesa poco) y su portada es propia, en papel:
las miniaturas de YouTube son oscuras y dicen «paciente» y «$12/HORA»."""
import pathlib

P = pathlib.Path('/home/claude/eco/pages')

CSS = """
.portada{padding-top:clamp(28px,6vw,64px);padding-bottom:clamp(40px,7vw,72px)}
.video{position:relative;aspect-ratio:16/9;border-radius:var(--r);overflow:hidden;box-shadow:var(--sombra);background:var(--papel-3);margin-top:34px}
.video iframe,.video>button{position:absolute;inset:0;width:100%;height:100%;border:0}
.video>button{display:grid;grid-template-columns:auto 1fr;align-items:center;gap:clamp(16px,4vw,36px);padding:clamp(18px,5vw,52px);background:var(--papel-3);box-shadow:inset 0 0 0 1px var(--linea);text-align:left;cursor:pointer;font:inherit;color:var(--tinta)}
.video .cara{position:relative;width:clamp(104px,24vw,190px);aspect-ratio:1}
.video .cara img{width:100%;height:100%;object-fit:cover;border-radius:50%;background:var(--papel-2);box-shadow:0 0 0 1px var(--oro),0 0 0 7px var(--papel-2),0 0 0 8px var(--linea)}
.video .play{position:absolute;right:-4px;bottom:-4px;width:clamp(46px,9vw,64px);aspect-ratio:1;border-radius:50%;background:var(--tinta);display:grid;place-items:center;box-shadow:0 0 0 4px var(--papel-3),0 14px 26px -14px rgba(43,39,36,.8);transition:transform .35s var(--e)}
.video .play::before{content:"";margin-left:5px;border-style:solid;border-width:10px 0 10px 16px;border-color:transparent transparent transparent var(--papel-2)}
.video>button:hover .play,.video>button:focus-visible .play{transform:scale(1.08)}
.video .pt{display:block;font-family:var(--f-titulo);font-size:clamp(25px,6vw,44px);font-weight:600;line-height:1.05;letter-spacing:-.01em}
.video .dur{display:inline-block;margin-top:12px;font-size:16px;font-weight:800;letter-spacing:.14em;text-transform:uppercase;color:var(--oro-texto)}
.cuentas{margin-top:34px;padding:clamp(22px,5vw,32px)}
.cuentas .fila{display:flex;justify-content:space-between;align-items:baseline;gap:16px;padding:14px 0;border-bottom:1px solid var(--linea);font-size:18px;line-height:1.4}
.cuentas .fila b{flex:none;font-family:var(--f-titulo);font-size:30px;font-weight:600;line-height:1;font-variant-numeric:lining-nums}
.cuentas .total{border-bottom:0;padding-bottom:0}
.cuentas .total span{font-weight:800}
.cuentas .total b{color:var(--oro-texto);font-size:44px}
.cuentas .ej{display:block;font-size:16px;font-weight:800;letter-spacing:.14em;text-transform:uppercase;color:var(--oro-texto);margin-bottom:6px}
.modelos{display:grid;gap:14px;margin-top:34px}
@media (min-width:700px){ .modelos{grid-template-columns:1fr 1fr} }
.modelo{padding:24px}
.modelo span{display:block;font-size:16px;font-weight:800;letter-spacing:.14em;text-transform:uppercase}
.modelo.antes span{color:var(--tinta-2)} .modelo.despues span{color:var(--verde)}
.modelo b{display:block;font-family:var(--f-titulo);font-size:clamp(44px,10vw,56px);font-weight:600;line-height:1;margin-top:10px;font-variant-numeric:lining-nums}
.modelo p{margin-top:8px;font-size:18px;color:var(--tinta-2)}
.modelo.despues{border-color:var(--tinta);box-shadow:0 0 0 1px var(--tinta),var(--sombra)}
.dentro{list-style:none;margin:30px 0 0;padding:0;display:grid;gap:10px}
.dentro li{display:flex;justify-content:space-between;align-items:baseline;gap:16px;padding:16px 20px;background:var(--papel-2);border:1px solid var(--linea);border-radius:16px}
.dentro b{font-family:var(--f-titulo);font-size:25px;font-weight:600;line-height:1.15}
.dentro span{flex:none;font-size:16px;font-weight:700;color:var(--oro-texto)}
@media (max-width:520px){ .dentro li{flex-direction:column;align-items:flex-start;gap:2px} }
.nota-c{margin-top:22px;font-size:18px;color:var(--tinta-2)}
.nota-c b{color:var(--tinta)}
.otro{margin-top:18px;font-size:17px}
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
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,500;0,600;1,500;1,600&family=Manrope:wght@500;600;700;800&display=swap">
<style>/*BASE_CSS*/</style>
<style>""" + CSS + """</style>
</head>
<body data-pagina="@@SLUG@@" data-pagos="">
"""

# el video entra al tocarlo; el clic a la comunidad queda medido
JS = """
<script>
(function(){
  var pag=document.body.getAttribute('data-pagina');
  document.querySelectorAll('[data-yt]').forEach(function(v){
    var b=v.querySelector('button'); if(!b) return;
    b.addEventListener('click',function(){
      v.innerHTML='<iframe src="https://www.youtube-nocookie.com/embed/'+v.getAttribute('data-yt')+'?autoplay=1&rel=0&playsinline=1" title="'+(v.getAttribute('data-titulo')||'Video')+'" allow="autoplay; encrypted-media; picture-in-picture; fullscreen" allowfullscreen></iframe>';
      if(window.pxc) pxc('VerVideo',{content_name:pag});
    });
  });
  document.querySelectorAll('[data-link="comunidad"]').forEach(function(a){
    a.addEventListener('click',function(){ if(window.pxc) pxc('IrComunidad',{content_name:pag}); });
  });
})();
</script>
"""

COMUNIDAD = """
<!-- ═══ LA COMUNIDAD ═══ -->
<section class="sec">
 <div class="wrap">
  <span class="kick rv">La comunidad</span>
  <h2 class="t2 rv">Entra <em>sin costo.</em></h2>
  <p class="lead rv">Profesionales que atienden 1 a 1 y construyen su consulta con sistemas. Adentro tienes las herramientas:</p>
  <ul class="dentro rv">
   <li><b>Calculadora de tu hora real</b><span>2 minutos</span></li>
   <li><b>Los 5 mensajes de reactivación</b><span>listos para enviar</span></li>
   <li><b>Checklist de automatización</b><span>12 procesos</span></li>
   <li><b>Tu protocolo, paso a paso</b><span>resultado, tiempo y método</span></li>
   <li><b>Guía de precios</b><span>por especialidad</span></li>
   <li><b>Neuro-Escáner IA</b><span>tu patrón con el precio</span></li>
  </ul>
  <div class="botones rv"><a class="btn" data-link="comunidad" href="#"><span>Entrar a la comunidad</span> <span class="fl">→</span></a></div>
 </div>
</section>

<!-- ═══ QUIÉN ═══ -->
<section class="sec junto">
 <div class="wrap">
  <div class="autor card rv">
   <img class="foto" data-foto data-ancho="240" alt="Javo Katz" width="120" height="120">
   <div>
    <b>Javo Katz</b>
    <p class="rol">Mentor y autor · Bariloche, Patagonia</p>
    <p class="bio">Hace más de 6 años acompaña a profesionales que atienden 1 a 1. Más de 50, de Latinoamérica, España y EE. UU., ya trabajaron con él.</p>
   </div>
  </div>
 </div>
</section>
"""


def pagina(slug, title, desc, kick, h1, lead, video, poster, minutos, cta, cuerpo, cierre, ejemplos=False):
    s = HEAD.replace('@@TITLE@@', title).replace('@@DESC@@', desc).replace('@@SLUG@@', slug)
    s += f"""
<header class="top"><div class="top-in">
  <a class="marca" data-link="inicio" href="#">Javo Katz<small>Tu Clínica Digital</small></a>
  <a class="btn" data-link="comunidad" href="#"><span>{cta}</span></a>
</div></header>

<main>
<!-- ═══ PORTADA ═══ -->
<section class="portada" data-barra-desde>
 <div class="wrap">
  <span class="kick rv">{kick}</span>
  <h1 class="t1 rv d1">{h1}</h1>
  <p class="lead rv d2">{lead}</p>
  <div class="video rv d2" data-yt="{video}" data-titulo="{title}">
   <button type="button" aria-label="Ver el video: {poster}">
    <span class="cara"><img data-foto data-ancho="400" alt="" width="190" height="190"><span class="play" aria-hidden="true"></span></span>
    <span><span class="pt">{poster}</span><span class="dur">Video · {minutos} min</span></span>
   </button>
  </div>
  <div class="botones rv d3"><a class="btn" data-link="comunidad" href="#"><span>{cta}</span> <span class="fl">→</span></a></div>
  <p class="micro rv d3">Sin costo, dentro de la comunidad.</p>
 </div>
</section>
{cuerpo}
{COMUNIDAD}
<!-- ═══ CIERRE ═══ -->
<section class="sec centro" data-barra-hasta>
 <div class="wrap">
  <hr class="regla">
  <p class="frase-final rv">{cierre}</p>
  <div class="botones rv"><a class="btn" data-link="comunidad" href="#"><span>{cta}</span> <span class="fl">→</span></a></div>
  <p class="otro rv">¿Quieres que lo instalemos juntos? <a class="link" data-link="agenda" data-hash="#agenda" href="#">Agenda tu diagnóstico</a></p>
 </div>
</section>
</main>

<footer class="pie"><div class="wrap">
 <div class="lomos" aria-hidden="true"><i></i><i></i><i></i><i></i><i></i><i></i><i></i><i></i></div>
 <nav><a data-link="inicio" href="#">Inicio</a><a data-link="agenda" href="#">Mentoría e instalación</a><a data-link="appPagina" href="#">La app</a><a data-link="numero" href="#">El Número</a><a data-link="libros" href="#">Los libros</a><a data-link="recursos" href="#">Recursos</a></nav>
 <p>Javo Katz · Tu Clínica Digital · Bariloche, Patagonia</p>{'''
 <p>Los números de esta página son un ejemplo para hacer la cuenta.</p>''' if ejemplos else ''}
</div></footer>

<div class="barra"><a class="btn" data-link="comunidad" href="#"><span>{cta}</span></a></div>

<script>/*BASE_JS*/</script>"""
    s += JS + "</body>\n</html>\n"
    (P / f'{slug}.html').write_text(s)


def ruta(kick, h2, pasos, nota=''):
    li = '\n'.join(f'   <li class="paso rv" data-n="{n}"><h3>{t}</h3>' + (f'<p class="min">{m}</p>' if m else '') + f'<p>{p}</p></li>' for n, t, m, p in pasos)
    n = f'\n  <p class="nota-c rv">{nota}</p>' if nota else ''
    return f"""
<section class="sec">
 <div class="wrap">
  <span class="kick rv">{kick}</span>
  <h2 class="t2 rv">{h2}</h2>
  <ol class="ruta">
{li}
  </ol>{n}
 </div>
</section>
"""


def cuentas(kick, h2, filas, total, nota=''):
    fs = '\n'.join(f'   <div class="fila"><span>{a}</span><b>{b}</b></div>' for a, b in filas)
    n = f'\n  <p class="nota-c rv">{nota}</p>' if nota else ''
    return f"""
<section class="sec junto">
 <div class="wrap">
  <span class="kick rv">{kick}</span>
  <h2 class="t2 rv">{h2}</h2>
  <div class="cuentas card rv">
   <span class="ej">Un ejemplo</span>
{fs}
   <div class="fila total"><span>{total[0]}</span><b>{total[1]}</b></div>
  </div>{n}
 </div>
</section>
"""


# ── 1 · HORA REAL ───────────────────────────────────────────────────
pagina('phr', 'Tu hora real', 'Cuánto te queda por cada hora que de verdad trabajas, y las 3 palancas que mueven ese número.',
  'Calculadora', 'Cuánto vale <em>tu hora real.</em>',
  'Cobras por sesión, y tu semana también tiene WhatsApp, gestión y traslados. <b>Tu hora real es lo que te queda por cada hora que de verdad trabajas.</b>',
  'WyVK5WFTosA', 'Calcula tu hora real conmigo', 11, 'Calcular mi hora real',
  cuentas('La cuenta', 'Tres números, <em>dos minutos.</em>', [
      ('Lo que facturas en el mes', '5.000 USD'),
      ('Gastos fijos: consultorio, plataformas y formación', '− 900 USD'),
      ('Lo que te queda', '4.100 USD'),
      ('Horas reales del mes: sesiones, WhatsApp y gestión (55 por semana)', '236 h'),
  ], ('Tu hora real', '17 USD'), 'Este número depende de cómo está armada tu semana. <b>Tiene 3 palancas.</b>') +
  ruta('Las 3 palancas', 'Lo que mueve <em>tu número.</em>', [
      ('1', 'Menos horas de gestión', '', 'Lo que no necesita tu formación lo hace un sistema: confirmaciones, recordatorios y respuestas.'),
      ('2', 'Más valor por consultante', '', 'Un programa con principio, final y resultado, en lugar de sesiones sueltas.'),
      ('3', 'Menos consultantes, mejor acompañados', '', 'Más ingreso por hora, menos horas y más presencia en cada consulta.'),
  ]),
  'Calcula <em>tu número.</em>', ejemplos=True)

# ── 2 · REACTIVACIÓN ────────────────────────────────────────────────
pagina('generador-caja', 'Los consultantes que ya tienes', 'Antes de invertir en publicidad, mira tu base. Los 5 mensajes exactos para volver a hablarles esta semana.',
  'Reactivación', 'Los consultantes que ya tienes <em>valen más.</em>',
  'Antes de invertir en publicidad, mira tu base: personas que ya confiaron en ti. <b>Los 5 mensajes exactos para volver a hablarles esta semana.</b>',
  'qzioGaxuD_U', 'Los 5 mensajes, uno por uno', 10, 'Quiero los 5 mensajes',
  cuentas('La cuenta', 'El ingreso <em>que ya tienes cerca.</em>', [
      ('Personas que atendiste alguna vez', '100'),
      ('Si vuelve el 15 %', '15'),
      ('Inversión en publicidad', '0 USD'),
  ], ('A 150 USD cada una', '2.250 USD')) +
  ruta('Por qué no volvieron', 'Les faltó <em>una invitación.</em>', [
      ('1', 'Faltó un próximo paso claro', '', 'La consulta terminó bien y nadie dijo qué seguía. La vida hizo el resto.'),
      ('2', 'Volver sin explicar les cuesta', '', 'Para no explicar la ausencia, esperan. Un mensaje tuyo que no la menciona les abre la puerta.'),
      ('3', 'Tu mensaje les da permiso', '', 'Cuando escribes tú primero, sienten alivio: pueden volver sin explicar nada.'),
  ], 'Los 5 mensajes son una secuencia de 10 días, con el texto exacto. Cada uno cumple una función.'),
  'Escríbeles <em>esta semana.</em>', ejemplos=True)

# ── 3 · AUTOMATIZAR ─────────────────────────────────────────────────
pagina('automatizar', 'Un consultorio que funciona aunque tú pares', 'Las horas que van a la gestión, qué herramienta resuelve cada una y en qué orden, en 4 semanas.',
  'Checklist', 'Un consultorio que funciona <em>aunque tú pares.</em>',
  'Las horas que hoy van a confirmar turnos, responder lo mismo y cobrar. <b>Qué herramienta resuelve cada una, y en qué orden, en 4 semanas.</b>',
  'THjdk3TJVek', 'Las 4 semanas, en orden', 12, 'Quiero el checklist',
  ruta('Los 5 procesos', 'Lo que hoy <em>lleva tu tiempo.</em>', [
      ('1', 'Confirmar turnos', '', 'Mensaje por mensaje, todos los días.'),
      ('2', 'Responder consultas nuevas', '', 'Precio, horarios y modalidad: la misma respuesta, muchas veces por semana.'),
      ('3', 'Recordar la consulta', '', 'Con un recordatorio a tiempo, más personas llegan a su turno.'),
      ('4', 'Acompañar después de la consulta', '', 'Con seguimiento, más personas terminan su proceso.'),
      ('5', 'Cobrar', '', 'Pedir, esperar y confirmar cada transferencia.'),
  ], 'Nada de esto necesita tu formación. <b>Necesita un proceso.</b>') +
  ruta('El orden que funciona', 'Semana <em>a semana.</em>', [
      ('1', 'WhatsApp Business', 'Semana 1', 'Mensajes automáticos y respuestas rápidas. Lo primero, y lo más simple.'),
      ('2', 'Tu agenda online', 'Semana 2', 'Cargas tu calendario y compartes el enlace: cada persona elige su horario.'),
      ('3', 'Tu secuencia de seguimiento', 'Semana 3', 'Confirmación, recordatorio y seguimiento después de la consulta, solos.'),
      ('4', 'Palabras clave en Instagram', 'Semana 4', 'Si ya publicas, cada palabra clave abre una conversación sola.'),
  ], 'Sin saber de tecnología: el checklist de los 12 procesos, con la herramienta para cada uno, está en la comunidad.'),
  'Empieza <em>esta semana.</em>')

# ── 4 · PROTOCOLO ───────────────────────────────────────────────────
pagina('creatuprotocolo', 'Vende el resultado', 'Tu consultante quiere el resultado que tus sesiones le dan. Las 3 cosas que tiene un protocolo que se vende.',
  'Protocolo', 'Vende <em>el resultado.</em>',
  'Tu consultante quiere el resultado que tus sesiones le dan. <b>Cuando vendes el resultado, cambia todo, también el precio.</b>',
  '-Ex9XtRZV4g', 'Arma tu protocolo conmigo', 13, 'Crear mi protocolo',
  """
<section class="sec junto">
 <div class="wrap">
  <span class="kick rv">Dos formas de vender lo mismo</span>
  <h2 class="t2 rv">La sesión tiene techo. <em>El resultado, no.</em></h2>
  <div class="modelos rv">
   <div class="modelo antes card"><span>Vendes sesiones</span><b>50 USD</b><p>por sesión suelta: cada semana se decide de nuevo.</p></div>
   <div class="modelo despues card"><span>Vendes un programa</span><b>1.000 USD</b><p>por el resultado completo: la persona se compromete con su proceso.</p></div>
  </div>
 </div>
</section>
""" +
  ruta('Los 3 componentes', 'Un protocolo <em>tiene 3 cosas.</em>', [
      ('1', 'Un resultado concreto', '', '«Recuperar tu energía en 8 semanas», en lugar de «mejorar tu alimentación». Específico y medible.'),
      ('2', 'Un tiempo definido', '', 'Un principio y un final: la persona sabe cuánto dura y qué va a lograr.'),
      ('3', 'Un método con nombre', '', 'Tus sesiones ordenadas en un camino con pasos. Pasa a ser «tu proceso».'),
  ]) +
  ruta('Qué cambia', 'Tres cosas <em>a la vez.</em>', [
      ('A', 'Tu consultante se compromete', '', 'Con un principio, un final y un resultado, la persona se involucra distinto.'),
      ('B', 'Tú planificas mejor', '', 'Sabes cuántas sesiones, en qué orden y hacia dónde.'),
      ('C', 'Cobras por valor', '', 'El precio habla del resultado. Ahí crece tu ticket.'),
  ]),
  'Arma <em>tu protocolo.</em>', ejemplos=True)

# ── 5 · PRECIO (misma página en /modelodenegocio y /guiadeprecios) ─
for slug in ('modelodenegocio', 'guiadeprecios'):
    pagina(slug, 'Un precio sano', 'Lo que sostiene tu precio y los 3 pasos para subirlo con método.',
      'Precio', 'Un precio sano <em>es parte del cuidado.</em>',
      'Un precio sano te deja energía para sostener a quien acompañas. <b>Así se calcula, y así se sube.</b>',
      'wD5V5MAJPO4', 'Tu precio, paso a paso', 11, 'Ver la guía de precios',
      ruta('Lo que sostiene tu precio', 'Tu precio cubre <em>4 cosas.</em>', [
          ('1', 'La hora de sesión', '', 'La única que se ve, y la que casi todos cuentan.'),
          ('2', 'Tu formación', '', 'Años de estudio, cursos y supervisión, presentes en cada decisión.'),
          ('3', 'La gestión invisible', '', 'WhatsApp, notas, coordinación y seguimiento: horas reales.'),
          ('4', 'Tu sostenibilidad', '', 'Descanso, ahorro y futuro, para seguir acompañando por años.'),
      ]) +
      ruta('Los 3 pasos', 'Cómo subir tu precio <em>con método.</em>', [
          ('1', 'Parte del valor', '', 'Del resultado que das, más que del costo de tu hora.'),
          ('2', 'Estrénalo con quien llega', '', 'El precio nuevo arranca con las personas que empiezan desde hoy.'),
          ('3', 'Dilo una vez', '', 'Con calma, y espera la respuesta.'),
      ]),
      'Pon <em>tu precio.</em>')

# ── 6 · CREENCIAS ───────────────────────────────────────────────────
pagina('impostor', 'Es un meme, y se cambia', '«¿Quién soy yo para cobrar esto?» Esa frase se aprende. Los 3 patrones y el primer movimiento para cambiarla.',
  'Creencias', 'Es un meme, <em>y se cambia.</em>',
  '«¿Quién soy yo para cobrar esto?» Esa frase la aprendiste: en la facultad, en los pasillos, en el ambiente. <b>Y lo que se aprende, se cambia.</b>',
  '3JPGgF4cjDw', 'Tu patrón, y cómo cambiarlo', 14, 'Hacer el Neuro-Escáner IA',
  ruta('Los 3 patrones', 'Cuál <em>opera en ti.</em>', [
      ('A', 'Ofreces descuento antes de que te lo pidan', '', 'La persona lee duda donde había valor.'),
      ('B', 'Explicas tu precio con tu currículum', '', 'El precio se presenta con calma. Tu formación ya está en tu trabajo.'),
      ('C', 'Das de más para compensar', '', 'Sumas tiempo y seguimientos sin cobrarlos: más horas por el mismo ingreso.'),
  ], 'El Neuro-Escáner IA identifica cuál pesa más en ti y el primer movimiento para cambiarlo.') +
  ruta('El primer movimiento', 'Tres pasos <em>concretos.</em>', [
      ('1', 'Identifica tu patrón', '', 'Con el Neuro-Escáner IA, sin costo, dentro de la comunidad.'),
      ('2', 'Cobra el precio correcto una vez', '', 'A una persona nueva, al precio que corresponde. Su «sí» te enseña más que cualquier teoría.'),
      ('3', 'Repítelo', '', 'El segundo es más fácil. El décimo, natural.'),
  ]),
  'Identifica <em>tu patrón.</em>')

print('ok')
