# SP1 · Actividad Apertura — Subproducto No. 1 "Aplicación Nativa"

**Repo:** `JazyelAe/kotlin` · **App:** AquaTrack. El README actual indica que hay que crear el proyecto desde Android Studio, así que probablemente el repo no está completo.
**Sugerencia:** proponer renombrar el repo a `AquaTrack-Nativa` (GitHub redirige el nombre viejo). Pedir confirmación antes de hacerlo.

## Qué debe hacer la app (mínimo)
- RF-1 Registrar vasos o mililitros de agua consumidos (botones rápidos de 250 y 500 ml y entrada personalizada).
- RF-2 Meta diaria configurable, con barra o anillo de progreso.
- RF-3 Historial por día, persistido localmente (DataStore o SharedPreferences, o Room si es sencillo).
- RF-4 **Función nativa del dispositivo**: recordatorio con notificación local (WorkManager o AlarmManager) y/o vibración al alcanzar la meta. Pedir el permiso `POST_NOTIFICATIONS` en Android 13+.
- RF-5 Interfaz con Jetpack Compose y Material 3. Icono propio.

## Técnico
- Proyecto Gradle completo y compilable: `gradlew`, wrapper, `app/`, `minSdk 26`, paquete `com.jaziel.aquatrack`.
- `.github/workflows/android.yml`: compilar `assembleDebug` y adjuntar el APK a un **GitHub Release** (`v1.0.0`). El enlace "URL de la aplicación" es el de la página del Release.
- Si puedo correr un emulador, toma las capturas con `adb exec-out screencap -p > docs/capturas/xx.png`. Si no, pídeme capturas de: pantalla principal, registro de consumo, meta alcanzada, historial y notificación.

## Criterios de aceptación
- [ ] El workflow de Actions pasa en verde y el Release tiene el APK descargable.
- [ ] La app instala y abre en Android 8+; los datos persisten al cerrar y abrir.
- [ ] Llega la notificación de recordatorio.
- [ ] README con capturas, instrucciones y enlaces.

## Reporte
`SP1_Aplicacion_Nativa_SerranoArana.pdf`, con la estructura de CLAUDE.md. Ilustración: diagrama "código Kotlin → compilado para Android → APIs del sistema (notificaciones, almacenamiento)".
Ejemplos reales sugeridos, por verificar: WhatsApp (Android, Play Store), Google Maps para Android y la app de Cámara del sistema. Explicar por qué son nativas (SDK de la plataforma, acceso a hardware, distribución por tienda).
