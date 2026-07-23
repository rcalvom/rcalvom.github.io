import { defineConfig } from "astro/config";
import sitemap from "@astrojs/sitemap";

export default defineConfig({
  site: "https://rcalvom.github.io",
  output: "static",
  trailingSlash: "always",
  integrations: [sitemap()],
  redirects: {
    "/about/": "/",
    "/about.html": "/",
    "/resume": "/cv/",
    "/resume-json": "/cv/"
  }
});
