# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Commands

```bash
npm install        # Install dependencies
npm run dev        # Dev server at http://localhost:4321
npm run build      # Static build to dist/
npm run preview    # Preview production build locally
```

Deploy: `./deploy.sh elmisi-com` (production via traefik.services). Local test: `docker compose up --build` (multi-stage Node 20 -> Nginx Alpine).

## Architecture

Astro static site (`output: 'static'`, zero JS frameworks). Personal portfolio with a terminal/CLI aesthetic.

### Data-driven pages

Three pages, each consuming JSON data files from `src/data/`:

- `index.astro` — About, skills (`skills.json`), AI workflow stats
- `projects.astro` — Live services + OSS repos (`projects.json`)
- `experience.astro` — Career timeline in `git log` format (`experience.json`)

**Content changes go in JSON data files, not in page templates.**

### Blog

Astro content collections (configured in `src/content.config.ts`). Articles are markdown files in `src/content/blog/` with frontmatter (title, date, description, tags).

- `src/pages/blog/index.astro` — Listing page styled as `ls -la articles/`
- `src/pages/blog/[slug].astro` — Article detail page with `cat` command and rendered markdown

To add a new article: create a `.md` file in `src/content/blog/` with the required frontmatter.

### Key patterns

- `src/layouts/BaseLayout.astro` wraps all pages (Head + Nav + slot + Footer)
- `src/components/Terminal.astro` is the reusable terminal window chrome (title bar + dots + body slot) — most visual sections are wrapped in this
- `src/scripts/typing.js` — sole client JS; typing animation via IntersectionObserver with `<noscript>` fallback

### Styling

Custom CSS only (no frameworks). Two global stylesheets in `src/styles/`:

- `global.css` — CSS variables, reset, base layout. Design tokens: `--accent-green`, `--accent-amber`, `--accent-cyan`, `--accent-red`, `--accent-purple`. Spacing: `--space-1` through `--space-8`. Mobile breakpoint at 640px.
- `terminal.css` — Terminal chrome classes (`.terminal`, `.prompt`, `.command`, `.output`, `.comment`, `.tag`, `.cursor`, `.ascii-art`)

## Conventions

- Self-hosted JetBrains Mono font (woff2 in `public/fonts/`)
- All navigation styled as terminal commands (`visitor@elmisi.com:~$`)
- Semver tracked in `VERSION` file; update VERSION + CHANGELOG.md on commits
- Site URL hardcoded as `https://elmisi.com` in `astro.config.mjs` and `Head.astro`
