"""Genera reportes/SP7_Aplicacion_Web_Progresiva_SerranoArana.pdf
Uso (desde la raíz de AWP-Unidad-I):  python tools/reportes/sp7.py"""
import os
import sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from comun import RAIZ, Reporte, P, li, R, url, tabla, enlace, build_pdf  # noqa: E402

APP = "https://jazyelae.github.io/MiRecetario-PWA/"
REPO = "https://github.com/JazyelAe/MiRecetario-PWA"
SP2 = "https://github.com/JazyelAe/Mi_Recetario"
r = Reporte("SP7")

cuerpo = [
    P("1. Introducción", "h1"),
    P("Las aplicaciones web progresivas (PWA) reúnen lo mejor de dos mundos: se publican y se abren como cualquier página web, "
      "con un enlace y sin tienda de aplicaciones, pero se pueden instalar, tienen su propio icono y ventana, y funcionan sin "
      "conexión como una app nativa. En este subproducto se define qué es una PWA, sus características, ventajas, desventajas y "
      "herramientas de desarrollo, y se presentan evidencias de cada característica sobre una app propia, <b>Mi Recetario PWA</b>, "
      "y sobre PWA reales."),
    P("Mi Recetario PWA es la <b>evolución de la aplicación web del Subproducto 2</b> (Mi_Recetario). Aquella era una app web "
      "clásica: solo funcionaba con Internet y vivía en una pestaña del navegador. Sobre esa base se agregaron una base de datos en "
      "la nube (Firebase Firestore), un manifiesto, un service worker y una caché sin conexión, que son las piezas que convierten una "
      "app web en una PWA."),
    tabla([["", "App web (SP2)", "PWA (SP7)"],
           ["Datos", "JSON local y localStorage", "Firestore con caché persistente sin conexión"],
           ["Sin Internet", "No abre", "Abre y muestra las recetas guardadas"],
           ["Instalación", "No", "Sí: icono propio y ventana independiente"],
           ["Archivos", "Se descargan en cada visita", "Service worker y Cache Storage"]],
          [90, 207, 207]),

    P("2. Definición", "h1"),
    P("Una <b>aplicación web progresiva</b> es una aplicación construida con tecnologías web (HTML, CSS y JavaScript) que, gracias "
      "a capacidades modernas del navegador, ofrece una experiencia comparable a la de una aplicación instalada: se puede instalar en "
      "el dispositivo, funciona de forma confiable aun con mala conexión o sin ella, y se integra con el sistema operativo. Es "
      "«progresiva» porque funciona para cualquier usuario en cualquier navegador y va agregando capacidades según lo que el "
      "navegador soporte (web.dev, s.f.; MDN Web Docs, s.f.-a)."),
    P("Microsoft la describe como una app que se ejecuta desde un sitio web, pero que puede instalarse en el dispositivo, "
      "aparecer en el menú Inicio o la barra de tareas, funcionar sin conexión y recibir notificaciones, usando una sola base de "
      "código para todas las plataformas (Microsoft, s.f.). Técnicamente, lo mínimo que la distingue es un <b>manifiesto de "
      "aplicación web</b>, un <b>service worker</b> y servirse por <b>HTTPS</b>."),

    P("3. Características", "h1"),
    li("<b>Instalable:</b> el manifiesto describe nombre, iconos y colores; el navegador ofrece instalarla y la abre en su propia ventana."),
    li("<b>Funciona sin conexión (offline):</b> el service worker guarda los archivos en Cache Storage y responde aunque no haya red."),
    li("<b>Responsive:</b> se adapta a teléfono, tableta y computadora."),
    li("<b>Segura:</b> solo funciona por HTTPS, lo que protege los datos y evita alteraciones."),
    li("<b>Similar a una app (<i>app-like</i>):</b> ventana sin barra de direcciones, pantalla de inicio e icono en el sistema."),
    li("<b>Actualizable:</b> al cambiar el service worker, los usuarios reciben la nueva versión sin reinstalar nada."),
    li("<b>Descubrible:</b> es un sitio web; los buscadores la indexan y se comparte con un enlace."),
    li("<b>Re-engageable:</b> puede avisar al usuario (notificaciones, avisos de conexión) para que vuelva."),

    P("4. Ventajas y desventajas", "h1"),
    tabla([["Ventajas", "Desventajas"],
           ["Un solo código para todas las plataformas.", "El acceso al hardware es menor que en una app nativa (algunas APIs no existen o varían)."],
           ["Se instala sin tienda de aplicaciones y sin revisión.", "No aparece automáticamente en las tiendas; hay que promoverla."],
           ["Funciona sin conexión y carga rápido desde la caché.", "La estrategia de caché agrega complejidad (versiones, datos desactualizados)."],
           ["Se actualiza sola al publicar en el servidor.", "Safari en iOS soporta menos funciones que Chrome o Edge."],
           ["Ocupa mucho menos espacio que una app nativa.", "Si el usuario borra los datos del navegador, se pierde lo guardado."],
           ["Se comparte con un enlace y la indexan los buscadores.", "Requiere HTTPS y un servidor para probarla (no basta abrir el archivo)."]],
          [252, 252]),

    P("5. Herramientas de desarrollo", "h1"),
    tabla([["Herramienta", "Para qué sirve (uso en Mi Recetario)"],
           ["Web App Manifest", "Archivo JSON con nombre, iconos, colores y modo de pantalla (manifest.json con icono maskable y capturas)"],
           ["Service Worker API", "Script que intercepta las peticiones y decide de dónde responder (service-worker.js)"],
           ["Cache Storage API", "Almacén de respuestas HTTP en el dispositivo (archivos de la app y fotos)"],
           ["Firebase Firestore", "Base de datos en la nube con caché persistente en IndexedDB para funcionar sin conexión"],
           ["Chrome DevTools (Application)", "Inspeccionar el manifiesto, el service worker y las cachés"],
           ["Chrome DevTools Protocol + Playwright", "Pruebas automáticas: instalabilidad, modo sin conexión y capturas"],
           ["PWABuilder", "Herramienta de Microsoft para validar una PWA y empaquetarla para tiendas (no usada en el código)"],
           ["Workbox", "Biblioteca de Google para generar service workers con estrategias listas (alternativa a escribirlo a mano)"]],
          [150, 354]),
    P("La Figura 1 resume cómo trabajan juntas estas piezas en Mi Recetario."),
    r.fig("fig_arquitectura.png", "Funcionamiento de Mi Recetario PWA con y sin conexión.", ancho=504),

    P("6. Ejemplos de aplicaciones web progresivas", "h1"),
    P("Mi Recetario PWA (propia)", "h2"),
    P("Recetario de cocina casera con base de datos en Firebase y búsqueda en TheMealDB. Se instala, abre sin conexión mostrando "
      "las recetas guardadas y sincroniza lo agregado sin red al volver la conexión."),
    url(APP), url(REPO, "Repositorio"),
    P("Squoosh (Google Chrome Labs)", "h2"),
    P("Compresor de imágenes que trabaja por completo en el navegador, sin subir las fotos a un servidor. Su repositorio oficial la "
      "llama «Squoosh PWA»; Chrome confirmó que tiene manifiesto, service worker activo y ningún error de instalabilidad "
      "(GoogleChromeLabs, s.f.)."),
    url("https://squoosh.app/"),
    P("Uber (m.uber.com)", "h2"),
    P("Versión web para pedir viajes, pensada para teléfonos de gama baja y redes lentas. El equipo de ingeniería de Uber explica "
      "que la construyó muy ligera y que usa service workers para seguir funcionando con conexiones intermitentes (Uber "
      "Engineering, 2017). Chrome confirmó que tiene manifiesto y es instalable."),
    url("https://m.uber.com/"),
    P("Pinterest", "h2"),
    P("Red para guardar ideas en imágenes. Su equipo de ingeniería relata que el nuevo sitio móvil se construyó como una PWA con "
      "<i>app shell</i>, instalación en la pantalla de inicio, notificaciones push y caché de recursos (Pinterest Engineering, 2018). "
      "Chrome confirmó que tiene manifiesto y es instalable."),
    url("https://www.pinterest.com/"),

    P("7. Evidencias de identificación de características", "h1"),
    P("Las evidencias se obtuvieron sobre la app publicada en GitHub Pages. Las marcadas como automáticas se leyeron del propio "
      "Chrome con Playwright y el Chrome DevTools Protocol; las de DevTools e instalación son capturas tomadas por el autor en su "
      "computadora. Resultado de las pruebas automáticas: 11 de 11 comprobaciones correctas."),
    "EVIDENCIAS",

    P("8. Conclusión", "h1"),
    P("Convertir la app web del Subproducto 2 en una PWA no requirió rehacerla, sino agregar piezas bien definidas: un manifiesto "
      "para que el sistema la reconozca como app, un service worker con una estrategia de caché para cada tipo de archivo y la caché "
      "persistente de Firestore para los datos. Con ellas, Mi Recetario se instala con su icono, abre en su propia ventana y sigue "
      "mostrando las recetas sin Internet."),
    P("Las pruebas también revelaron fallas que no se veían a simple vista: sin conexión la lista quedaba vacía, el icono maskable "
      "se habría recortado en Android y las reglas de la base permitían que cualquiera borrara todo. Corregirlas me enseñó que una PWA "
      "no es solo «una página que se instala»: la confiabilidad sin conexión y la seguridad de los datos se tienen que diseñar y "
      "comprobar."),

    P("9. Referencias", "h1"),
    R("GoogleChromeLabs. (s.f.). <i>Squoosh</i> [Repositorio de código]. GitHub. " + enlace("https://github.com/GoogleChromeLabs/squoosh")),
    R("Google. (s.f.). <i>Enable offline data</i>. Firebase documentation. "
      + enlace("https://firebase.google.com/docs/firestore/manage-data/enable-offline")),
    R("MDN Web Docs. (s.f.-a). <i>Aplicaciones web progresivas</i>. Mozilla. "
      + enlace("https://developer.mozilla.org/es/docs/Web/Progressive_web_apps")),
    R("MDN Web Docs. (s.f.-b). <i>API Service Worker</i>. Mozilla. "
      + enlace("https://developer.mozilla.org/es/docs/Web/API/Service_Worker_API")),
    R("Microsoft. (s.f.). <i>Información general sobre las aplicaciones web progresivas (PWA)</i>. Microsoft Learn. "
      + enlace("https://learn.microsoft.com/es-es/microsoft-edge/progressive-web-apps/")),
    R("Pinterest Engineering. (2018, 20 de julio). <i>A one year PWA retrospective</i>. Medium. "
      + enlace("https://medium.com/pinterest-engineering/a-one-year-pwa-retrospective-f4a2f4129e05")),
    R("Serrano Arana, J. J. (2026). <i>Mi Recetario PWA</i> [Aplicación web progresiva]. GitHub. " + enlace(REPO)),
    R("Uber Engineering. (2017, 26 de junio). <i>Building m.uber: Engineering a high-performance web app for the global market</i>. "
      "Uber Blog. " + enlace("https://www.uber.com/blog/m-uber/")),
    R("web.dev. (s.f.). <i>Learn PWA</i>. Google. " + enlace("https://web.dev/learn/pwa/")),
]

