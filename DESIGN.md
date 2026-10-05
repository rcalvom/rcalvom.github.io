# Design notes, carried over from the slides template

These are the design decisions from
[`personal-slides-template`](https://github.com/rcalvom/personal-slides-template),
written down for whoever works on this site next.

They are here because the two things share an origin and should share a look: both take their colours from `~/.config/nvim/lua/ricardo/colors.lua`, the same file Alacritty and Hyprland read.
The site already knows this — `--accent-strong: #008ec4` is exactly `rzc@blue` from that palette.

What follows is the part that transfers.
There is a section at the end for the part that does not, which is most of the LaTeX-specific work and is listed so nobody tries to port it.

Written one sentence per line, which is the convention in the slides repository and the reason a diff there names the sentence that changed rather than the paragraph that reflowed around it.

---

## 1. The rule that matters most: two layers, never one

A palette has a machine layer and a role layer, and they are not the same thing.

The **machine layer** is what the terminal actually shows: eighteen colours taken 1:1 from `colors.lua`, plus white and Hyprland's `$muted`, which are the two that are not on the machine.
It is a record, it is named after the machine (`--rz-blue`, `--rz-bright-green`), and it is **never edited to restyle anything**.
If a colour in it is wrong, it is wrong because the terminal changed.

The **role layer** is what everything else paints with: canvas, surface, text, accent, muted, line.
Roles point at machine colours.
Switching to the light scheme re-points the roles and touches nothing in the machine layer.

This site currently has the role layer and not the machine layer.
`:root` and `:root[data-theme="light"]` each hard-code hex values, which works and is not broken — but it means the same blue is written out in two places and nothing records that it *is* the terminal's blue.
Adding the machine layer underneath is a small change with a real payoff:

```css
:root {
  /* machine layer -- colors.lua. Never edited to restyle. */
  --rz-black: #000000;
  --rz-cursorline: #212121;
  --rz-selection: #2c2c2c;
  --rz-muted: #4c566a;        /* hypr $muted -- not from colors.lua */
  --rz-dim-fg: #818181;
  --rz-fg: #d6d6d6;
  --rz-bright-fg: #f1f1f1;
  --rz-white: #ffffff;        /* the one colour not on the machine */
  --rz-accent: #20bbfc;
  --rz-blue: #008ec4;
  --rz-dark-blue: #005f87;
  --rz-cyan: #20a5ba;
  --rz-green: #10a778;
  --rz-bright-green: #5fd7af;
  --rz-yellow: #a89c14;
  --rz-bright-yellow: #f3e430;
  --rz-red: #c30771;
  --rz-bright-red: #fb007a;
  --rz-magenta: #6855de;
  --rz-dark-magenta: #523c79;

  /* role layer -- this is what components use */
  --accent: var(--rz-accent);
  --text: var(--rz-fg);
}
```

The payoff is that a question like "is this blue the terminal's blue or something someone picked" stops being unanswerable.

## 2. The light scheme is not an inversion

This is the part most sites get wrong, and it is worth stating because it looks like extra work until you see the numbers.

A terminal palette comes in normal/bright pairs **because the two ends are built for opposite backgrounds**.
`#20bbfc` measures 9.6:1 on black and 2.2:1 on white.
`#005f87` is the reverse: 3.0:1 on black, 7.0:1 on white.

So the light scheme is not the dark one inverted, and it is not a second set of colours either.
It is the same palette read from the other end.
Only white is genuinely new, and only yellow and cyan needed adjusting, because neither end of those two clears 3:1 on white.

The site already does this correctly, in structure if not in exact values — `--accent` goes from `#24b8f6` on dark to `#075f98` on light, which is the same normal/bright move with the site's own near-neighbours of `#20bbfc` and `#005f87`.
Whether to snap those two to the palette's values is a judgement call and not a correction; both pass.
What matters is knowing *why* the swap works, so nobody "simplifies" it later into a filter or an inversion.

## 3. The roles, resolved, with measured contrast

Every value below is measured against its own scheme's canvas.
These are the slides' roles; they are here as a reference for meaning and for verified values, not as an instruction to replace what the site has.

**Dark** (canvas `#000000`)

| Role | Hex | On canvas |
|---|---|---|
| surface | `#212121` | 1.30 |
| surface alt | `#2c2c2c` | 1.50 |
| text | `#d6d6d6` | 14.45 |
| text strong | `#f1f1f1` | 18.59 |
| muted | `#898989` | 6.00 |
| accent | `#20bbfc` | 9.58 |
| ok | `#5fd7af` | 11.83 |
| warn | `#f3e430` | 15.95 |
| error | `#fc4aa1` | 6.63 |

**Light** (canvas `#ffffff`)

| Role | Hex | On canvas |
|---|---|---|
| surface | `#f1f1f1` | 1.13 |
| surface alt | `#d6d6d6` | 1.45 |
| text | `#212121` | 16.10 |
| text strong | `#000000` | 21.00 |
| muted | `#6e6e6e` | 5.10 |
| accent | `#005f87` | 7.03 |
| ok | `#0b6e4f` | 6.25 |
| warn | `#6a620d` | 6.24 |
| error | `#b50769` | 6.56 |

Eight of these moved during an accessibility pass, each by the smallest distance that clears 4.5:1, in the same hue.
A terminal palette is tuned for a screen an arm's length away, not for a projector at the back of a hall or a phone in daylight, and it shows.
The machine layer was left untouched throughout — the adjustments live in the role layer, which is the whole point of having two.

## 4. What I measured on this site, today

Run against `src/styles/global.css` as it stands.
This is the useful part of the document, so it is stated plainly.

**Text passes everywhere, in both schemes.**
Nothing in `--text`, `--text-strong`, `--muted`, `--accent` or `--accent-strong` falls below 4.5:1 on `--canvas` or `--surface`.
The worst is `--muted` on light canvas at 4.70, which clears AA with little room but clears it.

**Two things are worth a decision.**

`--accent-deep` (`#033e8c`) is **1.95:1 on dark canvas** and 1.82 on dark surface.
That is unusable for anything a reader has to perceive.
If it is only ever a gradient stop, a shadow tint or a decorative fill, it is fine and WCAG does not apply.
If it ever carries meaning on a dark background — a link, a state, an icon that means something — it fails, and nothing in the build will say so.

`--line` (1.58) and `--line-soft` (1.32) on canvas are below 3:1 in both schemes.
This is genuinely "it depends", and the distinction is worth getting right rather than assuming either way.
WCAG 1.4.11 asks 3:1 of *user-interface components and graphical objects that convey information*.
A divider between two sections is decoration and is exempt.
A border that is the only thing marking the edge of a text input, or the only thing showing which card is selected or focused, is a UI component and is not.
So: audit where `--line` is load-bearing, and give those uses a stronger token rather than lifting the divider colour and losing the quiet look.

## 5. Typography: what carries over and what does not

The typefaces carry over exactly, and the site already uses them: Ubuntu Mono for code and chrome, Ubuntu for prose.
In the slides everything is monospace, including headings — that is the identity, and it is worth keeping wherever the site wants to feel like the terminal.

**The type scale does not carry over, and should not be copied.**
Its sizes come from an argument about projection: presentation guidance asks for body text at a 24pt equivalent on a 13.33in slide, and the slide here is 160mm, so a point is worth 2.117 points there and the floor works out at 11.34pt.
None of that means anything on a web page.

What does carry over is the *shape* of the decision: a small set of named sizes, each with a written reason, and no component inventing its own.
On the web that is `--text-sm` / `--text-base` / `--text-lg` as custom properties in `rem`, with a comment saying what each is for.
The rule to keep is the one in the slides: **no component hard-codes a size**, because the moment one does, the scale stops being a scale.

## 6. The identity marks

These are what make it look like *the terminal* rather than merely dark.
Reuse the ones that fit a web page; ignore the rest.

- **The prompt arrow `➜` in green, before a title in accent blue.**
  Every frame title in the deck is a green arrow followed by blue words.
  It is the one place two colours run in a single line, and it is deliberate: the arrow is the prompt, the words are what you typed.
  `#5fd7af` on dark, `#0b6e4f` on light.
- **A lualine-style status bar**: coloured segments separated by powerline arrows, first segment `dark_blue` with `bright_fg`, second `selection` with `fg`.
  Taken from the real `~/.config/nvim/lua/ricardo/plugins.lua`, not invented.
- **Chrome fills stay dark in both schemes.**
  A dark status bar under a light page reads as deliberate and keeps the identity.
  This is a rule the slides follow and it is worth following here.
- **Code plates**, not code blocks with borders: a filled surface in `--surface`, no rule, a title bar in dark blue like an active buffer tab.

## 7. The method, which is the most portable thing here

The colours are worth copying.
The habit is worth more.

**Contrast is checked by a script, not by eye, and the build fails on it.**
`scripts/check-contrast.py` in the slides repository reads the palette, walks 42 colour pairs across both schemes, and exits non-zero if any falls below its bar — 4.5:1 for text, 3:1 for large text and for marks that carry meaning without words.
It is plain Python over hex strings and it works here unchanged; only the input parser needs to read CSS custom properties instead of `\definecolor`.

That check has caught real things twice, and neither was visible by looking:

- A second copy of the palette in the diagram stylesheet drifted a whole release behind, leaving diagrams drawn in colours the deck had stopped using, two of them below AA.
- Code was set in a syntax theme built for a dark background while the page was light — grey on near-white, unreadable, and invisible to every other check because the colours never passed through the palette at all.

That second one is the lesson worth carrying: **a colour that does not go through your token layer is a colour nothing can check.**
Syntax highlighting, embedded SVG, an iframe, a chart library's defaults — those are where accessibility quietly breaks, because the discipline you apply to CSS variables does not reach them.

If you add one thing to this site from this document, make it a contrast check in CI.
The slides run theirs on every push, alongside a PDF/UA validator, and the whole accessibility claim rests on that rather than on anyone remembering.

## 8. What does **not** transfer

Listed so nobody spends an afternoon on it.

- Everything about `ltx-talk`, `tagpdf`, `minted`, `tcolorbox` and PDF tagging.
  The web has its own accessibility model and it is a better one; PDF/UA has no analogue here.
- The `177.8/160` scale factor, and every millimetre derived from it.
  It exists because the class fixes the slide height at 100mm.
- The one-slide-per-file folder convention.
  It solves a problem — LaTeX has no way to list a directory — that Astro's content collections already solve better.
- The point sizes in the type scale, per section 5.

---

*Source: `personal-slides-template`, `theme/ricardo-palette.sty` and `scripts/check-contrast.py`.
The palette's own source of truth is `~/.config/nvim/lua/ricardo/colors.lua`; if it changes, both repositories are downstream of it.*
