import math
from typing import TYPE_CHECKING, Optional

if TYPE_CHECKING:
    from pint import Quantity

from ...units import get_unit_registry
from ...utils import optics as optics_utils
from ...opticalequipment.binoculars import Binoculars
from ...opticalequipment.naked_eye import NakedEye


class PhotometryMixIn:
    def brightness(self) -> "Quantity":
        if "brightness" in self._cache: # type: ignore
            return self._cache["brightness"] # type: ignore

        from ...opticalequipment.smart_telescope import SmartTelescope

        if isinstance(self.telescope, (Binoculars, NakedEye, SmartTelescope)): # type: ignore
            # self.telescope.brightness() returns a float like 75.0 (for 75%)
            # OutputOpticalEquipment.brightness returns a value like <Quantity(75.0, 'dimensionless')>
            # To be consistent so that .magnitude can be called later:
            brightness = self.telescope.brightness() * get_unit_registry().dimensionless # type: ignore
        else:
            # This already returns a pint Quantity from OutputOpticalEquipment's method
            brightness = self.output.brightness(self.telescope, self.zoom()) # type: ignore

        # Account for filters transmission
        for f in self.filters: # type: ignore
            brightness *= f.transmission

        self._cache["brightness"] = brightness # type: ignore
        return brightness

    def exit_pupil(self) -> "Quantity":
        from ...opticalequipment.smart_telescope import SmartTelescope

        if isinstance(self.telescope, (Binoculars, NakedEye, SmartTelescope)): # type: ignore
            return self.telescope.exit_pupil()  # This returns a Quantity

        # Original logic for telescopes:
        # telescope.aperture should be a Quantity (e.g., mm)
        # self.zoom() returns a dimensionless Quantity
        # The result will be in units of aperture (e.g., mm)
        if hasattr(self.telescope, "aperture"): # type: ignore
            zoom_value = self.zoom() # type: ignore
            if zoom_value.magnitude == 0:  # pyright: ignore
                return 0 * get_unit_registry().mm
            return self.telescope.aperture / zoom_value # type: ignore

        # If it's not Binoculars and telescope has no aperture (should not happen for Telescopes)
        # return a zero quantity to avoid crashes, though this indicates a data problem.
        return 0 * get_unit_registry().mm

    def sky_flux(self, sqm: float) -> Optional[float]:
        """
        Calculates the sky background flux in electrons per second per pixel.
        Assumes an L-band (clear) filter equivalent and a zero point where a 21.83 mag/arcsec^2
        sky produces a specific reference flux.

        :param sqm: Sky Quality Meter reading in mag/arcsec^2.
        :return: Sky flux in e-/s/pixel.
        """
        from ...opticalequipment.camera import Camera
        from ...opticalequipment.smart_telescope import SmartTelescope

        scale = self.pixel_scale() # type: ignore
        if scale is None or not isinstance(self.output, (Camera, SmartTelescope)): # type: ignore
            return None
        if self.output.quantum_efficiency is None: # type: ignore
            return None

        area_cm2 = self.telescope.aperture_area().to("cm**2").magnitude # type: ignore
        qe = self.output.quantum_efficiency # type: ignore
        transmission = 1.0
        for f in self.filters: # type: ignore
            transmission *= f.transmission

        flux = optics_utils.calculate_sky_flux(
            sqm, area_cm2, qe, scale.magnitude, transmission
        )
        return float(flux)

    def object_flux(
        self,
        magnitude: float,
        altitude: Optional[float] = None,
        extinction_k: float = 0.2,
    ) -> Optional[float]:
        """
        Calculates the total integrated flux from an object in electrons per second.
        The calculation is based on the object's magnitude and the setup's aperture and QE.

        :param magnitude: Apparent magnitude of the object.
        :param altitude: Optional altitude in degrees to account for atmospheric extinction.
        :param extinction_k: Atmospheric extinction coefficient (default 0.2).
        :return: Total integrated object flux in e-/s.
        """
        from ...opticalequipment.camera import Camera
        from ...opticalequipment.smart_telescope import SmartTelescope

        if (
            not isinstance(self.output, (Camera, SmartTelescope)) # type: ignore
            or self.output.quantum_efficiency is None # type: ignore
        ):
            return None

        # Apply atmospheric extinction if altitude is provided
        effective_magnitude = magnitude
        if altitude is not None:
            effective_magnitude = self.atmospheric_extinction( # type: ignore
                magnitude, altitude, extinction_k
            )

        area_cm2 = self.telescope.aperture_area().to("cm**2").magnitude # type: ignore
        qe = self.output.quantum_efficiency # type: ignore
        transmission = 1.0
        for f in self.filters: # type: ignore
            transmission *= f.transmission

        flux = optics_utils.calculate_object_flux(
            effective_magnitude, area_cm2, qe, transmission
        )
        return float(flux)

    def snr(
        self,
        magnitude: float,
        sqm: float,
        exposure_time: float,
        n_subs: int = 1,
        n_pix: int = 4,
        altitude: Optional[float] = None,
        extinction_k: float = 0.2,
        in_db: bool = False,
    ) -> Optional[float]:
        """
        Calculates the Signal-to-Noise Ratio (SNR) for an object in the given optical path.
        The model accounts for object shot noise, sky background shot noise, and sensor read noise.
        It assumes aperture photometry where the object signal is integrated over `n_pix` pixels.

        :param magnitude: Apparent magnitude of the object.
        :param sqm: Sky Quality Meter reading in mag/arcsec^2.
        :param exposure_time: Exposure time per sub-exposure in seconds.
        :param n_subs: Number of sub-exposures stacked.
        :param n_pix: Number of pixels over which the object signal is integrated (default 4).
        :param altitude: Optional altitude in degrees for atmospheric extinction.
        :param extinction_k: Atmospheric extinction coefficient (default 0.2).
        :param in_db: If True, returns SNR in decibels (20 * log10).
        :return: SNR (dimensionless linear ratio or dB).
        """
        from ...opticalequipment.camera import Camera
        from ...opticalequipment.smart_telescope import SmartTelescope

        obj_flux = self.object_flux( # type: ignore
            magnitude, altitude=altitude, extinction_k=extinction_k
        )
        sky_flux_val = self.sky_flux(sqm) # type: ignore

        if (
            obj_flux is None
            or sky_flux_val is None
            or not isinstance(self.output, (Camera, SmartTelescope)) # type: ignore
            or self.output.read_noise is None # type: ignore
        ):
            return None

        snr_val = optics_utils.calculate_snr(
            obj_flux,
            sky_flux_val,
            self.output.read_noise, # type: ignore
            exposure_time,
            n_subs,
            n_pix,
            in_db,
        )
        return float(snr_val)

    def psf_peak_fraction(self, seeing: float) -> Optional[float]:
        """
        Calculates the fraction of light from a point source that falls into the central pixel,
        assuming a Gaussian Point Spread Function (PSF).
        Formula: f = erf(pixel_scale * sqrt(ln2) / seeing)^2
        Where 'seeing' is the Full Width at Half Maximum (FWHM) in arcseconds.
        """
        scale = self.pixel_scale() # type: ignore
        if scale is None or seeing <= 0:
            return None

        # f = erf(L * sqrt(ln2) / FWHM)^2
        # where L is pixel scale and FWHM is seeing.
        arg = (scale.magnitude * math.sqrt(math.log(2))) / seeing
        fraction = math.erf(arg) ** 2
        return float(fraction)
