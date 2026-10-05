# AGENTS Guide

This file guides agents modifying this static Astro website.

## Stack

- Astro static site generator with TypeScript.
- Markdown content collections defined in `src/content.config.ts`.
- Plain CSS design system in `src/styles/global.css`.
- GitHub Pages deployment through `.github/workflows/deploy.yml`.
- Docker Compose provides the local development environment.

## Local development

Run from repository root:

```bash
npm install
npm run dev
```

Or run the Docker preview:

```bash
docker compose up -d --build
docker compose logs -f site
```

The local site runs at `http://localhost:4000`.

Validate production output with:

```bash
npm run build
```

## Project structure

- `src/pages/`: public routes.
- `src/layouts/`: shared page shell.
- `src/components/`: reusable UI components.
- `src/styles/`: global tokens and responsive layout styles.
- `src/config/site.ts`: site metadata, feature flags, and navigation.
- `src/content/publications/`: publication Markdown records.
- `src/content/talks/`: talk Markdown records.
- `src/content/posts/`: blog post Markdown records.
- `src/content/pages/cv.md`: canonical Markdown CV source.
- `src/assets/`: optimized source images imported by Astro.
- `public/`: directly served files, including `/files/cv.pdf` and legacy image URLs.
- `scripts/`: build-time checks that are not part of the Astro pipeline.

## Content rules

### Home page

- The home page is the one a hiring reviewer reads first. Keep the order: hero (which carries the one-line research interests), selected work, technical skills, education, research experience, teaching, industry experience, academic service, grants.
- `site.availability` in `src/config/site.ts` drives the hero banner. Set `seeking: false` to remove it; nothing else needs to change.
- Technical skills intentionally appear only on the home page until an industry resume is introduced. Do not add them to the CV or duplicate the list elsewhere without an explicit request.
- Employment dates on the home page must match the CV entry for the same role.

### Publications

- Publication detail URLs live under `/publication/<slug>/` with lowercase, descriptive slugs. If a slug changes, add a redirect from the old path in `astro.config.mjs` so published links keep working.
- Keep abstracts in the Markdown body.
- Publication lists must remain compact and must not render abstracts.

### Talks

- Preserve public URLs under `/talks/<slug>/`.
- Include complete front matter: `title`, `slug`, `type`, `date`, `venue`, and `location`.

### Blog

- `site.blogEnabled` in `src/config/site.ts` controls whether blog routes and navigation are generated.
- Keep drafts as `draft: true`; they must not generate public pages.
- Copy `templates/post.md` into `src/content/posts/` when creating a post.

### CV

- The Markdown file is the web source of truth.
- Keep `/files/cv.pdf` as the downloadable official PDF.
- Preserve the profile panel in the CV layout.

### Images

- Use `src/assets/` imports for displayed images so Astro can generate responsive formats.
- Keep `public/images/` for stable legacy/static image paths.
- The photography gallery uses PhotoSwipe and should remain progressively enhanced.

### Discovery metadata

- Keep `public/robots.txt` permissive and point it to `/sitemap-index.xml`.
- Keep `public/llms.txt` concise, public, and aligned with the canonical site routes.
- `BaseLayout.astro` owns canonical URLs, manifest, Open Graph/Twitter metadata, and Person JSON-LD. Pass a useful `title` and `description` from pages rather than duplicating these tags.
- Preserve the sitemap integration in `astro.config.mjs` and the static manifest in `public/site.webmanifest`.

## Design rules

`DESIGN.md` explains the reasoning; this section is the operative summary.

- Use the Ubuntu and Ubuntu Mono font families loaded in `BaseLayout.astro`.
- Preserve the dark-first academic-workstation visual language.
- Keep interactions lightweight; avoid client-side frameworks unless a feature requires hydration.

### The palette has two layers

- The **machine layer** (`--rz-*` in `:root`) is a record of the terminal's colours, taken from `~/.config/nvim/lua/ricardo/colors.lua`. Never edit it to restyle anything. It changes only when the machine does.
- The **role layer** (`--canvas`, `--surface`, `--text`, `--accent`, `--ok`, ...) is what components paint with. Roles point at machine colours where they can.
- `:root[data-theme="light"]` re-points roles only. The light scheme is the same palette read from the other end, not an inversion and not a second set of colours. Do not replace it with a filter or `invert()`.
- Never hard-code a colour in a component. A colour that does not go through the token layer is a colour nothing can check.

### Load-bearing versus decorative

- `--line` and `--line-soft` are decoration: dividers, which WCAG 1.4.11 exempts.
- `--line-strong` is for a border that is the only thing marking a control's edge or state. Use it there, and do not lift `--line` to cover those cases.
- `--accent-deep` is decorative only, at 1.95:1 on the dark canvas. It may be a fill, a gradient stop, or a shadow tint. It must never be a foreground. Text placed on it uses `--on-accent`.

### Type scale

- Sizes come from `--text-2xs` through `--text-2xl`, each with a comment saying what it is for.
- No component hard-codes a `font-size`. The moment one does, the scale stops being a scale.

### Identity marks

- Section headings carry the prompt arrow `➜` in `--ok` before the title in `--accent`: the arrow is the prompt, the words are what you typed. It is the one place two colours run in a single line.
- Code blocks are plates, not bordered boxes: a filled `--surface`, no rule, and a title bar in `--accent-strong` like an active buffer tab.

### Contrast

- `scripts/check-contrast.py` walks every role pair in both schemes and exits non-zero below its bar: 4.5:1 for text, 3:1 for UI components and meaningful graphics.
- It runs in `.github/workflows/deploy.yml` before the build. Do not remove that step; the accessibility claim rests on it rather than on anyone remembering.
- Add a pair to `PAIRS` whenever a new role starts carrying meaning.
- Run it locally with `python3 scripts/check-contrast.py`.

## Deployment rules

- `master` is the deployment branch.
- GitHub Pages must be configured to use GitHub Actions as its source before merging the Astro implementation.
- The Pages workflow builds `dist/`; do not deploy source files or use a server adapter.
- Preserve route compatibility for `/`, `/publications/`, `/publication/*`, `/talks/`, `/cv/`, and `/about-me/`.

## Pre-deploy checklist

0. Run `python3 scripts/check-contrast.py` and see every pair clear its bar.
1. Run `npm run build` without errors.
2. Verify the key public routes locally return HTTP 200.
3. Verify disabled blog routes do not generate when `site.blogEnabled` is `false`.
4. Verify publication detail pages retain abstracts while listing pages do not.
5. Check desktop and mobile layouts, color toggle, PDF link, and gallery lightbox.
