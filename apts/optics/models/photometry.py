from typing import Optional, TYPE_CHECKING
import numpy
from ...units import get_unit_registry
from ...utils import optics as optics_utils

if TYPE_CHECKING:
    from pint import Quantity
    from typing import Any, List


class PhotometryMixIn:
    if TYPE_CHECKING:
        def pixel_scale(self) -> "Quantity": ...
        output: Any
        telescope: Any
        filters: List[Any]
        def atmospheric_extinction(self, magnitude: float, altitude_degrees: float, extinction_k: float = 0.2) -> float: ...

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

        scale = self.pixel_scale()
        if scale is None or not isinstance(self.output, (Camera, SmartTelescope)):
            return None
        if self.output.quantum_efficiency is None:
            return None

        area_cm2 = self.telescope.aperture_area().to("cm**2").magnitude
        qe = self.output.quantum_efficiency
        transmission = 1.0
        for f in self.filters:
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
            not isinstance(self.output, (Camera, SmartTelescope))
            or self.output.quantum_efficiency is None
        ):
            return None

        # Apply atmospheric extinction if altitude is provided
        effective_magnitude = magnitude
        if altitude is not None:
            effective_magnitude = self.atmospheric_extinction(
                magnitude, altitude, extinction_k
            )

        area_cm2 = self.telescope.aperture_area().to("cm**2").magnitude
        qe = self.output.quantum_efficiency
        transmission = 1.0
        for f in self.filters:
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

        obj_flux = self.object_flux(
            magnitude, altitude=altitude, extinction_k=extinction_k
        )
        sky_flux_val = self.sky_flux(sqm)

        if (
            obj_flux is None
            or sky_flux_val is None
            or not isinstance(self.output, (Camera, SmartTelescope))
            or self.output.read_noise is None
        ):
            return None

        snr_val = optics_utils.calculate_snr(
            obj_flux,
            sky_flux_val,
            self.output.read_noise,
            exposure_time,
            n_subs,
            n_pix,
            in_db,
        )
        return float(snr_val)

    def required_subs_for_snr(
        self,
        target_snr: float,
        magnitude: float,
        sqm: float,
        exposure_time: float,
        n_pix: int = 4,
        altitude: Optional[float] = None,
        extinction_k: float = 0.2,
    ) -> Optional[float]:
        """
        Calculates the number of sub-exposures needed to reach a target SNR.
        Formula derived from SNR equation: N = SNR^2 * (S + B + R) / S^2
        Where S is signal, B is sky noise squared, R is read noise squared (all per sub).
        """
        obj_flux = self.object_flux(
            magnitude, altitude=altitude, extinction_k=extinction_k
        )
        sky_flux_val = self.sky_flux(sqm)

        if (
            obj_flux is None
            or sky_flux_val is None
            or not hasattr(self.output, "read_noise")
            or self.output.read_noise is None
        ):
            return None

        # Signal and noise per single sub
        s = obj_flux * exposure_time
        b = sky_flux_val * exposure_time * n_pix
        r = (self.output.read_noise**2) * n_pix

        if s <= 0:
            return numpy.inf

        n_required = (target_snr**2) * (s + b + r) / (s**2)
        return float(numpy.ceil(n_required))

    def required_integration_time(
        self,
        target_snr: float,
        magnitude: float,
        sqm: float,
        exposure_time: float,
        n_pix: int = 4,
        altitude: Optional[float] = None,
        extinction_k: float = 0.2,
    ) -> Optional["Quantity"]:
        """
        Calculates the total integration time needed to reach a target SNR.
        """
        n_subs = self.required_subs_for_snr(
            target_snr,
            magnitude,
            sqm,
            exposure_time,
            n_pix=n_pix,
            altitude=altitude,
            extinction_k=extinction_k,
        )
        if n_subs is None:
            return None
        return n_subs * exposure_time * get_unit_registry().second

    def optimum_sub_exposure(
        self, sqm: float, swamp_factor: float = 10.0
    ) -> Optional["Quantity"]:
        """
        Calculates the exposure time at which the sky noise (shot noise from the sky background)
        becomes dominant over the sensor's read noise by a given 'swamp factor'.

        A common rule of thumb is a swamp factor of 10.0, meaning sky noise power is 10x
        the read noise power (sky noise is ~3.16x read noise), resulting in a
        signal-to-noise ratio loss of only ~5% compared to an infinite exposure.

        Formula: t = (swamp_factor * read_noise^2) / sky_flux
        """
        from ...opticalequipment.camera import Camera
        from ...opticalequipment.smart_telescope import SmartTelescope

        flux = self.sky_flux(sqm)
        if (
            flux is None
            or not isinstance(self.output, (Camera, SmartTelescope))
            or self.output.read_noise is None
        ):
            return None
        # Time where SkyNoise^2 = swamp_factor * ReadNoise^2
        # SkyNoise^2 = Flux * Time
        # Time = swamp_factor * ReadNoise^2 / Flux
        time = (swamp_factor * self.output.read_noise**2) / flux
        return time * get_unit_registry().second

    def camera_limiting_magnitude(
        self,
        sqm: float,
        total_integration_time: float,
        sub_exposure_time: float,
        target_snr: float = 5.0,
        n_pix: int = 4,
        altitude: Optional[float] = None,
        extinction_k: float = 0.2,
    ) -> Optional[float]:
        """
        Calculates the limiting magnitude for a camera based on reaching a target SNR.
        Uses binary search to find the magnitude where SNR equals target_snr.
        Search range: 0.0 to 30.0 magnitude. Convergence: 0.01 magnitude.
        """
        low = 0.0
        high = 30.0
        n_subs = int(numpy.ceil(total_integration_time / sub_exposure_time))

        for _ in range(12):  # 2^12 = 4096, plenty for 0.01 prec in 30 range
            mid = (low + high) / 2
            current_snr = self.snr(
                mid,
                sqm,
                sub_exposure_time,
                n_subs=n_subs,
                n_pix=n_pix,
                altitude=altitude,
                extinction_k=extinction_k,
            )
            if current_snr is None:
                return None
            if current_snr > target_snr:
                low = mid
            else:
                high = mid

        return round(float(low), 2)

    def limiting_magnitude(self, sqm: float, integration_time: float) -> float:
        from ...opticalequipment.camera import Camera
        from ...opticalequipment.smart_telescope import SmartTelescope

        # integration_time in seconds
        if (
            not isinstance(self.output, (Camera, SmartTelescope))
            or self.output.quantum_efficiency is None
        ):
            # Fallback to telescope limiting magnitude if no camera data
            return self.telescope.limiting_magnitude()

        aperture_cm = self.telescope.aperture.to("cm").magnitude
        # Base limiting magnitude for 1 second at SQM 21
        base = 7.7 + 5 * numpy.log10(aperture_cm)
        # Add integration time factor: 1.25 * log10(T)
        time_factor = 1.25 * numpy.log10(integration_time)
        # SQM factor: (SQM - 21)
        sqm_factor = sqm - 21.0

        return base + time_factor + sqm_factor
