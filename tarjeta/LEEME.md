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

## Pendiente

- **Cargo de Renato**: no está puesto en la tarjeta porque no lo teníamos confirmado.
