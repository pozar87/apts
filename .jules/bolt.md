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
