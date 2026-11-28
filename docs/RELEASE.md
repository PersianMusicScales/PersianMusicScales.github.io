# Publication checklist

1. Review representative English and Persian articles with a musician familiar with the relevant radif. Confirm preferred transliterations, attribution, the website’s reuse terms and any publisher/contact disclosure appropriate to the final host. Recheck Qaṭar Digital Library’s manuscript catalog in a regular browser.
2. On GitHub, sign in as the repository owner and verify the exact name PersianMusicScales.github.io is available. GitHub documents the user-site naming convention at https://docs.github.com/en/pages/getting-started-with-github-pages/what-is-github-pages. Confirm the target repository and root address before enabling Pages.
3. Import this standalone source into the dedicated repository. Use a staging branch for edits and review the workflow file. Retain the release archive and tag the exact commit. Use main for the approved release.
4. Run the build and checker from README.md with PREVIEW unset. Verify the public robots file and intended canonical domain. Review the application, Atlas, Wiki and contact links. Inspect a mode page, search, the light and dark themes, and the Persian layout on intended devices.
5. After explicit launch approval, select GitHub Actions as the Pages publishing source in that repository. Approved pushes and merges to main trigger publication automatically. Use the Run workflow button on main for manual redeployment. The deployment job alone receives pages:write and id-token:write.
6. Open the public root, /en/, /fa/, a nested mode page and /sitemap.xml. Follow links to both existing project sites and verify access. Keep the Google Site available at its existing URLs. After approval add a visible bilingual notice linking to the new gateway on its homepage and high-traffic pages; retain old attribution and listening links.
7. For rollback after a later release, restore the last approved content via a revert commit on main, let the automatic workflow run its checks and deploy the revert. If the very first release must come down, use the central repository’s Pages controls after the owner approves. Record the affected release and keep both application repositories independent.

## After launch

Collect field performance data only if a privacy-compatible method is chosen and disclosed. Seek review from Persian-speaking performers and teachers. Obtain documented media permissions before embedding any recordings. Request independent validation before adding claims about recognition accuracy. Consider French once a translator and ongoing editor are available.
