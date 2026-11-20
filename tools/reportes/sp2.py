"""Genera reportes/SP2_Aplicacion_Web_SerranoArana.pdf
Uso (desde la raíz de AWP-Unidad-I):  python tools/reportes/sp2.py"""
import os
import sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from comun import RAIZ, Reporte, P, li, R, url, tabla, enlace, build_pdf

APP = "https://jazyelae.github.io/Mi_Recetario/"
REPO = "https://github.com/JazyelAe/Mi_Recetario"
r = Reporte("SP2")

cuerpo = [
    P("1. Introducción", "h1"),
    P("Las aplicaciones web son el tipo de software más extendido en Internet: basta un navegador y una dirección URL para usarlas, "
      "sin instalar nada. En este subproducto se define qué es una aplicación web, sus características y la tecnología con que se "
      "construye, y se presenta un ejemplo propio: <b>Mi Recetario</b>, un catálogo de recetas publicado en GitHub Pages que carga sus "
      "datos con <i>fetch</i> desde un archivo JSON y desde la API pública TheMealDB. Esta misma app evoluciona en el Subproducto 7 "
      "hacia una aplicación web progresiva (PWA); por eso aquí se documenta también su principal limitación: sin conexión no funciona."),

    P("2. Definición", "h1"),
    P("Una <b>aplicación web</b> es un programa que se ejecuta en el navegador y cuyos archivos (HTML, CSS y JavaScript) y datos "
      "residen en un servidor. El usuario accede a ella escribiendo una URL; el navegador solicita los recursos al servidor mediante "
      "el protocolo HTTP o HTTPS, los interpreta y muestra la interfaz. No requiere instalación y funciona en cualquier sistema operativo "
      "con un navegador moderno, pero depende de la conexión a Internet para obtener sus archivos y su información "
      "(MDN Web Docs, s.f.-a)."),

    P("3. Características", "h1"),
    li("<b>Arquitectura cliente-servidor:</b> el navegador (cliente) pide los recursos y el servidor los entrega por HTTP/HTTPS."),
    li("<b>Sin instalación:</b> se usa desde una URL; no ocupa espacio en el dispositivo ni pasa por tiendas de aplicaciones."),
    li("<b>Multiplataforma por naturaleza:</b> la misma app funciona en Windows, macOS, Linux, Android o iOS."),
    li("<b>Actualización inmediata:</b> al publicar una nueva versión en el servidor, todos los usuarios la reciben en su siguiente visita."),
    li("<b>Tecnologías estándar:</b> HTML para la estructura, CSS para el diseño y JavaScript para la lógica."),
    li("<b>Datos remotos:</b> consume información de archivos o APIs en formato JSON (MDN Web Docs, s.f.-c)."),
    li("<b>Diseño adaptable (responsive):</b> la interfaz se ajusta a celulares, tabletas y computadoras (MDN Web Docs, s.f.-b)."),
    li("<b>Dependencia de la conexión:</b> sin Internet el navegador no puede descargarla y muestra una página de error."),
    li("<b>Acceso limitado al dispositivo:</b> solo puede usar lo que el navegador permite (almacenamiento local, formularios, etc.)."),

    P("4. Tecnología utilizada", "h1"),
    tabla([["Elemento", "Tecnología en Mi Recetario"],
           ["Estructura", "HTML5 semántico: header, main, section, article, form y dialog"],
           ["Diseño", "CSS3 con variables, Grid, Flexbox y media queries (390, 768 y 1366 px)"],
           ["Lógica", "JavaScript sin frameworks: fetch, async/await, manejo del DOM, hashchange y localStorage"],
           ["Datos propios", "Archivo data/recetas.json con 12 recetas (ingredientes y pasos)"],
           ["Datos externos", "API REST pública TheMealDB, respuestas en JSON (TheMealDB, s.f.)"],
           ["Servidor", "GitHub Pages con HTTPS (GitHub, s.f.)"],
           ["Control de versiones", "Git y GitHub"],
           ["Pruebas y capturas", "Playwright con Google Chrome (escritorio, tableta y celular)"]], [130, 374]),

    P("5. Ilustración", "h1"),
    P("La Figura 1 muestra el funcionamiento: el navegador solicita la aplicación a GitHub Pages por HTTPS y después, con "
      "<i>fetch</i>, pide los datos en JSON tanto al archivo propio como a la API externa. La Figura 2 muestra la pantalla de inicio."),
    r.fig("fig_arquitectura.png", "Funcionamiento de una aplicación web: navegador, servidor web y fuentes de datos.", ancho=504),
    r.fig("01_inicio.png", "Pantalla de inicio de Mi Recetario en escritorio (1366 × 768).", ancho=460),

    P("6. Ejemplo propio: Mi Recetario", "h1"),
    P("<b>Propósito.</b> Facilitar la cocina casera con recetas sencillas, ingredientes fáciles de conseguir y la posibilidad de "
      "explorar recetas de otros países."),
    url(APP, "Aplicación publicada"),
    url(REPO, "Repositorio"),
    P("<b>Evidencias.</b> Las capturas y pruebas se generaron automáticamente con Playwright y Google Chrome contra la URL pública. "
      "Los 9 criterios de aceptación se cumplieron: carga sin errores en la consola, datos desde JSON, filtro y búsqueda, detalle, "
      "API externa, validación del formulario, diseño adaptable, ausencia de manifest y service worker, y la prueba sin conexión."),
    P("Cómo funciona, paso a paso", "h2"),
    P("<b>Paso 1. Cargar el catálogo.</b> Al abrir la URL, GitHub Pages entrega index.html, la hoja de estilos y los scripts. "
      "Después, JavaScript pide <i>data/recetas.json</i> con <i>fetch</i> y dibuja una tarjeta por receta."),
    P("<b>Paso 2. Filtrar y buscar.</b> Los botones de categoría y el buscador se combinan. La búsqueda revisa el nombre y los "
      "ingredientes sin distinguir acentos ni mayúsculas: «jitomate» y «JITÓMATE» dan los mismos 4 resultados."),
    r.fig("02_filtro_sopas.png", "Filtro por la categoría «Sopas».", ancho=420),
    r.fig("03_busqueda_aguacate.png", "Búsqueda por el ingrediente «aguacate».", ancho=420),
    P("<b>Paso 3. Ver el detalle.</b> Al tocar una tarjeta se abre una ventana con porciones, tiempo, dificultad, ingredientes y "
      "pasos. La dirección cambia a <i>#receta/&lt;id&gt;</i>, de modo que el enlace se puede compartir; la tecla Esc la cierra."),
    r.fig("04_detalle.png", "Detalle de la receta «Tacos de papa».", ancho=420),
    P("<b>Paso 4. Consumir una API externa.</b> En «Recetas del mundo» la app consulta en vivo el servicio REST TheMealDB "
      "(<i>search.php?s=chicken</i>), convierte su JSON al formato propio y muestra fotos, origen e instrucciones."),
    r.fig("05_mealdb.png", "Resultados en vivo de la API TheMealDB para «chicken».", ancho=420),
    r.fig("05b_mealdb_detalle.png", "Detalle de un platillo obtenido de TheMealDB, con foto e ingredientes.", ancho=420),
    P("<b>Paso 5. Enviar una sugerencia.</b> El formulario se valida en el navegador: nombre, correo, categoría y mensaje de 10 a "
      "300 caracteres. Como la app no tiene servidor propio, la sugerencia se guarda en el almacenamiento local del navegador."),
    r.fig("06_formulario_errores.png", "Validación en el cliente: mensajes de error por campo.", ancho=420),
    r.fig("07_formulario_ok.png", "Envío correcto de la sugerencia.", ancho=420),
    P("<b>Paso 6. Usarla en cualquier pantalla.</b> En el celular las tarjetas se reacomodan en dos columnas y el menú se "
      "convierte en un botón desplegable; en tableta el contenido pasa a una sola columna."),
    r.fila([("09_movil_inicio.png", "Inicio en celular (390 px)."),
            ("10_movil_menu.png", "Menú desplegable."),
            ("11_movil_detalle.png", "Detalle en celular.")], alto_max=300),
    P("<b>Paso 7. Limitación: sin conexión no funciona.</b> Al cortar la red y recargar, el navegador no puede descargar la app y "
      "muestra su página de error (<i>ERR_INTERNET_DISCONNECTED</i>). Mi Recetario no tiene manifest ni service worker que guarden "
      "una copia; esa es justamente la mejora que incorpora su versión PWA en el Subproducto 7."),
    r.fig("08b_sin_conexion_recorte.png", "Sin conexión, Chrome muestra su página de error (ERR_INTERNET_DISCONNECTED) y la aplicación web no carga.", ancho=400),

    P("7. Ejemplos de aplicaciones web existentes", "h1"),
    P("Gmail", "h2"),
    P("Servicio de correo electrónico de Google que se usa desde el navegador. <b>Cómo funciona:</b> el usuario inicia sesión en la "
      "URL y la interfaz, construida con JavaScript, pide al servidor los mensajes y los muestra sin recargar la página; los correos "
      "se guardan en los servidores de Google, por lo que se ven igual desde cualquier computadora."),
    url("https://mail.google.com/"),
    P("Documentos de Google", "h2"),
    P("Procesador de textos en línea de Google Workspace. <b>Cómo funciona:</b> el documento vive en la nube; cada cambio se envía "
      "al servidor y se guarda automáticamente, y varias personas pueden editar a la vez viendo los cambios de los demás en tiempo "
      "real, sin instalar ningún programa."),
    url("https://www.google.com/docs/about/"),
    P("Wikipedia", "h2"),
    P("Enciclopedia libre y colaborativa de la Fundación Wikimedia. <b>Cómo funciona:</b> cada artículo se genera en el servidor con "
      "el software MediaWiki y se envía al navegador como HTML; cualquier persona puede consultarlo desde una URL y los editores "
      "modifican el contenido desde la misma interfaz web."),
    url("https://es.wikipedia.org/"),

    P("8. Ventajas y desventajas", "h1"),
    tabla([["Ventajas", "Desventajas"],
           ["No requiere instalación: basta una URL.", "Necesita conexión a Internet; sin ella no carga."],
           ["Funciona en cualquier sistema operativo con navegador.", "Acceso limitado al hardware y a las funciones del dispositivo."],
           ["Una sola base de código para todos los usuarios.", "El rendimiento depende del navegador y de la red."],
           ["Actualizaciones inmediatas desde el servidor.", "No aparece en las tiendas de aplicaciones."],
           ["Desarrollo y publicación de bajo costo (por ejemplo, GitHub Pages).",
            "No envía notificaciones ni se instala como app (lo que sí logran las PWA)."],
           ["Fácil de compartir y enlazar (URL y enlaces directos).",
            "Las diferencias entre navegadores pueden requerir pruebas adicionales."]],
          [252, 252]),

    P("9. Conclusión", "h1"),
    P("Al convertir Mi Recetario en una aplicación web completa comprendí el papel de cada parte del modelo cliente-servidor: GitHub "
      "Pages entrega los archivos, el navegador los interpreta y JavaScript solicita los datos con <i>fetch</i>, tanto de un archivo "
      "propio como de un servicio externo. Separar los datos en un JSON hizo que el código fuera más ordenado y fácil de mantener, "
      "y la API de TheMealDB me mostró lo sencillo que es integrar información de otros servicios."),
    P("También comprobé su principal desventaja: en cuanto se pierde la conexión, la aplicación desaparece. Esta prueba es el punto "
      "de partida del Subproducto 7, en el que la misma idea se convierte en una PWA instalable y capaz de funcionar sin conexión."),

    P("10. Referencias", "h1"),
    R("GitHub. (s.f.). <i>¿Qué es GitHub Pages?</i> GitHub Docs. "
      + enlace("https://docs.github.com/es/pages/getting-started-with-github-pages/about-github-pages")),
    R("Google LLC. (s.f.-a). <i>Documentos de Google</i> [Aplicación web]. " + enlace("https://www.google.com/docs/about/")),
    R("Google LLC. (s.f.-b). <i>Gmail</i> [Aplicación web]. " + enlace("https://mail.google.com/")),
    R("MDN Web Docs. (s.f.-a). <i>Cómo funciona la web</i>. Mozilla. "
      + enlace("https://developer.mozilla.org/es/docs/Learn_web_development/Getting_started/Web_standards/How_the_web_works")),
    R("MDN Web Docs. (s.f.-b). <i>Diseño web adaptable</i>. Mozilla. "
      + enlace("https://developer.mozilla.org/es/docs/Learn_web_development/Core/CSS_layout/Responsive_Design")),
    R("MDN Web Docs. (s.f.-c). <i>Fetch API</i>. Mozilla. " + enlace("https://developer.mozilla.org/es/docs/Web/API/Fetch_API")),
    R("Serrano Arana, J. J. (2026). <i>Mi Recetario</i> [Aplicación web]. GitHub. " + enlace(REPO)),
    R("TheMealDB. (s.f.). <i>Free recipe API</i>. " + enlace("https://www.themealdb.com/api.php")),
    R("Wikimedia Foundation. (s.f.). <i>Wikipedia, la enciclopedia libre</i>. " + enlace("https://es.wikipedia.org/")),
]

salida = os.path.join(RAIZ, "reportes", "SP2_Aplicacion_Web_SerranoArana.pdf")
build_pdf(salida, titulo="SUBPRODUCTO No. 2: APLICACIÓN WEB",
          subtitulo="Actividad Desarrollo · Unidad I – Introducción a aplicaciones web progresivas",
          cuerpo=cuerpo, encabezado="APLICACIONES WEB PROGRESIVAS · SUBPRODUCTO 2")
print("PDF:", salida)
