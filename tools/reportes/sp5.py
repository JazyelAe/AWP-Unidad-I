"""Genera reportes/SP5_Aplicacion_Multiplataforma_SerranoArana.pdf
Uso (desde la raíz de AWP-Unidad-I):  python tools/reportes/sp5.py"""
import os
import sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from comun import RAIZ, Reporte, P, li, R, url, tabla, enlace, build_pdf  # noqa: E402

REPO = "https://github.com/JazyelAe/ConvierteYA-Multiplataforma"
RELEASE = REPO + "/releases/tag/v1.0.1"
WEB = "https://jazyelae.github.io/ConvierteYA-Multiplataforma/"
r = Reporte("SP5")

# Las capturas web de escritorio (1280 px) dejan la app al centro con 480 px de ancho; para el reporte
# se recorta esa columna de la captura real, sin modificar su contenido.
from PIL import Image, ImageChops  # noqa: E402
for base in ("02_web_divisas", "03_web_historial", "05_web_sin_conexion"):
    im = Image.open(os.path.join(r.evid, base + ".png")).convert("RGB")
    col = im.crop((390, 0, 890, im.height))
    fondo = Image.new("RGB", col.size, col.getpixel((2, col.height - 2)))
    caja = ImageChops.difference(col, fondo).getbbox()
    col.crop((0, 0, col.width, min(col.height, caja[3] + 30))).save(os.path.join(r.evid, base + "_recorte.png"))

