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
