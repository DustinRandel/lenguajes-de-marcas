---
title: "Layout responsive"
subtitulo: "UT4. Dosier de apuntes"
modulo: "0373. Lenguajes de marcas y sistemas de gestión de información"
curso: "2026-2027"
profesor: "Dustin Randel de Lara García"
centro: "Sant Josep Obrer"
ut: "UT4"
---

# Cómo usar este dosier {.nobreak}

Esta unidad entra cuando ya sabes escribir HTML y CSS. El problema nuevo no es pintar una caja: es que esa caja se vea bien en el móvil, en la tablet y en el portátil **con el mismo HTML**.

Copia los ejemplos, cambia el ancho de la ventana y mira F12. Flexbox y Grid se entienden mucho mejor viendo cómo se mueven las cajas que leyendo la lista de propiedades.

<!-- Notas del profesor: siguiente unidad tras CSS (cronograma: 17/12). Acompañan las diapositivas «UT4. Presentación: Layout responsive» y los ejercicios de Flexbox, Grid y Media queries. -->

A lo largo del texto encontrarás las mismas cajas de siempre:

!!! definicion "Definición"
    Un término que tienes que saber explicar con tus propias palabras.

!!! ejemplo "Ejemplo"
    Un caso concreto con su código.

!!! ojo "Ojo"
    Un error típico o una confusión frecuente.

!!! predice "Predice"
    Antes de probarlo en el navegador, apunta lo que crees que va a pasar.

!!! comprueba "Comprueba"
    Preguntas cortas al final de cada bloque.

## Qué vas a aprender

Al terminar esta unidad deberías ser capaz de:

- **Explicar** qué es un layout responsive y por qué no se hace una página distinta por dispositivo.
- **Colocar** elementos en una dimensión con Flexbox (menú, fila de tarjetas, pie).
- **Repartir** el espacio sobrante con `flex-grow`, `flex-shrink` y `flex-basis`.
- **Maquetar** en dos dimensiones con Grid (cabecera, columnas, áreas con nombre).
- **Cambiar** el layout según el ancho con media queries, sin tocar el HTML.

## Índice

