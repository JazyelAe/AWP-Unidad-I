# SP5 · Actividad Desarrollo — Subproducto No. 5 "Aplicación Multiplataforma"

**Repo:** NUEVO `JazyelAe/ConvierteYA-Multiplataforma` · **App:** ConvierteYA (conversor de unidades y divisas).
**Tecnología:** React Native + Expo (JavaScript). **Punto clave del reporte:** UNA sola base de código que corre en Android, iOS y Web.

## Qué debe hacer la app (mínimo)
- RF-1 Conversión de unidades por categorías (longitud, peso, temperatura, volumen).
- RF-2 Conversión de divisas con **API pública** de tipos de cambio sin clave (por ejemplo frankfurter.app; verificar que siga disponible) y último valor guardado para usarlo sin conexión.
- RF-3 Historial de conversiones con AsyncStorage.
- RF-4 Intercambiar origen y destino, y copiar el resultado al portapapeles.
- RF-5 Código compartido; si algo difiere por plataforma, usar `Platform.OS` y documentarlo.

## Técnico
- `npx expo export -p web` → publicar `dist/` en **GitHub Pages** (Actions). Ajustar `baseUrl` para `/ConvierteYA-Multiplataforma/`.
- Android: instrucciones para probar con **Expo Go** (QR) y, opcionalmente, un APK con EAS Build. EAS requiere cuenta Expo: pídeme que inicie sesión yo; no lo hagas tú.
- Capturas: Playwright de la versión web (escritorio y móvil). Pídeme 2–3 capturas de la misma app en el teléfono con Expo Go, para demostrar que es multiplataforma (misma app, dos plataformas, lado a lado en el reporte).

## Criterios de aceptación
- [ ] La versión web en Pages funciona.
- [ ] La misma base de código corre en Android (Expo Go).
- [ ] La API de divisas responde y hay respaldo sin conexión.
- [ ] El historial persiste.
- [ ] README con capturas y enlaces.

## Reporte
`SP5_Aplicacion_Multiplataforma_SerranoArana.pdf`. Ilustración: diagrama "un código (JS/React Native) → Android, iOS y Web".
Ejemplos reales sugeridos, por verificar: Discord (Electron/React Native), Microsoft Teams y Google Pay (Flutter). Confirmar con fuente oficial el framework de cada uno.
