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
- **Initial State:** Generic `type_telescope` type for most. Missing explicit aperture, focal length, and central obstruction. Mass values were rounded or inaccurate.
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

## 2024-06-06 - Audit of Celestron OTA and Beginner series

- **Items:** Celestron C6, C8, C9.25, C11, C14 OTA assemblies, FirstScope 76, and Inspire 100AZ.
- **Vendor File:** `apts/opticalequipment/telescope/vendors/celestron.py`
- **Initial State:**
    - OTA models had generic `type_telescope` type, missing aperture/focal/CO, and rounded/inaccurate mass values.
    - FirstScope 76: missing aperture/focal/CO, incorrect mass (1000g).
    - Inspire 100AZ: missing aperture/focal/CO, incorrect mass (3500g).
- **Verified Specs (Source: Celestron Official Website):**
    - **C6 OTA:** 150/1500mm, CO 56mm, Mass 4.54kg (10 lbs). Type: Schmidt-Cassegrain.
    - **C8 OTA:** 203.2/2032mm, CO 64mm, Mass 5.67kg (12.5 lbs). Type: Schmidt-Cassegrain.
    - **C9.25 OTA:** 234.95/2350mm, CO 85mm, Mass 9.07kg (20 lbs). Type: Schmidt-Cassegrain.
    - **C11 OTA:** 279.4/2800mm, CO 95mm, Mass 12.47kg (27.5 lbs). Type: Schmidt-Cassegrain.
    - **C14 OTA:** 355.6/3910mm, CO 114mm, Mass 20.41kg (45 lbs). Type: Schmidt-Cassegrain.
    - **FirstScope 76:** 76/300mm, CO 28mm, Mass 0.64kg (1.4 lbs OTA). Type: Newtonian Reflector.
    - **Inspire 100AZ:** 100/660mm, CO 0mm, Mass 2.2kg (4.9 lbs OTA). Type: Refractor.
- **Action:** Updated all models with verified physical specs and documentation sources. Created `tests/unit/test_celestron_ota_specs.py` for verification.
- **Source URLs:**
    - https://www.celestron.com/products/c6-optical-tube-assembly-cg-5-dovetail
    - https://www.celestron.com/products/c8-optical-tube-assembly-cg-5-dovetail
    - https://www.celestron.com/products/c9-1-4-optical-tube-assembly-cg-5-dovetail
    - https://www.celestron.com/products/c11-optical-tube-assembly-cge-dovetail
    - https://www.celestron.com/products/c14-optical-tube-assembly-cge-dovetail
    - https://www.celestron.com/products/firstscope-telescope
    - https://www.celestron.com/products/inspire-100az-refractor-telescope

## 2024-06-07 - Audit of Meade LX85, LX200, and LX600 ACF series

