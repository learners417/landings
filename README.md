# Las landings de Javo Katz · Tu Clínica Digital

Aquí se guarda y se arma el código de las páginas. Las páginas viven en GHL (tuclinica.digital/ruta),
con sus calendarios, formularios, estadísticas y automatizaciones.

## Cómo llega cada página a GHL
Cada página de GHL tiene un solo bloque «Código personalizado» con una línea: `ghl-linea.html`.
Es la misma línea en todas. Esa línea trae `cargador.js`, y el cargador trae `site/<ruta>.html`
(la ruta de GHL decide el archivo: `/impostor` → `site/impostor.html`) y la monta dentro de la
página de GHL. GHL sigue haciendo lo suyo por detrás: estadísticas del embudo, atribución,
formularios y calendarios.

- Fuente principal: jsDelivr (`cdn.jsdelivr.net/gh/learners417/landings@main/...`). Respaldo: GitHub.
- La página se ve igual que sola: el cargador apaga los estilos de GHL y corre los scripts en orden.
- El píxel de TCD recibe sus eventos solo (`trackSingle`), aunque GHL tenga otro píxel en la página.

## Cómo se corrige y se sube
1. Se edita la fuente: `pages/*.html` (las páginas), `src/` (la piel común y `config.js`:
   rutas, precios, links de pago, WhatsApp, píxel), `fijas/` (la agenda y la preparación).
2. Se arma: `python3 build.py && python3 publicar.py` (de `pages/` a `dist/`, y todo a `site/`).
3. Se revisa: `python3 chico.py 390 dist/*.html` (errores y letra menor a 16 px).
4. Push a `main` y se purga jsDelivr de cada archivo que cambió:
   `https://purge.jsdelivr.net/gh/learners417/landings@main/site/<ruta>.html`.
   En un minuto está en vivo. GHL no se toca.

## Una página nueva
1. `pages/<ruta>.html` → armar → push → purga.
2. En GHL: se clona un paso que ya tenga la línea y se le pone la ruta exacta. Título y descripción
   en la configuración SEO del paso (es lo que muestran WhatsApp y Facebook al compartir).

Las meditaciones van con barra: `pages/libro-<x>.html` sale en `site/libro/<x>.html` y GHL la sirve en `/libro/<x>`.
Una misma página con dos rutas: `TAMBIEN` en publicar.py (recursos.html sale como /recursos-gratuitos y /para-empezar).

La lista de espera: formulario de GHL «Lista de espera» `YX3xdi92MbG4VuM15vPk` (nombre, correo y el campo oculto
`contact.lista_de_espera`, clave de consulta `lista`). Cada botón `data-espera="<lista>"` lo abre con su lista puesta.

La puerta de las seis herramientas (8 nov 2026): formulario de GHL «Herramientas · para empezar» `0RGhK8342PTwkXk0MsCa`
(nombre, correo y el campo oculto `contact.herramienta`, clave de consulta `herramienta`, con contacto fijo).
En /phr, /guiadeprecios, /impostor, /creatuprotocolo, /generador-caja y /automatizar, cada botón a la comunidad lo abre
con la ruta de la página puesta y, al enviarlo, lleva a Skool (y su mensaje de «Listo» trae el link a la comunidad).
Quien ya dejó su correo en ese navegador entra directo. En GHL, el flujo publicado «Herramientas · etiqueta» suma
`herramientas`, `carta-semanal` y `herramienta-<ruta>` (etiqueta dinámica con el campo). No entra a «Lectores · 10 días»:
su correo 1 dice «Tu capítulo está abierto».

Los tres formularios (herramientas, lista de espera y la puerta de los capítulos) van en un iframe simple, sin
`form_embed.js`: ese script los escondía desde la segunda visita. La dirección lleva el dato oculto y las UTM de la página.
El envío se detecta con el mensaje `set-sticky-contacts` de GHL; por eso el formulario de las herramientas y el de la
puerta de los capítulos (`s3o93G3fWK3VrO6Gin1n`) tienen «Contacto fijo» encendido. Sin probar todavía con un envío real.

Si un paso de GHL tiene otra ruta pero debe mostrar una página existente, va una línea antes:
`<script>window.TCD_PAGINA='el-numero'</script>` (así está `/el-numero-2245`).

## La agenda (/instala-tu-clinica) es la excepción
No usa la línea: su bloque de GHL tiene `fijas/agenda.html` entera (la página de la campaña carga más rápido así).
Para cambiarla: se edita `fijas/agenda.html`, se sube, y el mismo cambio se escribe en el editor del bloque en GHL
(Guardar → guardar la página → Publicar). Después se compara lo publicado con el repo: tienen que ser iguales byte a byte.
En GHL, guardar no publica: hasta tocar «Publicar», en vivo sigue la versión anterior.

