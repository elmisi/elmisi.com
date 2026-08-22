# ASCII Image Guidelines

Blog covers use a two-stage process: create a conventional high-resolution bitmap, then convert it into a static HTML matrix. The published site contains real ASCII characters and never loads the source bitmap.

## Visual Direction

- Start from a polished, conceptual 16:9 bitmap with clear volume, lighting, and depth.
- Never generate the source from letters, digits, code, grids, or typographic textures. Characters belong only to the conversion stage.
- Prefer one strong metaphor over a literal diagram. Avoid titles, labels, logos, watermarks, circuit patterns, and falling-code clichés.
- Use `#0a0e14` for the cover canvas so it merges with the article terminal (`#0d1117` remains the outer page background). Keep subjects in forest green, phosphor green, and restrained mint-white highlights.
- Fill the frame while preserving a small quiet margin. Covers must merge into the site's black background without a border or visible rectangle.

## Output Specification

- Matrix: **180 columns × 63 rows** (`20:7` character ratio).
- Rendered visual ratio: approximately **1.95:1**, accounting for monospace glyph proportions.
- Font: self-hosted JetBrains Mono; ligatures disabled.
- Format: standalone HTML containing a `<pre>` and palette spans—no `<img>`, canvas, Base64 data, JavaScript, or bitmap reference.
- Palette: `#0a0e14`, `#0b2814`, `#105021`, `#18752e`, `#229b3c`, `#39d353`, `#78e889`, `#d7ffdc`.

## Generation Procedure

1. Generate the source bitmap at high resolution. Ask for a normal 3D or editorial illustration and explicitly exclude characters, typography, code, and text-like textures.
2. Save the selected source under `assets/ascii-sources/<slug>.png`. This directory is excluded from the Docker build and is never deployed.
3. Install the converter dependency if needed: `python3 -m pip install Pillow`.
4. Generate the HTML:

   ```bash
   python3 scripts/render_ascii_html.py \
     assets/ascii-sources/context-squared.png \
     public/context-squared-ascii.html \
     --title "Context Squared — ASCII study" \
     --alt "A luminous green infinity loop reconstructed entirely from ASCII characters" \
     --columns 180 \
     --height-scale 0.62
   ```

5. Add the cover to the article frontmatter:

   ```yaml
   asciiImage:
     src: "/context-squared-ascii.html"
     alt: "A concise description of the subject."
   ```

6. Run `npm run build`. Confirm the generated HTML contains no bitmap references with `rg '<img|<canvas|data:image|\.png|\.jpe?g' public/<slug>-ascii.html`.

The converter crops quiet margins, samples luminance, increases contrast, maps brightness to ASCII glyphs, groups adjacent colors into spans, and emits an accessible standalone document. During the Astro build, the article renderer extracts that document's `<pre>` and embeds the characters directly; this avoids frames and extra requests. Blog-list pages intentionally do not render covers.
