# V5 minimal cards and scroll stories — 24 November 2026

## Accepted brief and design boundary

User supplied ten annotated browser comments at the existing V5 URL. Keep the project’s navy/Libre Baskerville/IBM Plex design system and the overall paper-trail story; simplify the cards, use Higgsfield and GSAP, remove redundant framing and visible dataset, and make sample-report entry choose a different car. This is an update to the existing private Site. Reports remain mock histories with reference photos. No Figma, provider or score-model changes.

Scope: `build_home.py`, `build_reports.py`, homepage output, `minimal-home.css`, `scroll-stories.js`, existing preference-aware `motion.js`, `sample-router.js`/template, contextual guide links, report picker removal and verification scripts. No existing source files deleted; only user-selected page content removed. V4 stays preserved.

## Comment-by-comment result

| Comment | Applied result |
| --- | --- |
| 1 · Cluttered header report | Sparse vehicle card with new Higgsfield ink illustration, identity and one separate mileage badge. Existing hero headline retained. GSAP arrival settles the cards. No oversized VIB/seal/caption/record-date stack. |
| 2 · Slogan strip | Removed “Read the records / Find the question / Know what to ask” strip. |
| 3 · Finding-label strip | Removed “Follow one finding / Swift mileage records” row. |
| 4 · Flat mileage section | “Let’s get into the details of this Swift.” One composed navy scene: elevated service receipt, descending connection and mechanical odometer. Native values remain selectable HTML and labelled text. |
| 5 · Repeated explanation | Removed isolated lower-reading paragraph; explanation appears once beneath the seller question. |
| 6 · Weak link | Direct action: “View this Swift’s report,” linked to that car’s mileage section. |
| 7 · Visible dataset | Entire homepage catalogue removed; report picker removed. Ten report records remain behind the sample entry action, with shuffled session rotation and no repeat until a cycle completes. |
| 8 · Contents accordion | Six naturally scrolling text points; right-hand sticky companion assembles compact evidence cards. Mobile uses a shorter companion above the current text. |
| 9 · Process buttons | Three scroll steps; left-hand companion stacks finding → original document → inspection. No click accordion needed. |
| 10 · Closing graphic | New Higgsfield report-folio and key artwork, concise HTML caption, layered surface and restrained entry motion. |

## Applicable skills and proof

Applied Sites workflow; project design-system extraction (`knowledge/design-system.md`, source-extract/tokens); UX writing playbook `agent-copywriting-expert` (plain actions, protected headline, no unsupported claims); bounded motion planning; responsive inspection; Higgsfield generation. Used Hallmark’s restraint/spacing/brand-boundary critique as review guidance; no claim of executing its complete themed workflow or unavailable support files. No unrelated brand theme or component library introduced.

Reader: used-car buyer comparing a seller’s claim with available records. Primary action: view a report. One message: the details tell you what to ask next. Existing mock Swift supplies 72,000/58,000 km, ₹42,000 claim and ₹3,000 challans. Preserve agreed headline and distinguish a discrepancy from proof of tampering. User requested no visible dataset UI; it is now implementation data only.

Two Higgsfield GPT Image 2 generations: `f2fe036c-5d6b-4848-b305-333fe1240e7c` (hatchback/archive), `05ab22f1-c269-4333-b14c-76a555a3eaec` (folio/key). Both visually inspected, optimized WebP, supporting illustrations rather than vehicle evidence. No uploaded reference image. Full provenance in `minimal-art-provenance.json`. Original model-matched report photos remain intact.

## Motion contract

- Existing locally vendored GSAP + ScrollTrigger 3.15.1, preserving the V5 motion preference owner.
- State changes follow scroll position, in either direction. No autoplay loop, snapping or scroll hijack; sticky positioning only.
- Six contents states, three process states. Current card is opaque; older cards move behind it and show paper edges. Future cards stay hidden. This avoids crossfade text ghosting found in the first implementation pass.
- Existing timing vocabulary: paper/stack 0.58 s `power2.out`, chart connection 0.65 s; short transforms and opacity only for arrivals. No flashing or image-text rasterization.
- Reduced motion: no enhancement class; all nine complete inline cards visible in normal reading order. Same fallback without GSAP. Stage copies are aria-hidden; inline evidence remains in the accessibility tree even when visually clipped in enhanced mode.
- Short mobile landscape (<620 px high) uses inline cards to avoid crowding. Standard mobile has a 300 px sticky visual and legible text beneath it.
- Data and report links work independently of motion. Generic sample entry selects a car; explicit Swift/guide evidence links keep their correct vehicle/fragment.

Official API references reviewed: https://gsap.com/docs/v3/Plugins/ScrollTrigger/ and https://gsap.com/docs/v3/GSAP/gsap.matchMedia()/ .

## Verification

- Source/resource/fragment/ARIA checker: 16 HTML routes, all27V4files unchanged.
- Fixture checks: ten histories/40 image hashes, dates/totals, no visible catalogue or report picker, six contents + three process steps.
- Router: real browser opened ten distinct reports in a cycle. Node VM independently checked two complete cycles, no adjacent boundary repeat, storage-denied fallback, sample CTA interception and hash preservation.
- Browser sample actions: mobile nav → City, next hero action → Swift; explicit Swift action → Swift#mileage.
- Responsive homepage at320/375/390/414/768/1440: no document overflow or broken completed images. Every nine scroll state at1440and390 verified (18state checks). Backward change verified. Hero finding does not overlap identity caption.
- Reduced-motion toggle produced zero enhanced stories and all nine inline cards; all active-step text remains fully opaque. Native OS preference and missing-library branches are source-backed fallbacks, not new physical-device tests.
- JS syntax checks pass. No screen-reader, physical-device or participant testing claimed. Evidence under `qa/minimal-cards-2026-11-24/`.

Publication identifiers and live verification are recorded in the project knowledge note after deployment.
