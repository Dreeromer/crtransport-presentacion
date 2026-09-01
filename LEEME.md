# CR Transport — presentación web

Carta de presentación de CR Transport (CR Proveedores Industriales SAC) en
formato web. Reemplaza al PDF de 7 páginas.

**Versión 2 (1 set 2026)** — incorpora las correcciones que Renato mandó por
WhatsApp. Ver *Qué cambió en la v2* al final.

Un solo archivo (`index.html`) con todo el CSS y el JavaScript dentro, más las
carpetas `img/` y `fonts/`. No usa librerías ni conexión a internet: se abre
igual desde un servidor, desde una USB o sin señal.

---

## ⚠️ Antes de enseñársela al cliente

### ✅ El contacto ya está activo

Teléfono **944 600 229**, correo **Rmenacho@transport-cr.com**, dirección
**Av. Las Artes 1286 — San Borja, Lima**. Las constantes `WHATSAPP` y `CORREO`
del final de `index.html` ya están completas, así que el formulario arma el
mensaje y lo abre en WhatsApp (o en el correo) con los datos ya escritos.

### ✅ Ya no queda nada pendiente

La página no tiene ningún dato marcado como "por confirmar". La tabla de flota
lista los tipos de unidad, su capacidad y para qué se usa cada una, **sin decir
cuántas unidades hay de cada tipo** — decisión del cliente.

Si alguna vez hace falta volver a marcar un dato como pendiente, la clase `.tbc`
sigue en el CSS: pinta el texto en ámbar con subrayado punteado.

```html
<span class="tbc" title="Falta el dato">por confirmar</span>
```

---

## Cosas que conviene decirle al cliente

- **Hay dos logos conviviendo.** El de la portada del PDF (isotipo azul y verde,
  "CR TRANSPORT" en arco) no es el mismo que está rotulado en las unidades
  ("CR transport — Centro Logístico de Transporte"). La web usa el primero.
  Habría que definir cuál es el vigente y rotular en consecuencia.
- **El logo está en mapa de bits**, sacado del PDF. Para impresión o para una
  versión más grande hace falta el vector (.ai, .eps o .svg).
- **Las fotos son las que él mismo mandó** por WhatsApp el 1 de setiembre de
  2026 (`img/n-*.webp`). Las del PDF quedaron fuera porque se veían mal, que era
  justamente una de sus observaciones. Siguen siendo fotos de celular: si quiere
  subir el nivel, vale la pena una sesión de fotos de la flota y del almacén.
- **A la foto de Condorcocha se le recortó** la marca de fecha/GPS que traía
  quemada en la esquina.
- **Falta el sector minería en el material original.** Él lo mencionó en el
  audio pero no estaba en el PDF; aquí sí aparece.
- **Se quitó la lámina de Trazabilidad** a pedido suyo. El seguimiento GPS
  sigue mencionado en Quiénes somos y en Flota, pero ya no hay sección propia ni
  el dato de "4 sistemas". Si algún día la quiere de vuelta, está en el
  historial de git (commit anterior).
- **El almacén de Chiclayo dejó de ser lámina propia** y ahora va dentro de
  Cobertura, también a pedido suyo. Ojo: en el audio del 28 de agosto el almacén
  era el eje del encargo, así que conviene confirmárselo en la reunión.

---

## Cómo verla

Doble clic en `index.html` funciona, pero para verla como se va a publicar:

```
cd ~/Desktop/CRTransport-Presentacion
python3 -m http.server 8000
```

y abre `http://127.0.0.1:8000` (con `127.0.0.1`, no con `file://`).

---

## Cómo está armada

| Sección | Qué hace |
|---|---|
| Portada | Escena 3D: la calzada en fuga y las unidades flotando en profundidad |
| Cifras | Desde 2016, 5 ciudades, 1.5–32 t |
| Quiénes somos | Misión, visión y ficha de datos + foto con inclinación al pasar el cursor |
| Servicios | Los cuatro frentes, cada uno con su tipo de unidad |
| Flota | Sección anclada: recorrido en profundidad por las unidades + tabla |
| Cobertura | Esquema del corredor norte + el almacén propio de Chiclayo |
| Sectores | Minería, agroindustria y retail |
| Equipo | Personal propio |
| Clientes | Los 9 logos, en gris hasta que pasas el cursor |
| Contacto | Formulario que abre WhatsApp con el mensaje escrito |

**El riel de la izquierda** es la ruta: avanza con el scroll y va encendiendo
cada sección como si fueran paradas.

Detalles técnicos: una sola curva de animación y cuatro duraciones para toda la
página; un único bucle `requestAnimationFrame` para todo lo que va atado al
scroll; en pantallas de menos de 760 px los recorridos anclados se convierten en
contenido normal; y si el sistema tiene activado "reducir movimiento", se apaga
todo lo que se mueve.