cuerpo = [
    P("1. Introducción", "h1"),
    P("Desarrollar la misma aplicación por separado para Android, iOS y la web implica tres equipos, tres lenguajes y tres veces el "
      "mantenimiento. Las aplicaciones multiplataforma resuelven este problema con una sola base de código que se ejecuta en varios "
      "sistemas. En este subproducto se define qué es una aplicación multiplataforma, sus características y tecnologías, y se presenta "
      "un ejemplo propio: <b>ConvierteYA</b>, un conversor de unidades y divisas escrito una sola vez en JavaScript con React Native y "
      "Expo, que se publicó como página web y como APK de Android a partir del mismo código. A diferencia del Subproducto 4, cuyo "
      "enfoque era la experiencia móvil, aquí lo importante es <b>compartir el código</b> entre plataformas."),

    P("2. Definición", "h1"),
    P("Una <b>aplicación multiplataforma</b> es una aplicación que, a partir de una misma base de código, se ejecuta en varios sistemas "
      "operativos o entornos, como Android, iOS, la web o el escritorio. Frameworks como <b>React Native</b> (JavaScript) o "
      "<b>Flutter</b> (Dart) traducen ese código a componentes o a gráficos de cada plataforma, de modo que el usuario recibe una app "
      "instalable y con apariencia propia del sistema (React Native, s.f.-a). Las diferencias inevitables entre plataformas, como un "
      "permiso o un componente que solo existe en el teléfono, se resuelven en puntos concretos del código (React Native, s.f.-b)."),

    P("3. Características", "h1"),
    li("<b>Una sola base de código:</b> la mayor parte de la lógica y de la interfaz se escribe una vez."),
    li("<b>Varios destinos:</b> el mismo proyecto genera una app de Android, una de iOS y, en algunos frameworks, una versión web."),
    li("<b>Componentes de cada plataforma:</b> React Native convierte &lt;View&gt; o &lt;Text&gt; en vistas nativas de Android o iOS, y "
       "react-native-web los convierte en HTML y CSS (Gallagher, s.f.)."),
    li("<b>Código específico cuando hace falta:</b> mediante <i>Platform.OS</i> o archivos por plataforma."),
    li("<b>Acceso a funciones del dispositivo</b> mediante módulos (portapapeles, vibración, cámara), que en la web pueden no existir."),
    li("<b>Menor costo y tiempo:</b> un equipo y un lenguaje; las correcciones llegan a todas las plataformas a la vez."),
    li("<b>Herramientas de compilación y prueba:</b> Expo Go permite probar en el teléfono sin compilar (Expo, s.f.-b)."),

    P("4. Tecnología utilizada", "h1"),
    tabla([["Elemento", "Tecnología en ConvierteYA"],
           ["Lenguaje", "JavaScript (ES2022), el mismo para todas las plataformas"],
           ["Framework", "React Native 0.88 con Expo SDK 58; react-native-web para la versión web"],
           ["Persistencia", "AsyncStorage: historial y último tipo de cambio (en la web usa localStorage)"],
           ["Módulos del dispositivo", "expo-clipboard (copiar el resultado) y expo-haptics (vibración, solo en el teléfono)"],
           ["Datos remotos", "API REST Frankfurter con los tipos de cambio del Banco Central Europeo, consultada con fetch"],
           ["Diferencias por plataforma", "Platform.OS en un solo archivo (src/plataforma.js): avisos y vibración"],
           ["Pruebas", "jest (12 pruebas de conversión), Playwright (web) y emulador Android 14 con adb"],
           ["Publicación", "GitHub Actions: expo export → GitHub Pages; expo prebuild + Gradle → APK en un Release"]],
          [130, 374]),

    P("5. Ilustración", "h1"),
    P("La Figura 1 muestra la idea central: un solo código en JavaScript pasa por React Native y Expo, y cada plataforma lo presenta "
      "con sus propios componentes. La Figura 2 compara la misma conversión ejecutándose en el navegador y en Android."),
    r.fig("fig_arquitectura.png", "Un solo código de ConvierteYA y sus tres destinos.", ancho=504),
    r.fig("11_misma_app_web_android.png", "La misma app y la misma conversión en la web (izquierda) y en Android (derecha).",
          ancho=430, alto_max=330),

    P("6. Ejemplo propio: ConvierteYA", "h1"),
    P("<b>Propósito.</b> Convertir rápidamente medidas y monedas de uso diario, como recetas en tazas, temperaturas en °F o "
      "precios en dólares, desde el teléfono o desde el navegador, con un historial de las últimas conversiones."),
    url(WEB, "Versión web"),
    url(RELEASE, "Descarga (APK)"),
    url(REPO, "Repositorio"),
    P("<b>Evidencias.</b> Las capturas web se tomaron con Chrome controlado por Playwright sobre la página publicada. Las de Android "
      "se tomaron instalando el APK del Release en un emulador Pixel 6 con Android 14 en español, dentro de GitHub Actions, con toques "
      "reales mediante <i>adb</i>. En ambas plataformas se repitieron las mismas conversiones y se compararon los resultados."),
    P("Cómo funciona, paso a paso", "h2"),
    P("<b>Paso 1. Convertir unidades.</b> Se elige la categoría (longitud, peso, temperatura o volumen), se escribe la cantidad y se "
      "seleccionan las unidades de origen y de destino. El resultado se recalcula al escribir cada número."),
    P("<b>Paso 2. Intercambiar y copiar.</b> El botón «Intercambiar» invierte origen y destino. «Copiar» coloca el texto completo "
      "(por ejemplo «37 °F = 2.77778 °C») en el portapapeles. En Android aparece un Toast nativo y el teléfono vibra; en la web, "
      "como no hay Toast ni vibración, la app dibuja su propio aviso. Es la única parte del código que cambia por plataforma."),
    "FILA_UNIDADES",
    P("<b>Paso 3. Consultar divisas.</b> Al abrir la pestaña se descargan los tipos de cambio de la API Frankfurter y se guardan en "
      "el dispositivo. La barra superior indica la fecha de los datos (la Figura 2 muestra esta pantalla en ambas plataformas)."),
    P("<b>Paso 4. Funcionar sin conexión.</b> Si no hay Internet (modo avión en Android, red desconectada en Chrome), la app usa los "
      "últimos tipos guardados y lo indica en color ámbar con «Sin conexión · tipos del dd/mm/aaaa»."),
    "FILA_DIVISAS",
    P("<b>Paso 5. Historial.</b> «Guardar en historial» conserva hasta 30 conversiones con su fecha. Persisten al recargar la página y "
      "al cerrar y volver a abrir la app, y se pueden borrar una por una o todas."),
    P("<b>Paso 6. Instalar en Android.</b> El APK se generó sin cuenta de Expo: en GitHub Actions, <i>expo prebuild</i> crea el "
      "proyecto nativo y Gradle lo compila. La app aparece con su icono propio y sigue el tema oscuro del sistema. Para iOS el código es "
      "el mismo, pero compilarlo requiere una Mac o una cuenta de Expo/Apple, por lo que <b>no se probó</b> en este trabajo."),
    "FILA_HISTORIAL",
    "FILA_ANDROID",
    P("<b>Nota sobre la versión.</b> En la primera prueba en el emulador (v1.0.0), la app decía «En línea» aunque el teléfono "
      "estaba en modo avión. La API permite guardar su respuesta en caché un día, y React Native en Android ignora la opción "
      "<i>cache: 'no-store'</i> que sí respeta el navegador. Se corrigió agregando una marca de tiempo distinta a cada consulta y se "
      "publicó la v1.0.1, que es la que se entrega y la que aparece en las capturas."),

    P("7. Ejemplos de aplicaciones multiplataforma existentes", "h1"),
    P("Discord", "h2"),
    P("Plataforma de chat de voz, video y texto. <b>Cómo funciona:</b> su app de iOS se construyó con React Native a partir del "
      "núcleo de su app de React para web y escritorio; el equipo explica que comparte una gran cantidad de código entre ambas y que, "
      "con solo tres ingenieros de iOS, logró un rendimiento que se siente nativo (Discord, 2019)."),
    url("https://play.google.com/store/apps/details?id=com.discord"),
    P("Microsoft Teams", "h2"),
    P("Herramienta de comunicación y colaboración para escuelas y empresas. <b>Cómo funciona:</b> la vitrina oficial de React Native "
      "la presenta como una de las apps de Microsoft construidas con React Native, que comparten componentes entre Android e iOS "
      "(React Native, s.f.-c)."),
    url("https://play.google.com/store/apps/details?id=com.microsoft.teams"),
    P("Google Pay", "h2"),
    P("Aplicación de pagos de Google. <b>Cómo funciona:</b> su versión para Android e iOS se reescribió completa con Flutter, el framework "
      "multiplataforma de Google, para mantener una sola base de código. Según el propio caso de éxito, el código bajó de 1.7 a 1.1 "
      "millones de líneas (35 % menos) (Flutter, s.f.)."),
    url("https://play.google.com/store/apps/details?id=com.google.android.apps.nbu.paisa.user"),

    P("8. Ventajas y desventajas", "h1"),
    tabla([["Ventajas", "Desventajas"],
           ["Un solo código y un solo lenguaje para varias plataformas.", "Las funciones muy específicas de un sistema requieren código o módulos aparte."],
           ["Menor costo y tiempo de desarrollo y mantenimiento.", "Rendimiento algo menor que el nativo en animaciones o gráficos exigentes."],
           ["Una corrección llega a todas las plataformas a la vez.", "Dependencia del framework y de sus actualizaciones (cambios entre versiones de SDK)."],
           ["Apariencia propia de cada sistema (componentes nativos).", "Algunas funciones no existen en la web (vibración, Toast) y hay que adaptarlas."],
           ["La versión web permite probarla sin instalar nada.", "Compilar para iOS sigue requiriendo una Mac o un servicio en la nube."],
           ["Gran comunidad (React y JavaScript).", "Depurar puede implicar entender capas nativas y de JavaScript."]],
          [252, 252]),

    P("9. Conclusión", "h1"),
    P("Con ConvierteYA comprobé que una sola base de código puede convertirse en una página web y en un APK de Android con "
      "resultados idénticos: las mismas conversiones dieron los mismos números en ambas plataformas. Solo tuve que separar por "
      "plataforma dos detalles, el aviso al copiar y la vibración, y todo quedó concentrado en un archivo con <i>Platform.OS</i>. Esto "
      "muestra la mayor ventaja del enfoque: escribir y corregir una vez."),
    P("También encontré sus límites. La caché de la respuesta de la API hacía que la app dijera «En línea» sin red, y la solución "
      "del navegador no funcionaba en Android: el mismo código no siempre se comporta igual por debajo. Además, iOS no pudo compilarse sin una Mac. Las PWA llevan la idea de «un solo código» todavía "
      "más lejos, porque la misma página se instala en cualquier sistema desde el navegador, como se verá en el Subproducto 7."),

    P("10. Referencias", "h1"),
    R("Discord. (2019). <i>How Discord achieves native iOS performance with React Native</i>. "
      + enlace("https://discord.com/blog/how-discord-achieves-native-ios-performance-with-react-native")),
    R("Expo. (s.f.-a). <i>Expo documentation</i>. " + enlace("https://docs.expo.dev/")),
    R("Expo. (s.f.-b). <i>Expo Go</i>. " + enlace("https://docs.expo.dev/get-started/expo-go/")),
    R("Expo. (s.f.-c). <i>Continuous Native Generation (Prebuild)</i>. " + enlace("https://docs.expo.dev/workflow/prebuild/")),
    R("Flutter. (s.f.). <i>Google Pay</i> [Caso de éxito]. Google. " + enlace("https://flutter.dev/showcase/google-pay")),
    R("Frankfurter. (s.f.). <i>Frankfurter: Exchange rates API</i>. " + enlace("https://frankfurter.dev/")),
    R("Gallagher, N. (s.f.). <i>React Native for Web</i>. " + enlace("https://necolas.github.io/react-native-web/")),
    R("React Native. (s.f.-a). <i>React Native: Learn once, write anywhere</i>. Meta. " + enlace("https://reactnative.dev/")),
    R("React Native. (s.f.-b). <i>Platform-specific code</i>. Meta. "
      + enlace("https://reactnative.dev/docs/platform-specific-code")),
    R("React Native. (s.f.-c). <i>Who's using React Native?</i> Meta. " + enlace("https://reactnative.dev/showcase")),
    R("React Native Async Storage. (s.f.). <i>Async Storage</i>. " + enlace("https://react-native-async-storage.github.io/2.0/")),
    R("Serrano Arana, J. J. (2026). <i>ConvierteYA</i> (Versión 1.0.1) [Aplicación multiplataforma]. GitHub. " + enlace(REPO)),
]

