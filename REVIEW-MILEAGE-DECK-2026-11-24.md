# Swift mileage and homepage case deck — 24 Nov 2026

Implemented for review on the existing private VIB V5 Site. This is prototype data, not a live vehicle lookup.

## Accepted direction and scope

The homepage hero now turns through three vehicle files: Swift mileage discrepancy, Creta active lender entry, and Brezza unpaid challan. Each illustration, finding, explanation and report link changes together. The existing navy, paper, blue ink and restrained gold treatment is retained. Existing lower homepage sections are unchanged.

Desktop uses a native sticky hero with GSAP 3D card turns as the visitor scrolls. Explicit case buttons also work. Mobile and short viewports use the same buttons without a long pinned section. Reduced motion removes the flip and scroll pin. There is no automatic timed carousel. Inactive card content is inert and hidden from assistive technology. Without JavaScript the three stories remain available.

The Swift report keeps its chapter-based story and photo gallery. Chapter introductions stay sticky on spacious desktop viewports, then return to normal document flow on mobile. The chart uses a smooth monotone cubic curve through dated service records, with a separate seller-declaration marker and discrepancy bracket. It does not imply that actual mileage fell between the two sources. The native slider, previous/next controls and pointer selection expose the seven exact dated readings. Motion never invents intermediate odometer values.

## Mock data revision

Six annual service readings are now 9,800; 21,750; 29,400; 46,300; 58,750; and 72,000 km. Dates remain 8 July 2021–2026. Uneven annual increments avoid the previous mechanically linear sequence. The later seller declaration remains 58,000 km on 20 November 2026 and the discrepancy remains 14,000 km. Invoices and timeline derive from the same data. All other Swift facts, scores, money and dates remain unchanged; all nine other car objects remain unchanged. The other nine report designs are outside the Swift-first redesign scope.

Creta and Brezza cases reuse their existing mock lender/challan entries rather than adding new adverse claims. All forty report photos remain unchanged. New generated images are supporting blue-ink illustrations, not vehicle inspection evidence; generation provenance is retained in the two art JSON files.

## Design references and skills

Applied Sites, the project design system, UX copywriting, interface-motion guidance, UI/UX chart guidance and Higgsfield generation. The core concept is a small archive of vehicle files: one car, one finding, one next step.

- Strava progress charts: direct selection of a dated point to inspect its underlying activity. https://support.strava.com/en-us/articles/15401618-progress-summary-chart
- Observable Plot curve documentation: monotone interpolation for smooth transitions through discrete points. https://observablehq.github.io/plot/features/curves

These informed interaction and interpolation choices; the UI preserves VIB's own visual system.

## Validation

Existing route/resource/fragment/ARIA checker, ten-history fixture checker, Swift scope guard and sample router checks pass. The new mileage/deck check verifies the data scope, no overshoot over 500 curve samples, seven chart states, three matching case links, unchanged lower homepage markup and protected assets.

Browser review covered 320, 375, 390, 414, 768 and 1440 px widths: no page overflow or broken completed images. All seven slider states, mobile keyboard navigation, desktop sticky introductions, desktop card turns and release to the following section, manual mobile selection and reduced-motion selection were exercised. Small-screen axis labels were simplified to prevent overlap. Assistive-technology and physical-device testing remain unverified.
