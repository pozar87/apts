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
