import math
from typing import TYPE_CHECKING, Any, Optional

if TYPE_CHECKING:
    from pint import Quantity

from ...constants import astronomy
from ...units import get_unit_registry
from ..calculations import resolution as optics_utils


class ResolutionMixIn:
    if TYPE_CHECKING:
        telescope: Any
        output: Any
        _cache: dict[str, Any]
        def effective_barlow(self) -> float: ...
        def rayleigh_limit(self, wavelength_nm: float | int = 550) -> Optional["Quantity"]: ...

    def pixel_scale(self) -> Optional["Quantity"]:
        if "pixel_scale" in self._cache:
            return self._cache["pixel_scale"]

        from ...opticalequipment.camera import Camera
        from ...opticalequipment.smart_telescope import SmartTelescope

        if not isinstance(self.output, (Camera, SmartTelescope)):
            self._cache["pixel_scale"] = None
            return None
        # Effective focal length
        eff_focal_length = self.telescope.focal_length * self.effective_barlow()
        # Pixel size
        p_size = self.output.pixel_size()
        # Formula: (p_size / eff_focal_length) * RAD_TO_ARCSEC
        scale = (
            p_size.to("mm").magnitude / eff_focal_length.to("mm").magnitude
        ) * astronomy.RAD_TO_ARCSEC
        res = scale * get_unit_registry().arcsecond
        self._cache["pixel_scale"] = res
        return res

    def sampling(self, seeing: float) -> Optional[str]:
        """
        Calculates the sampling status based on the resolution limit and the pixel scale.
        """
        scale = self.pixel_scale()
        if scale is None or scale.magnitude == 0:
            return None

        # Effective resolution limit is the larger of seeing and diffraction limit
        r_limit = seeing
        diffraction_limit = self.rayleigh_limit()
        if diffraction_limit is not None:
            r_limit = max(seeing, diffraction_limit.to("arcsecond").magnitude)

        ratio = r_limit / scale.magnitude
        if ratio < 1.0:
            return "Under-sampled"
        elif ratio <= 3.0:
            return "Well-sampled"
        else:
            return "Over-sampled"

    def sampling_status(self, seeing: float = 2.0) -> Optional[str]:
        """
        Returns the sampling status as a string for a given seeing in arcseconds.
        """
        return self.sampling(seeing)

    def critical_focus_zone(self, wavelength: float = 550) -> Optional["Quantity"]:
        if not hasattr(self.telescope, "focal_ratio"):
            return None
        # wavelength in nm
        fr = (self.telescope.focal_ratio() * self.effective_barlow()).magnitude
        # CFZ = 2.44 * (wavelength/1000) * fr^2
        cfz = 2.44 * (wavelength / 1000.0) * (fr**2)
        return cfz * get_unit_registry().micrometer

    def dawes_limit(self) -> Optional["Quantity"]:
        """
        Calculates the Dawes' limit (resolving power) of the telescope in arcseconds.
        """
        if "dawes_limit" not in self._cache:
            if hasattr(self.telescope, "dawes_limit"):
                self._cache["dawes_limit"] = self.telescope.dawes_limit()
            else:
                self._cache["dawes_limit"] = None
        return self._cache["dawes_limit"]

    def rayleigh_limit(self, wavelength_nm: float | int = 550) -> Optional["Quantity"]:
        """
        Calculates the Rayleigh limit (resolving power) of the telescope in arcseconds.
        """
        cache_key = f"rayleigh_limit_{wavelength_nm}"
        if cache_key not in self._cache:
            if hasattr(self.telescope, "rayleigh_limit"):
                self._cache[cache_key] = self.telescope.rayleigh_limit(
                    wavelength_nm=wavelength_nm
                )
            else:
                self._cache[cache_key] = None
        return self._cache[cache_key]

    def airy_disk_diameter(self, wavelength_nm: float = 550) -> Optional["Quantity"]:
        """
        Calculates the physical diameter of the Airy disk (first dark ring) in micrometers.
        """
        if not hasattr(self.telescope, "focal_ratio"):
            return None
        # Effective focal ratio
        fr = (self.telescope.focal_ratio() * self.effective_barlow()).magnitude
        diameter_um = optics_utils.calculate_airy_disk_diameter(fr, wavelength_nm)
        return float(diameter_um) * get_unit_registry().micrometer

    def ideal_planetary_focal_ratio(self, k: float = 5.0) -> Optional[float]:
        """
        Calculates the ideal focal ratio for planetary imaging based on the pixel size.
        """
        from ...opticalequipment.camera import Camera
        from ...opticalequipment.smart_telescope import SmartTelescope

        if not isinstance(self.output, (Camera, SmartTelescope)):
            return None

        # Pixel size in microns
        p_size_q = self.output.pixel_size()
        if p_size_q is None:
            return None
        p_size = p_size_q.to("micrometer").magnitude
        return k * p_size

    def nyquist_focal_ratio(
        self, wavelength_nm: float = 550, sampling_factor: float = 3.0
    ) -> Optional[float]:
        """
        Calculates the ideal focal ratio for a given wavelength and sampling factor.
        """
        from ...opticalequipment.camera import Camera
        from ...opticalequipment.smart_telescope import SmartTelescope

        if not isinstance(self.output, (Camera, SmartTelescope)):
            return None

        p_size_q = self.output.pixel_size()
        if p_size_q is None:
            return None

        p_um = p_size_q.to("micrometer").magnitude
        lambda_um = wavelength_nm / 1000.0

        return (p_um * sampling_factor) / (1.22 * lambda_um)

    def psf_peak_fraction(self, seeing: float) -> Optional[float]:
        """
        Calculates the fraction of light from a point source that falls into the central pixel.
        """
        scale = self.pixel_scale()
        if scale is None or seeing <= 0:
            return None

        arg = (scale.magnitude * math.sqrt(math.log(2))) / seeing
        fraction = math.erf(arg) ** 2
        return float(fraction)
