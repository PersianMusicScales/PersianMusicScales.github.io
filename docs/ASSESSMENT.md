# Editorial and technical assessment

Reviewed 23 November 2026. The legacy site identifies the circular scale comparison as the project’s original teaching device. Its eleven-page inventory and the eighteen bilingual Wiki topics are mapped in MIGRATION.md. The detailed app and Atlas sources supply the methods and uncertainties behind each guide.

| Resource | Finding | Responsibility in this edition |
|---|---|---|
| Google Site | Eight named traditions distributed over seven mode pages, plus home, article, Advar and contact. Repetitive embeddings and credits. | Introductions, historical essay link and original migration map. |
| GitHub account | Public API listed Persian-Music-Scales-App, urmawi-advar-atlas and pouya-hosseini. The proposed user-site name and root returned 404 to public requests. | Dedicated review repository. A private repository or later namespace change still needs an owner-side check. |
| Main application | Public app source at revision 77d184f1400221814c3349ecd7a7f2ff1b7a37b6. Circle and transposition, calculated notation, local analysis worker, microphone, file processing, synthesized playback, ranked scale/tonic matches, V4 mode comparison and separate tuner. English, Persian and French. Cached application assets support offline use following an initial load. | Explain workflows and link to current tools. Avoid independent datasets, scores or per-mode URLs without a supported route. |
| Wiki | Nine paired English/Persian guides covering theory, scales, usage, audio, scientific and technical methods, FAQ and rights. | Deep reading and maintenance authority. |
| Advar Atlas | Independent bilingual-plus educational app. Learn, Explore, Construct, Listen, Species & Modes, and Train & Data lead from monochord experiments to a reconstruction of historical material. | Dedicated historical guide with primary-source catalog and scholarly commentary. Qualify modern reconstructions and the listening model. |
| Creator portfolio | Public biography identifies Pouya Hosseini as an electrochemist, surface scientist and musician. | Concise attribution and contact through the professional site. |

## Site map and design

English and Persian share matching slugs under /en/ and /fa/. Home opens the mode guide and the application. Theory leads to notation and a 24-position teaching circle. Modes leads to seven dastgah entries and five avaz entries. Tools explains the existing explorer and analyzer. History introduces the Atlas. Research lists primary documentation, scholarship and citation metadata. About and Search are available in the footer. The root uses the English home with its canonical at /en/.

The dark teal hero pairs original radial geometry with an editorial serif, restrained gold accents and local Vazirmatn for Persian. The language switch preserves the subject. Both themes use logical spacing and the circle retains the same clockwise pitch direction in either language.

Python static generation keeps 21 subjects synchronized in two languages without a CMS, account system or client framework. A future editor needs to rebuild after a change. Each route works as ordinary HTML and analysis remains in the existing apps. All font and drawing requests stay on the gateway origin.

## Review decisions

The app dataset assigns distinct identities to Mahur and Rast Panjgah despite a shared pitch model. Role labels can depend on context or carry provisional status. The V4 passage comparison, Natural Minor test and circle ranking use distinct evidence. Numerical accuracy for one evaluation cannot automatically be used for the others. The Wiki’s broader use of ist can obscure a temporary pause versus a final close. The gateway distinguishes these terms in context.

The earlier article’s 60-degree equal-spacing statement conflicts with its cent-proportional mapping. The current guide uses 360 degrees per 1,200 cents. The Google Site uses open-source language despite restrictive application terms. Website access does not settle reuse rights. The Atlas points to a cataloged manuscript, while modern explanatory illustrations and synthesis are editorial choices. Each project retains its own notices.

The first edition prioritizes full English and Persian coverage. The application’s French edition makes French a plausible later gateway language after commissioning the paired editorial review. Other useful additions are permission-cleared, annotated performances for the listening prompts and independent validation of the current recognition pipeline.
