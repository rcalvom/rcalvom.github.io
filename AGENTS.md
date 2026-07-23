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

## Content rules

### Publications

- Preserve the existing public detail URLs under `/publication/<slug>/`.
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

## Design rules

- Use the Ubuntu and Ubuntu Mono font families loaded in `BaseLayout.astro`.
- Preserve the dark-first academic-workstation visual language.
- Use the color tokens in `src/styles/global.css`; do not introduce isolated hard-coded colors in components.
- Keep interactions lightweight; avoid client-side frameworks unless a feature requires hydration.

## Deployment rules

- `master` is the deployment branch.
- GitHub Pages must be configured to use GitHub Actions as its source before merging the Astro implementation.
- The Pages workflow builds `dist/`; do not deploy source files or use a server adapter.
- Preserve route compatibility for `/`, `/publications/`, `/publication/*`, `/talks/`, `/cv/`, and `/about-me/`.

## Pre-deploy checklist

1. Run `npm run build` without errors.
2. Verify the key public routes locally return HTTP 200.
3. Verify disabled blog routes do not generate when `site.blogEnabled` is `false`.
4. Verify publication detail pages retain abstracts while listing pages do not.
5. Check desktop and mobile layouts, color toggle, PDF link, and gallery lightbox.
