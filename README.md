# Academic Website

Static academic website built with Astro.

## Use as a template

Select **Use this template** on GitHub to create your own repository, then update:

- `src/config/site.ts` with your name, contact details, and navigation.
- `src/content/` with your publications, talks, posts, and CV.
- `src/assets/profile/ricardo.jpg` and `src/assets/photos/` with your images.
- `public/files/cv.pdf` with your downloadable CV.

In the new repository, configure GitHub Pages to use **GitHub Actions** as its source. Pushes to `master` build and deploy the static site.

## Development

```bash
npm install
npm run dev
```

The development server runs at `http://localhost:4000`.

To use Docker:

```bash
docker compose up -d --build
```

## Build

```bash
npm run build
```

The generated static site is written to `dist/`.

## Content

- Publications: `src/content/publications/`
- Talks: `src/content/talks/`
- Blog posts: `src/content/posts/`
- New-post template: `templates/post.md`
- Markdown CV: `src/content/pages/cv.md`
- Downloadable PDF CV: `public/files/cv.pdf`

Blog publication is controlled through `site.blogEnabled` in `src/config/site.ts`.
