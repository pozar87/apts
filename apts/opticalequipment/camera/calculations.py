import numpy

from ...optics.calculations import calculate_camera_field_of_view
from ...units import get_unit_registry
from ...utils import map_conn, map_gender


def normalize_camera_database_entry(entry: dict) -> dict:
    """
    Normalizes a camera database entry by filling in missing sensor dimensions
    using fallback heuristics and mapping input connection formats.
    """
    entry = entry.copy()
    name = entry.get("name", "")

    sw, sh = (entry.get("sensor_width_mm"), entry.get("sensor_height_mm"))
    w, h = (entry.get("width"), entry.get("height"))

    if sw is None or sh is None or w is None or h is None:
        name_lower = name.lower()
        sw_h, sh_h = (23.5, 15.7)
        w_h, h_h = (6000, 4000)
        if "full frame" in name_lower or "36x24" in name_lower:
            sw_h, sh_h = (35.9, 23.9)
            w_h, h_h = (8256, 5504)
        elif "4/3" in name_lower or "micro four thirds" in name_lower:
            sw_h, sh_h = (17.3, 13.0)
            w_h, h_h = (4656, 3520)

        entry["sensor_width_mm"] = sw if sw is not None else sw_h
        entry["sensor_height_mm"] = sh if sh is not None else sh_h
        entry["width"] = w if w is not None else w_h
        entry["height"] = h if h is not None else h_h

    inputs = entry.get("inputs")
    if inputs is None:
        tt = map_conn(entry.get("tside_thread"))
        tg = map_gender(entry.get("tside_gender"))
        entry["inputs"] = [(tt, tg)] if tt else []
    else:
        entry["inputs"] = [
            (map_conn(c), map_gender(g)) if isinstance(c, str) else (c, g)
            for c, g in inputs
        ]

    return entry


def calculate_sensor_diagonal(sensor_width: float, sensor_height: float) -> float:
    """
    Calculates the sensor diagonal length from width and height.
    """
    return float(numpy.sqrt(sensor_width**2 + sensor_height**2))


def calculate_camera_fov_width(
    sensor_width_mm: float,
    focal_length_mm: float,
    barlow_magnification: float = 1.0,
):
    """
    Calculates horizontal field of view in degrees.
    """
    ureg = get_unit_registry()
    f_eff_mm = focal_length_mm * barlow_magnification
    fov_deg = calculate_camera_field_of_view(sensor_width_mm, f_eff_mm)
    return fov_deg * ureg.deg


def calculate_camera_fov_height(
    sensor_height_mm: float,
    focal_length_mm: float,
    barlow_magnification: float = 1.0,
):
    """
    Calculates vertical field of view in degrees.
    """
    ureg = get_unit_registry()
    f_eff_mm = focal_length_mm * barlow_magnification
    fov_deg = calculate_camera_field_of_view(sensor_height_mm, f_eff_mm)
    return fov_deg * ureg.deg


def calculate_camera_fov_diagonal(
    sensor_width_mm: float,
    sensor_height_mm: float,
    focal_length_mm: float,
    barlow_magnification: float = 1.0,
):
    """
    Calculates diagonal field of view in degrees.
    """
    ureg = get_unit_registry()
    d_mm = calculate_sensor_diagonal(sensor_width_mm, sensor_height_mm)
    f_eff_mm = focal_length_mm * barlow_magnification
    fov_deg = calculate_camera_field_of_view(d_mm, f_eff_mm)
    return fov_deg * ureg.deg
