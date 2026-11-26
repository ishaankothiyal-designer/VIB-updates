# VIB animation and registration widget visual QA
Scope: local screenshot-selected component improvement,26November2026. This is visual/frontend acceptance only, not production launch approval.

Source: user-selected animation screenshot in chat, original live component reproduced in owner Chrome at https://vib-v5.cars24.chatgpt.site/. Saved visual truth `.agent/uat/original-story-reference.jpg`. The attachment temporary source file was no longer present, so source was captured from the original website; visible same mileage state/layout as the attachment.
Implementation: `.agent/uat/final-stack-desktop.jpg`, local index.html#report-contents.
Density: both browser captures1469x802px at1469x802CSS viewport; attachment rendered at2938x1604px is2x the same CSS frame. No comparison of mismatched densities.
Full-view comparison: `.agent/uat/design-comparison.jpg`, viewed side by side. Focused readable card comparison `.agent/uat/design-card-comparison.jpg`, viewed side by side. Original has ownership copy above mileage while mileage card is active; implementation intentionally aligns mileage copy higher beside mileage card.

Findings and resolved iterations:
- Initial restored mileage card used horizontal readings. Changed to vertical readings to preserve selected reference. Final desktop screenshot and focused comparison confirm.
- Earlier preview had removed animated story. Restored layered cards, centered sticky companion, short transitions and active-copy rule. Mobile uses paired evidence rather than the original pinned overlay.
- No remaining P0/P1/P2 visual findings within this component scope.

Required surfaces:
- Typography: existing Libre/Plex, navy serif headings and numeric hierarchy preserved. Card heading30px, reading31px, increased card height450px vs original420px intentional for readable breathing room. No truncation.
- Spacing/layout: same two-column paper composition and420px card width; selected copy/card remain related. Active marker/progress is an intentional addition.
- Tokens: existing field/paper/navy/brass palette retained, lighter shadow and restrained sheet rotations.
- Images: original reference artwork reused; no replacement assets or placeholders. Sample source photos unchanged. Favicon uses existing repo seal.
- Copy: original fictional evidence facts preserved. Sample context retained. Widget explicitly preview/no live lookup; no fake vehicle result or OTP.

Interactions: all6desktop card states forward, reverse fast jump, one visible companion panel; dynamic reduce toggle removed stage and restored6 original cards;390px mobile paired evidence screenshot `.agent/uat/final-story-mobile.jpg`; widget empty/valid/BH-format/Enter and local anchor verified.320px,390px,412px and768px layouts have no horizontal overflow; short1469x650viewport has no sticky stage. Registration retained only in current DOM; no network/storage code.
Fallback: first-party JS resource failure simulated in Chrome, all6 evidence cards visible, widget submit disabled, sample links available. Block removed and interactive widget verified enabled again. Full Emulation disable-script test interrupted harness; this is not claimed as a completed browser-wide JavaScript-disable test.
Console: no first-party Runtime.exceptionThrown observed during observed startup. Browser-extension CSP diagnostic unrelated to site, and missing implicit favicon request identified; favicon added. Native security headers/real devices/assistive technology/field performance outside local visual acceptance.

Follow-up: real APIs and production launch acceptance remain blocked, as documented in README.

final result: passed

# Full-site homepage consistency audit,26November2026
Current scope supersedes the earlier component-only visual acceptance. All16HTMLroutes covered: index; guide index+mileage+finance+inspection;10sample vehicles; legacy sample.html (verified redirect to Swift, same flat directory).

Changes: common header primary/mobile entry, shared final CSS layers and one common footer signature on every page; report backgrounds/surfaces/heading scale/button radii and guide backgrounds/reading cards match home. Variant names wrap; sample disclosures align to report width. Mobile footer follows signature,brand,navigation,motion order. Mobile guides expose3native contents links. Data-dependent chapter order and dense report evidence remain intentional.

Visual evidence: `.agent/uat/all-pages/coverage.csv` and coverage.json contain32route/viewport entries,1440x900 desktop and390x844mobile. Fullpage captures exist for every entry; contact-desktop-1..4.jpg and contact-mobile-1..4.jpg were viewed for cover/middle/footer comparison across all16pages. Actual pixel widths1440/390 and full document heights retained. No density mismatch. Home's native sticky stage is verified interactively; a fullpage still image cannot show its changing position through the whole scroll. Prior original-vs-current stack side-by-side evidence remains in .agent/uat.

