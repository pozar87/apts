from typing import Any
import numpy as np


def calculate_exit_pupil(aperture: Any, zoom: Any) -> Any:
    """
    Calculates the exit pupil of an optical system.
    Formula: EP = aperture / zoom
    """
    from ...units import get_unit_registry
    ureg = get_unit_registry()
    # Default unit for exit pupil if telescope aperture is problematic
    default_mm_unit = ureg.mm

    # Validate aperture
    if (
        aperture is None
        or not hasattr(aperture, "units")
        or not hasattr(aperture, "magnitude")
        or np.isnan(float(aperture.magnitude))
    ):
        return np.nan * default_mm_unit  # Aperture is invalid

    aperture_units = aperture.units

    # Validate zoom
    zoom_magnitude = getattr(zoom, "magnitude", np.nan)
    if (
        not hasattr(zoom, "units")
        or np.isnan(float(zoom_magnitude))
        or zoom_magnitude == 0
    ):
        return np.nan * aperture_units

    try:
        result = aperture / zoom
        # Ensure result has the same dimensionality as aperture (length)
        if result.dimensionality != aperture.dimensionality:
            return np.nan * aperture_units
        return result
    except Exception:
        return np.nan * aperture_units


def calculate_brightness(exit_pupil: Any) -> Any:
    """
    Calculates the relative brightness of an optical system compared to the human eye.
    Formula: B = (exit_pupil / 7mm)^2 * 100
    """
    from ...units import get_unit_registry
    ureg = get_unit_registry()

    # After calling exit_pupil, ep_val should always be a Quantity.
    # Check if its magnitude is NaN (this means exit_pupil determined a NaN result).
    ep_magnitude = getattr(exit_pupil, "magnitude", np.nan)
    if not hasattr(exit_pupil, "units") or np.isnan(float(ep_magnitude)):
        return np.nan * ureg.dimensionless

    try:
        # ep_val should have length units (e.g., mm, inch) from robust exit_pupil.
        ep_mm = exit_pupil.to(ureg.mm)
    except Exception:
        return np.nan * ureg.dimensionless

    # Check if ep_mm.magnitude became NaN after conversion or if units are missing
    ep_mm_magnitude = getattr(ep_mm, "magnitude", np.nan)
    if not hasattr(ep_mm, "units") or np.isnan(float(ep_mm_magnitude)):
        return np.nan * ureg.dimensionless

    seven_mm = 7 * ureg.mm

    # Avoid division by zero if seven_mm is somehow misconfigured
    seven_mm_magnitude = getattr(seven_mm, "magnitude", 0)
    if seven_mm_magnitude == 0:
        return np.nan * ureg.dimensionless

    ratio = (
        ep_mm / seven_mm
    )

    # Check if ratio.magnitude is NaN or if units are unexpectedly missing
    ratio_magnitude = getattr(ratio, "magnitude", np.nan)
    if not hasattr(ratio, "units") or np.isnan(float(ratio_magnitude)):
        return np.nan * ureg.dimensionless

    return (ratio**2) * 100 * ureg.dimensionless
