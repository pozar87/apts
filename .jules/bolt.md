## 2026-07-22 - [Polar Alignment Star Tracking Optimization]
**Learning:** In star-matching and asterism tracking algorithms, comparing local configurations of stars involves high-frequency distance computations. We can achieve massive speedups by: (1) caching/hoisting distance calculations to avoid double-evaluating the same pair, (2) sorting on precomputed values to avoid sorting key lambda overhead, and (3) pre-calculating a squared distance matching limit (`max_limit_sq`) from the largest target neighbor and checking `dist_sq <= max_limit_sq` first. This fast-path pruning bypasses expensive `math.sqrt` operations for almost all stars in the frame (often >95% of candidates), while adding a robust empty-list guard prevents potential `IndexError` crashes.
**Action:** Always prefer squared distance comparisons (`dist_sq <= limit_sq`) for coarse spatial checks before invoking `math.sqrt`. Always guard list indexing when dealing with dynamic neighbor counts in astrometric algorithms.

## 2025-01-30 - [Astronomical Computation Bottleneck]
**Learning:** Iterative astronomical solvers (like Skyfield's find_discrete) are exceptionally slow when applied to Keplerian orbits evaluated in Python (e.g., minor planets). Vectorizing these calculations using a geometric approximation provides a massive speedup (5x in this case) with acceptable accuracy trade-offs for visualization. Additionally, redundant instantiation of complex objects (like Place, which involves timezone lookups) adds unnecessary overhead that can be bypassed using lightweight surrogates.
**Action:** Always prefer vectorized geometric approximations for non-critical astronomical visualizations. Use SimpleNamespace or similar to mock heavy objects in performance-critical loops when only a few properties are needed.

## 2025-02-02 - [Star Visibility Vectorization]
**Learning:** Checking visibility for thousands of stars across multiple time points is a major bottleneck when using rigorous coordinate transformations. For coarse filtering (like candidate identification), using vectorized geometric formulas (NumPy broadcasting) provides a massive speedup (~7x) with acceptable accuracy loss (~0.5 deg).
**Action:** Use NumPy broadcasting and geometric approximations for large-scale astronomical visibility checks. Always check if required columns like 'skyfield_object' exist before vectorized access.

## 2026-02-24 - [Pint Quantity Series Optimization]
**Learning:** Creating a Series of Pint Quantities using `s.apply(lambda x: x * ureg.unit)` is extremely slow compared to `list(s.values * ureg.unit)`. The latter utilizes NumPy vectorization within Pint and then converts the resulting array-backed Quantity into a list of individual Quantities, providing a ~7x speedup for large Series (~14k items).
**Action:** Always use `list(values * unit)` pattern when initializing columns with Pint units in large astronomical catalogs.

## 2026-02-26 - [Visibility Search Optimization]
**Learning:** When performing visibility checks for large catalogs across multiple time points, complexity can be significantly reduced by implementing a "maximum altitude" (culmination) pre-filter to prune objects that never rise above the horizon. Furthermore, trigonometric broadcasting over an $N \times M$ grid can be optimized from $O(N \times M)$ to $O(N + M)$ function calls by using trigonometric identities to decompose compound angles into separate object and time components.
**Action:** Implement a culmination pre-filter before dense time-based checks. Use trigonometric identities to optimize grid-based coordinate transformations.

## 2026-03-05 - [Skyfield Vectorized Observations]
**Learning:** Skyfield's performance is heavily dependent on using its vectorization capabilities. Calling `observer.at(t).observe(body)` inside a Python loop is an order of magnitude slower than passing an array of times to `observer.at(times).observe(body)`. In conjunction searches, replacing an hourly loop with a single vectorized call and NumPy-based minima finding provided a ~12x speedup.
**Action:** Always use Skyfield's vectorized `at(times)` method for any repetitive astronomical calculations.

## 2026-03-07 - [Fixed Object Broadcasting with ICRF]
**Learning:** For astronomical searches involving fixed objects (stars, DSOs) over many time points, rigorous coordinate transformations can be avoided by observing the object once (at the start of the interval) and broadcasting its ICRF position across the time array using `ICRF(pos[:, np.newaxis], t=times)`. This provides a significant speedup with sub-arcsecond accuracy loss.
**Action:** Use ICRF broadcasting for all star-related conjunction and occultation searches to eliminate redundant coordinate transformations.

## 2026-03-07 - [Ecliptic Latitude Filtering]
**Learning:** The Moon's orbit is inclined only ~5.1 degrees to the ecliptic. When searching for Moon-star occultations, filtering candidates by ecliptic latitude (e.g., within 10 degrees) can prune more than 60% of target stars before any expensive separation calculations begin.
**Action:** Always implement a geometric pre-filter (like ecliptic latitude for lunar events) before performing dense time-based separation checks.

## 2026-03-08 - [Loop Consolidation and Observer Hoisting]
**Learning:** Consolidated multiple iteration loops (e.g., `ephem` and `skyfield` calculations) in `SolarObjects.compute` into a single `iterrows()` pass, significantly reducing Pandas overhead. Additionally, hoisting the expensive Skyfield `observer.at(times)` call out of the object iteration loop in `get_visible` prevents redundant coordinate transformations across all objects in a collection.
**Action:** Always consolidate loops processing the same DataFrame and hoist expensive coordinate setup (like Skyfield observers) outside of iteration loops.

## 2026-03-09 - [Skyfield Vectorized Observation Requirements]
**Learning:** While Skyfield supports vectorization over Time objects, its `observe` method does not natively support a Python list of astronomical objects (e.g., Stars). To achieve full vectorization over multiple objects, one must initialize a single Skyfield object (like `Star`) using NumPy arrays for its coordinates (RA, Dec). This allows a single `observe` call to return a position vector for all objects at once, which is significantly faster than iterative observations.
**Action:** When vectorizing searches over multiple celestial objects, always consolidate them into a single Skyfield object with array-backed coordinates instead of passing a list of objects to the observer.

## 2026-03-10 - [Lazy Catalog Loading]
**Learning:** Eagerly loading large astronomical catalogs (Messier, NGC, Bright Stars) during package import significantly increases startup time (e.g., from ~6.4s to ~3.7s). This "import penalty" can be eliminated by implementing lazy loading via property getters, ensuring that heavy I/O and data processing only occur when a catalog is actually needed.
**Action:** Always implement lazy loading for large datasets (catalogs, ephemerides, etc.) in the library's core to ensure fast application startup and minimal memory footprint for lightweight scripts.

## 2026-03-11 - [Vectorized Skymap Plotting]
**Learning:** Plotting thousands of objects (like the 14k NGC catalog) in a zoomed view can be a major bottleneck if the filtering or observation steps use row-wise `.apply()`. Replacing string-based coordinate parsing with pre-calculated floats and using a single vectorized `observer.observe()` call on the filtered subset (supported by an array-backed `Star` object) eliminates massive Python loop overhead.
**Action:** Ensure all plotting utilities use vectorized coordinate access and bulk Skyfield observations for large catalogs. Support vectorized input in `get_skyfield_object` to facilitate this.

## 2025-03-24 - [Bulk Timezone Conversion Optimization]
**Learning:** Performing timezone conversions on individual `pd.Timestamp` objects within a list comprehension (e.g., `t.astimezone(tz)`) is significantly slower than using the vectorized `pd.Series.dt.tz_convert(tz)` method. For a dataset of 10,000 timestamps, the vectorized approach provided a ~13-15x speedup. Converting back to native Python objects using `.dt.to_pydatetime()` maintains compatibility with code expecting standard datetime objects while still benefiting from the bulk processing.
**Action:** Always use `pd.Series.dt.tz_convert()` for bulk timezone localization/conversion instead of iterative `.astimezone()` calls.

## 2025-03-25 - [Vectorized Weather Condition Evaluation]
**Learning:** Evaluating multiple weather conditions (thresholds) on large datasets using `iterrows()` is extremely slow. Replacing it with vectorized Pandas boolean masks for the initial "good/bad" pass and then using `.to_dict('records')` on the bad-hour subset for localized string generation provides a ~2.6x to ~4x speedup. Iterating over a list of dicts is significantly faster than using `.iloc` inside a Python loop for small subsets.
**Action:** Use vectorized boolean masks for bulk condition checks. If row-specific logic (like string formatting) is still needed, apply it only to filtered subsets converted to Python primitives (e.g., list of dicts).

## 2025-03-26 - [Skyfield Pairwise Vectorization]
**Learning:** Skyfield's `.observe()` method supports pairwise vectorization (N unique bodies observed at N unique times) when the length of the `Time` object matches the length of the `Star` (or other body) object. This yields a single position vector of length N, bypassing the O(N) loop of individual observations. Additionally, for meridian culminations, expensive topocentric `altaz()` calls can be replaced by the geometric approximation `90 - |lat - dec|` plus Bennett's refraction formula, which is sub-arcsecond accurate and orders of magnitude faster.
**Action:** Always use pairwise vectorization and geometric meridian shortcuts for large-scale culmination and transit searches.

## 2025-05-22 - [Class-level Caching for Large Static Resources]
**Learning:** Loading large static resources (like the 14400x5600 light pollution map) in every class instantiation is a major performance bottleneck. Using class-level attributes for lazy-loading such resources dramatically improves performance for repeated operations.
**Action:** Always check if classes loading external data files (images, databases, etc.) can benefit from class-level or module-level caching, especially if the data is static.

## 2025-05-23 - [Vectorized Weather and Planetary Calculations]
**Learning:** Vectorizing iterative calculations over Pandas DataFrames using NumPy and removing scalar-forcing casts (like `float()`) in utility functions (`get_planet_magnitude`, `get_planet_phase_angle`) provides a massive speedup (~17.8x) for astronomical and weather data processing. Replacing `iterrows()` with vectorized array operations and boolean masking (`np.where`, `np.clip`) is essential when handling large weather datasets.
**Action:** Always prefer vectorized NumPy/Pandas operations over `iterrows()` or `apply()` for numerical calculations. Ensure utility functions support both scalar and array-backed Skyfield Time objects by avoiding explicit scalar type casting on return.

## 2025-05-24 - [Bulk Translation Optimization]
**Learning:** Translating large DataFrames row-by-row using `.apply(lambda x: gettext_(x))` is a major bottleneck due to redundant function calls and Python loop overhead. Implementing an early return for the default language (e.g., 'en') and a unique-value mapping strategy (handling unhashable lists by converting to tuples) provides a massive speedup (~15x to 90x).
**Action:** Always use unique-value mapping (via `df[col].map(translation_map)`) for bulk translations. Ensure unhashable types like lists are handled by falling back to a custom unique collection or converting to tuples for set/dict operations.

## 2025-06-12 - [Moon Magnitude Consolidation]
**Learning:** Calculating Moon magnitude requires both phase angle and distance. Implementing these via separate calls to `get_planet_phase_angle` and `get_moon_distance` results in redundant Skyfield observations of the Moon. Consolidating these into a single observation and extracting both properties from the resulting astrometric object yields a ~12x speedup for large time arrays.
**Action:** When multiple physical properties (distance, phase angle, position) of the same moving body are needed for a calculation, always perform a single Skyfield observation and reuse the resulting astrometric object.

## 2025-06-15 - [Vectorized Logarithmic Surface Brightness]
**Learning:** Vectorizing calculations that involve logarithms (like surface brightness) requires careful handling of non-positive inputs to avoid `RuntimeWarning`. Using `np.log10(x, where=x>0, out=res)` followed by `np.where(x>0, ..., np.inf)` ensures vectorized performance while remaining silent and correct for invalid inputs.
**Action:** Always use the `where` and `out` parameters of NumPy ufuncs when vectorizing functions with restricted domains (log, sqrt, etc.) to prevent noisy warnings in production.

## 2025-06-20 - [Supermoon Bulk Search Optimization]
**Learning:** Iterative per-event searches for related orbital extremes (e.g., finding the nearest perigee for every Full Moon) is inefficient in Skyfield. Consolidating these into bulk maxima/minima searches over the entire padded date range, combined with NumPy-based nearest-neighbor matching, significantly reduces overhead.
**Action:** Replace iterative 'find_maxima/minima' calls inside loops with a single bulk search over the full range plus padding, and use NumPy to match events.

## 2025-06-21 - [Solar Eclipse Search Optimization]
**Learning:** Performing a direct topocentric `find_minima` search for solar eclipses over long periods is extremely inefficient. Since solar eclipses can only occur during a New Moon, a two-step approach—identifying geocentric New Moons first and then performing a narrow topocentric search (+/- 12 hours)—provides a ~20x performance gain.
**Action:** Use geocentric "event triggers" (like moon phases or conjunctions) to narrow the search window for expensive topocentric astronomical calculations. Always pad the trigger search range to ensure events shifted by parallax across boundaries are not missed.

## 2025-06-22 - [Conjunction Vectorization over Catalogs]
**Learning:** Iterative creation of `Star` objects and row-wise coordinate extraction (`.ra.hours`, `.dec.degrees`) from catalogs is a significant bottleneck in conjunction searches. Refactoring the search engine to accept pre-vectorized `Star` objects and utilizing pre-calculated float coordinate columns (e.g., `ra_hours`, `dec_degrees`) eliminates thousands of redundant Python calls, providing a ~19% speedup for Messier object searches.
**Action:** Always utilize pre-calculated float coordinate columns and vectorized `Star` object creation for large-scale astronomical searches. Ensure core search utilities support vectorized inputs to avoid redundant object instantiation.

## 2025-05-25 - [StormGlass Precipitation Vectorization]
**Learning:** Replacing row-wise `df.apply(axis=1)` with vectorized NumPy masking and `pd.to_numeric(errors='coerce')` in weather data providers eliminates significant Python loop overhead. This approach provides a ~6.7x speedup for 10,000 rows while improving robustness when handling API-specific string fallbacks like "none".
**Action:** Always replace row-wise `apply` calls with vectorized NumPy/Pandas operations in data normalization layers.

## 2025-05-24 - [Skyfield AltAz Optimization via Manual Apparent Wrapping]
**Learning:** Skyfield's `.altaz()` requires an `Apparent` object, but `.apparent()` triggers expensive Standard calculations (nutation, aberration, deflection). When accuracy requirements are loose (e.g., visibility gating), manually wrapping an `Astrometric` position in an `Apparent` object bypasses these bottlenecks.
**Action:** Use `app = Apparent(pos.position.au, pos.velocity.au_per_d, pos.t); app.center = pos.center` to perform fast AltAz checks.

## 2025-05-25 - [Conjunction Refinement Linear Propagation]
**Learning:** During iterative refinement of conjunctions over a small +/- 30-minute window, the absolute motion of moving bodies is extremely linear. We can observe the absolute position and velocity of moving bodies once at the rough conjunction time and propagate them linearly (`pos + vel * dt`) inside the refinement search loop. This avoids thousands of expensive, iterative topocentric coordinate conversions and ephemeris lookups on every step of the minimization solver, leading to a ~15-20% speedup in conjunction searches.
**Action:** Always prefer linear propagation of absolute positions and velocities over small time windows during iterative searches/refinements to bypass redundant topocentric ephemeris calculations.

## 2025-05-24 - [Event Calculation Benchmarks (30-day range)]
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

### Optimizations

#### 1. Culminations
The original implementation performed an iterative search (`find_maxima`) for each major planet over the entire requested time range. This was slow as it required many small-step evaluations.

**Optimization Strategy:**
- **Analytical Estimation:** Used the condition that culmination occurs when Local Sidereal Time (LST) equals Right Ascension (RA).
- **Vectorized Search:** Calculated culmination times for all days in the range simultaneously for each planet.
- **Two-Step Refinement:** Initialized with mid-day estimates, then refined once using the estimated culmination time to account for proper motion (especially important for the Moon).
- **Vectorized Filtering:** Performed altitude, Sun visibility, and date-range filtering in bulk using NumPy.
- **Result:** Reduced execution time for a 30-day range from **~3.3s to ~0.2s (~16x speedup)**.

#### 2. Lunar Planetary Occultations
The original implementation performed an iterative search (`almanac.find_discrete`) for each of the 7 major planets over the entire requested time range. This resulted in redundant Skyfield observations and multiple full-range searches.

**Optimization Strategy:**
- **Vectorized Coarse Check:** Used a 20-minute grid to observe the Moon and all planets simultaneously.
- **Candidate Filtering:** Identified potential occultation windows where Moon-Planet separation was within a safe margin, considering Moon altitude and Sun altitude.
- **Precision Refinement:** For identified windows only, performed the standard `almanac.find_discrete` search. This preserves the original sub-second accuracy while avoiding searches in empty regions.
- **Result:** Reduced execution time by **>90%** while maintaining full precision.

#### 2. NASA Comets
Fixed a `KeyError: 'name'` and unhandled `429 Too Many Requests` error in `calculate_nasa_comets`. Added safety checks for empty responses and missing data fields in the NeoWs API response.

### Conclusion
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


## 2025-06-25 - [Geometric Projection Hoisting]
**Learning:** In geometric searches involving multiple bodies observed from the same sources (e.g., Earth and Sun projecting onto Galilean moons), many projection parameters are invariant across the bodies. Hoisting pole-direction dot products and scaled projection radii out of the body iteration loop, and reusing intermediate dot products (`p_z`, `p_sq`) across different projection targets, significantly reduces redundant NumPy operations.
**Action:** Always identify and hoist invariant geometric parameters out of iteration loops in complex astronomical state functions.

## 2026-06-04 - [OWM Parsing Optimization and Robustness]
**Learning:** For small DataFrames typically encountered in weather API responses (~48 rows), iterating with list comprehensions over `.values` can be faster than Pandas `.apply()` due to reduced function call overhead. More importantly, relying on `df[col].iloc[0]` to check for column data presence is a bug-prone anti-pattern; it misses data if the first row is null but subsequent rows are not.
**Action:** Use list comprehensions for row-wise extraction on small datasets. Always prefer vectorized logic or full-column iteration over single-row type checks to ensure data robustness.

## 2025-06-28 - [Iterrows vs Itertuples Optimization]
**Learning:** Replacing Pandas `.iterrows()` with `.itertuples()` or `.to_dict('records')` provides a massive performance boost (~4x) in iteration-heavy logic. While `.itertuples()` is generally faster, it returns NamedTuples which do not support dictionary-style `['col']` indexing. Implementing robust attribute access via `getattr(obj, 'col', default)` in downstream consumers (like `get_skyfield_object`) is essential to avoid breaking changes when switching iteration methods.
**Action:** Always prefer `.itertuples()` or `.to_dict('records')` over `.iterrows()`. Ensure receiving methods use `getattr` or support both Series and NamedTuples.

## 2025-07-02 - [Pre-calculated Catalog Search Columns]
**Learning:** Repeatedly applying complex string normalization (regex, etc.) via `df.apply()` during catalog searches is a major bottleneck. Pre-calculating these normalized versions once during catalog load and storing them in dedicated columns allows for vectorized equality checks, yielding a massive speedup (~17x).
**Action:** Always pre-calculate and store normalized search keys for large catalogs during initialization.

## 2025-07-03 - [Fast-Path Altitude Gating]
**Learning:** When performing visibility gating on a time grid, calculating apparent coordinates (with refraction) for every point is extremely expensive ((N \times M)$). For the primary use case of a simple altitude threshold (no complex horizon or azimuth constraints), converting the threshold into the same space as pre-calculated geometric values (like ) allows for direct array comparison. This bypasses thousands of calls to , , and iterative refraction formulas.
**Action:** Always implement a fast-path for simple geometric thresholds before falling back to full coordinate transformations. Convert the threshold once (using first-order refraction approximation if needed) instead of transforming the entire data grid.

## 2025-07-03 - [Fast-Path Altitude Gating]
**Learning:** When performing visibility gating on a time grid, calculating apparent coordinates (with refraction) for every point is extremely expensive ($O(N \times M)$). For the primary use case of a simple altitude threshold (no complex horizon or azimuth constraints), converting the threshold into the same space as pre-calculated geometric values (like `sin_alt`) allows for direct array comparison. This bypasses thousands of calls to `arcsin`, `arctan2`, and iterative refraction formulas.
**Action:** Always implement a fast-path for simple geometric thresholds before falling back to full coordinate transformations. Convert the threshold once (using first-order refraction approximation if needed) instead of transforming the entire data grid.

## 2025-05-26 - [Vectorized Aurora Coordinate Search]
**Learning:** Performing a 2D nearest-neighbor search on a 64,800-point grid (1-degree resolution) using Pandas DataFrame instantiation and Series-based distance calculation is significantly slower than using raw NumPy arrays. Additionally, for a single-point global forecast, using  is extremely inefficient compared to direct scalar assignment.
**Action:** Use NumPy broadcasting and `np.argmin` for large coordinate searches. Prefer scalar assignment over complex merges when the enrichment data consists of a single value applied to all time points.

## 2025-05-26 - [Vectorized Aurora Coordinate Search]
**Learning:** Performing a 2D nearest-neighbor search on a 64,800-point grid (1-degree resolution) using Pandas DataFrame instantiation and Series-based distance calculation is significantly slower than using raw NumPy arrays. Additionally, for a single-point global forecast, using `pd.merge_asof` is extremely inefficient compared to direct scalar assignment.
**Action:** Use NumPy broadcasting and `np.argmin` for large coordinate searches. Prefer scalar assignment over complex merges when the enrichment data consists of a single value applied to all time points.

## 2025-05-27 - [Pandas Datetime Coercion and DataFrame Update Bottleneck]
**Learning:** Assigning raw Python lists of datetimes with dateutil timezones back to DataFrame columns triggers expensive, row-by-row datetime coercion and auto-timezone inference in Pandas. Wrapping the computed lists in `pd.Series` with an explicit `index` and `dtype=object` completely bypasses this inference. Furthermore, `df.update()` has massive overhead due to alignment checks; direct column assignment when computing on the full catalog bypasses this entirely.
**Action:** Always wrap lists of timezone-aware datetimes in `pd.Series(..., dtype=object, index=df.index)` before assigning to DataFrame columns. Prefer direct column assignment over `.update()` when updating the full master DataFrame.

## 2026-03-12 - [Twilight fast_altaz Transition Optimization]
**Learning:** When performing searches or transitions involving twilight or sun positions (such as finding golden and blue hours), using rigorous `.apparent().altaz()` is a major bottleneck due to expensive standard apparent coordinate conversions. Replaced with `fast_altaz` to bypass standard apparent calculations for a ~20% speedup on golden/blue hour detection loops. However, always exercise caution since weather-related and place-specific unit tests often mock nested `.apparent().altaz()` calls directly.
**Action:** Use `fast_altaz` for fast-path solar and twilight evaluations. Avoid breaking tests by checking if existing unit tests mock standard nested paths prior to refactoring weather and place mixins.

## 2026-06-05 - [Vectorized Discovery Service Geometric Scoring]
**Learning:** In the discovery service, performing high-precision Skyfield observations (with nutation, aberration, etc.) for hundreds of candidate targets is extremely slow. Since discovery scoring only requires coarse accuracy, replacing these with vectorized NumPy geometric formulas (spherical trigonometry) for altitude and moon separation provides a ~20x speedup for this phase. Additionally, pre-extracting Pint Quantity magnitudes into float arrays before iteration avoids significant overhead in FOV ratio calculations.
**Action:** Use vectorized geometric formulas for coarse astronomical calculations (like scoring) and pre-extract float values from wrapped Quantities before high-frequency loops or bulk calculations.

## 2025-05-24 - [Vectorized External Link Generation]
**Learning:** Replacing row-wise `urllib.parse.quote` list comprehensions with vectorized Pandas `.str.replace(" ", "%20", regex=False)` for simple alphanumeric columns in large DataFrames avoids significant Python loop overhead. For the ~14k row NGC catalog, this provided a ~2.1x speedup in total catalog access time.
**Action:** Always replace row-wise URL quoting with vectorized string operations when the dataset's character set is constrained and known.

## 2026-07-13 - [Observer at Times Hoisting]
**Learning:** Skyfield's topocentric observer alignment and setup via `observer.at(times)` can be a hidden bottleneck when repeatedly called inside a loop for different bodies. For instance, in multi-body configuration, alignment, or transit searches, hoisting `observer.at(times)` out of the loop and reusing the same `Time` / `Observer` reference avoids redundant coordinate transformations and time epoch calculations.
**Action:** Always hoist `observer.at(times)` calls out of search/observation loops involving multiple target objects.

## 2026-07-20 - [Vectorized Highest Altitude Analytical Solver]
**Learning:** Finding the maximum altitude of a celestial body over a long period using numerical step solvers (such as Skyfield's `find_maxima` on a dense 0.1-day grid) is extremely slow because it requires computing apparent refraction-corrected positions thousands of times. Since a planet's maximum daily altitude always occurs at its culmination, we can instead find the exact culmination times for each day in a fully vectorized operation (using the LST = RA analytical condition), and then evaluate the precise altitudes only at those culmination moments.
**Action:** Replace grid-based numerical peak solvers with vectorized analytical daily culmination solvers when finding maximum altitude over a period.

## 2026-07-21 - [Meteor Shower Radiant Altitude Vectorization]
**Learning:** Checking topocentric altitudes for hundreds of unique candidate objects (like drifted meteor shower radiants) at their respective times using standard row-wise `Star.apparent().altaz()` inside a loop creates significant overhead. Replacing this with a pairwise geometric AltAz calculation in NumPy, followed by `calculate_refraction`, achieves a massive speedup (~500x for coordinate conversion alone) with sub-degree accuracy differences.
**Action:** Prefer pairwise geometric AltAz calculations with refraction for visibility checks of multiple unique targets at multiple unique times over iterative rigorous Skyfield observations.

## 2025-08-11 - [Empty/NaN Weather Plot Midnight Annotation Bottleneck]
**Learning:** When plotting weather forecast metrics that are empty or contain only `NaN` values (which occurs when fallback columns are added or during specific unit testing scenarios), Matplotlib defaults to a fallback x-axis date limit range of 10 years (e.g., 2000-01-01 to 2010-01-01). Attempting to plot vertical line markers for every single midnight (`ax.axvline`) in a loop over this large range results in thousands of slow Matplotlib rendering calls per plot. Skipping daily midnight annotation when the range is larger than 14 days avoids this rendering loop entirely.
**Action:** Always check the span of the x-axis limits (`(dmax - dmin).days`) before executing dense daily loops such as midnight marker lines. Skip daily lines if the range exceeds 14 days, as they would clutter the plot anyway.

## 2025-08-12 - [Skyfield Solar Eclipse Separation Optimization]
**Learning:** In Skyfield-based searches for solar eclipses over a timescale, finding the local minima of separation using `find_minima` evaluates the separation function dozens of times per interval. Bypassing expensive `.apparent()` place calculations (which apply nutation, aberration, gravitational deflection, etc.) and using raw astrometric observations (`observer.at(t).observe(...)`) during this step-search/refinement phase provides a major performance boost (~18% speedup on solar eclipse search tests) with zero accuracy loss, as high-precision `.apparent()` coordinate transformations are still applied once the actual minima have been identified.
**Action:** Always bypass expensive `.apparent()` place calculations in favor of astrometric observations (`.observe()`) when iteratively searching/solving for separation minima or alignments.
