# Bolt Performance Journal ⚡

## Event Calculation Benchmarks (30-day range)

Initial benchmarking of all astronomical event calculations identified the following slowest components:

| Event Type | Initial Duration (s) | Optimized Duration (s) | Speedup |
| :--- | :--- | :--- | :--- |
| **Lunar Planetary Occultations** | 3.02s | 0.26s | ~11.6x |
| **Culminations** | 3.32s | 0.20s | ~16.6x |
| **NASA Comets** | 1.73s (Failed) | 0.25s | - |
| **Jovian Mutual Events** | 2.51s | - | - |
| **Jovian Moon Events** | 2.21s | - | - |
| **Conjunctions** | 1.05s | - | - |

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
