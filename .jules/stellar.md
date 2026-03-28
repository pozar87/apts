# Stellar's Journal

## Tasks
- Added `atmospheric_dispersion` calculation to `OpticalPath` in `apts/optics.py`.
- Implemented Peck and Reeder (1972) refractive index formula for high accuracy.
- Verified calculation with unit tests: ~1.437" at 45° and ~2.489" at 30° altitude (400nm to 700nm).
- Conducted data audit and updated ZWO planetary camera specifications in `apts/opticalequipment/camera/vendors/zwo.py`.
- Targeted ASI462, ASI585, and ASI678 series (MC/MM and V2 variants) for high-accuracy sensor data.
- Refactored `ZWO_ASI585MC` factory method to use `from_database` for improved maintainability.

## Learnings
- Atmospheric dispersion is a critical factor for high-resolution planetary imaging.
- The formula $\Delta R = (n_1 - n_2) \tan z$ provides a solid first-order approximation for dispersion.
- Peck and Reeder (1972) is the preferred standard for refractive index in the visible and near-IR.
- ZWO uses consistent mounting patterns across their uncooled camera lines (e.g., 6.5mm optical length with M42 thread).
- IMX585 and IMX678 sensors significantly increase full well capacity over previous generation planetary sensors.

## 2024-05-23 - Adding popular missing equipment

### Observe
- The ZWO ASI432MM is a popular camera for solar and lunar imaging due to its large 9µm pixels and global shutter, but it's missing from `apts/opticalequipment/camera/vendors/zwo.py`.
- The Sky-Watcher Evolux series (62ED, 82ED) are popular modern refractors missing from `apts/opticalequipment/telescope/vendors/sky_watcher.py`.

### Target
- Priority 2: Add missing popular camera and telescopes to the internal database.
- Choosing to add ASI432MM and the Evolux series.

### Calibrate
- ASI432MM specs: 1608x1104, 9.0µm pixels, 14.5x9.9mm sensor, 97ke- full well, 79% QE, 2.4e- read noise, 126g mass.
- Evolux 62ED specs: 62mm aperture, 400mm focal length, 2.5kg mass.
- Evolux 82ED specs: 82mm aperture, 530mm focal length, 2.92kg (OTA) mass.

### Develop
- I added these entries to the respective `_DATABASE` dictionaries and added factory methods.
- Verified with unit tests that they can be instantiated and their properties are correct.

## 2025-05-15 - Data audit for Player One Poseidon series

### Observe
- The Player One Poseidon-C Pro and Poseidon-M Pro entries in `apts/opticalequipment/camera/vendors/player_one.py` were missing detailed sensor specifications, limiting the utility of FoV and SNR calculations.
- Backfocus (optical length) was incorrectly set to 6.5mm instead of the standard 17.5mm for these cooled DSO cameras.

### Target
- Priority 2: Add missing specifications for popular cameras in the internal database.

### Calibrate
- Poseidon-C/M Pro specs: Sony IMX571 sensor, 6252x4176 resolution, 3.76µm pixels, 23.5x15.7mm sensor size, 71.7ke- full well, 81%/91% QE, 1.0e- read noise, 650g mass, 17.5mm backfocus.
- Citing: Manufacturer official specification manual for Poseidon series.

### Develop
- Updated `apts/opticalequipment/camera/vendors/player_one.py` with the accurate data.
- Added `tests/unit/test_player_one_specs.py` to ensure data integrity.
- Verified with `pytest`.

## 2025-05-16 - Planetary Angular Size and Projection

### Observe
- Users need to know how large a planet will appear on their sensor to choose the right focal length/Barlow.
- The library was missing physical radius data for major planets and the Moon, as well as functions to calculate apparent angular diameter.

### Target
- Priority 3: Implement a new utility function.
- Added planetary size projection in pixels for imaging setups.

### Calibrate
- Radius data source: IAU 2015 Standards (already in `apts/constants/astronomy.py`, but not fully mapped).
- Angular diameter formula: $\delta = 2 \arcsin(R/D)$ where R is radius and D is geocentric distance.
- Integrated `planetary_size_in_pixels` into `OpticalPath`.

