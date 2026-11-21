"""Genera reportes/SP6_Aplicacion_Servicios_SerranoArana.pdf
Uso (desde la raíz de AWP-Unidad-I):  python tools/reportes/sp6.py"""
import os
import sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from comun import RAIZ, Reporte, P, li, R, url, tabla, enlace, build_pdf  # noqa: E402

REPO = "https://github.com/JazyelAe/BiblioServ-Servicios"
CLIENTE = "https://jazyelae.github.io/BiblioServ-Servicios/"
E2E = REPO + "/actions/workflows/extremo.yml"
r = Reporte("SP6")

cuerpo = [
    P("1. Introducción", "h1"),
    P("Muchas aplicaciones actuales no son un solo programa, sino un conjunto de servicios que se comunican entre sí por la red: "
      "uno autentica a los usuarios, otro guarda los datos, otro cobra y otros más se contratan a terceros, como mapas o pagos. En "
      "este subproducto se define qué es una aplicación orientada a servicios, sus características y tecnologías, y se presenta un "
      "ejemplo propio: <b>BiblioServ</b>, una biblioteca escolar formada por un servicio de autenticación, un servicio de catálogo, "
      "el consumo de un servicio externo (Open Library) y un cliente web separado. Todos se comunican por HTTP con mensajes JSON."),

    P("2. Definición", "h1"),
    P("Una <b>aplicación orientada a servicios</b> es aquella cuya funcionalidad se divide en servicios independientes, cada uno con "
      "una responsabilidad concreta y una interfaz bien definida (normalmente una API REST sobre HTTP), que otros programas consumen "
      "sin conocer su implementación interna. Cuando los servicios son pequeños y se despliegan por separado se habla de "
      "<b>microservicios</b>: componentes independientes que se comunican mediante APIs ligeras (Amazon Web Services, s.f.). Los "
      "servicios pueden ser propios o externos, contratados a otra organización."),

    P("3. Características", "h1"),
    li("<b>Responsabilidad única por servicio:</b> autenticación, catálogo, pagos, búsqueda, etcétera."),
    li("<b>Comunicación por la red con un formato estándar:</b> HTTP con JSON (REST) y códigos de estado como 200, 201, 401 o 404."),
    li("<b>Contrato explícito:</b> los endpoints se documentan (por ejemplo, con OpenAPI/Swagger) para que otros los consuman (SmartBear, s.f.)."),
    li("<b>Bajo acoplamiento:</b> el cliente no conoce la base de datos; un servicio puede cambiar por dentro sin afectar a los demás."),
    li("<b>Reutilización de servicios externos:</b> se integran APIs de terceros en lugar de construir todo."),
    li("<b>Seguridad en cada llamada:</b> tokens en el encabezado <i>Authorization</i> y reglas CORS para los navegadores (MDN, s.f.)."),
    li("<b>Despliegue y escalado independientes:</b> cada servicio puede ejecutarse en su propio servidor o en varias copias."),

    P("4. Tecnología utilizada", "h1"),
    tabla([["Elemento", "Tecnología en BiblioServ"],
           ["Servicios propios", "Python 3.12 con Flask 3.1; cada servicio es un blueprint en su propio archivo (Pallets, s.f.-a)"],
           ["Autenticación", "Tokens firmados con itsdangerous que caducan en 8 horas (Pallets, s.f.-b)"],
           ["Datos", "SQLite: tabla de libros que se crea y se llena con 5 ejemplos al arrancar"],
           ["Servicio externo", "API REST de Open Library, consultada desde el servidor con requests (Internet Archive, s.f.)"],
           ["Cliente", "HTML, CSS y JavaScript con fetch, publicado en GitHub Pages"],
           ["Seguridad web", "flask-cors: solo el cliente de Pages y localhost pueden llamar a la API desde el navegador"],
           ["Documentación", "OpenAPI 3 escrita a mano y Swagger UI en /docs"],
           ["Servidor de producción", "gunicorn (probado en Linux dentro de GitHub Actions)"],
           ["Pruebas", "pytest (14 pruebas) y Playwright (15 comprobaciones de extremo a extremo)"]],
          [130, 374]),

    P("5. Ilustración", "h1"),
    P("La Figura 1 muestra la arquitectura: el cliente web solo habla con la API por HTTP/JSON; dentro de la API, cada servicio "
      "tiene sus propios endpoints, y el servicio de consumo externo, a su vez, es cliente de Open Library. La Figura 2 es la "
      "respuesta JSON real del servicio de catálogo."),
    r.fig("fig_arquitectura.png", "Servicios de BiblioServ y cómo se comunican.", ancho=504),
    r.fig("07_json_libros.png", "Respuesta JSON de GET /api/libros vista en el navegador.", ancho=380, alto_max=300),

    P("6. Ejemplo propio: BiblioServ", "h1"),
    P("<b>Propósito.</b> Administrar el catálogo y los préstamos de una biblioteca escolar: cualquiera puede consultar los libros, "
      "pero solo el bibliotecario, con su token, puede agregarlos, editarlos, prestarlos o borrarlos. Para dar de alta un libro, los "
      "datos se pueden traer de Open Library en lugar de capturarlos a mano."),
    url(CLIENTE, "Cliente web"),
    url(REPO, "Repositorio"),
    url(E2E, "Prueba de extremo a extremo"),
    P("<b>Sobre el despliegue.</b> La API <b>no se publicó en un hosting</b>: se decidió no crear una cuenta en Render. El cliente "
      "publicado en GitHub Pages se conecta a la API que se ejecuta en la computadora con <i>python app.py</i> (Chrome pide permiso de "
      "«red local» la primera vez). Además, en cada cambio, GitHub Actions levanta la API con gunicorn, el servidor de producción, y "
      "recorre el cliente con Chrome. Ambas pruebas dieron 15 de 15 comprobaciones correctas."),
    P("Servicios y endpoints", "h2"),
    tabla([["Servicio", "Método y ruta", "Token", "Respuestas"],
           ["Autenticación", "POST /api/login", "No", "200 · 401"],
           ["Autenticación", "GET /api/perfil", "Sí", "200 · 401"],
           ["Catálogo", "GET /api/libros?q=", "No", "200"],
           ["Catálogo", "GET /api/libros/{id}", "No", "200 · 404"],
           ["Catálogo", "POST /api/libros", "Sí", "201 · 400 · 401"],
           ["Catálogo", "PUT /api/libros/{id}", "Sí", "200 · 400 · 401 · 404"],
           ["Catálogo", "DELETE /api/libros/{id}", "Sí", "204 · 401 · 404"],
           ["Externo", "GET /api/externo/buscar?q=", "No", "200 · 400 · 502"]],
          [100, 190, 50, 164]),
    P("Cómo funciona, paso a paso", "h2"),
    P("<b>Paso 1. Consultar sin sesión.</b> Al abrir el cliente, este comprueba que la API responda y pide la lista al servicio de "
      "catálogo, que es pública. Si la API no está en ejecución, el cliente lo indica y explica cómo iniciarla."),
    "FILA_INICIO",
    P("<b>Paso 2. Iniciar sesión.</b> El cliente envía usuario y contraseña a <i>POST /api/login</i>; el servicio de autenticación "
      "responde con un token firmado. Desde ese momento el cliente lo envía en cada escritura y aparecen los botones de acción."),
    P("<b>Paso 3. Buscar en Open Library.</b> El bibliotecario escribe un título o un ISBN. La API consulta Open Library, simplifica "
      "su respuesta (título, autor, año, ISBN y portada) y el botón «Usar estos datos» llena el formulario."),
    "FILA_SESION",
    P("<b>Paso 4. Alta, edición, préstamo y borrado.</b> Cada acción es una petición HTTP distinta: POST para dar de alta (201), PUT "
      "para editar o cambiar el estado a «Prestado» y DELETE para borrar (204). La Figura 9 muestra las peticiones que registró "
      "gunicorn durante la prueba en GitHub Actions, incluidas las peticiones OPTIONS que el navegador hace antes por CORS."),
    "FILA_CRUD",
    "FIG_REGISTRO",
    P("<b>Paso 5. Seguridad: sin token no hay escritura.</b> Si el token falta, es falso o caducó, el servicio responde 401 y el "
      "cliente pide iniciar sesión otra vez. La Figura 10 muestra el cliente con un token falsificado."),
    P("<b>Paso 6. Documentación del contrato.</b> Swagger UI, en <i>/docs</i>, muestra los ocho endpoints y permite probarlos desde "
      "el navegador, incluido el botón «Authorize» para pegar el token."),
    "FILA_DOCS",

    P("7. Ejemplos de aplicaciones orientadas a servicios", "h1"),
    P("Netflix", "h2"),
    P("Plataforma de streaming. <b>Cómo funciona:</b> en 2008 comenzó a migrar su servicio de una aplicación Java monolítica en su "
      "propio centro de datos a microservicios en la nube de AWS. Esa arquitectura permite que sus equipos trabajen y publiquen "
      "cambios de forma independiente (Netflix Technology Blog, 2016)."),
    url("https://netflixtechblog.com/how-we-build-code-at-netflix-c5d9bd727f15"),
    P("Mercado Pago (API de pagos)", "h2"),
    P("Servicio de pagos de Mercado Libre que otras tiendas y aplicaciones integran. <b>Cómo funciona:</b> ofrece una API REST en "
      "<i>api.mercadopago.com</i> con endpoints GET, POST, PUT y DELETE; cada petición se autentica con un <i>Access Token</i> en el "
      "encabezado <i>Authorization: Bearer</i>, el mismo esquema que usa BiblioServ (Mercado Pago, s.f.)."),
    url("https://www.mercadopago.com.mx/developers/es/reference"),
    P("Google Maps Platform", "h2"),
    P("Conjunto de servicios de mapas de Google. <b>Cómo funciona:</b> las aplicaciones no construyen sus propios mapas, sino que "
      "consumen servicios separados por función: Maps (mapas), Routes (rutas), Places (lugares y geocodificación) y otros, mediante "
      "servicios web y SDK (Google, s.f.)."),
    url("https://developers.google.com/maps"),

    P("8. Ventajas y desventajas", "h1"),
    tabla([["Ventajas", "Desventajas"],
           ["Cada servicio se desarrolla, prueba y cambia por separado.", "Más piezas que configurar, desplegar y vigilar."],
           ["Se reutilizan servicios externos (Open Library, pagos, mapas).", "Dependencia de servicios de terceros: si fallan, hay que manejar el error (502)."],
           ["Cualquier cliente (web, móvil, otra API) usa el mismo servicio.", "La red añade latencia y posibles fallos en cada llamada."],
           ["Escalado independiente del servicio más usado.", "Seguridad en cada punto: tokens, CORS, validación."],
           ["Contrato claro y documentado (OpenAPI).", "Publicar la API requiere un servidor o hosting (aquí no se publicó)."],
           ["Equipos pueden trabajar en paralelo.", "Depurar un error puede implicar seguir la petición entre varios servicios."]],
          [252, 252]),

    P("9. Conclusión", "h1"),
    P("BiblioServ me mostró que separar responsabilidades simplifica cada parte: el cliente no sabe nada de SQLite ni de Open "
      "Library, solo de endpoints y códigos de estado; la autenticación es un servicio que los demás usan con un decorador; y "
      "traer datos de un servicio externo me ahorró capturar información a mano. Documentar el contrato con OpenAPI y probarlo con "
      "pytest y con el navegador dio confianza en que cada servicio cumple lo que promete."),
    P("También aprendí sus costos: hubo que configurar CORS (el navegador hace peticiones OPTIONS antes de cada llamada), manejar "
      "fallas del servicio externo y decidir dónde ejecutar la API. Al no usar un hosting, la API corre en la computadora y en "
      "GitHub Actions. Las PWA también son clientes de servicios como este, con la ventaja de funcionar sin conexión, como se verá "
      "en el Subproducto 7."),

    P("10. Referencias", "h1"),
    R("Amazon Web Services. (s.f.). <i>What are microservices?</i> " + enlace("https://aws.amazon.com/microservices/")),
    R("Google. (s.f.). <i>Google Maps Platform</i>. Google for Developers. " + enlace("https://developers.google.com/maps")),
    R("Internet Archive. (s.f.). <i>Open Library search API</i>. Open Library. "
      + enlace("https://openlibrary.org/dev/docs/api/search")),
    R("Mercado Pago. (s.f.). <i>API reference</i>. Mercado Pago Developers. "
      + enlace("https://www.mercadopago.com.mx/developers/es/reference")),
    R("MDN Web Docs. (s.f.). <i>Intercambio de recursos de origen cruzado (CORS)</i>. Mozilla. "
      + enlace("https://developer.mozilla.org/es/docs/Web/HTTP/Guides/CORS")),
    R("Netflix Technology Blog. (2016, 9 de marzo). <i>How we build code at Netflix</i>. "
      + enlace("https://netflixtechblog.com/how-we-build-code-at-netflix-c5d9bd727f15")),
    R("Pallets. (s.f.-a). <i>Modular applications with blueprints</i>. Flask documentation. "
      + enlace("https://flask.palletsprojects.com/en/stable/blueprints/")),
    R("Pallets. (s.f.-b). <i>ItsDangerous</i>. " + enlace("https://itsdangerous.palletsprojects.com/")),
    R("Serrano Arana, J. J. (2026). <i>BiblioServ</i> [Aplicación orientada a servicios]. GitHub. " + enlace(REPO)),
    R("SmartBear. (s.f.). <i>OpenAPI specification</i>. Swagger. " + enlace("https://swagger.io/specification/")),
]

