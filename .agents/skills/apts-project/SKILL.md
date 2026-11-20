---
name: apts-project
description: Project structure, architecture, conventions, and key modules for the APTS astronomical planning library.
disable-model-invocation: false
---

# APTS — Astronomical Planning and Tracking System

## Overview

APTS (~200 KLOC Python) is a library for amateur astronomers and astrophotographers. It handles equipment management, observation planning, weather analysis, celestial event detection, and email notifications. Version `0.15.7`, Apache 2.0, by Łukasz Pożarlik. Backs [stargazer.earth](https://stargazer.earth).

## Quick Stats

- **Python 3.14+**, pure setuptools (`setup.py`), no build-system in `pyproject.toml`
- **~200 test files** under `tests/` (unit, integration, plotting, equipment, weather)
- **i18n**: 4 languages (de, es, pl, pt), Babel `.mo` compilation, thread-safe via `threading.local()`
- **Data modes**: `light` (bundled, fast) vs `full` (downloads large JPL ephemeris + MPCORB)
- **Config**: `~/.config/apts/apts.ini`, split into sub-modules under `apts/config/`
- **CI**: GitHub Actions on pushes/PRs to `master` — installs `libcairo2-dev`, compiles locale `.mo` files, runs flake8 + pytest.

## Top-Level Layout

```
apts/         → Main source package (public API + internal modules)
data/         → Large ephemeris SPK files (de421.bsp, Jovian, Hipparcos)
docs/         → PERFORMANCE_OPTIMIZATIONS.md, bom.json, licenses.md
examples/     → Usage examples (apts.ini template, performance scripts, skymap demo)
scripts/      → Utility scripts (audit, compile_translations, benchmark, format DB, verify specs)
tests/        → ~200 test files under unit/, integration/, plotting/, weather/, equipment/
stations.txt  → TLE orbital elements (ISS, CSS, other satellites)
```

## Core Public API (`apts/`)

| Symbol | Module | Description |
|---|---|---|
| `Observation` | `observations/base.py` | Central class — ties `Place` + `Equipment`, manages date range, triggers events, weather, visibility |
| `Place` | `place/base.py` | Location — lat/lon/elevation/timezone, day/night tracking |
| `Equipment` | `equipment/` | Equipment manager — register gear, compute magnifications/FOV, optical path finding |
| `Weather` | `weather/base.py` | Aggregates forecasts from plugin-based providers (PirateWeather, OpenWeatherMap, StormGlass, Visual Crossing, MeteoBlue) |
| `Notify` | `notify/client.py` | SMTP email sender with HTML Jinja templates |
| `Utils` | `utils/` | Shared helpers — astronomy, coordinates, graph pathfinding, FITS analyzer, polar alignment |
| `Conditions` | `conditions.py` | Observing condition thresholds (moon, seeing, SQM, clouds, wind, etc.) |
| `Catalogs` | `catalogs/` | Singleton — loads Messier, NGC, bright stars from bundled CSVs |
| `set_language()` | `i18n.py` | Set thread-local language for gettext |
| `download_all_data()` | `cache/base.py` | Download all ephemeris/catalog data |
| `get_events()` | `api.py` | Simplified facade — lat/lon + date range → astronomical events list |

## Key Internal Modules

| Module | Description |
|---|---|
| `cache/` | Cached access to Skyfield timescale/ephemeris, Hipparcos/MPCORB catalogs, NASA comets, scoring cache |
| `conditions.py` | `Conditions` dataclass with cloud/wind/temperature/precipitation/visibility/fog/aurora thresholds |
| `config/` | INI-file config reader/writer — weather, events, data mode, performance, place defaults |
| `constants/` | Enums — event types, astronomy constants, constellations, graph labels, plot constants, twilight, strategies |
| `equipment/` + `opticalequipment/` | **Massive vendor database** (hundreds of files) — telescopes, cameras, eyepieces, barlows, reducers, filters, adapters, plus optical path computing (backfocus, thread/gender compatibility) |
| `events/` + `skyfield_searches/` | Event calculation framework — conjunctions, occultations, meteor showers, eclipses, Jovian moon/GRS, satellite flybys, planetary alignments, culminations, twilight, rise/set |
| `i18n.py` | Thread-safe internationalization with `.po`/`.mo` files in `locale/` |
| `light_pollution.py` | Bortle scale / light pollution models |
| `observations/` | `Observation`, `ObservationWindow`, event integration, catalogs, weather engine, plotting dispatchers, HTML report generation |
| `objects/` | Astronomical object models — Messier, NGC, stars, solar system (MPC lookups), almanac, visibility |
| `optics/` | `OpticalPath` — full optical train simulation, formulas for refraction, exposure, FOV, photometry, resolution |
| `plotting/` | matplotlib/seaborn/pycairo/SVG — skymaps (polar, zoomed, textured), altitude charts, Jovian moons, sun/moon paths, weather plots |
| `scoring/` | `SuitabilityScorer` — rates observation windows by conditions |
| `secrets.py` | API key/secret management |
| `units.py` | Pint-based physical unit registry |
| `weather/` | Weather models and plugin-based providers |

## Conventions

1. **Lazy loading**: Heavy imports (`Observation`, `Place`, `Equipment`, `Weather`, `Notify`, pandas, seaborn) deferred via `__getattr__` in `apts/__init__.py`.
2. **Thread-safe i18n**: Language stored in `threading.local()`, use `set_language()` / `gettext_()` / `language_context()`.
3. **Config-driven**: All behavior controlled via `~/.config/apts/apts.ini` — weather provider, event types, data mode, performance auto-preload.
4. **Vendor-per-file**: Equipment specs in `type/vendors/vendor_name.py` — hundreds of files with real commercial product specs.
5. **Skyfield-first**: Primary ephemeris/TLE engine is Skyfield; `ephem` library is secondary fallback.
6. **Conditions pattern**: `Conditions` dataclass passed to weather analysis/plotting methods; `None` = defaults cached on `Observation`.

## Development

```bash
# Setup
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements-dev.txt
pip install -e .

# Compile translations
pybabel compile -d apts/locale

# Run tests
pytest

# Lint + type-check
ruff check .
pyright

# Single test file
pytest tests/unit/test_observation.py -v
```

## Remember

- Always run `pybabel compile` after editing `.po` files.
- Tests use `light` data mode and mocked weather (requests-mock) for speed.
- Before adding a new equipment vendor file, check the existing pattern in `opticalequipment/<type>/vendors/`.
