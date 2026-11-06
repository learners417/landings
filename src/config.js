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
  appPagina:   '/app',
  gracias:     '/gracias',
  recursos:    '/recursos-gratuitos',
  generador:   '/generador-pp',
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

  /* Los libros para descargar: súbelos a GHL (Sitios → Medios) y pega aquí el link de cada uno.
     Si un link está vacío, el botón abre tu WhatsApp para que se lo mandes tú. */
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
    numero:     '/checkout',   // El Número · 27 · el checkout de GHL (embudo Subir tus Precios)
    obra:       '',   // El Número + los 8 libros · 97
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
  /* Los testimonios: v = video tuyo (filesafe), y = YouTube. Se muestran en este orden. */
  media: 'https://assets.cdn.filesafe.space/SImzaMApYvtVV8UzvlgD/media/',
  testimonios: [['v','6ac4236b195f9172ed95c91c'],['v','6ad260a5f9a985d42cbe18a8'],['y','U7ablyCr2_Y'],['v','6abc83aa6c64b8e488a2f025'],['v','6ab9e5fa5597aeb9d7f13c31'],['y','FjW8chAxRPk'],['v','6ab9b6e65597aeb9d7eca5b7'],['v','6ab9ba4abe703c7b30305435'],['y','cdcGh-oIV9Y'],['v','6aa0b1e2fb76acb4a93c0ffd'],['v','6ab9e143b4d207ff9d0c5bc7'],['y','0q4Ah_PL_1w'],['v','6ab9e2aac13d4373c2d28d8a'],['v','6ab9df5c5597aeb9d7f0b331'],['y','siIRcFF_Fzc'],['v','6aa0b40116ed327815b69e1a'],['v','6ad263a2fdbcf67570a0b065'],['y','8yGijdiMzJE'],['v','6ad2646686f4a10b2fa62ae0'],['v','6ab9dcba5597aeb9d7f076da'],['y','syL0QvfQHJ4'],['v','6ab9d97f5597aeb9d7f02cd7'],['v','6abaf9f3c13d4373c2ef5b47'],['y','ZYdiTIIDl6g'],['v','6abaf9a37ef452865a2fd7b4'],['v','6abb018672844d8ecf2e9e54'],['v','689fb4467bb59edaff12c342'],['v','689fb4467bb59e069512c341'],['v','689fb44669618cd2effbd32b'],['v','6ad263a41de0b9886006376a']],
  /* Fotos de eventos y rodajes, y capturas de mensajes de clientes. */
  fotos: ['6a3f2d42d50c4ff184edb838.jpeg','6a7e0125c0662ee5c46bb552.jpg','693dba4697c0236220e081ea.jpg','6a3f2d42e2763b2eec24a60c.jpeg','6a7d3d929115899f03677541.png','6a7e00e4494aefa6d8297657.jpg','67a95b7bfc7685e4ad16a204.png','67a8027f9769a75cfe604f9b.png','67a8027f9769a71ac3604f9c.png','67a8027ffc768597de1360da.png','67a8027f4325e15ee6581091.png','67a8027f4325e17938581092.png','67a8027f8f9e7e4c006b47f6.png'],
  capturas: ['6a3f2d4ae2763b2eec24a678.jpeg','6790e3b22aa71a8f8b682154.jpeg','67a8080cfc76856ca1136421.jpeg']
};
