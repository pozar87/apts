from typing import ClassVar

from ...constants import GraphConstants, OpticalType
from ...i18n import gettext_ as _
from ...units import get_unit_registry
from ..base import OutputOpticalEquipment
from .calculations import (
    calculate_binoculars_brightness,
    calculate_binoculars_dawes_limit,
    calculate_binoculars_exit_pupil,
    calculate_binoculars_fov,
    calculate_binoculars_limiting_magnitude,
    calculate_binoculars_rayleigh_limit,
    normalize_binoculars_database_entry,
)


class Binoculars(OutputOpticalEquipment):
    """
    Class representing binoculars
    """

    path_layer = 1
    _DATABASE: ClassVar[dict] = {
        "Orion_GiantView_25x100_Binocular": {
            "brand": "Orion",
            "name": "GiantView 25x100 Binocular",
            "type": "type_telescope",
            "optical_length": 0,
            "mass": 2500,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": '2"',
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
    }

    @classmethod
    def normalize_database_entry(cls, entry: dict) -> dict:
        entry = normalize_binoculars_database_entry(entry)
        return super().normalize_database_entry(entry)

    @classmethod
    def from_database(cls, entry):
        entry = cls.normalize_database_entry(entry)
        vendor = entry.get("vendor", "")
        mass = entry.get("mass", 0)
        mag = entry.get("magnification", 10)
        obj = entry.get("objective_diameter", 50)
        apparent_fov = entry.get("apparent_fov_deg", 60)
        outputs = entry.get("outputs", [])

        return cls(mag, obj, vendor, apparent_fov, mass=mass, outputs=outputs)

    @classmethod
    def Orion_GiantView_25x100_Binocular(cls):
        return cls.from_database(cls._DATABASE["Orion_GiantView_25x100_Binocular"])

    def __init__(
        self,
        magnification,
        objective_diameter,
        vendor,
        apparent_fov_deg,
        focal_length=1,
        mass=0,
        outputs=None,
    ):
        # Call grandparent's init (OpticalEquipment)
        # We use a nominal focal_length (e.g., 1mm) because it's required by OpticalEquipment,
        # but not really used in the traditional sense for optical train calculations with binoculars.
        super().__init__(focal_length=focal_length, vendor=vendor, mass=mass, outputs=outputs)

        self.magnification = magnification
        self.objective_diameter = objective_diameter * get_unit_registry().mm
        self.apparent_fov_deg = apparent_fov_deg * get_unit_registry().deg
        self._type = OpticalType.BINOCULARS

    def get_name(self):
        return _("Binoculars")

    def __str__(self):
        # Format: <vendor> <magnification>x<objective_diameter>
        return f"{self.get_vendor()} {self.magnification}x{self.objective_diameter.to('mm').magnitude:.0f}"

    def field_of_view(self, telescope, zoom, barlow_magnification):
        return self.fov()

    def fov(self):
        afov_deg = self.apparent_fov_deg.to("deg").magnitude
        fov_deg = calculate_binoculars_fov(afov_deg, self.magnification)
        return fov_deg * get_unit_registry().deg

    def _zoom_divider(self):
        # For binoculars, the focal length is not typically used for zoom calculations.
        # But if compute_zoom is called, it returns telescope.focal_length * mag / output._zoom_divider().
        # For consistency, return a value that makes the math work, or just follow Eyepiece's pattern.
        return self.focal_length

    def exit_pupil(self, telescope=None, zoom=None):
        obj_mm = self.objective_diameter.to("mm").magnitude
        exit_pupil_mm = calculate_binoculars_exit_pupil(obj_mm, self.magnification)
        return exit_pupil_mm * get_unit_registry().mm

    def dawes_limit(self):
        """
        Calculate the maximum resolving power using the Dawes' Limit formula.
        :return: limit in arcsecond
        """
        obj_cm = self.objective_diameter.to("cm").magnitude
        limit_arcsec = calculate_binoculars_dawes_limit(obj_cm)
        return limit_arcsec * get_unit_registry().arcsecond

    def rayleigh_limit(self, wavelength_nm: float = 550):
        """
        Calculate the maximum resolving power using the Rayleigh Limit formula.
        θ = 1.22 * λ / D
        Where λ is the wavelength and D is the aperture (objective diameter).
        https://en.wikipedia.org/wiki/Angular_resolution
        :param wavelength_nm: wavelength in nanometers (default 550nm for green light)
        :return: limit in arcsecond
        """
        obj_m = self.objective_diameter.to("m").magnitude
        limit_arcsec = calculate_binoculars_rayleigh_limit(
            obj_m, wavelength_nm=wavelength_nm
        )
        return limit_arcsec * get_unit_registry().arcsecond

    def limiting_magnitude(self):
        """
        Calculate approximate limiting magnitude.
        :return: range in magnitude
        """
        obj_cm = self.objective_diameter.to("cm").magnitude
        return calculate_binoculars_limiting_magnitude(obj_cm)

    def brightness(self, telescope=None, zoom=None):
        exit_pupil_mm = self.exit_pupil().to("mm").magnitude
        return calculate_binoculars_brightness(exit_pupil_mm)

    def register(self, equipment):
        """
        Register binoculars in the optical equipment graph.
        Binoculars connect directly from SPACE to EYE.
        """
        # Add binocular node
        super()._register(equipment)
        # Connect binocular node to space node
        equipment.add_edge(GraphConstants.SPACE_ID, self.id())
        # Connect binocular node to eye node
        equipment.add_edge(self.id(), GraphConstants.EYE_ID)

    def output_type(self):
        # Describes the type of view produced, similar to Eyepiece or Camera
        return OpticalType.VISUAL

    def max_useful_zoom(self):
        # For binoculars, their own magnification is effectively the max useful zoom
        return self.magnification
