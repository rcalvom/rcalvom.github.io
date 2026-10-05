export type PublicationMetadata = {
  authors: string[];
  date: Date;
  doi?: string;
  pages?: string;
  slug: string;
  status: "published" | "preprint" | "forthcoming";
  title: string;
  venue: string;
};

function joinAuthors(authors: string[]) {
  if (authors.length === 1) return authors[0];
  if (authors.length === 2) return `${authors[0]} and ${authors[1]}`;
  return `${authors.slice(0, -1).join(", ")}, and ${authors.at(-1)}`;
}

export function formatAcmCitation(publication: PublicationMetadata) {
  const year = publication.date.getUTCFullYear();
  const venue = publication.status === "forthcoming"
    ? `Accepted at ${publication.venue}`
    : publication.status === "preprint"
      ? publication.venue
      : `In ${publication.venue}`;
  const pages = publication.pages
    ? publication.pages.includes("-")
      ? ` Pages ${publication.pages}.`
      : ` ${publication.pages} pages.`
    : "";
  const doi = publication.doi ? ` https://doi.org/${publication.doi}.` : "";

  return `${joinAuthors(publication.authors)}. ${year}. ${publication.title}. ${venue}.${pages}${doi}`;
}

export function formatBibtex(publication: PublicationMetadata) {
  const type = publication.status === "preprint" ? "article" : "inproceedings";
  const year = publication.date.getUTCFullYear();
  const fields = [
    ["title", publication.title],
    ["author", publication.authors.join(" and ")],
    ["year", String(year)],
    [type === "article" ? "journal" : "booktitle", publication.venue],
    publication.pages && ["pages", publication.pages],
    publication.doi && ["doi", publication.doi],
    publication.doi && ["url", `https://doi.org/${publication.doi}`],
    publication.status === "forthcoming" && ["note", "Accepted for publication"]
  ].filter(Boolean) as [string, string][];

  return `@${type}{${publication.slug},\n${fields.map(([key, value]) => `  ${key} = {${value}}`).join(",\n")}\n}\n`;
}

export function markdownToText(markdown: string) {
  return markdown.replace(/[`*_]/g, "").replace(/\s+/g, " ").trim();
}
