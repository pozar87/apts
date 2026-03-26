# 🔍 Optic's Journal - Sky-Watcher Audit

## Audit Date: 2025-05-22

### Vendor: Sky-Watcher

### Models Audited:
- **Explorer 150PDS / 200PDS / 250PDS**
- **Explorer 130P / 150P / 200P / 250P / 300P**
- **Heritage 100P / 130P / 150P**
- **Star Adventurer GTi 80ED**

### Findings & Corrections:

1.  **Aperture Correction (250mm vs 254mm):**
    - The `250PDS Newtonian` was listed with a rounded `250mm` aperture.
    - Official technical specs for the 10-inch Sky-Watcher Newtonians (BK250P / Explorer 250P) confirm a primary mirror diameter of **254mm**.
    - **Action:** Updated `Sky_Watcher_250PDS_Newtonian` aperture to `254mm`.

2.  **Mass Precision (Explorer 250P):**
    - `Explorer 250P` mass was listed as a rounded `14000g`.
    - Official documentation lists the OTA weight as **14.38kg**.
    - **Action:** Updated `Sky_Watcher_Explorer_250P` mass to `14380g` to match the high-precision entry for 250PDS.

3.  **Mass Recalibration (Heritage 150P):**
    - `Heritage 150P` and `Heritage 150P FlexTube` were listed with a mass of `7500g`.
    - This value included the tabletop Dobsonian base. Other portable models in the database use OTA-only weight (e.g., Heritage 130P at 3250g).
    - Technical specs list the 150P OTA weight as approximately **3.7kg**.
    - **Action:** Updated `Sky_Watcher_Heritage_150P` and `Sky_Watcher_Heritage_150P_FlexTube` mass to `3700g`.

4.  **Missing Data Recovery (Star Adventurer GTi 80ED):**
    - This model was missing `aperture_mm`, `focal_length_mm`, and `central_obstruction_mm`.
    - It is a known 80mm f/7.5 ED doublet refractor (same optics as Evostar 80ED).
    - **Action:** Added `aperture_mm: 80`, `focal_length_mm: 600`, and `central_obstruction_mm: 0`. Updated type to `type_refractor`.

### Verification:
- Added unit tests for all modified models in `tests/unit/test_sky_watcher_specs.py`.
- Verified that all 27 Sky-Watcher spec tests pass.
- Cross-referenced with Sky-Watcher Global and First Light Optics (FLO) technical data sheets.
