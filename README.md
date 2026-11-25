# VIB V5 — The car’s paper trail

Current: 25 November 2026. Existing private Site: https://vib-v5.cars24.chatgpt.site/ . Identity and static output configuration live in `.openai/hosting.json`; preserve audience and project ID. V4 and earlier design studies remain separate and unchanged.

## Build and preview

Buildless HTML/CSS/JavaScript with Python generators. Run `python3 build_reports.py` to rebuild the homepage, ten report routes, generic sample entry and routing script. Serve `dist/` locally, for example `python3 -m http.server 4336 --directory dist`. Sixteen HTML files comprise the homepage, ten car reports, generic sample entry and four guide routes.

`dist/cars.json` is the canonical authored mock dataset. Scores are preset, and photographs are separate model-matched listing references. No live lookup, payment, score calculation or production provider integration is implemented. Keep record dates at their fixture values; rebuilding is not a data refresh.

## Current report system

All ten reports use the minimal Swift report system: selected-photo gallery, four thumbnails and full-screen keyboard viewer; overview, eight story chapters, evidence surfaces, sources and seller questions. `build_swift_report.py` owns the original Swift story and generic no-script fallback. `build_issue_reports.py` builds the other nine with vehicle-specific facts and a lead story. `swift_mileage.py` derives graph dates, ticks, count, scale and controls from each fixture; the i20 service path stops at its actual last invoice rather than filling the missing years.

`dist/swift-report.css` owns shared report styling and responsive sticky introductions. `dist/swift-report.js` owns galleries, the accessible mileage slider, chapter progress and finite evidence arrival. `base.css` owns shared foundations/header/footer. Typography remains Libre Baskerville/IBM Plex Sans with the VIB navy, paper and restrained gold palette.

## Homepage motion

`build_home.py` and `hero_deck.py` compose the bounded homepage. No visible car catalogue or report picker: generic sample actions use a shuffled ten-car session cycle; explicit evidence links remain fixed. `hero-deck.js/css` owns the automatic three-car stack with matching CTA below. Each transition finishes the outgoing front face, commits the new case/link together and then reveals its front face. Back faces are removed and backing papers are decorative/stationary. Rapid Next requests serialize; pause, resize, visibility and preference interruptions settle to a complete case. Reduced motion retains static manual selection. Existing contents/process scroll stories remain in `scroll-stories.js`; shared preference owner is `motion.js`.

## Validation

Run:

```
python3 check.py
python3 check-fixtures.py
python3 check-swift-review.py
python3 check-mileage-deck.py
python3 check-issue-reports.py
python3 check-all-reports.py
node check-router.mjs
node --check dist/hero-deck.js
node --check dist/swift-report.js
```

The checks cover routes/assets/fragment/ARIA targets, original forty photo hashes, variable service histories, exact fixture facts and dates, scores, chapter/lead/question contracts, sample routing and protected lower homepage/assets/V4 scope. Dated scope baselines are historical; later allowlists record explicitly expanded report work. Rendered UAT, interruption cases and limitations are recorded under `docs/uat/2026-11-25-all-reports/`; these checks are not physical-device or assistive-technology certification.

## Historical records

Earlier explorations and source/generation provenance remain in `skills-integration.md`, `asset-provenance.json`, the two newer illustration provenance files, and dated review documents. `swift-report-review-2026-11-24.md`, `REVIEW-MILEAGE-DECK-2026-11-24.md` and `REVIEW-ISSUE-REPORTS-2026-11-25.md` describe previous releases. They do not supersede the current all-report scope or the user’s animation defect report.