# Una evidencia por característica: (título, [(captura, pie)], descripción de lo que demuestra)
EVID = [
    ("7.1 Manifiesto de aplicación web",
     [("04_manifest.png", "Manifiesto leído por Chrome (automático): 0 errores."),
      ("11_devtools_manifest.png", "DevTools → Application → Manifest (captura del autor).")],
     "Chrome reconoce nombre, nombre corto, URL de inicio, modo standalone, colores y los tres iconos, incluido el maskable."),
    ("7.2 Service worker activo",
     [("05_service_worker.png", "Service worker en estado activated y controlando la página (automático).")],
     "El script service-worker.js está registrado con alcance /MiRecetario-PWA/ y aplica una estrategia distinta según el tipo de petición."),
    ("7.3 Cache Storage",
     [("06_cache_storage.png", "Archivos guardados en el dispositivo por el service worker (automático).")],
     "La caché recetario-app-v2 contiene la app completa, la página offline y el SDK de Firebase: todo lo necesario para abrir sin red."),
    ("7.4 Instalación y ventana propia",
     [("07_instalable.png", "Page.getInstallabilityErrors: ninguno (automático)."),
      ("12_abrir_en_aplicacion.png", "Chrome ofrece «Abrir en aplicación» (captura del autor)."),
      ("13_ventana_standalone.png", "La app en su propia ventana, sin barra de direcciones (captura del autor).")],
     "Chrome no encuentra impedimentos para instalarla. Una vez instalada, la barra de direcciones muestra «Abrir en aplicación» y la app abre en una ventana independiente con el color del tema."),
    ("7.5 Funcionamiento sin conexión",
     [("08_offline.png", "Recarga sin red: indicador «Sin conexión» y las recetas visibles (automático)."),
      ("09_offline_html.png", "Página no guardada sin red: offline.html (automático).")],
     "Con la red desconectada (Playwright, set_offline) la página se recarga desde la caché y muestra las mismas 2 recetas que con conexión, gracias a la caché persistente de Firestore."),
    ("7.6 Responsive",
     [("01_escritorio.png", "Computadora, 1280 px."), ("02_movil.png", "Teléfono, 390 px.")],
     "El diseño se adapta al ancho de la pantalla sin desbordamiento horizontal (comprobado automáticamente)."),
    ("7.7 HTTPS",
     [("03_https.png", "Certificado y contexto seguro leídos por Chrome (automático).")],
     "GitHub Pages sirve la app con TLS; window.isSecureContext es verdadero, requisito para registrar el service worker."),
    ("7.8 Seguridad de los datos (reglas de Firestore)",
     [("14_regla_alta.png", "Receta de prueba creada desde la app; se borró dentro de los 10 minutos permitidos.")],
     "Se comprobó contra la base real: borrar una receta antigua y crear una con campos no permitidos fueron rechazados (403); crear una válida y borrarla dentro de 10 minutos sí se permitió (6 de 6 pruebas)."),
    ("7.9 La misma verificación en una PWA real",
     [("10_pwa_real_squoosh.png", "Squoosh: manifiesto, service worker activo e instalable (automático).")],
     "Las mismas lecturas aplicadas a Squoosh muestran las piezas que comparte con Mi Recetario: manifiesto con display standalone, service worker y criterios de instalación cumplidos."),
]


