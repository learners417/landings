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

Si un paso de GHL tiene otra ruta pero debe mostrar una página existente, va una línea antes:
`<script>window.TCD_PAGINA='el-numero'</script>` (así está `/el-numero-2245`).

## Dónde está cada página en GHL
Ubicación `SImzaMApYvtVV8UzvlgD`. Para abrir un paso:
`app.gohighlevel.com/v2/location/SImzaMApYvtVV8UzvlgD/funnels-websites/funnels/<embudo>/steps/<paso>/overview`

| Embudo | Ruta · paso |
|---|---|
| Lead Magnets CLINICA `k1NEUGyFTYaAoKUtWT7w` | phr `04a1dad1-1aeb-427f-8ce6-0bb9806cdcdb` · generador-caja `8eee0214-ed86-4b1a-b43a-a80eb003fc48` · automatizar `9546be7b-0d30-472a-9e94-e55aa00418d4` · creatuprotocolo `fad23d63-4d3f-4a19-82f7-23badba14bfc` · modelodenegocio `c777a39b-8f8a-4692-9262-5fc6674bb2e5` · guiadeprecios `f431f050-b031-4ca0-b7e5-ce49d658188d` · impostor `1ee2dadf-7755-4b2e-b2aa-96e23b7f9679` |
| Embudo VSL `K6tkjbXeKGJeq5QCdK6e` | recursos-gratuitos `0ce926ec-3813-4aa1-81ec-187cbafbeb66` · app-745191 `0454424a-dc52-4e05-a519-f936bc7e9d21` · generador-pp `ae874638-3a08-41c7-9da6-1661b4e6c75d` (código propio + capa) |
| Subir tus Precios `TFFgX8uSCcOGdx9B6Ssv` | el-numero `38121e9f-773e-47ee-8681-392800566c68` · checkout `85b82fce-6f00-4fec-99da-cf9f34d9f571` (formulario de pedido de GHL) |
| Libros y App `eQrRazCor9k0I4bsqIXc` | libros `1dc9a7d2-b2c8-4315-afd2-4d41dee290bd` · el-numero-2245 `fd8a7ed6-c15b-4f52-b5d7-7ab9d1239439` · gracias `888ce415-3d95-4d84-af14-5c1cff8aee51` · inicio `d41fdeaf-2684-4895-b89b-583bd81cf7a1` · app `f1facb03-a0a0-42bf-8dd0-28847c3e9090` · capitulos `5385d83c-8773-4e91-8d3e-65c93e484114` · capitulo-sanadores `7aa1a856-17e6-4a3e-959a-dcab08e6ec97` · capitulo-lago `ac8818b5-79cd-4ba1-bc48-f781e3ac69a4` · capitulo-montana `fca7d210-af67-4430-b149-f513c3ea3e82` · capitulo-viento `61fb8092-c937-48f4-9850-25c17776910d` · capitulo-rio `dbfb2896-64d9-44cc-bb89-67c89a7b051e` · capitulo-bosque `3a3c0b4a-d278-4811-85e4-3ef22667df43` · capitulo-heroe `449ae758-1222-4e0a-a7f0-06be9759af7c` · capitulo-libertades `c66fe98d-d68f-42d5-a0b7-fb2f459c262d` · lo-que-el-sur-te-ensena `232ab4b0-9cad-47ad-923f-7275dc5e6e6b` · heroe-descapado `35b9c5d3-e9ea-453f-98ca-c3b73f7d7a83` · materias-pendientes `fdae5089-6820-49f8-be33-f12f40642dc2` · intangibles `adf1be94-f4fe-4e1d-ac97-7c50c6726fcd` · clinica-del-lider `804f0033-9f85-446e-a72f-81b481c7f4c9` |

## Qué hay en cada carpeta
- `pages/` · las páginas · `src/` · base.css, base.js, config.js · `imgs/` · tapas e imágenes (van dentro de cada página)
- `fijas/` · agenda, preparación y la capa del generador (`/generador-pp` conserva su código; la capa va debajo)
- `tools.py` · arma las 6 páginas de herramientas · `port_capitulos.py` · arma los capítulos
- `cargador.js` y `ghl-linea.html` · cómo llegan las páginas a GHL
- `panel.py` · el panel de montaje manual (respaldo) · `site/` · lo que sirve el cargador (no se edita a mano)
- `ghl/retirado/` · copias de parches que vivían en el código de seguimiento de un embudo y ya pasaron a las páginas
  (el de Libros y App v3.2 salió de GHL el 6 nov 2026; los cambios de página se hacen aquí, no con parches)

## Reglas del estándar
Letra de 16 px o más · papel, sin fondo negro, sin degradés ni brillos · oro solo en líneas de 1 px,
versalitas y numerales · castellano neutro, tuteo · nunca «gente» ni «gratis» · sin señales de falta de
dinero · datos con su fuente · sin emojis.
