"""Genera reportes/SP1_Aplicacion_Nativa_SerranoArana.pdf
Uso (desde la raíz de AWP-Unidad-I):  python tools/reportes/sp1.py [--borrador]
--borrador: si falta una captura pone un recuadro "PENDIENTE" (solo para revisar el diseño, NO para entregar)."""
import os
import sys

RAIZ = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
sys.path.insert(0, os.path.join(RAIZ, "tools"))
from utp_doc import *  # noqa: E402,F403
from reportlab.lib.styles import ParagraphStyle  # noqa: E402
from reportlab.platypus import Paragraph, Table, TableStyle, KeepTogether  # noqa: E402

BORRADOR = "--borrador" in sys.argv
EVID = os.path.join(RAIZ, "evidencias", "SP1")
REPO = "https://github.com/JazyelAe/AquaTrack-Nativa"
RELEASE = REPO + "/releases/tag/v1.0.0"
s = estilos()
n_fig = [0]


def P(texto, estilo="body"):
    return Paragraph(texto, s[estilo])


REF = ParagraphStyle("ref", parent=s["bullet"], leftIndent=22, firstLineIndent=-22)


def R(texto):
    """Referencia APA 7 con sangría francesa, alineada a la izquierda."""
    return Paragraph(texto, REF)


def url(u):
    return Paragraph("<b>URL:</b> " + enlace(u), s["bullet"])


def li(texto):
    return Paragraph("•&nbsp;&nbsp;" + texto, s["bullet"])


def fig(nombre, pie, ancho=420, alto_max=330):
    ruta = os.path.join(EVID, nombre)
    n_fig[0] += 1
    texto = f"Figura {n_fig[0]}. {pie}"
    if os.path.exists(ruta):
        return figura(ruta, texto, ancho, alto_max)
    if not BORRADOR:
        sys.exit(f"Falta la captura {ruta}")
    t = Table([[f"PENDIENTE: {nombre}"]], colWidths=[ancho * 0.8], rowHeights=[min(alto_max, 160)])
    t.setStyle(TableStyle([("BOX", (0, 0), (-1, -1), 1, GRIS_CLARO), ("ALIGN", (0, 0), (-1, -1), "CENTER"),
                           ("VALIGN", (0, 0), (-1, -1), "MIDDLE")]))
    t.hAlign = "CENTER"
    return KeepTogether([t, P(texto, "bajada")])


def par(capturas):
    """Dos capturas de teléfono lado a lado."""
    # Dentro de una celda no se puede usar KeepTogether: se pasa su contenido como lista.
    celdas = [fig(n, p, ancho=200, alto_max=360)._content for n, p in capturas]
    t = Table([celdas], colWidths=[252, 252])
    t.setStyle(TableStyle([("VALIGN", (0, 0), (-1, -1), "TOP")]))
    return t