def alto_figura(nombre, ancho, alto_max):
    from PIL import Image
    w, h = Image.open(os.path.join(r.evid, nombre)).size
    return h * min(ancho / w, alto_max / h)


def evidencias():
    """Cada evidencia (título + descripción + figuras) pasa a la página siguiente solo si no cabe completa."""
    from reportlab.platypus import CondPageBreak
    bloques = []
    for titulo, capturas, texto in EVID:
        if len(capturas) == 1:
            alto = alto_figura(capturas[0][0], 380, 215)
            figura = r.fig(capturas[0][0], capturas[0][1], ancho=380, alto_max=215)
        else:
            columna = 504 / len(capturas) - 12
            alto = max(alto_figura(n, columna, 225) for n, _ in capturas)
            figura = r.fila(capturas, alto_max=225)
        bloques += [CondPageBreak(alto + 95), P(titulo, "h2"), P(texto), figura]
    return bloques


final = []
for c in cuerpo:
    final += evidencias() if c == "EVIDENCIAS" else [c]

salida = os.path.join(RAIZ, "reportes", "SP7_Aplicacion_Web_Progresiva_SerranoArana.pdf")
build_pdf(salida, titulo="SUBPRODUCTO No. 7: APLICACIÓN WEB PROGRESIVA",
          subtitulo="Actividad Cierre · Unidad I – Introducción a aplicaciones web progresivas",
          cuerpo=final, encabezado="APLICACIONES WEB PROGRESIVAS · SUBPRODUCTO 7")
print("PDF:", salida)
