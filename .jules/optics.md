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

## 2024-05-31 - Audit of Sky-Watcher Heritage 130P variants

- **Item:** Sky-Watcher Heritage 130P, Heritage 130P FlexTube, Heritage P130 FlexTube, Virtuoso GTi 130P, Starquest 130P, Star Discovery 130i
- **Vendor File:** `apts/opticalequipment/telescope/vendors/sky_watcher.py`
- **Initial State:** type: 'type_telescope', missing aperture, focal length, and central obstruction. Various mass values (3000g-3300g).
- **Verified Specs (Source: Sky-Watcher Official Website / Manual):**
    - Aperture: 130mm
    - Focal Length: 650mm
    - Central Obstruction: 34.5mm
    - Mass (OTA): 3.25 kg -> 3250g (Standard for FlexTube 130 variants)
    - Type: Newtonian Reflector
    - Focuser: 1.25"
- **Action:** Updated all 130/650 Heritage/Tabletop variants with verified specs, corrected type, and added source comment.
- **Source URL:** http://skywatcher.com/product/heritage-p130/

## 2024-05-31 - Audit of ZWO ASI664MC

- **Item:** ZWO ASI664MC Color Camera
- **Vendor File:** `apts/opticalequipment/camera/vendors/zwo.py`
- **Initial State:** Incorrect resolution (3840x2160 instead of 2704x1536), incorrect pixel size (2.0µm instead of 2.9µm), incorrect full well capacity (35ke- instead of 36.5ke-), and incorrect backfocus (6.5mm instead of 12.5mm).
- **Verified Specs (Source: ZWO Official Manual):**
    - Sensor: Sony IMX664 (1/1.8")
    - Resolution: 2704 x 1536
    - Pixel Size: 2.9µm
    - Sensor Dimensions: 7.841mm x 4.454mm
    - Full Well: 36.5 ke- (36500e-)
    - Read Noise: 0.46e-
    - Backfocus: 12.5mm
- **Action:** Updated database entry with verified specs and added source URL.
- **Source URL:** https://www.bhphotovideo.com/lit_files/1114240.pdf (Official ZWO Product Manual)

## 2024-06-01 - Audit of Celestron StarSense Explorer DX 130

- **Item:** Celestron StarSense Explorer DX 130 Newtonian Telescope
- **Vendor File:** `apts/opticalequipment/telescope/vendors/celestron.py`
- **Initial State:** type: 'type_telescope', mass: 5000g, missing aperture, focal length, and central obstruction.
- **Verified Specs (Source: Celestron Official Website):**
    - Aperture: 130mm
    - Focal Length: 650mm
    - Central Obstruction: 45mm (34% by diameter)
    - Mass (OTA): 8.8 lbs -> 3.99 kg -> 3990g
    - Type: Newtonian Reflector
    - Focuser: 2" (with 1.25" adapter typically, but tube side is 2" for these DX models)
- **Action:** Updated database entry with verified specs and added source comment.
- **Source URL:** https://www.celestron.com/products/starsense-explorer-dx-130az

## 2024-06-02 - Audit of Celestron StarSense Explorer LT series

- **Items:** Celestron StarSense Explorer LT 114AZ, LT 127AZ, LT 80AZ
- **Vendor File:** `apts/opticalequipment/telescope/vendors/celestron.py`
- **Initial State:**
    - LT 114AZ: type: 'type_telescope', mass: 4000g, focuser: 2", missing aperture/focal/CO.
    - LT 127AZ: Missing from database.
    - LT 80AZ: type: 'type_telescope', mass: 1800g, missing aperture/focal/CO.
- **Verified Specs (Source: Celestron Official Website):**
    - **LT 114AZ:**
        - Aperture: 114mm
        - Focal Length: 1000mm
        - Central Obstruction: 44mm (38% by diameter)
        - Mass (OTA): 6.6 lbs -> 2.99 kg -> 2990g
        - Type: Newtonian Reflector
        - Focuser: 1.25"
    - **LT 127AZ:**
        - Aperture: 127mm
        - Focal Length: 1000mm
        - Central Obstruction: 41mm (32% by diameter)
        - Mass (OTA): 7.6 lbs -> 3.44 kg -> 3440g
        - Type: Newtonian Reflector
        - Focuser: 1.25"
    - **LT 80AZ:**
        - Aperture: 80mm
        - Focal Length: 900mm
        - Central Obstruction: 0mm (Refractor)
        - Mass (OTA): 5.4 lbs -> 2.45 kg -> 2450g
        - Type: Refractor
        - Focuser: 1.25"
- **Action:** Updated LT 114AZ and LT 80AZ with verified specs; added LT 127AZ with full verified specs. Added source comments.
- **Source URLs:**
    - https://www.celestron.com/products/starsense-explorer-lt-114az
    - https://www.celestron.com/products/starsense-explorer-lt-127az
    - https://www.celestron.com/products/starsense-explorer-lt-80az

## 2024-06-03 - Audit of Sky-Watcher Explorer 150P

- **Item:** Sky-Watcher Explorer 150P Newtonian Telescope
- **Vendor File:** `apts/opticalequipment/telescope/vendors/sky_watcher.py`
- **Initial State:** type: 'type_telescope', mass: 5200g, cside_thread: '2"', missing aperture, focal length, and central obstruction.
- **Verified Specs (Source: APM Telescopes / Manufacturer Technical Data):**
    - Aperture: 150mm
    - Focal Length: 750mm (f/5)
    - Central Obstruction: 47mm
    - Mass (OTA): 5.9 kg -> 5900g
    - Type: Newtonian Reflector
    - Focuser: 1.25" (Standard visual model has 1.25" focuser)
