import { getCollection } from "astro:content";

export async function getPublications() {
  const publications = await getCollection("publications");
  return publications.sort((a, b) => b.data.date.getTime() - a.data.date.getTime());
}

export async function getTalks() {
  const talks = await getCollection("talks");
  return talks.sort((a, b) => b.data.date.getTime() - a.data.date.getTime());
}

export async function getPublishedPosts() {
  const posts = await getCollection("posts", ({ data }) => !data.draft);
  return posts.sort((a, b) => b.data.date.getTime() - a.data.date.getTime());
}

export function formatDate(date: Date, options: Intl.DateTimeFormatOptions = {}) {
  return new Intl.DateTimeFormat("en", {
    month: "short",
    year: "numeric",
    timeZone: "UTC",
    ...options
  }).format(date);
}

export function formatLongDate(date: Date) {
  return new Intl.DateTimeFormat("en", {
    day: "numeric",
    month: "long",
    year: "numeric",
    timeZone: "UTC"
  }).format(date);
}

export function getDatePath(date: Date) {
  return {
    year: String(date.getUTCFullYear()),
    month: String(date.getUTCMonth() + 1).padStart(2, "0")
  };
}
