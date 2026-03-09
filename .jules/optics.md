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

## 2024-05-25 - Audit of Celestron AstroMaster 130EQ

- **Item:** Celestron AstroMaster 130EQ Newtonian Telescope
- **Vendor File:** `apts/opticalequipment/telescope/vendors/celestron.py`
- **Initial State:** type: 'type_telescope', mass: 3800g, cside_thread: '2"', missing explicit aperture, focal length, and central obstruction.
- **Verified Specs (Source: Celestron Official Website):**
    - Aperture: 130mm
    - Focal Length: 650mm
    - Central Obstruction: 44mm (34% by diameter)
    - Mass (OTA): 3.5kg -> 3500g
    - Type: Newtonian Reflector
    - Focuser: 1.25"
- **Action:** Updated database entry with verified specs, corrected type and focuser size, and added source comment.
- **Source URL:** https://www.celestron.com/products/astromaster-130eq-telescope

## 2024-05-26 - Audit of Celestron AstroMaster 114EQ

- **Item:** Celestron AstroMaster 114EQ Newtonian Telescope
- **Vendor File:** `apts/opticalequipment/telescope/vendors/celestron.py`
- **Initial State:** type: 'type_telescope', mass: 2400g, cside_thread: '2"', missing explicit aperture, focal length, and central obstruction.
- **Verified Specs (Source: Celestron Official Website):**
    - Aperture: 114mm
    - Focal Length: 1000mm
    - Central Obstruction: 44mm (38% by diameter)
    - Mass (OTA): 5.9 lbs -> 2.68 kg -> 2676g
    - Type: Newtonian Reflector
    - Focuser: 1.25"
- **Action:** Updated database entry with verified specs, corrected type and focuser size, and added source comment.
- **Source URL:** https://www.celestron.com/products/astromaster-114eq-telescope

## 2024-05-27 - Audit of Celestron NexStar 130SLT

- **Item:** Celestron NexStar 130SLT Newtonian Telescope
- **Vendor File:** `apts/opticalequipment/telescope/vendors/celestron.py`
- **Initial State:** type: 'type_telescope', mass: 3500g, missing aperture, focal length, and central obstruction.
- **Verified Specs (Source: Celestron Official Website):**
    - Aperture: 130mm
    - Focal Length: 650mm
    - Central Obstruction: 38mm (29% by diameter)
    - Mass (OTA): 8.8 lbs -> 3.99 kg -> 3990g
    - Type: Newtonian Reflector
- **Action:** Updated database entry with verified specs, corrected type, and added source comment.
- **Source URL:** https://www.celestron.com/products/nexstar-130slt-computerized-telescope

## 2024-05-28 - Audit of Celestron NexStar 127SLT

- **Item:** Celestron NexStar 127SLT Maksutov-Cassegrain Telescope
- **Vendor File:** `apts/opticalequipment/telescope/vendors/celestron.py`
- **Initial State:** type: 'type_telescope', mass: 3200g, cside_thread: '2"', missing aperture, focal length, and central obstruction.
- **Verified Specs (Source: Celestron Official Website):**
    - Aperture: 127mm
    - Focal Length: 1500mm
    - Central Obstruction: 40mm (~31% by diameter)
    - Mass (OTA): 8.7 lbs -> 3.95 kg -> 3950g
    - Type: Maksutov-Cassegrain
    - Focuser: 1.25"
- **Action:** Updated database entry with verified specs, corrected type and focuser size, and added source comment.
- **Source URL:** https://www.celestron.com/products/nexstar-127slt-computerized-telescope

## 2024-05-29 - Audit of Celestron AstroMaster 70AZ

- **Item:** Celestron AstroMaster 70AZ Refractor Telescope
- **Vendor File:** `apts/opticalequipment/telescope/vendors/celestron.py`
- **Initial State:** type: 'type_telescope', mass: 1500g, missing aperture, focal length, and central obstruction.
- **Verified Specs (Source: Celestron Official Website):**
    - Aperture: 70mm
    - Focal Length: 900mm
    - Central Obstruction: 0mm (Refractor)
    - Mass (OTA): 2.9 lbs -> 1.31 kg -> 1310g
    - Type: Refractor
- **Action:** Updated database entry with verified specs, corrected type and mass, and added source comment.
- **Source URL:** https://www.celestron.com/products/astromaster-70az-telescope

## 2024-05-30 - Audit of Celestron AstroMaster 90AZ

- **Item:** Celestron AstroMaster 90AZ Refractor Telescope
- **Vendor File:** `apts/opticalequipment/telescope/vendors/celestron.py`
- **Initial State:** type: 'type_telescope', mass: 2200g, missing aperture, focal length, and central obstruction.
- **Verified Specs (Source: Celestron Official Website):**
    - Aperture: 90mm
    - Focal Length: 1000mm
    - Central Obstruction: 0mm (Refractor)
    - Mass (OTA): 5 lbs -> 2.27 kg -> 2268g
    - Type: Refractor
- **Action:** Updated database entry with verified specs, corrected type and mass, and added source comment.
- **Source URL:** https://www.celestron.com/products/astromaster-90az-telescope

## 2024-05-31 - Audit of Celestron PowerSeeker 127EQ

- **Item:** Celestron PowerSeeker 127EQ Newtonian Telescope
- **Vendor File:** `apts/opticalequipment/telescope/vendors/celestron.py`
- **Initial State:** type: 'type_telescope', mass: 3200g, cside_thread: '1.25"', missing aperture, focal length, and central obstruction.
- **Verified Specs (Source: Celestron Official Website):**
    - Aperture: 127mm
    - Focal Length: 1000mm
    - Central Obstruction: 41mm (32% by diameter)
    - Mass (OTA): 7.1 lbs -> 3.23 kg -> 3230g
    - Type: Newtonian Reflector
- **Action:** Updated database entry with verified specs, corrected type and mass, and added source comment.
- **Source URL:** https://www.celestron.com/products/powerseeker-127eq-telescope
## 2024-05-31 - Audit of Sky-Watcher Explorer 130P

- **Item:** Sky-Watcher Explorer 130P Newtonian Telescope
- **Vendor File:** `apts/opticalequipment/telescope/vendors/sky_watcher.py`
- **Initial State:** type: 'type_telescope', mass: 3200g, cside_thread: '2"', missing aperture, focal length, and central obstruction.
- **Verified Specs (Source: Sky-Watcher Official Technical Data):**
    - Aperture: 130mm
    - Focal Length: 650mm
    - Central Obstruction: 34.5mm (Verified via manufacturer technical specs)
    - Mass (OTA): 3.66kg -> 3660g
    - Type: Newtonian Reflector
    - Focuser: 1.25"
- **Action:** Updated database entry with verified specs, corrected type, mass, and focuser size, and added source comment.
- **Source URL:** http://skywatcher.com/product/explorer-130p/ (and technical data via retailers)
