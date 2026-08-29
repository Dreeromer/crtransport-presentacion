# CR Transport — presentación web

Carta de presentación de CR Transport (CR Proveedores Industriales Selva SAC)
en formato web. Reemplaza al PDF de 7 páginas.

Un solo archivo (`index.html`) con todo el CSS y el JavaScript dentro, más las
carpetas `img/` y `fonts/`. No usa librerías ni conexión a internet: se abre
igual desde un servidor, desde una USB o sin señal.

---

## ⚠️ Antes de enseñársela al cliente

Hay dos cosas pendientes. La primera es obligatoria.

### 1. Activar el contacto (obligatorio)

Abre `index.html`, busca `PASO OBLIGATORIO` (está casi al final) y completa:

```js
var WHATSAPP = "";      /* ← ejemplo: "51987654321" (país + número, sin signos) */
var CORREO   = "";      /* ← ejemplo: "comercial@crtransport.pe" */
```

Mientras estén vacías, el botón de WhatsApp aparece apagado y el formulario
avisa que el canal todavía no está activo. Con el número puesto, el formulario
arma el mensaje y lo abre en WhatsApp con los datos ya escritos.

### 2. Completar los datos en ámbar

En la página hay 8 datos marcados en color ámbar con subrayado punteado que
dicen **"por confirmar"**. Son los que CR Transport no puso en su PDF y que
hacen falta para que la página venda:

| Dónde | Qué falta |
|---|---|
| Almacén Chiclayo | Área techada en m² |
| Almacén Chiclayo | Altura libre en metros |
| Almacén Chiclayo | Número de portones / accesos |
| Almacén Chiclayo | Dirección |
| Flota | N.º de furgonetas y vans |
| Flota | N.º de camiones furgón |
| Flota | N.º de semitrailers y plataformas |
| Contacto | Teléfono, correo y dirección |

Para cambiarlos, busca `class="tbc"` en el archivo y reemplaza el texto por el
dato real. Cuando pongas el dato, quita también `class="tbc"` para que deje de
salir en ámbar:

```html
<!-- antes -->
<span class="tbc" title="Falta el dato">m² por confirmar</span>
<!-- después -->
<span>1,200 m²</span>
```

Lo mismo en el plano del almacén: los textos `Largo · por confirmar`,
`Ancho · por confirmar` y `Altura libre · por confirmar` están dentro del
`<svg>`; cámbialos por las medidas reales y quítales `class="t-amber"`.

---

## Cosas que conviene decirle al cliente

- **Hay dos logos conviviendo.** El de la portada del PDF (isotipo azul y verde,
  "CR TRANSPORT" en arco) no es el mismo que está rotulado en las unidades
  ("CR transport — Centro Logístico de Transporte"). La web usa el primero.
  Habría que definir cuál es el vigente y rotular en consecuencia.
- **El logo está en mapa de bits**, sacado del PDF. Para impresión o para una
  versión más grande hace falta el vector (.ai, .eps o .svg).
- **Las fotos son las del PDF**, corregidas de color, ampliadas y unificadas en
  un mismo tratamiento. Son fotos de celular: si quiere subir el nivel, vale la
  pena una sesión de fotos de la flota y del almacén.
- **Falta el sector minería en el material original.** Él lo mencionó en el
  audio pero no estaba en el PDF; aquí sí aparece.
- **La hoja de ruta de la sección Trazabilidad es un ejemplo reconstruido** a
  partir del reporte real que salía fotografiado en el PDF. Mantiene los
  distritos y los conteos, pero sin placas ni nombres de conductores.

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
| Cifras | Contadores: 9 años, 5 ciudades, 1.5–26 t, 4 sistemas |
| Empresa | Ficha de datos + foto de unidad con inclinación al pasar el cursor |
| Servicios | Los cuatro frentes, cada uno con su tipo de unidad |
| Almacén Chiclayo | Sección anclada: la nave se acerca y el plano se dibuja con el scroll |
| Flota | Sección anclada: recorrido en profundidad por las unidades + tabla |
| Cobertura | Esquema del corredor norte con coordenadas y distancias reales |
| Sectores | Minería, agroindustria y retail |
| Trazabilidad | Las 4 plataformas + hoja de ruta de ejemplo |
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
