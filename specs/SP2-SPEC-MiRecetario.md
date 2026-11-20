# SPEC · Mi Recetario (web) — Subproducto No. 2 "Aplicación Web"

**Materia:** Aplicaciones Web Progresivas · Unidad I · Actividad Desarrollo
**Alumno:** Jahir Jaziel Serrano Arana · 10° D
**Repositorio:** `JazyelAe/Mi_Recetario` · **App publicada:** https://jazyelae.github.io/Mi_Recetario/
**Estado:** aprobado el 20/11/2026 · implementado · probado en GitHub Pages

## 1. Objetivo
Tener una **aplicación web clásica**: se usa desde el navegador sin instalar nada, se sirve desde un servidor web (GitHub Pages) y obtiene sus datos por HTTP (un archivo JSON propio y una API pública). **No** lleva manifest ni service worker: sin conexión no carga. Esa limitación se documenta a propósito, porque es la base de la comparación con la PWA del SP7, que es la misma app evolucionada.

## 2. Auditoría del repo actual
| Elemento | Estado | Decisión |
|---|---|---|
| `index.html` (77 líneas) | Inicio con "receta del día", recetas, buscador, consejos y formulario de contacto. Semántico y en español. | Se conserva la estructura y el estilo. |
| `js/app.js` (37 líneas) | 8 recetas **escritas dentro del JS**; filtro por categoría y búsqueda por nombre o ingrediente funcionan. | Las recetas pasan a `data/recetas.json` y se cargan con `fetch`. |
| Detalle de receta | **No existe** (las tarjetas no se pueden abrir y no hay pasos de preparación). | Se agrega. |
| Datos remotos | **No hay** `fetch` ni API. | Se agrega TheMealDB. |
| Formulario | Solo validación HTML (`required`) y dice "registrada" aunque no se guarda en ningún lado. | Validación propia con mensajes por campo y un mensaje honesto. |
| Responsive | Un solo `@media`; el menú no se adapta al celular. | Menú para móvil y rejilla adaptable. |
| Manifest / service worker | No tiene (correcto para SP2). | Se mantiene así. |
| GitHub Pages | Activo y sin errores en la consola. | Se conserva. |
| README | Básico. | Se completa. |

## 3. Requisitos funcionales
- **RF-1 Catálogo con tarjetas.** 12 recetas mexicanas caseras. Cada tarjeta muestra una ilustración (emoji grande con fondo de color), el nombre, la categoría, el tiempo y la dificultad. Las recetas de TheMealDB (RF-4) se muestran con su **foto real**.
- **RF-2 Filtro y buscador.** Chips de categoría (Todas, Antojitos, Sopas, Platos fuertes, Guarniciones, Ligeros, Desayunos). El buscador filtra por **ingrediente** o nombre, sin importar acentos ni mayúsculas, y muestra un contador de resultados. Ambos se combinan.
- **RF-3 Detalle de receta.** Al tocar una tarjeta se abre una ventana (`<dialog>`) con porciones, tiempo, dificultad, lista de ingredientes y pasos numerados. La URL cambia a `#receta/<id>`, así que el enlace se puede compartir y el botón Atrás la cierra.
- **RF-4 Datos remotos.**
  - a) Las recetas propias se cargan con `fetch("data/recetas.json")`.
  - b) La sección **"Recetas del mundo"** consulta la API pública **TheMealDB**: buscar por nombre en inglés (por ejemplo *chicken* o *taco*) y ver el detalle de un platillo con foto, ingredientes, instrucciones y enlace a YouTube si existe.
  - c) Mientras se espera la respuesta se muestra un estado de carga, y si falla la red aparece un mensaje de error.
- **RF-5 Formulario de sugerencias con validación en el cliente.**
  - Reglas: nombre de 3 a 40 letras, correo con formato válido, categoría elegida de una lista y mensaje de 10 a 300 caracteres con contador.
  - Muestra mensajes de error junto a cada campo y no envía si hay errores.
  - Como no hay servidor, al enviar avisa que la sugerencia **se guardó en este navegador** (`localStorage`) y muestra cuántas lleva guardadas.
- **RF-6 Responsive.** Se ve bien en **móvil (390 px), tablet (768 px) y escritorio (1366 px)**: menú desplegable en móvil, rejilla de 1, 2 o 3–4 columnas, imágenes fluidas y textos legibles.

## 4. Requisitos no funcionales
- **RNF-1** HTML5, CSS3 y JavaScript sin frameworks ni librerías, con código comentado en español.
- **RNF-2** Rutas relativas, para que funcione en `https://jazyelae.github.io/Mi_Recetario/`.
- **RNF-3** Sin errores en la consola al cargar ni al usar la app.
- **RNF-4** Accesibilidad básica: `alt` en imágenes, etiquetas en el formulario, foco visible, el diálogo se cierra con Esc y contraste suficiente.
- **RNF-5** **Sin** `manifest.json` ni service worker.

## 5. Tecnologías
| Capa | Tecnología |
|---|---|
| Estructura | HTML5 semántico (`header`, `main`, `section`, `article`, `dialog`, `form`) |
| Estilo | CSS3: variables, Grid, Flexbox y media queries |
| Lógica | JavaScript (ES2020): `fetch`, `async/await`, DOM, `localStorage`, `hashchange` |
| Datos | `data/recetas.json` (propio) + API REST pública TheMealDB (JSON) |
| Servidor | GitHub Pages (HTTPS) |
| Capturas y pruebas | Playwright (Chromium) |

