/* ════════════════════════════════════════════════════════════════
   TODO LO QUE SE CAMBIA, VIVE AQUÍ. Es el mismo bloque en todas las páginas.
   Si cambias un link o un precio, cámbialo igual en las 7 páginas.
   Si un link de pago está vacío, el botón abre tu WhatsApp con el producto escrito.
   ════════════════════════════════════════════════════════════════ */
window.TCD = {

  /* Las páginas del ecosistema, en GHL (tuclinica.digital). */
  inicio:      '/inicio',
  agenda:      '/instala-tu-clinica',
  preparacion: '/preparacion',
  libros:      '/libros',
  numero:      '/el-numero',
  appPagina:   '/libros',   // /app se retiró el 8 nov 2026: la app viene dentro de Tu nuevo precio
  gracias:     '/gracias',
  recursos:    '/recursos-gratuitos',
  generador:   '/generador-pp',
  camino:      '/camino',        // el Mapa del viaje para el lector (8 nov 2026)
  laCima:      '/la-cima',       // 4 días en Bariloche, 17 al 20 dic; se postula agendando
  mastermind:  '/mastermind',    // por invitación
  prensa:      '/prensa',
  appMedida:   '/app-745191',

  /* Los primeros capítulos, también en GHL. */
  capitulo:  '/capitulos',     // el índice: «¿Por cuál libro empiezas?»
  cap:       '/capitulo-',     // + lago, montana, viento, rio, bosque, sanadores, heroe o libertades

  /* Las colecciones. */
  sur:       '/lo-que-el-sur-te-ensena',
  heroe:     '/heroe-descapado',
  materias:  '/materias-pendientes',
  intangibles: '/intangibles',
  cdl:       '/clinica-del-lider',

  /* Los libros NO se pegan aquí: este código es público y cualquiera vería los links.
     Los manda el correo de entrega de GHL apenas entra el pago de Tu nuevo precio.
     Cuando ese correo ande, librosPorCorreo pasa a true y /gracias dice «te llegan por correo».
     Mientras tanto, cada botón de descarga abre tu WhatsApp para que se lo mandes tú. */
  librosPorCorreo: false,

  /* La puerta de los primeros capítulos: el id del formulario de GHL «Lectores · primer capítulo».
     Con el id puesto, cada capítulo pide nombre y correo antes de leer y arranca el flujo «Lectores · 10 días».
     Vacío: los capítulos se leen sin pedir nada. */
  formLectores: '',

  /* La lista de espera (las colecciones que vienen y La Clínica del Líder, que abre en 2027):
     el id del formulario de GHL «Lista de espera». Vacío: el botón abre tu WhatsApp con la lista escrita. */
  formEspera: '',

  /* La línea única de Tu nuevo precio: la misma en todas las páginas (cada [data-linea97] la toma de aquí).
     El 27 nov, con los audios de la primera tanda, pasa a:
     'Los 8 libros, los cinco primeros días de mi app y cinco mañanas con mi voz.' */
  linea97: 'Los 8 libros y los cinco primeros días de mi app.',
  descargas: {
    'Sanadores-Libres-Javo-Katz.pdf':              '',
    'Lo-que-el-lago-te-ensena-Javo-Katz.pdf':      '',
    'Lo-que-la-montana-te-ensena-Javo-Katz.pdf':   '',
    'Lo-que-el-viento-te-ensena-Javo-Katz.pdf':    '',
    'Lo-que-el-rio-te-ensena-Javo-Katz.pdf':       '',
    'Lo-que-el-bosque-te-ensena-Javo-Katz.pdf':    '',
    'Heroe-descapado-Javo-Katz.pdf':               '',
    'Las-7-libertades-fundamentales-Javo-Katz.pdf':'',
    'Los-8-libros-Javo-Katz.zip':                  ''
  },
  img:       '',

  /* Los links de pago de GHL (Pagos → Links de pago), entre las comillas. */
  pagos: {
    numero:     '',   // El Número · retirada el 6 nov 2026: su página lleva a /libros
    obra:       'https://link.fastpaydirect.com/payment-link/6aee2c6118be8d04a49be0b0',   // Tu nuevo precio · los 8 libros + 5 días en la app · 97 · se enciende con librosPorCorreo (ver al final)
    verde:      '',   // La app · Tu Sistema · 497
    negro:      '',   // La app · El Programa Completo · 997
    sanadores:  '',   // Sanadores Libres · 33
    lago:       '',   // Lo que el lago te enseña · 27
    montana:    '',   // Lo que la montaña te enseña · 27
    viento:     '',   // Lo que el viento te enseña · 27
    rio:        '',   // Lo que el río te enseña · 27
    bosque:     '',   // Lo que el bosque te enseña · 27
    heroe:      '',   // Héroe descapado · 47
    libertades: '',   // Las 7 libertades fundamentales · 37
    apaga:      '',   // La Clínica del Líder · Apaga la cabeza · 33
    ejeSolo:    '',   // La Clínica del Líder · El Eje Solo · 333
    ejeAcomp:   ''    // La Clínica del Líder · El Eje Acompañado · 999
  },

  /* Los precios, en dólares. */
  precios: {
    numero: 27, obra: 97, verde: 497, negro: 997,
    sanadores: 33, lago: 27, montana: 27, viento: 27, rio: 27, bosque: 27,
    heroe: 47, libertades: 37,
    apaga: 33, ejeSolo: 333, ejeAcomp: 999
  },

  /* Tu WhatsApp, solo números, con código de país. */
  whatsapp: '5492944217689',

  comunidad: 'https://www.skool.com/aprendedores-4619/about?ref=465a1ed1cf944d65a86766f0cd39eba2',
  app:       'https://app.tuclinica.digital',
  instagram: 'https://www.instagram.com/javieremilianok/',
  foto:      'https://assets.cdn.filesafe.space/SImzaMApYvtVV8UzvlgD/media/69da9fb1b30bc52371f82e69.jpeg',
  pixel:     '1306012398373458',
  /* Clarity (Microsoft): grabaciones y mapas de calor. Si GHL ya lo cargó en la página, no se carga dos veces. */
  clarity:   'z9r79a8723',
  /* Los testimonios: v = video tuyo (filesafe), y = YouTube. Se muestran en este orden. */
  media: 'https://assets.cdn.filesafe.space/SImzaMApYvtVV8UzvlgD/media/',
  testimonios: [['v','6ac4236b195f9172ed95c91c'],['v','6ad260a5f9a985d42cbe18a8'],['y','U7ablyCr2_Y'],['v','6abc83aa6c64b8e488a2f025'],['v','6ab9e5fa5597aeb9d7f13c31'],['y','FjW8chAxRPk'],['v','6ab9b6e65597aeb9d7eca5b7'],['v','6ab9ba4abe703c7b30305435'],['y','cdcGh-oIV9Y'],['v','6aa0b1e2fb76acb4a93c0ffd'],['v','6ab9e143b4d207ff9d0c5bc7'],['y','0q4Ah_PL_1w'],['v','6ab9e2aac13d4373c2d28d8a'],['v','6ab9df5c5597aeb9d7f0b331'],['y','siIRcFF_Fzc'],['v','6aa0b40116ed327815b69e1a'],['v','6ad263a2fdbcf67570a0b065'],['y','8yGijdiMzJE'],['v','6ad2646686f4a10b2fa62ae0'],['v','6ab9dcba5597aeb9d7f076da'],['y','syL0QvfQHJ4'],['v','6ab9d97f5597aeb9d7f02cd7'],['v','6abaf9f3c13d4373c2ef5b47'],['y','ZYdiTIIDl6g'],['v','6abaf9a37ef452865a2fd7b4'],['v','6abb018672844d8ecf2e9e54'],['v','689fb4467bb59edaff12c342'],['v','689fb4467bb59e069512c341'],['v','689fb44669618cd2effbd32b'],['v','6ad263a41de0b9886006376a']],
  /* Fotos de eventos y rodajes, y capturas de mensajes de clientes. */
  fotos: ['6a3f2d42d50c4ff184edb838.jpeg','6a7e0125c0662ee5c46bb552.jpg','693dba4697c0236220e081ea.jpg','6a3f2d42e2763b2eec24a60c.jpeg','6a7d3d929115899f03677541.png','6a7e00e4494aefa6d8297657.jpg','67a95b7bfc7685e4ad16a204.png','67a8027f9769a75cfe604f9b.png','67a8027f9769a71ac3604f9c.png','67a8027ffc768597de1360da.png','67a8027f4325e15ee6581091.png','67a8027f4325e17938581092.png','67a8027f8f9e7e4c006b47f6.png'],
  capturas: ['6a3f2d4ae2763b2eec24a678.jpeg','6790e3b22aa71a8f8b682154.jpeg','67a8080cfc76856ca1136421.jpeg']
};

/* Tu nuevo precio se cobra con su link solo cuando el correo de entrega anda: la página de pago promete
   «los libros te llegan por correo». Mientras librosPorCorreo sea false, el botón de 97 abre tu WhatsApp.
   El día que pase a true, cambian juntos el botón (PayPal) y /gracias (los libros llegan por correo). */
if (!window.TCD.librosPorCorreo) window.TCD.pagos.obra = '';