### Develop
- Mapped `PLANET_RADII_KM` in `apts/utils/planetary.py`.
- Implemented `get_planet_angular_diameter` and `planetary_size_in_pixels`.
- Conducted data audit for ZWO ASI224MC and updated its specs in `zwo.py` to resolve heuristic inaccuracies.
- Verified with `tests/unit/test_stellar_v5.py` and regression tests.

## 2025-05-17 - Alt-Az Field Rotation Calculation

### Observe
- Smart telescopes and Alt-Az mounts are increasingly popular, but users often struggle with field rotation limits.
- The library was missing a way to predict the rotation rate and max exposure time before blur occurs.

### Target
- Priority 3: Implement a new utility function.
- Added `field_rotation_rate` and `max_exposure_alt_az` to `OpticalPath`.

### Calibrate
- Formula: $\frac{dq}{dt} = \omega_e \frac{\cos(\phi) \cos(Az)}{\cos(h)}$ where $\omega_e$ is sidereal rotation rate, $\phi$ is latitude, $Az$ is azimuth, and $h$ is altitude.
- Source: Jean Meeus, *Astronomical Algorithms*.
- Blur tolerance is calculated at the sensor's corner (half-diagonal) for the worst-case scenario.

### Develop
- Implemented in `apts/optics.py`.
- Verified with `tests/unit/test_field_rotation.py`.
- Benchmarked for Seestar S50 at 45° lat/alt: ~12.5s limit for 1px blur.

## 2025-05-18 - Apparent Magnitude for Solar System Bodies

### Observe
- Astrophotographers need to know the brightness of their targets (Sun, Moon, planets) to plan exposure times and check for potential sensor saturation.
- The library was missing a unified way to calculate apparent magnitudes for these objects.

### Target
- Priority 3: Implement a new utility function.
- Added `get_planet_magnitude` to `apts/utils/planetary.py` and exposed it via `OpticalPath.planetary_magnitude`.

### Calibrate
- **Major Planets:** Uses Skyfield's `magnitudelib`, which implements the Mallama & Hilton (2018) model.
- **The Moon:** Implements the Krisciunas & Schaefer (1991) phase-based model: $V = -12.73 + 0.026 |\alpha| + 4 \cdot 10^{-9} \alpha^4$, with a $5 \log_{10}(\Delta / 384400)$ distance correction.
- **The Sun:** Uses a standard inverse-square law: $V = -26.74 + 5 \log_{10}(d_{AU})$.
- Source: Krisciunas & Schaefer (1991), Mallama & Hilton (2018), IAU 2015 Standards.

### Develop
- Integrated into `apts/utils/planetary.py`.
- Added convenience method in `apts/optics.py`.
- Verified with `tests/unit/test_planetary_magnitude.py`.
- All 364 unit tests passed after compiling locale binary files.

## 2025-05-19 - Sensor Saturation for Point Sources

### Observe
- Astrophotographers need to know which stars will saturate their sensors and what the maximum safe exposure time is.
- The library was missing a PSF-aware saturation model for point sources.

### Target
- Priority 3: Implement new utility functions for sensor saturation.
- Added `psf_peak_fraction`, `saturation_time`, and `saturation_magnitude` to `OpticalPath`.

### Calibrate
- **PSF Model:** Assumes a Gaussian PSF. The fraction of light in the central pixel is $f = \text{erf}\left(\frac{L \sqrt{\ln 2}}{\text{FWHM}}\right)^2$ where $L$ is the pixel scale and FWHM is the seeing.
- **Saturation Time:** $t_{\text{sat}} = \frac{\text{FullWell}}{\text{Flux} \cdot f}$.
- **Saturation Magnitude:** Analytical inversion of the flux formula.
- **Data Audit:** Added missing `full_well_e` capacity for ZWO Seestar S50 (12,000e-) and S30/S30 Pro (54,000e-) based on Sony IMX462 and IMX662 datasheets.

### Develop
- Implemented in `apts/optics.py`.
- Updated `apts/opticalequipment/telescope/vendors/zwo.py` with full-well data.
- Verified with `tests/unit/test_optics_saturation.py`.
- Confirmed consistency: `saturation_magnitude(saturation_time(m)) == m`.

