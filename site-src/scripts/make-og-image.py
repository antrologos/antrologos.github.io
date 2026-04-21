"""Generate polished Open Graph image for Transcritorio site.

Output: site-src/public/img/og-image.png (1200x630).
"""
from __future__ import annotations

import math
import random
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont, ImageFilter

W, H = 1200, 630
BG_TOP = (11, 17, 26)       # #0b111a
BG_BOTTOM = (16, 25, 38)    # slightly lighter
ACCENT = (68, 215, 182)     # #44d7b6
ACCENT_DIM = (68, 215, 182, 40)
TEXT_PRIMARY = (247, 247, 242)
TEXT_MUTED = (167, 176, 189)
TEXT_FAINT = (107, 116, 128)
CARD_BG = (17, 26, 38)
CARD_BORDER = (247, 247, 242, 22)


def vertical_gradient(size, top, bottom):
    img = Image.new("RGB", size, top)
    draw = ImageDraw.Draw(img)
    w, h = size
    for y in range(h):
        t = y / max(1, h - 1)
        r = int(top[0] * (1 - t) + bottom[0] * t)
        g = int(top[1] * (1 - t) + bottom[1] * t)
        b = int(top[2] * (1 - t) + bottom[2] * t)
        draw.line([(0, y), (w, y)], fill=(r, g, b))
    return img


def radial_glow(size, center, radius, color, alpha):
    w, h = size
    layer = Image.new("RGBA", size, (0, 0, 0, 0))
    draw = ImageDraw.Draw(layer)
    cx, cy = center
    for i in range(60, 0, -1):
        r = int(radius * i / 60)
        a = int(alpha * (i / 60) ** 2)
        draw.ellipse(
            [(cx - r, cy - r), (cx + r, cy + r)],
            fill=(color[0], color[1], color[2], a),
        )
    return layer.filter(ImageFilter.GaussianBlur(30))


def load_font(size, bold=False):
    candidates = []
    if bold:
        candidates += [
            r"C:\Windows\Fonts\segoeuib.ttf",
            r"C:\Windows\Fonts\arialbd.ttf",
        ]
    candidates += [
        r"C:\Windows\Fonts\segoeui.ttf",
        r"C:\Windows\Fonts\arial.ttf",
    ]
    for p in candidates:
        if Path(p).exists():
            return ImageFont.truetype(p, size)
    return ImageFont.load_default()


def draw_waveform(img, x, y, width, height, bars=42):
    draw = ImageDraw.Draw(img, "RGBA")
    random.seed(7)
    bar_w = 5
    gap = (width - bars * bar_w) // max(1, bars - 1)
    for i in range(bars):
        t = i / (bars - 1)
        env = math.sin(math.pi * t) ** 0.8
        noise = 0.7 + 0.3 * random.random()
        h = int(height * env * noise)
        bx = x + i * (bar_w + gap)
        by = y + (height - h) // 2
        draw.rounded_rectangle(
            [bx, by, bx + bar_w, by + h],
            radius=2,
            fill=ACCENT + (235,),
        )


