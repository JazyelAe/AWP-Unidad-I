"""Genera reportes/SP4_Aplicacion_Movil_SerranoArana.pdf
Uso (desde la raíz de AWP-Unidad-I):  python tools/reportes/sp4.py"""
import os
import sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from comun import RAIZ, Reporte, P, li, R, url, tabla, enlace, build_pdf  # noqa: E402

REPO = "https://github.com/JazyelAe/MisPendientes-Movil"
RELEASE = REPO + "/releases/tag/v1.0.1"
WEB = "https://jazyelae.github.io/MisPendientes-Movil/"
r = Reporte("SP4")

cuerpo = [
    P("1. Introducción", "h1"),
    P("El teléfono celular es hoy el dispositivo más usado para acceder a servicios digitales, y las aplicaciones móviles están "
      "diseñadas específicamente para él: pantallas pequeñas, uso con una mano, interacción táctil y acceso a capacidades como "
      "notificaciones, vibración, cámara o GPS. En este subproducto se define qué es una aplicación móvil, sus características y la "
      "tecnología con que se construye, y se presenta un ejemplo propio: <b>Mis Pendientes</b>, un gestor de tareas hecho con Flutter "
      "que se instala como APK en Android, se maneja con gestos y envía recordatorios. Se distingue del Subproducto 1 (app nativa "
      "programada con el SDK de Android) porque aquí el enfoque está en la experiencia móvil, y del Subproducto 5 (multiplataforma), "
      "cuyo enfoque es compartir un solo código entre sistemas."),

    P("2. Definición", "h1"),
    P("Una <b>aplicación móvil</b> es un programa diseñado para ejecutarse en dispositivos portátiles como teléfonos inteligentes y "
      "tabletas. Se instala desde una tienda (Google Play, App Store) o mediante un paquete (APK en Android), y su interfaz está "
      "pensada para pantallas táctiles pequeñas. Aprovecha las capacidades del dispositivo, como notificaciones, sensores, cámara, "
      "ubicación y almacenamiento local, y suele funcionar total o parcialmente sin conexión. Puede desarrollarse de forma nativa "
      "(Kotlin, Swift) o con frameworks como Flutter, que compilan a código nativo del teléfono (Flutter, s.f.)."),

    P("3. Características", "h1"),
    li("<b>Diseño para pantalla pequeña:</b> una columna, botones grandes y acciones principales al alcance del pulgar."),
    li("<b>Interacción táctil y gestos:</b> tocar, deslizar, mantener presionado, pellizcar y jalar para actualizar (Android Developers, s.f.)."),
    li("<b>Acceso a capacidades del teléfono:</b> notificaciones, vibración, cámara, GPS, micrófono y sensores."),
    li("<b>Instalación en el dispositivo:</b> desde una tienda de aplicaciones o un APK; tiene su icono en el teléfono."),
    li("<b>Uso sin conexión:</b> guarda datos localmente y se sincroniza cuando hay red."),
    li("<b>Permisos explícitos:</b> el usuario autoriza funciones sensibles, como las notificaciones en Android 13 o superior."),
    li("<b>Sesiones cortas y frecuentes:</b> pensada para usarse muchas veces al día durante poco tiempo, con recordatorios que invitan a volver."),
    li("<b>Consumo eficiente:</b> cuida la batería y los datos (por ejemplo, recordatorios inexactos agrupados por el sistema)."),

    P("4. Tecnología utilizada", "h1"),
    tabla([["Elemento", "Tecnología en Mis Pendientes"],
           ["Lenguaje y framework", "Dart 3.13 con Flutter 3.47: la interfaz se compila a código ARM nativo para Android"],
           ["Interfaz", "Material 3 (Material Design, s.f.): botón flotante, hoja inferior, ChoiceChip, SegmentedButton, modo oscuro"],
           ["Gestos", "Dismissible (deslizar), onLongPress (mantener presionado) y RefreshIndicator (jalar para actualizar)"],
           ["Persistencia", "shared_preferences: las tareas se guardan en formato JSON en el teléfono"],
           ["Notificaciones", "flutter_local_notifications + timezone: recordatorio a las 9:00 del día límite y notificación de prueba"],
           ["Háptica", "HapticFeedback: vibración corta al completar, borrar y mantener presionado"],
           ["Icono", "flutter_launcher_icons: icono adaptativo para Android y para la demo web"],
           ["Integración y entrega", "GitHub Actions: flutter analyze, flutter test, APK en un Release y demo web en GitHub Pages"],
           ["Pruebas en dispositivo", "Emulador Pixel 6 con Android 14 en GitHub Actions, manejado con adb"]], [130, 374]),

    P("5. Ilustración", "h1"),
    P("La Figura 1 resume el funcionamiento: los gestos del usuario llegan a los widgets de Flutter, la lógica de la app actualiza la "
      "lista y, según la acción, usa los servicios del teléfono: notificaciones, vibración y almacenamiento local. La Figura 2 muestra "
      "la pantalla principal en el teléfono."),
    r.fig("fig_arquitectura.png", "Interacción táctil, app Flutter y capacidades del teléfono.", ancho=504),
    r.fig("01_lista.png", "Pantalla principal de Mis Pendientes (emulador Pixel 6, Android 14).", ancho=200, alto_max=380),

    P("6. Ejemplo propio: Mis Pendientes", "h1"),
    P("<b>Propósito.</b> Organizar tareas personales y escolares desde el celular: anotarlas rápido, saber cuáles vencen pronto y "
      "recibir un aviso el día límite."),
    url(RELEASE, "Descarga (APK)"),
    url(WEB, "Demo web"),
    url(REPO, "Repositorio"),
    P("<b>Evidencias.</b> Las capturas de Android se tomaron instalando el APK publicado en un emulador Pixel 6 con Android 14 en "
      "español, dentro de GitHub Actions. Los gestos se ejecutaron como toques reales con <i>adb</i> (<i>input motionevent</i> permite "
      "detener el dedo a mitad del deslizamiento para fotografiarlo). Además, <i>flutter test</i> verifica el alta, los dos "
      "deslizamientos, el botón Deshacer, la edición con pulsación larga y que los datos se guarden."),
    P("Cómo funciona, paso a paso", "h2"),
    P("<b>Paso 1. Crear una tarea.</b> El botón flotante «Nueva tarea» abre una hoja inferior con título, nota, prioridad y fecha "
      "límite; la fecha se elige con el calendario de Material en español."),
    r.fila([("02_nueva_tarea.png", "Hoja para crear una tarea."),
            ("03_selector_fecha.png", "Selector de fecha límite.")], alto_max=330),
    P("<b>Paso 2. Deslizar a la derecha para completar.</b> Al deslizar aparece un fondo verde con «Completar»; al soltar, la tarea "
      "se tacha y baja al final de la lista, y el teléfono vibra brevemente."),
    P("<b>Paso 3. Deslizar a la izquierda para borrar.</b> El fondo cambia a rojo; al soltar, la tarea desaparece y una barra inferior "
      "ofrece «Deshacer» para recuperarla."),
    r.fila([("04_deslizar_completar.png", "Deslizar a la derecha (gesto real detenido a la mitad)."),
            ("05a_deslizar_borrar.png", "Deslizar a la izquierda para borrar."),
            ("05_borrar_deshacer.png", "Tarea borrada con opción «Deshacer».")], alto_max=300),
    P("<b>Paso 4. Mantener presionado para editar.</b> Una pulsación larga abre la misma hoja con los datos de la tarea, "
      "acompañada de una vibración corta."),
    P("<b>Paso 5. Ordenar, filtrar y actualizar.</b> El menú permite ordenar por fecha, prioridad o recientes; los filtros muestran "
      "todas, pendientes, completadas o vencidas (en rojo). Jalar la lista hacia abajo la vuelve a leer del almacenamiento."),
    r.fila([("06_editar.png", "Edición con pulsación larga."),
            ("07_orden_prioridad.png", "Orden por prioridad."),
            ("07b_filtro_vencidas.png", "Filtro «Vencidas».")], alto_max=300),
    P("<b>Paso 6. Recibir notificaciones.</b> Cada tarea con fecha límite programa un recordatorio a las 9:00 de ese día. En Ajustes, "
      "«Probar notificación» solicita el permiso de Android 13+ y muestra un aviso inmediato en la barra del sistema."),
    r.fila([("09a_permiso.png", "Permiso de notificaciones."),
            ("09_notificacion.png", "Notificación en la barra del sistema."),
            ("12_jalar_actualizar.png", "Lista tras jalar para actualizar.")], alto_max=300),
    P("<b>Paso 7. Personalizar y usar en cualquier lugar.</b> La app sigue el modo oscuro del sistema o se elige en Ajustes, tiene su "
      "propio icono y conserva los datos aunque se cierre. La demo web permite verla desde el navegador en tamaño de celular."),
    r.fila([("08_modo_oscuro.png", "Modo oscuro."),
            ("10_icono.png", "Icono en el cajón de apps."),
            ("11_web_movil.png", "Demo web en vista móvil.")], alto_max=300),
    r.fig("13_release.png", "Release v1.0.1 en GitHub con el APK, generado por GitHub Actions.", ancho=440),
    P("<b>Nota sobre la versión.</b> La primera versión publicada (v1.0.0) se quedaba en la pantalla de arranque: al compilar en modo "
      "<i>release</i>, Android eliminó el icono de la notificación porque solo se nombraba como texto desde Dart. Se detectó en la "
      "prueba con el emulador, se corrigió y se publicó la v1.0.1, que es la que se entrega."),

    P("7. Ejemplos de aplicaciones móviles existentes", "h1"),
    P("Instagram", "h2"),
    P("Red social para compartir fotos y videos. <b>Cómo funciona:</b> usa la cámara del teléfono para tomar y editar contenido al "
      "instante; la navegación se basa en gestos (deslizar entre historias, doble toque para «me gusta») y las notificaciones push "
      "avisan de mensajes y reacciones."),
    url("https://play.google.com/store/apps/details?id=com.instagram.android"),
    P("Uber", "h2"),
    P("Plataforma de transporte y entregas. <b>Cómo funciona:</b> obtiene la ubicación del GPS para fijar el punto de partida, muestra "
      "en un mapa al conductor en tiempo real, cobra con el método de pago guardado y envía notificaciones del estado del viaje; "
      "solo tiene sentido en un dispositivo que el usuario lleva consigo."),
    url("https://play.google.com/store/apps/details?id=com.ubercab"),
    P("Duolingo", "h2"),
    P("Aplicación para aprender idiomas. <b>Cómo funciona:</b> divide el aprendizaje en lecciones cortas que se completan con toques, "
      "usa el micrófono para ejercicios de pronunciación y envía recordatorios diarios para mantener la racha, aprovechando el uso "
      "frecuente del teléfono."),
    url("https://play.google.com/store/apps/details?id=com.duolingo"),

    P("8. Ventajas y desventajas", "h1"),
    tabla([["Ventajas", "Desventajas"],
           ["Siempre a la mano: el usuario lleva el teléfono a todas partes.", "Pantalla pequeña: limita la cantidad de información visible."],
           ["Gestos táctiles naturales y rápidos.", "Hay que adaptar el diseño a muchos tamaños y versiones de Android."],
           ["Acceso a notificaciones, vibración, cámara, GPS y sensores.", "Depende de permisos que el usuario puede negar."],
           ["Funciona sin conexión con datos locales.", "Consumo de batería, almacenamiento y datos móviles."],
           ["Notificaciones que invitan a volver a la app.", "Instalar desde un APK requiere permitir orígenes desconocidos."],
           ["Distribución masiva en tiendas de aplicaciones.", "Publicar en tiendas implica revisión, cuotas y políticas."]],
          [252, 252]),

    P("9. Conclusión", "h1"),
    P("Desarrollar Mis Pendientes me hizo pensar primero en cómo se usa un teléfono: con el pulgar, en momentos cortos y esperando "
      "que la app avise sin tener que abrirla. Los gestos de deslizar, la pulsación larga y el jalar para actualizar hacen que las "
      "acciones sean rápidas, y las notificaciones y la vibración aprovechan capacidades que una página web tradicional no tiene. "
      "Flutter me permitió lograrlo con un solo lenguaje y compilar un APK real con GitHub Actions."),
    P("También aprendí que lo móvil depende de detalles del sistema: el permiso de notificaciones de Android 13, la versión de "
      "compilación que exigen las librerías y las pruebas en un emulador. Las PWA buscan llevar parte de esta experiencia "
      "(instalación, notificaciones, uso sin conexión) a la web, como se verá en el Subproducto 7."),

    P("10. Referencias", "h1"),
    R("Android Developers. (s.f.). <i>Use touch gestures</i>. Google. "
      + enlace("https://developer.android.com/develop/ui/views/touch-and-input/gestures")),
    R("Duolingo. (s.f.). <i>Duolingo: Learn Languages</i> [Aplicación móvil]. Google Play. "
      + enlace("https://play.google.com/store/apps/details?id=com.duolingo")),
    R("Flutter. (s.f.). <i>Flutter documentation</i>. Google. " + enlace("https://docs.flutter.dev/")),
    R("Instagram. (s.f.). <i>Instagram</i> [Aplicación móvil]. Google Play. "
      + enlace("https://play.google.com/store/apps/details?id=com.instagram.android")),
    R("Material Design. (s.f.). <i>Material Design 3</i>. Google. " + enlace("https://m3.material.io/")),
    R("Pub.dev. (s.f.-a). <i>flutter_local_notifications</i> [Paquete de Flutter]. "
      + enlace("https://pub.dev/packages/flutter_local_notifications")),
    R("Pub.dev. (s.f.-b). <i>shared_preferences</i> [Paquete de Flutter]. " + enlace("https://pub.dev/packages/shared_preferences")),
    R("Serrano Arana, J. J. (2026). <i>Mis Pendientes</i> (Versión 1.0.1) [Aplicación móvil]. GitHub. " + enlace(REPO)),
    R("Uber Technologies. (s.f.). <i>Uber</i> [Aplicación móvil]. Google Play. "
      + enlace("https://play.google.com/store/apps/details?id=com.ubercab")),
]

salida = os.path.join(RAIZ, "reportes", "SP4_Aplicacion_Movil_SerranoArana.pdf")
build_pdf(salida, titulo="SUBPRODUCTO No. 4: APLICACIÓN MÓVIL",
          subtitulo="Actividad Desarrollo · Unidad I – Introducción a aplicaciones web progresivas",
          cuerpo=cuerpo, encabezado="APLICACIONES WEB PROGRESIVAS · SUBPRODUCTO 4")
print("PDF:", salida)
