"""Genera reportes/P1_Reporte_Comparativo_SerranoArana.pdf (Producto No. 1)
Los textos resumen los reportes SP1–SP7 ya aprobados.
Uso (desde la raíz de AWP-Unidad-I):  python tools/reportes/p1.py"""
import os
import sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from comun import RAIZ, Reporte, P, li, R, tabla, enlace, build_pdf  # noqa: E402
from utp_doc import horizontal, vertical  # noqa: E402

GH = "https://github.com/JazyelAe/"
PAGES = "https://jazyelae.github.io/"
CENTRAL = GH + "AWP-Unidad-I"
r = Reporte("P1")
r.evid = os.path.join(RAIZ, "evidencias")   # la galería usa capturas de todas las carpetas SP1…SP7


def lista(*puntos):
    return "<br/>".join("• " + p for p in puntos)


def urls(app, repo, ejemplo):
    """Celda de URL: app propia, repositorio y un ejemplo real (todos clicables)."""
    return "<br/>".join([f"<b>App:</b> {app}", f"<b>Repo:</b> {repo}", f"<b>Ejemplo:</b> {ejemplo}"])


FILAS = [
    ("Nativa",
     "Programa hecho para un solo sistema operativo con su lenguaje y SDK oficiales (Kotlin/Java + Android SDK, Swift + iOS SDK); "
     "se compila e instala en el dispositivo (Android Developers, s.f.).",
     lista("Una plataforma por código", "Acceso completo al hardware y APIs", "Alto rendimiento", "Se instala (APK/AAB, IPA) desde tiendas"),
     lista("Máximo rendimiento", "Cámara, GPS, sensores, notificaciones", "Interfaz del sistema", "Funciona sin conexión"),
     lista("Un código por plataforma", "Mayor costo y tiempo", "Revisión y cuotas de tiendas", "Hay que actualizar la app"),
     lista("Kotlin, Jetpack Compose", "Android Studio, Gradle", "Swift, Xcode", "GitHub Actions"),
     urls(enlace(GH + "AquaTrack-Nativa/releases/tag/v1.0.0", "AquaTrack (APK)"),
          enlace(GH + "AquaTrack-Nativa", "AquaTrack-Nativa"),
          enlace("https://play.google.com/store/apps/details?id=com.whatsapp", "WhatsApp"))),
    ("Web",
     "Programa que se ejecuta en el navegador; sus archivos (HTML, CSS, JavaScript) y datos están en un servidor y se piden por "
     "HTTP/HTTPS desde una URL (MDN Web Docs, s.f.-a).",
     lista("Cliente-servidor", "Sin instalación", "Funciona en cualquier sistema", "Actualización inmediata"),
     lista("Solo se necesita una URL", "Un código para todos", "Bajo costo (GitHub Pages)", "Fácil de compartir"),
     lista("Requiere Internet", "Acceso limitado al dispositivo", "No está en tiendas", "Diferencias entre navegadores"),
     lista("HTML5, CSS3, JavaScript", "fetch y APIs JSON", "VS Code, DevTools", "GitHub Pages"),
     urls(enlace(PAGES + "Mi_Recetario/", "Mi Recetario"), enlace(GH + "Mi_Recetario", "Mi_Recetario"),
          enlace("https://mail.google.com/", "Gmail"))),
    ("Escritorio",
     "Programa que se instala y ejecuta en el sistema operativo de una computadora (Windows, macOS, Linux), en su propia ventana y "
     "con recursos locales, sin navegador (The Qt Company, s.f.).",
     lista("Ventana propia", "Funciona sin Internet", "Archivos, impresoras, hardware", "Ejecutable por sistema (.exe)"),
     lista("Alto rendimiento", "Datos privados en el equipo", "Interfaz rica", "No requiere servidor"),
     lista("Instalar en cada equipo", "Depende del sistema operativo", "Actualizar equipo por equipo", "Ocupa espacio en disco"),
     lista("Python + PySide6 (Qt)", "C#/.NET, Java, C++", "PyInstaller", "Visual Studio, VS Code"),
     urls(enlace(GH + "App_de_Escritorio/releases/tag/v1.0.0", "DeskData Pro (.exe)"),
          enlace(GH + "App_de_Escritorio", "App_de_Escritorio"),
          enlace("https://code.visualstudio.com/", "Visual Studio Code"))),
    ("Orientada a servicios",
     "Aplicación dividida en servicios independientes, cada uno con una responsabilidad y una interfaz (API REST) que se consume por "
     "HTTP/JSON; si son pequeños y separados se llaman microservicios (Amazon Web Services, s.f.).",
     lista("Servicios con una sola función", "Comunicación HTTP/JSON", "Contrato documentado (OpenAPI)", "Bajo acoplamiento"),
     lista("Se cambian por separado", "Reutiliza servicios externos", "Cualquier cliente los usa", "Escalado independiente"),
     lista("Más piezas que desplegar", "Depende de la red y de terceros", "Seguridad en cada llamada", "Requiere servidor o hosting"),
     lista("Flask (Python), Node.js", "SQLite, Firestore", "Swagger/OpenAPI", "pytest, gunicorn"),
     urls(enlace(PAGES + "BiblioServ-Servicios/", "BiblioServ (cliente; API local)"),
          enlace(GH + "BiblioServ-Servicios", "BiblioServ-Servicios"),
          enlace("https://www.mercadopago.com.mx/developers/es/reference", "API de Mercado Pago"))),
    ("Móvil",
     "Aplicación diseñada para teléfonos y tabletas: pantalla táctil pequeña, uso con una mano y capacidades del dispositivo como "
     "notificaciones y vibración; puede ser nativa o hecha con frameworks como Flutter (Flutter, s.f.).",
     lista("Diseño para pantalla pequeña", "Gestos táctiles", "Notificaciones y sensores", "Permisos del usuario"),
     lista("Siempre a la mano", "Gestos rápidos y naturales", "Notificaciones que invitan a volver", "Funciona sin conexión"),
     lista("Poca pantalla", "Muchos tamaños y versiones", "Permisos que se pueden negar", "Batería y almacenamiento"),
     lista("Flutter + Dart", "Material 3", "Emulador Android", "Notificaciones locales"),
     urls(enlace(GH + "MisPendientes-Movil/releases/tag/v1.0.1", "Mis Pendientes (APK)") + " · "
          + enlace(PAGES + "MisPendientes-Movil/", "demo web"),
          enlace(GH + "MisPendientes-Movil", "MisPendientes-Movil"),
          enlace("https://play.google.com/store/apps/details?id=com.instagram.android", "Instagram"))),
    ("Multiplataforma",
     "Aplicación que, con una sola base de código, se ejecuta en varios sistemas (Android, iOS, web); el framework traduce el código "
     "a los componentes de cada plataforma (React Native, s.f.).",
     lista("Un solo código", "Varios destinos", "Componentes de cada sistema", "Código por plataforma solo si hace falta"),
     lista("Menor costo y tiempo", "Una corrección llega a todos", "Aspecto propio de cada sistema", "Versión web sin instalar"),
     lista("Funciones específicas requieren módulos", "Algo menos de rendimiento", "Depende del framework", "iOS requiere Mac o nube"),
     lista("React Native + Expo", "Flutter", "Expo Go", "jest, GitHub Actions"),
     urls(enlace(PAGES + "ConvierteYA-Multiplataforma/", "ConvierteYA (web)") + " · "
          + enlace(GH + "ConvierteYA-Multiplataforma/releases/tag/v1.0.1", "APK"),
          enlace(GH + "ConvierteYA-Multiplataforma", "ConvierteYA-Multiplataforma"),
          enlace("https://play.google.com/store/apps/details?id=com.discord", "Discord"))),
    ("Web progresiva (PWA)",
     "Aplicación web que, con un manifiesto, un service worker y HTTPS, se instala en el dispositivo, funciona sin conexión y se "
     "comporta como una app instalada (web.dev, s.f.; MDN Web Docs, s.f.-b; Microsoft, s.f.-a).",
     lista("Instalable", "Funciona sin conexión", "Responsive y segura (HTTPS)", "Actualizable y descubrible"),
     lista("Un código para todos", "Sin tienda de aplicaciones", "Rápida desde la caché", "Ocupa poco espacio"),
     lista("Menos acceso al hardware", "iOS soporta menos funciones", "Caché más compleja", "No aparece sola en tiendas"),
     lista("Web App Manifest", "Service Worker y Cache Storage", "Firebase, Workbox", "DevTools, PWABuilder"),
     urls(enlace(PAGES + "MiRecetario-PWA/", "Mi Recetario PWA"), enlace(GH + "MiRecetario-PWA", "MiRecetario-PWA"),
          enlace("https://squoosh.app/", "Squoosh"))),
]

