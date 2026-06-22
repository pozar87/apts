from typing import Optional, TYPE_CHECKING
from ...units import get_unit_registry

if TYPE_CHECKING:
    from pint import Quantity

from ..calculations import atmospheric as optics_utils
from ..utils import OpticsUtils


class AtmosphericMixIn:
    if TYPE_CHECKING:
        def pixel_scale(self) -> Optional["Quantity"]: ...

    def airmass(self, altitude_degrees: float) -> float:
        """
        Calculates the relative airmass for a given altitude in degrees.
        """
        return float(OpticsUtils.calculate_airmass(altitude_degrees))

    def atmospheric_extinction(
        self, magnitude: float, altitude_degrees: float, extinction_k: float = 0.2
    ) -> float:
        """
        Calculates the apparent magnitude of an object accounting for atmospheric extinction.
        Formula: m_apparent = m_zero + k * X
        Where k is the extinction coefficient and X is the airmass.
        k typically ranges from 0.15 (very clear) to 0.5+ (hazy/polluted). Default 0.2.
        """
        airmass_val = self.airmass(altitude_degrees)
        return float(
            optics_utils.calculate_atmospheric_extinction(
                magnitude, airmass_val, extinction_k
            )
        )

    def atmospheric_dispersion(
        self, altitude_degrees: float, lambda1_nm: float = 400, lambda2_nm: float = 700
    ) -> "Quantity":
        """
        Calculates the atmospheric dispersion (angular separation) between two wavelengths
        at a given altitude using the Peck and Reeder (1972) refractive index formula.
        Formula: (n-1) * 10^6 = 64.328 + 29498.1 / (146 - lambda^-2) + 255.4 / (41 - lambda^-2)
        Dispersion Delta R = (n1 - n2) * tan(zenith_distance)
        Source: Peck & Reeder (1972), "Refractive Index of Air in the Near Infrared"
        """
        dispersion_arcsec = optics_utils.calculate_atmospheric_dispersion(
            altitude_degrees, lambda1_nm, lambda2_nm
        )
        return float(dispersion_arcsec) * get_unit_registry().arcsecond

    def atmospheric_dispersion_in_pixels(
        self, altitude_degrees: float, lambda1_nm: float = 400, lambda2_nm: float = 700
    ) -> Optional[float]:
        """
        Calculates the atmospheric dispersion in pixels for the current optical path.
        Useful for planetary imaging to determine if an Atmospheric Dispersion Corrector (ADC) is needed.
        """
        dispersion = self.atmospheric_dispersion(
            altitude_degrees, lambda1_nm, lambda2_nm
        )
        scale = self.pixel_scale()
        if scale is None or scale.magnitude == 0:
            return None
        return float(
            dispersion.to("arcsecond").magnitude / scale.to("arcsecond").magnitude
        )
