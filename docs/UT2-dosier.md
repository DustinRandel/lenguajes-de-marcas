---
title: "El documento HTML"
subtitulo: "UT2. Dosier de apuntes"
modulo: "0373. Lenguajes de marcas y sistemas de gestión de información"
curso: "2026-2027"
profesor: "Dustin Randel de Lara García"
centro: "Sant Josep Obrer"
ut: "UT2"
---

# Cómo usar este dosier {.nobreak}

En la UT1 escribiste el primer `index.html` y lo abriste. Aquí entra el documento de verdad: qué va en el `head`, cómo se anidan las etiquetas, listas, enlaces, imágenes y tablas de datos.

Copia los ejemplos, rómpelos a propósito y mira qué hace el navegador. F12, pestaña Elementos, es tu sitio de trabajo.

<!-- Notas del profesor: UF1 Html, ya examinada el 12/11. Se reordena el material de «Introducción al documento HTML» y «Estructura, etiquetas y tablas». Formularios y rutas relativas siguen en la carpeta UF1. -->

## Qué vas a aprender

Al terminar esta unidad deberías ser capaz de:

- **Escribir** un documento HTML5 con DOCTYPE, `html`, `head` y `body`.
- **Anidar** etiquetas con criterio y poner atributos entre comillas.
- **Marcar** títulos, párrafos, listas, enlaces e imágenes.
- **Crear** una tabla de datos con `table`, `tr`, `th` y `td`.
- **Explicar** qué va en el `head` (charset, title) y qué se ve en el `body`.

## Índice

