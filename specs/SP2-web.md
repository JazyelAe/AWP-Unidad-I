# SP2 · Actividad Desarrollo — Subproducto No. 2 "Aplicación Web"

**Repo:** `JazyelAe/Mi_Recetario` · **App:** Mi Recetario, versión web clásica.
**Importante:** esta versión NO debe tener manifest ni service worker. Así se distingue de la PWA del SP7, que es la misma idea evolucionada. Este contraste "web → PWA" se menciona en ambos reportes.

## Qué debe hacer la app (mínimo)
- RF-1 Catálogo de recetas con tarjetas (imagen, nombre, categoría, tiempo).
- RF-2 Filtro por categoría y buscador por ingrediente.
- RF-3 Vista de detalle de receta (ingredientes y pasos).
- RF-4 Datos cargados desde un archivo `data/recetas.json` con `fetch`, y/o una API pública (por ejemplo TheMealDB) para mostrar que consume datos remotos.
- RF-5 Formulario de sugerencias con validación en el cliente.
- RF-6 Diseño responsive (móvil, tablet y escritorio).

## Técnico
- HTML5, CSS3 y JavaScript sin framework. Publicada en **GitHub Pages**: `https://jazyelae.github.io/Mi_Recetario/`. Verificar que funcione en esa ruta (rutas relativas).
- Capturas automáticas con Playwright (escritorio 1366×768 y móvil 390×844): inicio, filtro aplicado, búsqueda, detalle, formulario con validación.
- Agregar una captura que muestre que **sin conexión la app no carga**. Es evidencia útil para comparar con la PWA.

## Criterios de aceptación
- [ ] La URL de Pages carga sin errores en la consola.
- [ ] Filtro, búsqueda, detalle y formulario funcionan.
- [ ] Se ve bien en móvil y escritorio.
- [ ] README con capturas y enlace.

## Reporte
`SP2_Aplicacion_Web_SerranoArana.pdf`. Ilustración: diagrama cliente (navegador) ⇄ servidor web (GitHub Pages) ⇄ datos (JSON/API).
Ejemplos reales sugeridos, por verificar: Gmail web, Google Docs y Wikipedia.
