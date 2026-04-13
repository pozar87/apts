import math
from typing import Optional, TYPE_CHECKING
import numpy
from ...units import get_unit_registry
from ...constants import astronomy
from ...utils import optics as optics_utils

if TYPE_CHECKING:
    from pint import Quantity


class ExposureMixIn:
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
        obj_flux = self.object_flux( # type: ignore
            magnitude, altitude=altitude, extinction_k=extinction_k
        )
        sky_flux_val = self.sky_flux(sqm) # type: ignore

        if (
            obj_flux is None
            or sky_flux_val is None
            or not hasattr(self.output, "read_noise") # type: ignore
            or self.output.read_noise is None # type: ignore
        ):
            return None

        # Signal and noise per single sub
        s = obj_flux * exposure_time
        b = sky_flux_val * exposure_time * n_pix
        r = (self.output.read_noise**2) * n_pix # type: ignore

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

        flux = self.sky_flux(sqm) # type: ignore
        if (
            flux is None
            or not isinstance(self.output, (Camera, SmartTelescope)) # type: ignore
            or self.output.read_noise is None # type: ignore
        ):
            return None
        # Time where SkyNoise^2 = swamp_factor * ReadNoise^2
        # SkyNoise^2 = Flux * Time
        # Time = swamp_factor * ReadNoise^2 / Flux
        time = (swamp_factor * self.output.read_noise**2) / flux # type: ignore
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
            current_snr = self.snr( # type: ignore
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
            not isinstance(self.output, (Camera, SmartTelescope)) # type: ignore
            or self.output.quantum_efficiency is None # type: ignore
        ):
            # Fallback to telescope limiting magnitude if no camera data
            return self.telescope.limiting_magnitude() # type: ignore

        aperture_cm = self.telescope.aperture.to("cm").magnitude # type: ignore
        # Base limiting magnitude for 1 second at SQM 21
        base = 7.7 + 5 * numpy.log10(aperture_cm)
        # Add integration time factor: 1.25 * log10(T)
        time_factor = 1.25 * numpy.log10(integration_time)
        # SQM factor: (SQM - 21)
        sqm_factor = sqm - 21.0

        return float(base + time_factor + sqm_factor)

    def npf_rule(
        self, declination: float = 0, k: float = 1.0, simplified: bool = False
    ) -> Optional["Quantity"]:
        """
        Calculates the maximum exposure time to avoid star trailing using the NPF rule.
        The NPF rule is more accurate than the 'Rule of 500' for modern high-resolution sensors.

        Two versions are available:
        1. Complete (default): t = k * (16.9 * N + 0.10 * F + 13.7 * P) / (F * cos(dec))
        2. Simplified: t = k * (35 * N + 30 * P) / (F * cos(dec))

        Where:
        - N: f-number (focal ratio)
        - P: pixel pitch in micrometers (µm)
        - F: focal length in millimeters (mm)
        - dec: declination of the target in degrees
        - k: tolerance factor (1.0 for pinpoint stars, up to 3.0 for slightly elongated)

        Source: Frédéric Michaud, Société Astronomique du Havre (SAH)
        https://sahavre.fr/wp/regle-npf-rule/
        """
        if not hasattr(self.output, "pixel_size") or not hasattr( # type: ignore
            self.telescope, "focal_ratio" # type: ignore
        ):
            return None

        # F-number (N)
        n = (self.telescope.focal_ratio() * self.effective_barlow()).magnitude # type: ignore
        # Pixel pitch in microns (P)
        p_size_q = self.output.pixel_size() # type: ignore
        if p_size_q is None:
            return None
        p = p_size_q.to("micrometer").magnitude
        # Focal length in mm (F)
        f = (self.telescope.focal_length * self.effective_barlow()).to("mm").magnitude # type: ignore

        res = optics_utils.calculate_npf_rule(n, p, f, declination, k, simplified)
        return float(res) * get_unit_registry().second

    def estimated_star_trailing(
        self, exposure_time: float, declination: float = 0
    ) -> Optional[float]:
        """
        Estimates the amount of star trailing in pixels for a given exposure time and declination
        assuming a stationary (non-tracking) mount.

        Formula: trailing_pixels = (sidereal_rate * exposure_time * cos(declination)) / pixel_scale
        Where sidereal_rate is ~15.041 arcseconds per second.
        """
        scale_q = self.pixel_scale() # type: ignore
        if scale_q is None:
            return None

        scale = scale_q.magnitude  # arcsec/pixel
        if scale == 0:
            return 0.0

        # Sidereal rotation rate in arcseconds per second
        sidereal_rate = 15.041067

        cos_dec = math.cos(math.radians(declination))
        trailing_arcsec = sidereal_rate * exposure_time * cos_dec

        return float(trailing_arcsec / scale)

    def field_rotation_rate(
        self, latitude_deg: float, azimuth_deg: float, altitude_deg: float
    ) -> "Quantity":
        """
        Calculates the field rotation rate for an Alt-Az mount in arcseconds per second.
        Formula: omega_rot = omega_earth * cos(lat) * cos(az) / cos(alt)
        Where omega_earth is the sidereal rotation rate (15.041067 "/s).
        Source: "Field Rotation" - Bill Keicher
        """
        rate = optics_utils.calculate_field_rotation_rate(
            latitude_deg, azimuth_deg, altitude_deg
        )
        return float(rate) * (
            get_unit_registry().arcsecond / get_unit_registry().second
        )

    def max_exposure_alt_az(
        self,
        latitude_deg: float,
        azimuth_deg: float,
        altitude_deg: float,
        tolerance_pixels: float = 1.0,
    ) -> Optional["Quantity"]:
        """
        Calculates the maximum exposure time for an Alt-Az mount to avoid field rotation trailing.
        The calculation is based on the movement of the furthest pixel from the sensor center (the corners).
        """
        from ...opticalequipment.camera import Camera
        from ...opticalequipment.smart_telescope import SmartTelescope

        if not isinstance(self.output, (Camera, SmartTelescope)): # type: ignore
            return None

        # Field rotation rate in arcsec/s
        rot_rate_q = self.field_rotation_rate(latitude_deg, azimuth_deg, altitude_deg)
        if rot_rate_q is None:
            return None
        rot_rate = rot_rate_q.to("arcsecond/second").magnitude

        if rot_rate < 1e-10:
            return 3600 * get_unit_registry().second

        # Pixel scale in arcsec/pixel
        p_scale = self.pixel_scale() # type: ignore
        if p_scale is None:
            return None

        # Distance from center to corner in pixels
        # r = sqrt((width/2)^2 + (height/2)^2)
        r = 0.5 * numpy.sqrt(self.output.width**2 + self.output.height**2) # type: ignore

        t = (tolerance_pixels * astronomy.RAD_TO_ARCSEC) / (r * rot_rate)

        return t * get_unit_registry().second

    def rule_of_500(self) -> "Quantity":
        """
        Calculates the maximum exposure time to avoid star trailing using the classic Rule of 500.
        Formula: t = 500 / (F_actual * crop_factor)
        """
        # Actual focal length
        f_actual = (
            (self.telescope.focal_length * self.effective_barlow()).to("mm").magnitude # type: ignore
        )

        if f_actual == 0:
            return 0 * get_unit_registry().second

        if hasattr(self.output, "sensor_width") and hasattr( # type: ignore
            self.output, "sensor_height" # type: ignore
        ):
            # crop_factor = 43.27 / diagonal
            # diagonal of 35mm sensor (36x24) is ~43.27mm
            diagonal = numpy.sqrt(
                self.output.sensor_width.to("mm").magnitude ** 2 # type: ignore
                + self.output.sensor_height.to("mm").magnitude ** 2 # type: ignore
            )
            if diagonal == 0:
                return (500 / f_actual) * get_unit_registry().second
            crop_factor = 43.27 / diagonal
            t = 500 / (f_actual * crop_factor)
        else:
            # Fallback for non-camera or visual setup (though less relevant)
            t = 500 / f_actual

        return t * get_unit_registry().second

    def dynamic_range(self) -> Optional[float]:
        """
        Calculates the dynamic range of the camera or smart telescope in the optical path.
        """
        from ...opticalequipment.camera import Camera
        from ...opticalequipment.smart_telescope import SmartTelescope

        if isinstance(self.output, (Camera, SmartTelescope)): # type: ignore
            return self.output.dynamic_range()
        return None

    def saturation_time(
        self,
        magnitude: float,
        seeing: float,
        altitude: Optional[float] = None,
        extinction_k: float = 0.2,
    ) -> Optional["Quantity"]:
        """
        Calculates the maximum exposure time before the central pixel of a point source saturates.
        Based on the full-well capacity of the sensor and the Gaussian PSF model.
        """
        from ...opticalequipment.camera import Camera
        from ...opticalequipment.smart_telescope import SmartTelescope

        if not isinstance(self.output, (Camera, SmartTelescope)): # type: ignore
            return None

        if self.output.full_well is None: # type: ignore
            return None

        obj_flux = self.object_flux( # type: ignore
            magnitude, altitude=altitude, extinction_k=extinction_k
        )
        f = self.psf_peak_fraction(seeing) # type: ignore

        if obj_flux is None or f is None or obj_flux <= 0 or f <= 0:
            return None

        # S_peak = flux * t * f
        # t = full_well / (flux * f)
        t = self.output.full_well / (obj_flux * f) # type: ignore
        return t * get_unit_registry().second

    def saturation_magnitude(
        self,
        exposure_time: float,
        seeing: float,
        altitude: Optional[float] = None,
        extinction_k: float = 0.2,
    ) -> Optional[float]:
        """
        Calculates the magnitude of a point source that would just saturate the sensor
        at the given exposure time and seeing conditions.
        """
        from ...opticalequipment.camera import Camera
        from ...opticalequipment.smart_telescope import SmartTelescope

        if not isinstance(self.output, (Camera, SmartTelescope)): # type: ignore
            return None

        if self.output.full_well is None: # type: ignore
            return None

        f = self.psf_peak_fraction(seeing) # type: ignore
        if f is None or f <= 0 or exposure_time <= 0:
            return None

        # target_flux = full_well / (t * f)
        target_flux = self.output.full_well / (exposure_time * f) # type: ignore

        # flux = 0.005 * 10^(0.4 * (21.83 - m_eff)) * Area * QE * Transmission
        # We can find m_eff using binary search or analytical inversion.
        # Since we have object_flux(m), we know object_flux(0)
        flux_at_zero = self.object_flux(0.0, altitude=None, extinction_k=0.0) # type: ignore
        if flux_at_zero is None:
            return None

        # target_flux = flux_at_zero * 10^(-0.4 * m_eff)
        # 10^(-0.4 * m_eff) = target_flux / flux_at_zero
        # -0.4 * m_eff = log10(target_flux / flux_at_zero)
        # m_eff = -2.5 * log10(target_flux / flux_at_zero)
        m_eff = -2.5 * math.log10(target_flux / flux_at_zero)

        if altitude is not None:
            # m_eff = m + k * X
            # m = m_eff - k * X
            airmass_val = self.airmass(altitude) # type: ignore
            return float(m_eff - extinction_k * airmass_val)

        return float(m_eff)
