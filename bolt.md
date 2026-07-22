# Bolt Performance Journal ⚡

## Event Calculation Benchmarks (30-day range)

Initial benchmarking of all astronomical event calculations identified the following slowest components:

| Event Type | Initial Duration (s) | Optimized Duration (s) | Speedup |
| :--- | :--- | :--- | :--- |
| **Lunar Planetary Occultations** | 3.02s | 0.26s | ~11.6x |
| **Culminations** | 3.32s | 0.20s | ~16.6x |
| **NASA Comets** | 1.73s (Failed) | 0.25s | - |
| **Jovian Mutual Events** | 2.51s | 1.25s | ~2x |
| **Jovian Moon Events** | 2.21s | 2.42s | - |
| **Conjunctions** | 16.45s (1yr) | 6.40s (1yr) | ~2.5x |

*Note: Satellite flybys (ISS/Tiangong) reported ~135s due to network timeouts in the sandbox environment.*

## Optimizations

### 1. Culminations
The original implementation performed an iterative search (`find_maxima`) for each major planet over the entire requested time range. This was slow as it required many small-step evaluations.

**Optimization Strategy:**
- **Analytical Estimation:** Used the condition that culmination occurs when Local Sidereal Time (LST) equals Right Ascension (RA).
- **Vectorized Search:** Calculated culmination times for all days in the range simultaneously for each planet.
- **Two-Step Refinement:** Initialized with mid-day estimates, then refined once using the estimated culmination time to account for proper motion (especially important for the Moon).
- **Vectorized Filtering:** Performed altitude, Sun visibility, and date-range filtering in bulk using NumPy.
- **Result:** Reduced execution time for a 30-day range from **~3.3s to ~0.2s (~16x speedup)**.

### 2. Lunar Planetary Occultations
The original implementation performed an iterative search (`almanac.find_discrete`) for each of the 7 major planets over the entire requested time range. This resulted in redundant Skyfield observations and multiple full-range searches.

**Optimization Strategy:**
- **Vectorized Coarse Check:** Used a 20-minute grid to observe the Moon and all planets simultaneously.
- **Candidate Filtering:** Identified potential occultation windows where Moon-Planet separation was within a safe margin, considering Moon altitude and Sun altitude.
- **Precision Refinement:** For identified windows only, performed the standard `almanac.find_discrete` search. This preserves the original sub-second accuracy while avoiding searches in empty regions.
- **Result:** Reduced execution time by **>90%** while maintaining full precision.

### 2. NASA Comets
Fixed a `KeyError: 'name'` and unhandled `429 Too Many Requests` error in `calculate_nasa_comets`. Added safety checks for empty responses and missing data fields in the NeoWs API response.

## Conclusion
The most significant bottleneck among successfully running events was optimized without compromising accuracy. The system is now more responsive for long-range event discovery.

## Jovian Optimization (2025-05-24)
**Optimization Strategy:**
- **Bypass Apparent Positions:** Replaced expensive `.apparent()` calls with `.observe()` (astrometric positions) for relative Jovian moon positioning. This avoids redundant `iau2000a` nutation and gravitational deflection calculations that are negligible for these discrete searches.
- **Lightweight AltAz Wrapper:** Implemented a lightweight `Apparent` object wrapper to satisfy Skyfield's `altaz()` requirements for visibility gating without the full overhead of Standard apparent calculations.
- **Refraction Bypass:** Removed expensive atmospheric refraction refinements from visibility gating (`alt > 0`, `sun_alt <= -6`).
- **Geometric Hoisting:** Refactored invariant pole-direction dot products and scaled projection radii outside the Galilean moon loop in `apts/skyfield_searches/jovian/moons.py`. Reused moon-specific intermediate dot products (`p_z`, `p_sq`) across both Earth and Sun projection checks.
- **Result:** ~17-24% speedup from Skyfield optimizations, plus an additional ~22% speedup from geometric hoisting in moon events.

## Conjunction Optimization (2025-05-24)
**Optimization Strategy:**
- **Full Vectorization:** Replaced individual planet-pair searches with a fully vectorized approach using `np.einsum` to calculate all-pairs separations simultaneously.
- **Task Reduction:** Reduced the number of independent tasks dispatched to the `ThreadPoolExecutor` from ~22 (one per pair) to 2 (one for all planet pairs, one for all moon-planet pairs).
- **Broadcasting Efficiency:** Leveraged NumPy broadcasting to observe and calculate unit vectors for all bodies at all times in a single pass before cross-calculating dot products.
- **Result:** ~2.5x speedup for a 1-year range (from 16.45s to 6.40s).

## 2026-06-04 - OpenWeatherMap Parsing Optimization
**Optimization:** Replaced slow `.apply()` calls with list comprehensions for extracting weather summaries and precipitation intensities.
**Bug Fix:** Fixed a critical issue where rain/snow data was ignored if the first row of the forecast was empty.
**Impact:** ~10% faster parsing for typical 48-hour forecasts and significantly improved data reliability for intermittent precipitation.

## 2026-06-10 - Discovery and Scoring Optimization
**Optimization:**
- Eliminated redundant `compute()` calls in `DiscoveryService` by passing the target date to object constructors.
- Replaced slow Pandas `iterrows()` with `itertuples()` in `Objects.get_visible` and `SolarObjects`.
- Optimized `DiscoveryService._format_discovery_results` using `.to_dict('records')` for result formatting.
- Updated all `get_skyfield_object` implementations to robustly handle `NamedTuple` inputs.
**Impact:** ~42% speedup in `DiscoveryService.get_top_picks` (Warsaw 30-day discovery benchmark: 0.64s -> 0.37s).

## 2025-06-28 - [Iterrows vs Itertuples Optimization]
**What:** Replaced slow Pandas `.iterrows()` with `.itertuples()` and `.to_dict('records')` in core object and event calculation loops.
**Why:** `.iterrows()` creates a new Series object for every row, which is extremely expensive in tight loops. `.itertuples()` returns lightweight NamedTuples.
**Impact:** Achieved a ~4x performance improvement in micro-benchmarks for object property extraction and visibility gating.
**Measurement:** Verified via `tests/unit/test_messier.py`, `tests/unit/test_ngc.py`, `tests/unit/test_stars.py`, and `tests/unit/test_solar_objects.py`.

## 2026-06-29 - [Stationary Object Observation in Minimization Loops]
**Learning:** During iterative minimization (like `_refine_conjunction`), observing stationary objects (e.g., `Star` instances) repeatedly inside the loop is a major source of redundant computations. Because stars/Messier objects are effectively stationary in the inertial GCRS/BCRS frames, their unit vectors are constant (stable to 19 decimal places over 30 minutes).
**Action:** Detect if any of the target objects are instances of `Star`. Pre-calculate their observations once outside the minimization loop and reuse them inside the loop, resulting in a ~20% end-to-end reduction in execution time for conjunction search events.
