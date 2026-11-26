# OVO unified website

One static site for Askovo, Growovo and Verovo. It replaces three independently styled product homepages with one OVO workbench, case library, engineering journal and real-task entry.

## Modules

- `index.html` / `en.html`: family promise, interactive product workbench, three flagship service groups, evaluation model, evidence preview and task entry.
- `cases.html` / `en-cases.html`: product-filtered real research, internal use, negative results and synthetic examples with explicit evidence boundaries.
- `journal.html` / `en-journal.html`: six OVO engineering deep dives and Verovo’s agent-economics article, filterable by product. The full essay archive remains at https://roy-tong.github.io/essays/.
- `start.html` / `en-start.html`: independent installation and real-task entry for all three products.
- `llms.txt`: machine-readable product selection, module links, repositories and evidence boundaries.

## Design system

- Light editorial surfaces with one navy execution console and precise teal actions.
- Geist display and code fonts, self-hosted under `assets/fonts/`; system Chinese fallbacks.
- Shared navigation, spacing, typography, service lists, evidence rows, filter buttons, task cards and responsive rules.
- Product identity comes from service content and proof, not inconsistent layouts or themes.
- No framework, tracking, external script, build step or runtime dependency.
- Product switching and case/journal filtering use native buttons and keyboard focus. Essential content remains available without JavaScript.
- Mobile navigation, skip links, reduced motion and print fallbacks are included.

## Local preview

```bash
cd website
python3 -m http.server 4173 --bind 127.0.0.1
# Open http://127.0.0.1:4173/
```

## Content maintenance

- Product service descriptions and quickstart commands live in `index.html` and `en.html`.
- Cases live in both case pages; keep real research, internal use, negative results and synthetic examples explicitly separate.
- Journal entries live in both journal pages and link to the canonical OVO engineering articles. Add new articles in the same product structure and update both languages.
- `llms.txt`, `sitemap.xml`, `robots.txt` and `assets/social-preview.png` use the canonical `/ovo/` path. Update them when the public URL changes.
- `PRODUCT.md` records durable product truth. `DESIGN.md` records the implemented visual system after browser review.

## Deployment

The canonical site is `https://roy-tong.github.io/ovo/`, served from the `main` branch of `roy-tong/ovo` with GitHub Pages. The repository also publishes the 20-page OVO family BP as PDF and editable PPTX under `assets/bp/`.

The three product repositories retain deep guides and examples while their former homepages redirect here. Product installation commands on this site intentionally pin the current prerelease versions; external business delivery and adoption remain separately validated.

For subsequent changes, run `python3 internal/check_site.py`, commit to `main`, push, and verify the public pages, old-product redirects, deep documentation links, social preview and `llms.txt`.
