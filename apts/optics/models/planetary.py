import math
from typing import Optional, Any, Union, cast, TYPE_CHECKING
import numpy
from ...units import get_unit_registry

if TYPE_CHECKING:
    from pint import Quantity


class PlanetaryMixIn:
    def planetary_size_in_pixels(
        self, planet_name: str, time: Any, which: str = "equatorial"
    ) -> Optional[Union[float, numpy.ndarray]]:
        """
        Calculates the projected size of a planet on the sensor in pixels.
        Uses the planet's angular diameter and the setup's pixel scale.

        :param planet_name: Name of the planet (e.g., 'Jupiter').
        :param time: Skyfield Time object.
        :param which: 'equatorial' (default), 'polar', or 'apparent_polar'.
                      'apparent_polar' accounts for the planet's tilt towards Earth.
        """
        from ...utils import planetary

        angular_diameter = planetary.get_planet_angular_diameter(
            planet_name, time, which=which
        )
        p_scale = self.pixel_scale()

        if p_scale is None or p_scale.magnitude == 0:
            return None

        res = angular_diameter / p_scale.magnitude
        if numpy.isscalar(res):
            return float(cast(Any, res))
        return cast(numpy.ndarray, res)

    def saturn_ring_size_in_pixels(
        self, time: Any
    ) -> Optional[tuple[Union[float, numpy.ndarray], Union[float, numpy.ndarray]]]:
        """
        Calculates the projected size of Saturn's rings on the sensor in pixels.
        Returns a tuple (major_axis_pixels, minor_axis_pixels).
        """
        from ...utils import planetary

        details = planetary.get_saturn_ring_details(time)
        p_scale = self.pixel_scale()

        if p_scale is None or p_scale.magnitude == 0:
            return None

        major = details["major_axis_arcsec"] / p_scale.magnitude
        minor = details["minor_axis_arcsec"] / p_scale.magnitude

        def _maybe_cast(val):
            if numpy.isscalar(val):
                return float(cast(Any, val))
            return cast(numpy.ndarray, val)

        return _maybe_cast(major), _maybe_cast(minor)

    def planetary_phase_angle(
        self, planet_name: str, time: Any
    ) -> Union[float, numpy.ndarray]:
        """
        Calculates the phase angle (Sun-Object-Earth) for a planet or the Moon.
        """
        from ...utils import planetary

        return planetary.get_planet_phase_angle(planet_name, time)

    def moon_libration(self, time: Any) -> tuple[float, float]:
        """
        Calculates the Moon's libration in longitude and latitude in degrees.
        """
        from ...utils import planetary

        lon, lat = planetary.get_moon_libration(time)
        if numpy.isscalar(lon):
            return float(cast(Any, lon)), float(cast(Any, lat))
        return cast(Any, (lon, lat))

    def moon_position_angle_bright_limb(self, time: Any) -> float:
        """
        Calculates the position angle of the Moon's bright limb in degrees.
        """
        from ...utils import planetary

        return planetary.get_moon_position_angle_bright_limb(time)

    def planetary_magnitude(
        self, planet_name: str, time: Any
    ) -> Union[float, numpy.ndarray]:
        """
        Calculates the apparent magnitude of a planet, the Moon, or the Sun.
        """
        from ...utils import planetary

        return planetary.get_planet_magnitude(planet_name, time)

    def planetary_phase(
        self, planet_name: str, time: Any
    ) -> Union[float, numpy.ndarray]:
        """
        Calculates the illuminated fraction of a planet or the Moon as a percentage (0-100).
        """
        from ...utils import planetary

        return planetary.get_planet_phase(planet_name, time)

    def planetary_surface_brightness(
        self, planet_name: str, time: Any
    ) -> Union[float, numpy.ndarray]:
        """
        Calculates the average surface brightness of a planet, the Moon, or the Sun
        in mag/arcsec².
        """
        from ...utils import planetary

        return planetary.get_planet_surface_brightness(planet_name, time)

    def moon_colongitude(self, time: Any) -> Union[float, numpy.ndarray]:
        """
        Calculates the Moon's selenographic colongitude in degrees.
        """
        from ...utils import planetary

        return planetary.get_moon_colongitude(time)

    def jupiter_cml(self, time: Any, system: int = 2) -> Union[float, numpy.ndarray]:
        """
        Calculates Jupiter's Central Meridian Longitude (CML) for the specified system (1 or 2).
        """
        from ...utils import planetary

        return planetary.get_jupiter_cml(time, system)

    def mars_cml(self, time: Any) -> Union[float, numpy.ndarray]:
        """
        Calculates Mars' Central Meridian Longitude (CML).
        """
        from ...utils import planetary

        return planetary.get_mars_cml(time)

    def saturn_cml(self, time: Any, system: int = 3) -> Union[float, numpy.ndarray]:
        """
        Calculates Saturn's Central Meridian Longitude (CML) for the specified system (1, 2 or 3).
        """
        from ...utils import planetary

        return planetary.get_saturn_cml(time, system)

    def sun_physical_details(self, time: Any) -> dict:
        """
        Calculates the physical details of the Sun (P, B0, L0).
        """
        from ...utils import planetary

        return planetary.get_sun_physical_details(time)

    def max_planetary_rotation_duration(
        self, planet_name: str, time: Any, tolerance_pixels: float = 1.0
    ) -> Optional["Quantity"]:
        """
        Calculates the maximum recording duration (in seconds) before planetary rotation
        causes a blur exceeding the given pixel tolerance.
        Useful for planetary imagers (lucky imaging) to determine when to start a new capture
        or use tools like WinJUPOS for de-rotation.
        """
        from ...utils import planetary

        scale_q = self.pixel_scale()
        if scale_q is None:
            return None

        scale = scale_q.to("arcsecond").magnitude

        # Equatorial angular radius (half of diameter)
        r_eq = (
            planetary.get_planet_angular_diameter(planet_name, time, which="equatorial")
            / 2.0
        )

        # Sidereal rotation period in seconds
        period = planetary.get_planet_rotation_period(planet_name)

        # Sub-observer latitude (tilt)
        try:
            de_deg = planetary.get_sub_observer_latitude(planet_name, time)
            cos_de = math.cos(math.radians(de_deg))
        except ValueError:
            # Fallback for planets without pole models (e.g., Mercury, Venus)
            cos_de = 1.0

        if r_eq <= 0 or period <= 0:
            return None

        # Angular velocity of a point at the center of the disk as seen from Earth (arcsec/s)
        # v_arcsec = (2 * pi * r_eq_arcsec * cos(De)) / T
        omega = (2.0 * math.pi * r_eq * cos_de) / period

        if omega <= 1e-12:
            return (
                3600 * get_unit_registry().second
            )  # Cap at 1 hour for very slow rotators

        t_max = (tolerance_pixels * scale) / omega

        return t_max * get_unit_registry().second
