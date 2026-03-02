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
