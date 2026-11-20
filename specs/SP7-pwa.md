# SP7 · Actividad Cierre — Subproducto No. 7 "Aplicación Web Progresiva"

**Repo:** `JazyelAe/web` · **App:** Mi Recetario PWA (Firebase Firestore + manifest + service worker). Es mi app más completa: **solo verificar y pulir, no rehacer.**
**Sugerencia:** proponer renombrar el repo a `MiRecetario-PWA`. Pedir confirmación antes. Después actualizar los enlaces de Pages.
Relación con SP2: es la evolución de la app web `Mi_Recetario`. Hay que explicarlo en el reporte.

## Verificar o completar en la app
- RF-1 `manifest.json` completo: `name`, `short_name`, `start_url`, `scope`, `display: standalone`, `theme_color`, `background_color` e iconos 192/512 (incluido uno *maskable*).
- RF-2 Service worker registrado, con estrategia de caché documentada (por ejemplo *cache first* para estáticos y *network first* para datos) y página `offline.html`.
- RF-3 **Instalable** desde Chrome/Edge (escritorio y Android).
- RF-4 Funciona **sin conexión**: muestra las recetas cacheadas; la persistencia offline de Firestore está activada.
- RF-5 Servida por HTTPS (GitHub Pages) y responsive.
- RF-6 Reglas de Firestore revisadas (lectura pública y escritura limitada a sugerencias).

## Estructura propia del reporte (lo que pide la profesora)
1. Introducción (incluye la relación web → PWA con SP2)
2. Definición (basada en web.dev, MDN y Microsoft Learn; citar)
3. Características (instalable, offline, responsive, segura con HTTPS, *app-like*, actualizable, descubrible, re-engageable)
4. Ventajas y desventajas (tabla)
5. Herramientas de desarrollo (manifest, Service Worker API, Cache Storage, Firebase, DevTools, PWABuilder, Workbox)
6. Ejemplos con URL: **mi app** + 3 PWA reales verificadas (por ejemplo Starbucks `app.starbucks.com`, Uber `m.uber.com`, Spotify `open.spotify.com`, Squoosh `squoosh.app`)
7. **Evidencias de identificación de características**: una figura por característica con descripción de qué demuestra. Se hacen sobre MI app y, si es posible, también sobre 1 PWA real:
   - Manifest (captura del JSON o del panel Application → Manifest)
   - Service worker activo (Application → Service Workers)
   - Cache Storage con archivos cacheados
   - Instalación (botón o diálogo de instalar) y app abierta en ventana *standalone*
   - Funcionamiento offline (Playwright: `context.set_offline(True)` + recarga → la app sigue mostrando contenido)
   - Responsive (capturas móvil y escritorio)
   - HTTPS (candado o URL)

   Lo automatizable con Playwright, hazlo tú. Las capturas de DevTools y de instalación pídemelas con nombre de archivo y qué debe verse. Nota: Lighthouse ya no tiene categoría "PWA", así que no la uses como evidencia.
8. Conclusión
9. Referencias APA 7 (incluir las 3 fuentes del material de lectura)

## Criterios de aceptación
- [ ] Instalable y offline comprobados.
- [ ] Todas las evidencias presentes con descripción.
- [ ] Enlaces de los 4 ejemplos verificados.
- [ ] `SP7_Aplicacion_Web_Progresiva_SerranoArana.pdf` generado y subido.
