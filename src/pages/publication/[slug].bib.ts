import { getCollection } from "astro:content";
import { formatBibtex } from "../../lib/publications";

export async function getStaticPaths() {
  const publications = await getCollection("publications");
  return publications.map((publication) => ({
    params: { slug: publication.data.slug },
    props: { publication }
  }));
}

export async function GET({ props }: { props: Awaited<ReturnType<typeof getStaticPaths>>[number]["props"] }) {
  return new Response(formatBibtex(props.publication.data), {
    headers: {
      "Content-Type": "application/x-bibtex; charset=utf-8",
      "Content-Disposition": `attachment; filename="${props.publication.data.slug}.bib"`
    }
  });
}
