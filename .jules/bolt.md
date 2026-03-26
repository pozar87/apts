## 2025-05-22 - [Class-level Caching for Large Static Resources]
**Learning:** Loading large static resources (like the 14400x5600 light pollution map) in every class instantiation is a major performance bottleneck. Using class-level attributes for lazy-loading such resources dramatically improves performance for repeated operations.
**Action:** Always check if classes loading external data files (images, databases, etc.) can benefit from class-level or module-level caching, especially if the data is static.