APPS = [
    ("SP1", "Nativa", "AquaTrack", "AquaTrack-Nativa", GH + "AquaTrack-Nativa/releases/tag/v1.0.0", "APK v1.0.0",
     "SP1_Aplicacion_Nativa_SerranoArana.pdf", "SP1/01_inicio.png", "AquaTrack (nativa, Kotlin): registro de agua del día."),
    ("SP2", "Web", "Mi Recetario", "Mi_Recetario", PAGES + "Mi_Recetario/", "GitHub Pages",
     "SP2_Aplicacion_Web_SerranoArana.pdf", "SP2/01_inicio.png", "Mi Recetario (web): recetas en el navegador."),
    ("SP3", "Escritorio", "DeskData Pro", "App_de_Escritorio", GH + "App_de_Escritorio/releases/tag/v1.0.0", "DeskDataPro.exe v1.0.0",
     "SP3_Aplicacion_Escritorio_SerranoArana.pdf", "SP3/01_inicio.png", "DeskData Pro (escritorio, PySide6): ventana de Windows."),
    ("SP4", "Móvil", "Mis Pendientes", "MisPendientes-Movil", GH + "MisPendientes-Movil/releases/tag/v1.0.1", "APK v1.0.1",
     "SP4_Aplicacion_Movil_SerranoArana.pdf", "SP4/01_lista.png", "Mis Pendientes (móvil, Flutter) en Android."),
    ("SP5", "Multiplataforma", "ConvierteYA", "ConvierteYA-Multiplataforma", PAGES + "ConvierteYA-Multiplataforma/", "Web + APK v1.0.1",
     "SP5_Aplicacion_Multiplataforma_SerranoArana.pdf", "SP5/11_misma_app_web_android.png",
     "ConvierteYA (multiplataforma): el mismo código en web y Android."),
    ("SP6", "Orientada a servicios", "BiblioServ", "BiblioServ-Servicios", PAGES + "BiblioServ-Servicios/", "Cliente en Pages (API local)",
     "SP6_Aplicacion_Servicios_SerranoArana.pdf", "SP6/02_lista.png", "BiblioServ (servicios): cliente que consume la API."),
    ("SP7", "Web progresiva", "Mi Recetario PWA", "MiRecetario-PWA", PAGES + "MiRecetario-PWA/", "App instalable",
     "SP7_Aplicacion_Web_Progresiva_SerranoArana.pdf", "SP7/13_ventana_standalone.png", "Mi Recetario PWA instalada, en su propia ventana."),
]

