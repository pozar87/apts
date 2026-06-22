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
