# Progreso · AWP Unidad I

Leyenda: ⬜ pendiente · 🟨 en curso · ✅ terminado · 🛑 esperando revisión

## Preparación
- ✅ Herramientas verificadas (git, gh autenticado como JazyelAe, Python 3.13, Node 24, Flutter 3.x). Falta Android SDK/adb/emulador y JDK 17.
- ✅ Dependencias de la plantilla: reportlab, pillow, playwright + chromium.
- ✅ Repo central `AWP-Unidad-I` creado.
- ✅ PDF de prueba de `tools/utp_doc.py` generado y revisado en Windows (portada + 1 página).
- ✅ Auditoría rápida de repos existentes (clonados en `../repos/`):
  - `kotlin`: 1 commit; MainActivity.kt (Compose, SharedPreferences) duplicado en raíz; sin gradlew/wrapper, sin notificación, sin Actions. No compilable aún.
  - `Mi_Recetario`: Pages OK sin errores, sin SW (correcto para SP2). Datos fijos en JS, sin fetch/JSON, sin detalle.
  - `App_de_Escritorio`: PySide6 + `--self-test` pasa. Mezcla PWA (index.html, manifest, SW). Sin `--capturas`, sin PyInstaller/Release.
  - `service`: Flask con token y SQLite; GET sin token da 401 (debe ser público); `init_db` solo en `__main__`; `send_from_directory("static")` pero no existe `static/`. Sin README, Open Library, pytest ni despliegue.
  - `web`: PWA en Pages con SW activo, manifest y Firestore. Faltan `offline.html`, persistencia offline de Firestore e icono maskable propio.
- ✅ "continúa" recibido: SP1 iniciado.

## Subproductos
| # | Estado | Paso del flujo (1–12) | Notas |
|---|---|---|---|
| SP1 Nativa | ✅ | 12 · Aprobado | Repo AquaTrack-Nativa, Release v1.0.0 con APK, capturas reales en emulador Android 14 (workflow *Capturas en emulador*), CA-1…CA-10 ✅ en SPEC, PDF `reportes/SP1_Aplicacion_Nativa_SerranoArana.pdf` (10 págs.) revisado. Aprobado el 20/11/2026 (opcional: probar en teléfono real). |
| SP2 Web | ✅ | 12 · Aprobado | Pages actualizado (JSON + TheMealDB + detalle + validación + responsive, sin PWA). Pruebas `tools/pruebas_sp2.py` 9/9 contra la URL pública; 13 capturas automáticas; PDF `reportes/SP2_Aplicacion_Web_SerranoArana.pdf` (9 págs.) revisado. Aprobado el 20/11/2026. |
| SP3 Escritorio | ✅ | 12 · Aprobado | Archivos web eliminados y Pages desactivado (aprobado). App reescrita en módulos en español; CPU real con psutil; datos en %APPDATA%; --capturas; Release v1.0.0 con DeskDataPro.exe probado en windows-latest; PDF (10 págs.). Aprobado el 20/11/2026. |
| SP4 Móvil | ✅ | 12 · Aprobado | Repo nuevo MisPendientes-Movil (Flutter). flutter test 3/3; Release v1.0.1 (v1.0.0 tenía error de arranque, no usar); demo web en Pages; capturas reales con gestos en emulador Android 14; PDF (11 págs.). Aprobado el 20/11/2026. |
| SP5 Multiplataforma | ✅ | 12 · Aprobado | Repo nuevo ConvierteYA-Multiplataforma (React Native + Expo SDK 58). jest 12/12; web en Pages 14/14 (Playwright); APK v1.0.1 con expo prebuild + Gradle, sin EAS (v1.0.0 decía «En línea» en modo avión, no usar); mismas conversiones en web y emulador Android 14; iOS no probado; PDF (8 págs.). Aprobado el 20/11/2026. |
| SP6 Servicios | ✅ | 12 · Aprobado | Repo renombrado a BiblioServ-Servicios. Autenticación (token firmado), catálogo CRUD, Open Library, cliente en Pages, Swagger. pytest 14/14; Playwright 15/15 con el cliente de Pages + API local y 15/15 con gunicorn en Actions. Sin Render (decisión de Jaziel): la API no tiene URL pública. PDF (8 págs.). Aprobado el 20/11/2026. |
| SP7 PWA | ✅ | 12 · Aprobado | Repo renombrado a MiRecetario-PWA. Firestore offline, SW con estrategias, offline.html, maskable, screenshots. Playwright 11/11 en Pages; reglas publicadas por Jaziel y comprobadas 6/6; capturas de DevTools e instalación de Jaziel. PDF (9 págs.). Aprobado el 20/11/2026. |
| P1 Producto 1 | ✅ | 12 · Aprobado | PDF de 8 págs.: tabla comparativa horizontal (7 tipos × 7 columnas), galería, enlaces y referencias. 42/42 enlaces verificados. Aprobado el 20/11/2026. |

## ✅ Unidad I completa (20/11/2026)
Los 7 subproductos y el Producto No. 1 están aprobados, con sus PDF en `reportes/` y sus evidencias en `evidencias/`.
