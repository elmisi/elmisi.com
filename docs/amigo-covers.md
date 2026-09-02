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

- 16:9, canvas `#0a0e14`, subject in forest/phosphor green with restrained mint-white highlights.
- Perfectly uniform background: no gradient, haze, particles, floor glow, reflections, bloom, environmental shadows.
- No letters, digits, code, grids, typographic textures, titles, labels, logos, watermarks.
- One strong metaphor, crisp outer contours, broad tonal steps, explicit separation between surfaces.
- Subject fills the frame with a small quiet margin.

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

Save the chosen source under `assets/ascii-sources/<slug>.png`, then
convert with `scripts/render_ascii_html.py` and add the `asciiImage`
frontmatter (see `ascii-images.md`).

## Workflow

One article at a time. For each article:

1. Draft one prompt per candidate backend, following that backend's
   discipline above.
2. Generate all candidates (same seed where comparable).
3. Convert every candidate to ASCII with `render_ascii_html.py`.
4. Compare the **ASCII results**, not the bitmaps — the ASCII matrix
   is what the reader sees.
5. Keep the winner as `assets/ascii-sources/<slug>.png`.