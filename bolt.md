# Bolt Performance Journal ⚡

## Event Calculation Benchmarks (30-day range)

Initial benchmarking of all astronomical event calculations identified the following slowest components:

| Event Type | Initial Duration (s) | Optimized Duration (s) | Speedup |
| :--- | :--- | :--- | :--- |
| **Lunar Planetary Occultations** | 3.02s | 0.26s | ~11.6x |
| **Culminations** | 2.54s | - | - |
| **Jovian Mutual Events** | 2.51s | - | - |
| **Jovian Moon Events** | 2.21s | - | - |
| **NASA Comets** | 1.73s (Failed) | 0.25s | - |
| **Conjunctions** | 1.05s | - | - |

*Note: Satellite flybys (ISS/Tiangong) reported ~135s due to network timeouts in the sandbox environment.*

## Optimizations

### 1. Lunar Planetary Occultations
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