## 2025-05-20 - Airy Disk Diameter Calculation

### Observe
- Astrophotographers need to compare the physical size of the diffraction-limited spot (Airy disk) with their sensor's pixel size to determine if they are diffraction-limited or sensor-limited.
- The library was missing a direct way to calculate the Airy disk diameter on the focal plane.

### Target
- Priority 3: Implement a new utility function.
- Added `airy_disk_diameter` to `OpticalPath`.

### Calibrate
- Formula: $D_{Airy} = 2.44 \cdot \lambda \cdot f/D$ where $\lambda$ is wavelength and $f/D$ is the effective focal ratio.
- Source: Fundamental optics formula for circular aperture diffraction.
- Returns a `pint.Quantity` in micrometers.

### Develop
- Implemented in `apts/optics.py`.
- Verified with `tests/unit/test_airy_disk.py`.
- Example: f/10 at 550nm yields ~13.42µm.

## 2026-03-18 - Jupiter GRS Longitude and Virtuoso GTi Specs

### Observe
- The `JUPITER_GRS_LONGITUDE_SYSTEM_II` constant was outdated (66.0, from early 2025). GRS drifts ~16°/year.
- The Sky-Watcher Virtuoso GTi 150P database entry used generic types and lacked explicit optical specs.

### Target
- Priority 1: Correct an inaccuracy in a physical constant.
- Priority 2: Add/correct popular equipment specifications.

### Calibrate
- **Jupiter GRS:** Projected transit at ~12:21 UTC on March 18, 2026 (Project Pluto). Calculated CML II at this time is ~79.6°. Setting constant to 80.0.
- **Virtuoso GTi 150P:** 150mm aperture, 750mm focal length, 48mm secondary diameter (32% obstruction). Newtonian reflector design.
- Source: Project Pluto (GRS), Manufacturer official specs (Virtuoso).

### Develop
- Updated `apts/constants/astronomy.py` with the corrected GRS longitude and updated the comment.
- Updated `apts/opticalequipment/telescope/vendors/sky_watcher.py` with verified Virtuoso GTi 150P specifications.
- Verified hardware spec parsing and GRS transit predictor with unit tests.

## 2025-05-21 - Solar Physical Details and SQA55 Specs

### Observe
- Solar astrophotographers need physical orientation data (Position Angle, Heliographic Latitude, Carrington Longitude) to track sunspots and solar features.
- The popular Askar SQA55 Petzval refractor was missing from the database.
- The ZWO ASI664MC full-well specification was slightly inaccurate (36.5ke- vs 38.5ke-).

### Target
- Priority 3: Implement new solar utility functions.
- Priority 2: Add missing popular telescope and correct camera data.

### Calibrate
- **Solar Physical Details:** Uses formulas from Jean Meeus, *Astronomical Algorithms*, Chapter 29. Accuracy is ~0.01° for elements and ~0.05° for final values.
- **Askar SQA55:** 55mm aperture, 264mm focal length (f/4.8), 1.84kg mass. Petzval design.
- **ZWO ASI664MC/MM:** Corrected full-well to 38,500e- per official ZWO specs.

### Develop
- Implemented `get_sun_physical_details` in `apts/utils/planetary.py` and exposed via `OpticalPath`.
- Updated `askar.py` and `zwo.py` with verified specifications.
- Verified with `tests/unit/test_solar_physical.py` (Meeus Example 29.a benchmark) and `tests/unit/test_stellar_v7.py`.

## 2025-05-22 - Jupiter System I CML and SV550 Specs

### Observe
- Jupiter has three systems of longitude. The library previously only supported System II (temperate regions/GRS). System I is needed for equatorial features.
- The SVBony SV550 122ED and SV550 60 are popular modern triplet refractors missing from the database.

### Target
- Priority 3: Implement a new utility function (Jupiter System I CML).
- Priority 2: Add missing popular telescopes to the internal database.