| | Bloque |
|---|---|
| [1](#bloque-1-el-documento-html5) | El documento HTML5 |
| [2](#bloque-2-etiquetas-atributos-y-anidacion) | Etiquetas, atributos y anidación |
| [3](#bloque-3-texto-listas-y-divisiones) | Texto, listas y divisiones |
| [4](#bloque-4-enlaces-e-imagenes) | Enlaces e imágenes |
| [5](#bloque-5-tablas-de-datos) | Tablas de datos |
| A | Glosario |
| B | Mapa |
| C | Autoevaluación |

# Bloque 1. El documento HTML5

## 1.1 El navegador pide un archivo, no magia

Cuando escribes una dirección, tu navegador (el cliente) pide al servidor unos archivos: HTML, CSS, imágenes. El HTML es texto plano. El navegador lo interpreta y pinta la página. Clic derecho, «Ver código fuente», enseña exactamente eso.

!!! definicion "HTML"
    Lenguaje de marcas para crear páginas web. Define la estructura y el contenido. El aspecto lo pone CSS y el comportamiento, JavaScript. La versión actual es HTML5.

## 1.2 El esqueleto no se improvisa

```html
<!DOCTYPE html>
<html lang="es">
  <head>
    <meta charset="UTF-8">
    <title>Videoclub La Palma</title>
  </head>
  <body>
    <h1>Cartelera</h1>
  </body>
</html>
```

| Pieza | Para qué |
|---|---|
| `<!DOCTYPE html>` | Dice al navegador: esto es HTML5 |
| `<html lang="es">` | Raíz del documento. `lang` ayuda al lector de pantalla y al corrector |
| `<head>` | Datos para el navegador: no se ven en la página |
| `<meta charset="UTF-8">` | Tildes y eñes bien. Sin esto, «año» puede salir raro |
| `<title>` | Texto de la pestaña |
| `<body>` | Lo que se ve |

!!! ojo "Ojo"
    El `title` no es el `h1`. El título de la pestaña va en el `head`. El título visible, en el `body`.

!!! comprueba "Comprueba"
    1. ¿Qué pasa si omites el charset y escribes «Mallorca»?
    2. ¿Dónde aparece el texto de `<title>`?
    3. ¿El `DOCTYPE` se cierra?

# Bloque 2. Etiquetas, atributos y anidación

## 2.1 Anatomía de un elemento

Un elemento con contenido tiene apertura, contenido y cierre:

```html
<p>Un párrafo con <strong>énfasis</strong>.</p>
```

Algunos no tienen contenido y no se cierran: `<img>`, `<br>`, `<hr>`, `<meta>`.

!!! definicion "Elemento HTML"
    Unidad del documento: una etiqueta de apertura (con o sin atributos), un contenido opcional y, si lo hay, una etiqueta de cierre. El navegador no enseña las marcas: enseña el resultado.

Los atributos van en la apertura, con el valor entre comillas:

```html
<img src="cartel.jpg" alt="Cartel de Dune">
```

`id` es único en la página. `class` se puede repetir. `title` (el atributo) es el texto al pasar el ratón, no el de la pestaña.

## 2.2 Anidar con orden

Se abre por fuera y se cierra por dentro, como cajas:

```html
<p>Correcto: <em>énfasis</em>.</p>
```

Esto está mal: `<p><em>énfasis</p></em>`. El navegador a veces «arregla» el HTML roto y el resultado te despista. En XML no te lo perdona.

HTML no distingue mayúsculas, pero se escribe en minúsculas. Los espacios de más en el fuente no se ven en la página: para un salto visible usas `<br>` o, mejor, otro párrafo.

!!! predice "Predice"
    `<p>Hola     mundo</p>` con cinco espacios. ¿Se ven los cinco en el navegador?

!!! comprueba "Comprueba"
    1. Cita dos etiquetas que no se cierran.
    2. ¿El valor de un atributo va con comillas o sin ellas?
    3. ¿Puedes poner un `<p>` dentro de otro `<p>`?

# Bloque 3. Texto, listas y divisiones

## 3.1 Títulos y párrafos

`h1` a `h6` son títulos, no tamaños de letra. Un `h1` por página, como regla de trabajo. El párrafo es `<p>`. Un salto de línea suelto en el fuente no pinta un renglón nuevo.

`<div>` agrupa. No significa nada por sí solo: sirve para maquetar cuando no hay una etiqueta con sentido (eso lo aprovecha CSS). Si es un menú, usa `<nav>`; si es el contenido principal, `<main>`.

## 3.2 Listas

```html
<ul>
  <li>Dune</li>
  <li>El padrino</li>
</ul>

<ol>
  <li>Alquilar</li>
  <li>Devolver</li>
</ol>
```

`ul` no ordena. `ol` numera. El ítem siempre es `li`. Se pueden anidar listas dentro de un `li`.

!!! comprueba "Comprueba"
    1. ¿Qué etiqueta usarías para el menú de la web?
    2. ¿`h1` es un tamaño de fuente?
    3. ¿Puede un `li` contener otro `ul`?

# Bloque 4. Enlaces e imágenes

## 4.1 El atributo href

```html
<a href="https://www.santjosepobrer.es">El colegio</a>
<a href="cartelera.html">Cartelera</a>
<a href="#pie">Ir al pie</a>
```

- Una URL absoluta empieza por `https://`.
- Una relativa, por el nombre de un archivo o una carpeta (lo mismo que en las rutas de siempre).
- Un ancla `#pie` salta al elemento con `id="pie"` de la misma página.

## 4.2 img siempre con alt

```html
<img src="imagenes/dune.jpg" alt="Cartel de Dune, arena y un personaje">
```

Sin `alt`, si la imagen no carga no hay recado, y el lector de pantalla no sabe qué hay. `width` y `height` reservan el hueco; el tamaño visual fino se deja para CSS.

!!! ojo "Ojo"
    `alt=""` (vacío) es para adornos. `alt` ausente es un fallo. No pongas «imagen de» en el alt: ya se sabe que es una imagen.

!!! comprueba "Comprueba"
    1. ¿Qué href usarías para saltar al `id="contacto"` de la misma página?
    2. ¿`img` tiene etiqueta de cierre?
    3. ¿Para qué sirve `alt` si la imagen se ve bien?

# Bloque 5. Tablas de datos

## 5.1 Solo para datos

Una tabla organiza filas y columnas. La pregunta: ¿tendría sentido en una hoja de cálculo? Si sí, va en una tabla. Si no (maquetar la página entera), no.

```html
<table>
  <caption>Alquileres de la semana</caption>
  <thead>
    <tr>
      <th>Película</th>
      <th>Días</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Dune</td>
      <td>3</td>
    </tr>
  </tbody>
</table>
```

| Etiqueta | Papel |
|---|---|
| `table` | La tabla |
| `caption` | Título de la tabla |
| `tr` | Fila |
| `th` | Celda de encabezado |
| `td` | Celda de dato |
| `thead` / `tbody` | Agrupan filas de cabecera y de cuerpo |

`colspan` y `rowspan` unen celdas. No abuses: si la tabla se vuelve un puzzle, revisa los datos.

!!! predice "Predice"
    Una fila con tres `td` y la siguiente con dos. ¿El navegador deja un hueco o rompe la tabla?

!!! comprueba "Comprueba"
    1. ¿Usarías una tabla para el menú de la web? ¿Por qué?
    2. ¿Qué diferencia hay entre `th` y `td`?
    3. ¿Dónde va `caption`, dentro o fuera de `table`?

# Anexo A. Glosario

| Término | Significado |
|---|---|
| DOCTYPE | Primera línea: declara HTML5 |
| head | Metadatos: title, charset, enlaces a CSS |
| body | Contenido visible |
| Atributo | Par nombre="valor" en la apertura |
| Ancla | Enlace a un `id` de la misma página |
| alt | Texto alternativo de una imagen |
| th | Celda de encabezado de tabla |

# Anexo B. Mapa

```text
Documento
  DOCTYPE, html lang, head (charset, title), body
  Etiqueta = apertura + atributos + contenido + cierre (si lo hay)
  Texto: h1-h6, p, ul/ol/li, div/nav/main
  href (absoluto, relativo, #id) e img src/alt
  table > tr > th|td
```

# Anexo C. Autoevaluación

## Preguntas cortas

1. Escribe el esqueleto mínimo de un HTML5.
2. ¿Por qué el `title` no va en el `body`?
3. Cita tres etiquetas vacías.
4. ¿Cuándo una tabla es el marcado correcto?

## Tipo test

1. `lang="es"` se pone en:
    - a) `body`
    - b) `html`
    - c) `title`
    - d) `p`
2. Un enlace al pie de la misma página:
    - a) `href="pie.html"`
    - b) `href="#pie"`
    - c) `src="#pie"`
    - d) `href="/pie"`
3. La celda de encabezado es:
    - a) `td`
    - b) `tr`
    - c) `th`
    - d) `head`

## Razona

Sara maqueta toda la portada con una tabla de 3×2 (logo, menú, contenido…). ¿Qué le dices y qué etiquetas le propones en su lugar?