## 6. Estructura propuesta
```
index.html
css/styles.css
js/app.js          ← catálogo, filtros, búsqueda, detalle y formulario
js/mealdb.js       ← consumo de la API TheMealDB
data/recetas.json  ← 12 recetas con ingredientes y pasos
docs/capturas/
README.md · SPEC.md
```

## 7. Criterios de aceptación
| # | Criterio | Cómo se verifica |
|---|---|---|
| CA-1 | La URL de Pages carga con 0 errores en la consola. | Playwright (escucha `console` y `pageerror`) |
| CA-2 | Las recetas vienen de `data/recetas.json` (petición 200). | Registro de red en Playwright |
| CA-3 | El filtro "Sopas" muestra solo sopas; buscar "aguacate" encuentra el guacamole; buscar "jitomate" funciona igual con o sin acento. | Playwright + capturas |
| CA-4 | Al abrir una tarjeta se ven ingredientes y pasos; Esc cierra; `#receta/<id>` abre directo. | Playwright + captura |
| CA-5 | TheMealDB devuelve resultados para "chicken" y abre su detalle con foto. | Playwright + captura |
| CA-6 | El formulario rechaza datos inválidos con mensajes por campo y acepta datos válidos. | Playwright + capturas |
| CA-7 | No hay desbordamiento horizontal en 390, 768 y 1366 px. | Playwright (`scrollWidth <= innerWidth`) + capturas |
| CA-8 | **Sin conexión la app no carga** (página de error del navegador). | Playwright `set_offline(True)` + recarga + captura |
| CA-9 | No existen manifest ni service worker registrado. | Playwright |
| CA-10 | README con capturas y enlace. | Revisar el repo |

## 8. Plan de despliegue
GitHub Pages ya está activo (rama `main`, carpeta raíz). Cada push publica la nueva versión. **URL de la aplicación:** https://jazyelae.github.io/Mi_Recetario/

## 9. Capturas (todas automáticas con Playwright, sin pedirte nada)
Escritorio 1366×768: `01_inicio.png`, `02_filtro_sopas.png`, `03_busqueda_aguacate.png`, `04_detalle.png`, `05_mealdb.png`, `06_formulario_errores.png`, `07_formulario_ok.png`, `08_sin_conexion.png`.
Móvil 390×844: `09_movil_inicio.png`, `10_movil_menu.png`, `11_movil_detalle.png`.
Además: diagrama **navegador ⇄ GitHub Pages ⇄ datos (recetas.json / TheMealDB)**.

## 10. Ejemplos reales propuestos (URL comprobadas el 20/11/2026)
| App | Por qué es web | URL |
|---|---|---|
| Gmail | Cliente de correo que corre en el navegador; los datos viven en servidores de Google y se sincronizan por HTTP. | https://mail.google.com/ |
| Documentos de Google | Editor de textos en el navegador con guardado automático en la nube y edición colaborativa en tiempo real. | https://www.google.com/docs/about/ |
| Wikipedia | Sitio y app web de contenido; cada página se genera en el servidor (MediaWiki) y se consulta desde cualquier navegador. | https://es.wikipedia.org/ |

Fuentes técnicas (comprobadas): MDN — *Cómo funciona la web*, *Fetch API* y *Diseño web adaptable*; GitHub Docs — *¿Qué es GitHub Pages?*; documentación de la API de TheMealDB.

## 11. Pruebas
Automatizadas con Playwright + Google Chrome contra la URL pública (`tools/pruebas_sp2.py` del repo AWP-Unidad-I), 20/11/2026. Resultado: **9/9 + README**.

| # | Resultado | Evidencia |
|---|---|---|
| CA-1 | ✅ 0 errores en consola (se agregó favicon para evitar el 404 de `favicon.ico`). | registro de la prueba |
| CA-2 | ✅ `data/recetas.json` respondió 200 y se pintaron 12 tarjetas. | `01_inicio.png` |
| CA-3 | ✅ "Sopas" → Sopa de lentejas y Caldo de pollo; "aguacate" → Guacamole clásico; "jitomate" y "JITÓMATE" → 4 resultados. | `02_filtro_sopas.png`, `03_busqueda_aguacate.png` |
| CA-4 | ✅ Detalle con 6 ingredientes y 5 pasos, URL `#receta/tacos-de-papa`; Esc cierra; `#receta/guacamole` abre directo. | `04_detalle.png`, `11_movil_detalle.png` |
| CA-5 | ✅ TheMealDB respondió 200: 25 resultados para "chicken"; detalle "Chicken Handi" con foto. | `05_mealdb.png`, `05b_mealdb_detalle.png` |
| CA-6 | ✅ Con datos inválidos marca 4 errores; con datos válidos guarda y agradece. | `06_formulario_errores.png`, `07_formulario_ok.png` |
| CA-7 | ✅ Sin desbordamiento horizontal en 1366, 768 y 390 px. | `09`–`12` |
| CA-8 | ✅ Sin conexión, la recarga falla con `ERR_INTERNET_DISCONNECTED` y Chrome muestra su página de error. | `08_sin_conexion.png` |
| CA-9 | ✅ 0 manifest y 0 service workers registrados. | registro de la prueba |
| CA-10 | ✅ README con capturas y enlace. | README.md |
