import math
from typing import Optional


def calculate_airy_disk_diameter(
    focal_ratio: float, wavelength_nm: float = 550
) -> float:
    """
    Calculates the physical diameter of the Airy disk (first dark ring) in micrometers.
    Formula: D = 2.44 * lambda * f/D
    Where lambda is the wavelength and f/D is the effective focal ratio.
    This represents the diffraction-limited spot size on the focal plane.
    """
    # wavelength in nm -> micron
    lambda_um = wavelength_nm / 1000.0
    diameter = 2.44 * lambda_um * focal_ratio
    return float(diameter)


def calculate_critical_focus_zone(
    focal_ratio: float, wavelength_nm: float = 550
) -> float:
    """
    Calculates the Critical Focus Zone (CFZ) in micrometers.
    Formula: CFZ = 2.44 * (wavelength_nm / 1000) * focal_ratio^2
    """
    return 2.44 * (wavelength_nm / 1000.0) * (focal_ratio**2)


def calculate_nyquist_focal_ratio(
    pixel_pitch_um: float, wavelength_nm: float = 550, sampling_factor: float = 3.0
) -> float:
    """
    Calculates the ideal focal ratio for a given wavelength, pixel size, and sampling factor.
    Formula: f/D = (pixel_pitch_um * sampling_factor) / (1.22 * (wavelength_nm / 1000))
    """
    lambda_um = wavelength_nm / 1000.0
    return (pixel_pitch_um * sampling_factor) / (1.22 * lambda_um)


def calculate_psf_peak_fraction(
    pixel_scale_arcsec: float, seeing_arcsec: float
) -> float:
    """
    Calculates the fraction of light from a point source that falls into the central pixel.
    Formula: fraction = erf((pixel_scale_arcsec * sqrt(ln(2))) / seeing_arcsec)^2
    """
    if seeing_arcsec <= 0:
        return 0.0
    arg = (pixel_scale_arcsec * math.sqrt(math.log(2))) / seeing_arcsec
    fraction = math.erf(arg) ** 2
    return float(fraction)


def calculate_sampling(
    seeing_arcsec: float,
    rayleigh_limit_arcsec: Optional[float],
    pixel_scale_arcsec: float,
) -> Optional[str]:
    """
    Calculates the sampling status based on the resolution limit and the pixel scale.
    """
    if pixel_scale_arcsec == 0:
        return None

    # Effective resolution limit is the larger of seeing and diffraction limit
    r_limit = seeing_arcsec
    if rayleigh_limit_arcsec is not None:
        r_limit = max(seeing_arcsec, rayleigh_limit_arcsec)

    ratio = r_limit / pixel_scale_arcsec
    if ratio < 1.0:
        return "Under-sampled"
    elif ratio <= 3.0:
        return "Well-sampled"
    else:
        return "Over-sampled"


def calculate_ideal_planetary_focal_ratio(
    pixel_pitch_um: float, k: float = 5.0
) -> float:
    """
    Calculates the ideal focal ratio for planetary imaging based on the pixel size.
    """
    return k * pixel_pitch_um
