from typing import Optional, TYPE_CHECKING, Any
from ...units import get_unit_registry
from ..calculations import exposure as optics_utils

if TYPE_CHECKING:
    from pint import Quantity


class ExposureMixIn:
    if TYPE_CHECKING:
        output: Any
        telescope: Any
        def effective_barlow(self) -> float: ...
        def pixel_scale(self) -> Optional["Quantity"]: ...

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
        if not hasattr(self.output, "pixel_size") or not hasattr(
            self.telescope, "focal_ratio"
        ):
            return None

        # F-number (N)
        n = (self.telescope.focal_ratio() * self.effective_barlow()).magnitude
        # Pixel pitch in microns (P)
        p_size_q = self.output.pixel_size()
        if p_size_q is None:
            return None
        p = p_size_q.to("micrometer").magnitude
        # Focal length in mm (F)
        f = (self.telescope.focal_length * self.effective_barlow()).to("mm").magnitude

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
        scale_q = self.pixel_scale()
        if scale_q is None:
            return None

        scale = scale_q.magnitude  # arcsec/pixel
        res = optics_utils.calculate_estimated_star_trailing(
            exposure_time, declination, scale
        )
        return float(res)

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

        if not isinstance(self.output, (Camera, SmartTelescope)):
            return None

        # Field rotation rate in arcsec/s
        rot_rate_q = self.field_rotation_rate(latitude_deg, azimuth_deg, altitude_deg)
        if rot_rate_q is None:
            return None
        rot_rate = rot_rate_q.to("arcsecond/second").magnitude

        # Distance from center to corner in pixels
        p_scale = self.pixel_scale()
        if p_scale is None:
            return None

        t = optics_utils.calculate_max_exposure_alt_az(
            rot_rate,
            float(self.output.width),
            float(self.output.height),
            tolerance_pixels,
        )

        return t * get_unit_registry().second

    def rule_of_500(self) -> "Quantity":
        """
        Calculates the maximum exposure time to avoid star trailing using the classic Rule of 500.
        Formula: t = 500 / (F_actual * crop_factor)
        """
        # Actual focal length
        f_actual = (
            (self.telescope.focal_length * self.effective_barlow()).to("mm").magnitude
        )

        if f_actual == 0:
            return 0 * get_unit_registry().second

        sensor_width = None
        sensor_height = None
        if hasattr(self.output, "sensor_width") and hasattr(
            self.output, "sensor_height"
        ):
            sensor_width = self.output.sensor_width.to("mm").magnitude
            sensor_height = self.output.sensor_height.to("mm").magnitude

        t = optics_utils.calculate_rule_of_500(f_actual, sensor_width, sensor_height)
        return t * get_unit_registry().second