---

## Publicar

Igual que la de AV Perú: subir la carpeta a un repositorio y activar GitHub
Pages. El archivo `.nojekyll` ya está puesto para que no se salte nada.


---

## Qué cambió en la v2 (1 set 2026)

Observaciones que mandó Renato por WhatsApp, y qué se hizo con cada una:

| Pidió | Se hizo |
|---|---|
| Empezar con un resumen de "¿Quiénes somos?" | La portada y la sección Empresa arrancan con la idea de 2016 y la operación nacional; se agregaron Misión y Visión |
| Corregir 1.5 a 32 toneladas | Cambiado en cifras, en el rótulo de Flota, en la tabla y en el texto |
| Borrar el dato de sistemas de trazabilidad | Fuera; las cifras quedaron en tres |
| Es CR Proveedores Industriales SAC, sin "Selva" | Corregido en portada, ficha, contacto y pie |
| "Flota propia; personal y conductores capacitados y seguimiento de GPS" | Es la bajada de Quiénes somos y el rótulo de la foto |
| Cambiar la imagen de la lámina 2 | Ahora va la cama baja cargada frente a la nave |
| Lámina 4: corregir las imágenes que no se ven bien | Todas las fotos del PDF fueron reemplazadas por las suyas |
| Agregar traslado de camiones cama baja y sobredimensionada | Tarjeta propia en Servicios, unidad propia en Flota y fila propia en la tabla |
| Borrar lo del almacén y pasarlo a cobertura | Hecho: la lámina anclada del almacén desapareció; queda un bloque dentro de Cobertura |
| Sacar la lámina de trazabilidad | Hecha fuera, junto con su ítem del menú |
| Equipo de trabajo: otro texto más imponente | Redactado de nuevo ("El que sube a la unidad es el que responde por la carga") |
| Más ilustrativa, menos texto | Se recortaron párrafos en Quiénes somos, Servicios y Almacén |

**Su audio del 1 set (0:19)** no traía instrucciones: solo aclara que las fotos
son de carga pesada y sobredimensionada del sector industrial y minero, y
pregunta si hacen falta más.

### Peso en celular

Cada foto existe en tres tamaños — `n-*-sm.webp` (800 px), `n-*-md.webp`
(1200 px) y la original (hasta 1600 px) — y el `srcset` de cada `<img>` deja que
el navegador elija según el ancho de pantalla. En un celular la carga inicial
baja a **~286 KB** (las cuatro fotos de la portada en versión chica más los
logos de clientes); el resto entra por `loading="lazy"` conforme se hace scroll.

Si cambias una foto, acuérdate de regenerar sus dos variantes y de actualizar el
`srcset`; si no, el celular se bajará la original completa.


---

## Correcciones de la v2.1

- **Se quitaron las repeticiones.** "Desde 2016" y el rango "1.5 a 32 t" ahora
  aparecen una sola vez cada uno, en la fila de cifras. Los textos de portada,
  Quiénes somos y Flota ya no los repiten (el rango sigue en la tabla de flota,
  desglosado por tipo de unidad, que es donde sirve).
- **Bug corregido en iPhone.** Las fotos de la sección Flota se estiraban a la
  altura de la pantalla y se veía solo el fondo. La causa: `.card img` tiene
  `height:100%` y la tarjeta de esa sección no tenía altura definida — Chrome lo
  resuelve con el `aspect-ratio` de la imagen, pero WebKit (el motor de Safari y
  de Chrome en iPhone) lo resuelve contra el viewport. Se arregló poniendo
  `aspect-ratio:16/10` en `.fleet__slab .card`.
  **Cuidado al añadir tarjetas nuevas:** si usas `.card` con una imagen dentro,
  la tarjeta necesita `aspect-ratio` o `min-height`, o se romperá igual en iOS.
- **Título de Equipo nuevo:** "La carga no la mueve la flota, la mueve la gente".
- **Botones de contacto arreglados.** El de "Escribir por WhatsApp" nacía con
  `href="#"` y solo se armaba cuando el visitante escribía algo: si lo tocabas
  al llegar, abría una pestaña en blanco. Ahora nace ya apuntando a WhatsApp con
  un mensaje genérico y se va enriqueciendo conforme se llena el formulario.
  "Enviar consulta" abre la pestaña nueva y, si el navegador la bloquea (pasa en
  iPhone), navega en la misma en vez de no hacer nada; además la nota de
  respuesta deja un enlace directo por si acaso.

Probado con WebKit a 390×844 (iPhone): las alturas de todas las imágenes
coinciden ya con las de Chrome.
