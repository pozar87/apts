import numpy

from ...optics.calculations import (
    calculate_camera_field_of_view,
    calculate_dynamic_range,
    calculate_pixel_size,
)
from ..base.calculations import normalize_intermediate_database_entry


def normalize_smart_telescope_database_entry(entry: dict) -> dict:
    """
    Normalizes a smart telescope database entry by creating a copy,
    delegating intermediate optical equipment normalization,
    and ensuring smart telescope specific default fields.
    """
    entry = normalize_intermediate_database_entry(entry)
    entry.setdefault("brand", "Unknown")
    entry.setdefault("name", "Unknown")
    entry.setdefault("mass", 0)
    return entry


def calculate_smart_telescope_pixel_size(
    sensor_width_mm: float,
    sensor_height_mm: float,
    width: int,
    height: int,
    pixel_size_um: float | None = None,
) -> float:
    """
    Calculates pixel size in micrometers.
    """
    return calculate_pixel_size(
        pixel_size_um=pixel_size_um,
        sensor_width_mm=sensor_width_mm,
        sensor_height_mm=sensor_height_mm,
        width=width,
        height=height,
    )


def calculate_smart_telescope_dynamic_range(
    full_well: float | None,
    read_noise: float | None,
) -> float | None:
    """
    Calculates the sensor's dynamic range in stops.
    Formula: DR = log2(Full Well Capacity / Read Noise)
    """
    return calculate_dynamic_range(full_well, read_noise)


def calculate_smart_telescope_fov_width(
    focal_length_mm: float,
    sensor_width_mm: float,
    barlow_magnification: float = 1.0,
) -> float:
    """
    Calculates horizontal field of view in degrees using the accurate arctan formula.
    """
    f = focal_length_mm * barlow_magnification
    return calculate_camera_field_of_view(sensor_width_mm, f)


def calculate_smart_telescope_fov_height(
    focal_length_mm: float,
    sensor_height_mm: float,
    barlow_magnification: float = 1.0,
) -> float:
    """
    Calculates vertical field of view in degrees using the accurate arctan formula.
    """
    f = focal_length_mm * barlow_magnification
    return calculate_camera_field_of_view(sensor_height_mm, f)


def calculate_smart_telescope_fov_diagonal(
    focal_length_mm: float,
    sensor_width_mm: float,
    sensor_height_mm: float,
    barlow_magnification: float = 1.0,
) -> float:
    """
    Calculates diagonal field of view in degrees using the accurate arctan formula.
    """
    f = focal_length_mm * barlow_magnification
    d = float(numpy.sqrt(sensor_width_mm**2 + sensor_height_mm**2))
    return calculate_camera_field_of_view(d, f)
