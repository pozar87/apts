from typing import Any, cast

from skyfield import almanac

from ..utils.planetary import get_skyfield_obj


def calculate_object_altitude(observer: Any, object_or_name: Any, target_time: Any) -> float:
    """
    Calculates the topocentric apparent altitude of a celestial object in degrees.
    Supports both Skyfield objects and string names (e.g., 'Jupiter').
    Uses high-precision refraction settings (10°C, 1013.25 mbar).
    """
    obj = (
        get_skyfield_obj(object_or_name)
        if isinstance(object_or_name, str)
        else object_or_name
    )
    alt, _, _ = (
        observer.at(target_time)
        .observe(obj)
        .apparent()
        .altaz(temperature_C=10.0, pressure_mbar=1013.25)
    )
    return float(alt.degrees)


def calculate_object_azimuth(observer: Any, object_or_name: Any, target_time: Any) -> float:
    """
    Calculates the topocentric apparent azimuth of a celestial object in degrees.
    Supports both Skyfield objects and string names (e.g., 'Jupiter').
    Uses high-precision refraction settings (10°C, 1013.25 mbar).
    """
    obj = (
        get_skyfield_obj(object_or_name)
        if isinstance(object_or_name, str)
        else object_or_name
    )
    _, az, _ = (
        observer.at(target_time)
        .observe(obj)
        .apparent()
        .altaz(temperature_C=10.0, pressure_mbar=1013.25)
    )
    return float(az.degrees)


def calculate_moon_phase_letter(eph: Any, date: Any) -> str:
    """
    Calculates the moon phase character code (A-Z) representing the moon phase angle.
    """
    phase_angle = almanac.moon_phase(eph, date)
    if hasattr(phase_angle, "degrees"):
        phase_angle_deg = phase_angle.degrees
    else:
        phase_angle_deg = float(phase_angle)  # type: ignore
    lunation = cast(float, phase_angle_deg) / 360.0
    letter = chr(ord("A") + int(round(lunation * 26)))
    return letter