## Dónde está cada página en GHL
Ubicación `SImzaMApYvtVV8UzvlgD`. Para abrir un paso:
`app.gohighlevel.com/v2/location/SImzaMApYvtVV8UzvlgD/funnels-websites/funnels/<embudo>/steps/<paso>/overview`

| Embudo | Ruta · paso |
|---|---|
| Lead Magnets CLINICA `k1NEUGyFTYaAoKUtWT7w` | phr `04a1dad1-1aeb-427f-8ce6-0bb9806cdcdb` · generador-caja `8eee0214-ed86-4b1a-b43a-a80eb003fc48` · automatizar `9546be7b-0d30-472a-9e94-e55aa00418d4` · creatuprotocolo `fad23d63-4d3f-4a19-82f7-23badba14bfc` · modelodenegocio `c777a39b-8f8a-4692-9262-5fc6674bb2e5` · guiadeprecios `f431f050-b031-4ca0-b7e5-ce49d658188d` · impostor `1ee2dadf-7755-4b2e-b2aa-96e23b7f9679` · herramienta `0ee9b0fe-6c4f-432e-8ca8-f251f5ff4f57` (9 nov, clon de phr: el link de los correos) |
| Embudo VSL `K6tkjbXeKGJeq5QCdK6e` | recursos-gratuitos `0ce926ec-3813-4aa1-81ec-187cbafbeb66` · app-745191 `0454424a-dc52-4e05-a519-f936bc7e9d21` · generador-pp `ae874638-3a08-41c7-9da6-1661b4e6c75d` (código propio + capa) · portada `/` paso home `107804f6-095f-468c-ad18-4d38adf02847` (la línea con `TCD_PAGINA='inicio'`, desde el 8 nov 2026) · instala-tu-clinica paso «VSL HIGH» `fcb49aa2-5ffa-4d64-8d7a-f02774e4461d` (nativa: `fijas/agenda.html` entera en el bloque) |
| Subir tus Precios `TFFgX8uSCcOGdx9B6Ssv` | el-numero `38121e9f-773e-47ee-8681-392800566c68` · checkout `85b82fce-6f00-4fec-99da-cf9f34d9f571` (formulario de pedido de GHL) |
| Libros y App `eQrRazCor9k0I4bsqIXc` | libros `1dc9a7d2-b2c8-4315-afd2-4d41dee290bd` · el-numero-2245 `fd8a7ed6-c15b-4f52-b5d7-7ab9d1239439` · gracias `888ce415-3d95-4d84-af14-5c1cff8aee51` · inicio `d41fdeaf-2684-4895-b89b-583bd81cf7a1` · app `f1facb03-a0a0-42bf-8dd0-28847c3e9090` · capitulos `5385d83c-8773-4e91-8d3e-65c93e484114` · capitulo-sanadores `7aa1a856-17e6-4a3e-959a-dcab08e6ec97` · capitulo-lago `ac8818b5-79cd-4ba1-bc48-f781e3ac69a4` · capitulo-montana `fca7d210-af67-4430-b149-f513c3ea3e82` · capitulo-viento `61fb8092-c937-48f4-9850-25c17776910d` · capitulo-rio `dbfb2896-64d9-44cc-bb89-67c89a7b051e` · capitulo-bosque `3a3c0b4a-d278-4811-85e4-3ef22667df43` · capitulo-heroe `449ae758-1222-4e0a-a7f0-06be9759af7c` · capitulo-libertades `c66fe98d-d68f-42d5-a0b7-fb2f459c262d` · lo-que-el-sur-te-ensena `232ab4b0-9cad-47ad-923f-7275dc5e6e6b` · heroe-descapado `35b9c5d3-e9ea-453f-98ca-c3b73f7d7a83` · materias-pendientes `fdae5089-6820-49f8-be33-f12f40642dc2` · intangibles `adf1be94-f4fe-4e1d-ac97-7c50c6726fcd` · clinica-del-lider `804f0033-9f85-446e-a72f-81b481c7f4c9` · camino `e06b0cea-5cd5-4735-903d-2f12e471f77a` · la-cima `5262a570-a55f-4bef-85be-b0846372f121` · mastermind `f08c3674-289f-4822-a709-19617dfd0db7` · para-empezar `784dfbaf-ce61-4aae-b5b6-b219813942d3` · prensa `e520afcd-a93e-409a-974f-20c1a9cc784d` · libro/umbral `e0362c99-4d2a-4cb5-900c-1667028486e5` · libro/audio `e404337b-2c3e-4e60-ab78-5986373bc84c` · libro/lago `c9dbf653-2700-4456-b77b-ee89d8a24f16` · libro/montana `a23de7c3-b40f-415c-91c7-61a173d9d1e9` · libro/viento `312900be-c7bc-4ebd-b3f2-c1bd4c07104a` · libro/rio `7dd0a5b0-557c-4c98-b109-b9cf1d37b9c7` · libro/bosque `7fc58030-4d68-4178-bf53-bce1eeee1674` (los 12 del 8 nov 2026) |