cuerpo = [
    P("1. Introducción", "h1"),
    P("Este producto reúne lo trabajado en la Unidad I: siete tipos de aplicaciones, cada una estudiada en un subproducto y "
      "acompañada de un proyecto propio, publicado y probado. Su propósito es <b>compararlas</b> en una sola tabla —definición, "
      "características, ventajas, desventajas, herramientas de desarrollo y URL— para decidir qué tipo conviene en cada situación "
      "y entender por qué las aplicaciones web progresivas son el tema central de la materia."),
    tabla([["Subproducto", "Tipo", "Proyecto propio", "Qué hace"],
           ["SP1", "Nativa", "AquaTrack", "Registro de consumo de agua con recordatorios (Kotlin)"],
           ["SP2", "Web", "Mi Recetario", "Recetas en el navegador con búsqueda en TheMealDB"],
           ["SP3", "Escritorio", "DeskData Pro", "Gestor de datos y monitor del equipo en Windows (PySide6)"],
           ["SP4", "Móvil", "Mis Pendientes", "Tareas con gestos y notificaciones (Flutter)"],
           ["SP5", "Multiplataforma", "ConvierteYA", "Conversor de unidades y divisas, web y Android (React Native)"],
           ["SP6", "Orientada a servicios", "BiblioServ", "Biblioteca con autenticación, catálogo y Open Library (Flask)"],
           ["SP7", "Web progresiva", "Mi Recetario PWA", "Recetario instalable que funciona sin conexión (Firebase)"]],
          [62, 92, 92, 258]),
    P("Los textos resumen los reportes de cada subproducto. Todos los enlaces de la tabla son clicables y se comprobaron el "
      "20 de noviembre de 2026."),
    horizontal(),
    P("2. Tabla comparativa", "h1"),
    tabla([["Tipo", "Definición", "Características", "Ventajas", "Desventajas", "Herramientas de desarrollo", "URL de la aplicación"]]
          + [[f"<b>{f[0]}</b>"] + list(f[1:]) for f in FILAS],
          [72, 122, 98, 96, 96, 86, 114]),
    vertical(),
    P("3. Galería de las aplicaciones", "h1"),
    P("Una captura real de cada proyecto, tomada en las pruebas de su subproducto."),
]

