# SP3 · Actividad Desarrollo — Subproducto No. 3 "Aplicación de escritorio"

**Repo:** `JazyelAe/App_de_Escritorio` · **App:** DeskData Pro (Python + PySide6).
**Ojo:** el repo mezcla archivos web (`index.html`, `manifest.json`, `service-worker.js`, `app.js`). En la auditoría, decide con evidencia si son restos. La app de escritorio debe ser Python + PySide6 pura; mueve lo web a `legacy/` o elimínalo, y pregúntame antes de borrar.

## Qué debe hacer la app (mínimo)
- RF-1 Ventana principal con tabla de registros (por ejemplo inventario o gastos), alta, edición y eliminación.
- RF-2 Persistencia local en JSON y **exportar/importar CSV** con diálogo de archivos del sistema.
- RF-3 Búsqueda y filtro en la tabla.
- RF-4 Gráfica o resumen simple (totales por categoría).
- RF-5 Funciona **sin internet** y usa recursos locales (archivos y diálogos nativos del sistema).
- RF-6 Opción `--capturas` que abre la app con datos de ejemplo y guarda capturas de cada vista con `QWidget.grab()` en `docs/capturas/`. Así Claude Code puede tomar las capturas sin mí.

## Técnico
- `requirements.txt` con versiones fijas. `README` con "cómo ejecutar".
- Empaquetado con **PyInstaller** (`--onefile --windowed`) mediante `.github/workflows/build.yml` en `windows-latest`. El `.exe` se adjunta a un **GitHub Release** `v1.0.0`; ese enlace es la "URL de la aplicación".
- Si conviene, desactivar GitHub Pages en este repo, porque ya no es web. Pregúntame antes.

## Criterios de aceptación
- [ ] `python main.py` abre la app en Windows sin errores.
- [ ] CRUD, búsqueda, CSV y resumen funcionan, y los datos persisten.
- [ ] El Release tiene el `.exe` y abre en otra PC con Windows sin tener Python instalado.
- [ ] Capturas generadas con `--capturas`.

## Reporte
`SP3_Aplicacion_Escritorio_SerranoArana.pdf`. Ilustración: diagrama app ⇄ sistema operativo (archivos, ventanas) ⇄ hardware local.
Ejemplos reales sugeridos, por verificar: Visual Studio Code, Microsoft Excel y OBS Studio.
