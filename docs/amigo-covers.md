# Amigo image generation for blog covers

Guidelines for generating the source bitmaps that feed the
[ASCII cover pipeline](ascii-images.md). Uses the Amigo HTTP API
(`https://amigo.elmisi.com/api/generate`).

## Auth

Token in `~/.secrets/amigo-token.txt` (not in git). Every call sends
`Authorization: Bearer <token>`.

## Resolution

All backends in this pipeline are native 1 MP. For 16:9 covers use the
`1344×768` bucket (the 16:9 entry in the 1024×1024 bucket table).
Never go above the native resolution: generate at native and upscale
later if needed.

## Backend selection

| Use case | Backend |
|---|---|
| Default, fast, editing-capable, best with long structured prompts | `sdcpp-flux2-klein-4b` |
| Quality, short dense prompts | `sdcpp-z-image-turbo` |
| Style fidelity, art-direction prompts | `sdcpp-krea2` |
| Typography (text in image) | `sdcpp-qwen-image` |

Server runs one generation at a time: a second concurrent call returns 409.

## Prompt discipline

The cover pipeline's output is an ASCII matrix, so the bitmap must be
simple: one strong metaphor, uniform dark background, broad tonal steps.
The model instructions below amplify that.

### FLUX.2 Klein (`sdcpp-flux2-klein-4b`)

Write clear, descriptive, compositional prompts in natural language.
Order: subject + action first, then environment, framing, light,
materials, style. Prioritize concrete visual details over keyword
lists. Avoid redundant prompts full of synonyms. If text must appear,
quote it exactly. For more control, describe subject positions,
perspective, and foreground/background relationship explicitly.

### Z-Image-Turbo (`sdcpp-z-image-turbo`)

Short, direct, high-information-density prompts. Put the most
important elements first: subject, scene, visual style, lighting,
camera. Avoid abstract instructions or long explanations: translate
intent into visible characteristics. Prefer few very specific
attributes over many generic qualifiers. It is speed-oriented:
reduce conflicts between instructions and do not overload the prompt
with micro-details.

### Krea 2 (`sdcpp-krea2`)

Write prompts focused on art direction, aesthetics, and final render.
Define clearly subject, composition, mood, palette, lighting,
texture/materials, and photographic or graphic language. Krea benefits
from coherent aesthetic references: build one strong visual direction
instead of mixing many styles. For photographic images, specify shot
type, lens/framing and light quality; for design and illustration,
describe layout, shapes, materials, and stylization level.

### Shared order

For all three: **subject → action/scene → composition → light →
style/materials → details → hard constraints**, dropping anything that
does not concretely change the image.

## Cover constraints (from `ascii-images.md`)

- 16:9, subject fills the frame with a small quiet margin.
- Perfectly uniform background: no gradient, haze, particles, floor glow, reflections, bloom, environmental shadows.
- No letters, digits, code, grids, typographic textures, titles, labels, logos, watermarks.
- One strong metaphor, crisp outer contours, broad tonal steps, explicit separation between surfaces.

### Do not impose the green palette on the model

The bitmap is generated in **neutral colors** (subject + composition +
uniform dark background + soft volumetric light). The phosphor-green
palette is applied **only by the converter**: `render_ascii_html.py`
maps luminance to its fixed 8-step green palette, so whatever hue the
model used becomes green after conversion. Asking the model for
"phosphor green / forest green / mint-white" makes it fight the
instruction and produce off-tone, low-contrast subjects. Keep color
language out of the prompt; keep subject, framing, background and
light.

If the subject needs a nudge (too small, too dark, too much glow at
the borders), adjust the PNG locally (contrast, luminance, crop) and
re-run the converter — do not regenerate the whole image.

## Converting

```bash
python3 scripts/render_ascii_html.py \
  assets/ascii-sources/<slug>.png \
  public/<slug>-ascii.html \
  --title "<Article title> — ASCII cover" \
  --alt "<one-line description>" \
  --columns 180 \
  --height-scale 0.88
```

### Choosing `--height-scale`

The converter samples a matrix of `--columns` × `rows` where
`rows = round(width / height * columns * height_scale)`. A monospace
glyph is roughly 1:0.62 (height:width), so:

| Subject shape | `--height-scale` | Resulting matrix |
|---|---|---|
| **Square / round** (gears, eyes, spheres, cubes) | `0.88` | 180×91 — preserves the subject's roundness |
| **Tall** (obelisks, columns, towers) | `0.62` | 180×64 — matches the subject's vertical proportion |
| **Wide / landscape** (horizons, wide scenes) | `0.55–0.62` | 180×58–64 |

A wrong scale **squashes** the subject in the ASCII matrix (e.g. a
round gear at `0.62` becomes a flat disc). Match the scale to the
subject's bounding-box ratio.

### Subject must fill the frame

After conversion the subject should occupy most of the matrix.
Heuristic: the subject's bounding box in the source PNG should be at
least **~50% of the width and ~67% of the height**; coverage
(luminance ≥ 40) of ~20% or more. If the subject is small with large
margins, the ASCII matrix has many empty rows — regenerate with a
prompt that says "fills the frame / edge to edge" rather than
"centered with a quiet margin".

## Workflow

One article at a time. For each article:

1. Pick **one strong metaphor** for the article (see the article's
   thesis, not its title).
2. Draft **one prompt per candidate backend** (usually just
   `sdcpp-flux2-klein-4b` unless the article needs a specific style),
   following that backend's discipline above. **No color words** in
   the prompt.
3. Generate at least **2–3 seeds** so you can pick the best subject
   framing (the model's composition varies with the seed).
4. Convert every candidate to ASCII with `render_ascii_html.py` using
   the right `--height-scale` for the subject shape.
5. Compare the **ASCII results**, not the bitmaps — the ASCII matrix
   is what the reader sees.
6. Keep the winner as `assets/ascii-sources/<slug>.png`, regenerate
   `public/<slug>-ascii.html`, add the `asciiImage` frontmatter,
   `npm run build`, verify the cover is inlined in
   `dist/blog/<slug>/index.html`.

## Generating a cover

```bash
TOKEN=$(cat ~/.secrets/amigo-token.txt)
curl -s -X POST https://amigo.elmisi.com/api/generate \
  -H "Authorization: Bearer $TOKEN" \
  -H 'Content-Type: application/json' \
  -d @payload.json
```

`payload.json` shape (single-shot; `/api/generate/stream` returns NDJSON instead):

```json
{
  "backend": "sdcpp-z-image-turbo",
  "prompt": "...",
  "width": 1344,
  "height": 768,
  "seed": 1337
}
```

`negative_prompt` is supported by `z-image-turbo` and `krea2`, ignored
by `sdcpp-flux2-klein-4b` — bake the exclusions into the prompt for
Flux.



