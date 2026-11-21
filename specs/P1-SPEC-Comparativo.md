# SPEC · Producto No. 1 — Reporte comparativo de tipos de aplicaciones

**Materia:** Aplicaciones Web Progresivas · Unidad I
**Alumno:** Jahir Jaziel Serrano Arana · 10° D
**Repositorio:** `JazyelAe/AWP-Unidad-I` (central)
**Archivo:** `reportes/P1_Reporte_Comparativo_SerranoArana.pdf`
**Estado:** aprobado el 20/11/2026 · PDF generado (8 páginas)

## 1. Objetivo
Entregar el reporte que pide la profesora: una **tabla comparativa** de los 7 tipos de aplicaciones (nativas, web, de escritorio, orientadas a servicios, móviles, multiplataforma y web progresivas) con:
- definiciones;
- características;
- ventajas y desventajas;
- herramientas de desarrollo;
- URL de la aplicación.

Sustituye al PDF anterior, `Reporte Comparativo de Aplicaciones.pdf`, que tenía enlaces equivocados y apps que no existen (GastoClaro, NotasYa).

## 2. Fuente de los textos
Todo sale de los **7 reportes ya aprobados (SP1–SP7)**, resumido y sin contradicciones. No se agrega información nueva sin fuente.

## 3. Estructura del PDF
1. **Portada UTP**
   - Título: `PRODUCTO No. 1: REPORTE COMPARATIVO DE TIPOS DE APLICACIONES`.
   - Subtítulo: `Unidad I – Introducción a aplicaciones web progresivas`.
2. **Introducción:** el propósito, los 7 tipos y los 7 proyectos propios.
3. **Tabla comparativa** en **páginas horizontales**.
   - Una sola tabla con las 7 columnas que pide la actividad: **Tipo · Definición · Características · Ventajas · Desventajas · Herramientas de desarrollo · URL de la aplicación**.
   - Una fila por tipo; el encabezado se repite en cada página.
   - Letra de **7.5 a 8 pt** y viñetas cortas (3 o 4 por celda) para que se lea bien.
   - Abarcará unas 3 o 4 páginas horizontales.
   - **Columna URL** (todos los enlaces clicables):
     - la app propia: Pages, Release o cliente;
     - el repositorio;
     - un ejemplo real, ya verificado en su subproducto.
4. **Galería:** una captura representativa de cada app (7 figuras, dos por fila).
5. **Tabla resumen de enlaces:** app, repositorio, URL pública y PDF del subproducto.
6. **Conclusión:**
   - cuándo conviene cada tipo;
   - por qué las PWA combinan lo mejor de la web y de lo nativo, con lo que aprendí en los 7 proyectos.
7. **Referencias APA 7:** consolidadas de los 7 reportes, sin duplicados y en orden alfabético.

## 4. Contenido de la columna URL
| Tipo | App propia | Repositorio | Ejemplo real |
|---|---|---|---|
| Nativa | AquaTrack · APK v1.0.0 (Release) | AquaTrack-Nativa | WhatsApp (Google Play) |
| Web | Mi Recetario · GitHub Pages | Mi_Recetario | Gmail |
| Escritorio | DeskData Pro · .exe v1.0.0 (Release) | App_de_Escritorio | Visual Studio Code |
| Orientada a servicios | BiblioServ · cliente en Pages (API local) | BiblioServ-Servicios | API de Mercado Pago |
| Móvil | Mis Pendientes · APK v1.0.1 + demo web | MisPendientes-Movil | Instagram (Google Play) |
| Multiplataforma | ConvierteYA · web + APK v1.0.1 | ConvierteYA-Multiplataforma | Discord (Google Play) |
| PWA | Mi Recetario PWA · app instalable | MiRecetario-PWA | Squoosh |

**Nota honesta en la fila de servicios:** la API de BiblioServ no tiene hosting público; se ejecuta en local y se prueba en GitHub Actions.

## 5. Galería (capturas ya existentes y reales)
| App | Captura |
|---|---|
| AquaTrack | `SP1/01_inicio.png` |
| Mi Recetario | `SP2/01_inicio.png` |
| DeskData Pro | `SP3/01_inicio.png` |
| BiblioServ | `SP6/02_lista.png` |
| Mis Pendientes | `SP4/01_lista.png` |
| ConvierteYA | `SP5/11_misma_app_web_android.png` |
| Mi Recetario PWA | `SP7/13_ventana_standalone.png` (tu captura) |

## 6. Criterios de aceptación
| # | Criterio | Cómo se verifica |
|---|---|---|
| CA-1 | Las 7 filas tienen todas las columnas llenas. | Revisar el PDF |
| CA-2 | **Todas las URL abren:** se extraen del PDF y se prueba cada una. | Script (curl + Chrome) |
| CA-3 | La tabla se lee bien (≥ 7.5 pt) y nada queda cortado. | Render de cada página a PNG y revisión una por una |
| CA-4 | El PDF está subido al repo central. | GitHub |
| CA-5 | El README del repo central muestra la tabla final de enlaces con P1. | GitHub |
| CA-6 | `PROGRESO.md` marca todo como completo. | GitHub |

## 7. Pruebas
| # | Resultado | Evidencia |
|---|---|---|
| CA-1 | ✅ Las 7 filas tienen las 7 columnas llenas: tabla en 2 páginas horizontales, letra de 7.5 pt y encabezado repetido. | PDF, págs. 2 y 3 |
| CA-2 | ✅ **42/42 enlaces del PDF abren** (extraídos con PyMuPDF y probados con curl). | `evidencias/P1/enlaces_verificados.txt` |
| CA-3 | ✅ Revisé cada página como imagen. Corregí dos palabras cortadas en la tabla («Multiplataforma» y un nombre de paquete). | — |
| CA-4 | ✅ PDF subido a `reportes/`. | GitHub |
| CA-5 | ✅ El README muestra la tabla final de enlaces con P1. | README.md |
| CA-6 | ✅ PROGRESO marca todo como completo. | PROGRESO.md |
