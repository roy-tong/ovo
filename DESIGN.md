---
name: OVO Unified Website
description: Three AI-native business-delivery products in one task workbench
colors:
  paper: "#f4f5f2"
  surface: "#ffffff"
  ink: "#10202a"
  navy: "#0d1b2a"
  navy-2: "#13283a"
  muted: "#53636c"
  line: "#d7dfda"
  teal: "#0f7c6b"
  teal-dark: "#09594e"
  mint: "#dcf1e8"
  blue: "#2868c7"
  amber: "#a96516"
typography:
  display:
    fontFamily: "Geist, PingFang SC, Hiragino Sans GB, Microsoft YaHei, sans-serif"
    fontSize: "clamp(2.55rem, 5.3vw, 4.55rem)"
    fontWeight: 780
    lineHeight: 1.06
    letterSpacing: "-0.045em"
  headline:
    fontFamily: "Geist, PingFang SC, Hiragino Sans GB, Microsoft YaHei, sans-serif"
    fontSize: "clamp(1.8rem, 3.3vw, 2.75rem)"
    fontWeight: 740
    lineHeight: 1.15
    letterSpacing: "-0.035em"
  body:
    fontFamily: "Geist, PingFang SC, Hiragino Sans GB, Microsoft YaHei, sans-serif"
    fontSize: "16px"
    fontWeight: 400
    lineHeight: 1.65
  label:
    fontFamily: "Geist Mono, ui-monospace, SFMono-Regular, Menlo, Consolas, monospace"
    fontSize: "0.74rem"
    fontWeight: 500
rounded:
  sm: "8px"
  md: "10px"
  lg: "14px"
spacing:
  sm: "12px"
  md: "24px"
  lg: "48px"
  xl: "76px"
components:
  button-primary:
    backgroundColor: "{colors.teal}"
    textColor: "#ffffff"
    rounded: "{rounded.sm}"
    padding: "10px 18px"
  button-primary-hover:
    backgroundColor: "{colors.teal-dark}"
    textColor: "#ffffff"
  filter-button:
    backgroundColor: "transparent"
    textColor: "{colors.muted}"
    rounded: "{rounded.sm}"
    padding: "7px 13px"
  filter-button-active:
    backgroundColor: "{colors.navy}"
    textColor: "#ffffff"
  task-card:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.ink}"
    rounded: "{rounded.lg}"
    padding: "24px"
---

# Design System: OVO Unified Website

## Overview

**Creative North Star: “The Shared Workbench.”**

OVO is one family with three professional services, not three independent visual brands. The site feels like a clear editorial guide wrapped around a single execution console: visitors first understand the real task, then see the mechanism and evidence, and finally start the work. Askovo, Growovo and Verovo differ in service content and proof, never in layout, typography or component behavior.

**Key Characteristics:**
- One navigation, task workbench, case library, journal and real-task entry for all three products.
- Light editorial pages balanced by one dark execution console.
- Evidence rows and service lists instead of unrelated feature-card grids.
- Real interactions stay small and useful: product switching, case/journal filtering and mobile navigation.
- Bilingual structure carries the same facts and evidence strength in Chinese and English.

## Colors

The palette is restrained: light surfaces for reading, deep navy for execution, and teal for action. Product identity is not encoded as three separate color themes.

### Primary
- **Execution Teal** (`#0f7c6b`): primary buttons, selected controls, active service markers and links.
- **Deep Teal** (`#09594e`): hover state and high-emphasis evidence text.
- **Mint Evidence** (`#dcf1e8`): evidence labels and soft status surfaces.

### Secondary
- **Workbench Navy** (`#0d1b2a`): hero, execution console and closing bands.
- **Console Navy 2** (`#13283a`): the workbench surface itself.
- **Instrument Blue** (`#2868c7`): focus indicators and technical comparisons.

### Neutral
- **Paper** (`#f4f5f2`): main page background.
- **Surface** (`#ffffff`): task cards and alternating sections.
- **Ink** (`#10202a`): primary text.
- **Muted** (`#53636c`): secondary text, metadata and evidence limits.
- **Line** (`#d7dfda`): borders, dividers and quiet structure.
- **Warning Amber** (`#a96516`): synthetic fixtures and unresolved conditions, used sparingly.

### Named Rules
**The One Console Rule.** A page may have one dominant dark execution area. Do not turn every section into a dark card or a new product theme.
**The Evidence Before Decoration Rule.** Color never upgrades evidence. Real, internal, negative, synthetic and future states are named in text before any color treatment.

## Typography

**Display Font:** Geist, with PingFang SC, Hiragino Sans GB and Microsoft YaHei fallbacks.
**Body Font:** Geist with the same Chinese system fallbacks.
**Label/Mono Font:** Geist Mono, used only for commands, metrics, dates and machine state.

The family has a direct technical-editorial voice: heavy display for the business proposition, compact body copy for evidence, and monospace reserved for code and measurable facts rather than decoration. Geist and Geist Mono are self-hosted under `assets/fonts/`.

### Hierarchy
- **Display** (780, `clamp(2.55rem, 5.3vw, 4.55rem)`, 1.06): the single family-level promise.
- **Headline** (740, `clamp(1.8rem, 3.3vw, 2.75rem)`, 1.15): module-level claims.
- **Title** (590–650, 0.94–1.22rem, 1.2): services, articles and task names.
- **Body** (400, 16px, 1.65): explanations, evidence and controls. Keep long prose near 65–75ch on wide screens.
- **Label** (500, 0.70–0.78rem): product tags, dates, metrics and command context.

