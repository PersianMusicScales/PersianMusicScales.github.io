# Verification record — 23 November 2026

| Check | Observed result |
|---|---|
| Production content | 21 subjects with matching English and Persian pages plus a root entry. Standard-library checker resolved 1,014 relative references and validated headings, language direction, local resources, canonical uniqueness, alternate locales and sitemap coverage. |
| Mode studies | All twelve requested modes have individually authored English and Persian articles, two study sections and source links. Shur-family, Homayoun/Esfahan and Mahur/Rast Panjgah pages cross-reference their related entries. |
| Browser interactions | Chrome loaded the English home. Enter on the next-pitch button updated the live output to 50 cents. The theme button changed the theme. Entering شور on the English mode index left Shur visible. Selecting its language switch opened the Persian Shur article. Persian mobile menu opened and Escape restored its closed state. |
| Responsive layout | Reviewed the desktop home and mobile English/Persian home visually. Fixed horizontal overflow found on the first Persian pass. Measured zero horizontal overflow on six final representative page/viewport combinations. |
| Accessibility | axe-core 4.10.3 ran against the two homepages, English notation, Persian Shur, English search and Persian history in Chrome. Tested WCAG 2 A/AA, 2.1 A/AA and tagged 2.2 AA rules. Zero automated violations on these six samples. Manual assistive-technology testing and full conformance assessment are outstanding. |
| Performance | Browser navigation load events on the managed preview measured 99 ms (English home, 1280 px), 43 ms (Persian home, 360 px), 35 ms (English notation, 320 px), 41 ms (Persian Shur, 390 px), 35 ms (English search, 768 px) and 38 ms (Persian history, 768 px). These are unthrottled local-preview measurements with shared cache. Field Core Web Vitals and production Lighthouse scores remain unmeasured. |
| External targets | 51 of 52 distinct links returned HTTP 200. The Or 136 manuscript catalog link provided by the Atlas returned 403 to the automated check. The original project essay, checked separately, returned 200 and is included in the count. |
| Licensing and privacy | Assets served locally; source font licenses included. No third-party player, analytics script or remotely loaded font in the gateway. Each application controls its own privacy and license terms. |
| Deployment | GitHub Pages workflow prepared for manual release on main. Public GitHub deployment, real-device Safari/Android testing, external-app microphone recording, and an independent Persian language/musicology review remain outside the completed verification. |

Run python3 scripts/build.py and python3 scripts/check.py after editing translations or templates. Test both a narrow Persian page and a wide English page after changing shared layout.