- **Items:** Meade LX85 ACF 6", 8"; LX200 ACF 8", 10", 12", 14", 16"; LX600 ACF 10", 12", 14".
- **Vendor File:** `apts/opticalequipment/telescope/vendors/meade.py`
- **Initial State:**
    - Rounded aperture values (e.g., 203mm for 8", 254mm for 10").
    - Rounded or inaccurate focal lengths (e.g., 2000mm for LX200 8", should be 2032mm).
    - Rounded mass values for several models.
- **Verified Specs (Sources: Meade Official Manuals, Agena Astro, OPT Telescopes):**
    - **LX85 ACF 6":** 152.4mm / 1524mm, CO 56mm, Mass 4.49kg (9.9 lbs OTA).
    - **LX85 ACF 8":** 203.2mm / 2032mm, CO 76mm, Mass 5.76kg (12.7 lbs OTA).
    - **LX200 ACF 8":** 203.2mm / 2032mm, CO 76mm, Mass 6.35kg (14 lbs OTA).
    - **LX200 ACF 10":** 254.0mm / 2540mm, CO 94mm, Mass 11.79kg (26 lbs OTA).
    - **LX200 ACF 12":** 304.8mm / 3048mm, CO 102mm, Mass 16.33kg (36 lbs OTA).
    - **LX200 ACF 14":** 355.6mm / 3556mm, CO 117mm, Mass 22.68kg (50 lbs OTA).
    - **LX200 ACF 16":** 406.4mm / 4064mm, CO 127mm, Mass 30.39kg (67 lbs OTA).
    - **LX600 ACF 10" (f/8):** 254.0mm / 2032mm, CO 121mm, Mass 12.25kg (27 lbs OTA).
    - **LX600 ACF 12" (f/8):** 304.8mm / 2438mm, CO 146mm (48% dia), Mass 16.78kg (37 lbs OTA).
    - **LX600 ACF 14" (f/8):** 355.6mm / 2845mm, CO 171mm (48% dia), Mass 23.13kg (51 lbs OTA).
- **Action:** Updated all models with verified physical specs and accurate mass/obstruction data. Added source comments. Created `tests/unit/test_meade_specs.py` for verification.
- **Source URLs:**
    - https://agenaastro.com/meade-lx200-telescope-specifications.html
    - https://agenaastro.com/meade-lx600-telescope-specifications.html
    - https://optcorp.com/products/lx85-6-acf-ota-only
    - https://eu.levenhuk.com/catalogue/telescopes/meade-lx85-8-acf-ota/

## 2024-06-08 - Audit of Takahashi Telescopes

- **Items:** Takahashi FSQ, FC, TSA, TOA, Epsilon, and Mewlon series.
- **Vendor File:** `apts/opticalequipment/telescope/vendors/takahashi.py`
- **Initial State:**
    - Refractors missing explicit `central_obstruction_mm: 0`.
    - Epsilon series had incorrect or missing central obstruction values (secondary minor axis).
    - Some mass values were slightly off or rounded.
- **Verified Specs (Sources: Takahashi Europe, Takahashi America, Agena Astro, Astronomics):**
    - **FSQ-85EDP:** Aperture 85mm, FL 450mm, Mass 3.6kg OTA, CO 0mm.
    - **FSQ-106ED:** Aperture 106mm, FL 530mm, Mass 6.8kg OTA, CO 0mm.
    - **Epsilon-130D:** Aperture 130mm, FL 430mm, CO 63mm.
    - **Epsilon-160ED:** Aperture 160mm, FL 530mm, CO 63mm.
    - **Epsilon-180ED:** Aperture 180mm, FL 500mm, Mass 10.7kg, CO 80mm.
    - **Mewlon-180C:** Aperture 180mm, FL 2160mm, CO 54mm (30% dia).
    - **Mewlon-210:** Aperture 210mm, FL 2415mm, CO 65mm (31% dia).
- **Action:** Updated all Takahashi models with verified physical specs, explicit central obstruction values, and added source comments. Verified with `tests/unit/test_takahashi_specs.py`.
- **Source URLs:**
    - https://takahashi-europe.com/catalog/refractors/wide-field-astrographs/fsq-85edx
    - https://takahashi-europe.com/catalog/refractors/wide-field-astrographs/fsq-106edx4
    - https://takahashi-europe.com/catalog/reflectors/epsilon/epsilon-130d
    - https://takahashi-europe.com/catalog/reflectors/epsilon/epsilon-160ed
    - https://takahashi-europe.com/catalog/reflectors/epsilon/epsilon-180ed
    - https://takahashi-europe.com/catalog/reflectors/mewlon/mewlon-180c
    - https://takahashi-europe.com/catalog/reflectors/mewlon/mewlon-210

## 2024-06-09 - Audit of Sky-Watcher Specialty and Desktop series

- **Items:** Sky-Watcher SkyMax (90, 102, 127, 150, 180), Heritage (76, 100P), Star Discovery (150P, 150i, 200P), Stargate (450P, 500P), AZ-EQ Newtonians, Starquest 80MC, Black Diamond ED, and Equinox series.
- **Vendor File:** `apts/opticalequipment/telescope/vendors/sky_watcher.py`
- **Initial State:**
    - Many models used generic `type_telescope` type.
    - Missing aperture, focal length, and central obstruction values.
    - Inaccurate or placeholder mass values.
- **Verified Specs (Sources: Sky-Watcher USA, First Light Optics, Agena Astro, Scope Views):**
    - **SkyMax 90/102/127/150/180:** Corrected Maksutov-Cassegrain specs and central obstructions (e.g., 180 Pro: 180/2700mm, CO 52mm).
    - **Heritage 76/100P:** Added missing physical specs (e.g., 100P: 100/400mm, CO 34mm, 1.1kg OTA).
    - **Star Discovery 150P/200P:** Corrected Newtonian specs (e.g., 150P: 150/750mm, CO 47mm, 4.9kg OTA).
    - **Stargate 450P/500P:** Added verified large-aperture specs (e.g., 500P: 508/2000mm, CO 136mm, 65kg assembled).
    - **Black Diamond ED & Equinox:** Verified refractor specs and masses.
    - **Starquest 80MC:** Corrected to Maksutov-Cassegrain (80/1000mm, CO 26mm).
- **Action:** Updated 23 Sky-Watcher models with verified physical specs, correct optical types, and accurate mass data. Added source comments. Verified with `tests/unit/test_sky_watcher_specs.py`.
- **Source URLs:**
    - https://www.skywatcherusa.com/products/sky-watcher-skymax-180
    - https://www.firstlightoptics.com/telescopes-in-stock/skywatcher-heritage-76-mini-dobsonian.html
    - https://agenaastro.com/sky-watcher-18-stargate-dobsonian-telescope-goto-s11920.html
    - http://www.scopeviews.co.uk/SWEq80ED.htm

## 2024-06-10 - Audit of William Optics Telescopes

- **Items:** William Optics RedCat 51, GT153, Pleiades 68, Pleiades 111.
- **Vendor File:** `apts/opticalequipment/telescope/vendors/william_optics.py`
- **Initial State:**
    - RedCat 51 mass was 1800g (actual 3.2 lbs / 1.45kg).
    - GT153 focal length was 1056mm (actual 1188mm) and mass 8400g (actual 13.5kg).
    - Pleiades 68 focal length was 260mm (actual 258.4mm) and mass 3800g (actual 2.98kg OTA).
    - Pleiades 111 was missing from the database.
- **Verified Specs (Source: William Optics Official & Support Documentation):**
    - **RedCat 51:** Aperture 51mm, FL 250mm, Mass 1.45kg OTA, CO 0mm.
    - **GT153:** Aperture 153mm, FL 1188mm, Mass 13.5kg OTA, CO 0mm.
    - **Pleiades 68:** Aperture 68mm, FL 258.4mm, Mass 2.98kg OTA, CO 0mm.
    - **Pleiades 111:** Aperture 111mm, FL 528mm, Mass 7.95kg OTA, CO 0mm.
- **Action:** Updated RedCat 51, GT153, and Pleiades 68 with verified physical specs. Added Pleiades 111 with verified specs. Ensured all refractor models have explicit `central_obstruction_mm: 0` and correct optical type. Added source comments. Verified with `tests/unit/test_william_optics_specs.py`.
- **Source URLs:**
    - https://support.williamoptics.com/products/gran-turismo-153
    - https://support.williamoptics.com/products/pleiades-68
    - https://williamoptics.com/products/pleiades-111
    - https://astrobackyard.com/william-optics-redcat-51/

## 2024-06-11 - Audit of GSO Ritchey-Chrétien, Newtonian, and Dobson series

- **Items:** GSO RC (6, 8, 10, 12), GSO Newtonian (6" f/5, 8" f/4, 8" f/5), and GSO Dobson (6, 8, 10, 12).
- **Vendor File:** `apts/opticalequipment/telescope/vendors/gso.py`
- **Initial State:**
    - All models missing `central_obstruction_mm`.
    - Many mass values were rounded or slightly off.
    - RC 6 focal length was correct (1370mm), but mass was placeholder (5400g).
- **Verified Specs (Sources: Agena Astro, Optical Universe, APM Telescopes, Teleskop-Service):**
    - **RC 6":** 152mm / 1370mm, CO 71mm, Mass 5.58kg.
    - **RC 8":** 203mm / 1624mm, CO 85mm, Mass 7.5kg.
    - **RC 10":** 254mm / 2000mm, CO 110mm, Mass 15kg.
    - **RC 12":** 304mm / 2432mm, CO 130mm, Mass 21kg.
    - **Newton 6" f/5:** 150mm / 750mm, CO 50mm, Mass 5.9kg OTA.
    - **Newton 8" f/4:** 200mm / 800mm, CO 70mm, Mass 8.9kg (OTA + acc).
    - **Newton 8" f/5:** 200mm / 1000mm, CO 63mm, Mass 9kg.
    - **Dobson 6":** 152mm / 1200mm, CO 42mm, Mass 8.3kg OTA.
    - **Dobson 8":** 203mm / 1200mm, CO 47mm, Mass 11.1kg OTA.
    - **Dobson 10":** 254mm / 1250mm, CO 64mm, Mass 18kg OTA.
    - **Dobson 12":** 305mm / 1520mm, CO 70mm, Mass 21.7kg OTA.
- **Action:** Updated all GSO models with verified physical specs, explicit central obstruction values, and added source comments. Created `tests/unit/test_gso_specs.py` for verification.
- **Source URLs:**
    - https://agenaastro.com/gso-8in-f4-newtonian-imaging-reflector-ota-eaf-focuser.html
    - https://agenaastro.com/gso-6in-f5-newtonian-reflector-ota.html
    - https://www.opticaluniversescientificinstrument.com/products/gso-6-ritchey-chretien-telescope
    - https://www.apm-telescopes.net/en/gso-dobson-teleskop-250c-offnung-10-zoll-mit-hochwertigem-crayford-auszug

## 2026-03-03 - Audit of Explore Scientific Telescopes

- **Items:** Explore Scientific ED FCD100 series (80, 102, 127, 152), Essential series (80, 102, 127), AR series (102, 127, 152), FirstLight Newtonians (114, 130, 152, 203), FirstLight Maksutovs (100, 127, 152), Truss Dobs (10", 12", 16"), and Comet Hunter 152 Mak-Newt.
- **Vendor File:** `apts/opticalequipment/telescope/vendors/explore_scientific.py`
- **Initial State:**
    - Many models used generic `type_refractor` or `newtonian_reflector` without specific central obstruction.
    - Missing aperture, focal length, and central obstruction values for several models.
    - Mass values were rounded or generic (e.g., 3500g for multiple models).
- **Verified Specs (Source: Explore Scientific Official Website / Manuals):**
    - **ED80/102/127/152 FCD100:** Corrected masses (e.g., 102: 4.94kg) and ensured `central_obstruction_mm: 0`.
    - **FirstLight 130mm Newtonian:** 130/600mm, CO 45mm, Mass 3175g (7 lbs).
    - **FirstLight 152mm Mak:** 152/1900mm, CO 47mm, Mass 7710g (17 lbs).
    - **Truss Dobs:** Corrected CO values (10": 61.5mm, 12": 63mm, 16": 88mm) and OTA masses.
    - **Comet Hunter 152 Mak-Newt:** 152/731mm, CO 49mm, Mass 6.9kg.
- **Action:** Updated all Explore Scientific models with verified physical specs, explicit central obstruction values, and added missing models. Created `tests/unit/test_explore_scientific_specs.py` for verification.
- **Source URLs:**
    - https://explorescientific.com/products/explore-firstlight-130mm-newtonian-telescope-fl-n130600
    - https://explorescientific.com/products/ed102-fcd-100
    - https://explorescientific.com/products/16-truss-tube-dobsonian
    - https://telescopescanada.ca/products/explore-scientific-firstlight-6-inch-maksutov-cassegrain-ota-only-fl-mc1521900

## 2026-03-23 - Audit of Sharpstar Telescopes

- **Items:** Sharpstar 61EDPH II, 61EDPH III, 76EDPH II, 94EDPH II, 140PH, 13028HNT, 15028HNT, 20032HNT.
- **Vendor File:** `apts/opticalequipment/telescope/vendors/sharpstar.py`
- **Initial State:**
    - Refractors (61EDPH II, 76EDPH II, 94EDPH II, 140PH) were missing `central_obstruction_mm`.
    - 94EDPH II mass was 4400g (gross weight), corrected to 3300g (net).
    - 15028HNT mass was 5950g (gross weight), corrected to 4450g (net).
    - 15028HNT and 20032HNT were missing `central_obstruction_mm`.
    - 61EDPH III and 13028HNT were missing from the database.
- **Verified Specs (Source: Sharpstar Official Website / High Point Scientific / First Light Optics):**
    - **61EDPH II:** Aperture 61mm, FL 335mm, Mass 1.5kg, CO 0mm.
    - **61EDPH III:** Aperture 61mm, FL 360mm, Mass 1.48kg, CO 0mm.
    - **76EDPH II:** Aperture 76mm, FL 418mm, Mass 2.3kg, CO 0mm.
    - **94EDPH II:** Aperture 94mm, FL 517mm, Mass 3.3kg, CO 0mm.
    - **140PH:** Aperture 140mm, FL 910mm, Mass 10.1kg, CO 0mm.
    - **13028HNT:** Aperture 130mm, FL 364mm, Mass 3.2kg, CO 65mm.
    - **15028HNT:** Aperture 150mm, FL 420mm, Mass 4.45kg, CO 70mm.
    - **20032HNT:** Aperture 200mm, FL 640mm, Mass 8.0kg, CO 90mm.
- **Action:** Updated all Sharpstar models with verified physical specs, explicit central obstruction values, corrected masses (converting gross weight to net weight), and added missing models. Added source comments. Verified with `tests/unit/test_sharpstar_specs.py`.
- **Source URLs:**
    - https://www.sharpstar-optics.com/Products_1/72.html
    - https://www.sharpstar-optics.com/Products_1/20.html
    - https://www.sharpstar-optics.com/Products_1/27.html
    - https://all-startelescope.com/products/sharpstar-94edph
    - https://www.sharpstar-optics.com/Products_1/50.html
    - https://astronomytechnologytoday.com/2020/11/12/sharpstar-20032pnt/

## 2026-03-24 - Audit of Vixen Telescopes

- **Items:** Vixen VC200L, VMC200L, R200SS, SD81S, SD103S, SD115S, AX103S, FL55SS, VSD100.
- **Vendor File:** `apts/opticalequipment/telescope/vendors/vixen.py`
- **Initial State:**
    - VC200L central obstruction was 75mm.
    - Refractors were missing explicit `central_obstruction_mm: 0`.
    - Some formatting inconsistencies.
- **Verified Specs (Source: Vixen Official Website / B&H Photo / Bintel Australia):**
    - **VC200L:** Aperture 200mm, FL 1800mm, Mass 6.0kg, CO 77mm.
    - **VMC200L:** Aperture 200mm, FL 1950mm, Mass 5.9kg, CO 80mm.
    - **R200SS:** Aperture 200mm, FL 800mm, Mass 5.3kg, CO 65mm.
    - **Refractors (SD81S, SD103S, SD115S, AX103S, FL55SS, VSD100):** Ensured `central_obstruction_mm: 0` and verified OTA masses.
- **Action:** Updated all Vixen models with verified physical specs and source comments. Updated VC200L central obstruction to 77mm based on technical spec data. Verified with `tests/unit/test_vixen_specs.py`.
- **Source URLs:**
    - https://global.vixen.co.jp/en/product/2632_02/
    - https://global.vixen.co.jp/en/product/58291_0/
    - https://www.bresser.com/p/vixen-r200ss-reflector-telescope-X000315
    - https://global.vixen.co.jp/en/product/37102_4/
    - https://global.vixen.co.jp/en/product/37103_1/

## 2026-03-25 - Audit of Sky-Watcher Newtonians and Refractors

- **Items:** Sky-Watcher 250PDS, Explorer 250P, Heritage 150P, Heritage 150P FlexTube, Star Adventurer GTi 80ED.
- **Vendor File:** `apts/opticalequipment/telescope/vendors/sky_watcher.py`
- **Initial State:**
    - 250PDS had rounded aperture (250mm).
    - Explorer 250P had rounded mass (14000g).
    - Heritage 150P models had system mass (7500g) instead of OTA mass.
    - Star Adventurer GTi 80ED was missing optical properties.
- **Verified Specs (Source: Sky-Watcher Official Website / First Light Optics):**
    - **250PDS:** Aperture 254mm, FL 1200mm, Mass 14.38kg, CO 63mm.
    - **Explorer 250P:** Aperture 254mm, FL 1200mm, Mass 14.38kg, CO 58mm.
    - **Heritage 150P:** Aperture 150mm, FL 750mm, Mass 3.7kg (OTA), CO 47mm.
    - **Star Adventurer GTi 80ED:** Aperture 80mm, FL 600mm, Mass 2.6kg, CO 0mm.
- **Action:** Updated all models with verified physical specs and added source comments. Updated `tests/unit/test_explorer_p_specs.py` and `tests/unit/test_sky_watcher_specs.py` to match new data.
- **Source URLs:**
    - https://www.firstlightoptics.com/reflectors/sky-watcher-explorer-150p-ds-with-eqm-35-pro-mount.html
    - http://skywatcher.com/product/bkp-250-ds/
    - https://www.skywatcherusa.com/products/esprit-80mm-ed-triplet-apo-refractor
## 2026-03-25 - Audit of Orion Telescopes

- **Items:** Orion EON (80, 110, 130), 8" f/3.9 Astrograph, XT8/10/12 Classic Dobs, SpaceProbe 130ST.
- **Vendor File:** `apts/opticalequipment/telescope/vendors/orion.py`
- **Initial State:**
    - Mass values were rounded or slightly off (e.g., EON 130mm was 10200g, corrected to 10210g based on 22.5 lbs).
    - Refractors were missing explicit `central_obstruction_mm: 0`.
    - SpaceProbe 130ST was missing `central_obstruction_mm` (added 36.4mm based on 28% diameter obstruction).
    - XT Dobs had slightly off mass values (e.g., XT8 corrected from 9300g to 9210g based on 20.3 lbs).
- **Verified Specs (Sources: Orion Telescopes & Binoculars Official Website / Manuals / High Point Scientific):**
    - **EON 130mm ED:** 130/910mm, Mass 10.21kg (22.5 lbs), CO 0mm.
    - **8" f/3.9 Astrograph:** 203/800mm, Mass 7.94kg (17.5 lbs), CO 70mm.
    - **EON 110mm ED:** 110/660mm, Mass 5.22kg (11.5 lbs), CO 0mm.
    - **EON 80mm ED:** 80/500mm (or 560mm/480mm variants, but 500mm confirmed for the triplet), Mass 2.95kg (6.5 lbs), CO 0mm.
    - **XT8 Classic Dob:** 203/1200mm, Mass 9.21kg (20.3 lbs OTA), CO 47mm.
    - **XT10 Classic Dob:** 254/1200mm, Mass 13.11kg (28.9 lbs OTA), CO 63mm.
    - **XT12 Classic Dob:** 305/1500mm, Mass 22.68kg (50.0 lbs OTA), CO 70mm.
    - **SpaceProbe 130ST:** 130/650mm, Mass 2.81kg (6.2 lbs OTA), CO 36.4mm (28%).
- **Action:** Updated all Orion telescope models with verified physical specs and added source comments. Created `tests/unit/test_orion_specs.py` for verification.
- **Source URLs:**
    - https://www.telescope.com/Orion-EON-130mm-ED-Triplet-Apochromatic-Refractor-Telescope/p/114817.uts
    - https://www.highpointscientific.com/amfile/file/download/file/1110/product/9530/
    - https://www.telescope.com/Orion-SpaceProbe-130ST-Equatorial-Reflector-Telescope/p/9007.uts
    - https://www.telescope.com/Orion-SkyQuest-XT8-Classic-Dobsonian-Telescope/p/102005.uts

## 2026-03-25 - Audit of Svbony Telescopes

- **Items:** SV503 (70ED Doublet, 70ED Quadruplet, 80ED, 102ED), SV550 (60, 80, 122), SV48P (90, 102).
- **Vendor File:** `apts/opticalequipment/telescope/vendors/svbony.py`
- **Initial State:**
    - SV503 70ED doublet was the only 70mm model.
    - SV503 80ED/102ED had rounded or placeholder mass values.
    - SV48 (90mm) was mislabeled and had incorrect mass.
    - SV503 70ED Quadruplet and SV48P 102mm were missing.
    - Refractors were missing explicit `central_obstruction_mm: 0`.
- **Verified Specs (Sources: Svbony Official Website / Blog / APM Telescopes):**
    - **SV503 70ED Doublet:** 70/420mm (f/6), Mass 2.22kg, CO 0mm.
    - **SV503 70ED Quadruplet:** 70/474mm (f/6.78), Mass 2.685kg, CO 0mm.
    - **SV503 80ED:** 80/560mm (f/7), Mass 3.00kg (OTA net weight), CO 0mm.
    - **SV503 102ED:** 102/714mm (f/7), Mass 4.00kg (OTA net weight), CO 0mm.
    - **SV550 60/80/122:** Verified masses and focal lengths.
    - **SV48P 90:** 90/500mm (f/5.5), Mass 2.73kg, CO 0mm.
    - **SV48P 102:** 102/663mm (f/6.5), Mass 3.40kg, CO 0mm.
- **Action:** Corrected existing models to use "Net Weight" (OTA only) for load calculation precision. Added new 70mm Quad and 102mm Achromat models without breaking existing keys. Renamed SV48 display name to SV48P 90. Ensured refractor `central_obstruction_mm: 0`.
- **Source URLs:**
    - https://www.svbony.com/blog/sv503-70-ed-telescope
    - https://www.svbony.com/products/sv503-70mm-flatfield-refractor-telescope
    - https://www.svbony.com/products/sv48p-102mm-achromatic-refractor-telescope-set-for-visual-observation
    - https://stargazerslounge.com/topic/390656-svbony-102ed-f7-refractor-first-light-impressions-sv503/

## 2026-03-26 - Audit of Bresser Telescopes

- **Items:** Messier AR-102xs, AR-127L, AR-152L, AR-152S, MC-127, MC-152, NT-150L, NT-203, NT-203s, NT-254.
- **Vendor File:** `apts/opticalequipment/telescope/vendors/bresser.py`
- **Initial State:**
    - Missing `central_obstruction_mm` for all models.
    - Many mass values were rounded or slightly off (e.g., NT-254 was 14000g, corrected to 16400g).
    - MC models were generically typed as `catadioptric`.
    - AR-152S and NT-203s were missing from the database.
- **Verified Specs (Sources: Bresser Official Website, India Telescope Shop, Astro Telescopios):**
    - **AR-102xs:** 102/460mm, Mass 2.8kg, CO 0mm.
    - **AR-127L:** 127/1200mm, Mass 7.9kg, CO 0mm.
    - **AR-152L:** 152/1200mm, Mass 11.1kg, CO 0mm.
    - **AR-152S:** 152/760mm, Mass 10.6kg, CO 0mm.
    - **MC-127:** 127/1900mm, Mass 3.4kg, CO 35mm. Type: Maksutov-Cassegrain.
    - **MC-152:** 152/1900mm, Mass 6.5kg, CO 45mm. Type: Maksutov-Cassegrain.
    - **NT-150L:** 150/1200mm, Mass 6.5kg, CO 45mm.
    - **NT-203:** 203/1000mm, Mass 11.5kg, CO 60mm.
    - **NT-203s:** 203/800mm, Mass 8.7kg, CO 85mm.
    - **NT-254:** 254/1270mm, Mass 16.4kg, CO 74mm.
- **Action:** Updated all models with verified physical specs, explicit central obstruction values, corrected masses, and added missing models. Added source comments for all entries. Verified with `verify_bresser.py`.
- **Source URLs:**
    - https://www.bresser.com/p/bresser-messier-ar-102xs-460-exos-1-eq4-4702467
    - https://www.bresser.com/p/bresser-messier-mc-127-1900-ota-optical-tube-4827190
    - https://www.indiatelescopeshop.com/product-page/bresser-messier-10-dobsonian

## 2026-04-10 - Audit of QHY Cameras

- **Items:** QHY268C, QHY268M, QHY600C, QHY600M.
- **Vendor File:** `apts/opticalequipment/camera/vendors/qhy.py`
- **Initial State:**
    - QHY268 series resolution was 6248x4176.
    - QHY268 series mass was 800g.
    - QHY600 series mass was 1050g.
    - QHY600C QE was 80%.
- **Verified Specs (Source: QHYCCD Official Website / Manuals):**
    - **QHY268C/M:** Effective pixels 6252 x 4176. Peak QE 92%. Mass 780g. Backfocus 17.5mm (standard with adapter).
    - **QHY600C/M:** Peak QE 91%. Mass 900g. Backfocus 17.5mm (standard with adapter).
- **Action:** Updated specifications for QHY268 and QHY600 series with verified data. Used effective resolution for FOV calculation accuracy. Corrected OTA masses.
- **Source URLs:**
    - https://www.qhyccd.com/astronomical-camera-qhy268/
    - https://www.qhyccd.com/astronomical-camera-qhy600/

## 2026-05-20 - Audit of Sky-Watcher Esprit and Quattro series

- **Items:** Esprit 80ED, 100ED, 120ED, 150ED, Quattro 150P, 200P, 250P, 300P.
- **Vendor File:** `apts/opticalequipment/telescope/vendors/sky_watcher.py`
- **Initial State:**
    - Esprit 150ED mass was 14520g.
    - Quattro 250P central obstruction was 82mm.
    - Quattro 300P central obstruction was 100mm.
- **Verified Specs (Source: Sky-Watcher Global / USA Official Website & Manuals):**
    - **Esprit 150ED:** Mass 15.0kg (OTA).
    - **Quattro 200P:** Aperture 200mm (8"), Central Obstruction 70mm.
    - **Quattro 250P:** Central Obstruction 89mm (35% linear).
    - **Quattro 300P:** Central Obstruction 102mm (33.4% linear).
- **Action:** Corrected Esprit 150ED mass and Quattro 250P/300P central obstructions. Added official source URLs and physical verified data in comments for Esprit and Quattro models. Standardized `type` to `type_refractor` for consistency across the Sky-Watcher database.
- **Source URLs:**
    - http://skywatcher.com/product/esprit-100-ed-apo-triplet/
    - http://skywatcher.com/product/esprit-120ed-apo-triplet/
    - http://skywatcher.com/product/esprit-80ed-apo-triplet/
    - https://inter-static.skywatcher.com/upfiles/en_download_caty01416868668.pdf (Esprit 150 Manual)
    - http://skywatcher.com/series/astrophotography-reflectors/
    - https://www.skywatcherusa.com/products/sky-watcher-quattro-250p-imaging-newtonian-10-254-mm
    - https://www.skywatcherusa.com/products/sky-watcher-quattro-300p-imaging-newtonian-12-305-mm

## 2026-05-21 - Audit of Sky-Watcher Evolux and Explorer/Quattro series

- **Items:** Evolux 62ED, Evolux 82ED, Explorer 200P, Quattro 200P.
- **Vendor File:** `apts/opticalequipment/telescope/vendors/sky_watcher.py`
- **Verified Specs (Source: Sky-Watcher Global / First Light Optics):**
    - **Evolux 62ED:** Aperture 62mm, FL 400mm, Mass 2.5kg (2500g). CO 0mm.
    - **Evolux 82ED:** Aperture 82mm, FL 530mm, Mass 2.92kg (2920g). CO 0mm.
    - **Explorer 200P:** Aperture 200mm, FL 1000mm, Mass 8.8kg (8800g). CO 52mm.
    - **Quattro 200P:** Aperture 205mm, FL 800mm, Mass 9.5kg (9500g). CO 70mm.
- **Action:** Updated all models with verified physical specs and added official source URLs in comments. Corrected Quattro 200P aperture to 205mm. Verified via static analysis of the database.
- **Source URLs:**
    - http://www.skywatcher.com/product/evolux-62ed/
    - http://www.skywatcher.com/product/evolux-82ed/
    - https://www.firstlightoptics.com/reflectors/skywatcher-explorer-200p-ota.html
    - http://skywatcher.com/product/quattro-200-st/

## 2026-05-22 - Audit of iOptron Photron RC and Refractor series

- **Items:** Photron RC 6", 8", 10" (Steel & Truss), 12" (Truss), 16" (Truss), and R80 refractor.
- **Vendor File:** `apts/opticalequipment/telescope/vendors/ioptron.py`
- **Initial State:** RC 6/8 had inaccurate mass and central obstruction values. RC 10/12/16 and R80 were missing. APO 80/102 were missing explicit central obstruction.
- **Verified Specs (Source: iOptron Official Website / Manuals):**
    - **Photron RC 6":** 150/1370mm, CO 67mm, Mass 5.44kg (12 lbs).
    - **Photron RC 8":** 200/1624mm, CO 95mm, Mass 8.16kg (18 lbs).
    - **Photron RC 10" (Steel):** 250/2000mm, CO 110mm, Mass 15.88kg (35 lbs).
    - **Photron RC 10" (Truss):** 254/2032mm, CO 110mm, Mass 15.42kg (34 lbs).
    - **Photron RC 12" (Truss):** 304/2432mm, CO 150mm, Mass 24.04kg (53 lbs).
    - **Photron RC 16" (Truss):** 406/3250mm, CO 171mm (est), Mass 42.18kg (93 lbs).
    - **R80 Achromatic:** 80/400mm, CO 0mm, Mass 1.0kg (2.2 lbs).
- **Action:** Updated RC6/RC8, added RC10/12/16 and R80 with verified specs. Standardized APO 80/102 with explicit `central_obstruction_mm: 0`. Added source comments.
- **Source URLs:**
    - https://www.ioptron.com/product-p/6111.htm (RC6)
    - https://www.ioptron.com/product-p/6112.htm (RC8)
    - https://www.ioptron.com/product-p/6113af.htm (RC10 Steel)
    - https://www.ioptron.com/v/Manuals/611X_RCTruss_Manual.pdf (RC Truss Manual)
    - https://www.ioptron.com/product-p/8710.htm (R80)

## 2024-06-12 - Audit of Stellarvue Telescopes

- **Items:** Stellarvue SVX (070T, 080T, 090T, 102T, 130T, 152T), SV60EDS, SV70T, Access (80, 102, 48).
- **Vendor File:** `apts/opticalequipment/telescope/vendors/stellarvue.py`
- **Initial State:**
    - Missing explicit `aperture_mm`, `focal_length_mm`, and `central_obstruction_mm`.
    - `mass` values were placeholders (e.g., 2800g for SVX080T).
- **Verified Specs (Sources: Stellarvue Official Manuals / Product Pages / AstroBin / OpticsPlanet):**
    - **SVX080T:** 80/480mm (f/6), Mass 2.95kg (6.5 lbs OTA).
    - **SVX102T:** 101.5/714mm (f/7), Mass 4.5kg (9.9 lbs OTA).
    - **SVX130T:** 130/910mm (f/7), Mass 7.62kg (16.8 lbs OTA).
    - **SVX152T:** 152/1200mm (f/7.9), Mass 10.52kg (23.2 lbs OTA).
    - **SV60EDS:** 60/330mm (f/5.5), Mass 1.13kg (2.5 lbs OTA).
    - **SV70T:** 70/420mm (f/6), Mass 2.5kg (5.5 lbs OTA).
    - **SVX090T:** 90/540mm (f/6), Mass 3.2kg (7.0 lbs OTA).
    - **Access 80:** 80/560mm (f/7), Mass 2.72kg (6.0 lbs OTA).
    - **Access 102:** 102/714mm (f/7), Mass 4.31kg (9.5 lbs OTA).
    - **SVX070T Raptor:** 70/420mm (f/6), Mass 1.81kg (4.0 lbs OTA).
- **Action:** Updated all 20 entries in `apts/opticalequipment/telescope/vendors/stellarvue.py` with verified physical specifications, ensuring `central_obstruction_mm: 0` for all refractors and correcting mass values to OTA-only weights. Added source comments. Verified with `scripts/verify_stellarvue_static.py`.
- **Source URLs:**
    - http://www.stellarvue.com/manuals/SVX80T-3SV_manual.pdf
    - https://www.stellarvue.com/product/svx102t
    - https://www.stellarvue.com/manuals/SVX130T_manual.pdf
    - https://telescope.fandom.com/wiki/Stellarvue_SVX152T
    - https://stargazerslounge.com/topic/234836-stellarvue-sv-60eds-unbox-mini-review/
    - https://ssr.app.astrobin.com/equipment/explorer/telescope/333/stellarvue-sv70t
    - https://www.stellarvue.com/product/svx090t
    - https://galileotelescope.com/telescopes/stellarvue-access-80mm-super-ed-2-5-sv-focuser-with-d1029ed-and-case.html

## 2026-05-23 - Audit of ZWO Cameras

- **Items:** ZWO ASI Pro Cooled and Uncooled camera series.
- **Vendor File:** `apts/opticalequipment/camera/vendors/zwo.py`
- **Initial State:**
    - Contained non-existent 'ghost' mono models based on color-only sensors (ASI071MM, ASI094MM, ASI128MM, ASI2400MM, ASI482MM, ASI485MM, ASI664MM, ASI676MM, ASI715MM).
    - Contained redundant 'V2' entries for several models.
    - Masses for cooled Pro cameras were inconsistent (720g vs 700g, 1010g vs 700g).
    - Masses for uncooled cameras were inaccurate (e.g., 340g-400g instead of ~126g).
    - Peak QE values were sometimes missing or incorrect for color vs mono variants.
- **Verified Specs (Source: ZWO Official Manuals / Website):**
    - **ASI2600/6200 Pro:** Mass 700g (0.7kg). Peak QE: 80% (MC), 91% (MM).
    - **ASI533/585 Pro:** Mass 470g (0.47kg).
    - **ASI183/294 Pro:** Mass 410g (0.41kg).
    - **Uncooled models (ASI533, ASI294, ASI183, ASI585, ASI662, ASI462):** Mass ~120g-129g.
    - **ASI2600 Air:** Mass 760g (0.76kg).
    - **Peak QE:** Standardized to 80% for modern OSC (IMX571, IMX455, IMX533) and 91% for Mono counterparts. Starvis 2 color sensors (IMX585, IMX662) verified at 91%.
- **Action:** Removed ghost mono models and redundant V2 entries. Updated specifications (mass, QE, sensor dimensions) for core models based on official manuals. Cleaned up factory methods. Updated `tests/unit/test_stellar_improvements_v3.py` to match verified 700g mass for Pro cameras.
- **Source URLs:**
    - https://www.zwoastro.com/product/new-asi2600mm-mc-pro/
    - https://www.zwoastro.com/product/asi6200/
    - https://www.zwoastro.com/product/asi585mc-mm-pro/
    - https://www.zwoastro.com/product/asi533mc-mm-pro/
    - https://www.zwoastro.com/product/asi294/
    - https://www.zwoastro.com/product/asi183/
    - https://www.zwoastro.com/product/asi2600mc-air/
