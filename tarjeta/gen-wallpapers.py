from PIL import Image, ImageDraw, ImageFont
import qrcode
from qrcode.constants import ERROR_CORRECT_H

F = "/tmp/claude-501/-Users-andree/4bc9ab97-45fd-470c-94b0-8f529f3a21a3/scratchpad/f/"
URL = "https://dreeromer.github.io/crtransport-presentacion/tarjeta/"
NIGHT, PANEL, BONE, LIME, MUTED, DIM = (6,11,28), (12,21,51), (231,236,247), (168,204,85), (147,160,192), (95,109,145)

def archivo(size, wght=800, wdth=112):
    f = ImageFont.truetype(F+"Archivo.ttf", size)
    f.set_variation_by_axes([wght, wdth]); return f
def mono(size):
    return ImageFont.truetype(F+"PlexMono.ttf", size)

def tw(d, font, text, track):
    w = 0
    for ch in text: w += d.textlength(ch, font=font) + track
    return w - track if text else 0

def draw_tracked(d, xy, text, font, fill, track=0, anchor_center=False):
    x, y = xy
    if anchor_center: x -= tw(d, font, text, track) / 2
    for ch in text:
        d.text((x, y), ch, font=font, fill=fill)
        x += d.textlength(ch, font=font) + track

def make_qr(px, logo_path):
    q = qrcode.QRCode(version=None, error_correction=ERROR_CORRECT_H, box_size=10, border=2)
    q.add_data(URL); q.make(fit=True)
    img = q.make_image(fill_color=NIGHT, back_color=BONE).convert("RGB").resize((px, px), Image.NEAREST)
    # Logo al centro, sobre pastilla clara con aire
    lg = Image.open(logo_path).convert("RGBA")
    side = int(px * 0.235)
    pad  = int(side * 0.13)
    plate = Image.new("RGBA", (side, side), (0,0,0,0))
    ImageDraw.Draw(plate).rounded_rectangle([0,0,side-1,side-1], radius=int(side*0.20), fill=BONE+(255,))
    inner = side - pad*2
    lg = lg.resize((inner, inner), Image.LANCZOS)
    plate.paste(lg, (pad, pad), lg)
    img = img.convert("RGBA")
    img.alpha_composite(plate, ((px-side)//2, (px-side)//2))
    return img.convert("RGB")

def wallpaper(W, H, logo_path, out):
    img = Image.new("RGB", (W, H), NIGHT)
    d = ImageDraw.Draw(img)
    # degradado vertical: panel arriba -> noche abajo
    for y in range(H):
        t = (y / H) ** 0.75
        d.line([(0,y),(W,y)], fill=tuple(int(PANEL[i] + (NIGHT[i]-PANEL[i]) * t) for i in range(3)))
    # grano
    noise = Image.effect_noise((W, H), 16).convert("L")
    img = Image.composite(img, Image.blend(img, Image.merge("RGB",(noise,noise,noise)), .055), Image.new("L",(W,H),0))
    img = Image.blend(img, Image.merge("RGB",(noise,noise,noise)), .045)
    d = ImageDraw.Draw(img)

    # ── QR en pastilla, dentro de la zona segura de la pantalla de bloqueo ──
    plate_side = int(W * 0.70)
    qr_side    = int(plate_side * 0.82)
    px, py = (W - plate_side)//2, int(H * 0.335)
    d.rounded_rectangle([px, py, px+plate_side, py+plate_side], radius=int(plate_side*0.075), fill=BONE)
    img.paste(make_qr(qr_side, logo_path), (px + (plate_side-qr_side)//2, py + (plate_side-qr_side)//2))

    # ── Textos bajo el QR ──
    cx = W // 2
    y = py + plate_side + int(H * 0.048)

    f_name = archivo(int(W*0.072), 800, 112)
    for line in ["RENATO MENACHO", "ALVAREZ"]:
        draw_tracked(d, (cx, y), line, f_name, BONE, track=-int(W*0.0012), anchor_center=True)
        y += int(f_name.size * 1.02)

    y += int(H * 0.016)
    f_role = mono(int(W*0.028))
    draw_tracked(d, (cx, y), "GERENTE GENERAL", f_role, LIME, track=W*0.0055, anchor_center=True)
    y += int(f_role.size * 2.0)

    # riel lima
    rw = int(W * 0.30)
    d.line([(cx-rw//2, y), (cx+rw//2, y)], fill=(26,38,80), width=max(1,int(H*0.0009)))
    d.ellipse([cx-int(W*0.006), y-int(W*0.006), cx+int(W*0.006), y+int(W*0.006)], fill=LIME)
    y += int(H * 0.026)

    f_cap = mono(int(W*0.0255))
    draw_tracked(d, (cx, y), "ESCANEA PARA GUARDAR MI CONTACTO", f_cap, MUTED, track=W*0.0028, anchor_center=True)
    y += int(f_cap.size * 1.85)
    draw_tracked(d, (cx, y), "CR TRANSPORT  ·  CARGA TERRESTRE", f_cap, DIM, track=W*0.0028, anchor_center=True)

    img.save(out, "PNG"); print("→", out, f"{W}x{H}")

LOGO = "img/cr-logo.webp"
for W, H, tag in [(1290,2796,"ProMax-1290x2796"), (1179,2556,"Pro-1179x2556"), (1170,2532,"iPhone-1170x2532")]:
    wallpaper(W, H, LOGO, f"tarjeta/wallpapers/fondo-{tag}.png")

# QR suelto en alta, para imprimir o pegar
qr = make_qr(2000, LOGO)
canvas = Image.new("RGB", (2200,2200), BONE)
canvas.paste(qr, (100,100)); canvas.save("tarjeta/wallpapers/qr-crtransport-2200px.png","PNG")
print("→ qr-crtransport-2200px.png")
