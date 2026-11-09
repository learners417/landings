# Correos nuevos · versión definitiva (9 nov 2026)

Dos flujos de GHL que faltaban. Remitente: Javo Katz, `javo@notificaciones.tuclinica.digital`.
Los links llevan `?lector=1` (abre el capítulo sin volver a pedir el correo) y
`utm_source=correo&utm_medium=email&utm_campaign=<flujo>&utm_content=<correo>`.

**El link de cada herramienta** es `https://tuclinica.digital/herramienta?h=<ruta>`: una página corta que
lleva adonde está la herramienta hoy (la comunidad) y, cuando pase a GHL, a su página nueva. Así los
correos no se tocan el día del cambio. Sale de `config.js` (`herramientas`).

**Después del correo de entrega**, al día siguiente, el contacto sigue en «Lectores · 10 días» desde el
correo 2 (no recibe el 1, que dice «Tu capítulo está abierto»).

El P. D. dice la línea de Tu nuevo precio de hoy («Los 8 libros y los cinco primeros días de mi app»): es verdad antes y después del 27 nov, así que no hay que tocarlo ese día.

## En GHL (9 nov 2026)

Cargados los 12 correos, en dos flujos nuevos, **en borrador** (Javo los publica con un clic):

- **«Herramientas · entrega»** (`3951ed6a-a246-486c-a267-692d5fa7693c`): formulario «Herramientas · para empezar» →
  Si/Si no por el campo «Herramienta» (phr, guiadeprecios, impostor, generador-caja, creatuprotocolo, automatizar,
  recursos) → un correo por rama. El flujo «Herramientas · etiqueta» (publicado) sigue poniendo las etiquetas.
- **«Lista de espera · primer correo»** (`7a8f9c51-594e-4d50-ac4e-7ddfe987fc93`): formulario «Lista de espera» →
  etiqueta `lista-espera` → Si/Si no por el campo «Lista de espera» (clinica-del-lider, materias-pendientes, intangibles,
  mastermind, heroe-descapado) → etiqueta `lista-<lista>` + su correo.

Remitente Javo Katz, `javo@notificaciones.tuclinica.digital`. Asunto y vista previa como arriba; el cuerpo es el HTML de
`ghl/correos/html/h-<ruta>.html` y `e-<lista>.html` (GHL lo pasa a su letra del editor al guardar).
El paso «seguir en Lectores · 10 días desde el correo 2» se agrega el 27 nov, cuando «Lectores · 10 días» se publica
(un flujo en borrador no recibe contactos).

---

## Herramientas · entrega (un correo por herramienta, al instante)

Lo dispara el formulario «Herramientas · para empezar» (`0RGhK8342PTwkXk0MsCa`). Rama por el campo
`contact.herramienta`.

### phr · Tu hora real
Asunto: Tu hora real
Vista previa: Tres números y dos minutos.

Hola {{contact.first_name}}:

Aquí está tu herramienta: la calculadora de tu hora real.

→ Abrir la calculadora — /herramienta?h=phr

Ten a mano tres números: lo que cobraste el mes pasado, tus gastos fijos y todas las horas que le diste a tu consulta, también las de WhatsApp.

En el ejemplo de la página, 5.000 USD al mes y 55 horas por semana dan 17 USD por hora. Haz la tuya: ese número dice más de tu modelo que de tu esfuerzo.

Esta herramienta es parte del lago, la primera estación del camino. Si quieres ir más hondo, lee el primer capítulo de *Lo que el lago te enseña*: termina en tu precio nuevo.

→ Leer el primer capítulo — /capitulo-lago?lector=1 (7 minutos)

Javo

P. D. Si quieres empezar ya: Tu nuevo precio. Los 8 libros y los cinco primeros días de mi app. 97 USD. Verlo — /libros#obra

### guiadeprecios · Un precio sano
Asunto: Tu guía de precios
Vista previa: Lo que sostiene tu precio, y cómo se sube.

Hola {{contact.first_name}}:

Aquí está tu herramienta: la guía de precios por especialidad.

→ Abrir la guía — /herramienta?h=guiadeprecios

