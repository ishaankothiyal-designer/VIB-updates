# VIB all-report rollout and animation repair — 25 November 2026

## Accepted scope

Apply the minimal Swift/Creta/Brezza treatment to the seven remaining reports. Preserve story format, own finding, photo gallery, evidence cards and seller question. Investigate the user-supplied broken automatic hero animation in detail and repair it. Keep automatic movement, no car tabs and one matching report action below the card. Preserve the authored mock dataset, scores, forty reference photos, lower homepage sections and V4. Fixture/report dates remain 24 November; task date does not refresh records.

## Findings and resolution

| Finding | Impact | Resolution / evidence |
| --- | --- | --- |
| Outgoing card rotated past −90°, exposing back face in same 3D scene as incoming face | Pale vertical plane crossed Brezza | Removed back-face markup; sequential −86° outgoing edge, atomic swap, +86° incoming face. Backing papers stationary. 66 captured observations through all three directions have at most one visible face. |
| CTA changed before incoming card was readable | Action could describe a different painted car | Commit card semantics and CTA at handoff; link inert during finite turn. Every captured frame matches active case and href; no active CTA during a turn. |
| Rapid Next killed/snap-normalized partially entered cards | Interrupted card could jump | Serialize finite transitions, retain pending requested case. Seven rapid presses plus resize settle to one readable face. |
| Preference/resize/offscreen could leave tween racing settled state | Possible residual rotation/disabled action | One cancellation/settle path; application and native reduced-motion mid-turn, resize and offscreen checks each leave one face, no stuck turn. |
| Perspective corner approached CTA | Paint could enter action gutter | 0.9 edge scale returns to 1 at rest. Minimum measured transient clearance 9.6 px at desktop; settled24.7px. Independent painted recheck passes. |
| Shared chart assumed six invoices and 2021–2026 | Wrong slider range/dates for short histories | Counts, max/value, date-proportional ticks, final invoice date and description derive from fixture. Nexon2, i20last2024, Baleno/City/Amaze5 handled. |
| Compact chart annual/end ticks collided | Nexon2026 andNov2026 overlapped | Phone charts keep first and final date only. Independent recheck and all14newreport width journeys preserve endpoint. |
| Branch copy could inherit wrong car/state | False expired PUC, missing closure, repair assumption | Data-specific branches: Venue closure document available + entry active; null claim is missing evidence; current owner count; PUC at report date; no invented transfer/closure dates. |
| City overview repeated owner row; singular grammar | Redundant copy | Distinct mileage/challan secondaries, correct singular owner, neutral policy heading for null claims. Automated assertions + independent copy recheck. |

## Report stories

| Car | Lead | Seller question |
| --- | --- | --- |
| Baleno | Five available service invoices | Can we compare these five invoices with the odometer today? |
| City | Two owners | Can we match the current seller’s details and ownership history to the registration certificate? |
| Nexon | Short history and active lender entry | Can we review the lender’s closure documents and the available service invoices? |
| Elite i20 | No service invoice after July2024 | Can we see the service invoices after July2024? |
| Venue | Closure document available, entry still active | Can we compare the closure letter with the latest registration entry? |
| Tiago | Latest asking price in context of reference range/history | How does the asking price reflect these records and the car’s condition today? |
| Amaze | Two owners and lender follow-up | Can we verify the current owner and lender closure documents before transfer? |

## Executed rendered UAT

- Three independent passes: visual/frontend QA, UX copy, brief compliance. Reviewer source findings drove fixes; visual reviewer used a separate temporary Chrome tab and closed/reset it afterward. Coordinator tested the intended in-app browser.
- All seven new reports at390and1440: direct load, refresh of lead anchor, correct cover, Dashboard thumbnail, full-screen open/next/close, vehicle-specific alt text, focus return, slider Home/End and lead story. 14journeys retained in route-gallery-checks.json with cover/lead screenshots.
- All ten reports at320/768/1024: correct titles, no horizontal overflow or broken completed images, responsive chapter behavior. Homepage375/414/834/1280/1440 and844×390landscape. 36states retained in responsive-matrix.json; combined with14newreport journeys gives50route/viewport observations.
- Full loopSwift→Creta→Brezza→Swift:66frame observations, transient screenshots and settled state after each direction, one face, no CTA mismatch, inert action while turning, positive gutter. verified-cycle-states.json and verified-turn-*.jpg.
- Rapid seven Next presses followed by resize; pause during turn; application reduced motion during turn. interruption-states.json.
- Native OS reduced-motion emulation mid-turn via CDP: autoplay paused, turn settled, one face. Emulation restored immediately.
- Scroll out of view during a turn: settled one face, action usable. Persistent pause retained same file beyond one playback interval. Automatic advancement was observed during initial review; timer still6seconds after finite-turn completion.
- JavaScript disabled: homepage renders all3static cases with their correct report links; report renders7storysections plusphotos,4nativephoto links. JavaScript execution restored/reloaded after test.
- No browser console errors observed in reviewed flows. Source visibility handler inspected; actual background-tab visibility interruption was not independently exercised in the coordinator browser.

## Automated checks

Routes/assets/fragments/ARIA/V4 preservation; ten histories and forty photo hashes; Swift content; mileage spline monotonicity; issue/all-report contracts; sample routing; JS syntax; retained UAT observation invariants. Dataset is byte/structure unchanged from the preceding release, with no live lookup or scoring change.

## Limits

Browser emulation and synthetic data only. Physical devices, assistive-technology walkthrough, participant testing and live vehicle-record provider integration are unverified. The report is not a certification of a real car. No unresolved material issue remained within the executed acceptance scope at packaging; this is not a claim of zero defects.
