#!/usr/bin/env python3
"""Check local content relationships that Astro's schema cannot express."""

from __future__ import annotations

import argparse
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
PUBLICATIONS = ROOT / "src" / "content" / "publications"
TALKS = ROOT / "src" / "content" / "talks"


def front_matter(path: Path) -> str:
    match = re.match(r"---\n(.*?)\n---", path.read_text(encoding="utf-8"), re.DOTALL)
    if match is None:
        raise AssertionError(f"{path.relative_to(ROOT)} has no front matter")
    return match.group(1)


def value(front_matter_text: str, name: str) -> str | None:
    match = re.search(rf'^{name}:\s*["\']?([^"\'\n]+)', front_matter_text, re.MULTILINE)
    return match.group(1).strip() if match else None


def check_source() -> None:
    canonical_pdf = ROOT / "public" / "files" / "cv.pdf"
    legacy_pdf = ROOT / "public" / "cv.pdf"
    assert canonical_pdf.is_file(), "missing canonical CV PDF"
    assert legacy_pdf.is_file(), "missing legacy CV PDF alias"
    assert canonical_pdf.read_bytes() == legacy_pdf.read_bytes(), "legacy CV PDF alias is out of sync"

    site_config = (ROOT / "src" / "config" / "site.ts").read_text(encoding="utf-8")
    assert 'cv: "/files/cv.pdf"' in site_config, "site.cv must use the canonical PDF"
    assert "blogEnabled: false" in site_config, "blog must remain disabled"

    publication_slugs: set[str] = set()
    for path in PUBLICATIONS.glob("*.md"):
        metadata = front_matter(path)
        slug = value(metadata, "slug")
        assert slug is not None, f"{path.name} is missing a slug"
        assert slug not in publication_slugs, f"duplicate publication slug: {slug}"
        assert "authors:" in metadata, f"{path.name} is missing authors"
        publication_slugs.add(slug)

    for path in TALKS.glob("*.md"):
        paper_slug = value(front_matter(path), "paperSlug")
        if paper_slug is not None:
            assert paper_slug in publication_slugs, f"{path.name} references unknown publication {paper_slug}"


def check_dist(dist: Path) -> None:
    assert (dist / "publication" / "autosoup" / "index.html").is_file(), "AutoSOUP page was not generated"
    assert not (dist / "year-archive").exists(), "disabled blog archive was generated"
    assert not (dist / "posts").exists(), "disabled blog posts were generated"
    autosoup = (dist / "publication" / "autosoup" / "index.html").read_text(encoding="utf-8")
    assert 'name="citation_title"' in autosoup, "publication citation metadata is missing"
    assert "ScholarlyArticle" in autosoup, "publication JSON-LD is missing"


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--dist", type=Path)
    args = parser.parse_args()

    check_source()
    if args.dist is not None:
        check_dist(args.dist)
    print("Content consistency checks passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