Tu precio cubre cuatro cosas: la hora de sesión, tu formación, la gestión invisible y tu sostenibilidad. La primera es la que se ve. Las otras tres también son trabajo.

Para subirlo, tres pasos: parte del valor que das, estrénalo con quien llega desde hoy y dilo una vez, con calma. Después, espera la respuesta.

Esta herramienta es parte del lago, la primera estación del camino. Su libro termina en un número: tu precio nuevo.

→ Leer el primer capítulo de *Lo que el lago te enseña* — /capitulo-lago?lector=1 (7 minutos)

Javo

P. D. Si quieres empezar ya: Tu nuevo precio. Los 8 libros y los cinco primeros días de mi app. 97 USD. Verlo — /libros#obra

### impostor · Es un meme, y se cambia
Asunto: Tu patrón con el precio
Vista previa: «¿Quién soy yo para cobrar esto?» se aprende. Y se cambia.

Hola {{contact.first_name}}:

Aquí está tu herramienta: el Neuro-Escáner IA.

→ Hacer el Neuro-Escáner — /herramienta?h=impostor

Te muestra cuál de tres patrones pesa más en ti: el descuento que ofreces antes de que te lo pidan, el precio que explicas con tu currículum o lo que das de más para compensar.

Después, un solo movimiento: cobrarle el precio correcto a una persona nueva, una vez. Su «sí» te enseña más que cualquier teoría.

Esta herramienta es parte del lago, la primera estación del camino.

→ Leer el primer capítulo de *Lo que el lago te enseña* — /capitulo-lago?lector=1 (7 minutos)

Javo

P. D. Si quieres empezar ya: Tu nuevo precio. Los 8 libros y los cinco primeros días de mi app. 97 USD. Verlo — /libros#obra

### generador-caja · Los consultantes que ya tienes
Asunto: Los 5 mensajes
Vista previa: Para las personas que ya confiaron en ti.

Hola {{contact.first_name}}:

Aquí están los 5 mensajes de reactivación: una secuencia de diez días, con el texto exacto.

→ Abrir los 5 mensajes — /herramienta?h=generador-caja

Antes de invertir en publicidad, mira tu base. En el ejemplo de la página, si de cien personas que atendiste vuelven quince, a 150 USD cada una son 2.250 USD, sin invertir en publicidad.

Escribe el primero hoy. Les faltaba una invitación, y la tuya les da permiso para volver sin explicar nada.

Esta herramienta es parte de la montaña, la estación donde armas tu programa.

→ Leer el primer capítulo de *Lo que la montaña te enseña* — /capitulo-montana?lector=1 (7 minutos)

Javo

P. D. Si quieres empezar ya: Tu nuevo precio. Los 8 libros y los cinco primeros días de mi app. 97 USD. Verlo — /libros#obra

### creatuprotocolo · Vende el resultado
Asunto: Tu protocolo
Vista previa: La sesión tiene techo. El resultado, no.

Hola {{contact.first_name}}:

Aquí está tu herramienta: la plantilla de tu protocolo, paso a paso.

→ Abrir la plantilla — /herramienta?h=creatuprotocolo

Un protocolo tiene tres cosas: un resultado concreto, un tiempo definido y un método con nombre.

Escribe hoy la primera: lo que logra una persona contigo, en una frase y con un número. «Recuperar tu energía en 8 semanas» se entiende, y se compra.

Esta herramienta es parte de la montaña, la estación donde armas tu programa.

→ Leer el primer capítulo de *Lo que la montaña te enseña* — /capitulo-montana?lector=1 (7 minutos)

Javo

P. D. Si quieres empezar ya: Tu nuevo precio. Los 8 libros y los cinco primeros días de mi app. 97 USD. Verlo — /libros#obra

### automatizar · Un consultorio que funciona aunque tú pares
Asunto: Tu checklist de 12 procesos
Vista previa: Una herramienta por semana, en orden.

Hola {{contact.first_name}}:

Aquí está tu herramienta: el checklist de los 12 procesos de tu semana, con la herramienta para cada uno.

