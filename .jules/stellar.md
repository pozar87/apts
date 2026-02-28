# Stellar's Journal

## Tasks
- Added `atmospheric_dispersion` calculation to `OpticalPath` in `apts/optics.py`.
- Implemented Peck and Reeder (1972) refractive index formula for high accuracy.
- Verified calculation with unit tests: ~1.437" at 45° and ~2.489" at 30° altitude (400nm to 700nm).

## Learnings
- Atmospheric dispersion is a critical factor for high-resolution planetary imaging.
- The formula $\Delta R = (n_1 - n_2) \tan z$ provides a solid first-order approximation for dispersion.
- Peck and Reeder (1972) is the preferred standard for refractive index in the visible and near-IR.
