"""Genera reportes/SP3_Aplicacion_Escritorio_SerranoArana.pdf
Uso (desde la raíz de AWP-Unidad-I):  python tools/reportes/sp3.py"""
import os
import sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from comun import RAIZ, Reporte, P, li, R, url, tabla, enlace, build_pdf  # noqa: E402

REPO = "https://github.com/JazyelAe/App_de_Escritorio"
RELEASE = REPO + "/releases/tag/v1.0.0"
r = Reporte("SP3")

cuerpo = [
    P("1. Introducción", "h1"),
    P("Las aplicaciones de escritorio son los programas que usamos todos los días en una computadora: editores, hojas de cálculo, "
      "reproductores o herramientas de diseño. En este subproducto se define qué es una aplicación de escritorio, sus características "
      "y la tecnología con que se construye, y se presenta un ejemplo propio: <b>DeskData Pro</b>, un inventario de equipo de cómputo "
      "hecho con Python y PySide6 (Qt) que se distribuye como un archivo .exe para Windows, funciona sin Internet, guarda sus datos "
      "en archivos locales y aprovecha los recursos del sistema operativo. Al final se analizan tres aplicaciones de escritorio reales."),

    P("2. Definición", "h1"),
    P("Una <b>aplicación de escritorio</b> es un programa que se instala y se ejecuta directamente en el sistema operativo de una "
      "computadora personal (Windows, macOS o Linux), dentro de su propia ventana y sin necesidad de un navegador. Utiliza los "
      "recursos locales del equipo, como el procesador, la memoria, el disco y los periféricos, y puede trabajar sin conexión a "
      "Internet porque su código y sus datos residen en la propia máquina. Se desarrolla con lenguajes y bibliotecas de interfaz "
      "gráfica como C++, C#, Java o Python con Qt (The Qt Company, s.f.)."),

    P("3. Características", "h1"),
    li("<b>Se instala o copia en la computadora</b> y se abre como cualquier programa, con su icono en el menú y en la barra de tareas."),
    li("<b>Ventana propia:</b> no depende de un navegador; usa los componentes visuales del sistema o de una biblioteca gráfica (Qt)."),
    li("<b>Funciona sin Internet:</b> el código y los datos están en el equipo."),
    li("<b>Acceso a recursos locales:</b> sistema de archivos, diálogos nativos, impresoras, CPU, memoria y disco (Rodola, s.f.)."),
    li("<b>Alto rendimiento:</b> aprovecha directamente el hardware de la computadora."),
    li("<b>Dependiente del sistema operativo:</b> el ejecutable se genera para una plataforma concreta (por ejemplo, un .exe para Windows)."),
    li("<b>Actualización manual o mediante instalador:</b> cada versión nueva debe descargarse e instalarse en cada equipo."),
    li("<b>Datos privados en el equipo:</b> la información no sale de la computadora, salvo que la app la envíe a propósito."),

    P("4. Tecnología utilizada", "h1"),
    tabla([["Elemento", "Tecnología en DeskData Pro"],
           ["Lenguaje", "Python 3.13"],
           ["Interfaz gráfica", "PySide6 6.12 (Qt 6): QMainWindow, QTableWidget, QFileDialog, QMessageBox y QPainter"],
           ["Segundo plano", "QThread con señales: actualiza las métricas sin congelar la ventana"],
           ["Recursos del equipo", "psutil 7.2: uso de CPU, memoria RAM y disco reales"],
           ["Persistencia", "Archivos JSON y CSV en la carpeta del usuario (%APPDATA%\\DeskDataPro) con respaldos"],
           ["Empaquetado", "PyInstaller 6.22 en modo --onefile --windowed: un solo DeskDataPro.exe con icono (PyInstaller, s.f.)"],
           ["Integración y entrega", "GitHub Actions en windows-latest: pruebas, empaquetado, prueba del .exe y GitHub Release"],
           ["Pruebas", "--self-test (lógica) y --capturas (abre la app y toma capturas con QWidget.grab())"]], [130, 374]),

    P("5. Ilustración", "h1"),
    P("La Figura 1 muestra la arquitectura: los módulos de la aplicación se comunican con el sistema operativo Windows (ventanas, "
      "diálogos, archivos e información del sistema), que a su vez administra el hardware de la computadora. No hay servidores ni "
      "navegador de por medio. La Figura 2 muestra la ventana principal."),
    r.fig("fig_arquitectura.png", "Arquitectura de una aplicación de escritorio: aplicación, sistema operativo y hardware local.", ancho=504),
    r.fig("01_inicio.png", "Ventana principal de DeskData Pro con el inventario.", ancho=480),

    P("6. Ejemplo propio: DeskData Pro", "h1"),
    P("<b>Propósito.</b> Llevar el control del equipo de cómputo de un laboratorio u oficina (laptops, monitores, licencias, "
      "componentes y equipo de red), saber cuánto vale el inventario y detectar a tiempo los artículos con pocas existencias."),
    url(RELEASE, "Descarga (DeskDataPro.exe)"),
    url(REPO, "Repositorio"),
    P("<b>Evidencias.</b> Las capturas se generaron con la opción <i>--capturas</i>, que abre la aplicación con datos de ejemplo en "
      "una carpeta temporal y guarda una imagen de cada vista con <i>QWidget.grab()</i>. Este mismo modo se ejecutó en GitHub "
      "Actions con el archivo DeskDataPro.exe ya empaquetado, en un Windows sin el código fuente, para comprobar que el ejecutable "
      "funciona por sí solo. La opción <i>--self-test</i> verificó la persistencia, el CSV, los filtros, el resumen y psutil."),
    P("Cómo funciona, paso a paso", "h2"),
    P("<b>Paso 1. Abrir la aplicación.</b> Al ejecutar DeskDataPro.exe aparece la ventana con cuatro indicadores: registros, unidades, "
      "valor del inventario y artículos con bajo stock. La primera vez se crea la carpeta %APPDATA%\\DeskDataPro con datos de ejemplo."),
    P("<b>Paso 2. Editar un registro.</b> Al seleccionar una fila, sus datos pasan al formulario y el título cambia a «Editando». "
      "Al guardar se actualiza la tabla y se reescribe el archivo JSON en el disco."),
    r.fig("02_formulario.png", "Edición del registro INV-005; la cantidad baja aparece resaltada en amarillo.", ancho=460),
    P("<b>Paso 3. Buscar y filtrar.</b> El buscador revisa el ID, el nombre y la ubicación, y los filtros por categoría y estado se "
      "combinan; un contador indica cuántos registros se muestran."),
    r.fig("03_busqueda.png", "Búsqueda del texto «laptop».", ancho=460),
    r.fig("04_filtro.png", "Filtro por la categoría «Periféricos».", ancho=460),
    P("<b>Paso 4. Dar de alta y eliminar.</b> El formulario valida que el ID y el nombre no estén vacíos y que el ID no se repita. "
      "Eliminar pide confirmación con un cuadro de mensaje del sistema."),
    r.fig("05_alta.png", "Alta del registro INV-013 «Impresora láser».", ancho=460),
    r.fig("06_confirmar_eliminar.png", "Cuadro de confirmación antes de eliminar.", ancho=300),
    P("<b>Paso 5. Importar y exportar archivos.</b> Los botones de CSV y JSON abren el diálogo nativo de Windows «Abrir» o "
      "«Guardar como». Antes de importar se crea un respaldo automático, y los registros se agregan o actualizan según su ID."),
    P("<b>Paso 6. Consultar el resumen.</b> La pestaña Resumen dibuja con QPainter una gráfica de barras de unidades por categoría "
      "y una tabla con el valor de cada una y su porcentaje del total."),
    r.fig("07_resumen.png", "Resumen: gráfica de unidades por categoría y valor del inventario.", ancho=460),
    P("<b>Paso 7. Ver los recursos del equipo.</b> Un hilo en segundo plano consulta cada 2 segundos el sistema operativo con psutil "
      "y muestra el uso real de CPU, memoria y disco, la ruta del archivo de datos y una bitácora de las operaciones."),
    r.fig("08_equipo.png", "Pestaña Equipo: recursos reales de la computadora y archivos locales.", ancho=460),
    r.fig("09_release.png", "Release v1.0.0 en GitHub con DeskDataPro.exe, generado por GitHub Actions.", ancho=460),
    P("<b>Paso 8. Ejecutarla en otra computadora.</b> El mismo DeskDataPro.exe se ejecutó en una máquina Windows de GitHub "
      "Actions (Windows Server 2025, 16 GB de RAM), que no tiene el código fuente: la aplicación abrió, operó con sus datos y leyó "
      "los recursos de esa otra computadora, lo que confirma que el ejecutable es independiente."),
    r.fig("10_exe_en_otra_pc.png", "DeskDataPro.exe ejecutándose en otra computadora (servidor Windows de GitHub Actions).", ancho=430),

    P("7. Ejemplos de aplicaciones de escritorio existentes", "h1"),
    P("Visual Studio Code", "h2"),
    P("Editor de código de Microsoft para Windows, macOS y Linux. <b>Cómo funciona:</b> se descarga e instala en la computadora; abre "
      "carpetas y archivos del disco, ejecuta la terminal y los compiladores instalados en el sistema y admite extensiones. Está "
      "construido con Electron, que empaqueta la interfaz como un programa de escritorio con acceso al sistema de archivos."),
    url("https://code.visualstudio.com/"),
    P("Microsoft Excel", "h2"),
    P("Hoja de cálculo de Microsoft 365. <b>Cómo funciona:</b> la versión de escritorio se instala en Windows o macOS, abre y guarda "
      "archivos .xlsx y .csv en el equipo, realiza cálculos con el procesador local y funciona sin conexión; la nube es opcional."),
    url("https://www.microsoft.com/es-mx/microsoft-365/excel"),
    P("OBS Studio", "h2"),
    P("Programa libre para grabar la pantalla y transmitir en vivo. <b>Cómo funciona:</b> captura directamente la pantalla, la cámara "
      "y el micrófono del equipo, mezcla las fuentes y codifica el video con el procesador o la tarjeta gráfica. Está escrito en "
      "C y C++, y su interfaz usa Qt, la misma biblioteca de DeskData Pro (OBS Project, s.f.-b)."),
    url("https://obsproject.com/"),

    P("8. Ventajas y desventajas", "h1"),
    tabla([["Ventajas", "Desventajas"],
           ["Funciona sin conexión a Internet.", "Hay que instalarla o copiarla en cada computadora."],
           ["Alto rendimiento y acceso directo al hardware.", "Depende del sistema operativo (un .exe solo funciona en Windows)."],
           ["Acceso completo a archivos, impresoras y periféricos.", "Las actualizaciones deben distribuirse e instalarse equipo por equipo."],
           ["Los datos permanecen en el equipo (privacidad).", "Si no se hacen respaldos, los datos se pierden con el equipo."],
           ["Interfaz rica y con respuesta inmediata.", "Ocupa espacio en disco (DeskDataPro.exe pesa unos 50 MB)."],
           ["No requiere servidor ni hosting.", "Sin firma digital, Windows SmartScreen muestra advertencias al instalar."]],
          [252, 252]),

    P("9. Conclusión", "h1"),
    P("Con DeskData Pro entendí qué distingue a una aplicación de escritorio: se ejecuta como un programa de Windows, trabaja con "
      "archivos de la propia computadora, usa diálogos nativos y puede leer el estado real del hardware, todo sin Internet. Al "
      "revisar la versión anterior descubrí que el uso de CPU mostrado era un valor fijo y que los datos se habrían perdido dentro "
      "del .exe; corregirlo con psutil y con la carpeta %APPDATA% me enseñó la importancia de probar la app tal como la usará el usuario."),
    P("También vi sus limitaciones: el ejecutable solo sirve para Windows y cada actualización debe volver a descargarse. Las "
      "aplicaciones web y las PWA resuelven precisamente la distribución y las actualizaciones, aunque con menos acceso al sistema."),

    P("10. Referencias", "h1"),
    R("Microsoft. (s.f.-a). <i>Microsoft Excel</i> [Software]. " + enlace("https://www.microsoft.com/es-mx/microsoft-365/excel")),
    R("Microsoft. (s.f.-b). <i>Visual Studio Code</i> [Software]. " + enlace("https://code.visualstudio.com/")),
    R("OBS Project. (s.f.-a). <i>OBS Studio</i> [Software]. " + enlace("https://obsproject.com/")),
    R("OBS Project. (s.f.-b). <i>obs-studio</i> [Repositorio de código]. GitHub. " + enlace("https://github.com/obsproject/obs-studio")),
    R("PyInstaller Development Team. (s.f.). <i>PyInstaller manual</i>. " + enlace("https://pyinstaller.org/en/stable/")),
    R("Rodola, G. (s.f.). <i>psutil documentation</i>. " + enlace("https://psutil.readthedocs.io/en/latest/")),
    R("Serrano Arana, J. J. (2026). <i>DeskData Pro</i> (Versión 1.0.0) [Software]. GitHub. " + enlace(REPO)),
    R("The Qt Company. (s.f.). <i>Qt for Python</i>. " + enlace("https://doc.qt.io/qtforpython-6/")),
]

salida = os.path.join(RAIZ, "reportes", "SP3_Aplicacion_Escritorio_SerranoArana.pdf")
build_pdf(salida, titulo="SUBPRODUCTO No. 3: APLICACIÓN DE ESCRITORIO",
          subtitulo="Actividad Desarrollo · Unidad I – Introducción a aplicaciones web progresivas",
          cuerpo=cuerpo, encabezado="APLICACIONES WEB PROGRESIVAS · SUBPRODUCTO 3")
print("PDF:", salida)
