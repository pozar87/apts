from ..constants import OpticalType, GraphConstants
from ..i18n import gettext_ as _
from ..units import get_unit_registry
from .abstract import OpticalEquipment


class Binoculars(OpticalEquipment):
    @classmethod
    def from_database(cls, entry):
        from ..utils import Utils

        brand = entry["brand"]
        name = entry["name"]
        vendor = f"{brand} {name}"
        mass = entry.get("mass", 0)
        mag = Utils.extract_number(name) or 10
        obj = Utils.extract_number(name, prefix=f"{int(mag)}x") or 50
        return cls(mag, obj, vendor, 60, mass=mass)

    """
    Class representing binoculars
    """

    def __init__(
        self,
        magnification,
        objective_diameter,
        vendor,
        apparent_fov_deg,
        focal_length=1,
        mass=0,
    ):
        # Call grandparent's init (OpticalEquipment)
        # We use a nominal focal_length (e.g., 1mm) because it's required by OpticalEquipment,
        # but not really used in the traditional sense for optical train calculations with binoculars.
        super().__init__(focal_length=focal_length, vendor=vendor, mass=mass)

        self.magnification = magnification
        self.objective_diameter = objective_diameter * get_unit_registry().mm
        self.apparent_fov_deg = apparent_fov_deg * get_unit_registry().deg
        self._type = OpticalType.BINOCULARS

    def get_name(self):
        return _("Binoculars")

    def __str__(self):
        # Format: <vendor> <magnification>x<objective_diameter>
        return f"{self.get_vendor()} {self.magnification}x{self.objective_diameter.to('mm').magnitude:.0f}"

    def fov(self):
        # True Field of View = Apparent FOV / Magnification
        return self.apparent_fov_deg / self.magnification

    def exit_pupil(self):
        return self.objective_diameter / self.magnification

    def dawes_limit(self):
        """
        Calculate the maximum resolving power using the Dawes' Limit formula.
        :return: limit in arcsecond
        """
        return (
            round((11.6 / self.objective_diameter.to("cm")).magnitude, 3)
            * get_unit_registry().arcsecond
        )

    def rayleigh_limit(self):
        """
        Calculate the maximum resolving power using the Rayleigh Limit formula.
        :return: limit in arcsecond
        """
        return (
            round((13.8 / self.objective_diameter.to("cm")).magnitude, 3)
            * get_unit_registry().arcsecond
        )

    def limiting_magnitude(self):
        """
        Calculate approximate limiting magnitude.
        :return: range in magnitude
        """
        # Using the same formula as Telescope, based on aperture (objective_diameter for binoculars)
        import numpy

        return 7.7 + 5 * numpy.log10(self.objective_diameter.to("cm").magnitude)

    def brightness(self):
        # Relative brightness: (Exit Pupil (mm) / 7mm)^2 * 100
        # Assuming 7mm is the max human eye pupil diameter
        return (self.exit_pupil().to("mm").magnitude / 7) ** 2 * 100

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

    _DATABASE = {
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
    def Orion_GiantView_25x100_Binocular(cls):
        return cls.from_database(cls._DATABASE["Orion_GiantView_25x100_Binocular"])