cuerpo = [
    P("1. Introducción", "h1"),
    P("Las aplicaciones nativas son el punto de partida para entender la evolución de las aplicaciones hasta llegar a las "
      "aplicaciones web progresivas (PWA). En este subproducto se define qué es una aplicación nativa, sus características y "
      "la tecnología con que se construye, y se presenta un ejemplo propio: <b>AquaTrack</b>, una app de Android escrita en "
      "Kotlin que registra el consumo diario de agua y utiliza funciones exclusivas del sistema operativo, como notificaciones "
      "locales, tareas en segundo plano y vibración. Al final se analizan tres aplicaciones nativas reales y se comparan "
      "sus ventajas y desventajas."),

    P("2. Definición", "h1"),
    P("Una <b>aplicación nativa</b> es un programa desarrollado específicamente para un sistema operativo concreto (Android o iOS), "
      "con el lenguaje y el kit de desarrollo (SDK) oficiales de esa plataforma: Kotlin o Java con el Android SDK, y Swift u "
      "Objective-C con el SDK de Apple. El código se compila para esa plataforma y se instala en el dispositivo, normalmente desde "
      "una tienda de aplicaciones como Google Play o App Store. Gracias a ello, la app accede de forma directa a las APIs del sistema "
      "y al hardware (cámara, GPS, sensores, notificaciones, almacenamiento) con el mejor rendimiento posible (Android Developers, s.f.-a)."),

    P("3. Características", "h1"),
    li("<b>Desarrollada para una sola plataforma:</b> una app de Android no se ejecuta en iOS y viceversa; cada una necesita su propio código."),
    li("<b>Lenguaje y SDK oficiales:</b> Kotlin/Java + Android SDK, o Swift + iOS SDK, con los entornos Android Studio o Xcode."),
    li("<b>Compilada e instalada en el dispositivo:</b> se distribuye como paquete (APK/AAB o IPA) por tiendas oficiales o descarga directa."),
    li("<b>Acceso completo al hardware y al sistema:</b> cámara, GPS, sensores, contactos, notificaciones, Bluetooth y almacenamiento."),
    li("<b>Alto rendimiento y fluidez:</b> se ejecuta directamente sobre el runtime del sistema (ART en Android), sin navegador."),
    li("<b>Interfaz con el aspecto del sistema:</b> sigue las guías de diseño de la plataforma (Material Design en Android)."),
    li("<b>Funciona sin conexión</b> cuando sus datos se guardan en el dispositivo."),
    li("<b>Permisos explícitos:</b> el usuario autoriza el acceso a funciones sensibles, como las notificaciones en Android 13+ "
       "(Android Developers, s.f.-d)."),

    P("4. Tecnología utilizada", "h1"),
    tabla([["Elemento", "Tecnología en AquaTrack"],
           ["Lenguaje", "Kotlin 2.0"],
           ["Interfaz", "Jetpack Compose + Material 3 (Android Developers, s.f.-b)"],
           ["SDK / plataforma", "Android SDK, minSdk 26 (Android 8.0), targetSdk 34"],
           ["Almacenamiento local", "SharedPreferences (tomas por día, meta y ajustes)"],
           ["Segundo plano", "WorkManager 2.9: tarea periódica de recordatorio (Android Developers, s.f.-c)"],
           ["APIs del sistema", "NotificationManager, permiso POST_NOTIFICATIONS, Vibrator"],
           ["Compilación", "Gradle 8.9 + Android Gradle Plugin 8.5, JDK 17"],
           ["Integración y entrega", "GitHub Actions compila el APK y lo publica en un GitHub Release"],
           ["Entorno sugerido", "Android Studio (emulador o teléfono físico)"]], [130, 374]),

    P("5. Ilustración", "h1"),
    P("La Figura 1 muestra cómo el código Kotlin se compila con Gradle hasta convertirse en un APK que se ejecuta en Android y "
      "usa directamente las APIs del sistema operativo y el hardware del teléfono. La Figura 2 muestra la pantalla principal de la app."),
    fig("fig_arquitectura.png", "Arquitectura de una app nativa: del código Kotlin a la compilación, el APK y las APIs del sistema Android.", ancho=504),
    fig("01_inicio.png", "Pantalla principal de AquaTrack (emulador Pixel 6, Android 14).", ancho=220, alto_max=400),

    P("6. Ejemplo propio: AquaTrack", "h1"),
    P("<b>Propósito.</b> Ayudar a mantener una buena hidratación: el usuario registra cada vaso de agua, ve su avance contra una meta "
      "diaria y recibe recordatorios. <b>Repositorio:</b> " + enlace(REPO) + ". <b>Descarga (APK):</b> " + enlace(RELEASE) + "."),
    P("<b>Evidencias.</b> Las capturas se tomaron instalando el APK publicado en un emulador Pixel 6 con Android 14 (API 34) en "
      "español. El recorrido se automatizó con <i>adb</i> y UI Automator en GitHub Actions (script <i>scripts/capturas.sh</i>), que "
      "además dejó un registro de las pruebas: instalación, suma y resta de tomas, felicitación, vibración registrada por el sistema, "
      "persistencia tras cerrar la app, permiso de notificaciones, tarea de WorkManager programada y notificación publicada."),
    P("Cómo funciona, paso a paso", "h2"),
    P("<b>Paso 1. Registrar agua.</b> En la pestaña <i>Hoy</i> se toca +250 ml, +500 ml u <i>Otra cantidad</i> (50–2000 ml). "
      "Cada toma se guarda con su hora en SharedPreferences y el anillo de progreso se actualiza; <i>Deshacer</i> quita la última toma."),
    P("<b>Paso 2. Cumplir la meta.</b> Al alcanzar la meta, la app hace vibrar el teléfono con la API <i>Vibrator</i> (dos pulsos "
      "de 300 ms, registrados por el servicio de vibración del sistema) y muestra una felicitación, una vez por día."),
    par([("02_registro.png", "Registro de tomas del día."), ("03_meta_alcanzada.png", "Meta alcanzada: felicitación y vibración.")]),
    P("<b>Paso 3. Consultar el historial.</b> La pestaña <i>Historial</i> muestra el total de los últimos 7 días y marca los "
      "días en que se cumplió la meta. Los datos persisten aunque se cierre la app o se reinicie el teléfono."),
    P("<b>Paso 4. Configurar meta y recordatorio.</b> En <i>Ajustes</i> se elige la meta (1000–5000 ml) y se activa el recordatorio "
      "cada 1, 2 o 3 horas. En Android 13 o superior el sistema pide el permiso de notificaciones; si se niega, la app sigue funcionando."),
    par([("04_historial.png", "Historial de los últimos 7 días."), ("05_ajustes.png", "Ajustes: meta diaria y recordatorio.")]),
    P("<b>Paso 5. Recibir el recordatorio.</b> WorkManager ejecuta una tarea en segundo plano cada cierto tiempo; si aún falta agua "
      "para la meta, publica una notificación local que abre la app al tocarla. El botón <i>Probar notificación</i> permite "
      "demostrarlo al instante."),
    par([("06_permiso.png", "Diálogo del sistema para el permiso de notificaciones."),
         ("07_notificacion.png", "Notificación local enviada con el botón Probar notificación.")]),
    fig("08_icono.png", "Icono propio de AquaTrack instalado en el cajón de aplicaciones.", ancho=220, alto_max=300),
    fig("09_release.png", "Release v1.0.0 en GitHub con el APK descargable, generado por GitHub Actions.", ancho=480),

    P("7. Ejemplos de aplicaciones nativas existentes", "h1"),
    P("WhatsApp Messenger", "h2"),
    P("Aplicación de mensajería instantánea con versiones nativas independientes para Android e iOS, distribuidas en sus tiendas "
      "oficiales. <b>Cómo funciona:</b> se instala desde Google Play, verifica el número telefónico por SMS y usa directamente la "
      "cámara, el micrófono, los contactos y las notificaciones push del sistema para enviar mensajes, fotos, notas de voz y llamadas "
      "cifradas de extremo a extremo."),
    url("https://play.google.com/store/apps/details?id=com.whatsapp"),
    P("Google Maps", "h2"),
    P("Aplicación de mapas y navegación de Google. <b>Cómo funciona:</b> obtiene la ubicación del GPS y la orientación de la brújula "
      "del teléfono, dibuja los mapas en el dispositivo, calcula rutas y da indicaciones por voz aunque la pantalla esté apagada; "
      "también permite descargar mapas para usarlos sin conexión."),
    url("https://play.google.com/store/apps/details?id=com.google.android.apps.maps"),
    P("Pixel Camera (Cámara de Google)", "h2"),
    P("Aplicación de cámara de los teléfonos Google Pixel. <b>Cómo funciona:</b> controla directamente el sensor y la lente de la "
      "cámara mediante las APIs de bajo nivel de Android y procesa las fotos en el propio dispositivo (por ejemplo, el modo nocturno "
      "y el modo retrato), algo que exige el máximo rendimiento y acceso total al hardware."),
    url("https://play.google.com/store/apps/details?id=com.google.android.GoogleCamera"),

    P("8. Ventajas y desventajas", "h1"),
    tabla([["Ventajas", "Desventajas"],
           ["Máximo rendimiento y fluidez.", "Hay que desarrollar y mantener un código distinto por plataforma (Android e iOS)."],
           ["Acceso completo al hardware y a las APIs del sistema (cámara, GPS, sensores, notificaciones).",
            "Mayor costo y tiempo de desarrollo."],
           ["Interfaz consistente con el sistema operativo.", "Se debe instalar y ocupa espacio en el dispositivo."],
           ["Funciona sin conexión.", "Publicar en tiendas implica revisión, cuotas y políticas de cada tienda."],
           ["Distribución y visibilidad en tiendas oficiales.",
            "Cada actualización requiere que el usuario descargue una nueva versión."],
           ["Seguridad reforzada por el modelo de permisos y el aislamiento (sandbox) del sistema.",
            "Requiere conocimientos específicos (Kotlin, Swift, SDK de cada plataforma)."]],
          [252, 252]),

    P("9. Conclusión", "h1"),
    P("Desarrollar AquaTrack me permitió entender en la práctica qué hace nativa a una aplicación: no es solo que se instale en el "
      "teléfono, sino que está escrita con el lenguaje y el SDK oficiales de Android y se comunica directamente con el sistema. "
      "Funciones como el recordatorio con WorkManager, la notificación local, el permiso en tiempo de ejecución y la vibración son "
      "las que dan a la app una experiencia completa y fluida, y no se logran de la misma forma desde un sitio web tradicional."),
    P("Al mismo tiempo, vi su principal limitación: este código solo sirve para Android, y para llevar AquaTrack a iPhone habría "
      "que reescribirlo en Swift. Esa desventaja es la que motiva los siguientes tipos de aplicaciones de la unidad (web, "
      "multiplataforma y, sobre todo, las PWA), que buscan acercarse a la experiencia nativa con una sola base de código."),

    P("10. Referencias", "h1"),
    R("Android Developers. (s.f.-a). <i>Platform architecture</i>. Google. " + enlace("https://developer.android.com/guide/platform")),
    R("Android Developers. (s.f.-b). <i>Jetpack Compose</i>. Google. " + enlace("https://developer.android.com/develop/ui/compose")),
    R("Android Developers. (s.f.-c). <i>Getting started with WorkManager</i>. Google. "
      + enlace("https://developer.android.com/develop/background-work/background-tasks/persistent/getting-started")),
    R("Android Developers. (s.f.-d). <i>Notification runtime permission</i>. Google. "
      + enlace("https://developer.android.com/develop/ui/views/notifications/notification-permission")),
    R("Google LLC. (s.f.-a). <i>Google Maps</i> [Aplicación móvil]. Google Play. "
      + enlace("https://play.google.com/store/apps/details?id=com.google.android.apps.maps")),
    R("Google LLC. (s.f.-b). <i>Pixel Camera</i> [Aplicación móvil]. Google Play. "
      + enlace("https://play.google.com/store/apps/details?id=com.google.android.GoogleCamera")),
    R("Serrano Arana, J. J. (2026). <i>AquaTrack</i> (Versión 1.0.0) [Software]. GitHub. " + enlace(REPO)),
    R("WhatsApp LLC. (s.f.). <i>WhatsApp Messenger</i> [Aplicación móvil]. Google Play. "
      + enlace("https://play.google.com/store/apps/details?id=com.whatsapp")),
]

nombre = "SP1_Aplicacion_Nativa_SerranoArana" + ("_BORRADOR" if BORRADOR else "") + ".pdf"
salida = os.path.join(RAIZ, "reportes", nombre)
build_pdf(salida, titulo="SUBPRODUCTO No. 1: APLICACIÓN NATIVA",
          subtitulo="Actividad Apertura · Unidad I – Introducción a aplicaciones web progresivas",
          cuerpo=cuerpo, encabezado="APLICACIONES WEB PROGRESIVAS · SUBPRODUCTO 1")
print("PDF:", salida)