## Qué hay en cada carpeta
- `pages/` · las páginas · `src/` · base.css, base.js, config.js · `imgs/` · tapas e imágenes (van dentro de cada página)
- `fijas/` · agenda, preparación y la capa del generador (`/generador-pp` conserva su código; la capa va debajo)
- `tools.py` · arma las 6 páginas de herramientas · `port_capitulos.py` · arma los capítulos
- `cargador.js` y `ghl-linea.html` · cómo llegan las páginas a GHL
- `panel.py` · el panel de montaje manual (respaldo) · `site/` · lo que sirve el cargador (no se edita a mano)
- `ghl/retirado/` · copias de parches que vivían en el código de seguimiento de un embudo y ya pasaron a las páginas
  (el de Libros y App v3.2 salió de GHL el 6 nov 2026; los cambios de página se hacen aquí, no con parches)

## La Edición Libres (9 nov 2026, aprobada y en vivo)
Cada página es un libro de la colección: portadilla, índice, capítulos y colofón. Las páginas nuevas piden
`<style>/*EDICION_CSS*/</style>` y `<script>/*EDICION_JS*/</script>` (build.py pone `src/edicion.css`, `config.js`,
`clarity.js`, `base.js` y `src/edicion.js`). Desde el 9 nov **todas** las páginas están en la Edición, menos `/gracias`
(lógica del otro chat, sigue con `/*BASE_CSS*/` y el puente de `base.css`). Detalle del diseño: `EDICION.md`.
- La fuente de cada página es su archivo en `pages/`: todo cambio se hace ahí, a mano, y después se arma. Los generadores
  de la migración (`camino_ed.py`, `sur_ed.py`, `cdl_ed.py`, `proximos_ed.py`, `medita_ed.py`) vivían fuera del repo y
  quedaron atrás de `pages/` desde el 9 nov (las estaciones 1-7 · 8-14 · 15-35 · 36-84 · 85-90 se corrigieron en `pages/`):
  no se vuelven a correr.
- `/el-numero`, `/app` y `/app-745191` son redirecciones (El Número y la app suelta se retiraron: llevan a Tu nuevo precio).
- El precio en los botones (`… · <span data-precio>97</span> USD`): build.py lo envuelve en `.pr` para que en el celular
  baje entero a su propia línea («Quiero Tu nuevo precio» / «97 USD»).
- El estante de los 8 libros es uno solo: `src/estante.html`, puesto donde la página dice `<!--ESTANTE-->`.
- Las 6 herramientas salen de `tools.py` (con su palabra, su estación y su libro): `python3 tools.py` y después armar.
- Vista previa antes de publicar: subir a la rama `edicion` y abrir `tuclinica.digital/<ruta>?rama=edicion`
  (el cargador trae esa rama; sin píxel ni Clarity). Purgar `@edicion` en jsDelivr como `@main`.
- Los correos de entrega de las herramientas y de la lista de espera: `ghl/correos/herramientas-y-espera.md`.
  Su link es `/herramienta?h=<ruta>` (`pages/herramienta.html` + `TCD.herramientas` en config.js), con su paso en GHL desde el 9 nov.
  Los 12 correos están en GHL, en dos flujos publicados el 9 nov: «Herramientas · entrega» y «Lista de espera · primer correo».
- Tu nuevo precio (97) cobra solo desde el 9 nov (`librosPorCorreo: true`): el link de pago de GHL lleva a
  `/gracias?c=obra` y el flujo «Tu nuevo precio · entrega» (`327dd697-6e63-4f5a-8df4-0823faf7ffbc`, clon de «Acceso
  inmediato a app») hace: «Pago recibido» del producto Tu Precio Nuevo → alta en la app (el mismo webhook de El Número)
  → correo «Tus 8 libros» (`ghl/correos/html/obra-entrega.html`) → aviso a Javo → etiqueta `compro-97`.
  Los libros están en una carpeta de Drive de Javo compartida por link; ese link vive solo en el correo de GHL,
  nunca en este repo (es público). Para una edición nueva, se reemplaza el PDF dentro de esa carpeta.

## Reglas del estándar
Letra de 16 px o más · papel, sin fondo negro, sin degradés ni brillos · oro solo en líneas de 1 px,
versalitas y numerales · Cormorant Garamond titula y Literata se lee · sin flechas en los botones · castellano neutro, tuteo · nunca «gente» ni «gratis» · sin señales de falta de
dinero · datos con su fuente · sin emojis.