Fidelity surfaces checked: existing Libre/Plex heading/body families; navy/paper/brass tokens; shared1184px desktop column width; white evidence surfaces/5px borders; common footer contrast; no substituted report photographs or fixture claims. Source40photo hashes and10history fixtures pass protected integrity checks. No remaining P0/P1/P2 consistency findings within this scope.

Resolved iterations: missing report header CTA and15non-home refinement/footer omissions; long variant nowrap; double-inset report notice; mobile footer old grid order; mobile guide contents hidden; low-contrast new footer heading; cached old carousel/refinement assets. Both shared styles now have content hashes and deterministic order.

Control evidence: interactions.json records all10reports passed dashboard selection, fullscreen open, Escape close+focus return, previous/next reading restore and service disclosure collapse/reopen. Mobile chapter jump reaches Timeline and closes menu. guide-interactions.json records all3guide contents paths on desktop+mobile. Report and guide primary mobile actions reach same-page widget on home. Existing home widget/6-topic story and repaired carousel were verified in Chrome. Explicit Play persists over pointer/focus re-entry until Pause; real timed transitions on desktop/mobile verified. Regression check-carousel.mjs failed before fix, now green including re-entry.

12Python tests; router,input/geometry,carousel assertions;16route resource/anchor/ARIA checks;8JS syntax checks all pass in all-page-verify.txt. All16startup console checks have no localhost first-party errors; console.json separates extension diagnostics. No document/flagged-element overflow or broken loaded images in32route readbacks. Contrast calculations: footer16.69:1; guide quote15.40:1; guide body6.39:1 (specific sampled token pairs, not accessibility certification).

Independent Claude packet review completed (reference-claude-review.json and parity-claude-review.json); primary resolved playback override/cache findings and confirmed flat paths. Mobile guide retest completed after the review packet. Reviewer had no browser/files tools and did not certify live results. Safari/Firefox and physical assistive technology remain untested; no speculative relatedTarget fallback added without a reproduced defect.

Production boundary: local frontend candidate only. Real lookup/OTP/report purchase/delivery and deployment/device/performance/legal acceptance remain pending, per owner instruction to wire later. No push/deploy.

final result: passed

## Presentation revision review
The previous embedded-form acceptance is superseded by the owner's full-hero-then-registration direction.

1. Opening positioning: corrected. Initial paper folio shows three existing vehicle artworks and the repository line “Know the history. Ask a better question.” A single model is no longer the initial product identity.
2. Copy hierarchy: corrected. Repository “The car’s paper trail” and service/ownership/finance description replace the internal sample-preview heading. Company details and animation preference live in the footer. Sample labels remain next to the example data.
3. Discovery and control: corrected. Four named selectors are visible; Next, requested playback, Pause and matching report URLs verified in Chrome. No autoplay required to understand the offering.
4. Registration: frontend-only and honest. Form follows full hero and stays on page. Empty input error and valid-format unavailable state checked. No live lookup, OTP, payment or delivery is wired. This remains a real customer launch blocker, accepted for the presentation.
5. Mobile: inspected390×844, no horizontal document overflow. Desktop1440×1000 inspected. Device viewport override removed after verification.
6. Residual limits: physical devices, Safari/Firefox, full assistive-technology coverage and host production acceptance are unverified. No claims of verified universal vehicle coverage or live results.

Evidence: private .agent/uat/presentation/ screenshots; .agent/presentation-verify.txt all checks; prior complete16-route audit covers unchanged report/guide layouts. This revision does not constitute a repeated32-render audit after the shared motion text/script URL change.

## Final presentation acceptance (supersedes intermediate variants)
Source visual truth: owner screenshots at5:39:58 and5:40:45/50, live vehicleinformationbureau.com first screen, and V5 scroll reference. Captured reference .agent/uat/final-presentation/scroll-reference.png. Implementation same directory: homepage-final.png,desktop-index.html.png,mobile-index.html.png and all16route names at both sizes.
Viewports: desktop1440×1000 at1CSSpx/devicepx, mobile390×844 at1. Reference screenshot1512×~772, so scroll-comparison.jpg intentionally compares composition/active finance state, not pixel matching across different viewport heights. Both originals shown together; no claim of equal density fidelity.