FILAS = {
    "FILA_UNIDADES": [("04_web_movil.png", "Web en vista de teléfono: 10 km = 6.21371 mi."),
                      ("06_android_unidades.png", "Android: 37 °C = 98.6 °F y Toast «Guardado»."),
                      ("06b_android_copiar.png", "Android: Toast y vista previa del portapapeles.")],
    "FILA_DIVISAS": [("02_web_divisas_recorte.png", "Divisas en la web (en línea)."),
                     ("05_web_sin_conexion_recorte.png", "Web sin conexión."),
                     ("09_android_sin_conexion.png", "Android en modo avión.")],
    "FILA_HISTORIAL": [("03_web_historial_recorte.png", "Historial en la web."),
                       ("08_android_historial.png", "Historial en Android."),
                       ("12_android_oscuro.png", "Tema oscuro del sistema en Android.")],
    "FILA_ANDROID": [("10_android_icono.png", "Icono en el cajón de apps."),
                     ("13_release.png", "Release v1.0.1 con el APK, generado por GitHub Actions.")],
}
cuerpo = [r.fila(FILAS[c], alto_max=300) if isinstance(c, str) else c for c in cuerpo]

salida = os.path.join(RAIZ, "reportes", "SP5_Aplicacion_Multiplataforma_SerranoArana.pdf")
build_pdf(salida, titulo="SUBPRODUCTO No. 5: APLICACIÓN MULTIPLATAFORMA",
          subtitulo="Actividad Desarrollo · Unidad I – Introducción a aplicaciones web progresivas",
          cuerpo=cuerpo, encabezado="APLICACIONES WEB PROGRESIVAS · SUBPRODUCTO 5")
print("PDF:", salida)
