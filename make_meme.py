#!/usr/bin/env python3
"""Compose the GTA 6 meme for the make.fun bounty gta6-meme-x-01.

The base scene (assets/scene.png) is an AI-generated illustration of
make.fun's ghost mascot — white ghost, thick black outline, sparkle eyes,
magenta star coin — standing on a Vice City beach at sunset, drawn from
the official press mark (https://make.fun/press/). This script adds the
meme caption in large bold letters so it stays readable when the picture
is shrunk to 480x480, which is how the judge sees it.

The joke: GTA fans waited thirteen years since GTA V for GTA 6. The ghost
died waiting — and still showed up for launch week.
"""

from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

HERE = Path(__file__).resolve().parent
SCENE = HERE / "assets" / "scene.png"
OUT = HERE / "meme.png"
FONT_PATH = "/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf"

TOP_LINE = "WAITED 13 YEARS FOR GTA 6"
BOTTOM_LINES = ["DIED. STILL SHOWED UP", "FOR LAUNCH WEEK."]


def fit_font(draw: ImageDraw.ImageDraw, text: str, max_width: int, start: int) -> ImageFont.FreeTypeFont:
    """Largest font size (from `start` down) whose rendered text fits max_width."""
    size = start
    while size > 10:
        font = ImageFont.truetype(FONT_PATH, size)
        left, _, right, _ = draw.textbbox((0, 0), text, font=font, stroke_width=max(2, size // 14))
        if right - left <= max_width:
            return font
        size -= 4
    return ImageFont.truetype(FONT_PATH, size)


def draw_caption(draw: ImageDraw.ImageDraw, text: str, center_y: int, img_w: int) -> int:
    """Draw one centered caption line; return the y just below it."""
    font = fit_font(draw, text, int(img_w * 0.92), start=150)
    stroke = max(3, font.size // 13)
    draw.text(
        (img_w // 2, center_y),
        text,
        font=font,
        fill=(255, 255, 255),
        stroke_width=stroke,
        stroke_fill=(0, 0, 0),
        anchor="mm",
    )
    return center_y + font.size // 2 + stroke + 6


def main() -> None:
    img = Image.open(SCENE).convert("RGB")
    w, h = img.size
    draw = ImageDraw.Draw(img)

    # Top caption sits in the sunset sky.
    draw_caption(draw, TOP_LINE, int(h * 0.085), w)

    # Bottom caption sits on the empty sand, stacked so it stays big.
    y = int(h * 0.862)
    for line in BOTTOM_LINES:
        font = fit_font(draw, line, int(w * 0.92), start=140)
        stroke = max(3, font.size // 13)
        draw.text(
            (w // 2, y),
            line,
            font=font,
            fill=(255, 255, 255),
            stroke_width=stroke,
            stroke_fill=(0, 0, 0),
            anchor="mm",
        )
        y += font.size + stroke * 2 + 10

    img.save(OUT, "PNG", optimize=True)
    print(f"wrote {OUT} ({w}x{h}, {OUT.stat().st_size} bytes)")


if __name__ == "__main__":
    main()