### Calibrate
- **Jupiter CML:** Uses PyEphem's `cmlI` and `cmlII` attributes. Calculations include light-travel time correction (evaluating Jupiter's rotation state at the moment light left the planet).
- **SVBony SV550 122ED:** 122mm aperture, 854mm focal length (f/7), 6440g mass.
- **SVBony SV550 60:** 60mm aperture, 300mm focal length (f/5), 2030g mass.
- Source: Manufacturer official specs (SVBony), PyEphem documentation.

### Develop
- Refactored `get_jupiter_system_ii_longitude` in `apts/utils/planetary.py` into a unified `get_jupiter_cml` function and added System I support.
- Exposed `jupiter_cml` via the `OpticalPath` class in `apts/optics.py`.
- Updated `apts/opticalequipment/telescope/vendors/svbony.py` with the new models.
- Verified with `tests/unit/test_jupiter_cml.py` and `tests/unit/test_svbony_122_specs.py`.

## 2025-05-23 - High-accuracy planetary geometry and phase

### Observe
- Astrophotographers need accurate planetary dimensions for framing, especially for highly oblate planets like Jupiter and Saturn.
- The library was missing polar radius data and the ability to calculate the apparent polar diameter, which varies with the planet's tilt relative to Earth.
- Users also needed a simple way to get the planetary phase as a percentage for targets like Venus.

### Target
- Priority 1: Correct an inaccuracy (or omission) in astronomical formulas and data.
- Improving planetary angular size calculations to account for oblateness and orientation.

### Calibrate
- **Polar Radii:** Added IAU 2015 standard values for Earth, Mars, Jupiter, Saturn, Uranus, and Neptune.
- **Physical Orientation:** Implemented `get_sub_observer_latitude` using the IAU 2015 pole models to calculate the tilt ($D_E$).
- **Apparent Polar Diameter:** Implemented the formula $d_p = d_{eq} \sqrt{1 - (2f - f^2) \cos^2(D_E)}$ where $f$ is the flattening.
- **Planetary Phase:** Added a percentage-based (0-100) illuminated fraction helper.
- Source: IAU 2015 Standards, *Explanatory Supplement to the Astronomical Almanac*.

### Develop
- Updated `apts/constants/astronomy.py`, `apts/utils/planetary.py`, and `apts/optics.py`.
- Verified with `tests/unit/test_planetary_geometry.py`.
- Example: Jupiter apparent polar diameter is ~6.5% smaller than equatorial.

## 2025-05-24 - Planetary Rotation Blur Limit

### Observe
- Planetary imagers (lucky imaging) need to know how long they can record a video before the planet's rotation causes visible blur in the final stacked image.
- The library was missing constants for planetary rotation periods and a method to calculate this duration limit based on the setup's pixel scale and target planet.

### Target
- Priority 3: Implement a new utility function.
- Added `max_planetary_rotation_duration` to `OpticalPath`.

### Calibrate
- **Rotation Periods:** Added sidereal rotation periods for Mercury, Venus, Earth, Mars, Jupiter, Saturn, Uranus, Neptune, and Pluto to `apts/constants/astronomy.py`. Derived from IAU 2015 rotation rates ($W$).
- **Formula:** $t_{max} = \frac{\text{Tolerance} \cdot \text{PixelScale}}{\text{EquatorialAngularVelocity}}$, where $\omega = \frac{2\pi \cdot R_{eq}}{T_{sidereal}}$.
- The blur is most severe at the center of the planet's disk (equator).
- Source: IAU 2015 Standards, Archinal et al. (2018).

### Develop
- Updated `astronomy.py` with rotation period constants.
- Implemented `get_planet_rotation_period` in `apts/utils/planetary.py`.
- Integrated `max_planetary_rotation_duration` into `OpticalPath` in `apts/optics.py`.
- Verified with `tests/unit/test_planetary_rotation.py`.
- Benchmarks: Jupiter at 0.1"/px scale allows ~24s for 1px blur; Mars at same scale allows ~200s.

## 2025-05-25 - Data audit for Player One Ceres and Xena series

### Observe
- The Player One Ceres-C and Ceres-M entries in `apts/opticalequipment/camera/vendors/player_one.py` were using inaccurate specifications.
- Popular new models like the Xena 585M and Ceres 462M were missing from the database.
- Backfocus (optical length) for these uncooled guiding cameras was incorrectly set or inconsistent.