GALERIA = [(a[7], a[8]) for a in APPS]
for i in range(0, len(GALERIA), 2):
    cuerpo.append(r.fila(GALERIA[i:i + 2], alto_max=230))

cuerpo += [
    P("4. Resumen de enlaces", "h1"),
    tabla([["", "Aplicación", "Repositorio", "URL pública", "Reporte"]]
          + [[a[0], f"<b>{a[2]}</b><br/>{a[1]}", enlace(GH + a[3], a[3]), enlace(a[4], a[5]),
              enlace(f"{CENTRAL}/blob/main/reportes/{a[6]}", f"{a[0]} PDF")] for a in APPS],
          [34, 100, 140, 130, 100]),
    P("La API de BiblioServ no se publicó en un hosting: se ejecuta en la computadora y se prueba en GitHub Actions con gunicorn. "
      "Repositorio central con todos los reportes y evidencias: " + enlace(CENTRAL) + "."),

    P("5. Conclusión", "h1"),
    P("Cada tipo de aplicación responde a una necesidad distinta. Una <b>app nativa</b> conviene cuando se necesita el máximo "
      "rendimiento y acceso total al hardware, aceptando mantener un código por plataforma. Una <b>app web</b> es la forma más "
      "barata y rápida de llegar a cualquiera con solo una URL, pero depende de Internet. Una <b>app de escritorio</b> es ideal para "
      "trabajo intensivo con archivos y recursos locales en una computadora. Una <b>app móvil</b> aprovecha gestos, notificaciones y "
      "el hecho de que el teléfono siempre está a la mano. Una <b>app multiplataforma</b> reduce el costo al compartir un código "
      "entre sistemas, y una <b>arquitectura orientada a servicios</b> organiza el sistema en piezas que se comunican por HTTP/JSON "
      "y que cualquier cliente puede reutilizar."),
    P("Las <b>aplicaciones web progresivas</b> combinan lo mejor de ambos mundos: conservan las ventajas de la web (una URL, un "
      "solo código, actualización inmediata y sin tiendas) y suman las de una app instalada (icono propio, ventana independiente y "
      "funcionamiento sin conexión). En Mi Recetario PWA lo comprobé al ver la misma app web del Subproducto 2 instalada en Windows "
      "y mostrando recetas sin Internet. Sus límites —menos acceso al hardware y soporte desigual en iOS— hacen que no sustituyan "
      "por completo a las apps nativas, pero para la mayoría de las aplicaciones de información y servicios son hoy la opción más "
      "equilibrada."),

    P("6. Referencias", "h1"),
    R("Amazon Web Services. (s.f.). <i>What are microservices?</i> " + enlace("https://aws.amazon.com/microservices/")),
    R("Android Developers. (s.f.). <i>Platform architecture</i>. Google. " + enlace("https://developer.android.com/guide/platform")),
    R("Discord Inc. (s.f.). <i>Discord</i> [Aplicación móvil]. Google Play. "
      + enlace("https://play.google.com/store/apps/details?id=com.discord")),
    R("Expo. (s.f.). <i>Expo documentation</i>. " + enlace("https://docs.expo.dev/")),
    R("Flutter. (s.f.). <i>Flutter documentation</i>. Google. " + enlace("https://docs.flutter.dev/")),
    R("GoogleChromeLabs. (s.f.). <i>Squoosh</i> [Repositorio de código]. GitHub. " + enlace("https://github.com/GoogleChromeLabs/squoosh")),
    R("Google LLC. (s.f.). <i>Gmail</i> [Aplicación web]. " + enlace("https://mail.google.com/")),
    R("Instagram. (s.f.). <i>Instagram</i> [Aplicación móvil]. Google Play. "
      + enlace("https://play.google.com/store/apps/details?id=com.instagram.android")),
    R("MDN Web Docs. (s.f.-a). <i>Cómo funciona la web</i>. Mozilla. "
      + enlace("https://developer.mozilla.org/es/docs/Learn_web_development/Getting_started/Web_standards/How_the_web_works")),
    R("MDN Web Docs. (s.f.-b). <i>Aplicaciones web progresivas</i>. Mozilla. "
      + enlace("https://developer.mozilla.org/es/docs/Web/Progressive_web_apps")),
    R("Mercado Pago. (s.f.). <i>API reference</i>. Mercado Pago Developers. "
      + enlace("https://www.mercadopago.com.mx/developers/es/reference")),
    R("Microsoft. (s.f.-a). <i>Información general sobre las aplicaciones web progresivas (PWA)</i>. Microsoft Learn. "
      + enlace("https://learn.microsoft.com/es-es/microsoft-edge/progressive-web-apps/")),
    R("Microsoft. (s.f.-b). <i>Visual Studio Code</i> [Software]. " + enlace("https://code.visualstudio.com/")),
    R("React Native. (s.f.). <i>React Native: Learn once, write anywhere</i>. Meta. " + enlace("https://reactnative.dev/")),
    R("Serrano Arana, J. J. (2026). <i>AWP-Unidad-I: Reportes y evidencias de la Unidad I</i> [Repositorio]. GitHub. "
      + enlace(CENTRAL)),
    R("The Qt Company. (s.f.). <i>Qt for Python</i>. " + enlace("https://doc.qt.io/qtforpython-6/")),
    R("web.dev. (s.f.). <i>Learn PWA</i>. Google. " + enlace("https://web.dev/learn/pwa/")),
    R("WhatsApp LLC. (s.f.). <i>WhatsApp Messenger</i> [Aplicación móvil]. Google Play. "
      + enlace("https://play.google.com/store/apps/details?id=com.whatsapp")),
]

salida = os.path.join(RAIZ, "reportes", "P1_Reporte_Comparativo_SerranoArana.pdf")
build_pdf(salida, titulo="PRODUCTO No. 1: REPORTE COMPARATIVO DE TIPOS DE APLICACIONES",
          subtitulo="Unidad I – Introducción a aplicaciones web progresivas",
          cuerpo=cuerpo, encabezado="APLICACIONES WEB PROGRESIVAS · PRODUCTO 1")
print("PDF:", salida)
