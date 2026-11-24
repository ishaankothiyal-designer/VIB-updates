# Creta, Brezza and automatic case deck — 25 November 2026

## User direction

Bring Creta and Brezza up to the Swift report standard while keeping the story format. Creta leads with its lender entry, Brezza with its challan. Change the homepage stack from scroll-led/manual tabs to automatic movement with the matching report action underneath. Interpreted “city under it” as CTA based on the immediately preceding “View Brezza’s Report” instruction; no location was invented.

## Implementation

Both reports reuse the Swift typography, quiet evidence surfaces, desktop sticky introductions, source rows, seller questions and eight-chapter story. Creta starts with the active entry, missing closure documents and current registration to verify. Brezza starts with its one ₹1,500 unpaid challan and existing expired PUC date. Secondary service, ownership, repair, policy, valuation and timeline details come from each car’s own unchanged fixture.

Each report has its four original model-matched reference photos, a selected photo with thumbnails, a full-screen dialog, previous/next controls, Escape and arrow-key navigation, focus containment and return. The shared gallery now accepts a vehicle name instead of hard-coding Swift in image descriptions. Both get the interactive smooth mileage chart, scaled to their actual values and correctly describing the seller reading as higher. Brezza’s 96,300 km fits the enlarged axis. The Swift retains its lower-reading finding.

The homepage automatically turns through Swift, Creta and Brezza with GSAP, with six seconds per file and the same 0.65-second incoming turn. Removed tabs and the long sticky scroll sequence. Static left introduction; the card carries its own finding and short explanation. One matching “View …’s report” link sits directly below. Minimal pause and next controls remain. Hover, keyboard focus, an out-of-view deck or a hidden page stops the timer. Reduced motion stops automatic movement and removes the turn while retaining next-car access. Without JavaScript all three cases and their report links remain available. Links and findings update together.

## Content and scope

Dataset unchanged, including preset scores, lender/challan/PUC facts and all forty photo hashes. No live lookup, score model, payment or finance workflow was added. Seven other report files remain unchanged; lower homepage sections and V4 remain unchanged. New builder `build_issue_reports.py` runs after the Swift builder and uses that report shell, with all chapters replaced from the correct car fixture. All photography and illustrations are reused, with their existing provenance; no generation was needed.

Applied Sites, the project report design system, agent-copywriting-expert and specify-interface-motion skills. Copy brief: a used-car buyer reading a sample report; take a specific evidence-based question to the seller; lead with the individual finding; use existing fixture dates/amounts/statuses; preserve British English, direct copy and a discreet sample provenance note.

## Validation

Automated routes/resources/ARIA/fragments, ten histories and forty photo hashes, Swift content, smooth-curve scope, sample routing and issue-report scope checks pass. Browser checks at 320, 375, 390, 414, 768 and 1440 px show no horizontal page overflow or broken completed images for both reports and homepage. Tested each new gallery, correct vehicle descriptions, full-screen controls and focus return; Brezza slider reaches 96,300 km with “4,300 km above”; Creta exposes 64,900 km with “2,900 km above.” Automatic playback observed changing case and matching link, with no tabs. Physical-device and assistive-technology testing remain unverified.

Additional browser results: persistent pause held the same file beyond a full playback interval; next controls exposed matching Creta and Brezza report URLs; reduced motion reported autoplay paused and retained next-car selection. All three cases kept 26 px clearance above the CTA at 320 px. Browser console errors: none observed in the reviewed flow.
