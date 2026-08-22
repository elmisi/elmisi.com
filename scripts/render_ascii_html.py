#!/usr/bin/env python3
"""Convert a bitmap into a standalone HTML image made only of ASCII glyphs."""

from __future__ import annotations

import argparse
import html
from pathlib import Path

from PIL import Image, ImageEnhance, ImageOps


GLYPHS = " .,:;+=xX$#@"
COLORS = (
    "#0a0e14",
    "#0b2814",
    "#105021",
    "#18752e",
    "#229b3c",
    "#39d353",
    "#78e889",
    "#d7ffdc",
)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("source", type=Path)
    parser.add_argument("output", type=Path)
    parser.add_argument("--columns", type=int, default=180)
    parser.add_argument("--height-scale", type=float, default=0.62)
    parser.add_argument("--title", default="ASCII image")
    parser.add_argument("--alt", default="")
    return parser.parse_args()


def crop_to_subject(image: Image.Image) -> Image.Image:
    """Trim mostly empty black margins while ignoring isolated dim particles."""
    probe = ImageOps.grayscale(image.copy())
    probe.thumbnail((640, 640), Image.Resampling.LANCZOS)
    mask = probe.point(lambda value: 255 if value >= 20 else 0)
    width, height = mask.size
    pixels = mask.load()
    min_column_pixels = max(2, round(height * 0.01))
    min_row_pixels = max(2, round(width * 0.01))
    columns = [
        x for x in range(width)
        if sum(pixels[x, y] > 0 for y in range(height)) >= min_column_pixels
    ]
    rows = [
        y for y in range(height)
        if sum(pixels[x, y] > 0 for x in range(width)) >= min_row_pixels
    ]
    if not columns or not rows:
        return image

    scale_x = image.width / width
    scale_y = image.height / height
    left = round(columns[0] * scale_x)
    top = round(rows[0] * scale_y)
    right = round((columns[-1] + 1) * scale_x)
    bottom = round((rows[-1] + 1) * scale_y)
    pad_x = round((right - left) * 0.04)
    pad_y = round((bottom - top) * 0.08)
    box = (
        max(0, left - pad_x),
        max(0, top - pad_y),
        min(image.width, right + pad_x),
        min(image.height, bottom + pad_y),
    )
    return image.crop(box)


def render_row(values: list[int]) -> str:
    parts: list[str] = []
    active_level: int | None = None
    run: list[str] = []

    def flush() -> None:
        if active_level is not None and run:
            parts.append(f'<span class="p{active_level}">{html.escape("".join(run))}</span>')
            run.clear()

    for value in values:
        glyph_index = round(value / 255 * (len(GLYPHS) - 1))
        glyph = GLYPHS[glyph_index]
        level = min(len(COLORS) - 1, value * len(COLORS) // 256)
        if level != active_level:
            flush()
            active_level = level
        run.append(glyph)
    flush()
    return "".join(parts)


def main() -> None:
    args = parse_args()
    source = Image.open(args.source).convert("RGB")
    rows = max(1, round(source.height / source.width * args.columns * args.height_scale))
    source = crop_to_subject(source)
    image = source.resize((args.columns, rows), Image.Resampling.LANCZOS)
    luminance = ImageOps.grayscale(image)
    luminance = ImageOps.autocontrast(luminance, cutoff=(1, 1))
    luminance = ImageEnhance.Contrast(luminance).enhance(1.18)

    pixels = list(luminance.getdata())
    art = "\n".join(
        render_row(pixels[offset : offset + args.columns])
        for offset in range(0, len(pixels), args.columns)
    )
    palette = "\n".join(
        f"      .p{index} {{ color: {color}; }}"
        for index, color in enumerate(COLORS)
    )
    document = f"""<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>{html.escape(args.title)}</title>
    <style>
      @font-face {{
        font-family: "JetBrains Mono";
        src: url("/fonts/JetBrainsMono-Regular.woff2") format("woff2");
        font-display: swap;
      }}

      :root {{ color-scheme: dark; }}

      * {{ box-sizing: border-box; }}

      html, body {{ min-height: 100%; }}

      body {{
        margin: 0;
        display: grid;
        min-height: 100vh;
        place-items: center;
        overflow: hidden;
        background: #0a0e14;
      }}

      figure {{
        display: grid;
        width: 100vw;
        margin: 0;
        place-items: center;
      }}

      pre {{
        margin: 0;
        font-family: "JetBrains Mono", monospace;
        font-size: clamp(3px, 0.88vw, 13px);
        font-variant-ligatures: none;
        font-weight: 400;
        letter-spacing: 0;
        line-height: 0.88;
        text-shadow: 0 0 0.55em currentColor;
        user-select: text;
      }}

{palette}

      figcaption {{
        position: absolute;
        width: 1px;
        height: 1px;
        overflow: hidden;
        clip-path: inset(50%);
        white-space: nowrap;
      }}
    </style>
  </head>
  <body>
    <main>
      <figure>
        <pre role="img" aria-label="{html.escape(args.alt, quote=True)}">{art}</pre>
        <figcaption>{html.escape(args.alt)}</figcaption>
      </figure>
    </main>
  </body>
</html>
"""
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(document, encoding="utf-8")
    print(
        f"Wrote {args.output} ({args.columns} columns x {rows} rows, "
        f"{args.output.stat().st_size} bytes)"
    )


if __name__ == "__main__":
    main()
