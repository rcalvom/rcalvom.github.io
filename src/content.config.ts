import { defineCollection } from "astro:content";
import { glob } from "astro/loaders";
import { z } from "astro/zod";

const publications = defineCollection({
  loader: glob({ pattern: "**/*.md", base: "./src/content/publications" }),
  schema: z.object({
    title: z.string(),
    slug: z.string(),
    category: z.string().default("refereed-conference-publications"),
    date: z.coerce.date(),
    venue: z.string(),
    citation: z.string(),
    paperUrl: z.string().optional(),
    slidesUrl: z.string().optional(),
    bibtexUrl: z.string().optional()
  })
});

const talks = defineCollection({
  loader: glob({ pattern: "**/*.md", base: "./src/content/talks" }),
  schema: z.object({
    title: z.string(),
    slug: z.string(),
    type: z.string(),
    date: z.coerce.date(),
    venue: z.string(),
    location: z.string(),
    paperSlug: z.string().optional()
  })
});

const posts = defineCollection({
  loader: glob({ pattern: "**/*.md", base: "./src/content/posts" }),
  schema: z.object({
    title: z.string(),
    slug: z.string(),
    date: z.coerce.date(),
    description: z.string().optional(),
    tags: z.array(z.string()).default([]),
    draft: z.boolean().default(false)
  })
});

const pages = defineCollection({
  loader: glob({ pattern: "**/*.md", base: "./src/content/pages" }),
  schema: z.object({
    title: z.string()
  })
});

export const collections = { publications, talks, posts, pages };
