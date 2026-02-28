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

## 2024-06-07 - Audit of Sky-Watcher Esprit Series

- **Item:** Sky-Watcher Esprit 80ED, 100ED, 120ED, 150ED
- **Vendor File:** `apts/opticalequipment/telescope/vendors/sky_watcher.py`
- **Initial State:** Mass values were rounded or significantly underestimated (e.g., 150ED at 12kg vs 14.52kg). Missing explicit `aperture_mm`, `focal_length_mm`, and `central_obstruction_mm`.
- **Verified Specs (Source: Sky-Watcher Global Official Website):**
    - **Esprit 80ED:**
        - Aperture: 80mm
        - Focal Length: 400mm
        - Mass (Tube): 3.97kg -> 3970g
        - Central Obstruction: 0mm
        - Source: https://www.skywatcher.com/product/esprit-80ed-apo-triplet/
    - **Esprit 100ED:**
        - Aperture: 100mm
        - Focal Length: 550mm
        - Mass (Tube): 6.3kg -> 6300g
        - Central Obstruction: 0mm
        - Source: https://www.skywatcher.com/product/esprit-100-ed-apo-triplet/
    - **Esprit 120ED:**
        - Aperture: 120mm
        - Focal Length: 840mm
        - Mass (Tube): 9.61kg -> 9610g
        - Central Obstruction: 0mm
        - Source: http://skywatcher.com/product/esprit-120ed-apo-triplet/
    - **Esprit 150ED:**
        - Aperture: 150mm
        - Focal Length: 1050mm
        - Mass (Tube): 14.52kg -> 14520g
        - Central Obstruction: 0mm
        - Source: http://skywatcher.com/product/esprit-150ed-apo-triplet/
- **Action:** Updated database entries with verified specs and added source comments.
