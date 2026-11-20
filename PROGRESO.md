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
| SP2 Web | 🛑 | 12 · Checkpoint B | Pages actualizado (JSON + TheMealDB + detalle + validación + responsive, sin PWA). Pruebas `tools/pruebas_sp2.py` 9/9 contra la URL pública; 13 capturas automáticas; PDF `reportes/SP2_Aplicacion_Web_SerranoArana.pdf` (9 págs.) revisado. Esperando revisión. |
| SP3 Escritorio | ⬜ | — | |
| SP4 Móvil | ⬜ | — | |
| SP5 Multiplataforma | ⬜ | — | |
| SP6 Servicios | ⬜ | — | |
| SP7 PWA | ⬜ | — | |
| P1 Producto 1 | ⬜ | — | |