### Target
- Priority 2: Add missing popular cameras and correct existing equipment specifications.

### Calibrate
- **Xena 585M:** Sony IMX585 mono, 3856x2180, 2.9µm pixels, 47ke- full well, 91% QE, 0.7e- read noise, 11.2x6.3mm chip, 7.5mm backfocus, 65g mass.
- **Ceres 462M:** Sony IMX462 mono, 1944x1096, 2.9µm pixels, 12ke- full well, 91% QE, 0.7e- read noise, 5.6x3.2mm chip, 7.5mm backfocus, 65g mass.
- **Ceres-C:** Updated to verified IMX224 specs (19.4ke- full well, 80% QE, 0.74e- read noise, 7.5mm backfocus).
- **Ceres-M:** Corrected from IMX462 specs to accurate AR0130 specs (1284x964, 18ke- full well, 80% QE, 3.6e- read noise, 7.5mm backfocus).
- Source: Player One Astronomy official product pages and manuals.

### Develop
- Updated `apts/opticalequipment/camera/vendors/player_one.py` with the accurate data.
- Standardized the 7.5mm back focal length for the "Dwarf Planet" series.
- Added factory methods for the new models.
- Updated `tests/unit/test_player_one_specs.py` with the new/verified specifications.
- All 9 Player One specification tests passed.

## 2025-05-26 - Data audit for ZWO v2/Air series and Smart Telescopes

### Observe
- Many ZWO "v2" and "Pro v2" models in the database were missing critical optical specifications, relying on fallback heuristics.
- The new ZWO "Air" series (integrated controller cameras) were missing entirely.
- The Seestar S30 full-well capacity was overestimated (54ke- vs 38.2ke-).
- The Dwarf 3 was missing full-well capacity data.

### Target
- Priority 2: Add missing popular cameras and correct existing equipment specifications.
- Priority 1: Correct inaccuracies in hardware data.

### Calibrate
- **ZWO v2/Pro v2:** Completed specs for 183, 2600, 294, 533, 662, 482, 715, 678, and 585 series. Data verified via ZWO manuals and Sony datasheets.
- **ASI2600 Air:** Added MC and MM models. Specs match IMX571 sensor. Mass updated to 1050g (integrated hardware).
- **Seestar S30:** Corrected full-well to 38,200e- (Sony IMX662).
- **Dwarf 3:** Added full-well of 11,270e- (Sony IMX678).
- Source: ZWO Official Website, Sony Sensor Datasheets, DwarfLab Specs.

### Develop
- Updated  and  / .
- Verified with .
- Verified no regressions in existing optics tests.

## 2025-05-26 - Data audit for ZWO v2/Air series and Smart Telescopes

### Observe
- Many ZWO "v2" and "Pro v2" models in the database were missing critical optical specifications, relying on fallback heuristics.
- The new ZWO "Air" series (integrated controller cameras) were missing entirely.
- The Seestar S30 full-well capacity was overestimated (54ke- vs 38.2ke-).
- The Dwarf 3 was missing full-well capacity data.

### Target
- Priority 2: Add missing popular cameras and correct existing equipment specifications.
- Priority 1: Correct inaccuracies in hardware data.

### Calibrate
- **ZWO v2/Pro v2:** Completed specs for 183, 2600, 294, 533, 662, 482, 715, 678, and 585 series. Data verified via ZWO manuals and Sony datasheets.
- **ASI2600 Air:** Added MC and MM models. Specs match IMX571 sensor. Mass updated to 1050g (integrated hardware).
- **Seestar S30:** Corrected full-well to 38,200e- (Sony IMX662).
- **Dwarf 3:** Added full-well of 11,270e- (Sony IMX678).
- Source: ZWO Official Website, Sony Sensor Datasheets, DwarfLab Specs.

### Develop
- Updated `apts/opticalequipment/camera/vendors/zwo.py` and `apts/opticalequipment/telescope/vendors/zwo.py` / `dwarflab.py`.
- Verified with `tests/unit/test_stellar_audit_v2.py`.
- Verified no regressions in existing optics tests.
