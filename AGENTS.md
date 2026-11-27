# VIB website

Static Python-generated HTML/CSS/JavaScript preview. Canonical fixture data is `dist/cars.json`. Python build dependency is pinned in `requirements.txt`. No production backend or secrets are required.

## Commands

- Setup: `python3 -m venv .venv`, then `.venv/bin/python -m pip install -r requirements.txt`.
- Build: `.venv/bin/python build_reports.py`.
- Serve and rebuild: `.venv/bin/python dev.py` (localhost4336; `--port` supported).
- Current complete source checks: `.venv/bin/python verify.py` (Node.js on PATH required).
- Targeted regressions: `.venv/bin/python -m unittest discover -s tests -v`.

These commands passed locally on2026-11-26 with Python3.14.0/Node26.13.1. Browser/device evidence is separate. Dated snapshot check scripts preserve older review scopes and are not current acceptance commands; see README.

## Editing

Edit `build_home.py`/`hero_deck.py` for homepage, report builders for report facts/layout, and `site_content.py` for shared disclosures/navigation/metadata. Rebuild generated `dist/*.html`. CSS and JS in `dist/` are authored source. Preserve fixture facts and all40reference-photo hashes unless a data change is explicitly requested.

## Verification

Run `verify.py`, inspect changed routes in the owner's Chrome at mobile and desktop widths, and exercise changed controls. Keep sample disclosures beside report titles, galleries and scores. No live-service eligibility, price, score or provider claims without evidence. Test ordinary links/no-JS reading when modifying navigation.

## Boundaries

Do not change `.openai/hosting.json`, hosting access or deployment workflow without explicit authorization. The existing Vercel setup deploys checked-in `dist/`; the hosting migration identifies `ishaan-staging` as the Production Branch. Preserve `vercel.json` and `.vercelignore`. Local changes are for owner review; do not push/create PR/merge/deploy without approval. `.agent/` and `.venv/` are ignored private/runtime state.