- **Action:** Updated database entry with verified specs, corrected type, mass, and focuser size, and added source comment.
- **Source URL:** https://www.apm-telescopes.net/en/skywatcher-explorer-150p-newtonian-reflector-ota

## 2024-06-04 - Audit of Sky-Watcher Skyliner series

- **Items:** Sky-Watcher Skyliner 150P, 200P, 250P, 300P and their FlexTube/variants.
- **Vendor File:** `apts/opticalequipment/telescope/vendors/sky_watcher.py`
- **Initial State:** Generic `type_telescope` type. Missing explicit aperture, focal length, and central obstruction. Mass values were rounded or inaccurate.
- **Verified Specs (Sources: Sky-Watcher Official, First Light Optics, Agena Astro):**
    - **Skyliner 150P:** 153mm / 1200mm (f/8), CO 34.5mm, Mass 5.9kg OTA.
    - **Skyliner 200P (inc. FlexTube):** 203mm / 1200mm (f/6), CO 47mm, Mass 11kg OTA.
    - **Skyliner 250P:** 254mm / 1200mm (f/4.7), CO 58mm, Mass 12.5kg OTA.
    - **Skyliner 250P FlexTube:** 254mm / 1200mm (f/4.7), CO 58mm, Mass 15kg OTA.
    - **Skyliner 300P:** 305mm / 1500mm (f/4.9), CO 70mm, Mass 19.5kg OTA.
    - **Skyliner 300P FlexTube:** 305mm / 1500mm (f/4.9), CO 70mm, Mass 21kg OTA.
    - **Skyliner 350P FlexTube:** 355mm / 1650mm (f/4.65), CO 83mm, Mass 23.5kg OTA.
    - **Skyliner 400P:** 406mm / 1800mm (f/4.4), CO 102mm, Mass 38kg OTA.
- **Action:** Updated all models with verified physical specs, set type to `newtonian_reflector`, and added source comments. Verified with `scripts/verify_skyliner_specs.py`.
- **Source URLs:**
    - https://www.skywatcherusa.com/products/sky-watcher-classic-200p
    - https://www.firstlightoptics.com/dobsonians/skywatcher-skyliner-150p-dobsonian.html
    - https://agenaastro.com/sky-watcher-14-goto-collapsible-dobsonian-telescope-s11830.html

## 2024-06-05 - Audit of Celestron Omni XLT series

- **Items:** Celestron Omni XLT 102, 120, 127 SCT, 150, 150R
- **Vendor File:** `apts/opticalequipment/telescope/vendors/celestron.py`
- **Initial State:** Generic `type_telescope` type for most. Missing explicit aperture, focal length, and central obstruction. Placeholder or inaccurate mass values.
- **Verified Specs (Source: Celestron Official Website):**
    - **Omni XLT 102:** 102mm / 1000mm (f/9.8), CO 0mm, Mass 4.31kg (9.5 lbs). Type: Refractor.
    - **Omni XLT 120:** 120mm / 1000mm (f/8.33), CO 0mm, Mass 5.67kg (12.5 lbs). Type: Refractor.
    - **Omni XLT 127 SCT:** 127mm / 1250mm (f/9.84), CO 40mm, Mass 2.95kg (6.5 lbs). Type: Schmidt-Cassegrain.
    - **Omni XLT 150:** 150mm / 750mm (f/5), CO 47mm, Mass 5.44kg (12 lbs). Type: Newtonian Reflector.
    - **Omni XLT 150R:** 150mm / 750mm (f/5), CO 0mm, Mass 7.26kg (16 lbs). Type: Refractor.
- **Action:** Updated all models with verified physical specs, set correct optical types, and added source comments.
- **Source URLs:**
    - https://www.celestron.com/products/omni-xlt-102-telescope
    - https://www.celestron.com/products/omni-xlt-120-telescope
    - https://www.celestron.com/products/omni-xlt-127-telescope
    - https://www.celestron.com/products/omni-xlt-150-telescope
    - https://www.celestron.com/products/omni-xlt-150-refractor-telescope
