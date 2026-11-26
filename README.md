# VIB website local preview

This is a static vehicle-history **sample preview**, based on `vikas-staging` at `64187cf`. The local review changes are on `codex/vib-user-experience`.

The preview uses ten fictional vehicle histories, preset example scores and forty model-matched reference photographs. It has no live registration lookup, payment integration, coverage verification or production score calculation. Rebuilding does not refresh the fixture dates or fetch new customer data.

## Run locally

You need Python 3 with venv/pip. The current local setup was verified with Python 3.14. Node.js is only needed to run JavaScript validation; the site itself needs no Node server or npm installation.

```bash
cd /Users/a40811/Documents/second-brain/10-Projects/vib-website
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python dev.py
```

Open **http://127.0.0.1:4336/** in Chrome. Stop the server with Ctrl+C. If the port is occupied, run `python dev.py --port 4337` and open the port printed by the command.

`dev.py` rebuilds the pages and serves only `dist/`, bound to localhost. It does not publish anything, read cloud credentials or expose the repository's private task evidence. It has no automatic rebuild watcher: after editing generators, run `python build_reports.py` or restart `dev.py`, then refresh Chrome.

You can also serve the checked-in output without installing build dependencies:

```bash
python3 -m http.server 4336 --bind 127.0.0.1 --directory dist
```

## Build and check

```bash
source .venv/bin/activate
python build_reports.py
python verify.py
```

`verify.py` rebuilds, runs the journey/metadata regression tests, validates all sixteen HTML routes and their assets/fragments/ARIA targets, checks all ten report histories and forty photo hashes, tests predictable sample routing and checks the syntax of every first-party JavaScript file in `dist/`. Node.js must be on PATH for these JavaScript checks (local validation used Node 26.13.1).

The dated `check-swift-review.py`, `check-mileage-deck.py` and `check-issue-reports.py` scripts preserve constraints from earlier, narrower design reviews. They intentionally freeze sections changed by this user-experience revision and are historical checks, not the current acceptance command. They remain available with their source records. `check.py --v4-root /actual/path/to/website-v4/dist` can additionally validate V4 only when that separate source exists; this repository does not contain it.

Browser checks are separate from these source checks. Local Chrome screenshots and results are private under `.agent/uat/`. They cover all ten report covers at 390px and 1440px, the changed homepage and selected shared interactions. Physical devices, complete assistive-technology validation and field performance are not certified by these checks.

## What changed for visitors

- An explicit preview proposition and stable sample action before the large hero illustration.
- A concern-led sample chooser, plus a native expandable list of all ten named cars. Sample choices work as ordinary links without JavaScript.
- Swift labelled as a specific example rather than implied eligibility. Actual service coverage is not promised.
- Each report-contents topic keeps its explanation with its expandable sample evidence. The detached pinned story layer is removed.
- A short three-step follow-up checklist rather than another long card story.
- Fictional-history context at the top of every report, reference-photo labels beside galleries and preset-score context beside scores.
- Generic sample URLs consistently open the Swift example; explicit car/fragment links retain their destination. No random report cycle or session storage is needed for routing.
- Hero autoplay starts paused; readers can play it or move to the next car. The global reduced-motion control appears near the first animation and retains its existing system-preference behavior.
- Shared navigation returns visitors to the sample chooser. The timeline is described as available records rather than a complete history.

## Source map

- `build_reports.py`: full generation entry point.
- `build_home.py`, `hero_deck.py`: homepage content and three-car illustrated deck.
- `build_swift_report.py`, `build_issue_reports.py`, `swift_mileage.py`: report content, individual lead stories and graphs.
- `site_content.py`: shared navigation, sample disclosures and metadata after report generation.
- `dist/cars.json`: canonical authored fixture data. Preserve its facts, dates and photo provenance unless a data change is explicitly intended.
- `dist/journey.css`: the user-experience revision using the existing navy, paper, Libre and Plex system.
- `dist/base.css`, `dist/swift-report.css`: existing foundations and report presentation.
- `dist/hero-deck.js`, `dist/swift-report.js`, `dist/motion.js`: hero transitions, report controls and the preference-aware motion owner.
- `data/sample-router-template.js`: legacy sample-entry behavior.
- `tests/`, `verify.py`: current regression and verification entry points.

The report generators first compose the original templates, then the Swift report, then the nine issue-led reports. `site_content.py` applies shared context last. Update generator sources and rebuild; do not hand-edit generated report HTML because the next build replaces it. Shared CSS/JS under `dist/` are authored sources, not bundled output.

## Deployment configuration

The GitHub Pages workflow at `.github/workflows/deploy-pages.yml` publishes checked-in `dist/` on pushes to **`ishaan-staging`**, or an explicit manual workflow run. It does not run the Python generator. The repository also has `main`, `pankaj-staging` and `vikas-staging`; a branch name alone is not a deployed environment. This task did not push, merge, run the workflow or change deployment settings.

`.openai/hosting.json` separately identifies the existing private Sites project and its `dist/` directory. Its project identity and audience have not been changed.

If an approved public launch base is available, supply it at build time:

```bash
VIB_SITE_URL=https://your-approved-domain.example/ python build_reports.py
```

The base must be HTTPS, without a query or fragment. A project subpath is supported. This writes absolute canonical/Open Graph URLs; without it, local builds have no invented canonical domain. Rebuilding without the variable removes earlier deployment URLs. The website has no need for an `.env` file, API key or secret to run locally. Domain selection, policy pages, real provider coverage and production report fulfillment still need their owning teams.
