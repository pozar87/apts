import functools
import operator
from typing import Any

import numpy

from .opticalequipment.binoculars import Binoculars
from .opticalequipment.naked_eye import NakedEye
from .units import get_unit_registry


class OpticsUtils:
    @staticmethod
    def expand(path):
        from .opticalequipment.barlow import Barlow
        from .opticalequipment.diagonal import Diagonal
        from .opticalequipment.filter import Filter
        from .opticalequipment.reducer import Corrector, Flattener, Reducer
        from .opticalequipment.smart_telescope import SmartTelescope

        # First item in the path should be the telescope or binoculars
        main_optic = path[0]
        if isinstance(main_optic, (Binoculars, NakedEye, SmartTelescope)):
            # Treat binoculars as the 'output' as well for path structure consistency
            return (main_optic, [], [], [], [], main_optic)

        # Original logic for telescopes
        telescope = main_optic
        # Last item in the path is output
        output = path[-1]
        # Intermediate elements
        intermediate = path[1:-1]
        # We treat Reducer, Flattener, and Corrector similarly to Barlow for magnification purposes
        barlows = [
            item
            for item in intermediate
            if isinstance(item, (Barlow, Reducer, Flattener, Corrector))
        ]
        diagonals = [item for item in intermediate if isinstance(item, Diagonal)]
        filters = [item for item in intermediate if isinstance(item, Filter)]
        others = [
            item
            for item in intermediate
            if not isinstance(
                item, (Barlow, Reducer, Flattener, Corrector, Diagonal, Filter)
            )
        ]
        return (telescope, barlows, diagonals, filters, others, output)

    @staticmethod
    def barlows_multiplications(barlows_list):
        barlows = [barlow.magnification for barlow in barlows_list]
        # Multiply all barlows
        return functools.reduce(operator.mul, barlows, 1)

    @staticmethod
    def compute_zoom(telescope, barlows, output):
        from .opticalequipment.smart_telescope import SmartTelescope

        if isinstance(telescope, (Binoculars, NakedEye, SmartTelescope)):
            return telescope.magnification * get_unit_registry().dimensionless

        # Original logic
        magnification = OpticsUtils.barlows_multiplications(barlows)
        return telescope.focal_length * magnification / output._zoom_divider()

    @staticmethod
    def calculate_airmass(altitude_degrees):
        """
        Calculates the relative airmass using the Kasten-Young (1989) formula.
        Formula: X = 1 / (sin(h) + 0.50572 * (h + 6.07995)^-1.6364)
        Where h is the apparent altitude in degrees.
        Source: https://en.wikipedia.org/wiki/Air_mass_(astronomy)
        """
        # Ensure altitude is at least 0 to avoid complex numbers/errors
        h = max(altitude_degrees, 0.0)
        return 1.0 / (numpy.sin(numpy.radians(h)) + 0.50572 * (h + 6.07995) ** -1.6364)

    @staticmethod
    def compute_field_of_view(telescope, barlows, output):
        from .opticalequipment.smart_telescope import SmartTelescope

        if isinstance(telescope, (Binoculars, NakedEye, SmartTelescope)):
            return telescope.fov()

        # Original logic
        magnification = OpticsUtils.barlows_multiplications(barlows)
        zoom = OpticsUtils.compute_zoom(telescope, barlows, output)
        # TODO: this is not best way to do it
        return output.field_of_view(telescope, zoom, magnification)


