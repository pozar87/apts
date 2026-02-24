## 2025-01-30 - [Astronomical Computation Bottleneck]
**Learning:** Iterative astronomical solvers (like Skyfield's find_discrete) are exceptionally slow when applied to Keplerian orbits evaluated in Python (e.g., minor planets). Vectorizing these calculations using a geometric approximation provides a massive speedup (5x in this case) with acceptable accuracy trade-offs for visualization. Additionally, redundant instantiation of complex objects (like Place, which involves timezone lookups) adds unnecessary overhead that can be bypassed using lightweight surrogates.
**Action:** Always prefer vectorized geometric approximations for non-critical astronomical visualizations. Use SimpleNamespace or similar to mock heavy objects in performance-critical loops when only a few properties are needed.

## 2025-02-02 - [Star Visibility Vectorization]
**Learning:** Checking visibility for thousands of stars across multiple time points is a major bottleneck when using rigorous coordinate transformations. For coarse filtering (like candidate identification), using vectorized geometric formulas (NumPy broadcasting) provides a massive speedup (~7x) with acceptable accuracy loss (~0.5 deg).
**Action:** Use NumPy broadcasting and geometric approximations for large-scale astronomical visibility checks. Always check if required columns like 'skyfield_object' exist before vectorized access.
## 2026-02-24 - [Pint Quantity Series Optimization]
**Learning:** Creating a Series of Pint Quantities using `s.apply(lambda x: x * ureg.unit)` is extremely slow compared to `list(s.values * ureg.unit)`. The latter utilizes NumPy vectorization within Pint and then converts the resulting array-backed Quantity into a list of individual Quantities, providing a ~7x speedup for large Series (~14k items).
**Action:** Always use `list(values * unit)` pattern when initializing columns with Pint units in large astronomical catalogs.
