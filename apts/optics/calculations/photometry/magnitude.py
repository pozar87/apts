import numpy as np
from typing import Optional, Callable


def calculate_limiting_magnitude_simple(
    aperture_cm: float, sqm: float, integration_time: float
) -> float:
    """
    Calculates a simplified limiting magnitude for a setup.

    :param aperture_cm: Telescope aperture in centimeters.
    :param sqm: Sky Quality Meter reading in mag/arcsec^2.
    :param integration_time: Total integration time in seconds.
    :return: Limiting magnitude.
    """
    # Base limiting magnitude for 1 second at SQM 21
    base = 7.7 + 5 * np.log10(aperture_cm)
    # Add integration time factor: 1.25 * log10(T)
    time_factor = 1.25 * np.log10(integration_time)
    # SQM factor: (SQM - 21)
    sqm_factor = sqm - 21.0

    return float(base + time_factor + sqm_factor)


def calculate_camera_limiting_magnitude(
    snr_calculator_callable: Callable[[float], Optional[float]],
    target_snr: float = 5.0,
) -> Optional[float]:
    """
    Calculates the limiting magnitude for a camera based on reaching a target SNR.
    Uses binary search to find the magnitude where SNR equals target_snr.
    Search range: 0.0 to 30.0 magnitude. Convergence: 0.01 magnitude.

    :param snr_calculator_callable: A callable (typically a lambda or function)
                                    that takes magnitude (float) and returns
                                    the SNR (float or None).
    :param target_snr: Target Signal-to-Noise Ratio (default 5.0).
    :return: Limiting magnitude as float, or None if calculation fails.
    """
    low = 0.0
    high = 30.0

    for _ in range(12):  # 2^12 = 4096, plenty for 0.01 prec in 30 range
        mid = (low + high) / 2
        current_snr = snr_calculator_callable(mid)
        if current_snr is None:
            return None
        if current_snr > target_snr:
            low = mid
        else:
            high = mid

    return round(float(low), 2)