FILAS = {
    "FILA_INICIO": [("01_login.png", "Cliente en Pages: lista pública y formulario de inicio de sesión."),
                    ("09_sin_api.png", "Aviso cuando la API no está en ejecución.")],
    "FILA_SESION": [("02_lista.png", "Sesión iniciada: aparecen las acciones."),
                    ("04_busqueda_openlibrary.png", "Resultados de Open Library (servicio externo).")],
    "FILA_CRUD": [("03_alta.png", "Libro dado de alta con datos de Open Library."),
                  ("05_editar.png", "Edición del libro.")],
    "FILA_DOCS": [("06_sin_token_401.png", "Token falsificado: el servicio responde 401."),
                  ("08_swagger.png", "Swagger UI con los 8 endpoints.")],
}


def armar(c):
    """Las figuras se crean aquí, en orden de aparición, para que la numeración sea correcta."""
    if c == "FIG_REGISTRO":
        return r.fig("11_registro_peticiones.png",
                     "Registro real de gunicorn: método, ruta y código de cada petición del cliente.", ancho=330, alto_max=330)
    return r.fila(FILAS[c], alto_max=260) if isinstance(c, str) else c


cuerpo = [armar(c) for c in cuerpo]

salida = os.path.join(RAIZ, "reportes", "SP6_Aplicacion_Servicios_SerranoArana.pdf")
build_pdf(salida, titulo="SUBPRODUCTO No. 6: APLICACIÓN ORIENTADA A SERVICIOS",
          subtitulo="Actividad Desarrollo · Unidad I – Introducción a aplicaciones web progresivas",
          cuerpo=cuerpo, encabezado="APLICACIONES WEB PROGRESIVAS · SUBPRODUCTO 6")
print("PDF:", salida)
