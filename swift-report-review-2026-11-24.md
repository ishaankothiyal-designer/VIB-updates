# Swift report — minimal design review, 24 November 2026

User requested the homepage’s minimal treatment for the report, better evidence cards and photo gallery, preserved story format, and Swift first for focused review.

## Delivered scope

Only `dist/sample-swift.html` uses the new treatment, through standalone `build_swift_report.py`, `swift-report.css` and `swift-report.js`. The full generator calls the Swift builder last so future rebuilds preserve this review version. `data/swift-report-before.html` retains the preceding report. The dated scope baseline/check verifies all89existingnon-Swiftdistfiles remain byte-identical: homepage, other nine reports, default sample entry, shared scripts/styles, fixture JSON and all photograph bytes. All27V4files also remain unchanged. No Figma, provider, audience or score-model change.

## Design and story

- Existing navy / Libre Baskerville / IBM Plex system; open reading canvas instead of one large nested folio. One main white evidence surface per chapter, understated borders/shadow, flat rows and brass accents.
- Opening combines identity, declared mileage, owner/service facts and the photo gallery. Generic sample-report header CTA removed on this Swift page to keep the review focused; toolbar offers Back to VIB and Print report.
- Condition snapshot remains separate from the three priorities; condition64is the same preset sample value. Financial/legal findings do not calculate it.
- Eight chapters preserved: photos → mileage/service → ownership → finance → repairs/insurance → challans/documents → price → timeline. Same story headings or equivalent intent, one useful seller question beneath each evidence chapter, dated source metadata and grouped coverage at the end.
- Mileage chart, reading explorer and six service invoices use the fixture readings. The important72,000/58,000km discrepancy,₹42,000claim,₹3,000challans,₹3.4–3.8lakh reference range and previous asking prices remain intact. Sample score, record histories and photo provenance remain explicit at the end.
- Work/parts/workshop/invoice data are still available; service visits default open and can be folded. Repair uncertainties are grouped in a native disclosure. Existing document, legal and factory-equipment gaps are retained. Timeline now also joins the two existing challan events; no new underlying facts.

## Photo gallery

Same four source photographs and hash identities: front right, rear right, dashboard, front left. Large selected image, labelled thumbnails with pressed state, view/count, full-screen native dialog. No generated replacement or image filtering. Next/previous buttons, arrow keys in the viewer, Home/End/arrow keys across thumbnails, Escape/close, explicit Tab/Shift+Tab focus loop and return to the opening control. Body scroll restores after close. No automatic photo movement. Native no-script fallback provides four direct photo links.

## Copy and motion

Applied the existing project foundation and the UX-writing playbook: reader is a buyer checking the available evidence; primary task is to understand each finding and ask for the right document. Preserved core facts, report story and protected footer text. Removed repeated headings, heavy nested callouts and duplicate reading-date output. Source/provider gaps are not turned into positive clearances.

Uses existing vendored GSAP + shared motion preference. Small evidence arrival (0.4s,10px,power2.out) and chart draw(0.65s); no pinned report narrative or auto-advancing photos. Reduced motion clears enhancement while keeping all content. No new Higgsfield imagery needed: the report prioritizes the existing model-matched car photographs and one small original-system finance illustration.

## Verification

- Full generator rebuild succeeded. Source/resources/fragments/ARIA checks pass for16routes; fixture checks pass for10histories/40photohashes. Swift-specific check verifies eight chapters, four original photos, six invoices, seven reading states, original key facts and89untouchedexistingnon-Swiftfiles. JS syntax passes.
- Browser at320/375/390/414/768/1440: no document overflow, no main-content element outside the viewport, no broken completed images, all eight chapters present.
- All four thumbnail views, Home/right-arrow navigation, modal next/left-arrow, Escape/close, Tab/Shift+Tab cycling and focus/scroll restoration verified. Fixed a focus-loop issue found in the first pass. At320px all gallery controls remain reachable and at least44pxhigh; no dialog horizontal overflow.
- First/latest reading selections produce12,000and58,000km respectively. Mobile chapter menu closes after selection and leaves the chapter heading clear of the sticky bar. Reduced motion keeps every evidence card visible. Representative console has no errors.
- Print media emulation hides chrome/navigation and keeps evidence visible; not a paginated PDF or physical-printer test. Print hooks expand folded record details and restore the reader’s state afterward (source checked).
- JavaScript-disabled browser check retained eight chapters/six invoice rows/four direct photograph links and hid the inactive reading control. No physical-device, touch-gesture, screen-reader or participant testing claimed.
- Local screenshots: `qa/swift-report-2026-11-24/cover-desktop.jpg`, `mileage-desktop.jpg`, `cover-mobile.jpg`, `gallery-mobile.jpg`. Live verification and deployment IDs are recorded in the project knowledge note after publication.

## Review entry and future scope

Use the direct Swift route for review, not the rotating generic sample entry. This treatment has not been applied to the other nine reports. The dated `check-swift-review.py` scope guard is specific to this review; intentionally broader future releases should update its baseline under their authorized scope.
