# Optic's Journal

## 2024-05-23 - Audit of Celestron AstroFi 130

- **Item:** Celestron Astro Fi 130mm Newtonian Telescope
- **Vendor File:** `apts/opticalequipment/telescope/vendors/celestron.py`
- **Initial State:** Missing aperture, focal length, and central obstruction. Generic telescope type. Mass slightly off (3500g vs 3.6kg/8lbs).
- **Verified Specs (Source: Celestron Official Website):**
    - Aperture: 130mm
    - Focal Length: 650mm
    - Central Obstruction: 38mm
    - Mass (OTA): 3.6kg (8 lbs) -> 3628g
    - Type: Newtonian Reflector
- **Action:** Updated database entry with verified specs and added source comment.
- **Source URL:** https://www.celestron.com/products/astro-fi-130mm-newtonian-telescope

## 2024-05-24 - Audit of Sky-Watcher Evostar 80ED

- **Item:** Sky-Watcher Evostar 80ED APO Refractor
- **Vendor File:** `apts/opticalequipment/telescope/vendors/sky_watcher.py`
- **Initial State:** Mass 2500g, missing explicit aperture, focal length, and central obstruction.
- **Verified Specs (Source: Sky-Watcher Official Website):**
    - Aperture: 80mm
    - Focal Length: 600mm
    - Central Obstruction: 0mm (Refractor)
    - Mass (OTA): 2.47kg -> 2470g
- **Action:** Updated database entry with verified specs and added source comment.
- **Source URL:** http://skywatcher.com/product/bk-80ed-otaw/
