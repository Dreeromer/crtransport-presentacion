# Tarjeta de presentación digital — CR Transport

**URL:** https://dreeromer.github.io/crtransport-presentacion/tarjeta/

Esa es la dirección que se graba en el tag NFC y la que codifica el QR de la propia página.

## Cómo grabar el tag NFC (una sola vez, desde el iPhone)

1. Compra tags **NTAG215** — tarjeta PVC blanca o sticker. En Perú se consiguen entre S/3 y S/8; en AliExpress salen a menos de S/1 comprando 10.
2. Instala **NFC Tools** (gratis, App Store).
3. Abre → *Escribir* → *Añadir un registro* → **URL/URI**.
4. Pega `https://dreeromer.github.io/crtransport-presentacion/tarjeta/` y toca *OK* → *Escribir*.
5. Acerca el tag a la parte superior del iPhone hasta que confirme.
6. Opcional: *Otros* → *Bloquear el tag* para que nadie pueda reescribirlo. **Es irreversible.**

## Cómo se usa

Acerca la tarjeta a la parte de arriba del celular del cliente. Le salta una notificación con el enlace; toca y se abre la tarjeta. Funciona sin app en **iPhone XS o posterior** y en casi todo Android reciente. Quien no tenga NFC escanea el QR del pie.

## Editar los datos

- Contenido y diseño: `index.html`.
- Lo que se guarda en Contactos: `contacto.vcf` (los dos hay que actualizarlos si cambia un dato).
- Publicar cambios: `git add tarjeta && git commit && git push`. GitHub Pages tarda ~1 minuto.

Como la URL nunca cambia, el tag ya grabado sigue sirviendo aunque se edite todo lo demás.

## Fondo de pantalla con QR

En `wallpapers/` hay tres versiones del fondo de bloqueo, ya con el logo dentro del QR:

| Archivo | Para |
|---|---|
| `fondo-ProMax-1290x2796.png` | iPhone 14/15/16 Pro Max, y Plus |
| `fondo-Pro-1179x2556.png` | iPhone 14/15/16 Pro |
| `fondo-iPhone-1170x2532.png` | iPhone 11/12/13/14 estándar |
| `qr-crtransport-2200px.png` | El QR solo, para imprimir, vinilar o pegar en el camión |

**Cómo ponerlo:** guarda la imagen en Fotos → Ajustes → Fondo de pantalla → Añadir nuevo fondo → Fotos → elígela → *Añadir* → *Definir como pareja de fondos*.

El QR está colocado por debajo del reloj y por encima de los botones de linterna y cámara, así que no lo tapa nada. Verificado: decodifica incluso reducido al 25%, o sea que se escanea de lejos y a través de la pantalla.

Para regenerarlos si cambia la URL: `python3 gen-wallpapers.py` (necesita `pip3 install qrcode pillow fonttools brotli`).

## Corregido el 2026-09-05

El correo estaba con el dominio invertido (`transport-cr.com`). Lo correcto es **rmenacho@cr-transport.com** y ya está arreglado tanto en la tarjeta como en la presentación.