### Named Rules
**The One Proposition Rule.** Each view has one dominant headline; supporting headings answer the next business question rather than repeating the brand promise.
**The Readable Translation Rule.** English and Chinese pages may use different line breaks but never different evidence strength or product claims.

## Layout

- **Container:** maximum 1180px with a 48px viewport gutter, tightening to 32px on small screens.
- **Hero:** 1.04fr / 0.96fr split at desktop, collapsing to one column below 980px. The workbench never exceeds the text viewport.
- **Sections:** 76px vertical rhythm at desktop and 58px below 760px. Use more space above a heading than below it.
- **Services:** three columns at desktop, one column below 980px. Service rows use a shared top rule rather than independent visual themes.
- **Cases and journal:** evidence rows with metadata, main finding and boundary/action. Rows become single-column below 760px.
- **Evaluation and tasks:** two-column comparison and three task entries, collapsing in the same sequence.
- **Navigation:** sticky desktop navigation, native menu button and expandable mobile panel below 760px.
- **Responsive constraints:** panel grids become one column below 520px, long English titles wrap naturally, and local links remain reachable by keyboard or touch.

## Elevation & Depth

The system is flat at rest, using borders and tonal layering for structure. The workbench is the only elevated object, because it represents the active execution surface rather than a decorative card.

### Shadow Vocabulary
- **Execution console** (`0 22px 60px rgba(3, 12, 20, 0.28)`): soft offset shadow only on the interactive workbench.

### Named Rules
**The Flat-By-Default Rule.** Do not add soft shadows to cards, filters or evidence rows. Depth belongs to the workbench, not to every container.
**The Single Motion Rule.** Motion is limited to meaningful state changes and reduced-motion fallbacks. Do not animate every section entrance.

## Shapes

- **Small controls:** 8px radius for buttons, filters and code blocks.
- **Medium containers:** 10px radius for evaluation groups and navigation panels.
- **Workbench and task cards:** 14px radius with 1px borders.
- **Tags:** compact 6px radius with evidence labels, not oversized pill decoration.
- **Service rows:** straight top rules and editorial separators instead of nested cards.
- **Icons:** consistent inline SVG strokes, used only for navigation, actions and checks.

## Components

### Buttons
- **Shape:** 8–9px radius, minimum 44px height for primary actions.
- **Primary:** teal background, white text, 10px 18px padding.
- **Hover / Focus:** deep teal background or border; 3px instrument-blue focus outline with 3px offset.
- **Secondary / Ghost:** transparent background with a quiet border, retaining contrast in the workbench.
- **Small actions:** 36px minimum height for secondary links; native button elements for all actions.

### Chips and filters
- **Style:** transparent background, muted text, 1px border, 8px radius.
- **Selected:** navy background with white text and `aria-pressed="true"`.
- **Behavior:** native buttons and keyboard focus; filtering never depends on pointer-only controls.

### Cards and containers
- **Corner style:** 14px radius with 1px border.
- **Background:** white for task cards, navy-2 for the workbench.
- **Shadow strategy:** no shadow for ordinary cards; workbench only.
- **Internal padding:** 24px for tasks and 18px for the workbench.

### Navigation
- Sticky 68px desktop navigation with OVO brand, Products, Cases, Journal, Start and language switch.
- Below 760px, use a native menu button with `aria-expanded`; menu links remain visible without JavaScript when scripting is unavailable.
- Close the mobile menu on selection, outside click and Escape. Preserve visible focus.

### Workbench
- One console with local-first product switching. Askovo is the default; Growovo and Verovo remain available without JavaScript as readable content.
- Each product panel contains its service family, value, actual evidence, installation command and repository link.
- Switching updates `aria-pressed`, visible panel and URL hash without a page reload.

### Cases and journal
- Real cases and articles share one row structure: product tag, finding, evidence boundary and action.
- Product filters use the same interaction contract in both languages.
- The journal links to canonical OVO engineering articles rather than duplicating them in another visual system.

## Do's and Don'ts

### Do:
- **Do** keep one OVO navigation, task workbench, case library, journal and task entry for all three products.
- **Do** use Geist/Geist Mono self-hosted fonts and system Chinese fallbacks.
- **Do** separate observed facts, internal use, synthetic examples and future validation in content.
- **Do** keep native buttons, visible focus, skip links, reduced motion and no-JavaScript content fallbacks.
- **Do** preserve deep product guides and examples when replacing old homepages with unified redirects.
- **Do** validate Chinese and English pages at desktop and mobile widths before deployment.

### Don't:
- **Don't** create product-specific navigation, typography, buttons, card geometry or color themes.
- **Don't** add a kicker, eyebrow, icon wall, nested cards, gradient text or decorative glass effects.
- **Don't** use monospace for general prose or as a decorative technical costume.
- **Don't** turn record counts, send volume, test counts or synthetic fixtures into adoption, savings or market-share claims.
- **Don't** make essential product, evidence or installation content depend on JavaScript.
- **Don't** deploy a new visual homepage without checking Chinese rendering, mobile overflow, interaction behavior and local links.

### Not canonized
- The previous three independently styled product homepages are not inherited as design rules. They remain migration history and deep-documentation sources only.
- The custom LibreOffice profile used for PPT export is not a website or document-production rule; it caused a Chinese font regression and was removed.
