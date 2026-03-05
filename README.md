# elmisi.com

Personal portfolio site with a terminal aesthetic. Built with [Astro](https://astro.build), served with Nginx, deployed behind [Traefik](https://traefik.io).

```
       _           _     _
   ___| |_ __ ___ (_)___(_)
  / _ \ | '_ ` _ \| / __| |
 |  __/ | | | | | | \__ \ |
  \___|_|_| |_| |_|_|___/_|
```

## Live

**[elmisi.com](https://elmisi.com)**

## Stack

- **Framework:** [Astro](https://astro.build) (static output, zero JS by default)
- **Font:** JetBrains Mono (self-hosted)
- **Styling:** Custom CSS, no frameworks
- **Deploy:** Multi-stage Docker build (Node → Nginx Alpine) behind Traefik reverse proxy
- **AI stats:** Real usage data extracted from Claude Code history

## Design

Terminal-inspired UI: dark background, monospace font, green/amber accents, command-prompt navigation. Every section is presented as a terminal command and its output.

Pages:
- `/` — About, skills, AI workflow stats
- `/projects/` — Live services + open source
- `/experience/` — Career timeline in `git log` format

## Development

```bash
npm install
npm run dev        # http://localhost:4321
npm run build      # static output in dist/
```

## Deploy

```bash
docker compose up --build    # local test
./deploy.sh elmisi-com       # production (via traefik.services)
```

## License

MIT
