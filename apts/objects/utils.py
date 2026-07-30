from ..utils.astronomy.refraction import calculate_refraction
from ..utils.astronomy.calculations import (
    vectorized_geometric_compute,
    vectorized_geometric_imaging_duration,
)

# Keep the original exports for backward compatibility
__all__ = [
    "calculate_refraction",
    "vectorized_geometric_compute",
    "vectorized_geometric_imaging_duration",
]