class OpticalPath:
    """
    Class representing an optical path in a telescope setup.
    """

    def __init__(self, telescope, barlows, diagonals, filters, others, output=None):
        self.telescope = telescope
        self.barlows = barlows
        self.diagonals = diagonals
        self.filters = filters
        if output is None:
            # Handle 5-argument constructor calls for backward compatibility
            self.others = []
            self.output = others
        else:
            self.others = others
            self.output = output

    @classmethod
    def from_path(cls, path):
        telescope, barlows, diagonals, filters, others, output = OpticsUtils.expand(
            path
        )
        return cls(telescope, barlows, diagonals, filters, others, output)

    def zoom(self):
        return OpticsUtils.compute_zoom(self.telescope, self.barlows, self.output)

    def effective_barlow(self):
        return OpticsUtils.barlows_multiplications(self.barlows)

    def label(self):
        from .opticalequipment.smart_telescope import SmartTelescope

        if isinstance(self.telescope, (Binoculars, NakedEye, SmartTelescope)):
            return str(self.telescope)
        return ", ".join(
            [str(self.telescope)]
            + [str(item) for item in self.barlows]
            + [str(item) for item in self.diagonals]
            + [str(item) for item in self.filters]
            + [str(item) for item in self.others]
            + [str(self.output)]
        )

    def length(self):
        from .opticalequipment.smart_telescope import SmartTelescope

        # For binoculars, path is [Binoculars], expanded to (Binoculars, [], Binoculars)
        # So self.barlows is []. Length should be 1 for a direct binocular path.
        # Original: return 2 + len(self.barlows) (Telescope + Output + Barlows)
        if isinstance(self.telescope, (Binoculars, NakedEye, SmartTelescope)):
            return 1  # Just the binoculars itself
        return (
            2
            + len(self.barlows)
            + len(self.diagonals)
            + len(self.filters)
            + len(self.others)
        )

    def fov(self):
        return OpticsUtils.compute_field_of_view(
            self.telescope, self.barlows, self.output
        )

    def fov_width(self):
        return self.output.field_of_view_width(
            self.telescope, self.zoom(), self.effective_barlow()
        )

    def fov_height(self):
        return self.output.field_of_view_height(
            self.telescope, self.zoom(), self.effective_barlow()
        )

    def fov_diagonal(self):
        return self.output.field_of_view_diagonal(
            self.telescope, self.zoom(), self.effective_barlow()
        )

    def airmass(self, altitude_degrees):
        """
        Calculates the relative airmass for a given altitude in degrees.
        """
        return OpticsUtils.calculate_airmass(altitude_degrees)

    def atmospheric_extinction(self, magnitude, altitude_degrees, extinction_k=0.2):
        """
        Calculates the apparent magnitude of an object accounting for atmospheric extinction.
        Formula: m_apparent = m_zero + k * X
        Where k is the extinction coefficient and X is the airmass.
        k typically ranges from 0.15 (very clear) to 0.5+ (hazy/polluted). Default 0.2.
        """
        airmass_val = self.airmass(altitude_degrees)
        return magnitude + extinction_k * airmass_val

    def atmospheric_dispersion(self, altitude_degrees, lambda1_nm=400, lambda2_nm=700):
        """
        Calculates the atmospheric dispersion (angular separation) between two wavelengths
        at a given altitude using the Peck and Reeder (1972) refractive index formula.
        Formula: (n-1) * 10^6 = 64.328 + 29498.1 / (146 - lambda^-2) + 255.4 / (41 - lambda^-2)
        Dispersion Delta R = (n1 - n2) * tan(zenith_distance)
        Source: Peck & Reeder (1972), "Refractive Index of Air in the Near Infrared"
        """
        if altitude_degrees >= 90:
            return 0.0 * get_unit_registry().arcsecond

        z = numpy.radians(90.0 - max(altitude_degrees, 0.1))  # Avoid tan(90)

        def get_n_minus_1(lambda_nm):
            l_um = lambda_nm / 1000.0
            l_inv_sq = 1.0 / (l_um**2)
            n_minus_1_e6 = (
                64.328 + 29498.1 / (146.0 - l_inv_sq) + 255.4 / (41.0 - l_inv_sq)
            )
            return n_minus_1_e6 * 1e-6

        n1_m_1 = get_n_minus_1(lambda1_nm)
        n2_m_1 = get_n_minus_1(lambda2_nm)

        dispersion_rad = abs(n1_m_1 - n2_m_1) * numpy.tan(z)
        dispersion_arcsec = numpy.degrees(dispersion_rad) * 3600.0

        return dispersion_arcsec * get_unit_registry().arcsecond

    def brightness(self):
        from .opticalequipment.smart_telescope import SmartTelescope

        if isinstance(self.telescope, (Binoculars, NakedEye, SmartTelescope)):
            # self.telescope.brightness() returns a float like 75.0 (for 75%)
            # OutputOpticalEquipment.brightness returns a value like <Quantity(75.0, 'dimensionless')>
            # To be consistent so that .magnitude can be called later:
            brightness = self.telescope.brightness() * get_unit_registry().dimensionless
        else:
            # This already returns a pint Quantity from OutputOpticalEquipment's method
            brightness = self.output.brightness(self.telescope, self.zoom())

        # Account for filters transmission
        for f in self.filters:
            brightness *= f.transmission

        return brightness

    def exit_pupil(self):
        from .opticalequipment.smart_telescope import SmartTelescope

        if isinstance(self.telescope, (Binoculars, NakedEye, SmartTelescope)):
            return self.telescope.exit_pupil()  # This returns a Quantity

        # Original logic for telescopes:
        # telescope.aperture should be a Quantity (e.g., mm)
        # self.zoom() returns a dimensionless Quantity
        # The result will be in units of aperture (e.g., mm)
        if hasattr(self.telescope, "aperture"):
            zoom_value = self.zoom()
            if zoom_value.magnitude == 0:  # pyright: ignore
                return 0 * get_unit_registry().mm
            return self.telescope.aperture / zoom_value

        # If it's not Binoculars and telescope has no aperture (should not happen for Telescopes)
        # return a zero quantity to avoid crashes, though this indicates a data problem.
        return 0 * get_unit_registry().mm

    def elements(self):
        """
        Return immutable set of elements - used for removing redundant optical paths
        """
        elements = set((self.telescope, self.output))
        elements |= set(self.barlows)
        elements |= set(self.diagonals)
        elements |= set(self.filters)
        elements |= set(self.others)
        return frozenset(elements)

    def total_mass(self):
        from .opticalequipment.abstract import OpticalEquipment

        all_equipment: set[OpticalEquipment] = set()
        for item in (
            [self.telescope]
            + self.barlows
            + self.diagonals
            + self.filters
            + self.others
            + [self.output]
        ):
            if hasattr(item, "collect_all_attached"):
                item.collect_all_attached(all_equipment)
            else:
                all_equipment.add(item)

        total = 0 * get_unit_registry().gram
        for eq in all_equipment:
            mass = getattr(eq, "mass", 0 * get_unit_registry().gram)
            if mass is not None:
                total += mass
        return total

    def backfocus_gap(self):
        """
        Calculate the backfocus gap.
        Returns a Quantity (distance) or None if no backfocus requirement is defined.
        """
        # 1. Find the component that defines the required backfocus
        required_bf = None
        start_index = -1

        # Flatten path for searching
        path = (
            [self.telescope]
            + self.barlows
            + self.diagonals
            + self.filters
            + self.others
            + [self.output]
        )

        for i, item in enumerate(path):
            # Check if component has required_backfocus (Reducer, Flattener, etc.)
            if (
                hasattr(item, "required_backfocus")
                and item.required_backfocus is not None
            ):
                required_bf = item.required_backfocus
                start_index = i
            # For telescopes, 'backfocus' property can also mean required backfocus from flange
            elif i == 0 and hasattr(item, "backfocus") and item.backfocus is not None:
                required_bf = item.backfocus
                start_index = i

        if required_bf is None:
            return None

        # 2. Calculate actual distance from that component's output to the sensor
        actual_distance = 0 * get_unit_registry().mm
        # Sum optical lengths of everything between start and end
        for item in path[start_index + 1 : -1]:
            item_ol = getattr(item, "optical_length", 0 * get_unit_registry().mm)
            if item_ol is not None:
                actual_distance += item_ol

        # 3. Add the output component's backfocus contribution (e.g. sensor depth)
        if hasattr(self.output, "backfocus") and self.output.backfocus is not None:
            actual_distance += self.output.backfocus

        return required_bf - actual_distance

    def get_image_orientation(self):
        from .opticalequipment.telescope import Telescope

        if not isinstance(self.telescope, Telescope):
            return (False, False)

        # Start with the telescope's inversion (1 horizontal + 1 vertical flip)
        flipped_horizontally = True
        flipped_vertically = True

        # Diagonals are typically used with Refractors and Catadioptrics,
        # and their effect depends on the telescope type.
        for diagonal in self.diagonals:
            if diagonal.is_erecting:
                # Erecting diagonal adds 1 horizontal and 1 vertical flip
                flipped_horizontally = not flipped_horizontally
                flipped_vertically = not flipped_vertically
            else:
                # Standard star diagonal adds 1 vertical flip
                flipped_vertically = not flipped_vertically

        return (flipped_horizontally, flipped_vertically)

    def pixel_scale(self) -> Any | None:
        from .opticalequipment.camera import Camera
        from .opticalequipment.smart_telescope import SmartTelescope

        if not isinstance(self.output, (Camera, SmartTelescope)):
            return None
        # Effective focal length
        eff_focal_length = self.telescope.focal_length * self.effective_barlow()
        # Pixel size
        p_size = self.output.pixel_size()
        # Formula: (p_size / eff_focal_length) * 206265
        scale = (
            p_size.to("mm").magnitude / eff_focal_length.to("mm").magnitude
        ) * 206265
        return scale * get_unit_registry().arcsecond

    def sampling(self, seeing: float) -> str | None:
        """
        Calculates the sampling status based on the resolution limit and the pixel scale.
        The resolution limit is the larger of the atmospheric seeing and the telescope's diffraction limit (Rayleigh limit).

        According to the Nyquist-Shannon sampling theorem, the ideal sampling (critical sampling)
        is at least 2 pixels per resolution element. In astrophotography, a ratio of 2.0 to 3.0
        is often considered ideal to capture all available detail without excessive oversampling.

        Thresholds:
        - Under-sampled: ratio < 1.0 (Information lost, stars look like squares)
        - Well-sampled: 1.0 <= ratio <= 3.0 (Good balance for most conditions)
        - Over-sampled: ratio > 3.0 (No extra detail gained, smaller field of view, lower SNR)

        Source: Nyquist-Shannon sampling theorem
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

    def sampling_status(self, seeing: float = 2.0) -> str | None:
        """
        Returns the sampling status as a string for a given seeing in arcseconds.
        """
        return self.sampling(seeing)

    def critical_focus_zone(self, wavelength=550):
        if not hasattr(self.telescope, "focal_ratio"):
            return None
        # wavelength in nm
        fr = (self.telescope.focal_ratio() * self.effective_barlow()).magnitude
        # CFZ = 2.44 * (wavelength/1000) * fr^2
        cfz = 2.44 * (wavelength / 1000.0) * (fr**2)
        return cfz * get_unit_registry().micrometer

    def thermal_drift(self, delta_t):
        if (
            not hasattr(self.telescope, "tube_material")
            or self.telescope.tube_material is None
        ):
            return None
        # delta_t in Celsius
        length = self.telescope.focal_length.to("mm").magnitude
        alpha = self.telescope.tube_material.value  # m/(m*K)
        drift = length * alpha * delta_t
        return drift * get_unit_registry().mm

    def sky_flux(self, sqm):
        from .opticalequipment.camera import Camera
        from .opticalequipment.smart_telescope import SmartTelescope

        scale = self.pixel_scale()
        if scale is None or not isinstance(self.output, (Camera, SmartTelescope)):
            return None
        if self.output.quantum_efficiency is None:
            return None

        area_cm2 = self.telescope.aperture_area().to("cm**2").magnitude
        qe = self.output.quantum_efficiency / 100.0

        # Account for filters transmission
        transmission = 1.0
        for f in self.filters:
            transmission *= f.transmission

        pixel_area_arcsec2 = scale.magnitude**2

        # Formula
        flux = (
            0.005
            * 10 ** (0.4 * (21.83 - sqm))
            * area_cm2
            * qe
            * transmission
            * pixel_area_arcsec2
        )
        return flux  # e-/s/pixel

    def object_flux(self, magnitude, altitude=None, extinction_k=0.2):
        from .opticalequipment.camera import Camera
        from .opticalequipment.smart_telescope import SmartTelescope

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
        qe = self.output.quantum_efficiency / 100.0

        # Account for filters transmission
        transmission = 1.0
        for f in self.filters:
            transmission *= f.transmission

        # Total flux from the object
        # Based on the same zero point as sky_flux
        flux = (
            0.005
            * 10 ** (0.4 * (21.83 - effective_magnitude))
            * area_cm2
            * qe
            * transmission
        )
        return flux  # e-/s total

    def snr(
        self,
        magnitude,
        sqm,
        exposure_time,
        n_subs=1,
        n_pix=4,
        altitude=None,
        extinction_k=0.2,
    ):
        from .opticalequipment.camera import Camera
        from .opticalequipment.smart_telescope import SmartTelescope

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

        # Total signal
        signal = obj_flux * exposure_time * n_subs

        # Noise components (squared)
        shot_noise_sq = obj_flux * exposure_time * n_subs
        sky_noise_sq = sky_flux_val * exposure_time * n_subs * n_pix
        read_noise_sq = (self.output.read_noise**2) * n_subs * n_pix

        total_noise = numpy.sqrt(shot_noise_sq + sky_noise_sq + read_noise_sq)

        if total_noise == 0:
            return 0.0

        return signal / total_noise

    def required_subs_for_snr(
        self,
        target_snr,
        magnitude,
        sqm,
        exposure_time,
        n_pix=4,
        altitude=None,
        extinction_k=0.2,
    ):
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
        target_snr,
        magnitude,
        sqm,
        exposure_time,
        n_pix=4,
        altitude=None,
        extinction_k=0.2,
    ):
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

    def optimum_sub_exposure(self, sqm):
        from .opticalequipment.camera import Camera
        from .opticalequipment.smart_telescope import SmartTelescope

        flux = self.sky_flux(sqm)
        if (
            flux is None
            or not isinstance(self.output, (Camera, SmartTelescope))
            or self.output.read_noise is None
        ):
            return None
        # Time where SkyNoise^2 = 10 * ReadNoise^2
        # SkyNoise^2 = Flux * Time
        # Time = 10 * ReadNoise^2 / Flux
        time = (10 * self.output.read_noise**2) / flux
        return time * get_unit_registry().second

    def camera_limiting_magnitude(
        self,
        sqm,
        total_integration_time,
        sub_exposure_time,
        target_snr=5.0,
        n_pix=4,
        altitude=None,
        extinction_k=0.2,
    ):
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

    def limiting_magnitude(self, sqm, integration_time):
        from .opticalequipment.camera import Camera
        from .opticalequipment.smart_telescope import SmartTelescope

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

    def npf_rule(self, declination: float = 0, k: float = 1.0) -> Any | None:
        """
        Calculates the maximum exposure time to avoid star trailing using the NPF rule.
        The NPF rule is more accurate than the 'Rule of 500' for modern high-resolution sensors.
        Formula: t = k * (35 * N + 30 * P) / (F * cos(declination))
        Where N is f-number, P is pixel pitch (microns), F is focal length (mm),
        and k is a tolerance factor (default 1.0 for pinpoint stars).
        Source: Frédéric Michaud
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

        if f == 0:
            return 0 * get_unit_registry().second

        cos_dec = numpy.cos(numpy.radians(declination))

        if numpy.abs(cos_dec) < 1e-10:
            # At the celestial poles, star movement is minimal.
            # We return a 1-hour cap (3600s) to avoid infinity.
            return 3600 * get_unit_registry().second

        t = k * (35 * n + 30 * p) / (f * cos_dec)
        return t * get_unit_registry().second

    def field_rotation_rate(
        self, latitude_deg: float, azimuth_deg: float, altitude_deg: float
    ) -> Any:
        """
        Calculates the field rotation rate for an Alt-Az mount in arcseconds per second.
        Formula: omega_rot = omega_earth * cos(lat) * cos(az) / cos(alt)
        Where omega_earth is the sidereal rotation rate (15.041067 "/s).
        Source: "Field Rotation" - Bill Keicher
        """
        # Sidereal rotation rate in arcseconds per second
        omega_earth = 15.041067

        phi = numpy.radians(latitude_deg)
        az = numpy.radians(azimuth_deg)
        alt = numpy.radians(
            min(altitude_deg, 89.99)
        )  # Avoid division by zero at zenith

        rate = omega_earth * numpy.cos(phi) * numpy.cos(az) / numpy.cos(alt)
        return abs(rate) * (get_unit_registry().arcsecond / get_unit_registry().second)

    def max_exposure_alt_az(
        self,
        latitude_deg: float,
        azimuth_deg: float,
        altitude_deg: float,
        tolerance_pixels: float = 1.0,
    ) -> Any | None:
        """
        Calculates the maximum exposure time for an Alt-Az mount to avoid field rotation trailing.
        The calculation is based on the movement of the furthest pixel from the sensor center (the corners).
        """
        from .opticalequipment.camera import Camera
        from .opticalequipment.smart_telescope import SmartTelescope

        if not isinstance(self.output, (Camera, SmartTelescope)):
            return None

        # Field rotation rate in arcsec/s
        rot_rate_q = self.field_rotation_rate(latitude_deg, azimuth_deg, altitude_deg)
        if rot_rate_q is None:
            return None
        rot_rate = rot_rate_q.to("arcsecond/second").magnitude

        if rot_rate < 1e-10:
            return 3600 * get_unit_registry().second

        # Pixel scale in arcsec/pixel
        p_scale = self.pixel_scale()
        if p_scale is None:
            return None

        # Distance from center to corner in pixels
        # r = sqrt((width/2)^2 + (height/2)^2)
        r = 0.5 * numpy.sqrt(self.output.width**2 + self.output.height**2)

        t = (tolerance_pixels * 206265.0) / (r * rot_rate)

        return t * get_unit_registry().second

    def dawes_limit(self) -> Any | None:
        """
        Calculates the Dawes' limit (resolving power) of the telescope in arcseconds.
        Based on the telescope aperture.
        """
        if hasattr(self.telescope, "dawes_limit"):
            return self.telescope.dawes_limit()
        return None

    def rayleigh_limit(self, wavelength_nm: float | int = 550) -> Any | None:
        """
        Calculates the Rayleigh limit (resolving power) of the telescope in arcseconds.
        Based on the telescope aperture and the provided wavelength (default 550nm).
        """
        if hasattr(self.telescope, "rayleigh_limit"):
            return self.telescope.rayleigh_limit(wavelength_nm=wavelength_nm)
        return None

    def ideal_planetary_focal_ratio(self, k: float = 5.0) -> float | None:
        """
        Calculates the ideal focal ratio for planetary imaging based on the pixel size.
        Rule of thumb: Ideal focal ratio is between 3x and 5x the pixel size in microns.
        Formula: Ideal Focal Ratio = k * Pixel Size (µm)
        Where k is usually 5.0 for average to good seeing.
        """
        from .opticalequipment.camera import Camera
        from .opticalequipment.smart_telescope import SmartTelescope

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
    ) -> float | None:
        """
        Calculates the ideal focal ratio for a given wavelength and sampling factor based on the Nyquist criterion.
        Formula: f/D = (p * s) / (1.22 * lambda)
        Where p is pixel size (µm), s is sampling factor, and lambda is wavelength (µm).
        A sampling factor of 2.0-3.0 is typically used for planetary imaging.
        Source: Nyquist-Shannon sampling theorem applied to diffraction-limited optics.
        """
        from .opticalequipment.camera import Camera
        from .opticalequipment.smart_telescope import SmartTelescope

        if not isinstance(self.output, (Camera, SmartTelescope)):
            return None

        p_size_q = self.output.pixel_size()
        if p_size_q is None:
            return None

        p_um = p_size_q.to("micrometer").magnitude
        lambda_um = wavelength_nm / 1000.0

        return (p_um * sampling_factor) / (1.22 * lambda_um)

    def planetary_size_in_pixels(self, planet_name: str, time: Any) -> float | None:
        """
        Calculates the projected size of a planet on the sensor in pixels.
        Uses the planet's angular diameter and the setup's pixel scale.
        """
        from .utils import planetary

        angular_diameter = planetary.get_planet_angular_diameter(planet_name, time)
        p_scale = self.pixel_scale()

        if p_scale is None or p_scale.magnitude == 0:
            return None

        return float(angular_diameter / p_scale.magnitude)

    def saturn_ring_size_in_pixels(self, time: Any) -> tuple[float, float] | None:
        """
        Calculates the projected size of Saturn's rings on the sensor in pixels.
        Returns a tuple (major_axis_pixels, minor_axis_pixels).
        """
        from .utils import planetary

        details = planetary.get_saturn_ring_details(time)
        p_scale = self.pixel_scale()

        if p_scale is None or p_scale.magnitude == 0:
            return None

        major = details["major_axis_arcsec"] / p_scale.magnitude
        minor = details["minor_axis_arcsec"] / p_scale.magnitude

        return float(major), float(minor)

    def rule_of_500(self):
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

        if hasattr(self.output, "sensor_width") and hasattr(
            self.output, "sensor_height"
        ):
            # crop_factor = 43.27 / diagonal
            # diagonal of 35mm sensor (36x24) is ~43.27mm
            diagonal = numpy.sqrt(
                self.output.sensor_width.to("mm").magnitude ** 2
                + self.output.sensor_height.to("mm").magnitude ** 2
            )
            if diagonal == 0:
                return (500 / f_actual) * get_unit_registry().second
            crop_factor = 43.27 / diagonal
            t = 500 / (f_actual * crop_factor)
        else:
            # Fallback for non-camera or visual setup (though less relevant)
            t = 500 / f_actual

        return t * get_unit_registry().second