→ Abrir el checklist — /herramienta?h=automatizar

Empieza por lo más simple: WhatsApp Business, con mensajes automáticos y respuestas rápidas. Es la semana 1. Las otras tres, en orden: tu agenda online, tu secuencia de seguimiento y las palabras clave en Instagram.

Nada de esto necesita tu formación. Necesita un proceso.

Esta herramienta es parte del río, la estación donde todo empieza a correr solo.

→ Leer el primer capítulo de *Lo que el río te enseña* — /capitulo-rio?lector=1 (8 minutos)

Javo

P. D. Si quieres empezar ya: Tu nuevo precio. Los 8 libros y los cinco primeros días de mi app. 97 USD. Verlo — /libros#obra

### recursos · La comunidad
Asunto: Ya estás adentro
Vista previa: Los jueves a las 19:00, en vivo.

Hola {{contact.first_name}}:

Ya puedes entrar a la comunidad: las seis herramientas, el aula y el vivo de los jueves a las 19:00 (hora de Argentina), donde traes tu caso y te vas con un plan.

→ Entrar a la comunidad — /herramienta?h=recursos

Si no sabes por dónde empezar, empieza por tu hora real. Son dos minutos.

Javo

---

## Lista de espera · primer correo (al instante)

Lo dispara el formulario «Lista de espera» (`YX3xdi92MbG4VuM15vPk`). Rama por `contact.lista_de_espera`: clinica-del-lider, materias-pendientes, intangibles, mastermind y heroe-descapado (la trilogía, desde el 9 nov).
Etiqueta `lista-espera` y `lista-<lista>`. Al día siguiente sigue en «Lectores · 10 días» desde el correo 2.

### clinica-del-lider
Asunto: Estás en la lista
Vista previa: La Clínica del Líder abre en 2027.

Hola {{contact.first_name}}:

Ya estás en la lista de espera de La Clínica del Líder. Abre en 2027, y te escribo a ti primero.

Mientras tanto, empieza por el libro que la sostiene: *Héroe descapado*. La apertura se lee aquí mismo, sin costo.

→ Leer la apertura — /capitulo-heroe?lector=1 (9 minutos)

Javo

### materias-pendientes
Asunto: Estás en la lista
Vista previa: Lo que la escuela no te enseñó a propósito.

Hola {{contact.first_name}}:

Ya estás en la lista de Materias pendientes: siete materias, un libro por materia, una habilidad por libro. Te escribo el día que sale el primero.

Mientras tanto, empieza por el libro que las junta: *Las 7 libertades fundamentales*.

→ Leer el primer capítulo — /capitulo-libertades?lector=1 (5 minutos)

Javo

### intangibles
Asunto: Estás en la lista
Vista previa: Lo que no se toca, pero te toca.

Hola {{contact.first_name}}:

Ya estás en la lista de Intangibles: un gran maestro por libro, llevado a tu vida y a tu negocio. Te escribo el día que sale el primero.

Mientras tanto, empieza por *Las 7 libertades fundamentales*: es mi filosofía completa, en un libro.

→ Leer el primer capítulo — /capitulo-libertades?lector=1 (5 minutos)

Javo

### mastermind
Asunto: Estás en la lista
Vista previa: Se llega recorriendo el camino.

Hola {{contact.first_name}}:

Ya estás en la lista del mastermind. Se entra por invitación, y se llega recorriendo el camino.

El primer paso es Tu nuevo precio: los 8 libros y los cinco primeros días de mi app, donde sellas tu precio nuevo.

→ Ver Tu nuevo precio — /libros#obra

Javo

### heroe-descapado
Asunto: Estás en la lista
Vista previa: La trilogía de El Eje, en preparación.

Hola {{contact.first_name}}:

Ya estás en la lista de la trilogía *Héroe descapado*: *La capa*, *El camino* y *Liderarte*. Te escribo el día que sale el primer tomo.

Mientras tanto, el libro ya está. La apertura se lee aquí mismo, sin costo.

→ Leer la apertura — /capitulo-heroe?lector=1 (9 minutos)

Javo
