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
