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