| | Bloque |
|---|---|
| [1](#bloque-1-que-es-un-layout-responsive) | Qué es un layout responsive |
| [2](#bloque-2-flexbox-el-contenedor) | Flexbox: el contenedor |
| [3](#bloque-3-flexbox-los-items) | Flexbox: los ítems |
| [4](#bloque-4-css-grid) | CSS Grid |
| [5](#bloque-5-media-queries) | Media queries |
| A | Glosario |
| B | Mapa |
| C | Autoevaluación |

# Bloque 1. Qué es un layout responsive

## 1.1 El layout es cómo se colocan las cajas

En la UT3 cada elemento era una caja (contenido, relleno, borde, margen) y `display` decía si ocupaba todo el renglón o se ponía en línea. Eso no basta cuando hay que alinear un menú, centrar un logo y poner tres tarjetas en fila.

!!! definicion "Layout"
    Manera de colocar y organizar las cajas de una página. No es una propiedad suelta: es el conjunto de reglas (display, flex, grid, floats antiguos) que decide quién va al lado de quién y cómo se reparte el hueco.

Durante años se maquetaba con tablas (`<table>` para todo) y después con `float`. Las dos cosas eran un apaño. Hoy el trabajo serio se hace con **Flexbox** (una dimensión: una fila o una columna) y **Grid** (dos dimensiones: filas y columnas a la vez).

## 1.2 Una sola página, muchos anchos

El móvil, la tablet y el portátil no tienen el mismo ancho. Si escribes un HTML distinto para cada uno, cada cambio se multiplica por tres y se te olvida uno.

!!! definicion "Diseño responsive"
    Un mismo HTML (y, en lo posible, un mismo CSS) que se reorganiza según el ancho disponible: el menú pasa de horizontal a vertical, las tres columnas se apilan, el texto baja de tamaño. El contenido no se recorta ni obliga a hacer scroll horizontal.

No se trata de «hacer la web más pequeña». Se trata de **reordenar**. El mismo `nav` puede ser una fila en el portátil y una columna en el móvil.

!!! ojo "Ojo"
    `width: 1200px` en el contenedor principal rompe el responsive: en un móvil de 360 px aparece una barra horizontal. Empieza por `max-width` y anchos en `%` o `fr`.

!!! comprueba "Comprueba"
    1. ¿Qué problema hay en hacer tres HTML, uno por dispositivo?
    2. ¿Flexbox resuelve una dimensión o dos?
    3. Si una caja tiene `width: 1200px`, ¿qué pasa en un móvil de 360 px?

# Bloque 2. Flexbox: el contenedor

## 2.1 El padre es flex, los hijos son ítems

Flexbox no es una propiedad: es un **sistema**. Se activa en el padre.

```css
nav {
  display: flex;
}
```

A partir de ahí, los hijos directos de `nav` pasan a ser **ítems flex**. Las propiedades del padre colocan a todos; las de cada hijo retocan a uno.

!!! definicion "Contenedor flex"
    Elemento con `display: flex` (o `inline-flex`). Define el eje principal y cómo se reparte el espacio. Sus hijos directos son los ítems.

## 2.2 Eje principal y eje cruzado

Por defecto el eje principal va de izquierda a derecha (`flex-direction: row`). El eje cruzado es el perpendicular (arriba-abajo). Si pones `flex-direction: column`, se intercambian.

| Propiedad | Qué decide |
|---|---|
| `flex-direction` | Dirección del eje principal: `row`, `row-reverse`, `column`, `column-reverse` |
| `flex-wrap` | Si los ítems pueden saltar de línea: `nowrap` (por defecto) o `wrap` |
| `justify-content` | Reparto en el eje principal: `flex-start`, `center`, `space-between`, `space-around`, `space-evenly` |
| `align-items` | Alineación en el eje cruzado: `stretch` (por defecto), `flex-start`, `center`, `flex-end`, `baseline` |
| `align-content` | Alineación de las **líneas** cuando hay wrap. No mueve ítems sueltos |
| `gap` | Hueco entre ítems, sin tocar los bordes del padre |

```css
nav {
  display: flex;
  justify-content: space-between;
  align-items: center;
  gap: 1rem;
}
```

Ese `nav` pone el logo a un lado, los enlaces al otro, centrados en vertical, con un rem de aire entre ellos.

!!! predice "Predice"
    Un `nav` con `display: flex` y cinco enlaces. Sin `flex-wrap`. La ventana mide 320 px y los enlaces no caben. ¿Se apilan en dos líneas o se aplastan?

!!! ojo "Ojo"
    `align-content` no hace nada si los ítems caben en una sola línea. Si crees que «no va», mira antes si hay `flex-wrap: wrap` y de verdad hay varias filas.

!!! comprueba "Comprueba"
    1. ¿Qué propiedad activa Flexbox?
    2. ¿`justify-content` mueve en el eje principal o en el cruzado?
    3. ¿Qué valor de `flex-wrap` hace falta para que `align-content` tenga efecto?

# Bloque 3. Flexbox: los ítems

## 3.1 Tres números que se recuerdan juntos

Cada ítem puede decir cuánto crece, cuánto encoge y de qué tamaño parte.

```css
.item {
  flex-grow: 1;
  flex-shrink: 1;
  flex-basis: 0;
}
```

Se abrevia `flex: 1 1 0` (o, más corto, `flex: 1`).

| Propiedad | Por defecto | Qué hace |
|---|---|---|
| `flex-grow` | 0 | Cuánto **crece** para comerse el hueco sobrante. 0 = no crece |
| `flex-shrink` | 1 | Cuánto **encoge** si no caben. 0 = no encoge |
| `flex-basis` | auto | Tamaño de partida, antes de crecer o encoger |
| `order` | 0 | Orden visual, sin cambiar el HTML. Cuidado con la accesibilidad |
| `align-self` | auto | Anula el `align-items` del padre solo para este ítem |

!!! ejemplo "Ejemplo"
    Tres columnas con `flex: 1` se reparten el ancho a partes iguales. Si a la del medio le pones `flex-grow: 2`, se lleva el doble de hueco sobrante que las otras.

## 3.2 Un cálculo que sale en clase

Contenedor de 400 px. Tres ítems con `flex-basis: 0` y `flex-grow: 1, 2, 1`. El sobrante es todo el ancho (porque el basis es 0):

- ítem 1: 1/4 → 100 px
- ítem 2: 2/4 → 200 px
- ítem 3: 1/4 → 100 px

Si el basis no es 0, primero se reserva ese tamaño y **después** se reparte lo que quede.

!!! ojo "Ojo"
    `order` cambia el orden en pantalla, no en el HTML. El lector de pantalla y el tabulador siguen el HTML. No lo uses para «arreglar» un menú: reordena el marcado.

!!! comprueba "Comprueba"
    1. ¿Qué significa `flex: 1`?
    2. Si `flex-grow` vale 0 en todos, ¿quién se come el hueco sobrante?
    3. ¿`align-self: center` en un ítem cambia a sus hermanos?

# Bloque 4. CSS Grid

## 4.1 Filas y columnas a la vez

Flexbox coloca en **una** dirección. Grid dibuja una cuadrícula: filas y columnas, y cada hijo ocupa una o varias celdas.

```css
.tablero {
  display: grid;
  grid-template-columns: 1fr 1fr 1fr;
  gap: 1rem;
}
```

Tres columnas del mismo ancho. `fr` es una fracción del espacio libre: `1fr 2fr` es un tercio y dos tercios.

!!! definicion "CSS Grid"
    Sistema de layout en dos dimensiones. El padre (`display: grid`) define pistas (filas y columnas). Cada hijo se coloca en celdas, con línea de inicio y de fin, o con un nombre de área.

## 4.2 Líneas y áreas

Las líneas se numeran desde 1. Un ítem puede decir «de la línea 1 a la 3»:

```css
.destacado {
  grid-column: 1 / 3;
  grid-row: 1 / 2;
}
```

Con nombres se lee mejor:

```css
.pagina {
  display: grid;
  grid-template-columns: 1fr 200px;
  grid-template-areas:
    "cabecera cabecera"
    "principal lateral"
    "pie pie";
}
header { grid-area: cabecera; }
main   { grid-area: principal; }
aside  { grid-area: lateral; }
footer { grid-area: pie; }
```

| Propiedad | Dónde | Para qué |
|---|---|---|
| `grid-template-columns` | padre | Ancho de cada columna (`200px`, `1fr`, `repeat(3, 1fr)`) |
| `grid-template-rows` | padre | Alto de cada fila |
| `grid-template-areas` | padre | Mapa con nombres |
| `gap` | padre | Hueco entre pistas |
| `grid-column` / `grid-row` | hijo | De qué línea a qué línea |
| `grid-area` | hijo | Nombre del área que ocupa |

!!! predice "Predice"
    `grid-template-columns: 100px 1fr 1fr` en un contenedor de 500 px. ¿Cuánto mide cada columna?

!!! ojo "Ojo"
    Grid no sustituye a Flexbox. Una página suele ser Grid por fuera (cabecera, columnas, pie) y Flexbox por dentro (el menú, las tarjetas de una fila).

!!! comprueba "Comprueba"
    1. ¿Qué unidad usas para «el resto del hueco» en Grid?
    2. ¿`grid-template-areas` va en el padre o en el hijo?
    3. ¿Cuándo elegirías Flexbox en vez de Grid?

# Bloque 5. Media queries

## 5.1 El CSS pregunta el ancho

Una media query es un «si el viewport mide tanto, aplica estas reglas». El HTML no cambia.

```css
.caja {
  background: navy;
  font-size: 24px;
}

@media (max-width: 768px) {
  .caja {
    background: teal;
    font-size: 18px;
  }
}
```

Por encima de 768 px, navy y 24 px. A 768 px o menos, teal y 18 px.

!!! definicion "Media query"
    Bloque `@media` con una condición sobre el viewport (ancho, alto, orientación). Las reglas de dentro solo se aplican si la condición se cumple.

## 5.2 Desktop first y mobile first

**Desktop first:** escribes el CSS del portátil y, con `max-width`, recortas hacia el móvil.

**Mobile first:** escribes el CSS del móvil y, con `min-width`, añades reglas al agrandar.

Los dos valen. En clase usaremos sobre todo `max-width`, que es el que sale en los ejercicios, y al final probarás uno con `min-width` para ver la diferencia.

Un patrón habitual de menú:

```css
.menu {
  display: flex;
  flex-direction: row;
  gap: 1rem;
}

@media (max-width: 600px) {
  .menu {
    flex-direction: column;
  }
}
```

En el portátil, fila. En el móvil, columna. Mismo HTML.

!!! ojo "Ojo"
    El punto de corte no es «el de Bootstrap» por obligación. Míralo con tu contenido: estrecha la ventana hasta que el diseño rompa, y pon el corte ahí. 600, 768 y 1024 px son puntos de partida, no leyes.

!!! comprueba "Comprueba"
    1. ¿Hace falta un HTML distinto para el móvil si usas media queries?
    2. ¿`max-width: 768px` se cumple en 800 px o en 700 px?
    3. ¿Qué propiedad de Flexbox cambia un menú de fila a columna?

# Anexo A. Glosario

| Término | Significado |
|---|---|
| Layout | Colocación de las cajas en la página |
| Responsive | El mismo HTML se reorganiza según el ancho |
| Contenedor flex | Elemento con `display: flex` |
| Ítem flex | Hijo directo de un contenedor flex |
| Eje principal | Dirección de `flex-direction` |
| `fr` | Fracción del espacio libre en Grid |
| Área | Región con nombre en `grid-template-areas` |
| Media query | Bloque `@media` que aplica CSS según el viewport |
| Breakpoint | Ancho en el que cambia el layout |

# Anexo B. Mapa

```text
Mismo HTML
  -> Flexbox (1 dimensión): menú, fila de tarjetas
  -> Grid (2 dimensiones): página entera, tablero, áreas
  -> @media (max-width / min-width): cambia direction, columnas, tipo
```

# Anexo C. Autoevaluación

## Preguntas cortas

1. ¿Qué problema resuelve el diseño responsive que no resuelve hacer tres HTML?
2. Cita tres propiedades del contenedor flex y di qué hace cada una.
3. ¿Qué es `flex: 1`?
4. ¿En qué se diferencia Grid de Flexbox?
5. Escribe una media query que ponga `flex-direction: column` por debajo de 600 px.

## Tipo test

1. `justify-content` reparte el espacio:
    - a) En el eje cruzado
    - b) En el eje principal
    - c) Solo si hay `flex-wrap: wrap`
    - d) Entre el padding y el borde
2. `align-content`:
    - a) Alinea un ítem suelto
    - b) Alinea las líneas cuando hay wrap
    - c) Es lo mismo que `align-items`
    - d) Cambia el eje principal
3. En Grid, `1fr 2fr` en un contenedor de 300 px (sin gap) mide:
    - a) 100 px y 200 px
    - b) 150 px y 150 px
    - c) 1 px y 2 px
    - d) 300 px y 600 px

## Razona

Una tienda tiene cabecera, menú, listado de productos (tres por fila en portátil, uno en móvil) y un pie. Di qué pondrías en Grid, qué en Flexbox y qué media query escribirías. No hace falta el CSS entero: el criterio.
