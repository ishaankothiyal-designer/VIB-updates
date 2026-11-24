# V5 paper trail motion

24 November 2026. Scoped to `dist/motion.js`. V4 remains unchanged. The authored HTML and CSS are the full reading experience; GSAP adds short acknowledgements to already readable content.

| Moment | Treatment | Duration |
| --- | --- | --- |
| Hero copy | One short settle, 12 px desktop / 7 px mobile, opacity starts at 0.82 | 0.48 s |
| Archive assembly | Existing sheets settle in source order, same small displacement, opacity 0.84; authored paper angles retained | 0.58 s + 0.045 s stagger |
| Evidence slips | Local opacity reveal, preserves CSS paper rotations; dated values remain readable | 0.4 s + 0.07 s stagger |
| Process update | New `.desk-paper` content acknowledges a button choice, 3 px settle / opacity 0.82 | 0.22 s |
| Report/coverage change | Newly selected panel settles 4 px / opacity 0.82 | 0.22 s |
| Lower sections | `[data-reveal]`, optional child `[data-reveal-item]`; small settle with 0.04 s stagger | 0.4 s |
| Mileage evidence line | Draw once on entry, then clear stroke overrides; written values remain independent | 0.65 s |

No pinning, scroll scrubbing, pointer tilt, rotating interaction, height animation, number counting, offscreen story screen or automatic video playback is added. No content starts CSS-hidden for motion. Application code keeps ownership of ARIA, content replacement, focus and selected state; this file never moves focus or scrolls the page.

Process contract: dispatch `vib:process-change` after content update with `detail: { panel: document.querySelector('.desk-paper') }`. Report contract: `vib:report-change` with the newly visible panel. String selectors are also accepted. Each channel owns one pending frame, so successive choices replace pending animation rather than queueing them. Visible-state guards and `overwrite: auto` protect repeated switching. GSAP context teardown removes listeners and cancels both pending frames at a breakpoint/preference change.

The existing `vib-reduced-motion` sessionStorage key persists an explicit visitor choice across same-origin routes. Native reduced motion always wins and disables the manual switch. Storage access is guarded; if unavailable, the setting still works for the current page. Preference sync runs even if GSAP/ScrollTrigger fail, including disabling smooth scrolling. Activating reduction calls the GSAP preference refresh synchronously, reverting active contexts and their inline motion styles. Re-enabling does not replay already-seen hero or evidence arrivals. A native preference change uses the same refresh path. Existing static/native CSS reduced-motion rules remain necessary for any CSS transitions outside this file.

## Source verification

- `node --check design/website-v5/dist/motion.js`: passed.
- Isolated Node VM checks (no GSAP/ScrollTrigger) passed: persisted reduced choice, explicit on/off storage write, native priority, storage exceptions and native change notification. These verify fallback logic, not rendered browser behavior.
- Parent owns browser verification of actual GSAP rendering, breakpoint teardown, repeated process/coverage changes, focus stability and immediate style cleanup. No runtime success is claimed here.
