# Persian Music Scales

Bilingual educational gateway created for Dr. Pouya Hosseini. This repository contains the central website. Both interactive applications retain their own repositories.

**Public website:** https://persianmusicscales.github.io/

Use the Actions tab to run “Publish Persian Music Scales” on main after reviewing edits. The workflow builds from the editable source directories and verifies the output before deploying. Persian-Music-Scales-website.zip is the original review snapshot.

## Local development

Use Python 3.9 or newer. The build and link checker use the standard library.

    python3 scripts/build.py
    python3 scripts/check.py
    python3 -m http.server 8000 --directory dist

Open http://localhost:8000/. Edit the source and repeat the first two commands to refresh rendered pages. The build replaces the generated dist directory. Deploy its contents as one unit. Clean URLs require a static host that serves directory index files.

## Structure and editing

| Location | Purpose |
|---|---|
| content/navigation.json | Home, mode directory and search introductions |
| content/modes.json | Twelve paired English and Persian mode articles |
| content/theory.json | Theory, notation and application guides |
| content/atlas.json | Historical theory, research, attribution and permissions |
| scripts/build.py | Route map, semantic page templates, navigation, metadata, search index, sitemap |
| scripts/figures.py | Clockwise 24-position circle and original graphics |
| assets | Local fonts, font licenses, theme, interaction code and social preview |
| docs | Source audit, migration decisions, verification record and release checklist |
| dist | Generated HTML, assets and sitemap |
| .github/workflows/pages.yml | Build checks and an explicitly invoked public release |

Each content key is a stable page slug. Under it keep en and fa objects with title, lead, sections and links. Sections are ordered heading/paragraph pairs. Links are label/absolute URL pairs. Text is escaped during the build. Pair translations in the same change. A new ordinary content key is generated in both editions and added to search and the sitemap. Add an editorial link from a relevant existing page. For a mode, also update MODES and its classification in the generator. Keep published slugs stable.

Edit APP and ATLAS in the generator to update common launch buttons. Article citations and feature-specific routes live in their respective JSON entries. Verify the target in its own application before changing a link. Keep a current project-method link alongside historical sources wherever interpretations differ. Edit supplements and citations in both languages together.

Use SITE_URL to choose the final absolute origin, optionally with a subpath. It defaults to https://persianmusicscales.github.io. Navigation and assets are relative. PREVIEW=1 adds noindex and disallows crawlers. For an approved public release use the default build with PREVIEW unset. See docs/RELEASE.md.

## Rights and attribution

Dr. Pouya Hosseini is the project creator. Rights and contacts for each linked application appear on the About pages. Font distributions include their SIL Open Font Licenses in assets/fonts. The new site uses original instructional diagrams and links to external recordings and manuscript collections through their sources. Inclusion of a link grants no additional redistribution rights. Confirm the intended reuse policy for the new editorial material before public release.