def draw_mock_ui_card(img, x, y, w, h):
    """Draws a small stylized Transcritorio turn-list card."""
    card = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    d = ImageDraw.Draw(card)

    # Card background
    d.rounded_rectangle([0, 0, w - 1, h - 1], radius=18, fill=CARD_BG)
    # 1px border
    d.rounded_rectangle([0, 0, w - 1, h - 1], radius=18, outline=(247, 247, 242, 30), width=1)

    # Mock titlebar with 3 dots
    bar_h = 28
    d.rounded_rectangle([0, 0, w - 1, bar_h], radius=18, fill=(26, 36, 48))
    d.rectangle([0, bar_h // 2, w - 1, bar_h], fill=(26, 36, 48))
    for i, color in enumerate([(255, 95, 87), (254, 188, 46), (40, 200, 64)]):
        cx = 16 + i * 16
        cy = bar_h // 2
        d.ellipse([cx - 5, cy - 5, cx + 5, cy + 5], fill=color)

    # Rows mimicking speaker turns
    pad = 20
    row_h = 34
    row_y = bar_h + 16
    font_small = load_font(12, bold=True)
    for i in range(5):
        ry = row_y + i * row_h
        # Speaker badge
        label = "Entrevistador" if i % 2 == 0 else "Entrevistada"
        badge_w = 110
        badge_color = ACCENT + (60,) if i % 2 == 0 else (122, 167, 255, 60)
        text_color = ACCENT if i % 2 == 0 else (122, 167, 255)
        d.rounded_rectangle(
            [pad, ry, pad + badge_w, ry + 22],
            radius=6,
            fill=badge_color,
        )
        d.text((pad + 8, ry + 4), label, font=font_small, fill=text_color)
        # Fake transcript line
        line_colors = [(200, 210, 225), (180, 190, 205), (170, 180, 195)]
        for j in range(2):
            ly = ry + 4 + j * 10
            lw = w - (pad + badge_w + 16 + pad) - random.randint(0, 40)
            d.rounded_rectangle(
                [pad + badge_w + 16, ly, pad + badge_w + 16 + lw, ly + 4],
                radius=2,
                fill=(*line_colors[j], 120),
            )

    # Soft outer shadow
    shadow = Image.new("RGBA", (w + 80, h + 80), (0, 0, 0, 0))
    sd = ImageDraw.Draw(shadow)
    sd.rounded_rectangle([40, 40, w + 40, h + 40], radius=18, fill=(0, 0, 0, 170))
    shadow = shadow.filter(ImageFilter.GaussianBlur(24))
    img.alpha_composite(shadow, (x - 40, y - 40 + 12))
    img.alpha_composite(card, (x, y))


def main():
    base = vertical_gradient((W, H), BG_TOP, BG_BOTTOM).convert("RGBA")

    # Radial glow upper-right (accent)
    glow = radial_glow((W, H), (int(W * 0.82), int(H * 0.3)), 420, ACCENT, 80)
    base.alpha_composite(glow)

    draw = ImageDraw.Draw(base)

    # Left column: title and subtitle
    left_x = 72
    # Accent vertical bar
    bar_w = 6
    bar_h = 110
    bar_y = 180
    draw.rounded_rectangle(
        [left_x, bar_y, left_x + bar_w, bar_y + bar_h],
        radius=3,
        fill=ACCENT,
    )

    font_title = load_font(84, bold=True)
    font_subtitle = load_font(30)
    font_footer = load_font(20)
    font_tag = load_font(18, bold=True)

    # Title
    title_x = left_x + 28
    title_y = 172
    draw.text((title_x, title_y), "Transcritório", font=font_title, fill=TEXT_PRIMARY)

    # Subtitle (2 lines)
    sub_y = title_y + 116
    draw.text((title_x, sub_y), "Transcrição local de entrevistas", font=font_subtitle, fill=TEXT_MUTED)
    draw.text((title_x, sub_y + 40), "em português brasileiro", font=font_subtitle, fill=TEXT_MUTED)

    # "100% LOCAL" tag chip (separate layer for proper alpha compositing)
    chip_label = "100% LOCAL  ·  SEM NUVEM"
    bbox = draw.textbbox((0, 0), chip_label, font=font_tag)
    chip_tw = bbox[2] - bbox[0]
    chip_th = bbox[3] - bbox[1]
    chip_pad_x = 16
    chip_pad_y = 8
    chip_w = chip_tw + 2 * chip_pad_x
    chip_h = chip_th + 2 * chip_pad_y
    chip_x = title_x
    chip_y = 108
    chip_radius = chip_h // 2
    chip_layer = Image.new("RGBA", (chip_w, chip_h), (0, 0, 0, 0))
    cd = ImageDraw.Draw(chip_layer)
    cd.rounded_rectangle(
        [0, 0, chip_w - 1, chip_h - 1],
        radius=chip_radius,
        fill=(68, 215, 182, 50),
    )
    cd.text(
        (chip_pad_x, chip_pad_y - bbox[1]),
        chip_label,
        font=font_tag,
        fill=ACCENT + (255,),
    )
    base.alpha_composite(chip_layer, (chip_x, chip_y))

    # Right column: mock UI card
    card_w, card_h = 440, 260
    card_x = W - card_w - 72
    card_y = 175
    draw_mock_ui_card(base, card_x, card_y, card_w, card_h)

    # Waveform under the card
    wave_y = card_y + card_h + 28
    draw_waveform(base, card_x, wave_y, card_w, 40)

    # Footer separator
    draw.line([(72, H - 92), (W - 72, H - 92)], fill=(247, 247, 242, 25), width=1)

    # Footer row
    footer_y = H - 58
    draw.text((72, footer_y), "antrologos.github.io/Transcritorio", font=font_footer, fill=TEXT_FAINT)
    draw.text((72 + 360, footer_y), "·  MIT  ·  Windows / macOS / Linux", font=font_footer, fill=TEXT_FAINT)

    # Save
    out_path = Path(__file__).resolve().parent.parent / "public" / "img" / "og-image.png"
    out_path.parent.mkdir(parents=True, exist_ok=True)
    base.convert("RGB").save(out_path, "PNG", optimize=True)
    print(f"Wrote {out_path} ({out_path.stat().st_size} bytes)")


if __name__ == "__main__":
    main()
