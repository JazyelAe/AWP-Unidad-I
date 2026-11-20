# SP6 · Actividad Desarrollo — Subproducto No. 6 "Aplicación orientada a Servicios"

**Repo:** `JazyelAe/service` (hoy solo tiene `app.py` + `index.html`, sin README) · **App:** BiblioServ (biblioteca).
**Sugerencia:** proponer renombrar el repo a `BiblioServ-Servicios`. Pedir confirmación antes.
**Punto clave del reporte:** la app se compone de **servicios independientes que se comunican por HTTP/JSON**: un servicio propio, un servicio externo y un cliente que los consume.

## Qué debe hacer (mínimo)
- RF-1 **Servicio de catálogo** (API REST Flask): CRUD de libros (`GET/POST/PUT/DELETE /api/libros`) con SQLite.
- RF-2 **Servicio de autenticación** simple con token (`POST /api/login` devuelve un token; las rutas de escritura lo exigen). Puede ser un blueprint separado.
- RF-3 **Consumo de servicio externo**: buscar un libro por ISBN o título en la API pública de Open Library y precargar sus datos.
- RF-4 **Cliente web** (`cliente/`, HTML+JS) que consume la API: login, lista, alta, edición y búsqueda en Open Library.
- RF-5 Documentación de la API: tabla de endpoints en el README y, si es sencillo, OpenAPI/Swagger (`flasgger`).
- RF-6 CORS configurado para el dominio de Pages.

## Técnico
- Despliegue de la API en un hosting gratuito que soporte Python (por ejemplo Render). Requiere mi cuenta: pídeme que la cree e inicie sesión; tú preparas `render.yaml`/`Procfile`, `gunicorn` y variables de entorno.
- Cliente en **GitHub Pages** apuntando a la URL pública de la API. Si el despliegue no es posible, dejar la ejecución local documentada y decírmelo.
- Capturas: Playwright del cliente (login, lista, alta, búsqueda externa) + respuesta JSON de un endpoint + página de Swagger, si existe.
- Pruebas: `pytest` con al menos 5 pruebas de los endpoints.

## Criterios de aceptación
- [ ] La API pública responde `GET /api/libros`.
- [ ] Las escrituras sin token devuelven 401.
- [ ] El cliente en Pages hace el CRUD completo.
- [ ] La búsqueda en Open Library funciona.
- [ ] `pytest` pasa.
- [ ] README con diagrama, endpoints y enlaces.

## Reporte
`SP6_Aplicacion_Servicios_SerranoArana.pdf`. Ilustración: diagrama cliente ⇄ servicio de autenticación ⇄ servicio de catálogo ⇄ SQLite, y servicio de catálogo ⇄ Open Library (externo). Incluir la tabla de endpoints.
Ejemplos reales sugeridos, por verificar: la arquitectura de Netflix o Amazon (microservicios, con fuente oficial), la API de Mercado Pago o PayPal y Google Maps Platform.
