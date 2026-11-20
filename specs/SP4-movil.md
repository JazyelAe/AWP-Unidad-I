# SP4 · Actividad Desarrollo — Subproducto No. 4 "Aplicación Móvil"

**Repo:** NUEVO `JazyelAe/MisPendientes-Movil` · **App:** Mis Pendientes (gestor de tareas).
**Tecnología:** Flutter + Dart (ya tengo una carpeta `flutter` en mi usuario; verifica con `flutter doctor`).
**Enfoque:** lo que la hace "móvil" es el diseño para pantalla pequeña, la interacción táctil y el uso de capacidades del teléfono. Diferenciarla de SP1 (nativa con el SDK de Android) y de SP5 (multiplataforma).

## Qué debe hacer la app (mínimo)
- RF-1 Lista de tareas con alta, edición, completar y borrar.
- RF-2 **Gestos táctiles**: deslizar para borrar o completar, mantener presionado para editar y *pull to refresh*.
- RF-3 Prioridad y fecha límite, con orden y filtro.
- RF-4 Persistencia local (`shared_preferences` o `sqflite`).
- RF-5 Una capacidad del dispositivo: notificación local de recordatorio (`flutter_local_notifications`) o vibración/háptica.
- RF-6 Material 3, modo oscuro e icono propio.

## Técnico
- `.github/workflows/flutter.yml`: `flutter build apk --release`, que adjunta el APK a un **Release** `v1.0.0`, y `flutter build web --base-href /MisPendientes-Movil/`, que se publica en **GitHub Pages** como demo.
- Capturas: Playwright sobre la demo web en viewport móvil (390×844) y, si hay emulador, `adb screencap`. Si no, pídeme las capturas del teléfono o emulador.

## Criterios de aceptación
- [ ] El APK instala y funciona; los datos persisten.
- [ ] Los gestos funcionan.
- [ ] Llega la notificación o se siente la vibración.
- [ ] La demo web en Pages carga en vista móvil.
- [ ] README con capturas y enlaces.

## Reporte
`SP4_Aplicacion_Movil_SerranoArana.pdf`. Ilustración: diagrama de interacción táctil → app → sensores y servicios del teléfono.
Ejemplos reales sugeridos, por verificar: Instagram, Uber (app) y Duolingo.