Earlier P1: oversized/model-specific opening, dashboard-like outlined selectors, literal-glass interpretation and missing scroll narrative. Corrected with compact model-neutral folio, quiet selector row, original solid navy/gold/ivory and restored scroll stack. Earlier P1 mobile registration width collapse fixed with explicit auto button width. Earlier stale-script feedback fixed via content hashes.

Typography: existing display/body families and selected reference headings retained; checked wrapping at both widths. Spacing: compact opening, separate registration, reference split section titles. Color: navy/gold hero, ivory registration, pale-blue report/process and readable paper reports; final user-selected palette preserved. Images: all40fixturephoto hashes intact; no broken images in32route readback. Copy: no old operator branding in generated16routes; explicit sample and unwired service notices remain.

Interactions: all10report dashboard selection/modal/Escape/reading previous-next/service disclosure checks passed;3guide step2 links passed; carousel named selection,Next,Play,Pause passed; six evidence cards match all six active copy sections forward and reverse. Original evidence remains the accessible source; decorative stage aria-hidden. At reduced-motion rootreduced, stage removed and6originals visible; mobile also stage0 with6full-width originals.

Independent Claude review completed in .agent/final-scroll-claude-review.json. Empty/malformed story guard added. Existing chooseStep test checks selection boundaries; actual current scroll evidence replaces removed-tab evidence. Branding-match brittleness and whole-node replacement corrected and14tests rerun. Independent model did not run the browser; browser observations are primary-agent evidence.

Final full check: .agent/final-verify.txt PASS14Python plus all resource/data/photo/router/controller/syntax checks. All32rendered readbacks pass overflow/brokenimage/branding/headerfooter checks; console errors[] from tab log. Full-page/contact views reviewed for16routes; final changes after this comparison affect homepage/story only, verified directly.

Residual acceptance limits: physical devices, Safari/Firefox and full assistive-technology audit unverified. Real lookup/OTP/purchase/report delivery intentionally not connected. This is presentation frontend acceptance, not customer-service launch certification.
final result: passed

Final focus follow-up: removed double focus border after owner screenshot. Desktop/mobile verified one solid2px outer plate outline,inputoutline none,keyboardTabtoChecknow visible. Evidence final-presentation/registration-focus-*.png. Full focus-verify.txt passes.
final result: passed

## UX audit with fixes
Current-run evidence .agent/uat/ux-audit/; shareable report reports/ux-visual-audit-2026-11-26.html. Screenshot-first,7journey steps,priority finding table. Selected design retained.
P2 fixes: invalid registration previously visually normal; overly broad intro CSS enlarged helper; report notice187px on320px reduced to109.59px while retaining sample context; heading word separation. P3 fix: concise honest continuation and sample alternative.
Fresh32routecaptures and contact sheets reviewed (1440x900,390x844), plus320x800 snapshots; all shareheader/footer/oneH1,nooverflow,nobrokenimages,nooldbranding. Fourhero states fit at320px.10report gallery/modal/Escape/mileage/service interactions and3guidecontents links pass. Desktop6scrollstates andreturn; reduced-motion stages0 with6originalsvisible. Consoleerrorlog[].
Fidelity: approveddisplay/bodyfamilies retained,12pxsupportingnotes,navy/ivory/pale-blue unchanged,40photo hashes intact,copyhonestaboutdemo. Static screenshot cannot certifyscreenreadercompatibility.
BoundedClaude review caught double-space regression inSwift title; fixed source condition and fullsuite passed. Follow-up review questioned prior-history scope and repeated privacy copy: task-startdiffconfirms only authorized audit fixes; no operator/hosting changes in this task. No-save/no-send disclosure retained statically. RealHTML wrapper and newerror/clearingbehavior verified in Chrome, despite reviewer lacking DOM/tool access.
Evidence: ux-audit-verify.txt passes15tests/allchecks; ux-audit-claude-review.json and ux-audit-followup-review.json. HTML report readback10embeddedimages,0broken/externalimages,7stepsandallcaptionspresent.
Residual: realbackend intentionallyunwired; physicaldevices/Safari/Firefox/AT/fieldperformance outsidecurrentlocalverification.
final result: passed
