# Car files and report data — 24 November 2026

User request: ten mock car reports, five homepage examples that can be refreshed, photographs, original-report field coverage, the current story format and polished UX copy. Repeated “illustrative” labels removed. One quiet sample-history note and photograph provenance retained so fictional histories are not attributed to real photographed vehicles.

## Content and source decisions

Reviewed saved original Figma report image (`knowledge/assets/vib-report-2026-11-22/figma-report.png`), original 13-page PDF text, saved carVertical sample DOM/reference catalogue and existing V5. Fresh carVertical sample URL was opened but supplied no readable report; the comparison uses dated saved evidence, not a fresh full report inspection. Independent read-only research review supplied the section/field mapping. No Figma edits.

Kept the paper-trail story and established narrative headings. Report sequence: vehicle identity + photograph → concise record context → condition score and three findings → photos → mileage/service → identity/ownership/specifications → finance → insurance/repair → challans/documents → price context → timeline → coverage/next steps. Photos and timeline follow the saved carVertical pattern; content remains VIB-specific.

Original entries retained or expanded: score, findings, identity/year/fuel/transmission/owner/registration, finance, repair claims, compliance, service history and market context. Added private usage/modification status, ownership events, service work/invoice amounts/workshop labels, structural/flood/airbag/engine coverage, reference photographs and dated timeline. Full factory equipment, peer ranking, recalls and legal searches remain explicitly unavailable/unverified instead of fabricated source results. Scores are authored sample values, not model outputs; financial and legal findings remain separate.

## Mini-brief and copy pass

Reader: a used-car buyer evaluating what to ask before viewing/transferring a car. Action: open a car file, follow evidence and ask for supporting documents. Message: a dated record gives a useful next question. Proof in this preview: explicit mock fixtures; genuine model-matched reference photographs. Preserve agreed headlines, Indian English, plain finance language and no invented real customer/provider claims.

| Previous | Applied | Reason |
| --- | --- | --- |
| Illustrative vehicle history | Vehicle history | Remove repeated process framing |
| Repeated synthetic/illustrative labels | One sample-history note, photo provenance | Keep the story readable and provenance clear |
| One fixed Swift report | Ten linked reports; five homepage files at a time | Distinct cases and browseable examples |
| Illustrative design value | Sample condition score · preset for this report preview | Preserve original score role without claiming a model calculation |
| Generic service rows | Dated work, invoice amount, source/workshop and record ID | Show what the visit contributes |
| One isolated claim amount | Repair description, status, coverage limits and next question | Avoid inferring severity from price |

The Swift photo is an actual 2020 LXI listing reference; variant changed from VXi to LXI for identity consistency. Its 72,000/58,000 km story, ₹42,000 claim and ₹3,000 challans remain consistent across homepage and report. Earlier service readings are authored fixture values, with chart/table/timeline from the same data.

## Files and refresh

`dist/cars.json` is the editable record set; all ten histories and amounts are fictional. Names/models/year/fuel/transmission and photo references were sourced from the saved CARS24 India inventory snapshot and inspected corresponding listing pages. Source URLs, retrieved date, view and image hashes are stored per photo. Masked registrations are mock identifiers. No real owner identity or adverse actual-vehicle history is asserted.

Forty genuine listing photographs downloaded as optimized local WebP, four per car (exterior and dashboard/cabin when available), total about 1.9 MB. Photos are not generated, duplicated angles or attributed to historical claims. Capture dates remain unknown. Native dialog supports enlarged viewing, Escape and focus return.

Edit records in `dist/cars.json`, then run `python3 build_reports.py`. Homepage shows the first five, then the other five through “Show five more cars”; this is user-controlled rotation, not a live feed or autonomous refresh. Optional `python3 data/refresh_photos.py` refreshes matching photo views while preserving histories; rebuild afterward. No schedule was configured.

Build uses Python + BeautifulSoup; optional photo refresh additionally uses Requests and Pillow. No frontend build dependencies.

## Verification

- Native source/resource/fragment/ARIA checks: 16 HTML routes; all 27 V4 files preserved.
- Fixture checks: ten distinct IDs, forty matched image hashes, chronology, service readings, challan totals, eight chapters, ten picker options and five visible homepage cards.
- Browser: homepage + ten distinct reports at 320/390/768/1440 (44 states), no horizontal document overflow or broken completed images. Separate Swift gallery check confirmed all four photos loaded.
- Photo dialog open/close, car selector → Brezza, expired PUC content, five-more-cars state, mobile chapter jump, motion preference and console errors checked. No console errors observed in the representative flow.
- JS syntax checked for app, motion and vehicle scripts.
- Screenshots in `qa/car-files-2026-11-24/` are local tested-source captures. No physical-device, screen-reader or participant testing claimed.

Publication: handled through existing owner-private V5 Sites identity, with current sharing preserved. Final deployment identifiers recorded in the project knowledge note after native success.
