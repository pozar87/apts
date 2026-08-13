import numpy as np
from typing import Optional

def calculate_pixel_size(
    pixel_size_um: Optional[float],
    sensor_width_mm: float,
    sensor_height_mm: float,
    width: int,
    height: int,
) -> float:
    """
    Calculates the pixel size in micrometers.
    If an explicit pixel_size_um is provided, it is returned.
    Otherwise, it is calculated from the sensor's physical dimensions and resolution.
    """
    if pixel_size_um is not None:
        return float(pixel_size_um)

    if width <= 0 or height <= 0:
        return 0.0

    size_mm = np.sqrt(sensor_width_mm**2 + sensor_height_mm**2) / np.sqrt(width**2 + height**2)
    return float(size_mm * 1000.0)


def calculate_dynamic_range(
    full_well: Optional[float],
    read_noise: Optional[float],
) -> Optional[float]:
    """
    Calculates the sensor's dynamic range in stops.
    Formula: DR = log2(Full Well Capacity / Read Noise)
    """
    if full_well is None or read_noise is None or read_noise <= 0:
        return None
    return float(np.log2(full_well / read_noise))


def calculate_camera_field_of_view(
    sensor_dimension_mm: float,
    focal_length_eff_mm: float,
) -> float:
    """
    Calculates the field of view in degrees for a given sensor dimension
    and effective focal length using the accurate arctan formula.
    """
    if focal_length_eff_mm <= 0:
        return 0.0
    return float(2.0 * np.degrees(np.arctan(sensor_dimension_mm / (2.0 * focal_length_eff_mm))))
