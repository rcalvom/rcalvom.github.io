# AGENTS Guide

This file is the working guide for AI/code agents that modify this repository.

## Project overview

- Stack: Jekyll site based on Academic Pages.
- Main purpose: personal academic website.
- Local preview is expected to run with Docker Compose.

## Run and verify locally

Use these commands from repository root:

```bash
docker compose up -d
docker compose logs -f jekyll-site
```

Default local URL:

- `http://localhost:4000`

## Current public navigation

Keep this order unless the user asks to change it:

1. Publications
2. Talks
3. CV
4. About me

Notes:

- Blog is intentionally hidden for now.
- Hidden menu entries should stay commented in `_data/navigation.yml` until explicitly requested.

## Content conventions in this repo

### Publications

- Publications page is `_pages/publications.html`.
- Publication cards use `_includes/archive-single.html`.
- Abstracts are intentionally hidden in publication listings by passing `hide_excerpt=true`.
- Abstracts must still appear in each publication detail page.

### Talks

- Active talks live in `_talks/`.
- Talk entries should include complete front matter metadata (`title`, `collection`, `type`, `permalink`, `venue`, `date`, `location`).
- Old template talks were removed and should not be reintroduced.

### CV

- Public CV page is `_pages/cv.md`.
- Sidebar profile photo should remain visible (`author_profile: true`).
- CV PDF source used by the site is `files/cv.pdf`.

### About pages

- Home/profile page is `_pages/about.md`.
- Secondary about page is `_pages/about-me.md`.

### Blog

- Blog archive page `_pages/year-archive.html` is intentionally hidden (`published: false`).
- Draft posts should remain unpublished unless explicitly requested otherwise.

## Pages intentionally hidden

These pages are intentionally not public right now:

- `_pages/markdown.md`
- `_pages/talkmap.html`
- `_pages/collection-archive.html`
- `_pages/category-archive.html`
- `_pages/year-archive.html`

## Pre-deploy checklist

Before considering changes ready for deploy:

1. Ensure Jekyll rebuilds without Liquid errors in docker logs.
2. Verify key routes return HTTP 200:
   - `/`
   - `/publications/`
   - `/talks/`
   - `/cv/`
   - `/about-me/`
3. Verify intentionally hidden routes return 404 (unless user requested otherwise):
   - `/year-archive/`
   - `/talkmap.html`
   - `/markdown/`
4. Ensure no template/sample posts or talks are accidentally restored.

## Editing guidelines

- Keep content edits concise and consistent with existing tone.
- Prefer minimal, targeted changes over broad refactors.
- Do not change deployment model (GitHub Pages + Jekyll) unless user asks.
- Do not introduce secrets, credentials, or environment-specific absolute paths.
