#!/usr/bin/env python3
"""Fail the build when a colour pair in the role layer falls below its bar.

Ported from ``scripts/check-contrast.py`` in ``personal-slides-template``. The
algorithm is unchanged -- plain arithmetic over hex strings, WCAG 2.1 relative
luminance -- and only the input parser is new: it reads CSS custom properties
out of ``src/styles/global.css`` instead of LaTeX ``\\definecolor`` lines.

The check exists because contrast is not something anyone verifies by eye. In
the slides repository it caught two real regressions, neither of them visible by
looking: a second copy of the palette that had drifted a release behind, and
code set in a dark syntax theme on a light page. Both slipped through because
the colours never passed through the token layer. The lesson generalises: a
colour that does not go through your tokens is a colour nothing can check.

Bars, from WCAG 2.1:
  4.5:1  normal text (1.4.3 AA)
  3.0:1  large text, and user-interface components and graphical objects that
         convey information (1.4.11)

Dividers and other purely decorative lines are exempt from 1.4.11 and are not
listed below. ``--accent-deep`` is likewise exempt as a foreground: it is a
fill, a gradient stop or a shadow tint, never something a reader must perceive.
What is checked is the text placed on top of it.

Usage:
    python3 scripts/check-contrast.py [path/to/global.css]
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
DEFAULT_CSS = REPO_ROOT / "src" / "styles" / "global.css"

TEXT = 4.5
UI = 3.0

# (foreground, background, minimum ratio, what it is)
PAIRS: list[tuple[str, str, float, str]] = [
    ("text", "canvas", TEXT, "body copy on the page"),
    ("text", "surface", TEXT, "body copy on a card"),
    ("text", "surface-raised", TEXT, "body copy in the mobile nav panel"),
    ("text", "surface-hover", TEXT, "body copy on a hovered surface"),
    ("text-strong", "canvas", TEXT, "emphasised copy on the page"),
    ("text-strong", "surface", TEXT, "emphasised copy on a card"),
    ("muted", "canvas", TEXT, "secondary copy on the page"),
    ("muted", "surface", TEXT, "secondary copy on a card"),
    ("accent", "canvas", TEXT, "headings and links on the page"),
    ("accent", "surface", TEXT, "headings and links on a card"),
    ("accent", "surface-raised", TEXT, "links in the mobile nav panel"),
    ("ok", "canvas", TEXT, "the prompt arrow before a heading"),
    ("ok", "surface", TEXT, "the prompt arrow on a card"),
    ("warn", "canvas", TEXT, "warning role on the page"),
    ("error", "canvas", TEXT, "error role on the page"),
    ("on-accent", "accent-deep", TEXT, "button label on its fill"),
    ("canvas", "accent", TEXT, "button label on hover, which inverts"),
    ("accent-strong", "canvas", UI, "the button border, which marks its edge"),
    ("accent-strong", "surface", UI, "the code plate title bar"),
    ("line-strong", "canvas", UI, "borders that are the only marker of a control"),
    ("line-strong", "surface", UI, "borders that are the only marker of a control"),
]

SCHEMES = {
    "dark": r":root\s*\{(.*?)\n\}",
    "light": r':root\[data-theme="light"\]\s*\{(.*?)\n\}',
}

COMMENT = re.compile(r"/\*.*?\*/", re.DOTALL)
DECLARATION = re.compile(r"--([a-z0-9-]+)\s*:\s*([^;]+);")
VAR_REFERENCE = re.compile(r"var\(\s*--([a-z0-9-]+)\s*\)")
HEX = re.compile(r"^#(?:[0-9a-fA-F]{3}|[0-9a-fA-F]{6})$")


def read_block(css: str, pattern: str) -> dict[str, str]:
    match = re.search(pattern, css, re.DOTALL)
    if not match:
        raise SystemExit(f"check-contrast: no block matching {pattern!r}")
    return {name: value.strip() for name, value in DECLARATION.findall(match.group(1))}


def resolve(name: str, scope: dict[str, str], seen: frozenset[str] = frozenset()) -> str | None:
    """Resolve a token to a hex string, following var() references."""
    if name in seen:
        raise SystemExit(f"check-contrast: --{name} references itself")
    value = scope.get(name)
    if value is None:
        return None
    reference = VAR_REFERENCE.fullmatch(value)
    if reference:
        return resolve(reference.group(1), scope, seen | {name})
    return value if HEX.match(value) else None


def channel(component: int) -> float:
    ratio = component / 255
    return ratio / 12.92 if ratio <= 0.04045 else ((ratio + 0.055) / 1.055) ** 2.4


def luminance(hex_colour: str) -> float:
    digits = hex_colour.lstrip("#")
    if len(digits) == 3:
        digits = "".join(digit * 2 for digit in digits)
    red, green, blue = (int(digits[index : index + 2], 16) for index in (0, 2, 4))
    return 0.2126 * channel(red) + 0.7152 * channel(green) + 0.0722 * channel(blue)


def contrast(foreground: str, background: str) -> float:
    lighter, darker = sorted((luminance(foreground), luminance(background)), reverse=True)
    return (lighter + 0.05) / (darker + 0.05)


def main(argv: list[str]) -> int:
    css_path = Path(argv[1]) if len(argv) > 1 else DEFAULT_CSS
    # Strip comments first. A comment that happens to contain "--name: value"
    # would otherwise be read as a declaration and swallow the real one that
    # follows it, which is precisely the kind of silent drift this check exists
    # to catch -- and it did, on its first run against this file.
    css = COMMENT.sub("", css_path.read_text(encoding="utf-8"))

    machine_and_dark = read_block(css, SCHEMES["dark"])
    # The light scheme re-points roles only; the machine layer is inherited.
    light = {**machine_and_dark, **read_block(css, SCHEMES["light"])}
    scopes = {"dark": machine_and_dark, "light": light}

    failures: list[str] = []
    checked = 0

    for scheme, scope in scopes.items():
        print(f"\n{scheme} scheme")
        for foreground, background, bar, description in PAIRS:
            fg_hex = resolve(foreground, scope)
            bg_hex = resolve(background, scope)
            if fg_hex is None or bg_hex is None:
                failures.append(f"{scheme}: --{foreground} on --{background} does not resolve to a hex value")
                continue
            ratio = contrast(fg_hex, bg_hex)
            checked += 1
            ok = ratio >= bar
            mark = "  ok  " if ok else " FAIL "
            print(f"  [{mark}] {ratio:5.2f} >= {bar:.1f}  --{foreground} on --{background}  ({description})")
            if not ok:
                failures.append(
                    f"{scheme}: --{foreground} ({fg_hex}) on --{background} ({bg_hex}) "
                    f"is {ratio:.2f}:1, below {bar:.1f}:1 -- {description}"
                )

    print(f"\n{checked} pairs checked across {len(scopes)} schemes.")
    if failures:
        print("\nContrast check failed:", file=sys.stderr)
        for failure in failures:
            print(f"  - {failure}", file=sys.stderr)
        return 1

    print("All pairs clear their bar.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
