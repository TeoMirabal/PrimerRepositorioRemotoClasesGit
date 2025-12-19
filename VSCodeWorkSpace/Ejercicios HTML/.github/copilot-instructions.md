<!-- Copilot instructions for this small static HTML site -->
# Instrucciones rápidas para agentes de IA

Objetivo: ayudar a contribuir código y correcciones en este pequeño sitio estático de ejemplo (HTML) que documenta armas de Valorant.

- Estructura principal: archivos HTML planos en la raíz del repositorio.
  - `index.html` — página de inicio con enlaces a las secciones.
  - `pistolas.html`, `escopetas.html`, `subfusiles.html`, `rifles_francotirador.html`, `fusiles.htm` — páginas de contenido.

- Big picture y por qué: el proyecto es un conjunto de páginas estáticas sin pipeline de build ni dependencias. Los cambios normalmente son HTML/CSS simples. Mantén el marcado semántico (por ejemplo, evitar colocar `h2` dentro de un `a` si no es intencional).

- Convenciones observadas y problemas detectados:
  - Archivos HTML en la raíz; algunas extensiones usan `.htm` (`fusiles.htm`) mientras otras usan `.html`. Mantén consistencia a menos que una razón histórica justifique lo contrario.
  - En `index.html` hay enlaces que envuelven `h2` dentro de `a`. Esto es válido en HTML5 (contenedor de bloque dentro de enlace) pero puede confundir estilos. Si se requiere accesibilidad, asegúrate de que los enlaces tengan texto descriptivo y roles ARIA si es necesario.
  - Un enlace en `index.html` muestra texto "Rifles rifles_francotirador" — probable duplicación/typo; revisa y sugiere corrección a "Rifles francotirador" o similar.

- Patrones de edición y ejemplos concretos:
  - Para corregir un texto duplicado en `index.html` reemplaza la línea:
    - <h2>Rifles rifles_francotirador</h2>
    + <h2>Rifles francotirador</h2>
  - Para normalizar extensiones, renombra `fusiles.htm` a `fusiles.html` y actualiza los enlaces en `index.html`.
  - Si añades CSS, crea un archivo `styles.css` en la raíz o en `css/` y referencia desde el `head` de cada HTML.

- Flujo de trabajo recomendado para agentes:
  1. Buscar inconsistencias con una búsqueda simple (p. ej., extensiones `.htm` vs `.html` y textos repetidos en `index.html`).
  2. Proponer cambios mínimos y pruebas: abrir el HTML en un navegador local (arrastrar archivo o usar un servidor estático) para validar.
  3. Evitar cambios disruptivos (no introducir frameworks ni pipelines). Mantener el repo como sitio estático simple.

- Comandos útiles para desarrolladores (no automáticos):
  - Servir localmente con Python 3: `python -m http.server 8000` desde la raíz del proyecto, luego abrir http://localhost:8000/index.html

- Qué NO hacer:
  - No reemplazar la estructura por un framework complejo (React/Vite/etc.) sin aprobación.
  - No cambiar extensiones sin actualizar todos los enlaces relacionados.

Referencias a archivos clave:
- `index.html` — punto de entrada, contiene enlaces con texto y posibles typos.
- `fusiles.htm` — nota de inconsistencia de extensión.

Si algo no está claro (por ejemplo, intención del autor sobre `.htm` vs `.html`), pide aclaración antes de renombrar archivos.

-- Pregunta para el mantenedor: ¿prefieres normalizar todas las extensiones a `.html` y corregir el texto duplicado en `index.html`? 
