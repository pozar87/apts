import functools
import operator
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
        from .opticalequipment.smart_telescope import SmartTelescope

        # First item in the path should be the telescope or binoculars
        main_optic = path[0]
        if isinstance(main_optic, (Binoculars, NakedEye, SmartTelescope)):
            # Treat binoculars as the 'output' as well for path structure consistency
            return (main_optic, [], [], [], main_optic)

        # Original logic for telescopes
        telescope = main_optic
        # Last item in the path is output
        output = path[-1]
        # Intermediate elements
        intermediate = path[1:-1]
        barlows = [item for item in intermediate if isinstance(item, Barlow)]
        diagonals = [item for item in intermediate if isinstance(item, Diagonal)]
        filters = [item for item in intermediate if isinstance(item, Filter)]
        return (telescope, barlows, diagonals, filters, output)

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

    def __init__(self, telescope, barlows, diagonals, filters, output):
        self.telescope = telescope
        self.barlows = barlows
        self.diagonals = diagonals
        self.filters = filters
        self.output = output

    @classmethod
    def from_path(cls, path):
        telescope, barlows, diagonals, filters, output = OpticsUtils.expand(path)
        return cls(telescope, barlows, diagonals, filters, output)

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
            + [str(self.output)]
        )

    def length(self):
        from .opticalequipment.smart_telescope import SmartTelescope

        # For binoculars, path is [Binoculars], expanded to (Binoculars, [], Binoculars)
        # So self.barlows is []. Length should be 1 for a direct binocular path.
        # Original: return 2 + len(self.barlows) (Telescope + Output + Barlows)
        if isinstance(self.telescope, (Binoculars, NakedEye, SmartTelescope)):
            return 1  # Just the binoculars itself
        return 2 + len(self.barlows) + len(self.diagonals) + len(self.filters)

    def fov(self):
        return OpticsUtils.compute_field_of_view(
            self.telescope, self.barlows, self.output
        )

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
        return frozenset(elements)

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

    def pixel_scale(self):
        from .opticalequipment.camera import Camera

        if not isinstance(self.output, Camera):
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

    def sampling(self, seeing):
        scale = self.pixel_scale()
        if scale is None:
            return None
        ratio = seeing / scale.magnitude
        if ratio < 1.0:
            return "Under-sampled"
        elif ratio <= 2.0:
            return "Well-sampled"
        else:
            return "Over-sampled"

    def sampling_status(self, seeing=2.0):
        """
        Returns the sampling status as a string for a given seeing in arcseconds.
        """
        return self.sampling(seeing)

    def critical_focus_zone(self, wavelength=550):
        # wavelength in nm
        fr = self.telescope.focal_ratio() * self.effective_barlow()
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

        scale = self.pixel_scale()
        if scale is None or not isinstance(self.output, Camera):
            return None
        if self.output.quantum_efficiency is None:
            return None

        area_cm2 = self.telescope.aperture_area().to("cm**2").magnitude
        qe = self.output.quantum_efficiency / 100.0
        pixel_area_arcsec2 = scale.magnitude**2

        # Formula
        flux = 0.005 * 10 ** (0.4 * (21.83 - sqm)) * area_cm2 * qe * pixel_area_arcsec2
        return flux  # e-/s/pixel

    def optimum_sub_exposure(self, sqm):
        from .opticalequipment.camera import Camera

        flux = self.sky_flux(sqm)
        if (
            flux is None
            or not isinstance(self.output, Camera)
            or self.output.read_noise is None
        ):
            return None
        # Time where SkyNoise^2 = 10 * ReadNoise^2
        # SkyNoise^2 = Flux * Time
        # Time = 10 * ReadNoise^2 / Flux
        time = (10 * self.output.read_noise**2) / flux
        return time * get_unit_registry().second

    def limiting_magnitude(self, sqm, integration_time):
        from .opticalequipment.camera import Camera

        # integration_time in seconds
        if not isinstance(self.output, Camera) or self.output.quantum_efficiency is None:
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

    def npf_rule(self, declination=0):
        """
        Calculates the maximum exposure time to avoid star trailing using the NPF rule.
        The NPF rule is more accurate than the 'Rule of 500' for modern high-resolution sensors.
        Formula: t = (35 * N + 30 * P) / (F * cos(declination))
        Where N is f-number, P is pixel pitch (microns), F is focal length (mm).
        Source: Frédéric Michaud
        """
        if not hasattr(self.output, "pixel_size") or not hasattr(
            self.telescope, "focal_ratio"
        ):
            return None

        # F-number (N)
        n = (self.telescope.focal_ratio() * self.effective_barlow()).magnitude
        # Pixel pitch in microns (P)
        p = self.output.pixel_size().to("micrometer").magnitude
        # Focal length in mm (F)
        f = (self.telescope.focal_length * self.effective_barlow()).to("mm").magnitude

        if f == 0:
            return 0 * get_unit_registry().second

        cos_dec = numpy.cos(numpy.radians(declination))

        t = (35 * n + 30 * p) / (f * cos_dec)
        return t * get_unit_registry().second

    def rule_of_500(self):
        """
        Calculates the maximum exposure time to avoid star trailing using the classic Rule of 500.
        Formula: t = 500 / (F_actual * crop_factor)
        """
        # Actual focal length
        f_actual = (
            self.telescope.focal_length * self.effective_barlow()
        ).to("mm").magnitude

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
