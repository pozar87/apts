import numpy

from .abstract import OpticalEquipment
from ..units import get_unit_registry
from ..utils import ConnectionType, Gender
from ..constants import GraphConstants


from enum import Enum
from typing import Optional


class TelescopeType(Enum):
    REFRACTOR = "refractor"
    NEWTONIAN_REFLECTOR = "newtonian_reflector"
    SCHMIDT_CASSEGRAIN = "schmidt_cassegrain"
    MAKSTUTOV_CASSEGRAIN = "makstutov_cassegrain"
    CATADIOPTRIC = "catadioptric"


class TubeMaterial(Enum):
    ALUMINUM = 23.1e-6
    CARBON_FIBER = 0.5e-6
    STEEL = 12.0e-6
    BRASS = 19.0e-6
    GLASS_FIBER = 8.0e-6


class Telescope(OpticalEquipment):
    @classmethod
    def from_database(cls, entry):
        from ..utils import Utils, Gender

        brand = entry["brand"]
        name = entry["name"]
        vendor = f"{brand} {name}"
        ol = entry.get("optical_length", 0)
        mass = entry.get("mass", 0)
        ct = Utils.map_conn(entry.get("cside_thread"))
        cg = Utils.map_gender(entry.get("cside_gender"))
        aperture, focal_length = Utils.guess_optical_properties(name)
        bf_val = entry.get("bf_role") == "start"
        return cls(
            aperture or 80,
            focal_length or 500,
            vendor=vendor,
            connection_type=ct,
            connection_gender=cg or Gender.FEMALE,
            backfocus=ol if bf_val else None,
            mass=mass,
            optical_length=ol,
        )

    """
    Class representing telescope
    """

    def __init__(
        self,
        aperture,
        focal_length,
        vendor="unknown telescope",
        connection_type=ConnectionType.F_1_25,
        t2_output=False,
        telescope_type: Optional[TelescopeType] = TelescopeType.REFRACTOR,
        focuser_step_size=None,
        tube_material: Optional[TubeMaterial] = TubeMaterial.ALUMINUM,
        backfocus=None,
        mass=0,
        optical_length=0,
        connection_gender=Gender.FEMALE,
        central_obstruction=0,
    ):
        super(Telescope, self).__init__(
            focal_length, vendor, mass=mass, optical_length=optical_length
        )
        self.aperture = aperture * get_unit_registry().mm
        self.central_obstruction = central_obstruction * get_unit_registry().mm
        self.connection_type = connection_type
        self.connection_gender = connection_gender
        self.t2_output = t2_output
        self.telescope_type = telescope_type
        self.focuser_step_size = focuser_step_size
        self.tube_material = tube_material
        self.backfocus = (
            backfocus * get_unit_registry().mm if backfocus is not None else None
        )

    def focal_ratio(self):
        return self.focal_length / self.aperture

    def aperture_area(self):
        """
        Calculate the light gathering area of the telescope, accounting for central obstruction.
        :return: area in mm^2
        """
        return numpy.pi * (self.aperture**2 - self.central_obstruction**2) / 4.0

    def effective_aperture(self):
        """
        Return the diameter of a clear aperture that would have the same light-gathering area.
        :return: effective aperture in mm
        """
        return numpy.sqrt(self.aperture**2 - self.central_obstruction**2)

    def dawes_limit(self):
        """
        Calculate the maximum resolving power of your telescope using the Dawes' Limit formula.
        https://en.wikipedia.org/wiki/Dawes%27_limit
        :return: limit in arcsecond
        """
        return (
            round((11.6 / self.aperture.to("cm")).magnitude, 3)
            * get_unit_registry().arcsecond
        )

    def rayleigh_limit(self):
        """
        Calculate the maximum resolving power of your telescope using the Rayleigh Limit formula.
        https://en.wikipedia.org/wiki/Angular_resolution
        :return: limit in arcsecond
        """
        return (
            round((13.8 / self.aperture.to("cm")).magnitude, 3)
            * get_unit_registry().arcsecond
        )

    def limiting_magnitude(self):
        """
        Calculate a telescopes approximate limiting magnitude.
        Uses effective aperture diameter for better accuracy when central obstruction is present.
        :return: range in magnitude
        """
        return 7.7 + 5 * numpy.log10(self.effective_aperture().to("cm").magnitude)

    def light_grasp_ratio(self, other_aperture):
        """
        Calculate the light grasp ratio between two telescopes.
        Uses effective aperture area for better accuracy when central obstruction is present.
        :param other_aperture: aperture in mm
        :return: ratio between telescope and other aperture
        """
        other_aperture *= get_unit_registry().mm
        return self.effective_aperture() ** 2 / other_aperture**2

    def min_useful_zoom(self):
        return self.aperture.magnitude / 6

    def max_useful_zoom(self):
        return self.aperture.magnitude * 2.5

    def register(self, equipment):
        """
        Register telescope in optical equipment graph. Telescope node is build out of two vertices:
        telescope node and its output. Telescope node is automatically connected with SPACE node.
        """
        # Add telescope node
        super(Telescope, self)._register(equipment)
        # Add telescope output node and connect it to telescope
        self._register_output(equipment, self.connection_type, self.connection_gender)
        # Connect telescope node to space node
        equipment.add_edge(GraphConstants.SPACE_ID, self.id())
        # Handling optional T2 output
        if self.t2_output:
            self._register_output(equipment, ConnectionType.T2)

    def __str__(self):
        # Format: <vendor> <aperture>/<focal length>
        return "{} {}/{}".format(
            self.get_vendor(),
            self.aperture.magnitude,
            self.focal_length.magnitude,
        )

    _DATABASE = {
        "Celestron_C5_SCT": {
            "brand": "Celestron",
            "name": "C5 SCT",
            "type": "type_telescope",
            "optical_length": 0,
            "mass": 2700,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "SC (Schmidt-Cassegrain)",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Celestron_C6_SCT": {
            "brand": "Celestron",
            "name": "C6 SCT",
            "type": "type_telescope",
            "optical_length": 0,
            "mass": 4000,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "SC (Schmidt-Cassegrain)",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Celestron_C8_SCT": {
            "brand": "Celestron",
            "name": "C8 SCT",
            "type": "type_telescope",
            "optical_length": 0,
            "mass": 5670,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "SC (Schmidt-Cassegrain)",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Celestron_C9_25_SCT": {
            "brand": "Celestron",
            "name": "C9.25 SCT",
            "type": "type_telescope",
            "optical_length": 0,
            "mass": 9500,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "SC (Schmidt-Cassegrain)",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Celestron_C11_SCT": {
            "brand": "Celestron",
            "name": "C11 SCT",
            "type": "type_telescope",
            "optical_length": 0,
            "mass": 12500,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "SC (Schmidt-Cassegrain)",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Celestron_C14_SCT": {
            "brand": "Celestron",
            "name": "C14 SCT",
            "type": "type_telescope",
            "optical_length": 0,
            "mass": 20400,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "SC (Schmidt-Cassegrain)",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Celestron_C6_EdgeHD": {
            "brand": "Celestron",
            "name": "C6 EdgeHD",
            "type": "type_telescope",
            "optical_length": 0,
            "mass": 3800,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "SC (Schmidt-Cassegrain)",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Celestron_C8_EdgeHD": {
            "brand": "Celestron",
            "name": "C8 EdgeHD",
            "type": "type_telescope",
            "optical_length": 0,
            "mass": 5900,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "SC (Schmidt-Cassegrain)",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Celestron_C9_25_EdgeHD": {
            "brand": "Celestron",
            "name": "C9.25 EdgeHD",
            "type": "type_telescope",
            "optical_length": 0,
            "mass": 9800,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "SC (Schmidt-Cassegrain)",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Celestron_C11_EdgeHD": {
            "brand": "Celestron",
            "name": "C11 EdgeHD",
            "type": "type_telescope",
            "optical_length": 0,
            "mass": 12700,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "SC (Schmidt-Cassegrain)",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Celestron_C14_EdgeHD": {
            "brand": "Celestron",
            "name": "C14 EdgeHD",
            "type": "type_telescope",
            "optical_length": 0,
            "mass": 20500,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "SC (Schmidt-Cassegrain)",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Celestron_NexStar_4SE": {
            "brand": "Celestron",
            "name": "NexStar 4SE",
            "type": "type_telescope",
            "optical_length": 0,
            "mass": 3000,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "SC (Schmidt-Cassegrain)",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Celestron_NexStar_5SE": {
            "brand": "Celestron",
            "name": "NexStar 5SE",
            "type": "type_telescope",
            "optical_length": 0,
            "mass": 2800,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "SC (Schmidt-Cassegrain)",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Celestron_NexStar_6SE": {
            "brand": "Celestron",
            "name": "NexStar 6SE",
            "type": "type_telescope",
            "optical_length": 0,
            "mass": 2950,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "SC (Schmidt-Cassegrain)",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Celestron_NexStar_8SE": {
            "brand": "Celestron",
            "name": "NexStar 8SE",
            "type": "type_telescope",
            "optical_length": 0,
            "mass": 5400,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "SC (Schmidt-Cassegrain)",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Celestron_NexStar_Evolution_6": {
            "brand": "Celestron",
            "name": "NexStar Evolution 6",
            "type": "type_telescope",
            "optical_length": 0,
            "mass": 4500,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "SC (Schmidt-Cassegrain)",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Celestron_NexStar_Evolution_8": {
            "brand": "Celestron",
            "name": "NexStar Evolution 8",
            "type": "type_telescope",
            "optical_length": 0,
            "mass": 6000,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "SC (Schmidt-Cassegrain)",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Celestron_CGX_L_1100_SCT": {
            "brand": "Celestron",
            "name": "CGX-L 1100 SCT",
            "type": "type_telescope",
            "optical_length": 0,
            "mass": 12700,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "SC (Schmidt-Cassegrain)",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Celestron_CGX_L_1400_SCT": {
            "brand": "Celestron",
            "name": "CGX-L 1400 SCT",
            "type": "type_telescope",
            "optical_length": 0,
            "mass": 20500,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "SC (Schmidt-Cassegrain)",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Celestron_Advanced_VX_8_SCT": {
            "brand": "Celestron",
            "name": "Advanced VX 8 SCT",
            "type": "type_telescope",
            "optical_length": 0,
            "mass": 5800,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "SC (Schmidt-Cassegrain)",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Celestron_CPC_800": {
            "brand": "Celestron",
            "name": "CPC 800",
            "type": "type_telescope",
            "optical_length": 0,
            "mass": 5700,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "SC (Schmidt-Cassegrain)",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Celestron_CPC_1100": {
            "brand": "Celestron",
            "name": "CPC 1100",
            "type": "type_telescope",
            "optical_length": 0,
            "mass": 12600,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "SC (Schmidt-Cassegrain)",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Celestron_CPC_Deluxe_1100_EdgeHD": {
            "brand": "Celestron",
            "name": "CPC Deluxe 1100 EdgeHD",
            "type": "type_telescope",
            "optical_length": 0,
            "mass": 13000,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "SC (Schmidt-Cassegrain)",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Celestron_RASA_8": {
            "brand": "Celestron",
            "name": 'RASA 8"',
            "type": "type_telescope",
            "optical_length": 0,
            "mass": 5200,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "M48",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Celestron_RASA_11": {
            "brand": "Celestron",
            "name": 'RASA 11"',
            "type": "type_telescope",
            "optical_length": 0,
            "mass": 12500,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "M48",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Celestron_RASA_14": {
            "brand": "Celestron",
            "name": 'RASA 14"',
            "type": "type_telescope",
            "optical_length": 0,
            "mass": 22000,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "M48",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Celestron_RASA_36cm": {
            "brand": "Celestron",
            "name": "RASA 36cm",
            "type": "type_telescope",
            "optical_length": 0,
            "mass": 30000,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "M48",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Sky_Watcher_Esprit_80ED": {
            "brand": "Sky-Watcher",
            "name": "Esprit 80ED",
            "type": "type_refractor",
            "optical_length": 0,
            "mass": 4000,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "M48",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Sky_Watcher_Esprit_100ED": {
            "brand": "Sky-Watcher",
            "name": "Esprit 100ED",
            "type": "type_refractor",
            "optical_length": 0,
            "mass": 5400,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "M48",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Sky_Watcher_Esprit_120ED": {
            "brand": "Sky-Watcher",
            "name": "Esprit 120ED",
            "type": "type_refractor",
            "optical_length": 0,
            "mass": 7800,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "M48",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Sky_Watcher_Esprit_150ED": {
            "brand": "Sky-Watcher",
            "name": "Esprit 150ED",
            "type": "type_refractor",
            "optical_length": 0,
            "mass": 12000,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "M54",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Sky_Watcher_Evostar_72ED": {
            "brand": "Sky-Watcher",
            "name": "Evostar 72ED",
            "type": "type_refractor",
            "optical_length": 0,
            "mass": 1900,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "M48",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Sky_Watcher_Evostar_80ED": {
            "brand": "Sky-Watcher",
            "name": "Evostar 80ED",
            "type": "type_refractor",
            "optical_length": 0,
            "mass": 2500,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "M48",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Sky_Watcher_Evostar_100ED": {
            "brand": "Sky-Watcher",
            "name": "Evostar 100ED",
            "type": "type_refractor",
            "optical_length": 0,
            "mass": 4200,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "M48",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Sky_Watcher_Evostar_120ED": {
            "brand": "Sky-Watcher",
            "name": "Evostar 120ED",
            "type": "type_refractor",
            "optical_length": 0,
            "mass": 5400,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "M48",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Sky_Watcher_Evostar_72ED_DS_Pro": {
            "brand": "Sky-Watcher",
            "name": "Evostar 72ED DS-Pro",
            "type": "type_refractor",
            "optical_length": 0,
            "mass": 2200,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "M48",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Sky_Watcher_Evostar_80ED_DS_Pro": {
            "brand": "Sky-Watcher",
            "name": "Evostar 80ED DS-Pro",
            "type": "type_refractor",
            "optical_length": 0,
            "mass": 2800,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "M48",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Sky_Watcher_Evostar_100ED_DS_Pro": {
            "brand": "Sky-Watcher",
            "name": "Evostar 100ED DS-Pro",
            "type": "type_refractor",
            "optical_length": 0,
            "mass": 4500,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "M48",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Sky_Watcher_Evostar_150ED": {
            "brand": "Sky-Watcher",
            "name": "Evostar 150ED",
            "type": "type_refractor",
            "optical_length": 0,
            "mass": 8000,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "M54",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Sky_Watcher_Quattro_150P": {
            "brand": "Sky-Watcher",
            "name": "Quattro 150P",
            "type": "type_telescope",
            "optical_length": 0,
            "mass": 5000,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "M48",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Sky_Watcher_Quattro_200P": {
            "brand": "Sky-Watcher",
            "name": "Quattro 200P",
            "type": "type_telescope",
            "optical_length": 0,
            "mass": 8000,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "M48",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Sky_Watcher_Quattro_250P": {
            "brand": "Sky-Watcher",
            "name": "Quattro 250P",
            "type": "type_telescope",
            "optical_length": 0,
            "mass": 12000,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "M48",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Sky_Watcher_Quattro_300P": {
            "brand": "Sky-Watcher",
            "name": "Quattro 300P",
            "type": "type_telescope",
            "optical_length": 0,
            "mass": 16000,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "M48",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Sky_Watcher_150PDS_Newtonian": {
            "brand": "Sky-Watcher",
            "name": "150PDS Newtonian",
            "type": "type_telescope",
            "optical_length": 0,
            "mass": 4800,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": '2"',
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Sky_Watcher_200PDS_Newtonian": {
            "brand": "Sky-Watcher",
            "name": "200PDS Newtonian",
            "type": "type_telescope",
            "optical_length": 0,
            "mass": 8800,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": '2"',
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Sky_Watcher_250PDS_Newtonian": {
            "brand": "Sky-Watcher",
            "name": "250PDS Newtonian",
            "type": "type_telescope",
            "optical_length": 0,
            "mass": 11500,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": '2"',
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Sky_Watcher_Explorer_130P": {
            "brand": "Sky-Watcher",
            "name": "Explorer 130P",
            "type": "type_telescope",
            "optical_length": 0,
            "mass": 3200,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": '2"',
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Sky_Watcher_Explorer_150P": {
            "brand": "Sky-Watcher",
            "name": "Explorer 150P",
            "type": "type_telescope",
            "optical_length": 0,
            "mass": 5200,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": '2"',
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Sky_Watcher_Explorer_200P": {
            "brand": "Sky-Watcher",
            "name": "Explorer 200P",
            "type": "type_telescope",
            "optical_length": 0,
            "mass": 8500,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": '2"',
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Sky_Watcher_Explorer_250P": {
            "brand": "Sky-Watcher",
            "name": "Explorer 250P",
            "type": "type_telescope",
            "optical_length": 0,
            "mass": 11000,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": '2"',
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Sky_Watcher_Explorer_300P": {
            "brand": "Sky-Watcher",
            "name": "Explorer 300P",
            "type": "type_telescope",
            "optical_length": 0,
            "mass": 16000,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": '2"',
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Sky_Watcher_Skyliner_150P": {
            "brand": "Sky-Watcher",
            "name": "Skyliner 150P",
            "type": "type_telescope",
            "optical_length": 0,
            "mass": 5000,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": '2"',
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Sky_Watcher_Skyliner_200P": {
            "brand": "Sky-Watcher",
            "name": "Skyliner 200P",
            "type": "type_telescope",
            "optical_length": 0,
            "mass": 8500,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": '2"',
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Sky_Watcher_Skyliner_250P": {
            "brand": "Sky-Watcher",
            "name": "Skyliner 250P",
            "type": "type_telescope",
            "optical_length": 0,
            "mass": 11600,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": '2"',
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Sky_Watcher_Skyliner_300P": {
            "brand": "Sky-Watcher",
            "name": "Skyliner 300P",
            "type": "type_telescope",
            "optical_length": 0,
            "mass": 16000,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": '2"',
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Sky_Watcher_Skyliner_400P": {
            "brand": "Sky-Watcher",
            "name": "Skyliner 400P",
            "type": "type_telescope",
            "optical_length": 0,
            "mass": 25000,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": '2"',
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Sky_Watcher_Heritage_130P": {
            "brand": "Sky-Watcher",
            "name": "Heritage 130P",
            "type": "type_telescope",
            "optical_length": 0,
            "mass": 3000,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": '2"',
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Sky_Watcher_Heritage_150P": {
            "brand": "Sky-Watcher",
            "name": "Heritage 150P",
            "type": "type_telescope",
            "optical_length": 0,
            "mass": 4500,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": '2"',
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Sky_Watcher_Mak_90": {
            "brand": "Sky-Watcher",
            "name": "Mak-90",
            "type": "type_telescope",
            "optical_length": 0,
            "mass": 1600,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": '1.25"',
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Sky_Watcher_Mak_102": {
            "brand": "Sky-Watcher",
            "name": "Mak-102",
            "type": "type_telescope",
            "optical_length": 0,
            "mass": 2000,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": '1.25"',
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Sky_Watcher_Mak_127": {
            "brand": "Sky-Watcher",
            "name": "Mak-127",
            "type": "type_telescope",
            "optical_length": 0,
            "mass": 3500,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": '1.25"',
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Sky_Watcher_Mak_150": {
            "brand": "Sky-Watcher",
            "name": "Mak-150",
            "type": "type_telescope",
            "optical_length": 0,
            "mass": 5000,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": '2"',
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Sky_Watcher_Mak_180": {
            "brand": "Sky-Watcher",
            "name": "Mak-180",
            "type": "type_telescope",
            "optical_length": 0,
            "mass": 6300,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": '2"',
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Takahashi_FSQ_85EDP": {
            "brand": "Takahashi",
            "name": "FSQ-85EDP",
            "type": "type_refractor",
            "optical_length": 0,
            "mass": 3100,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "M82",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Takahashi_FSQ_106ED": {
            "brand": "Takahashi",
            "name": "FSQ-106ED",
            "type": "type_refractor",
            "optical_length": 0,
            "mass": 6200,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "M82",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Takahashi_FSQ_130ED": {
            "brand": "Takahashi",
            "name": "FSQ-130ED",
            "type": "type_refractor",
            "optical_length": 0,
            "mass": 9000,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "M82",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Takahashi_FC_76DCU": {
            "brand": "Takahashi",
            "name": "FC-76DCU",
            "type": "type_refractor",
            "optical_length": 0,
            "mass": 2600,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "M54",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Takahashi_FC_100DC": {
            "brand": "Takahashi",
            "name": "FC-100DC",
            "type": "type_refractor",
            "optical_length": 0,
            "mass": 3500,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "M54",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Takahashi_FC_100DZ": {
            "brand": "Takahashi",
            "name": "FC-100DZ",
            "type": "type_refractor",
            "optical_length": 0,
            "mass": 3800,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "M54",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Takahashi_FC_100DF": {
            "brand": "Takahashi",
            "name": "FC-100DF",
            "type": "type_refractor",
            "optical_length": 0,
            "mass": 3800,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "M54",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Takahashi_FS_60CB": {
            "brand": "Takahashi",
            "name": "FS-60CB",
            "type": "type_refractor",
            "optical_length": 0,
            "mass": 1400,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "M42",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Takahashi_FS_60Q": {
            "brand": "Takahashi",
            "name": "FS-60Q",
            "type": "type_refractor",
            "optical_length": 0,
            "mass": 1600,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "M42",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Takahashi_TSA_120": {
            "brand": "Takahashi",
            "name": "TSA-120",
            "type": "type_refractor",
            "optical_length": 0,
            "mass": 5200,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "M72",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Takahashi_TOA_130NFB": {
            "brand": "Takahashi",
            "name": "TOA-130NFB",
            "type": "type_refractor",
            "optical_length": 0,
            "mass": 7200,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "M92",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Takahashi_TOA_150": {
            "brand": "Takahashi",
            "name": "TOA-150",
            "type": "type_refractor",
            "optical_length": 0,
            "mass": 12000,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "M92",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Takahashi_Sky_90": {
            "brand": "Takahashi",
            "name": "Sky-90",
            "type": "type_refractor",
            "optical_length": 0,
            "mass": 2000,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "M54",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Takahashi_FOA_60": {
            "brand": "Takahashi",
            "name": "FOA-60",
            "type": "type_refractor",
            "optical_length": 0,
            "mass": 1200,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "M42",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Takahashi_FOA_60Q": {
            "brand": "Takahashi",
            "name": "FOA-60Q",
            "type": "type_refractor",
            "optical_length": 0,
            "mass": 1300,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "M42",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Takahashi_FS_60CP": {
            "brand": "Takahashi",
            "name": "FS-60CP",
            "type": "type_refractor",
            "optical_length": 0,
            "mass": 1400,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "M42",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Takahashi_FC_76DS": {
            "brand": "Takahashi",
            "name": "FC-76DS",
            "type": "type_refractor",
            "optical_length": 0,
            "mass": 2600,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "M54",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Takahashi_FC_76DC": {
            "brand": "Takahashi",
            "name": "FC-76DC",
            "type": "type_refractor",
            "optical_length": 0,
            "mass": 2500,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "M54",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Takahashi_TSA_102": {
            "brand": "Takahashi",
            "name": "TSA-102",
            "type": "type_refractor",
            "optical_length": 0,
            "mass": 4200,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "M72",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Takahashi_TOA_130S": {
            "brand": "Takahashi",
            "name": "TOA-130S",
            "type": "type_refractor",
            "optical_length": 0,
            "mass": 6800,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "M72",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Takahashi_FCT_65": {
            "brand": "Takahashi",
            "name": "FCT-65",
            "type": "type_refractor",
            "optical_length": 0,
            "mass": 1800,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "M42",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Takahashi_Epsilon_130D": {
            "brand": "Takahashi",
            "name": "Epsilon-130D",
            "type": "type_telescope",
            "optical_length": 0,
            "mass": 5500,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "M54",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Takahashi_Epsilon_180ED": {
            "brand": "Takahashi",
            "name": "Epsilon-180ED",
            "type": "type_telescope",
            "optical_length": 0,
            "mass": 9200,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "M82",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Takahashi_Epsilon_200": {
            "brand": "Takahashi",
            "name": "Epsilon-200",
            "type": "type_telescope",
            "optical_length": 0,
            "mass": 8000,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "M82",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Takahashi_CCA_250": {
            "brand": "Takahashi",
            "name": "CCA-250",
            "type": "type_telescope",
            "optical_length": 0,
            "mass": 16000,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "M92",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Takahashi_BRC_250": {
            "brand": "Takahashi",
            "name": "BRC-250",
            "type": "type_telescope",
            "optical_length": 0,
            "mass": 14000,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "M82",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Takahashi_Mewlon_180C": {
            "brand": "Takahashi",
            "name": "Mewlon-180C",
            "type": "type_telescope",
            "optical_length": 0,
            "mass": 6300,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "M72",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Takahashi_Mewlon_210": {
            "brand": "Takahashi",
            "name": "Mewlon-210",
            "type": "type_telescope",
            "optical_length": 0,
            "mass": 8300,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "M72",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Takahashi_Mewlon_250CRS": {
            "brand": "Takahashi",
            "name": "Mewlon-250CRS",
            "type": "type_telescope",
            "optical_length": 0,
            "mass": 12200,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "M92",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Takahashi_Mewlon_300CRS": {
            "brand": "Takahashi",
            "name": "Mewlon-300CRS",
            "type": "type_telescope",
            "optical_length": 0,
            "mass": 18000,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "M92",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Takahashi_CN_212": {
            "brand": "Takahashi",
            "name": "CN-212",
            "type": "type_telescope",
            "optical_length": 0,
            "mass": 7500,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "M72",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Takahashi_Mu_300_CRS": {
            "brand": "Takahashi",
            "name": "Mu-300 CRS",
            "type": "type_telescope",
            "optical_length": 0,
            "mass": 20000,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "M92",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "William_Optics_GT71": {
            "brand": "William Optics",
            "name": "GT71",
            "type": "type_refractor",
            "optical_length": 0,
            "mass": 2200,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "M48",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "William_Optics_GT81": {
            "brand": "William Optics",
            "name": "GT81",
            "type": "type_refractor",
            "optical_length": 0,
            "mass": 2800,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "M48",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "William_Optics_GT102": {
            "brand": "William Optics",
            "name": "GT102",
            "type": "type_refractor",
            "optical_length": 0,
            "mass": 4500,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "M48",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "William_Optics_GT153": {
            "brand": "William Optics",
            "name": "GT153",
            "type": "type_refractor",
            "optical_length": 0,
            "mass": 8000,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "M68",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "William_Optics_RedCat_51": {
            "brand": "William Optics",
            "name": "RedCat 51",
            "type": "type_refractor",
            "optical_length": 0,
            "mass": 1400,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "M48",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "William_Optics_SpaceCat_51": {
            "brand": "William Optics",
            "name": "SpaceCat 51",
            "type": "type_refractor",
            "optical_length": 0,
            "mass": 1350,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "M48",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "William_Optics_WhiteCat_51": {
            "brand": "William Optics",
            "name": "WhiteCat 51",
            "type": "type_refractor",
            "optical_length": 0,
            "mass": 1400,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "M48",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "William_Optics_FluoroStar_91": {
            "brand": "William Optics",
            "name": "FluoroStar 91",
            "type": "type_refractor",
            "optical_length": 0,
            "mass": 3500,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "M48",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "William_Optics_FluoroStar_132": {
            "brand": "William Optics",
            "name": "FluoroStar 132",
            "type": "type_refractor",
            "optical_length": 0,
            "mass": 6200,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "M68",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "William_Optics_ZenithStar_61_II": {
            "brand": "William Optics",
            "name": "ZenithStar 61 II",
            "type": "type_refractor",
            "optical_length": 0,
            "mass": 1600,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "M48",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "William_Optics_ZenithStar_73": {
            "brand": "William Optics",
            "name": "ZenithStar 73",
            "type": "type_refractor",
            "optical_length": 0,
            "mass": 2100,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "M48",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "William_Optics_ZenithStar_81": {
            "brand": "William Optics",
            "name": "ZenithStar 81",
            "type": "type_refractor",
            "optical_length": 0,
            "mass": 2500,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "M48",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "William_Optics_ZenithStar_103": {
            "brand": "William Optics",
            "name": "ZenithStar 103",
            "type": "type_refractor",
            "optical_length": 0,
            "mass": 4000,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "M48",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "William_Optics_Cat_71": {
            "brand": "William Optics",
            "name": "Cat 71",
            "type": "type_refractor",
            "optical_length": 0,
            "mass": 2000,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "M48",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "William_Optics_Pleiades_68": {
            "brand": "William Optics",
            "name": "Pleiades 68",
            "type": "type_refractor",
            "optical_length": 0,
            "mass": 1800,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "M48",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "William_Optics_Gran_Turismo_71": {
            "brand": "William Optics",
            "name": "Gran Turismo 71",
            "type": "type_refractor",
            "optical_length": 0,
            "mass": 2200,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "M48",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "William_Optics_UniStellar_80": {
            "brand": "William Optics",
            "name": "UniStellar 80",
            "type": "type_refractor",
            "optical_length": 0,
            "mass": 2800,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "M48",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Askar_FRA300_Pro": {
            "brand": "Askar",
            "name": "FRA300 Pro",
            "type": "type_refractor",
            "optical_length": 0,
            "mass": 1800,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "M42",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Askar_FRA400": {
            "brand": "Askar",
            "name": "FRA400",
            "type": "type_refractor",
            "optical_length": 0,
            "mass": 2200,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "M48",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Askar_FRA500": {
            "brand": "Askar",
            "name": "FRA500",
            "type": "type_refractor",
            "optical_length": 0,
            "mass": 3000,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "M48",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Askar_FRA600": {
            "brand": "Askar",
            "name": "FRA600",
            "type": "type_refractor",
            "optical_length": 0,
            "mass": 3500,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "M48",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Askar_103APO": {
            "brand": "Askar",
            "name": "103APO",
            "type": "type_refractor",
            "optical_length": 0,
            "mass": 4200,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "M68",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Askar_80PHQ": {
            "brand": "Askar",
            "name": "80PHQ",
            "type": "type_refractor",
            "optical_length": 0,
            "mass": 3500,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "M54",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Askar_65PHQ": {
            "brand": "Askar",
            "name": "65PHQ",
            "type": "type_refractor",
            "optical_length": 0,
            "mass": 2200,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "M48",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Askar_107PHQ": {
            "brand": "Askar",
            "name": "107PHQ",
            "type": "type_refractor",
            "optical_length": 0,
            "mass": 5000,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "M68",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Askar_130PHQ": {
            "brand": "Askar",
            "name": "130PHQ",
            "type": "type_refractor",
            "optical_length": 0,
            "mass": 6000,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "M68",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Askar_151PHQ": {
            "brand": "Askar",
            "name": "151PHQ",
            "type": "type_refractor",
            "optical_length": 0,
            "mass": 8500,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "M68",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Askar_185APO": {
            "brand": "Askar",
            "name": "185APO",
            "type": "type_refractor",
            "optical_length": 0,
            "mass": 12000,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "M68",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Askar_V_60Q": {
            "brand": "Askar",
            "name": "V 60Q",
            "type": "type_refractor",
            "optical_length": 0,
            "mass": 1600,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "M48",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Askar_V_80Q": {
            "brand": "Askar",
            "name": "V 80Q",
            "type": "type_refractor",
            "optical_length": 0,
            "mass": 2200,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "M48",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Askar_FMA_135": {
            "brand": "Askar",
            "name": "FMA 135",
            "type": "type_refractor",
            "optical_length": 0,
            "mass": 600,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "M42",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Askar_FMA_180_Pro": {
            "brand": "Askar",
            "name": "FMA 180 Pro",
            "type": "type_refractor",
            "optical_length": 0,
            "mass": 800,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "M42",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Askar_FMA_230": {
            "brand": "Askar",
            "name": "FMA 230",
            "type": "type_refractor",
            "optical_length": 0,
            "mass": 1000,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "M42",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Askar_200APO": {
            "brand": "Askar",
            "name": "200APO",
            "type": "type_refractor",
            "optical_length": 0,
            "mass": 14000,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "M68",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Askar_140APO": {
            "brand": "Askar",
            "name": "140APO",
            "type": "type_refractor",
            "optical_length": 0,
            "mass": 5500,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "M68",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Askar_120APO": {
            "brand": "Askar",
            "name": "120APO",
            "type": "type_refractor",
            "optical_length": 0,
            "mass": 4800,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "M68",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Askar_ACL200": {
            "brand": "Askar",
            "name": "ACL200",
            "type": "type_camera_lens",
            "optical_length": 0,
            "mass": 2400,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "M54",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Sharpstar_61EDPH_II": {
            "brand": "Sharpstar",
            "name": "61EDPH II",
            "type": "type_refractor",
            "optical_length": 0,
            "mass": 2500,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "M48",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Sharpstar_76EDPH_II": {
            "brand": "Sharpstar",
            "name": "76EDPH II",
            "type": "type_refractor",
            "optical_length": 0,
            "mass": 3200,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "M48",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Sharpstar_94EDPH_II": {
            "brand": "Sharpstar",
            "name": "94EDPH II",
            "type": "type_refractor",
            "optical_length": 0,
            "mass": 4500,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "M54",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Sharpstar_140PH": {
            "brand": "Sharpstar",
            "name": "140PH",
            "type": "type_refractor",
            "optical_length": 0,
            "mass": 6000,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "M68",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Sharpstar_200PH": {
            "brand": "Sharpstar",
            "name": "200PH",
            "type": "type_refractor",
            "optical_length": 0,
            "mass": 10000,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "M68",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Sharpstar_15028HNT": {
            "brand": "Sharpstar",
            "name": "15028HNT",
            "type": "type_telescope",
            "optical_length": 0,
            "mass": 9500,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "M68",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Sharpstar_20032HNT": {
            "brand": "Sharpstar",
            "name": "20032HNT",
            "type": "type_telescope",
            "optical_length": 0,
            "mass": 13000,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "M68",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Sharpstar_25040HNT": {
            "brand": "Sharpstar",
            "name": "25040HNT",
            "type": "type_telescope",
            "optical_length": 0,
            "mass": 18000,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "M68",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "GSO_RC_6": {
            "brand": "GSO",
            "name": 'RC 6"',
            "type": "type_telescope",
            "optical_length": 0,
            "mass": 5000,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "M72",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "GSO_RC_8": {
            "brand": "GSO",
            "name": 'RC 8"',
            "type": "type_telescope",
            "optical_length": 0,
            "mass": 8500,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "M72",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "GSO_RC_10": {
            "brand": "GSO",
            "name": 'RC 10"',
            "type": "type_telescope",
            "optical_length": 0,
            "mass": 12000,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "M72",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "GSO_RC_12": {
            "brand": "GSO",
            "name": 'RC 12"',
            "type": "type_telescope",
            "optical_length": 0,
            "mass": 16000,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "M84",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "GSO_RC_14": {
            "brand": "GSO",
            "name": 'RC 14"',
            "type": "type_telescope",
            "optical_length": 0,
            "mass": 20000,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "M84",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "GSO_RC_16": {
            "brand": "GSO",
            "name": 'RC 16"',
            "type": "type_telescope",
            "optical_length": 0,
            "mass": 28000,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "M84",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "CFF_RC_250_10": {
            "brand": "CFF",
            "name": 'RC 250 (10")',
            "type": "type_telescope",
            "optical_length": 0,
            "mass": 11000,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "M117",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "CFF_RC_300_12": {
            "brand": "CFF",
            "name": 'RC 300 (12")',
            "type": "type_telescope",
            "optical_length": 0,
            "mass": 16000,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "M117",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "TPO_RC_6": {
            "brand": "TPO",
            "name": 'RC 6"',
            "type": "type_telescope",
            "optical_length": 0,
            "mass": 5200,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "M72",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "TPO_RC_8": {
            "brand": "TPO",
            "name": 'RC 8"',
            "type": "type_telescope",
            "optical_length": 0,
            "mass": 8700,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "M72",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "TPO_RC_10": {
            "brand": "TPO",
            "name": 'RC 10"',
            "type": "type_telescope",
            "optical_length": 0,
            "mass": 12500,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "M72",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "TS_Optics_Photoline_72mm_APO": {
            "brand": "TS-Optics",
            "name": "Photoline 72mm APO",
            "type": "type_refractor",
            "optical_length": 0,
            "mass": 2200,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "M48",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "TS_Optics_Photoline_80mm_APO": {
            "brand": "TS-Optics",
            "name": "Photoline 80mm APO",
            "type": "type_refractor",
            "optical_length": 0,
            "mass": 2800,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "M48",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "TS_Optics_Photoline_100mm_APO": {
            "brand": "TS-Optics",
            "name": "Photoline 100mm APO",
            "type": "type_refractor",
            "optical_length": 0,
            "mass": 4200,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "M48",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "TS_Optics_Photoline_115mm_APO": {
            "brand": "TS-Optics",
            "name": "Photoline 115mm APO",
            "type": "type_refractor",
            "optical_length": 0,
            "mass": 5500,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "M48",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "TS_Optics_Photoline_130mm_APO": {
            "brand": "TS-Optics",
            "name": "Photoline 130mm APO",
            "type": "type_refractor",
            "optical_length": 0,
            "mass": 6800,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "M68",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "TS_Optics_ONTC_6_f_4_Newton": {
            "brand": "TS-Optics",
            "name": 'ONTC 6" f/4 Newton',
            "type": "type_telescope",
            "optical_length": 0,
            "mass": 5000,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "M48",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "TS_Optics_ONTC_8_f_4_Newton": {
            "brand": "TS-Optics",
            "name": 'ONTC 8" f/4 Newton',
            "type": "type_telescope",
            "optical_length": 0,
            "mass": 8000,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "M48",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "TS_Optics_ONTC_10_f_4_Newton": {
            "brand": "TS-Optics",
            "name": 'ONTC 10" f/4 Newton',
            "type": "type_telescope",
            "optical_length": 0,
            "mass": 12000,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "M48",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "TS_Optics_Ritchey_Chretien_6": {
            "brand": "TS-Optics",
            "name": 'Ritchey-Chretien 6"',
            "type": "type_telescope",
            "optical_length": 0,
            "mass": 5500,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "M72",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "TS_Optics_Ritchey_Chretien_8": {
            "brand": "TS-Optics",
            "name": 'Ritchey-Chretien 8"',
            "type": "type_telescope",
            "optical_length": 0,
            "mass": 9000,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "M72",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "TS_Optics_Ritchey_Chretien_10": {
            "brand": "TS-Optics",
            "name": 'Ritchey-Chretien 10"',
            "type": "type_telescope",
            "optical_length": 0,
            "mass": 13000,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "M72",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "TS_Optics_Ritchey_Chretien_12": {
            "brand": "TS-Optics",
            "name": 'Ritchey-Chretien 12"',
            "type": "type_telescope",
            "optical_length": 0,
            "mass": 18000,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "M84",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "TS_Optics_PHOTON_6_f_9_Mak_Cass": {
            "brand": "TS-Optics",
            "name": 'PHOTON 6" f/9 Mak-Cass',
            "type": "type_telescope",
            "optical_length": 0,
            "mass": 5000,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "SC (Schmidt-Cassegrain)",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "TS_Optics_CF_APO_80mm": {
            "brand": "TS-Optics",
            "name": "CF-APO 80mm",
            "type": "type_refractor",
            "optical_length": 0,
            "mass": 3000,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "M48",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "TS_Optics_CF_APO_102mm": {
            "brand": "TS-Optics",
            "name": "CF-APO 102mm",
            "type": "type_refractor",
            "optical_length": 0,
            "mass": 4500,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "M48",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "TS_Optics_CF_APO_130mm": {
            "brand": "TS-Optics",
            "name": "CF-APO 130mm",
            "type": "type_refractor",
            "optical_length": 0,
            "mass": 7000,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "M68",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "TS_Optics_CF_APO_152mm": {
            "brand": "TS-Optics",
            "name": "CF-APO 152mm",
            "type": "type_refractor",
            "optical_length": 0,
            "mass": 10000,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "M68",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "TS_Optics_Individual_65mm_Quad": {
            "brand": "TS-Optics",
            "name": "Individual 65mm Quad",
            "type": "type_refractor",
            "optical_length": 0,
            "mass": 1800,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "M48",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Explore_Scientific_ED80_FCD100": {
            "brand": "Explore Scientific",
            "name": "ED80 FCD100",
            "type": "type_refractor",
            "optical_length": 0,
            "mass": 3000,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "M48",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Explore_Scientific_ED102_FCD100": {
            "brand": "Explore Scientific",
            "name": "ED102 FCD100",
            "type": "type_refractor",
            "optical_length": 0,
            "mass": 4500,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "M48",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Explore_Scientific_ED127_FCD100": {
            "brand": "Explore Scientific",
            "name": "ED127 FCD100",
            "type": "type_refractor",
            "optical_length": 0,
            "mass": 7000,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "M68",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Explore_Scientific_ED152_FCD100": {
            "brand": "Explore Scientific",
            "name": "ED152 FCD100",
            "type": "type_refractor",
            "optical_length": 0,
            "mass": 11000,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "M68",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Explore_Scientific_ED80_Essential": {
            "brand": "Explore Scientific",
            "name": "ED80 Essential",
            "type": "type_refractor",
            "optical_length": 0,
            "mass": 2200,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "M48",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Explore_Scientific_ED102_Essential": {
            "brand": "Explore Scientific",
            "name": "ED102 Essential",
            "type": "type_refractor",
            "optical_length": 0,
            "mass": 3500,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "M48",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Explore_Scientific_ED127_Essential": {
            "brand": "Explore Scientific",
            "name": "ED127 Essential",
            "type": "type_refractor",
            "optical_length": 0,
            "mass": 5500,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "M68",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Explore_Scientific_FCD1_80": {
            "brand": "Explore Scientific",
            "name": "FCD1-80",
            "type": "type_refractor",
            "optical_length": 0,
            "mass": 2500,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "M48",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Explore_Scientific_FCD1_102": {
            "brand": "Explore Scientific",
            "name": "FCD1-102",
            "type": "type_refractor",
            "optical_length": 0,
            "mass": 3800,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "M48",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Explore_Scientific_FCD100_127_Triplet": {
            "brand": "Explore Scientific",
            "name": "FCD100-127 Triplet",
            "type": "type_refractor",
            "optical_length": 0,
            "mass": 7500,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "M68",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Explore_Scientific_DAR152065_6_f_5_Newton": {
            "brand": "Explore Scientific",
            "name": 'DAR152065 (6" f/5 Newton)',
            "type": "type_telescope",
            "optical_length": 0,
            "mass": 5500,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "M48",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Explore_Scientific_DAR20010001_8_f_5_Newton": {
            "brand": "Explore Scientific",
            "name": 'DAR20010001 (8" f/5 Newton)',
            "type": "type_telescope",
            "optical_length": 0,
            "mass": 8500,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "M48",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Explore_Scientific_Truss_Dob_10": {
            "brand": "Explore Scientific",
            "name": 'Truss Dob 10"',
            "type": "type_telescope",
            "optical_length": 0,
            "mass": 10000,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": '2"',
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Explore_Scientific_Truss_Dob_12": {
            "brand": "Explore Scientific",
            "name": 'Truss Dob 12"',
            "type": "type_telescope",
            "optical_length": 0,
            "mass": 14000,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": '2"',
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Explore_Scientific_Truss_Dob_16": {
            "brand": "Explore Scientific",
            "name": 'Truss Dob 16"',
            "type": "type_telescope",
            "optical_length": 0,
            "mass": 22000,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": '2"',
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Explore_Scientific_305mm_f_5_Newton": {
            "brand": "Explore Scientific",
            "name": "305mm f/5 Newton",
            "type": "type_telescope",
            "optical_length": 0,
            "mass": 11000,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": '2"',
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Meade_LX85_ACF_6": {
            "brand": "Meade",
            "name": 'LX85 ACF 6"',
            "type": "type_telescope",
            "optical_length": 0,
            "mass": 4200,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "SC (Schmidt-Cassegrain)",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Meade_LX85_ACF_8": {
            "brand": "Meade",
            "name": 'LX85 ACF 8"',
            "type": "type_telescope",
            "optical_length": 0,
            "mass": 5700,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "SC (Schmidt-Cassegrain)",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Meade_LX200_ACF_8": {
            "brand": "Meade",
            "name": 'LX200 ACF 8"',
            "type": "type_telescope",
            "optical_length": 0,
            "mass": 6000,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "SC (Schmidt-Cassegrain)",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Meade_LX200_ACF_10": {
            "brand": "Meade",
            "name": 'LX200 ACF 10"',
            "type": "type_telescope",
            "optical_length": 0,
            "mass": 11000,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "SC (Schmidt-Cassegrain)",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Meade_LX200_ACF_12": {
            "brand": "Meade",
            "name": 'LX200 ACF 12"',
            "type": "type_telescope",
            "optical_length": 0,
            "mass": 14000,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "SC (Schmidt-Cassegrain)",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Meade_LX200_ACF_14": {
            "brand": "Meade",
            "name": 'LX200 ACF 14"',
            "type": "type_telescope",
            "optical_length": 0,
            "mass": 18000,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "SC (Schmidt-Cassegrain)",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Meade_LX200_ACF_16": {
            "brand": "Meade",
            "name": 'LX200 ACF 16"',
            "type": "type_telescope",
            "optical_length": 0,
            "mass": 26000,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "SC (Schmidt-Cassegrain)",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Meade_LX600_ACF_10": {
            "brand": "Meade",
            "name": 'LX600 ACF 10"',
            "type": "type_telescope",
            "optical_length": 0,
            "mass": 11500,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "SC (Schmidt-Cassegrain)",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Meade_LX600_ACF_12": {
            "brand": "Meade",
            "name": 'LX600 ACF 12"',
            "type": "type_telescope",
            "optical_length": 0,
            "mass": 15000,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "SC (Schmidt-Cassegrain)",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Meade_LX600_ACF_14": {
            "brand": "Meade",
            "name": 'LX600 ACF 14"',
            "type": "type_telescope",
            "optical_length": 0,
            "mass": 22000,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "SC (Schmidt-Cassegrain)",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Meade_ETX_90": {
            "brand": "Meade",
            "name": "ETX-90",
            "type": "type_telescope",
            "optical_length": 0,
            "mass": 1500,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": '1.25"',
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Meade_ETX_125": {
            "brand": "Meade",
            "name": "ETX-125",
            "type": "type_telescope",
            "optical_length": 0,
            "mass": 3000,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "SC (Schmidt-Cassegrain)",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Vixen_VC200L": {
            "brand": "Vixen",
            "name": "VC200L",
            "type": "type_telescope",
            "optical_length": 0,
            "mass": 6900,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "M42",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Vixen_VSD100_F3_8": {
            "brand": "Vixen",
            "name": "VSD100 F3.8",
            "type": "type_refractor",
            "optical_length": 0,
            "mass": 4200,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "M48",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Vixen_VSD90SS": {
            "brand": "Vixen",
            "name": "VSD90SS",
            "type": "type_refractor",
            "optical_length": 0,
            "mass": 3500,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "M48",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Vixen_A80Mf": {
            "brand": "Vixen",
            "name": "A80Mf",
            "type": "type_refractor",
            "optical_length": 0,
            "mass": 2500,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "M42",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Vixen_A80M": {
            "brand": "Vixen",
            "name": "A80M",
            "type": "type_refractor",
            "optical_length": 0,
            "mass": 2700,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "M42",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Vixen_SD81S": {
            "brand": "Vixen",
            "name": "SD81S",
            "type": "type_refractor",
            "optical_length": 0,
            "mass": 3000,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "M48",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Vixen_SD103S": {
            "brand": "Vixen",
            "name": "SD103S",
            "type": "type_refractor",
            "optical_length": 0,
            "mass": 4500,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "M48",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Vixen_SD115S": {
            "brand": "Vixen",
            "name": "SD115S",
            "type": "type_refractor",
            "optical_length": 0,
            "mass": 6000,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "M48",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Vixen_AX103S": {
            "brand": "Vixen",
            "name": "AX103S",
            "type": "type_refractor",
            "optical_length": 0,
            "mass": 4800,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "M54",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Vixen_FL55SS": {
            "brand": "Vixen",
            "name": "FL55SS",
            "type": "type_refractor",
            "optical_length": 0,
            "mass": 1500,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "M48",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Vixen_R200SS": {
            "brand": "Vixen",
            "name": "R200SS",
            "type": "type_telescope",
            "optical_length": 0,
            "mass": 5500,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "M48",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Vixen_VMC200L": {
            "brand": "Vixen",
            "name": "VMC200L",
            "type": "type_telescope",
            "optical_length": 0,
            "mass": 6800,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "M42",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "PlaneWave_CDK12_5": {
            "brand": "PlaneWave",
            "name": "CDK12.5",
            "type": "type_telescope",
            "optical_length": 0,
            "mass": 15000,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "M117",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "PlaneWave_CDK14": {
            "brand": "PlaneWave",
            "name": "CDK14",
            "type": "type_telescope",
            "optical_length": 0,
            "mass": 21000,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "M117",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "PlaneWave_CDK17": {
            "brand": "PlaneWave",
            "name": "CDK17",
            "type": "type_telescope",
            "optical_length": 0,
            "mass": 32000,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "M117",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "PlaneWave_CDK20": {
            "brand": "PlaneWave",
            "name": "CDK20",
            "type": "type_telescope",
            "optical_length": 0,
            "mass": 50000,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "M117",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "PlaneWave_CDK24": {
            "brand": "PlaneWave",
            "name": "CDK24",
            "type": "type_telescope",
            "optical_length": 0,
            "mass": 65000,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "M117",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Officina_Stellare_RH200": {
            "brand": "Officina Stellare",
            "name": "RH200",
            "type": "type_telescope",
            "optical_length": 0,
            "mass": 8000,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "M68",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Officina_Stellare_RH300": {
            "brand": "Officina Stellare",
            "name": "RH300",
            "type": "type_telescope",
            "optical_length": 0,
            "mass": 14000,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "M84",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Officina_Stellare_RiDK_250": {
            "brand": "Officina Stellare",
            "name": "RiDK 250",
            "type": "type_telescope",
            "optical_length": 0,
            "mass": 11000,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "M68",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Officina_Stellare_RiDK_300": {
            "brand": "Officina Stellare",
            "name": "RiDK 300",
            "type": "type_telescope",
            "optical_length": 0,
            "mass": 15000,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "M84",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Officina_Stellare_RiDK_400": {
            "brand": "Officina Stellare",
            "name": "RiDK 400",
            "type": "type_telescope",
            "optical_length": 0,
            "mass": 25000,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "M84",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Officina_Stellare_Ultra_CRC_250": {
            "brand": "Officina Stellare",
            "name": "Ultra CRC 250",
            "type": "type_telescope",
            "optical_length": 0,
            "mass": 12000,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "M68",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Officina_Stellare_Ultra_CRC_300": {
            "brand": "Officina Stellare",
            "name": "Ultra CRC 300",
            "type": "type_telescope",
            "optical_length": 0,
            "mass": 16000,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "M84",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Astro_Physics_130GTX": {
            "brand": "Astro-Physics",
            "name": "130GTX",
            "type": "type_refractor",
            "optical_length": 0,
            "mass": 7500,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "M68",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Astro_Physics_Stowaway_92mm": {
            "brand": "Astro-Physics",
            "name": "Stowaway 92mm",
            "type": "type_refractor",
            "optical_length": 0,
            "mass": 3000,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "M48",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Astro_Physics_Traveler_105mm": {
            "brand": "Astro-Physics",
            "name": "Traveler 105mm",
            "type": "type_refractor",
            "optical_length": 0,
            "mass": 4000,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "M48",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Astro_Physics_StarFire_130_EDF": {
            "brand": "Astro-Physics",
            "name": "StarFire 130 EDF",
            "type": "type_refractor",
            "optical_length": 0,
            "mass": 6500,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "M68",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Astro_Physics_StarFire_155_EDF": {
            "brand": "Astro-Physics",
            "name": "StarFire 155 EDF",
            "type": "type_refractor",
            "optical_length": 0,
            "mass": 10000,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "M68",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Astro_Physics_StarFire_175_EDF": {
            "brand": "Astro-Physics",
            "name": "StarFire 175 EDF",
            "type": "type_refractor",
            "optical_length": 0,
            "mass": 13000,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "M68",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Astro_Physics_AP_92": {
            "brand": "Astro-Physics",
            "name": "AP 92",
            "type": "type_refractor",
            "optical_length": 0,
            "mass": 3200,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "M48",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Stellarvue_SVX080T": {
            "brand": "Stellarvue",
            "name": "SVX080T",
            "type": "type_refractor",
            "optical_length": 0,
            "mass": 2800,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "M48",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Stellarvue_SVX102T": {
            "brand": "Stellarvue",
            "name": "SVX102T",
            "type": "type_refractor",
            "optical_length": 0,
            "mass": 4200,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "M48",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Stellarvue_SVX102T_R": {
            "brand": "Stellarvue",
            "name": "SVX102T-R",
            "type": "type_refractor",
            "optical_length": 0,
            "mass": 4500,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "M54",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Stellarvue_SVX130T": {
            "brand": "Stellarvue",
            "name": "SVX130T",
            "type": "type_refractor",
            "optical_length": 0,
            "mass": 7000,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "M68",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Stellarvue_SVX152T": {
            "brand": "Stellarvue",
            "name": "SVX152T",
            "type": "type_refractor",
            "optical_length": 0,
            "mass": 10000,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "M68",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Stellarvue_SV60EDS": {
            "brand": "Stellarvue",
            "name": "SV60EDS",
            "type": "type_refractor",
            "optical_length": 0,
            "mass": 1200,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "M42",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Stellarvue_SV70T": {
            "brand": "Stellarvue",
            "name": "SV70T",
            "type": "type_refractor",
            "optical_length": 0,
            "mass": 1800,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "M48",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Stellarvue_SVX80T_IS": {
            "brand": "Stellarvue",
            "name": "SVX80T-IS",
            "type": "type_refractor",
            "optical_length": 0,
            "mass": 2500,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "M48",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Stellarvue_SVX090T": {
            "brand": "Stellarvue",
            "name": "SVX090T",
            "type": "type_refractor",
            "optical_length": 0,
            "mass": 3200,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "M48",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Stellarvue_Access_80": {
            "brand": "Stellarvue",
            "name": "Access 80",
            "type": "type_refractor",
            "optical_length": 0,
            "mass": 1500,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "M48",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Stellarvue_Access_102": {
            "brand": "Stellarvue",
            "name": "Access 102",
            "type": "type_refractor",
            "optical_length": 0,
            "mass": 3000,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "M48",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "TEC_TEC_110_FL": {
            "brand": "TEC",
            "name": "TEC 110 FL",
            "type": "type_refractor",
            "optical_length": 0,
            "mass": 4500,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "M54",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "TEC_TEC_140_FL": {
            "brand": "TEC",
            "name": "TEC 140 FL",
            "type": "type_refractor",
            "optical_length": 0,
            "mass": 7000,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "M68",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "TEC_TEC_160_FL": {
            "brand": "TEC",
            "name": "TEC 160 FL",
            "type": "type_refractor",
            "optical_length": 0,
            "mass": 10000,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "M68",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "TEC_TEC_180_FL": {
            "brand": "TEC",
            "name": "TEC 180 FL",
            "type": "type_refractor",
            "optical_length": 0,
            "mass": 14000,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "M68",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "TEC_TEC_200_FL": {
            "brand": "TEC",
            "name": "TEC 200 FL",
            "type": "type_refractor",
            "optical_length": 0,
            "mass": 18000,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "M68",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Borg_55FL": {
            "brand": "Borg",
            "name": "55FL",
            "type": "type_refractor",
            "optical_length": 0,
            "mass": 800,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "M42",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Borg_71FL": {
            "brand": "Borg",
            "name": "71FL",
            "type": "type_refractor",
            "optical_length": 0,
            "mass": 1200,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "M48",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Borg_89ED": {
            "brand": "Borg",
            "name": "89ED",
            "type": "type_refractor",
            "optical_length": 0,
            "mass": 2800,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "M48",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Borg_107FL": {
            "brand": "Borg",
            "name": "107FL",
            "type": "type_refractor",
            "optical_length": 0,
            "mass": 4000,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "M54",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Borg_90FL": {
            "brand": "Borg",
            "name": "90FL",
            "type": "type_refractor",
            "optical_length": 0,
            "mass": 2500,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "M48",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Borg_77EDII": {
            "brand": "Borg",
            "name": "77EDII",
            "type": "type_refractor",
            "optical_length": 0,
            "mass": 1800,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "M48",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "APM_LZOS_130_780": {
            "brand": "APM",
            "name": "LZOS 130/780",
            "type": "type_refractor",
            "optical_length": 0,
            "mass": 6500,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "M68",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "APM_LZOS_115_805": {
            "brand": "APM",
            "name": "LZOS 115/805",
            "type": "type_refractor",
            "optical_length": 0,
            "mass": 5000,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "M68",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "APM_LZOS_152_1200": {
            "brand": "APM",
            "name": "LZOS 152/1200",
            "type": "type_refractor",
            "optical_length": 0,
            "mass": 10000,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "M68",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "APM_LZOS_175_1400": {
            "brand": "APM",
            "name": "LZOS 175/1400",
            "type": "type_refractor",
            "optical_length": 0,
            "mass": 14000,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "M68",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "APM_TMB_80_480": {
            "brand": "APM",
            "name": "TMB 80/480",
            "type": "type_refractor",
            "optical_length": 0,
            "mass": 2000,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "M48",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "APM_TMB_105_650": {
            "brand": "APM",
            "name": "TMB 105/650",
            "type": "type_refractor",
            "optical_length": 0,
            "mass": 4000,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "M48",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "APM_TMB_130_780": {
            "brand": "APM",
            "name": "TMB 130/780",
            "type": "type_refractor",
            "optical_length": 0,
            "mass": 6500,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "M68",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Orion_EON_130mm_ED": {
            "brand": "Orion",
            "name": "EON 130mm ED",
            "type": "type_refractor",
            "optical_length": 0,
            "mass": 6200,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "M48",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Orion_8_f_3_9_Astrograph": {
            "brand": "Orion",
            "name": '8" f/3.9 Astrograph',
            "type": "type_telescope",
            "optical_length": 0,
            "mass": 8500,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "M48",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Orion_EON_110mm_ED": {
            "brand": "Orion",
            "name": "EON 110mm ED",
            "type": "type_refractor",
            "optical_length": 0,
            "mass": 4000,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "M48",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Orion_EON_80mm_ED": {
            "brand": "Orion",
            "name": "EON 80mm ED",
            "type": "type_refractor",
            "optical_length": 0,
            "mass": 2500,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "M48",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Orion_XT8_Classic_Dob": {
            "brand": "Orion",
            "name": "XT8 Classic Dob",
            "type": "type_telescope",
            "optical_length": 0,
            "mass": 8500,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": '2"',
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Orion_XT10_Classic_Dob": {
            "brand": "Orion",
            "name": "XT10 Classic Dob",
            "type": "type_telescope",
            "optical_length": 0,
            "mass": 11000,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": '2"',
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Orion_XT12_Classic_Dob": {
            "brand": "Orion",
            "name": "XT12 Classic Dob",
            "type": "type_telescope",
            "optical_length": 0,
            "mass": 15000,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": '2"',
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Orion_SkyQuest_XX12_Dob": {
            "brand": "Orion",
            "name": "SkyQuest XX12 Dob",
            "type": "type_telescope",
            "optical_length": 0,
            "mass": 14500,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": '2"',
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Orion_SkyQuest_XX14_Dob": {
            "brand": "Orion",
            "name": "SkyQuest XX14 Dob",
            "type": "type_telescope",
            "optical_length": 0,
            "mass": 20000,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": '2"',
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Orion_SpaceProbe_130ST": {
            "brand": "Orion",
            "name": "SpaceProbe 130ST",
            "type": "type_telescope",
            "optical_length": 0,
            "mass": 3800,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": '2"',
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Bresser_Messier_AR_102xs": {
            "brand": "Bresser",
            "name": "Messier AR-102xs",
            "type": "type_refractor",
            "optical_length": 0,
            "mass": 2800,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "M48",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Bresser_Messier_AR_127L": {
            "brand": "Bresser",
            "name": "Messier AR-127L",
            "type": "type_refractor",
            "optical_length": 0,
            "mass": 5000,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "M48",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Bresser_Messier_AR_152L": {
            "brand": "Bresser",
            "name": "Messier AR-152L",
            "type": "type_refractor",
            "optical_length": 0,
            "mass": 7000,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "M48",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Bresser_Messier_MC_127": {
            "brand": "Bresser",
            "name": "Messier MC-127",
            "type": "type_telescope",
            "optical_length": 0,
            "mass": 3200,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": '1.25"',
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Bresser_Messier_MC_152": {
            "brand": "Bresser",
            "name": "Messier MC-152",
            "type": "type_telescope",
            "optical_length": 0,
            "mass": 5500,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "SC (Schmidt-Cassegrain)",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Bresser_Messier_NT_150L_6": {
            "brand": "Bresser",
            "name": 'Messier NT-150L (6")',
            "type": "type_telescope",
            "optical_length": 0,
            "mass": 5000,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": '2"',
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Bresser_Messier_NT_203_8": {
            "brand": "Bresser",
            "name": 'Messier NT-203 (8")',
            "type": "type_telescope",
            "optical_length": 0,
            "mass": 8000,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": '2"',
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Bresser_Messier_NT_254_10": {
            "brand": "Bresser",
            "name": 'Messier NT-254 (10")',
            "type": "type_telescope",
            "optical_length": 0,
            "mass": 12000,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": '2"',
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Bresser_Messier_AR_80": {
            "brand": "Bresser",
            "name": "Messier AR-80",
            "type": "type_refractor",
            "optical_length": 0,
            "mass": 2000,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "M48",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Bresser_Messier_AR_90": {
            "brand": "Bresser",
            "name": "Messier AR-90",
            "type": "type_refractor",
            "optical_length": 0,
            "mass": 2300,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "M48",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Lacerta_Newton_200_800": {
            "brand": "Lacerta",
            "name": "Newton 200/800",
            "type": "type_telescope",
            "optical_length": 0,
            "mass": 7500,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "M48",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Lacerta_Newton_250_1000": {
            "brand": "Lacerta",
            "name": "Newton 250/1000",
            "type": "type_telescope",
            "optical_length": 0,
            "mass": 11500,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "M48",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Lacerta_Newton_200_1000": {
            "brand": "Lacerta",
            "name": "Newton 200/1000",
            "type": "type_telescope",
            "optical_length": 0,
            "mass": 7800,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "M48",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Lacerta_Newton_300_1200": {
            "brand": "Lacerta",
            "name": "Newton 300/1200",
            "type": "type_telescope",
            "optical_length": 0,
            "mass": 16000,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "M48",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Omegon_ProED_80": {
            "brand": "Omegon",
            "name": "ProED 80",
            "type": "type_refractor",
            "optical_length": 0,
            "mass": 2500,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "M48",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Omegon_ProED_100": {
            "brand": "Omegon",
            "name": "ProED 100",
            "type": "type_refractor",
            "optical_length": 0,
            "mass": 3800,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "M48",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Omegon_ProED_110": {
            "brand": "Omegon",
            "name": "ProED 110",
            "type": "type_refractor",
            "optical_length": 0,
            "mass": 4500,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "M48",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Omegon_N_200_800": {
            "brand": "Omegon",
            "name": "N 200/800",
            "type": "type_telescope",
            "optical_length": 0,
            "mass": 7000,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "M48",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Omegon_N_250_1000": {
            "brand": "Omegon",
            "name": "N 250/1000",
            "type": "type_telescope",
            "optical_length": 0,
            "mass": 11000,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "M48",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Omegon_Pro_APO_94": {
            "brand": "Omegon",
            "name": "Pro APO 94",
            "type": "type_refractor",
            "optical_length": 0,
            "mass": 3500,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "M48",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Omegon_Pro_APO_121": {
            "brand": "Omegon",
            "name": "Pro APO 121",
            "type": "type_refractor",
            "optical_length": 0,
            "mass": 5500,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "M48",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Omegon_Pro_APO_152": {
            "brand": "Omegon",
            "name": "Pro APO 152",
            "type": "type_refractor",
            "optical_length": 0,
            "mass": 9000,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "M68",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Sigma_135mm_f_2_Art": {
            "brand": "Sigma",
            "name": "135mm f/2 Art",
            "type": "type_camera_lens",
            "optical_length": 0,
            "mass": 1130,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "EOS",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Sigma_105mm_f_1_4_Art": {
            "brand": "Sigma",
            "name": "105mm f/1.4 Art",
            "type": "type_camera_lens",
            "optical_length": 0,
            "mass": 1645,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "EOS",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Sigma_150_600mm_f_5_6_3_DG": {
            "brand": "Sigma",
            "name": "150-600mm f/5-6.3 DG",
            "type": "type_camera_lens",
            "optical_length": 0,
            "mass": 2860,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "EOS",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Sigma_14mm_f_1_8_Art": {
            "brand": "Sigma",
            "name": "14mm f/1.8 Art",
            "type": "type_camera_lens",
            "optical_length": 0,
            "mass": 1120,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "EOS",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Samyang_Rokinon_135mm_f_2_0_ED_UMC": {
            "brand": "Samyang/Rokinon",
            "name": "135mm f/2.0 ED UMC",
            "type": "type_camera_lens",
            "optical_length": 0,
            "mass": 730,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "EOS",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Samyang_Rokinon_85mm_f_1_4_UMC": {
            "brand": "Samyang/Rokinon",
            "name": "85mm f/1.4 UMC",
            "type": "type_camera_lens",
            "optical_length": 0,
            "mass": 530,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "EOS",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Samyang_Rokinon_14mm_f_2_8_ED_UMC": {
            "brand": "Samyang/Rokinon",
            "name": "14mm f/2.8 ED UMC",
            "type": "type_camera_lens",
            "optical_length": 0,
            "mass": 550,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "EOS",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Samyang_Rokinon_24mm_f_1_4_ED_UMC": {
            "brand": "Samyang/Rokinon",
            "name": "24mm f/1.4 ED UMC",
            "type": "type_camera_lens",
            "optical_length": 0,
            "mass": 680,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "EOS",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Samyang_Rokinon_135mm_f_2_0_Canon_RF": {
            "brand": "Samyang/Rokinon",
            "name": "135mm f/2.0 (Canon RF)",
            "type": "type_camera_lens",
            "optical_length": 0,
            "mass": 730,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "Canon RF",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Samyang_Rokinon_135mm_f_2_0_Sony_E": {
            "brand": "Samyang/Rokinon",
            "name": "135mm f/2.0 (Sony E)",
            "type": "type_camera_lens",
            "optical_length": 0,
            "mass": 730,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "Sony E",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Samyang_Rokinon_135mm_f_2_0_Nikon_Z": {
            "brand": "Samyang/Rokinon",
            "name": "135mm f/2.0 (Nikon Z)",
            "type": "type_camera_lens",
            "optical_length": 0,
            "mass": 730,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "Nikon Z",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "SVBony_SV503_70ED": {
            "brand": "SVBony",
            "name": "SV503 70ED",
            "type": "type_refractor",
            "optical_length": 0,
            "mass": 1800,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "M48",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "SVBony_SV503_80ED": {
            "brand": "SVBony",
            "name": "SV503 80ED",
            "type": "type_refractor",
            "optical_length": 0,
            "mass": 2500,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "M48",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "SVBony_SV503_102ED": {
            "brand": "SVBony",
            "name": "SV503 102ED",
            "type": "type_refractor",
            "optical_length": 0,
            "mass": 4200,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "M48",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "SVBony_SV550_80ED": {
            "brand": "SVBony",
            "name": "SV550 80ED",
            "type": "type_refractor",
            "optical_length": 0,
            "mass": 2700,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "M48",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "SVBony_SV550_122ED": {
            "brand": "SVBony",
            "name": "SV550 122ED",
            "type": "type_refractor",
            "optical_length": 0,
            "mass": 6000,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "M68",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "SVBony_SV48": {
            "brand": "SVBony",
            "name": "SV48",
            "type": "type_refractor",
            "optical_length": 0,
            "mass": 2200,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "M48",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "SVBony_SV503_80": {
            "brand": "SVBony",
            "name": "SV503 80",
            "type": "type_refractor",
            "optical_length": 0,
            "mass": 2500,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "M48",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "iOptron_iOptron_RC_6": {
            "brand": "iOptron",
            "name": 'iOptron RC 6"',
            "type": "type_telescope",
            "optical_length": 0,
            "mass": 5200,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "M72",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "iOptron_iOptron_RC_8": {
            "brand": "iOptron",
            "name": 'iOptron RC 8"',
            "type": "type_telescope",
            "optical_length": 0,
            "mass": 8800,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "M72",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "iOptron_iOptron_80mm_APO": {
            "brand": "iOptron",
            "name": "iOptron 80mm APO",
            "type": "type_refractor",
            "optical_length": 0,
            "mass": 2500,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "M48",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "iOptron_iOptron_102mm_APO": {
            "brand": "iOptron",
            "name": "iOptron 102mm APO",
            "type": "type_refractor",
            "optical_length": 0,
            "mass": 4000,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "M48",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Saxon_Saxon_72ED": {
            "brand": "Saxon",
            "name": "Saxon 72ED",
            "type": "type_refractor",
            "optical_length": 0,
            "mass": 1800,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "M48",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Saxon_Saxon_80ED": {
            "brand": "Saxon",
            "name": "Saxon 80ED",
            "type": "type_refractor",
            "optical_length": 0,
            "mass": 2400,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "M48",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Saxon_Saxon_102ED": {
            "brand": "Saxon",
            "name": "Saxon 102ED",
            "type": "type_refractor",
            "optical_length": 0,
            "mass": 4000,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "M48",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Saxon_Saxon_127_Mak": {
            "brand": "Saxon",
            "name": "Saxon 127 Mak",
            "type": "type_telescope",
            "optical_length": 0,
            "mass": 3400,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": '1.25"',
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Saxon_Saxon_150_Mak": {
            "brand": "Saxon",
            "name": "Saxon 150 Mak",
            "type": "type_telescope",
            "optical_length": 0,
            "mass": 5000,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": '2"',
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Saxon_Saxon_200P_Dob": {
            "brand": "Saxon",
            "name": "Saxon 200P Dob",
            "type": "type_telescope",
            "optical_length": 0,
            "mass": 8000,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": '2"',
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Saxon_Saxon_250P_Dob": {
            "brand": "Saxon",
            "name": "Saxon 250P Dob",
            "type": "type_telescope",
            "optical_length": 0,
            "mass": 11000,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": '2"',
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Tecnosky_Tecnosky_60_360_APO": {
            "brand": "Tecnosky",
            "name": "Tecnosky 60/360 APO",
            "type": "type_refractor",
            "optical_length": 0,
            "mass": 1200,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "M48",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Tecnosky_Tecnosky_80_480_APO": {
            "brand": "Tecnosky",
            "name": "Tecnosky 80/480 APO",
            "type": "type_refractor",
            "optical_length": 0,
            "mass": 2500,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "M48",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Tecnosky_Tecnosky_102_714_APO": {
            "brand": "Tecnosky",
            "name": "Tecnosky 102/714 APO",
            "type": "type_refractor",
            "optical_length": 0,
            "mass": 4200,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "M48",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Tecnosky_Tecnosky_130_910_APO": {
            "brand": "Tecnosky",
            "name": "Tecnosky 130/910 APO",
            "type": "type_refractor",
            "optical_length": 0,
            "mass": 6500,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "M68",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Tecnosky_Tecnosky_RC_6": {
            "brand": "Tecnosky",
            "name": 'Tecnosky RC 6"',
            "type": "type_telescope",
            "optical_length": 0,
            "mass": 5200,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "M72",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Tecnosky_Tecnosky_RC_8": {
            "brand": "Tecnosky",
            "name": 'Tecnosky RC 8"',
            "type": "type_telescope",
            "optical_length": 0,
            "mass": 8500,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "M72",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Tecnosky_Tecnosky_RC_10": {
            "brand": "Tecnosky",
            "name": 'Tecnosky RC 10"',
            "type": "type_telescope",
            "optical_length": 0,
            "mass": 12000,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "M72",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Tecnosky_Tecnosky_RC_12": {
            "brand": "Tecnosky",
            "name": 'Tecnosky RC 12"',
            "type": "type_telescope",
            "optical_length": 0,
            "mass": 16000,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "M84",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "KUO_KUO_80_480_APO": {
            "brand": "KUO",
            "name": "KUO 80/480 APO",
            "type": "type_refractor",
            "optical_length": 0,
            "mass": 2300,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "M48",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "KUO_KUO_102_714_APO": {
            "brand": "KUO",
            "name": "KUO 102/714 APO",
            "type": "type_refractor",
            "optical_length": 0,
            "mass": 4000,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "M48",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "KUO_KUO_130_910_APO": {
            "brand": "KUO",
            "name": "KUO 130/910 APO",
            "type": "type_refractor",
            "optical_length": 0,
            "mass": 6200,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "M68",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "KUO_KUO_152_1200_APO": {
            "brand": "KUO",
            "name": "KUO 152/1200 APO",
            "type": "type_refractor",
            "optical_length": 0,
            "mass": 9000,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "M68",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Long_Perng_LP_66_400_APO": {
            "brand": "Long Perng",
            "name": "LP 66/400 APO",
            "type": "type_refractor",
            "optical_length": 0,
            "mass": 1500,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "M48",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Long_Perng_LP_80_480_APO": {
            "brand": "Long Perng",
            "name": "LP 80/480 APO",
            "type": "type_refractor",
            "optical_length": 0,
            "mass": 2300,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "M48",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Long_Perng_LP_90_500_APO": {
            "brand": "Long Perng",
            "name": "LP 90/500 APO",
            "type": "type_refractor",
            "optical_length": 0,
            "mass": 3000,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "M48",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Long_Perng_LP_110_660_APO": {
            "brand": "Long Perng",
            "name": "LP 110/660 APO",
            "type": "type_refractor",
            "optical_length": 0,
            "mass": 5000,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "M54",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Long_Perng_LP_127_952_APO": {
            "brand": "Long Perng",
            "name": "LP 127/952 APO",
            "type": "type_refractor",
            "optical_length": 0,
            "mass": 7000,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "M68",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Takahashi_FSQ_85EDX4": {
            "brand": "Takahashi",
            "name": "FSQ-85EDX4",
            "type": "type_refractor",
            "optical_length": 0,
            "mass": 3300,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "M82",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Takahashi_FSQ_106EDX4": {
            "brand": "Takahashi",
            "name": "FSQ-106EDX4",
            "type": "type_refractor",
            "optical_length": 0,
            "mass": 6500,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "M82",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "William_Optics_Saddle_Cat_51": {
            "brand": "William Optics",
            "name": "Saddle Cat 51",
            "type": "type_refractor",
            "optical_length": 0,
            "mass": 1300,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "M48",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "William_Optics_Redcat_71": {
            "brand": "William Optics",
            "name": "Redcat 71",
            "type": "type_refractor",
            "optical_length": 0,
            "mass": 2200,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "M48",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "William_Optics_GT131": {
            "brand": "William Optics",
            "name": "GT131",
            "type": "type_refractor",
            "optical_length": 0,
            "mass": 6500,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "M68",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Askar_FMA_80": {
            "brand": "Askar",
            "name": "FMA 80",
            "type": "type_refractor",
            "optical_length": 0,
            "mass": 1100,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "M42",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Askar_FMA_107APO": {
            "brand": "Askar",
            "name": "FMA 107APO",
            "type": "type_refractor",
            "optical_length": 0,
            "mass": 4000,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "M54",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Askar_ACL130": {
            "brand": "Askar",
            "name": "ACL130",
            "type": "type_refractor",
            "optical_length": 0,
            "mass": 2000,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "M54",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Askar_V_40Q": {
            "brand": "Askar",
            "name": "V 40Q",
            "type": "type_refractor",
            "optical_length": 0,
            "mass": 1200,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "M42",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Askar_72Q": {
            "brand": "Askar",
            "name": "72Q",
            "type": "type_refractor",
            "optical_length": 0,
            "mass": 2400,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "M48",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Celestron_StarSense_Explorer_LT_114": {
            "brand": "Celestron",
            "name": "StarSense Explorer LT 114",
            "type": "type_telescope",
            "optical_length": 0,
            "mass": 4000,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": '2"',
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Celestron_StarSense_Explorer_DX_130": {
            "brand": "Celestron",
            "name": "StarSense Explorer DX 130",
            "type": "type_telescope",
            "optical_length": 0,
            "mass": 5000,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": '2"',
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Celestron_Inspire_100AZ": {
            "brand": "Celestron",
            "name": "Inspire 100AZ",
            "type": "type_telescope",
            "optical_length": 0,
            "mass": 3500,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": '2"',
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Celestron_AstroMaster_130EQ": {
            "brand": "Celestron",
            "name": "AstroMaster 130EQ",
            "type": "type_telescope",
            "optical_length": 0,
            "mass": 3800,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": '2"',
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Bresser_Messier_MC_100": {
            "brand": "Bresser",
            "name": "Messier MC-100",
            "type": "type_telescope",
            "optical_length": 0,
            "mass": 3000,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": '1.25"',
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Bresser_Messier_NT_130": {
            "brand": "Bresser",
            "name": "Messier NT-130",
            "type": "type_telescope",
            "optical_length": 0,
            "mass": 4200,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": '2"',
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Bresser_Arcturus_60_700_AZ": {
            "brand": "Bresser",
            "name": "Arcturus 60/700 AZ",
            "type": "type_telescope",
            "optical_length": 0,
            "mass": 1200,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": '1.25"',
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Bresser_Pollux_150_1400": {
            "brand": "Bresser",
            "name": "Pollux 150/1400",
            "type": "type_telescope",
            "optical_length": 0,
            "mass": 5500,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": '2"',
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Bresser_Bresser_Spica_130_1000": {
            "brand": "Bresser",
            "name": "Bresser Spica 130/1000",
            "type": "type_telescope",
            "optical_length": 0,
            "mass": 4500,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": '2"',
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Bresser_Messier_AR_102L": {
            "brand": "Bresser",
            "name": "Messier AR-102L",
            "type": "type_refractor",
            "optical_length": 0,
            "mass": 3800,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "M48",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "National_Geographic_Nat_Geo_76_700_Newton": {
            "brand": "National Geographic",
            "name": "Nat. Geo. 76/700 Newton",
            "type": "type_telescope",
            "optical_length": 0,
            "mass": 2500,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": '1.25"',
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "National_Geographic_Nat_Geo_114_900_Newton": {
            "brand": "National Geographic",
            "name": "Nat. Geo. 114/900 Newton",
            "type": "type_telescope",
            "optical_length": 0,
            "mass": 4000,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": '1.25"',
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "National_Geographic_Nat_Geo_130_650_Newton": {
            "brand": "National Geographic",
            "name": "Nat. Geo. 130/650 Newton",
            "type": "type_telescope",
            "optical_length": 0,
            "mass": 4500,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": '2"',
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Canon_EF_200mm_f_2_8L_II": {
            "brand": "Canon",
            "name": "EF 200mm f/2.8L II",
            "type": "type_camera_lens",
            "optical_length": 0,
            "mass": 795,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "EOS",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Canon_EF_135mm_f_2L": {
            "brand": "Canon",
            "name": "EF 135mm f/2L",
            "type": "type_camera_lens",
            "optical_length": 0,
            "mass": 750,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "EOS",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Canon_EF_100mm_f_2_8L_Macro_IS": {
            "brand": "Canon",
            "name": "EF 100mm f/2.8L Macro IS",
            "type": "type_camera_lens",
            "optical_length": 0,
            "mass": 625,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "EOS",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Canon_EF_50mm_f_1_4": {
            "brand": "Canon",
            "name": "EF 50mm f/1.4",
            "type": "type_camera_lens",
            "optical_length": 0,
            "mass": 290,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "EOS",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Canon_EF_50mm_f_1_8_STM": {
            "brand": "Canon",
            "name": "EF 50mm f/1.8 STM",
            "type": "type_camera_lens",
            "optical_length": 0,
            "mass": 160,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "EOS",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Canon_EF_85mm_f_1_8": {
            "brand": "Canon",
            "name": "EF 85mm f/1.8",
            "type": "type_camera_lens",
            "optical_length": 0,
            "mass": 425,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "EOS",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Canon_EF_24_70mm_f_2_8L_II": {
            "brand": "Canon",
            "name": "EF 24-70mm f/2.8L II",
            "type": "type_camera_lens",
            "optical_length": 0,
            "mass": 805,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "EOS",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Canon_EF_70_200mm_f_2_8L_IS_III": {
            "brand": "Canon",
            "name": "EF 70-200mm f/2.8L IS III",
            "type": "type_camera_lens",
            "optical_length": 0,
            "mass": 1480,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "EOS",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Canon_EF_400mm_f_5_6L": {
            "brand": "Canon",
            "name": "EF 400mm f/5.6L",
            "type": "type_camera_lens",
            "optical_length": 0,
            "mass": 1250,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "EOS",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Canon_EF_300mm_f_4L_IS": {
            "brand": "Canon",
            "name": "EF 300mm f/4L IS",
            "type": "type_camera_lens",
            "optical_length": 0,
            "mass": 1190,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "EOS",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Canon_EF_24mm_f_1_4L_II": {
            "brand": "Canon",
            "name": "EF 24mm f/1.4L II",
            "type": "type_camera_lens",
            "optical_length": 0,
            "mass": 650,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "EOS",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Canon_RF_200mm_f_2_8": {
            "brand": "Canon",
            "name": "RF 200mm f/2.8",
            "type": "type_camera_lens",
            "optical_length": 0,
            "mass": 800,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "Canon RF",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Canon_RF_135mm_f_1_8L": {
            "brand": "Canon",
            "name": "RF 135mm f/1.8L",
            "type": "type_camera_lens",
            "optical_length": 0,
            "mass": 935,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "Canon RF",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Canon_RF_85mm_f_1_2L": {
            "brand": "Canon",
            "name": "RF 85mm f/1.2L",
            "type": "type_camera_lens",
            "optical_length": 0,
            "mass": 1195,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "Canon RF",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Canon_RF_50mm_f_1_8_STM": {
            "brand": "Canon",
            "name": "RF 50mm f/1.8 STM",
            "type": "type_camera_lens",
            "optical_length": 0,
            "mass": 160,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "Canon RF",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Canon_RF_100_400mm_f_5_6_8": {
            "brand": "Canon",
            "name": "RF 100-400mm f/5.6-8",
            "type": "type_camera_lens",
            "optical_length": 0,
            "mass": 635,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "Canon RF",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Canon_RF_100mm_f_2_8L_Macro_IS": {
            "brand": "Canon",
            "name": "RF 100mm f/2.8L Macro IS",
            "type": "type_camera_lens",
            "optical_length": 0,
            "mass": 730,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "Canon RF",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Nikon_AF_S_200mm_f_2G_ED_VR": {
            "brand": "Nikon",
            "name": "AF-S 200mm f/2G ED VR",
            "type": "type_camera_lens",
            "optical_length": 0,
            "mass": 2930,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "Nikon F",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Nikon_AF_S_105mm_f_1_4E_ED": {
            "brand": "Nikon",
            "name": "AF-S 105mm f/1.4E ED",
            "type": "type_camera_lens",
            "optical_length": 0,
            "mass": 985,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "Nikon F",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Nikon_AF_S_50mm_f_1_8G": {
            "brand": "Nikon",
            "name": "AF-S 50mm f/1.8G",
            "type": "type_camera_lens",
            "optical_length": 0,
            "mass": 185,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "Nikon F",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Nikon_AF_S_85mm_f_1_8G": {
            "brand": "Nikon",
            "name": "AF-S 85mm f/1.8G",
            "type": "type_camera_lens",
            "optical_length": 0,
            "mass": 350,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "Nikon F",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Nikon_AF_S_300mm_f_4E_PF_ED_VR": {
            "brand": "Nikon",
            "name": "AF-S 300mm f/4E PF ED VR",
            "type": "type_camera_lens",
            "optical_length": 0,
            "mass": 755,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "Nikon F",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Nikon_AF_S_70_200mm_f_2_8E_FL_ED_VR": {
            "brand": "Nikon",
            "name": "AF-S 70-200mm f/2.8E FL ED VR",
            "type": "type_camera_lens",
            "optical_length": 0,
            "mass": 1430,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "Nikon F",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Nikon_Z_135mm_f_1_8_S_Plena": {
            "brand": "Nikon",
            "name": "Z 135mm f/1.8 S Plena",
            "type": "type_camera_lens",
            "optical_length": 0,
            "mass": 995,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "Nikon Z",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Nikon_Z_50mm_f_1_8_S": {
            "brand": "Nikon",
            "name": "Z 50mm f/1.8 S",
            "type": "type_camera_lens",
            "optical_length": 0,
            "mass": 415,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "Nikon Z",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Nikon_Z_85mm_f_1_8_S": {
            "brand": "Nikon",
            "name": "Z 85mm f/1.8 S",
            "type": "type_camera_lens",
            "optical_length": 0,
            "mass": 470,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "Nikon Z",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Nikon_Z_200_600mm_f_5_6_6_3_VR": {
            "brand": "Nikon",
            "name": "Z 200-600mm f/5.6-6.3 VR",
            "type": "type_camera_lens",
            "optical_length": 0,
            "mass": 2115,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "Nikon Z",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Nikon_Z_100_400mm_f_4_5_5_6_VR_S": {
            "brand": "Nikon",
            "name": "Z 100-400mm f/4.5-5.6 VR S",
            "type": "type_camera_lens",
            "optical_length": 0,
            "mass": 1355,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "Nikon Z",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Sony_FE_135mm_f_1_8_GM": {
            "brand": "Sony",
            "name": "FE 135mm f/1.8 GM",
            "type": "type_camera_lens",
            "optical_length": 0,
            "mass": 950,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "Sony E",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Sony_FE_200_600mm_f_5_6_6_3_G": {
            "brand": "Sony",
            "name": "FE 200-600mm f/5.6-6.3 G",
            "type": "type_camera_lens",
            "optical_length": 0,
            "mass": 2115,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "Sony E",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Sony_FE_85mm_f_1_4_GM": {
            "brand": "Sony",
            "name": "FE 85mm f/1.4 GM",
            "type": "type_camera_lens",
            "optical_length": 0,
            "mass": 820,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "Sony E",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Sony_FE_50mm_f_1_4_GM": {
            "brand": "Sony",
            "name": "FE 50mm f/1.4 GM",
            "type": "type_camera_lens",
            "optical_length": 0,
            "mass": 516,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "Sony E",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Sony_FE_100_400mm_f_4_5_5_6_GM": {
            "brand": "Sony",
            "name": "FE 100-400mm f/4.5-5.6 GM",
            "type": "type_camera_lens",
            "optical_length": 0,
            "mass": 1395,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "Sony E",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Sony_FE_70_200mm_f_2_8_GM_II": {
            "brand": "Sony",
            "name": "FE 70-200mm f/2.8 GM II",
            "type": "type_camera_lens",
            "optical_length": 0,
            "mass": 1045,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "Sony E",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Tokina_opera_50mm_f_1_4_Canon": {
            "brand": "Tokina",
            "name": "opera 50mm f/1.4 (Canon)",
            "type": "type_camera_lens",
            "optical_length": 0,
            "mass": 950,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "EOS",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Tokina_opera_50mm_f_1_4_Nikon": {
            "brand": "Tokina",
            "name": "opera 50mm f/1.4 (Nikon)",
            "type": "type_camera_lens",
            "optical_length": 0,
            "mass": 950,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "Nikon F",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Tokina_ATX_i_11_16mm_f_2_8_Canon": {
            "brand": "Tokina",
            "name": "ATX-i 11-16mm f/2.8 (Canon)",
            "type": "type_camera_lens",
            "optical_length": 0,
            "mass": 555,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "EOS",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Tokina_ATX_i_11_16mm_f_2_8_Nikon": {
            "brand": "Tokina",
            "name": "ATX-i 11-16mm f/2.8 (Nikon)",
            "type": "type_camera_lens",
            "optical_length": 0,
            "mass": 555,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "Nikon F",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Tokina_SZ_500mm_f_8_Reflex_MF": {
            "brand": "Tokina",
            "name": "SZ 500mm f/8 Reflex (MF)",
            "type": "type_camera_lens",
            "optical_length": 0,
            "mass": 530,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "M42",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Tamron_SP_150_600mm_f_5_6_3_G2_Canon": {
            "brand": "Tamron",
            "name": "SP 150-600mm f/5-6.3 G2 (Canon)",
            "type": "type_camera_lens",
            "optical_length": 0,
            "mass": 2010,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "EOS",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Tamron_SP_150_600mm_f_5_6_3_G2_Nikon": {
            "brand": "Tamron",
            "name": "SP 150-600mm f/5-6.3 G2 (Nikon)",
            "type": "type_camera_lens",
            "optical_length": 0,
            "mass": 2010,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "Nikon F",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Tamron_100_400mm_f_4_5_6_3_Sony_E": {
            "brand": "Tamron",
            "name": "100-400mm f/4.5-6.3 (Sony E)",
            "type": "type_camera_lens",
            "optical_length": 0,
            "mass": 1115,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "Sony E",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Tamron_150_500mm_f_5_6_7_Sony_E": {
            "brand": "Tamron",
            "name": "150-500mm f/5-6.7 (Sony E)",
            "type": "type_camera_lens",
            "optical_length": 0,
            "mass": 1725,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "Sony E",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Sigma_180mm_f_2_8_APO_Macro_Canon": {
            "brand": "Sigma",
            "name": "180mm f/2.8 APO Macro (Canon)",
            "type": "type_camera_lens",
            "optical_length": 0,
            "mass": 975,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "EOS",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Sigma_180mm_f_2_8_APO_Macro_Nikon": {
            "brand": "Sigma",
            "name": "180mm f/2.8 APO Macro (Nikon)",
            "type": "type_camera_lens",
            "optical_length": 0,
            "mass": 975,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "Nikon F",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Sigma_500mm_f_4_DG_OS_HSM": {
            "brand": "Sigma",
            "name": "500mm f/4 DG OS HSM",
            "type": "type_camera_lens",
            "optical_length": 0,
            "mass": 3310,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "EOS",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Sigma_60_600mm_f_4_5_6_3_DG_Canon": {
            "brand": "Sigma",
            "name": "60-600mm f/4.5-6.3 DG (Canon)",
            "type": "type_camera_lens",
            "optical_length": 0,
            "mass": 2700,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "EOS",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Sigma_100_400mm_f_5_6_3_DG_Canon": {
            "brand": "Sigma",
            "name": "100-400mm f/5-6.3 DG (Canon)",
            "type": "type_camera_lens",
            "optical_length": 0,
            "mass": 1160,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "EOS",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Sigma_150_600mm_f_5_6_3_DG_Nikon": {
            "brand": "Sigma",
            "name": "150-600mm f/5-6.3 DG (Nikon)",
            "type": "type_camera_lens",
            "optical_length": 0,
            "mass": 2860,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "Nikon F",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Sigma_150_600mm_f_5_6_3_Sony_E": {
            "brand": "Sigma",
            "name": "150-600mm f/5-6.3 (Sony E)",
            "type": "type_camera_lens",
            "optical_length": 0,
            "mass": 2100,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "Sony E",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Irix_150mm_f_2_8_Macro_Canon": {
            "brand": "Irix",
            "name": "150mm f/2.8 Macro (Canon)",
            "type": "type_camera_lens",
            "optical_length": 0,
            "mass": 831,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "EOS",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Irix_150mm_f_2_8_Macro_Nikon": {
            "brand": "Irix",
            "name": "150mm f/2.8 Macro (Nikon)",
            "type": "type_camera_lens",
            "optical_length": 0,
            "mass": 831,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "Nikon F",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Irix_45mm_f_1_4_Canon": {
            "brand": "Irix",
            "name": "45mm f/1.4 (Canon)",
            "type": "type_camera_lens",
            "optical_length": 0,
            "mass": 710,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "EOS",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Irix_11mm_f_4_Canon": {
            "brand": "Irix",
            "name": "11mm f/4 (Canon)",
            "type": "type_camera_lens",
            "optical_length": 0,
            "mass": 620,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "EOS",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Russian_Soviet_Jupiter_37A_135mm_f_3_5": {
            "brand": "Russian/Soviet",
            "name": "Jupiter-37A 135mm f/3.5",
            "type": "type_camera_lens",
            "optical_length": 0,
            "mass": 600,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "M42",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Russian_Soviet_MTO_1000A_1000mm_f_10": {
            "brand": "Russian/Soviet",
            "name": "MTO-1000A 1000mm f/10",
            "type": "type_camera_lens",
            "optical_length": 0,
            "mass": 1600,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "M42",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Russian_Soviet_Helios_44_2_58mm_f_2": {
            "brand": "Russian/Soviet",
            "name": "Helios 44-2 58mm f/2",
            "type": "type_camera_lens",
            "optical_length": 0,
            "mass": 230,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "M42",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Russian_Soviet_Tair_3S_300mm_f_4_5": {
            "brand": "Russian/Soviet",
            "name": "Tair-3S 300mm f/4.5",
            "type": "type_camera_lens",
            "optical_length": 0,
            "mass": 700,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "M42",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Sky_Watcher_Heritage_76_Mini": {
            "brand": "Sky-Watcher",
            "name": "Heritage 76 Mini",
            "type": "type_telescope",
            "optical_length": 0,
            "mass": 1600,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": '1.25"',
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Sky_Watcher_Heritage_100P": {
            "brand": "Sky-Watcher",
            "name": "Heritage 100P",
            "type": "type_telescope",
            "optical_length": 0,
            "mass": 2200,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": '1.25"',
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Orion_SkyLine_6_Dob": {
            "brand": "Orion",
            "name": 'SkyLine 6" Dob',
            "type": "type_telescope",
            "optical_length": 0,
            "mass": 6000,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": '2"',
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Orion_SkyLine_8_Dob": {
            "brand": "Orion",
            "name": 'SkyLine 8" Dob',
            "type": "type_telescope",
            "optical_length": 0,
            "mass": 8500,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": '2"',
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Orion_SkyLine_10_Dob": {
            "brand": "Orion",
            "name": 'SkyLine 10" Dob',
            "type": "type_telescope",
            "optical_length": 0,
            "mass": 11000,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": '2"',
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Orion_SkyLine_12_Dob": {
            "brand": "Orion",
            "name": 'SkyLine 12" Dob',
            "type": "type_telescope",
            "optical_length": 0,
            "mass": 15000,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": '2"',
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Explore_Scientific_Ultra_Light_10": {
            "brand": "Explore Scientific",
            "name": 'Ultra Light 10"',
            "type": "type_telescope",
            "optical_length": 0,
            "mass": 10500,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": '2"',
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Explore_Scientific_Ultra_Light_12": {
            "brand": "Explore Scientific",
            "name": 'Ultra Light 12"',
            "type": "type_telescope",
            "optical_length": 0,
            "mass": 14000,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": '2"',
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Explore_Scientific_Ultra_Light_16": {
            "brand": "Explore Scientific",
            "name": 'Ultra Light 16"',
            "type": "type_telescope",
            "optical_length": 0,
            "mass": 22000,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": '2"',
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Sky_Watcher_Heritage_130P_FlexTube": {
            "brand": "Sky-Watcher",
            "name": "Heritage 130P FlexTube",
            "type": "type_telescope",
            "optical_length": 0,
            "mass": 3200,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": '2"',
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Sky_Watcher_Heritage_150P_FlexTube": {
            "brand": "Sky-Watcher",
            "name": "Heritage 150P FlexTube",
            "type": "type_telescope",
            "optical_length": 0,
            "mass": 4800,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": '2"',
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Sky_Watcher_Star_Discovery_130i": {
            "brand": "Sky-Watcher",
            "name": "Star Discovery 130i",
            "type": "type_telescope",
            "optical_length": 0,
            "mass": 3300,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": '2"',
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Sky_Watcher_Star_Discovery_150i": {
            "brand": "Sky-Watcher",
            "name": "Star Discovery 150i",
            "type": "type_telescope",
            "optical_length": 0,
            "mass": 5000,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": '2"',
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Sky_Watcher_Starquest_130P": {
            "brand": "Sky-Watcher",
            "name": "Starquest 130P",
            "type": "type_telescope",
            "optical_length": 0,
            "mass": 3200,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": '2"',
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Sky_Watcher_Virtuoso_GTi_130P": {
            "brand": "Sky-Watcher",
            "name": "Virtuoso GTi 130P",
            "type": "type_telescope",
            "optical_length": 0,
            "mass": 3300,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": '2"',
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Sky_Watcher_Virtuoso_GTi_150P": {
            "brand": "Sky-Watcher",
            "name": "Virtuoso GTi 150P",
            "type": "type_telescope",
            "optical_length": 0,
            "mass": 4800,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": '2"',
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Celestron_Omni_XLT_102": {
            "brand": "Celestron",
            "name": "Omni XLT 102",
            "type": "type_telescope",
            "optical_length": 0,
            "mass": 3500,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": '2"',
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Celestron_Omni_XLT_120": {
            "brand": "Celestron",
            "name": "Omni XLT 120",
            "type": "type_telescope",
            "optical_length": 0,
            "mass": 5200,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": '2"',
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Celestron_Omni_XLT_127_SCT": {
            "brand": "Celestron",
            "name": "Omni XLT 127 SCT",
            "type": "type_telescope",
            "optical_length": 0,
            "mass": 5500,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "SC (Schmidt-Cassegrain)",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Celestron_Omni_XLT_150R": {
            "brand": "Celestron",
            "name": "Omni XLT 150R",
            "type": "type_telescope",
            "optical_length": 0,
            "mass": 5800,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": '2"',
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Celestron_Omni_XLT_150": {
            "brand": "Celestron",
            "name": "Omni XLT 150",
            "type": "type_telescope",
            "optical_length": 0,
            "mass": 5500,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": '2"',
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Celestron_StarBright_XLT_C6_A_XLT": {
            "brand": "Celestron",
            "name": "StarBright XLT C6-A-XLT",
            "type": "type_telescope",
            "optical_length": 0,
            "mass": 4200,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "SC (Schmidt-Cassegrain)",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Celestron_AstroFi_130": {
            "brand": "Celestron",
            "name": "AstroFi 130",
            "type": "type_telescope",
            "optical_length": 0,
            "mass": 3500,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": '2"',
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Celestron_FirstScope_76": {
            "brand": "Celestron",
            "name": "FirstScope 76",
            "type": "type_telescope",
            "optical_length": 0,
            "mass": 1000,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": '1.25"',
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Celestron_PowerSeeker_127EQ": {
            "brand": "Celestron",
            "name": "PowerSeeker 127EQ",
            "type": "type_telescope",
            "optical_length": 0,
            "mass": 3200,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": '1.25"',
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Lunt_Solar_LS60THa_60mm_H_alpha": {
            "brand": "Lunt Solar",
            "name": "LS60THa 60mm H-alpha",
            "type": "type_telescope",
            "optical_length": 0,
            "mass": 2500,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "M42",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Lunt_Solar_LS80THa_80mm_H_alpha": {
            "brand": "Lunt Solar",
            "name": "LS80THa 80mm H-alpha",
            "type": "type_telescope",
            "optical_length": 0,
            "mass": 4500,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "M48",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Lunt_Solar_LS100THa_100mm_H_alpha": {
            "brand": "Lunt Solar",
            "name": "LS100THa 100mm H-alpha",
            "type": "type_telescope",
            "optical_length": 0,
            "mass": 7000,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "M48",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Lunt_Solar_LS130THa_130mm_H_alpha": {
            "brand": "Lunt Solar",
            "name": "LS130THa 130mm H-alpha",
            "type": "type_telescope",
            "optical_length": 0,
            "mass": 12000,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "M54",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Lunt_Solar_LS50THa_50mm_H_alpha": {
            "brand": "Lunt Solar",
            "name": "LS50THa 50mm H-alpha",
            "type": "type_telescope",
            "optical_length": 0,
            "mass": 1800,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "M42",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Coronado_PST_40mm": {
            "brand": "Coronado",
            "name": "PST 40mm",
            "type": "type_telescope",
            "optical_length": 0,
            "mass": 1200,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": '1.25"',
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Coronado_SolarMax_II_60": {
            "brand": "Coronado",
            "name": "SolarMax II 60",
            "type": "type_telescope",
            "optical_length": 0,
            "mass": 3000,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "M42",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Coronado_SolarMax_II_90": {
            "brand": "Coronado",
            "name": "SolarMax II 90",
            "type": "type_telescope",
            "optical_length": 0,
            "mass": 5000,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "M48",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Coronado_SolarMax_III_70": {
            "brand": "Coronado",
            "name": "SolarMax III 70",
            "type": "type_telescope",
            "optical_length": 0,
            "mass": 4000,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "M48",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "DayStar_Solar_Scout_60mm": {
            "brand": "DayStar",
            "name": "Solar Scout 60mm",
            "type": "type_telescope",
            "optical_length": 0,
            "mass": 2000,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "M42",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "DayStar_Solar_Scout_80mm": {
            "brand": "DayStar",
            "name": "Solar Scout 80mm",
            "type": "type_telescope",
            "optical_length": 0,
            "mass": 3500,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "M48",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Orion_UK_VX6_6_Newt": {
            "brand": "Orion UK",
            "name": 'VX6 (6" Newt)',
            "type": "type_telescope",
            "optical_length": 0,
            "mass": 5200,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": '2"',
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Orion_UK_VX8_8_Newt": {
            "brand": "Orion UK",
            "name": 'VX8 (8" Newt)',
            "type": "type_telescope",
            "optical_length": 0,
            "mass": 8500,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": '2"',
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Orion_UK_VX10_10_Newt": {
            "brand": "Orion UK",
            "name": 'VX10 (10" Newt)',
            "type": "type_telescope",
            "optical_length": 0,
            "mass": 12000,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": '2"',
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Orion_UK_VX12_12_Newt": {
            "brand": "Orion UK",
            "name": 'VX12 (12" Newt)',
            "type": "type_telescope",
            "optical_length": 0,
            "mass": 16000,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": '2"',
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Orion_UK_Europa_200_f_4": {
            "brand": "Orion UK",
            "name": "Europa 200 f/4",
            "type": "type_telescope",
            "optical_length": 0,
            "mass": 7800,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "M48",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Orion_UK_ODK_10": {
            "brand": "Orion UK",
            "name": 'ODK 10"',
            "type": "type_telescope",
            "optical_length": 0,
            "mass": 11000,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "M68",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Orion_UK_ODK_12": {
            "brand": "Orion UK",
            "name": 'ODK 12"',
            "type": "type_telescope",
            "optical_length": 0,
            "mass": 15000,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "M68",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Orion_UK_ODK_14": {
            "brand": "Orion UK",
            "name": 'ODK 14"',
            "type": "type_telescope",
            "optical_length": 0,
            "mass": 20000,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "M68",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Orion_UK_ODK_16": {
            "brand": "Orion UK",
            "name": 'ODK 16"',
            "type": "type_telescope",
            "optical_length": 0,
            "mass": 26000,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "M84",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Orion_UK_AG12_12_AG": {
            "brand": "Orion UK",
            "name": 'AG12 (12" AG)',
            "type": "type_telescope",
            "optical_length": 0,
            "mass": 14000,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "M84",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "SkyVision_SkyVision_T500_20": {
            "brand": "SkyVision",
            "name": 'SkyVision T500 (20")',
            "type": "type_telescope",
            "optical_length": 0,
            "mass": 35000,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": '2"',
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "SkyVision_SkyVision_T600_24": {
            "brand": "SkyVision",
            "name": 'SkyVision T600 (24")',
            "type": "type_telescope",
            "optical_length": 0,
            "mass": 50000,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": '2"',
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "SkyVision_SkyVision_T700_28": {
            "brand": "SkyVision",
            "name": 'SkyVision T700 (28")',
            "type": "type_telescope",
            "optical_length": 0,
            "mass": 65000,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": '2"',
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "SkyVision_SkyVision_T400_16": {
            "brand": "SkyVision",
            "name": 'SkyVision T400 (16")',
            "type": "type_telescope",
            "optical_length": 0,
            "mass": 22000,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": '2"',
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "TS_Optics_TS_6_f_6_Newton": {
            "brand": "TS-Optics",
            "name": 'TS 6" f/6 Newton',
            "type": "type_telescope",
            "optical_length": 0,
            "mass": 4800,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": '2"',
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "TS_Optics_TS_8_f_5_Newton": {
            "brand": "TS-Optics",
            "name": 'TS 8" f/5 Newton',
            "type": "type_telescope",
            "optical_length": 0,
            "mass": 8200,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": '2"',
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "TS_Optics_TS_8_f_4_Newton": {
            "brand": "TS-Optics",
            "name": 'TS 8" f/4 Newton',
            "type": "type_telescope",
            "optical_length": 0,
            "mass": 8000,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "M48",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "TS_Optics_TS_10_f_4_Newton": {
            "brand": "TS-Optics",
            "name": 'TS 10" f/4 Newton',
            "type": "type_telescope",
            "optical_length": 0,
            "mass": 12000,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "M48",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "TS_Optics_TS_10_f_5_Newton": {
            "brand": "TS-Optics",
            "name": 'TS 10" f/5 Newton',
            "type": "type_telescope",
            "optical_length": 0,
            "mass": 11500,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": '2"',
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "TS_Optics_TS_12_f_4_Newton": {
            "brand": "TS-Optics",
            "name": 'TS 12" f/4 Newton',
            "type": "type_telescope",
            "optical_length": 0,
            "mass": 16000,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "M48",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "TS_Optics_TS_12_f_5_Dobson": {
            "brand": "TS-Optics",
            "name": 'TS 12" f/5 Dobson',
            "type": "type_telescope",
            "optical_length": 0,
            "mass": 15000,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": '2"',
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "TS_Optics_TS_14_f_4_6_Newton": {
            "brand": "TS-Optics",
            "name": 'TS 14" f/4.6 Newton',
            "type": "type_telescope",
            "optical_length": 0,
            "mass": 20000,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "M48",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Lacerta_72_432_APO": {
            "brand": "Lacerta",
            "name": "72/432 APO",
            "type": "type_refractor",
            "optical_length": 0,
            "mass": 2000,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "M48",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Lacerta_80_480_APO": {
            "brand": "Lacerta",
            "name": "80/480 APO",
            "type": "type_refractor",
            "optical_length": 0,
            "mass": 2500,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "M48",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Lacerta_102_714_APO": {
            "brand": "Lacerta",
            "name": "102/714 APO",
            "type": "type_refractor",
            "optical_length": 0,
            "mass": 4200,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "M48",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Lacerta_130_910_APO": {
            "brand": "Lacerta",
            "name": "130/910 APO",
            "type": "type_refractor",
            "optical_length": 0,
            "mass": 6500,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "M68",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Vaonis_Stellina": {
            "brand": "Vaonis",
            "name": "Stellina",
            "type": "type_telescope",
            "optical_length": 0,
            "mass": 4500,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "M42",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Vaonis_Vespera": {
            "brand": "Vaonis",
            "name": "Vespera",
            "type": "type_telescope",
            "optical_length": 0,
            "mass": 2500,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "M42",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Vaonis_Vespera_Pro": {
            "brand": "Vaonis",
            "name": "Vespera Pro",
            "type": "type_telescope",
            "optical_length": 0,
            "mass": 3500,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "M48",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Unistellar_eVscope_2": {
            "brand": "Unistellar",
            "name": "eVscope 2",
            "type": "type_telescope",
            "optical_length": 0,
            "mass": 9000,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Voigtlander_Nokton_50mm_f_1_2_Sony_E": {
            "brand": "Voigtlander",
            "name": "Nokton 50mm f/1.2 (Sony E)",
            "type": "type_camera_lens",
            "optical_length": 0,
            "mass": 480,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "Sony E",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Voigtlander_APO_Lanthar_110mm_f_2_5_Sony_E": {
            "brand": "Voigtlander",
            "name": "APO-Lanthar 110mm f/2.5 (Sony E)",
            "type": "type_camera_lens",
            "optical_length": 0,
            "mass": 756,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "Sony E",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "ID_7Artisans_50mm_f_1_05_Sony_E": {
            "brand": "7Artisans",
            "name": "50mm f/1.05 (Sony E)",
            "type": "type_camera_lens",
            "optical_length": 0,
            "mass": 570,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "Sony E",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Viltrox_85mm_f_1_8_II_Sony_E": {
            "brand": "Viltrox",
            "name": "85mm f/1.8 II (Sony E)",
            "type": "type_camera_lens",
            "optical_length": 0,
            "mass": 312,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "Sony E",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Celestron_NexStar_127SLT": {
            "brand": "Celestron",
            "name": "NexStar 127SLT",
            "type": "type_telescope",
            "optical_length": 0,
            "mass": 3200,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": '2"',
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Celestron_NexStar_130SLT": {
            "brand": "Celestron",
            "name": "NexStar 130SLT",
            "type": "type_telescope",
            "optical_length": 0,
            "mass": 3500,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": '2"',
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Celestron_Astro_Fi_5_SCT": {
            "brand": "Celestron",
            "name": "Astro-Fi 5 SCT",
            "type": "type_telescope",
            "optical_length": 0,
            "mass": 2700,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "SC (Schmidt-Cassegrain)",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Celestron_Astro_Fi_6_SCT": {
            "brand": "Celestron",
            "name": "Astro-Fi 6 SCT",
            "type": "type_telescope",
            "optical_length": 0,
            "mass": 3700,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "SC (Schmidt-Cassegrain)",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Celestron_AstroMaster_114EQ": {
            "brand": "Celestron",
            "name": "AstroMaster 114EQ",
            "type": "type_telescope",
            "optical_length": 0,
            "mass": 2400,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": '2"',
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Celestron_AstroMaster_70AZ": {
            "brand": "Celestron",
            "name": "AstroMaster 70AZ",
            "type": "type_telescope",
            "optical_length": 0,
            "mass": 1500,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": '1.25"',
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Celestron_AstroMaster_90AZ": {
            "brand": "Celestron",
            "name": "AstroMaster 90AZ",
            "type": "type_telescope",
            "optical_length": 0,
            "mass": 2200,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": '1.25"',
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Celestron_StarSense_Explorer_8_SCT": {
            "brand": "Celestron",
            "name": 'StarSense Explorer 8" SCT',
            "type": "type_telescope",
            "optical_length": 0,
            "mass": 5700,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "SC (Schmidt-Cassegrain)",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Celestron_StarSense_Explorer_LT_80AZ": {
            "brand": "Celestron",
            "name": "StarSense Explorer LT 80AZ",
            "type": "type_telescope",
            "optical_length": 0,
            "mass": 1800,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": '1.25"',
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Celestron_Advanced_VX_6_SCT": {
            "brand": "Celestron",
            "name": "Advanced VX 6 SCT",
            "type": "type_telescope",
            "optical_length": 0,
            "mass": 4000,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "SC (Schmidt-Cassegrain)",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Celestron_Advanced_VX_9_25_SCT": {
            "brand": "Celestron",
            "name": "Advanced VX 9.25 SCT",
            "type": "type_telescope",
            "optical_length": 0,
            "mass": 9600,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "SC (Schmidt-Cassegrain)",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Celestron_Advanced_VX_11_SCT": {
            "brand": "Celestron",
            "name": "Advanced VX 11 SCT",
            "type": "type_telescope",
            "optical_length": 0,
            "mass": 12500,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "SC (Schmidt-Cassegrain)",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Meade_LightBridge_10_Dob": {
            "brand": "Meade",
            "name": 'LightBridge 10" Dob',
            "type": "type_telescope",
            "optical_length": 0,
            "mass": 10000,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": '2"',
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Meade_LightBridge_12_Dob": {
            "brand": "Meade",
            "name": 'LightBridge 12" Dob',
            "type": "type_telescope",
            "optical_length": 0,
            "mass": 14000,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": '2"',
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Meade_LightBridge_16_Dob": {
            "brand": "Meade",
            "name": 'LightBridge 16" Dob',
            "type": "type_telescope",
            "optical_length": 0,
            "mass": 24000,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": '2"',
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Meade_LightBridge_8_Dob": {
            "brand": "Meade",
            "name": 'LightBridge 8" Dob',
            "type": "type_telescope",
            "optical_length": 0,
            "mass": 7000,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": '2"',
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Meade_LX90_ACF_8": {
            "brand": "Meade",
            "name": 'LX90 ACF 8"',
            "type": "type_telescope",
            "optical_length": 0,
            "mass": 5800,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "SC (Schmidt-Cassegrain)",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Meade_LX90_ACF_10": {
            "brand": "Meade",
            "name": 'LX90 ACF 10"',
            "type": "type_telescope",
            "optical_length": 0,
            "mass": 10000,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "SC (Schmidt-Cassegrain)",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Meade_LX90_ACF_12": {
            "brand": "Meade",
            "name": 'LX90 ACF 12"',
            "type": "type_telescope",
            "optical_length": 0,
            "mass": 13000,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "SC (Schmidt-Cassegrain)",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Meade_StarNavigator_NG_102mm": {
            "brand": "Meade",
            "name": "StarNavigator NG 102mm",
            "type": "type_telescope",
            "optical_length": 0,
            "mass": 2800,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": '2"',
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Meade_StarNavigator_NG_130mm": {
            "brand": "Meade",
            "name": "StarNavigator NG 130mm",
            "type": "type_telescope",
            "optical_length": 0,
            "mass": 3200,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": '2"',
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Meade_Polaris_127mm_EQ": {
            "brand": "Meade",
            "name": "Polaris 127mm EQ",
            "type": "type_telescope",
            "optical_length": 0,
            "mass": 3600,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": '2"',
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Meade_Polaris_130mm_EQ": {
            "brand": "Meade",
            "name": "Polaris 130mm EQ",
            "type": "type_telescope",
            "optical_length": 0,
            "mass": 3500,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": '2"',
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Meade_S102_102mm_APO": {
            "brand": "Meade",
            "name": "S102 102mm APO",
            "type": "type_refractor",
            "optical_length": 0,
            "mass": 4500,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "M48",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Meade_S130_130mm_APO": {
            "brand": "Meade",
            "name": "S130 130mm APO",
            "type": "type_refractor",
            "optical_length": 0,
            "mass": 7000,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "M48",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Sky_Watcher_Star_Adventurer_GTi_80ED": {
            "brand": "Sky-Watcher",
            "name": "Star Adventurer GTi 80ED",
            "type": "type_telescope",
            "optical_length": 0,
            "mass": 2600,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": '2"',
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Sky_Watcher_Starquest_80MC": {
            "brand": "Sky-Watcher",
            "name": "Starquest 80MC",
            "type": "type_telescope",
            "optical_length": 0,
            "mass": 1800,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": '2"',
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Sky_Watcher_Heritage_P130_FlexTube": {
            "brand": "Sky-Watcher",
            "name": "Heritage P130 FlexTube",
            "type": "type_telescope",
            "optical_length": 0,
            "mass": 3100,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": '2"',
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Sky_Watcher_Skyliner_200P_FlexTube": {
            "brand": "Sky-Watcher",
            "name": "Skyliner 200P FlexTube",
            "type": "type_telescope",
            "optical_length": 0,
            "mass": 8600,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": '2"',
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Sky_Watcher_Skyliner_250P_FlexTube": {
            "brand": "Sky-Watcher",
            "name": "Skyliner 250P FlexTube",
            "type": "type_telescope",
            "optical_length": 0,
            "mass": 11700,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": '2"',
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Sky_Watcher_Skyliner_300P_FlexTube": {
            "brand": "Sky-Watcher",
            "name": "Skyliner 300P FlexTube",
            "type": "type_telescope",
            "optical_length": 0,
            "mass": 16200,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": '2"',
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Sky_Watcher_Skyliner_350P_FlexTube": {
            "brand": "Sky-Watcher",
            "name": "Skyliner 350P FlexTube",
            "type": "type_telescope",
            "optical_length": 0,
            "mass": 19000,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": '2"',
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Sky_Watcher_Stargate_500P_Truss_Dob": {
            "brand": "Sky-Watcher",
            "name": "Stargate 500P Truss Dob",
            "type": "type_telescope",
            "optical_length": 0,
            "mass": 35000,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": '2"',
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Sky_Watcher_Stargate_450P_Truss_Dob": {
            "brand": "Sky-Watcher",
            "name": "Stargate 450P Truss Dob",
            "type": "type_telescope",
            "optical_length": 0,
            "mass": 28000,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": '2"',
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Sky_Watcher_Evostar_150DX": {
            "brand": "Sky-Watcher",
            "name": "Evostar 150DX",
            "type": "type_refractor",
            "optical_length": 0,
            "mass": 8000,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "M48",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Sky_Watcher_Equinox_80": {
            "brand": "Sky-Watcher",
            "name": "Equinox 80",
            "type": "type_refractor",
            "optical_length": 0,
            "mass": 3000,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "M48",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Sky_Watcher_Equinox_100": {
            "brand": "Sky-Watcher",
            "name": "Equinox 100",
            "type": "type_refractor",
            "optical_length": 0,
            "mass": 4500,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "M48",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Sky_Watcher_Equinox_120": {
            "brand": "Sky-Watcher",
            "name": "Equinox 120",
            "type": "type_refractor",
            "optical_length": 0,
            "mass": 6500,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "M48",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Orion_SpaceProbe_130ST_EQ": {
            "brand": "Orion",
            "name": "SpaceProbe 130ST EQ",
            "type": "type_telescope",
            "optical_length": 0,
            "mass": 3800,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": '2"',
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Orion_StarBlast_4_5_EQ": {
            "brand": "Orion",
            "name": "StarBlast 4.5 EQ",
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
        "Orion_StarBlast_6": {
            "brand": "Orion",
            "name": "StarBlast 6",
            "type": "type_telescope",
            "optical_length": 0,
            "mass": 4000,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": '2"',
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Orion_AstroView_6_EQ": {
            "brand": "Orion",
            "name": "AstroView 6 EQ",
            "type": "type_telescope",
            "optical_length": 0,
            "mass": 4200,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": '2"',
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Orion_SkyQuest_XT6_Classic_Dob": {
            "brand": "Orion",
            "name": "SkyQuest XT6 Classic Dob",
            "type": "type_telescope",
            "optical_length": 0,
            "mass": 6000,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": '2"',
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Orion_SkyQuest_XX16g_Dob": {
            "brand": "Orion",
            "name": "SkyQuest XX16g Dob",
            "type": "type_telescope",
            "optical_length": 0,
            "mass": 28000,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": '2"',
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Orion_SkyLine_6_Dob_1": {
            "brand": "Orion",
            "name": "SkyLine 6 Dob",
            "type": "type_telescope",
            "optical_length": 0,
            "mass": 5000,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": '2"',
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Orion_SkyLine_8_Dob_1": {
            "brand": "Orion",
            "name": "SkyLine 8 Dob",
            "type": "type_telescope",
            "optical_length": 0,
            "mass": 7500,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": '2"',
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Orion_SkyLine_10_Dob_1": {
            "brand": "Orion",
            "name": "SkyLine 10 Dob",
            "type": "type_telescope",
            "optical_length": 0,
            "mass": 10500,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": '2"',
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Orion_SkyLine_12_Dob_1": {
            "brand": "Orion",
            "name": "SkyLine 12 Dob",
            "type": "type_telescope",
            "optical_length": 0,
            "mass": 14000,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": '2"',
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Orion_SkyView_Pro_8": {
            "brand": "Orion",
            "name": "SkyView Pro 8",
            "type": "type_telescope",
            "optical_length": 0,
            "mass": 7500,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": '2"',
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Orion_ED_80T_CF_Apochromat": {
            "brand": "Orion",
            "name": "ED 80T CF Apochromat",
            "type": "type_refractor",
            "optical_length": 0,
            "mass": 3000,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "M48",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Orion_EON_115mm_ED_Apochromat": {
            "brand": "Orion",
            "name": "EON 115mm ED Apochromat",
            "type": "type_refractor",
            "optical_length": 0,
            "mass": 5000,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "M48",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Bresser_Messier_AR_127S": {
            "brand": "Bresser",
            "name": "Messier AR-127S",
            "type": "type_refractor",
            "optical_length": 0,
            "mass": 4500,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "M48",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Bresser_Messier_NT_150S_6_f_5": {
            "brand": "Bresser",
            "name": 'Messier NT-150S (6" f/5)',
            "type": "type_telescope",
            "optical_length": 0,
            "mass": 5200,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": '2"',
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Bresser_Messier_Dobson_8": {
            "brand": "Bresser",
            "name": 'Messier Dobson 8"',
            "type": "type_telescope",
            "optical_length": 0,
            "mass": 7000,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": '2"',
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Bresser_Messier_Dobson_10": {
            "brand": "Bresser",
            "name": 'Messier Dobson 10"',
            "type": "type_telescope",
            "optical_length": 0,
            "mass": 10000,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": '2"',
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Bresser_Messier_Dobson_12": {
            "brand": "Bresser",
            "name": 'Messier Dobson 12"',
            "type": "type_telescope",
            "optical_length": 0,
            "mass": 14000,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": '2"',
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Bresser_Pollux_150_1400_EQ3": {
            "brand": "Bresser",
            "name": "Pollux 150/1400 EQ3",
            "type": "type_telescope",
            "optical_length": 0,
            "mass": 4000,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": '2"',
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Bresser_Lyra_70_900_EQ": {
            "brand": "Bresser",
            "name": "Lyra 70/900 EQ",
            "type": "type_refractor",
            "optical_length": 0,
            "mass": 1200,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "M48",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Bresser_Jupiter_70_700_AZ": {
            "brand": "Bresser",
            "name": "Jupiter 70/700 AZ",
            "type": "type_refractor",
            "optical_length": 0,
            "mass": 1000,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "M48",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Bresser_Taurus_90_900_NG": {
            "brand": "Bresser",
            "name": "Taurus 90/900 NG",
            "type": "type_refractor",
            "optical_length": 0,
            "mass": 2200,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "M48",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Vixen_A62SS": {
            "brand": "Vixen",
            "name": "A62SS",
            "type": "type_refractor",
            "optical_length": 0,
            "mass": 1100,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "M42",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Vixen_A70Lf": {
            "brand": "Vixen",
            "name": "A70Lf",
            "type": "type_refractor",
            "optical_length": 0,
            "mass": 1400,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "M42",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Vixen_A105M": {
            "brand": "Vixen",
            "name": "A105M",
            "type": "type_refractor",
            "optical_length": 0,
            "mass": 3500,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "M42",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Vixen_VSD100_F3_8_V2": {
            "brand": "Vixen",
            "name": "VSD100 F3.8 V2",
            "type": "type_refractor",
            "optical_length": 0,
            "mass": 4500,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "M48",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Vixen_R130Sf": {
            "brand": "Vixen",
            "name": "R130Sf",
            "type": "type_telescope",
            "optical_length": 0,
            "mass": 3000,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "M42",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Vixen_VMC95L": {
            "brand": "Vixen",
            "name": "VMC95L",
            "type": "type_telescope",
            "optical_length": 0,
            "mass": 2000,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "M42",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Vixen_VMC110L": {
            "brand": "Vixen",
            "name": "VMC110L",
            "type": "type_telescope",
            "optical_length": 0,
            "mass": 2800,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "M42",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Vixen_VMC260L": {
            "brand": "Vixen",
            "name": "VMC260L",
            "type": "type_telescope",
            "optical_length": 0,
            "mass": 12000,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "M54",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Explore_Scientific_AR102_Air_Spaced_Doublet": {
            "brand": "Explore Scientific",
            "name": "AR102 Air-Spaced Doublet",
            "type": "type_refractor",
            "optical_length": 0,
            "mass": 2500,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "M48",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Explore_Scientific_AR127_Air_Spaced": {
            "brand": "Explore Scientific",
            "name": "AR127 Air-Spaced",
            "type": "type_refractor",
            "optical_length": 0,
            "mass": 4000,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "M48",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Explore_Scientific_AR152_Air_Spaced": {
            "brand": "Explore Scientific",
            "name": "AR152 Air-Spaced",
            "type": "type_refractor",
            "optical_length": 0,
            "mass": 6000,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "M48",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Explore_Scientific_FirstLight_130mm_f_4_6_Newton": {
            "brand": "Explore Scientific",
            "name": "FirstLight 130mm f/4.6 Newton",
            "type": "type_telescope",
            "optical_length": 0,
            "mass": 4000,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "M48",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Explore_Scientific_FirstLight_150mm_f_5_Newton": {
            "brand": "Explore Scientific",
            "name": "FirstLight 150mm f/5 Newton",
            "type": "type_telescope",
            "optical_length": 0,
            "mass": 5000,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "M48",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Explore_Scientific_FirstLight_200mm_f_5_Newton": {
            "brand": "Explore Scientific",
            "name": "FirstLight 200mm f/5 Newton",
            "type": "type_telescope",
            "optical_length": 0,
            "mass": 8000,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "M48",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Explore_Scientific_FirstLight_102mm_Mak": {
            "brand": "Explore Scientific",
            "name": "FirstLight 102mm Mak",
            "type": "type_telescope",
            "optical_length": 0,
            "mass": 2800,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": '1.25"',
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Explore_Scientific_FirstLight_127mm_Mak": {
            "brand": "Explore Scientific",
            "name": "FirstLight 127mm Mak",
            "type": "type_telescope",
            "optical_length": 0,
            "mass": 3500,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": '1.25"',
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Explore_Scientific_FirstLight_80mm_APO": {
            "brand": "Explore Scientific",
            "name": "FirstLight 80mm APO",
            "type": "type_refractor",
            "optical_length": 0,
            "mass": 2800,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "M48",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Explore_Scientific_FirstLight_102mm_APO": {
            "brand": "Explore Scientific",
            "name": "FirstLight 102mm APO",
            "type": "type_refractor",
            "optical_length": 0,
            "mass": 4200,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "M48",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Explore_Scientific_ED_APO_80mm_CF": {
            "brand": "Explore Scientific",
            "name": "ED APO 80mm CF",
            "type": "type_refractor",
            "optical_length": 0,
            "mass": 3200,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "M48",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Explore_Scientific_ED_APO_102mm_CF": {
            "brand": "Explore Scientific",
            "name": "ED APO 102mm CF",
            "type": "type_refractor",
            "optical_length": 0,
            "mass": 4800,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "M48",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Explore_Scientific_ED_APO_127mm_CF": {
            "brand": "Explore Scientific",
            "name": "ED APO 127mm CF",
            "type": "type_refractor",
            "optical_length": 0,
            "mass": 7500,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "M68",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Explore_Scientific_ED_APO_152mm_CF": {
            "brand": "Explore Scientific",
            "name": "ED APO 152mm CF",
            "type": "type_refractor",
            "optical_length": 0,
            "mass": 12000,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "M68",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "GSO_Newton_6_f_5": {
            "brand": "GSO",
            "name": 'Newton 6" f/5',
            "type": "type_telescope",
            "optical_length": 0,
            "mass": 4500,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": '2"',
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "GSO_Newton_8_f_4": {
            "brand": "GSO",
            "name": 'Newton 8" f/4',
            "type": "type_telescope",
            "optical_length": 0,
            "mass": 7500,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": '2"',
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "GSO_Newton_8_f_5": {
            "brand": "GSO",
            "name": 'Newton 8" f/5',
            "type": "type_telescope",
            "optical_length": 0,
            "mass": 8000,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": '2"',
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "GSO_Newton_10_f_5": {
            "brand": "GSO",
            "name": 'Newton 10" f/5',
            "type": "type_telescope",
            "optical_length": 0,
            "mass": 11000,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": '2"',
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "GSO_Newton_12_f_5": {
            "brand": "GSO",
            "name": 'Newton 12" f/5',
            "type": "type_telescope",
            "optical_length": 0,
            "mass": 15000,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": '2"',
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "GSO_Newton_16_f_4_5": {
            "brand": "GSO",
            "name": 'Newton 16" f/4.5',
            "type": "type_telescope",
            "optical_length": 0,
            "mass": 26000,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": '2"',
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "GSO_Newton_6_f_8_Dob": {
            "brand": "GSO",
            "name": 'Newton 6" f/8 Dob',
            "type": "type_telescope",
            "optical_length": 0,
            "mass": 5500,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": '2"',
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "GSO_Newton_8_f_6_Dob": {
            "brand": "GSO",
            "name": 'Newton 8" f/6 Dob',
            "type": "type_telescope",
            "optical_length": 0,
            "mass": 8000,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": '2"',
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "GSO_Newton_10_f_6_Dob": {
            "brand": "GSO",
            "name": 'Newton 10" f/6 Dob',
            "type": "type_telescope",
            "optical_length": 0,
            "mass": 11500,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": '2"',
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "GSO_Newton_12_f_5_Dob": {
            "brand": "GSO",
            "name": 'Newton 12" f/5 Dob',
            "type": "type_telescope",
            "optical_length": 0,
            "mass": 15000,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": '2"',
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "GSO_GSO_80ED": {
            "brand": "GSO",
            "name": "GSO 80ED",
            "type": "type_refractor",
            "optical_length": 0,
            "mass": 2400,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "M48",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "GSO_GSO_102ED": {
            "brand": "GSO",
            "name": "GSO 102ED",
            "type": "type_refractor",
            "optical_length": 0,
            "mass": 3800,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "M48",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "TPO_RC_12": {
            "brand": "TPO",
            "name": 'RC 12"',
            "type": "type_telescope",
            "optical_length": 0,
            "mass": 17000,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "M84",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "TPO_RC_14": {
            "brand": "TPO",
            "name": 'RC 14"',
            "type": "type_telescope",
            "optical_length": 0,
            "mass": 22000,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "M84",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "TPO_TPO_6_f_4_Newton": {
            "brand": "TPO",
            "name": 'TPO 6" f/4 Newton',
            "type": "type_telescope",
            "optical_length": 0,
            "mass": 4800,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "M48",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "TPO_TPO_8_f_4_Newton": {
            "brand": "TPO",
            "name": 'TPO 8" f/4 Newton',
            "type": "type_telescope",
            "optical_length": 0,
            "mass": 7800,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "M48",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "TPO_TPO_10_f_4_Newton": {
            "brand": "TPO",
            "name": 'TPO 10" f/4 Newton',
            "type": "type_telescope",
            "optical_length": 0,
            "mass": 12000,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "M48",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "TPO_TPO_80mm_ED_APO": {
            "brand": "TPO",
            "name": "TPO 80mm ED APO",
            "type": "type_refractor",
            "optical_length": 0,
            "mass": 2600,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "M48",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "TPO_TPO_102mm_ED_APO": {
            "brand": "TPO",
            "name": "TPO 102mm ED APO",
            "type": "type_refractor",
            "optical_length": 0,
            "mass": 4200,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "M48",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "TPO_UltraWide_6_f_2_8_Astrograph": {
            "brand": "TPO",
            "name": 'UltraWide 6" f/2.8 Astrograph',
            "type": "type_telescope",
            "optical_length": 0,
            "mass": 6000,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "M54",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Apertura_AD6_Dobsonian": {
            "brand": "Apertura",
            "name": "AD6 Dobsonian",
            "type": "type_telescope",
            "optical_length": 0,
            "mass": 5000,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": '2"',
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Zhumell_Z6_Dobsonian": {
            "brand": "Zhumell",
            "name": "Z6 Dobsonian",
            "type": "type_telescope",
            "optical_length": 0,
            "mass": 5000,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": '2"',
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Apertura_AD8_Dobsonian": {
            "brand": "Apertura",
            "name": "AD8 Dobsonian",
            "type": "type_telescope",
            "optical_length": 0,
            "mass": 7500,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": '2"',
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Zhumell_Z8_Dobsonian": {
            "brand": "Zhumell",
            "name": "Z8 Dobsonian",
            "type": "type_telescope",
            "optical_length": 0,
            "mass": 7500,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": '2"',
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Apertura_AD10_Dobsonian": {
            "brand": "Apertura",
            "name": "AD10 Dobsonian",
            "type": "type_telescope",
            "optical_length": 0,
            "mass": 10000,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": '2"',
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Zhumell_Z10_Dobsonian": {
            "brand": "Zhumell",
            "name": "Z10 Dobsonian",
            "type": "type_telescope",
            "optical_length": 0,
            "mass": 10000,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": '2"',
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Apertura_AD12_Dobsonian": {
            "brand": "Apertura",
            "name": "AD12 Dobsonian",
            "type": "type_telescope",
            "optical_length": 0,
            "mass": 14000,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": '2"',
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Zhumell_Z12_Dobsonian": {
            "brand": "Zhumell",
            "name": "Z12 Dobsonian",
            "type": "type_telescope",
            "optical_length": 0,
            "mass": 14000,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": '2"',
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Apertura_AD14_Dobsonian": {
            "brand": "Apertura",
            "name": "AD14 Dobsonian",
            "type": "type_telescope",
            "optical_length": 0,
            "mass": 19000,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": '2"',
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Zhumell_Z14_Dobsonian": {
            "brand": "Zhumell",
            "name": "Z14 Dobsonian",
            "type": "type_telescope",
            "optical_length": 0,
            "mass": 19000,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": '2"',
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Apertura_AD16_Dobsonian": {
            "brand": "Apertura",
            "name": "AD16 Dobsonian",
            "type": "type_telescope",
            "optical_length": 0,
            "mass": 27000,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": '2"',
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Zhumell_Z16_Dobsonian": {
            "brand": "Zhumell",
            "name": "Z16 Dobsonian",
            "type": "type_telescope",
            "optical_length": 0,
            "mass": 27000,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": '2"',
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Sky_Watcher_SkyMax_102": {
            "brand": "Sky-Watcher",
            "name": "SkyMax 102",
            "type": "type_telescope",
            "optical_length": 0,
            "mass": 2200,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": '1.25"',
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Sky_Watcher_SkyMax_127": {
            "brand": "Sky-Watcher",
            "name": "SkyMax 127",
            "type": "type_telescope",
            "optical_length": 0,
            "mass": 3400,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": '1.25"',
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Sky_Watcher_SkyMax_150_Pro": {
            "brand": "Sky-Watcher",
            "name": "SkyMax 150 Pro",
            "type": "type_telescope",
            "optical_length": 0,
            "mass": 5200,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "SC (Schmidt-Cassegrain)",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Sky_Watcher_SkyMax_180_Pro": {
            "brand": "Sky-Watcher",
            "name": "SkyMax 180 Pro",
            "type": "type_telescope",
            "optical_length": 0,
            "mass": 6500,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "SC (Schmidt-Cassegrain)",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Vaonis_Hyperia": {
            "brand": "Vaonis",
            "name": "Hyperia",
            "type": "type_telescope",
            "optical_length": 0,
            "mass": 6000,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "M42",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Unistellar_eQuinox_2": {
            "brand": "Unistellar",
            "name": "eQuinox 2",
            "type": "type_telescope",
            "optical_length": 0,
            "mass": 7000,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "M42",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Unistellar_Odyssey": {
            "brand": "Unistellar",
            "name": "Odyssey",
            "type": "type_telescope",
            "optical_length": 0,
            "mass": 5000,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "M42",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Unistellar_Odyssey_Pro": {
            "brand": "Unistellar",
            "name": "Odyssey Pro",
            "type": "type_telescope",
            "optical_length": 0,
            "mass": 6000,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "M42",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "TeleVue_NP101is": {
            "brand": "TeleVue",
            "name": "NP101is",
            "type": "type_refractor",
            "optical_length": 0,
            "mass": 4200,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "M48",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "TeleVue_NP127fli": {
            "brand": "TeleVue",
            "name": "NP127fli",
            "type": "type_refractor",
            "optical_length": 0,
            "mass": 6500,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "M68",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "TeleVue_TV_60": {
            "brand": "TeleVue",
            "name": "TV-60",
            "type": "type_refractor",
            "optical_length": 0,
            "mass": 900,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "M48",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "TeleVue_TV_76": {
            "brand": "TeleVue",
            "name": "TV-76",
            "type": "type_refractor",
            "optical_length": 0,
            "mass": 1500,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "M48",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "TeleVue_TV_85": {
            "brand": "TeleVue",
            "name": "TV-85",
            "type": "type_refractor",
            "optical_length": 0,
            "mass": 2200,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "M48",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "TeleVue_TV_102": {
            "brand": "TeleVue",
            "name": "TV-102",
            "type": "type_refractor",
            "optical_length": 0,
            "mass": 3800,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "M48",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "TeleVue_TV_NP127is": {
            "brand": "TeleVue",
            "name": "TV-NP127is",
            "type": "type_refractor",
            "optical_length": 0,
            "mass": 6800,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "M68",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "TeleVue_TV_NP101": {
            "brand": "TeleVue",
            "name": "TV-NP101",
            "type": "type_refractor",
            "optical_length": 0,
            "mass": 4000,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "M48",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Lunt_Solar_LS60THa": {
            "brand": "Lunt Solar",
            "name": "LS60THa",
            "type": "type_refractor",
            "optical_length": 0,
            "mass": 2000,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "M42",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Lunt_Solar_LS80THa": {
            "brand": "Lunt Solar",
            "name": "LS80THa",
            "type": "type_refractor",
            "optical_length": 0,
            "mass": 3500,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "M48",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Lunt_Solar_LS100THa": {
            "brand": "Lunt Solar",
            "name": "LS100THa",
            "type": "type_refractor",
            "optical_length": 0,
            "mass": 5500,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "M48",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Lunt_Solar_LS130THa": {
            "brand": "Lunt Solar",
            "name": "LS130THa",
            "type": "type_refractor",
            "optical_length": 0,
            "mass": 8000,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "M48",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Lunt_Solar_LS152THa": {
            "brand": "Lunt Solar",
            "name": "LS152THa",
            "type": "type_refractor",
            "optical_length": 0,
            "mass": 12000,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "M48",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Lunt_Solar_LS50C_Ca_K": {
            "brand": "Lunt Solar",
            "name": "LS50C (Ca-K)",
            "type": "type_refractor",
            "optical_length": 0,
            "mass": 1200,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "M42",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Lunt_Solar_LS60MT": {
            "brand": "Lunt Solar",
            "name": "LS60MT",
            "type": "type_refractor",
            "optical_length": 0,
            "mass": 2200,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "M42",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Lunt_Solar_LS80MT": {
            "brand": "Lunt Solar",
            "name": "LS80MT",
            "type": "type_refractor",
            "optical_length": 0,
            "mass": 3800,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "M48",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "DayStar_SOLO_60_SE": {
            "brand": "DayStar",
            "name": "SOLO 60 SE",
            "type": "type_refractor",
            "optical_length": 0,
            "mass": 1800,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "M48",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "DayStar_SOLO_60_PE": {
            "brand": "DayStar",
            "name": "SOLO 60 PE",
            "type": "type_refractor",
            "optical_length": 0,
            "mass": 2200,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "M48",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "DayStar_SOLO_80_SE": {
            "brand": "DayStar",
            "name": "SOLO 80 SE",
            "type": "type_refractor",
            "optical_length": 0,
            "mass": 3000,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "M48",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "DayStar_SolaREDi_66": {
            "brand": "DayStar",
            "name": "SolaREDi 66",
            "type": "type_refractor",
            "optical_length": 0,
            "mass": 1200,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "M48",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "DayStar_SolaREDi_127": {
            "brand": "DayStar",
            "name": "SolaREDi 127",
            "type": "type_refractor",
            "optical_length": 0,
            "mass": 4500,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "M48",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Coronado_PST": {
            "brand": "Coronado",
            "name": "PST",
            "type": "type_refractor",
            "optical_length": 0,
            "mass": 700,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "M42",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Coronado_SolarMax_III_90": {
            "brand": "Coronado",
            "name": "SolarMax III 90",
            "type": "type_refractor",
            "optical_length": 0,
            "mass": 2500,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "M48",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Coronado_SolarMax_II_60_BF15": {
            "brand": "Coronado",
            "name": "SolarMax II 60 BF15",
            "type": "type_refractor",
            "optical_length": 0,
            "mass": 1500,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "M48",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Canon_EF_200mm_f_2_8L_II_USM": {
            "brand": "Canon",
            "name": "EF 200mm f/2.8L II USM",
            "type": "type_camera_lens",
            "optical_length": 0,
            "mass": 795,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "EOS",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Canon_EF_50mm_f_1_4_USM": {
            "brand": "Canon",
            "name": "EF 50mm f/1.4 USM",
            "type": "type_camera_lens",
            "optical_length": 0,
            "mass": 290,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "EOS",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Canon_EF_50mm_f_1_2L_USM": {
            "brand": "Canon",
            "name": "EF 50mm f/1.2L USM",
            "type": "type_camera_lens",
            "optical_length": 0,
            "mass": 580,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "EOS",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Canon_EF_85mm_f_1_4L_IS_USM": {
            "brand": "Canon",
            "name": "EF 85mm f/1.4L IS USM",
            "type": "type_camera_lens",
            "optical_length": 0,
            "mass": 950,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "EOS",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Canon_EF_85mm_f_1_8_USM": {
            "brand": "Canon",
            "name": "EF 85mm f/1.8 USM",
            "type": "type_camera_lens",
            "optical_length": 0,
            "mass": 425,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "EOS",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Canon_EF_100mm_f_2_USM": {
            "brand": "Canon",
            "name": "EF 100mm f/2 USM",
            "type": "type_camera_lens",
            "optical_length": 0,
            "mass": 460,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "EOS",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Canon_EF_135mm_f_2L_USM": {
            "brand": "Canon",
            "name": "EF 135mm f/2L USM",
            "type": "type_camera_lens",
            "optical_length": 0,
            "mass": 750,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "EOS",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Canon_EF_70_200mm_f_2_8L_IS_III_USM": {
            "brand": "Canon",
            "name": "EF 70-200mm f/2.8L IS III USM",
            "type": "type_camera_lens",
            "optical_length": 0,
            "mass": 1480,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "EOS",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Canon_EF_70_200mm_f_4L_IS_II_USM": {
            "brand": "Canon",
            "name": "EF 70-200mm f/4L IS II USM",
            "type": "type_camera_lens",
            "optical_length": 0,
            "mass": 780,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "EOS",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Canon_EF_200mm_f_2L_IS_USM": {
            "brand": "Canon",
            "name": "EF 200mm f/2L IS USM",
            "type": "type_camera_lens",
            "optical_length": 0,
            "mass": 2520,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "EOS",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Canon_EF_300mm_f_2_8L_IS_II_USM": {
            "brand": "Canon",
            "name": "EF 300mm f/2.8L IS II USM",
            "type": "type_camera_lens",
            "optical_length": 0,
            "mass": 2350,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "EOS",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Canon_EF_300mm_f_4L_IS_USM": {
            "brand": "Canon",
            "name": "EF 300mm f/4L IS USM",
            "type": "type_camera_lens",
            "optical_length": 0,
            "mass": 1190,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "EOS",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Canon_EF_400mm_f_2_8L_IS_III_USM": {
            "brand": "Canon",
            "name": "EF 400mm f/2.8L IS III USM",
            "type": "type_camera_lens",
            "optical_length": 0,
            "mass": 2840,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "EOS",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Canon_EF_400mm_f_5_6L_USM": {
            "brand": "Canon",
            "name": "EF 400mm f/5.6L USM",
            "type": "type_camera_lens",
            "optical_length": 0,
            "mass": 1250,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "EOS",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Canon_EF_500mm_f_4L_IS_II_USM": {
            "brand": "Canon",
            "name": "EF 500mm f/4L IS II USM",
            "type": "type_camera_lens",
            "optical_length": 0,
            "mass": 3190,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "EOS",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Canon_EF_24_70mm_f_2_8L_II_USM": {
            "brand": "Canon",
            "name": "EF 24-70mm f/2.8L II USM",
            "type": "type_camera_lens",
            "optical_length": 0,
            "mass": 805,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "EOS",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Canon_EF_16_35mm_f_2_8L_III_USM": {
            "brand": "Canon",
            "name": "EF 16-35mm f/2.8L III USM",
            "type": "type_camera_lens",
            "optical_length": 0,
            "mass": 790,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "EOS",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Canon_EF_24mm_f_1_4L_II_USM": {
            "brand": "Canon",
            "name": "EF 24mm f/1.4L II USM",
            "type": "type_camera_lens",
            "optical_length": 0,
            "mass": 650,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "EOS",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Canon_EF_14mm_f_2_8L_II_USM": {
            "brand": "Canon",
            "name": "EF 14mm f/2.8L II USM",
            "type": "type_camera_lens",
            "optical_length": 0,
            "mass": 645,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "EOS",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Canon_RF_50mm_f_1_2L_USM": {
            "brand": "Canon",
            "name": "RF 50mm f/1.2L USM",
            "type": "type_camera_lens",
            "optical_length": 0,
            "mass": 950,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "Canon RF",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Canon_RF_85mm_f_1_2L_USM": {
            "brand": "Canon",
            "name": "RF 85mm f/1.2L USM",
            "type": "type_camera_lens",
            "optical_length": 0,
            "mass": 1195,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "Canon RF",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Canon_RF_135mm_f_1_8L_IS_USM": {
            "brand": "Canon",
            "name": "RF 135mm f/1.8L IS USM",
            "type": "type_camera_lens",
            "optical_length": 0,
            "mass": 935,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "Canon RF",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Canon_RF_70_200mm_f_2_8L_IS_USM": {
            "brand": "Canon",
            "name": "RF 70-200mm f/2.8L IS USM",
            "type": "type_camera_lens",
            "optical_length": 0,
            "mass": 1070,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "Canon RF",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Canon_RF_100_500mm_f_4_5_7_1L_IS_USM": {
            "brand": "Canon",
            "name": "RF 100-500mm f/4.5-7.1L IS USM",
            "type": "type_camera_lens",
            "optical_length": 0,
            "mass": 1370,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "Canon RF",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Canon_RF_200_800mm_f_6_3_9_IS_USM": {
            "brand": "Canon",
            "name": "RF 200-800mm f/6.3-9 IS USM",
            "type": "type_camera_lens",
            "optical_length": 0,
            "mass": 2050,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "Canon RF",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Canon_RF_400mm_f_2_8L_IS_USM": {
            "brand": "Canon",
            "name": "RF 400mm f/2.8L IS USM",
            "type": "type_camera_lens",
            "optical_length": 0,
            "mass": 2890,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "Canon RF",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Canon_RF_600mm_f_4L_IS_USM": {
            "brand": "Canon",
            "name": "RF 600mm f/4L IS USM",
            "type": "type_camera_lens",
            "optical_length": 0,
            "mass": 3090,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "Canon RF",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Canon_RF_800mm_f_5_6L_IS_USM": {
            "brand": "Canon",
            "name": "RF 800mm f/5.6L IS USM",
            "type": "type_camera_lens",
            "optical_length": 0,
            "mass": 3140,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "Canon RF",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Canon_RF_100mm_f_2_8L_Macro_IS_USM": {
            "brand": "Canon",
            "name": "RF 100mm f/2.8L Macro IS USM",
            "type": "type_camera_lens",
            "optical_length": 0,
            "mass": 730,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "Canon RF",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Canon_RF_24_70mm_f_2_8L_IS_USM": {
            "brand": "Canon",
            "name": "RF 24-70mm f/2.8L IS USM",
            "type": "type_camera_lens",
            "optical_length": 0,
            "mass": 900,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "Canon RF",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Canon_RF_14_35mm_f_4L_IS_USM": {
            "brand": "Canon",
            "name": "RF 14-35mm f/4L IS USM",
            "type": "type_camera_lens",
            "optical_length": 0,
            "mass": 540,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "Canon RF",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Canon_RF_15_35mm_f_2_8L_IS_USM": {
            "brand": "Canon",
            "name": "RF 15-35mm f/2.8L IS USM",
            "type": "type_camera_lens",
            "optical_length": 0,
            "mass": 840,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "Canon RF",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Nikon_AF_S_200mm_f_2G_ED_VR_II": {
            "brand": "Nikon",
            "name": "AF-S 200mm f/2G ED VR II",
            "type": "type_camera_lens",
            "optical_length": 0,
            "mass": 2930,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "Nikon F",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Nikon_AF_S_300mm_f_2_8G_ED_VR_II": {
            "brand": "Nikon",
            "name": "AF-S 300mm f/2.8G ED VR II",
            "type": "type_camera_lens",
            "optical_length": 0,
            "mass": 2870,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "Nikon F",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Nikon_AF_S_500mm_f_4E_FL_ED_VR": {
            "brand": "Nikon",
            "name": "AF-S 500mm f/4E FL ED VR",
            "type": "type_camera_lens",
            "optical_length": 0,
            "mass": 3090,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "Nikon F",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Nikon_AF_S_600mm_f_4E_FL_ED_VR": {
            "brand": "Nikon",
            "name": "AF-S 600mm f/4E FL ED VR",
            "type": "type_camera_lens",
            "optical_length": 0,
            "mass": 3810,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "Nikon F",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Nikon_AF_S_85mm_f_1_4G": {
            "brand": "Nikon",
            "name": "AF-S 85mm f/1.4G",
            "type": "type_camera_lens",
            "optical_length": 0,
            "mass": 595,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "Nikon F",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Nikon_AF_S_50mm_f_1_4G": {
            "brand": "Nikon",
            "name": "AF-S 50mm f/1.4G",
            "type": "type_camera_lens",
            "optical_length": 0,
            "mass": 280,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "Nikon F",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Nikon_AF_S_14_24mm_f_2_8G_ED": {
            "brand": "Nikon",
            "name": "AF-S 14-24mm f/2.8G ED",
            "type": "type_camera_lens",
            "optical_length": 0,
            "mass": 970,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "Nikon F",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Nikon_AF_S_24_70mm_f_2_8E_ED_VR": {
            "brand": "Nikon",
            "name": "AF-S 24-70mm f/2.8E ED VR",
            "type": "type_camera_lens",
            "optical_length": 0,
            "mass": 1070,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "Nikon F",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Nikon_AF_S_180_400mm_f_4E_TC": {
            "brand": "Nikon",
            "name": "AF-S 180-400mm f/4E TC",
            "type": "type_camera_lens",
            "optical_length": 0,
            "mass": 3500,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "Nikon F",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Nikon_AF_S_200_500mm_f_5_6E_ED_VR": {
            "brand": "Nikon",
            "name": "AF-S 200-500mm f/5.6E ED VR",
            "type": "type_camera_lens",
            "optical_length": 0,
            "mass": 2300,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "Nikon F",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Nikon_Z_50mm_f_1_2_S": {
            "brand": "Nikon",
            "name": "Z 50mm f/1.2 S",
            "type": "type_camera_lens",
            "optical_length": 0,
            "mass": 1090,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "Nikon Z",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Nikon_Z_85mm_f_1_2_S": {
            "brand": "Nikon",
            "name": "Z 85mm f/1.2 S",
            "type": "type_camera_lens",
            "optical_length": 0,
            "mass": 1160,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "Nikon Z",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Nikon_Z_400mm_f_4_5_VR_S": {
            "brand": "Nikon",
            "name": "Z 400mm f/4.5 VR S",
            "type": "type_camera_lens",
            "optical_length": 0,
            "mass": 1245,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "Nikon Z",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Nikon_Z_600mm_f_4_TC_VR_S": {
            "brand": "Nikon",
            "name": "Z 600mm f/4 TC VR S",
            "type": "type_camera_lens",
            "optical_length": 0,
            "mass": 3260,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "Nikon Z",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Nikon_Z_800mm_f_6_3_VR_S": {
            "brand": "Nikon",
            "name": "Z 800mm f/6.3 VR S",
            "type": "type_camera_lens",
            "optical_length": 0,
            "mass": 2385,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "Nikon Z",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Nikon_Z_70_200mm_f_2_8_VR_S": {
            "brand": "Nikon",
            "name": "Z 70-200mm f/2.8 VR S",
            "type": "type_camera_lens",
            "optical_length": 0,
            "mass": 1360,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "Nikon Z",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Nikon_Z_24_70mm_f_2_8_S": {
            "brand": "Nikon",
            "name": "Z 24-70mm f/2.8 S",
            "type": "type_camera_lens",
            "optical_length": 0,
            "mass": 805,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "Nikon Z",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Nikon_Z_14_24mm_f_2_8_S": {
            "brand": "Nikon",
            "name": "Z 14-24mm f/2.8 S",
            "type": "type_camera_lens",
            "optical_length": 0,
            "mass": 650,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "Nikon Z",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Nikon_Z_180_600mm_f_5_6_6_3_VR": {
            "brand": "Nikon",
            "name": "Z 180-600mm f/5.6-6.3 VR",
            "type": "type_camera_lens",
            "optical_length": 0,
            "mass": 1955,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "Nikon Z",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Sony_FE_200_600mm_f_5_6_6_3_G_OSS": {
            "brand": "Sony",
            "name": "FE 200-600mm f/5.6-6.3 G OSS",
            "type": "type_camera_lens",
            "optical_length": 0,
            "mass": 2115,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "Sony E",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Sony_FE_400mm_f_2_8_GM_OSS": {
            "brand": "Sony",
            "name": "FE 400mm f/2.8 GM OSS",
            "type": "type_camera_lens",
            "optical_length": 0,
            "mass": 2895,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "Sony E",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Sony_FE_600mm_f_4_GM_OSS": {
            "brand": "Sony",
            "name": "FE 600mm f/4 GM OSS",
            "type": "type_camera_lens",
            "optical_length": 0,
            "mass": 3040,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "Sony E",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Sony_FE_70_200mm_f_2_8_GM_OSS_II": {
            "brand": "Sony",
            "name": "FE 70-200mm f/2.8 GM OSS II",
            "type": "type_camera_lens",
            "optical_length": 0,
            "mass": 1045,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "Sony E",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Sony_FE_100_400mm_f_4_5_5_6_GM_OSS": {
            "brand": "Sony",
            "name": "FE 100-400mm f/4.5-5.6 GM OSS",
            "type": "type_camera_lens",
            "optical_length": 0,
            "mass": 1395,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "Sony E",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Sony_FE_50mm_f_1_2_GM": {
            "brand": "Sony",
            "name": "FE 50mm f/1.2 GM",
            "type": "type_camera_lens",
            "optical_length": 0,
            "mass": 778,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "Sony E",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Sony_FE_24_70mm_f_2_8_GM_II": {
            "brand": "Sony",
            "name": "FE 24-70mm f/2.8 GM II",
            "type": "type_camera_lens",
            "optical_length": 0,
            "mass": 695,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "Sony E",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Sony_FE_14mm_f_1_8_GM": {
            "brand": "Sony",
            "name": "FE 14mm f/1.8 GM",
            "type": "type_camera_lens",
            "optical_length": 0,
            "mass": 460,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "Sony E",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Sony_FE_20mm_f_1_8_G": {
            "brand": "Sony",
            "name": "FE 20mm f/1.8 G",
            "type": "type_camera_lens",
            "optical_length": 0,
            "mass": 373,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "Sony E",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Sony_FE_35mm_f_1_4_GM": {
            "brand": "Sony",
            "name": "FE 35mm f/1.4 GM",
            "type": "type_camera_lens",
            "optical_length": 0,
            "mass": 524,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "Sony E",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Sony_FE_300mm_f_2_8_GM_OSS": {
            "brand": "Sony",
            "name": "FE 300mm f/2.8 GM OSS",
            "type": "type_camera_lens",
            "optical_length": 0,
            "mass": 2230,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "Sony E",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Sigma_135mm_f_1_8_Art_Sony_E": {
            "brand": "Sigma",
            "name": "135mm f/1.8 Art (Sony E)",
            "type": "type_camera_lens",
            "optical_length": 0,
            "mass": 1130,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "Sony E",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Sigma_105mm_f_1_4_Art_Sony_E": {
            "brand": "Sigma",
            "name": "105mm f/1.4 Art (Sony E)",
            "type": "type_camera_lens",
            "optical_length": 0,
            "mass": 1645,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "Sony E",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Sigma_135mm_f_1_8_Art_Nikon_F": {
            "brand": "Sigma",
            "name": "135mm f/1.8 Art (Nikon F)",
            "type": "type_camera_lens",
            "optical_length": 0,
            "mass": 1130,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "Nikon F",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Sigma_105mm_f_1_4_Art_Nikon_F": {
            "brand": "Sigma",
            "name": "105mm f/1.4 Art (Nikon F)",
            "type": "type_camera_lens",
            "optical_length": 0,
            "mass": 1645,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "Nikon F",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Sigma_85mm_f_1_4_Art_EOS": {
            "brand": "Sigma",
            "name": "85mm f/1.4 Art (EOS)",
            "type": "type_camera_lens",
            "optical_length": 0,
            "mass": 1130,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "EOS",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Sigma_85mm_f_1_4_Art_Sony_E": {
            "brand": "Sigma",
            "name": "85mm f/1.4 Art (Sony E)",
            "type": "type_camera_lens",
            "optical_length": 0,
            "mass": 1130,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "Sony E",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Sigma_85mm_f_1_4_Art_Nikon_F": {
            "brand": "Sigma",
            "name": "85mm f/1.4 Art (Nikon F)",
            "type": "type_camera_lens",
            "optical_length": 0,
            "mass": 1130,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "Nikon F",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Sigma_40mm_f_1_4_Art_EOS": {
            "brand": "Sigma",
            "name": "40mm f/1.4 Art (EOS)",
            "type": "type_camera_lens",
            "optical_length": 0,
            "mass": 1200,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "EOS",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Sigma_40mm_f_1_4_Art_Sony_E": {
            "brand": "Sigma",
            "name": "40mm f/1.4 Art (Sony E)",
            "type": "type_camera_lens",
            "optical_length": 0,
            "mass": 1200,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "Sony E",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Sigma_24mm_f_1_4_Art_EOS": {
            "brand": "Sigma",
            "name": "24mm f/1.4 Art (EOS)",
            "type": "type_camera_lens",
            "optical_length": 0,
            "mass": 665,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "EOS",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Sigma_24mm_f_1_4_Art_Sony_E": {
            "brand": "Sigma",
            "name": "24mm f/1.4 Art (Sony E)",
            "type": "type_camera_lens",
            "optical_length": 0,
            "mass": 665,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "Sony E",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Sigma_20mm_f_1_4_Art_EOS": {
            "brand": "Sigma",
            "name": "20mm f/1.4 Art (EOS)",
            "type": "type_camera_lens",
            "optical_length": 0,
            "mass": 950,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "EOS",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Sigma_20mm_f_1_4_Art_Sony_E": {
            "brand": "Sigma",
            "name": "20mm f/1.4 Art (Sony E)",
            "type": "type_camera_lens",
            "optical_length": 0,
            "mass": 950,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "Sony E",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Sigma_50mm_f_1_4_Art_EOS": {
            "brand": "Sigma",
            "name": "50mm f/1.4 Art (EOS)",
            "type": "type_camera_lens",
            "optical_length": 0,
            "mass": 815,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "EOS",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Sigma_50mm_f_1_4_Art_Sony_E": {
            "brand": "Sigma",
            "name": "50mm f/1.4 Art (Sony E)",
            "type": "type_camera_lens",
            "optical_length": 0,
            "mass": 815,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "Sony E",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Sigma_50mm_f_1_4_Art_Nikon_F": {
            "brand": "Sigma",
            "name": "50mm f/1.4 Art (Nikon F)",
            "type": "type_camera_lens",
            "optical_length": 0,
            "mass": 815,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "Nikon F",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Sigma_60_600mm_f_4_5_6_3_DG_EOS": {
            "brand": "Sigma",
            "name": "60-600mm f/4.5-6.3 DG (EOS)",
            "type": "type_camera_lens",
            "optical_length": 0,
            "mass": 2700,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "EOS",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Sigma_60_600mm_f_4_5_6_3_DG_Sony_E": {
            "brand": "Sigma",
            "name": "60-600mm f/4.5-6.3 DG (Sony E)",
            "type": "type_camera_lens",
            "optical_length": 0,
            "mass": 2700,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "Sony E",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Sigma_150_600mm_f_5_6_3_DG_Sony_E": {
            "brand": "Sigma",
            "name": "150-600mm f/5-6.3 DG (Sony E)",
            "type": "type_camera_lens",
            "optical_length": 0,
            "mass": 2860,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "Sony E",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Sigma_150_600mm_f_5_6_3_DG_Nikon_F": {
            "brand": "Sigma",
            "name": "150-600mm f/5-6.3 DG (Nikon F)",
            "type": "type_camera_lens",
            "optical_length": 0,
            "mass": 2860,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "Nikon F",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Sigma_100_400mm_f_5_6_3_DG_EOS": {
            "brand": "Sigma",
            "name": "100-400mm f/5-6.3 DG (EOS)",
            "type": "type_camera_lens",
            "optical_length": 0,
            "mass": 1160,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "EOS",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Sigma_100_400mm_f_5_6_3_DG_Sony_E": {
            "brand": "Sigma",
            "name": "100-400mm f/5-6.3 DG (Sony E)",
            "type": "type_camera_lens",
            "optical_length": 0,
            "mass": 1160,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "Sony E",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Tamron_SP_150_600mm_f_5_6_3_EOS": {
            "brand": "Tamron",
            "name": "SP 150-600mm f/5-6.3 (EOS)",
            "type": "type_camera_lens",
            "optical_length": 0,
            "mass": 2010,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "EOS",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Tamron_SP_150_600mm_f_5_6_3_Nikon_F": {
            "brand": "Tamron",
            "name": "SP 150-600mm f/5-6.3 (Nikon F)",
            "type": "type_camera_lens",
            "optical_length": 0,
            "mass": 2010,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "Nikon F",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Tamron_SP_150_600mm_f_5_6_3_Sony_E": {
            "brand": "Tamron",
            "name": "SP 150-600mm f/5-6.3 (Sony E)",
            "type": "type_camera_lens",
            "optical_length": 0,
            "mass": 2010,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "Sony E",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Tamron_150_500mm_f_5_6_7_Fuji_X": {
            "brand": "Tamron",
            "name": "150-500mm f/5-6.7 (Fuji X)",
            "type": "type_camera_lens",
            "optical_length": 0,
            "mass": 1725,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "Fuji X",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Tamron_100_400mm_f_4_5_6_3_EOS": {
            "brand": "Tamron",
            "name": "100-400mm f/4.5-6.3 (EOS)",
            "type": "type_camera_lens",
            "optical_length": 0,
            "mass": 1135,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "EOS",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Tamron_70_180mm_f_2_8_Sony_E": {
            "brand": "Tamron",
            "name": "70-180mm f/2.8 (Sony E)",
            "type": "type_camera_lens",
            "optical_length": 0,
            "mass": 815,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "Sony E",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Tamron_70_300mm_f_4_5_6_3_Sony_E": {
            "brand": "Tamron",
            "name": "70-300mm f/4.5-6.3 (Sony E)",
            "type": "type_camera_lens",
            "optical_length": 0,
            "mass": 545,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "Sony E",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Tamron_28_200mm_f_2_8_5_6_Sony_E": {
            "brand": "Tamron",
            "name": "28-200mm f/2.8-5.6 (Sony E)",
            "type": "type_camera_lens",
            "optical_length": 0,
            "mass": 575,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "Sony E",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Tamron_35_150mm_f_2_2_8_Sony_E": {
            "brand": "Tamron",
            "name": "35-150mm f/2-2.8 (Sony E)",
            "type": "type_camera_lens",
            "optical_length": 0,
            "mass": 1165,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "Sony E",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Tamron_50_400mm_f_4_5_6_3_Sony_E": {
            "brand": "Tamron",
            "name": "50-400mm f/4.5-6.3 (Sony E)",
            "type": "type_camera_lens",
            "optical_length": 0,
            "mass": 1155,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "Sony E",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Samyang_Rokinon_135mm_f_2_0_Nikon_F": {
            "brand": "Samyang/Rokinon",
            "name": "135mm f/2.0 (Nikon F)",
            "type": "type_camera_lens",
            "optical_length": 0,
            "mass": 730,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "Nikon F",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Samyang_Rokinon_85mm_f_1_4_EOS": {
            "brand": "Samyang/Rokinon",
            "name": "85mm f/1.4 (EOS)",
            "type": "type_camera_lens",
            "optical_length": 0,
            "mass": 530,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "EOS",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Samyang_Rokinon_85mm_f_1_4_Sony_E": {
            "brand": "Samyang/Rokinon",
            "name": "85mm f/1.4 (Sony E)",
            "type": "type_camera_lens",
            "optical_length": 0,
            "mass": 530,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "Sony E",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Samyang_Rokinon_85mm_f_1_4_Nikon_F": {
            "brand": "Samyang/Rokinon",
            "name": "85mm f/1.4 (Nikon F)",
            "type": "type_camera_lens",
            "optical_length": 0,
            "mass": 530,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "Nikon F",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Samyang_Rokinon_14mm_f_2_8_Sony_E": {
            "brand": "Samyang/Rokinon",
            "name": "14mm f/2.8 (Sony E)",
            "type": "type_camera_lens",
            "optical_length": 0,
            "mass": 550,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "Sony E",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Samyang_Rokinon_14mm_f_2_8_Nikon_F": {
            "brand": "Samyang/Rokinon",
            "name": "14mm f/2.8 (Nikon F)",
            "type": "type_camera_lens",
            "optical_length": 0,
            "mass": 550,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "Nikon F",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Samyang_Rokinon_24mm_f_1_4_Sony_E": {
            "brand": "Samyang/Rokinon",
            "name": "24mm f/1.4 (Sony E)",
            "type": "type_camera_lens",
            "optical_length": 0,
            "mass": 680,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "Sony E",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Samyang_Rokinon_24mm_f_1_4_Nikon_F": {
            "brand": "Samyang/Rokinon",
            "name": "24mm f/1.4 (Nikon F)",
            "type": "type_camera_lens",
            "optical_length": 0,
            "mass": 680,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "Nikon F",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Samyang_Rokinon_50mm_f_1_4_EOS": {
            "brand": "Samyang/Rokinon",
            "name": "50mm f/1.4 (EOS)",
            "type": "type_camera_lens",
            "optical_length": 0,
            "mass": 550,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "EOS",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Samyang_Rokinon_50mm_f_1_4_Sony_E": {
            "brand": "Samyang/Rokinon",
            "name": "50mm f/1.4 (Sony E)",
            "type": "type_camera_lens",
            "optical_length": 0,
            "mass": 550,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "Sony E",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Samyang_Rokinon_12mm_f_2_0_Sony_E": {
            "brand": "Samyang/Rokinon",
            "name": "12mm f/2.0 (Sony E)",
            "type": "type_camera_lens",
            "optical_length": 0,
            "mass": 260,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "Sony E",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Samyang_Rokinon_12mm_f_2_0_MFT": {
            "brand": "Samyang/Rokinon",
            "name": "12mm f/2.0 (MFT)",
            "type": "type_camera_lens",
            "optical_length": 0,
            "mass": 260,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "MFT",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Samyang_Rokinon_12mm_f_2_0_Fuji_X": {
            "brand": "Samyang/Rokinon",
            "name": "12mm f/2.0 (Fuji X)",
            "type": "type_camera_lens",
            "optical_length": 0,
            "mass": 260,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "Fuji X",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Samyang_Rokinon_8mm_f_3_5_Fisheye_EOS": {
            "brand": "Samyang/Rokinon",
            "name": "8mm f/3.5 Fisheye (EOS)",
            "type": "type_camera_lens",
            "optical_length": 0,
            "mass": 435,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "EOS",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Samyang_Rokinon_8mm_f_3_5_Fisheye_Nikon_F": {
            "brand": "Samyang/Rokinon",
            "name": "8mm f/3.5 Fisheye (Nikon F)",
            "type": "type_camera_lens",
            "optical_length": 0,
            "mass": 435,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "Nikon F",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Samyang_Rokinon_35mm_f_1_4_EOS": {
            "brand": "Samyang/Rokinon",
            "name": "35mm f/1.4 (EOS)",
            "type": "type_camera_lens",
            "optical_length": 0,
            "mass": 660,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "EOS",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Samyang_Rokinon_35mm_f_1_4_Sony_E": {
            "brand": "Samyang/Rokinon",
            "name": "35mm f/1.4 (Sony E)",
            "type": "type_camera_lens",
            "optical_length": 0,
            "mass": 660,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "Sony E",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Samyang_Rokinon_100mm_f_2_8_Macro_EOS": {
            "brand": "Samyang/Rokinon",
            "name": "100mm f/2.8 Macro (EOS)",
            "type": "type_camera_lens",
            "optical_length": 0,
            "mass": 720,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "EOS",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Voigtlander_Nokton_25mm_f_0_95_II_MFT": {
            "brand": "Voigtlander",
            "name": "Nokton 25mm f/0.95 II (MFT)",
            "type": "type_camera_lens",
            "optical_length": 0,
            "mass": 410,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "MFT",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Voigtlander_Nokton_42_5mm_f_0_95_MFT": {
            "brand": "Voigtlander",
            "name": "Nokton 42.5mm f/0.95 (MFT)",
            "type": "type_camera_lens",
            "optical_length": 0,
            "mass": 571,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "MFT",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Voigtlander_Macro_APO_Lanthar_65mm_f_2_Sony_E": {
            "brand": "Voigtlander",
            "name": "Macro APO-Lanthar 65mm f/2 (Sony E)",
            "type": "type_camera_lens",
            "optical_length": 0,
            "mass": 625,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "Sony E",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Voigtlander_Nokton_35mm_f_1_2_Sony_E": {
            "brand": "Voigtlander",
            "name": "Nokton 35mm f/1.2 (Sony E)",
            "type": "type_camera_lens",
            "optical_length": 0,
            "mass": 420,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "Sony E",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Voigtlander_Nokton_40mm_f_1_2_Sony_E": {
            "brand": "Voigtlander",
            "name": "Nokton 40mm f/1.2 (Sony E)",
            "type": "type_camera_lens",
            "optical_length": 0,
            "mass": 420,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "Sony E",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Voigtlander_Nokton_50mm_f_1_0_Nikon_Z": {
            "brand": "Voigtlander",
            "name": "Nokton 50mm f/1.0 (Nikon Z)",
            "type": "type_camera_lens",
            "optical_length": 0,
            "mass": 780,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "Nikon Z",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Voigtlander_HELIAR_40mm_f_2_8_Sony_E": {
            "brand": "Voigtlander",
            "name": "HELIAR 40mm f/2.8 (Sony E)",
            "type": "type_camera_lens",
            "optical_length": 0,
            "mass": 124,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "Sony E",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Voigtlander_APO_SKOPAR_90mm_f_2_8_Sony_E": {
            "brand": "Voigtlander",
            "name": "APO-SKOPAR 90mm f/2.8 (Sony E)",
            "type": "type_camera_lens",
            "optical_length": 0,
            "mass": 260,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "Sony E",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Voigtlander_COLOR_SKOPAR_21mm_f_3_5_Sony_E": {
            "brand": "Voigtlander",
            "name": "COLOR-SKOPAR 21mm f/3.5 (Sony E)",
            "type": "type_camera_lens",
            "optical_length": 0,
            "mass": 230,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "Sony E",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Tokina_opera_50mm_f_1_4_EOS": {
            "brand": "Tokina",
            "name": "opera 50mm f/1.4 (EOS)",
            "type": "type_camera_lens",
            "optical_length": 0,
            "mass": 950,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "EOS",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Tokina_opera_50mm_f_1_4_Nikon_F": {
            "brand": "Tokina",
            "name": "opera 50mm f/1.4 (Nikon F)",
            "type": "type_camera_lens",
            "optical_length": 0,
            "mass": 950,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "Nikon F",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Tokina_AT_X_11_20mm_f_2_8_EOS": {
            "brand": "Tokina",
            "name": "AT-X 11-20mm f/2.8 (EOS)",
            "type": "type_camera_lens",
            "optical_length": 0,
            "mass": 560,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "EOS",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Tokina_AT_X_11_20mm_f_2_8_Nikon_F": {
            "brand": "Tokina",
            "name": "AT-X 11-20mm f/2.8 (Nikon F)",
            "type": "type_camera_lens",
            "optical_length": 0,
            "mass": 560,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "Nikon F",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Tokina_AT_X_14_20mm_f_2_EOS": {
            "brand": "Tokina",
            "name": "AT-X 14-20mm f/2 (EOS)",
            "type": "type_camera_lens",
            "optical_length": 0,
            "mass": 735,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "EOS",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Tokina_AT_X_14_20mm_f_2_Nikon_F": {
            "brand": "Tokina",
            "name": "AT-X 14-20mm f/2 (Nikon F)",
            "type": "type_camera_lens",
            "optical_length": 0,
            "mass": 735,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "Nikon F",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Tokina_SZX_400mm_f_8_Reflex": {
            "brand": "Tokina",
            "name": "SZX 400mm f/8 Reflex",
            "type": "type_camera_lens",
            "optical_length": 0,
            "mass": 355,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "EOS",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Tokina_SZ_500mm_f_8_Reflex_Sony_E": {
            "brand": "Tokina",
            "name": "SZ 500mm f/8 Reflex (Sony E)",
            "type": "type_camera_lens",
            "optical_length": 0,
            "mass": 380,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "Sony E",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Tokina_atx_m_85mm_f_1_8_Sony_E": {
            "brand": "Tokina",
            "name": "atx-m 85mm f/1.8 (Sony E)",
            "type": "type_camera_lens",
            "optical_length": 0,
            "mass": 645,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "Sony E",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Tokina_atx_m_33mm_f_1_4_Fuji_X": {
            "brand": "Tokina",
            "name": "atx-m 33mm f/1.4 (Fuji X)",
            "type": "type_camera_lens",
            "optical_length": 0,
            "mass": 285,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "Fuji X",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Tokina_atx_m_23mm_f_1_4_Fuji_X": {
            "brand": "Tokina",
            "name": "atx-m 23mm f/1.4 (Fuji X)",
            "type": "type_camera_lens",
            "optical_length": 0,
            "mass": 263,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "Fuji X",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Tokina_ATX_i_100mm_f_2_8_Macro_EOS": {
            "brand": "Tokina",
            "name": "ATX-i 100mm f/2.8 Macro (EOS)",
            "type": "type_camera_lens",
            "optical_length": 0,
            "mass": 515,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "EOS",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "ID_7Artisans_35mm_f_0_95_Sony_E": {
            "brand": "7Artisans",
            "name": "35mm f/0.95 (Sony E)",
            "type": "type_camera_lens",
            "optical_length": 0,
            "mass": 530,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "Sony E",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "ID_7Artisans_55mm_f_1_4_Sony_E": {
            "brand": "7Artisans",
            "name": "55mm f/1.4 (Sony E)",
            "type": "type_camera_lens",
            "optical_length": 0,
            "mass": 340,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "Sony E",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "ID_7Artisans_25mm_f_1_8_Sony_E": {
            "brand": "7Artisans",
            "name": "25mm f/1.8 (Sony E)",
            "type": "type_camera_lens",
            "optical_length": 0,
            "mass": 160,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "Sony E",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "ID_7Artisans_35mm_f_1_2_Sony_E": {
            "brand": "7Artisans",
            "name": "35mm f/1.2 (Sony E)",
            "type": "type_camera_lens",
            "optical_length": 0,
            "mass": 450,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "Sony E",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "ID_7Artisans_60mm_f_2_8_Macro_Sony_E": {
            "brand": "7Artisans",
            "name": "60mm f/2.8 Macro (Sony E)",
            "type": "type_camera_lens",
            "optical_length": 0,
            "mass": 460,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "Sony E",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "ID_7Artisans_12mm_f_2_8_Sony_E": {
            "brand": "7Artisans",
            "name": "12mm f/2.8 (Sony E)",
            "type": "type_camera_lens",
            "optical_length": 0,
            "mass": 350,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "Sony E",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "ID_7Artisans_50mm_f_1_05_Nikon_Z": {
            "brand": "7Artisans",
            "name": "50mm f/1.05 (Nikon Z)",
            "type": "type_camera_lens",
            "optical_length": 0,
            "mass": 570,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "Nikon Z",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "ID_7Artisans_50mm_f_1_05_Canon_RF": {
            "brand": "7Artisans",
            "name": "50mm f/1.05 (Canon RF)",
            "type": "type_camera_lens",
            "optical_length": 0,
            "mass": 570,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "Canon RF",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "ID_7Artisans_35mm_f_0_95_MFT": {
            "brand": "7Artisans",
            "name": "35mm f/0.95 (MFT)",
            "type": "type_camera_lens",
            "optical_length": 0,
            "mass": 530,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "MFT",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "ID_7Artisans_35mm_f_0_95_Fuji_X": {
            "brand": "7Artisans",
            "name": "35mm f/0.95 (Fuji X)",
            "type": "type_camera_lens",
            "optical_length": 0,
            "mass": 530,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "Fuji X",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "ID_7Artisans_25mm_f_0_95_MFT": {
            "brand": "7Artisans",
            "name": "25mm f/0.95 (MFT)",
            "type": "type_camera_lens",
            "optical_length": 0,
            "mass": 560,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "MFT",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "ID_7Artisans_55mm_f_1_4_Fuji_X": {
            "brand": "7Artisans",
            "name": "55mm f/1.4 (Fuji X)",
            "type": "type_camera_lens",
            "optical_length": 0,
            "mass": 340,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "Fuji X",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "ID_7Artisans_55mm_f_1_4_MFT": {
            "brand": "7Artisans",
            "name": "55mm f/1.4 (MFT)",
            "type": "type_camera_lens",
            "optical_length": 0,
            "mass": 340,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "MFT",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "ID_7Artisans_12mm_f_2_8_EOS": {
            "brand": "7Artisans",
            "name": "12mm f/2.8 (EOS)",
            "type": "type_camera_lens",
            "optical_length": 0,
            "mass": 350,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "EOS",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Viltrox_85mm_f_1_8_II_Nikon_Z": {
            "brand": "Viltrox",
            "name": "85mm f/1.8 II (Nikon Z)",
            "type": "type_camera_lens",
            "optical_length": 0,
            "mass": 312,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "Nikon Z",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Viltrox_85mm_f_1_8_II_Canon_RF": {
            "brand": "Viltrox",
            "name": "85mm f/1.8 II (Canon RF)",
            "type": "type_camera_lens",
            "optical_length": 0,
            "mass": 312,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "Canon RF",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Viltrox_85mm_f_1_8_II_Fuji_X": {
            "brand": "Viltrox",
            "name": "85mm f/1.8 II (Fuji X)",
            "type": "type_camera_lens",
            "optical_length": 0,
            "mass": 312,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "Fuji X",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Viltrox_56mm_f_1_4_Sony_E": {
            "brand": "Viltrox",
            "name": "56mm f/1.4 (Sony E)",
            "type": "type_camera_lens",
            "optical_length": 0,
            "mass": 260,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "Sony E",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Viltrox_56mm_f_1_4_Fuji_X": {
            "brand": "Viltrox",
            "name": "56mm f/1.4 (Fuji X)",
            "type": "type_camera_lens",
            "optical_length": 0,
            "mass": 260,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "Fuji X",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Viltrox_56mm_f_1_4_Nikon_Z": {
            "brand": "Viltrox",
            "name": "56mm f/1.4 (Nikon Z)",
            "type": "type_camera_lens",
            "optical_length": 0,
            "mass": 260,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "Nikon Z",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Viltrox_23mm_f_1_4_Sony_E": {
            "brand": "Viltrox",
            "name": "23mm f/1.4 (Sony E)",
            "type": "type_camera_lens",
            "optical_length": 0,
            "mass": 245,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "Sony E",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Viltrox_23mm_f_1_4_Fuji_X": {
            "brand": "Viltrox",
            "name": "23mm f/1.4 (Fuji X)",
            "type": "type_camera_lens",
            "optical_length": 0,
            "mass": 245,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "Fuji X",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Viltrox_33mm_f_1_4_Sony_E": {
            "brand": "Viltrox",
            "name": "33mm f/1.4 (Sony E)",
            "type": "type_camera_lens",
            "optical_length": 0,
            "mass": 255,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "Sony E",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Viltrox_33mm_f_1_4_Fuji_X": {
            "brand": "Viltrox",
            "name": "33mm f/1.4 (Fuji X)",
            "type": "type_camera_lens",
            "optical_length": 0,
            "mass": 255,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "Fuji X",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Viltrox_13mm_f_1_4_Sony_E": {
            "brand": "Viltrox",
            "name": "13mm f/1.4 (Sony E)",
            "type": "type_camera_lens",
            "optical_length": 0,
            "mass": 420,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "Sony E",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Viltrox_13mm_f_1_4_Fuji_X": {
            "brand": "Viltrox",
            "name": "13mm f/1.4 (Fuji X)",
            "type": "type_camera_lens",
            "optical_length": 0,
            "mass": 420,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "Fuji X",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Viltrox_75mm_f_1_2_Sony_E": {
            "brand": "Viltrox",
            "name": "75mm f/1.2 (Sony E)",
            "type": "type_camera_lens",
            "optical_length": 0,
            "mass": 510,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "Sony E",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Viltrox_75mm_f_1_2_Fuji_X": {
            "brand": "Viltrox",
            "name": "75mm f/1.2 (Fuji X)",
            "type": "type_camera_lens",
            "optical_length": 0,
            "mass": 510,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "Fuji X",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Viltrox_AF_85mm_f_1_8_EOS": {
            "brand": "Viltrox",
            "name": "AF 85mm f/1.8 (EOS)",
            "type": "type_camera_lens",
            "optical_length": 0,
            "mass": 350,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "EOS",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Viltrox_AF_56mm_f_1_4_EOS_M": {
            "brand": "Viltrox",
            "name": "AF 56mm f/1.4 (EOS-M)",
            "type": "type_camera_lens",
            "optical_length": 0,
            "mass": 260,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "EOS",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Viltrox_24mm_f_1_8_Sony_E": {
            "brand": "Viltrox",
            "name": "24mm f/1.8 (Sony E)",
            "type": "type_camera_lens",
            "optical_length": 0,
            "mass": 255,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "Sony E",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "GSO_Dobson_6": {
            "brand": "GSO",
            "name": 'Dobson 6"',
            "type": "type_telescope",
            "optical_length": 0,
            "mass": 5000,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": '2"',
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Orion_IntelliScope_XT6_Dob": {
            "brand": "Orion",
            "name": "IntelliScope XT6 Dob",
            "type": "type_telescope",
            "optical_length": 0,
            "mass": 5000,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": '2"',
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "GSO_Dobson_8": {
            "brand": "GSO",
            "name": 'Dobson 8"',
            "type": "type_telescope",
            "optical_length": 0,
            "mass": 7000,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": '2"',
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Orion_IntelliScope_XT8_Dob": {
            "brand": "Orion",
            "name": "IntelliScope XT8 Dob",
            "type": "type_telescope",
            "optical_length": 0,
            "mass": 7000,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": '2"',
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "GSO_Dobson_10": {
            "brand": "GSO",
            "name": 'Dobson 10"',
            "type": "type_telescope",
            "optical_length": 0,
            "mass": 9500,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": '2"',
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Orion_IntelliScope_XT10_Dob": {
            "brand": "Orion",
            "name": "IntelliScope XT10 Dob",
            "type": "type_telescope",
            "optical_length": 0,
            "mass": 9500,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": '2"',
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "GSO_Dobson_12": {
            "brand": "GSO",
            "name": 'Dobson 12"',
            "type": "type_telescope",
            "optical_length": 0,
            "mass": 13000,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": '2"',
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Orion_IntelliScope_XT12_Dob": {
            "brand": "Orion",
            "name": "IntelliScope XT12 Dob",
            "type": "type_telescope",
            "optical_length": 0,
            "mass": 13000,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": '2"',
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "GSO_Dobson_14": {
            "brand": "GSO",
            "name": 'Dobson 14"',
            "type": "type_telescope",
            "optical_length": 0,
            "mass": 18000,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": '2"',
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Orion_IntelliScope_XT14_Dob": {
            "brand": "Orion",
            "name": "IntelliScope XT14 Dob",
            "type": "type_telescope",
            "optical_length": 0,
            "mass": 18000,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": '2"',
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "GSO_Dobson_16": {
            "brand": "GSO",
            "name": 'Dobson 16"',
            "type": "type_telescope",
            "optical_length": 0,
            "mass": 25000,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": '2"',
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Orion_IntelliScope_XT16_Dob": {
            "brand": "Orion",
            "name": "IntelliScope XT16 Dob",
            "type": "type_telescope",
            "optical_length": 0,
            "mass": 25000,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": '2"',
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Bresser_Messier_Dobson_6_Truss": {
            "brand": "Bresser",
            "name": 'Messier Dobson 6" Truss',
            "type": "type_telescope",
            "optical_length": 0,
            "mass": 4500,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": '2"',
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Bresser_Messier_Dobson_8_Truss": {
            "brand": "Bresser",
            "name": 'Messier Dobson 8" Truss',
            "type": "type_telescope",
            "optical_length": 0,
            "mass": 6800,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": '2"',
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Bresser_Messier_Dobson_10_Truss": {
            "brand": "Bresser",
            "name": 'Messier Dobson 10" Truss',
            "type": "type_telescope",
            "optical_length": 0,
            "mass": 9200,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": '2"',
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Bresser_Messier_Dobson_12_Truss": {
            "brand": "Bresser",
            "name": 'Messier Dobson 12" Truss',
            "type": "type_telescope",
            "optical_length": 0,
            "mass": 12500,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": '2"',
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Bresser_Messier_Dobson_14_Truss": {
            "brand": "Bresser",
            "name": 'Messier Dobson 14" Truss',
            "type": "type_telescope",
            "optical_length": 0,
            "mass": 17000,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": '2"',
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Bresser_Messier_Dobson_16_Truss": {
            "brand": "Bresser",
            "name": 'Messier Dobson 16" Truss',
            "type": "type_telescope",
            "optical_length": 0,
            "mass": 24000,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": '2"',
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Sky_Watcher_Traditional_Dob_6": {
            "brand": "Sky-Watcher",
            "name": 'Traditional Dob 6"',
            "type": "type_telescope",
            "optical_length": 0,
            "mass": 5000,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": '2"',
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Sky_Watcher_Traditional_Dob_8": {
            "brand": "Sky-Watcher",
            "name": 'Traditional Dob 8"',
            "type": "type_telescope",
            "optical_length": 0,
            "mass": 7500,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": '2"',
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Sky_Watcher_Traditional_Dob_10": {
            "brand": "Sky-Watcher",
            "name": 'Traditional Dob 10"',
            "type": "type_telescope",
            "optical_length": 0,
            "mass": 10000,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": '2"',
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Sky_Watcher_Traditional_Dob_12": {
            "brand": "Sky-Watcher",
            "name": 'Traditional Dob 12"',
            "type": "type_telescope",
            "optical_length": 0,
            "mass": 13500,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": '2"',
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Celestron_C8_A_XLT_OTA": {
            "brand": "Celestron",
            "name": "C8-A XLT (OTA)",
            "type": "type_telescope",
            "optical_length": 0,
            "mass": 5500,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "SC (Schmidt-Cassegrain)",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Celestron_C9_25_A_XLT_OTA": {
            "brand": "Celestron",
            "name": "C9.25-A XLT (OTA)",
            "type": "type_telescope",
            "optical_length": 0,
            "mass": 9300,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "SC (Schmidt-Cassegrain)",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Celestron_C11_A_XLT_OTA": {
            "brand": "Celestron",
            "name": "C11-A XLT (OTA)",
            "type": "type_telescope",
            "optical_length": 0,
            "mass": 12300,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "SC (Schmidt-Cassegrain)",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Celestron_C14_A_XLT_OTA": {
            "brand": "Celestron",
            "name": "C14-A XLT (OTA)",
            "type": "type_telescope",
            "optical_length": 0,
            "mass": 20200,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "SC (Schmidt-Cassegrain)",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Takahashi_Epsilon_160ED": {
            "brand": "Takahashi",
            "name": "Epsilon-160ED",
            "type": "type_telescope",
            "optical_length": 0,
            "mass": 7200,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "M68",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Takahashi_FS_128": {
            "brand": "Takahashi",
            "name": "FS-128",
            "type": "type_telescope",
            "optical_length": 0,
            "mass": 5800,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "M72",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Takahashi_Epsilon_130ED": {
            "brand": "Takahashi",
            "name": "Epsilon-130ED",
            "type": "type_telescope",
            "optical_length": 0,
            "mass": 5800,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "M54",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Omegon_Pro_APO_72_400": {
            "brand": "Omegon",
            "name": "Pro APO 72/400",
            "type": "type_refractor",
            "optical_length": 0,
            "mass": 1800,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "M48",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Omegon_Pro_APO_80_500": {
            "brand": "Omegon",
            "name": "Pro APO 80/500",
            "type": "type_refractor",
            "optical_length": 0,
            "mass": 2600,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "M48",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Omegon_Pro_APO_100_580": {
            "brand": "Omegon",
            "name": "Pro APO 100/580",
            "type": "type_refractor",
            "optical_length": 0,
            "mass": 3800,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "M48",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Omegon_Pro_APO_110_660": {
            "brand": "Omegon",
            "name": "Pro APO 110/660",
            "type": "type_refractor",
            "optical_length": 0,
            "mass": 4500,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "M48",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Omegon_Pro_APO_127_793": {
            "brand": "Omegon",
            "name": "Pro APO 127/793",
            "type": "type_refractor",
            "optical_length": 0,
            "mass": 6500,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "M68",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Omegon_Pro_APO_152_988": {
            "brand": "Omegon",
            "name": "Pro APO 152/988",
            "type": "type_refractor",
            "optical_length": 0,
            "mass": 9500,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "M68",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Omegon_Pro_Newton_200_800_OTA": {
            "brand": "Omegon",
            "name": "Pro Newton 200/800 OTA",
            "type": "type_telescope",
            "optical_length": 0,
            "mass": 7200,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "M48",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Omegon_Pro_Newton_250_1000_OTA": {
            "brand": "Omegon",
            "name": "Pro Newton 250/1000 OTA",
            "type": "type_telescope",
            "optical_length": 0,
            "mass": 11200,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "M48",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Omegon_Pro_RC_154_1370": {
            "brand": "Omegon",
            "name": "Pro RC 154/1370",
            "type": "type_telescope",
            "optical_length": 0,
            "mass": 6000,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "M72",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Omegon_Pro_RC_203_1624": {
            "brand": "Omegon",
            "name": "Pro RC 203/1624",
            "type": "type_telescope",
            "optical_length": 0,
            "mass": 9500,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "M72",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Omegon_Pro_RC_254_2000": {
            "brand": "Omegon",
            "name": "Pro RC 254/2000",
            "type": "type_telescope",
            "optical_length": 0,
            "mass": 13000,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "M72",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Omegon_Pro_RC_304_2432": {
            "brand": "Omegon",
            "name": "Pro RC 304/2432",
            "type": "type_telescope",
            "optical_length": 0,
            "mass": 17000,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "M84",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Omegon_Pro_RC_355_2845": {
            "brand": "Omegon",
            "name": "Pro RC 355/2845",
            "type": "type_telescope",
            "optical_length": 0,
            "mass": 22000,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "M84",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "TS_Optics_CF_APO_65mm_Quintuplet": {
            "brand": "TS-Optics",
            "name": "CF-APO 65mm Quintuplet",
            "type": "type_refractor",
            "optical_length": 0,
            "mass": 2000,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "M48",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "TS_Optics_CF_APO_90mm": {
            "brand": "TS-Optics",
            "name": "CF-APO 90mm",
            "type": "type_refractor",
            "optical_length": 0,
            "mass": 3500,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "M48",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "TS_Optics_RC_6_Pro": {
            "brand": "TS-Optics",
            "name": 'RC 6" Pro',
            "type": "type_telescope",
            "optical_length": 0,
            "mass": 5800,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "M72",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "TS_Optics_RC_8_Pro": {
            "brand": "TS-Optics",
            "name": 'RC 8" Pro',
            "type": "type_telescope",
            "optical_length": 0,
            "mass": 9500,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "M72",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "TS_Optics_RC_10_Pro": {
            "brand": "TS-Optics",
            "name": 'RC 10" Pro',
            "type": "type_telescope",
            "optical_length": 0,
            "mass": 13500,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "M72",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "TS_Optics_RC_12_Pro": {
            "brand": "TS-Optics",
            "name": 'RC 12" Pro',
            "type": "type_telescope",
            "optical_length": 0,
            "mass": 18500,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "M84",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "TS_Optics_ONTC_12_f_4": {
            "brand": "TS-Optics",
            "name": 'ONTC 12" f/4',
            "type": "type_telescope",
            "optical_length": 0,
            "mass": 18000,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "M68",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "TS_Optics_ONTC_14_f_4": {
            "brand": "TS-Optics",
            "name": 'ONTC 14" f/4',
            "type": "type_telescope",
            "optical_length": 0,
            "mass": 22000,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "M68",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "TS_Optics_ONTC_16_f_4": {
            "brand": "TS-Optics",
            "name": 'ONTC 16" f/4',
            "type": "type_telescope",
            "optical_length": 0,
            "mass": 28000,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "M68",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "TS_Optics_Individual_80mm_Quad": {
            "brand": "TS-Optics",
            "name": "Individual 80mm Quad",
            "type": "type_refractor",
            "optical_length": 0,
            "mass": 3200,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "M48",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "TS_Optics_Individual_102mm_Quad": {
            "brand": "TS-Optics",
            "name": "Individual 102mm Quad",
            "type": "type_refractor",
            "optical_length": 0,
            "mass": 4800,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "M48",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "TS_Optics_Individual_115mm_Quad": {
            "brand": "TS-Optics",
            "name": "Individual 115mm Quad",
            "type": "type_refractor",
            "optical_length": 0,
            "mass": 6000,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "M48",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "TS_Optics_Photoline_152mm_APO": {
            "brand": "TS-Optics",
            "name": "Photoline 152mm APO",
            "type": "type_refractor",
            "optical_length": 0,
            "mass": 9500,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "M68",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Celestron_C6_A_XLT_OTA": {
            "brand": "Celestron",
            "name": "C6-A XLT (OTA)",
            "type": "type_telescope",
            "optical_length": 0,
            "mass": 3850,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "SC (Schmidt-Cassegrain)",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Celestron_C5_OTA_XLT": {
            "brand": "Celestron",
            "name": "C5 OTA (XLT)",
            "type": "type_telescope",
            "optical_length": 0,
            "mass": 2800,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "SC (Schmidt-Cassegrain)",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Celestron_C6_OTA": {
            "brand": "Celestron",
            "name": "C6 OTA",
            "type": "type_telescope",
            "optical_length": 0,
            "mass": 3900,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "SC (Schmidt-Cassegrain)",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Celestron_C8_OTA": {
            "brand": "Celestron",
            "name": "C8 OTA",
            "type": "type_telescope",
            "optical_length": 0,
            "mass": 5600,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "SC (Schmidt-Cassegrain)",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Celestron_C9_25_OTA": {
            "brand": "Celestron",
            "name": "C9.25 OTA",
            "type": "type_telescope",
            "optical_length": 0,
            "mass": 9400,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "SC (Schmidt-Cassegrain)",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Celestron_C11_OTA": {
            "brand": "Celestron",
            "name": "C11 OTA",
            "type": "type_telescope",
            "optical_length": 0,
            "mass": 12400,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "SC (Schmidt-Cassegrain)",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Celestron_C14_OTA": {
            "brand": "Celestron",
            "name": "C14 OTA",
            "type": "type_telescope",
            "optical_length": 0,
            "mass": 20300,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "SC (Schmidt-Cassegrain)",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Celestron_C6_EdgeHD_OTA": {
            "brand": "Celestron",
            "name": "C6 EdgeHD OTA",
            "type": "type_telescope",
            "optical_length": 0,
            "mass": 3900,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "SC (Schmidt-Cassegrain)",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Celestron_C8_EdgeHD_OTA": {
            "brand": "Celestron",
            "name": "C8 EdgeHD OTA",
            "type": "type_telescope",
            "optical_length": 0,
            "mass": 5800,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "SC (Schmidt-Cassegrain)",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Celestron_C9_25_EdgeHD_OTA": {
            "brand": "Celestron",
            "name": "C9.25 EdgeHD OTA",
            "type": "type_telescope",
            "optical_length": 0,
            "mass": 9700,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "SC (Schmidt-Cassegrain)",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Celestron_C11_EdgeHD_OTA": {
            "brand": "Celestron",
            "name": "C11 EdgeHD OTA",
            "type": "type_telescope",
            "optical_length": 0,
            "mass": 12600,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "SC (Schmidt-Cassegrain)",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Celestron_C14_EdgeHD_OTA": {
            "brand": "Celestron",
            "name": "C14 EdgeHD OTA",
            "type": "type_telescope",
            "optical_length": 0,
            "mass": 20400,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "SC (Schmidt-Cassegrain)",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Sky_Watcher_SkyMax_90": {
            "brand": "Sky-Watcher",
            "name": "SkyMax 90",
            "type": "type_telescope",
            "optical_length": 0,
            "mass": 1500,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": '1.25"',
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Sky_Watcher_SkyMax_102_AZ_GTi": {
            "brand": "Sky-Watcher",
            "name": "SkyMax 102 AZ-GTi",
            "type": "type_telescope",
            "optical_length": 0,
            "mass": 2200,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": '2"',
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Sky_Watcher_SkyMax_127_AZ_GTi": {
            "brand": "Sky-Watcher",
            "name": "SkyMax 127 AZ-GTi",
            "type": "type_telescope",
            "optical_length": 0,
            "mass": 3400,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": '2"',
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Sky_Watcher_Star_Discovery_150P": {
            "brand": "Sky-Watcher",
            "name": "Star Discovery 150P",
            "type": "type_telescope",
            "optical_length": 0,
            "mass": 5000,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": '2"',
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Sky_Watcher_Star_Discovery_200P": {
            "brand": "Sky-Watcher",
            "name": "Star Discovery 200P",
            "type": "type_telescope",
            "optical_length": 0,
            "mass": 8200,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": '2"',
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Sky_Watcher_AZ_EQ5_GT_8_Newton": {
            "brand": "Sky-Watcher",
            "name": 'AZ-EQ5 GT 8" Newton',
            "type": "type_telescope",
            "optical_length": 0,
            "mass": 8500,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": '2"',
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Sky_Watcher_AZ_EQ6_Pro_8_Newton": {
            "brand": "Sky-Watcher",
            "name": 'AZ-EQ6 Pro 8" Newton',
            "type": "type_telescope",
            "optical_length": 0,
            "mass": 8600,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": '2"',
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Sky_Watcher_Black_Diamond_ED80": {
            "brand": "Sky-Watcher",
            "name": "Black Diamond ED80",
            "type": "type_refractor",
            "optical_length": 0,
            "mass": 2600,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "M48",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Sky_Watcher_Black_Diamond_ED100": {
            "brand": "Sky-Watcher",
            "name": "Black Diamond ED100",
            "type": "type_refractor",
            "optical_length": 0,
            "mass": 4300,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "M48",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Sky_Watcher_Black_Diamond_ED120": {
            "brand": "Sky-Watcher",
            "name": "Black Diamond ED120",
            "type": "type_refractor",
            "optical_length": 0,
            "mass": 6500,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "M48",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Orion_SpaceProbe_114ST_EQ": {
            "brand": "Orion",
            "name": "SpaceProbe 114ST EQ",
            "type": "type_telescope",
            "optical_length": 0,
            "mass": 2200,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": '2"',
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Orion_StarMax_90mm_Mak": {
            "brand": "Orion",
            "name": "StarMax 90mm Mak",
            "type": "type_telescope",
            "optical_length": 0,
            "mass": 1500,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": '1.25"',
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Orion_StarMax_127mm_Mak": {
            "brand": "Orion",
            "name": "StarMax 127mm Mak",
            "type": "type_telescope",
            "optical_length": 0,
            "mass": 3200,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": '2"',
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Orion_StarMax_102mm_Mak": {
            "brand": "Orion",
            "name": "StarMax 102mm Mak",
            "type": "type_telescope",
            "optical_length": 0,
            "mass": 2100,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": '2"',
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Orion_AstroView_90mm_EQ": {
            "brand": "Orion",
            "name": "AstroView 90mm EQ",
            "type": "type_telescope",
            "optical_length": 0,
            "mass": 2200,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": '1.25"',
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Orion_AstroView_120mm_EQ": {
            "brand": "Orion",
            "name": "AstroView 120mm EQ",
            "type": "type_telescope",
            "optical_length": 0,
            "mass": 3800,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": '2"',
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Orion_SkyQuest_XX8g_Dob": {
            "brand": "Orion",
            "name": "SkyQuest XX8g Dob",
            "type": "type_telescope",
            "optical_length": 0,
            "mass": 7800,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": '2"',
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Orion_SkyQuest_XT4_5_Classic_Dob": {
            "brand": "Orion",
            "name": "SkyQuest XT4.5 Classic Dob",
            "type": "type_telescope",
            "optical_length": 0,
            "mass": 3500,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": '2"',
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Orion_GoScope_80_Refractor": {
            "brand": "Orion",
            "name": "GoScope 80 Refractor",
            "type": "type_refractor",
            "optical_length": 0,
            "mass": 1200,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": '1.25"',
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Orion_ShortTube_80_Refractor": {
            "brand": "Orion",
            "name": "ShortTube 80 Refractor",
            "type": "type_refractor",
            "optical_length": 0,
            "mass": 1000,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": '1.25"',
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Orion_CT80_Refractor_OTA": {
            "brand": "Orion",
            "name": "CT80 Refractor OTA",
            "type": "type_refractor",
            "optical_length": 0,
            "mass": 1100,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": '1.25"',
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Orion_ED80T_CF_OTA": {
            "brand": "Orion",
            "name": "ED80T CF OTA",
            "type": "type_refractor",
            "optical_length": 0,
            "mass": 3000,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "M48",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Bresser_Lyra_150_1200_EQ3": {
            "brand": "Bresser",
            "name": "Lyra 150/1200 EQ3",
            "type": "type_refractor",
            "optical_length": 0,
            "mass": 4200,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": '2"',
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Bresser_Solarix_76_350_AZ": {
            "brand": "Bresser",
            "name": "Solarix 76/350 AZ",
            "type": "type_telescope",
            "optical_length": 0,
            "mass": 1000,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": '1.25"',
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Bresser_Pollux_150_750_EQ3": {
            "brand": "Bresser",
            "name": "Pollux 150/750 EQ3",
            "type": "type_telescope",
            "optical_length": 0,
            "mass": 3800,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": '2"',
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Bresser_National_Geographic_114_500_AZ": {
            "brand": "Bresser",
            "name": "National Geographic 114/500 AZ",
            "type": "type_telescope",
            "optical_length": 0,
            "mass": 2200,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": '1.25"',
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Bresser_National_Geographic_90_1250_Mak": {
            "brand": "Bresser",
            "name": "National Geographic 90/1250 Mak",
            "type": "type_telescope",
            "optical_length": 0,
            "mass": 2000,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": '1.25"',
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Bresser_National_Geographic_130_650_EQ": {
            "brand": "Bresser",
            "name": "National Geographic 130/650 EQ",
            "type": "type_telescope",
            "optical_length": 0,
            "mass": 3200,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": '2"',
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Bresser_FirstLight_152_1200_EQ3": {
            "brand": "Bresser",
            "name": "FirstLight 152/1200 EQ3",
            "type": "type_telescope",
            "optical_length": 0,
            "mass": 5200,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": '2"',
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Bresser_FirstLight_102_460_Table_Dob": {
            "brand": "Bresser",
            "name": "FirstLight 102/460 (Table Dob)",
            "type": "type_telescope",
            "optical_length": 0,
            "mass": 1800,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": '1.25"',
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Meade_ETX_105": {
            "brand": "Meade",
            "name": "ETX-105",
            "type": "type_telescope",
            "optical_length": 0,
            "mass": 3800,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "SC (Schmidt-Cassegrain)",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Meade_ETX_80_AT": {
            "brand": "Meade",
            "name": "ETX-80 AT",
            "type": "type_telescope",
            "optical_length": 0,
            "mass": 1500,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": '1.25"',
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Meade_Infinity_70mm_AZ": {
            "brand": "Meade",
            "name": "Infinity 70mm AZ",
            "type": "type_telescope",
            "optical_length": 0,
            "mass": 900,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": '1.25"',
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Meade_Infinity_80mm_AZ": {
            "brand": "Meade",
            "name": "Infinity 80mm AZ",
            "type": "type_telescope",
            "optical_length": 0,
            "mass": 1200,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": '1.25"',
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Meade_Infinity_90mm_AZ": {
            "brand": "Meade",
            "name": "Infinity 90mm AZ",
            "type": "type_telescope",
            "optical_length": 0,
            "mass": 1800,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": '1.25"',
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Meade_Infinity_102mm_AZ": {
            "brand": "Meade",
            "name": "Infinity 102mm AZ",
            "type": "type_telescope",
            "optical_length": 0,
            "mass": 2500,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": '1.25"',
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Meade_Polaris_114mm_EQ": {
            "brand": "Meade",
            "name": "Polaris 114mm EQ",
            "type": "type_telescope",
            "optical_length": 0,
            "mass": 2400,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": '1.25"',
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Meade_Polaris_70mm_EQ": {
            "brand": "Meade",
            "name": "Polaris 70mm EQ",
            "type": "type_telescope",
            "optical_length": 0,
            "mass": 1100,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": '1.25"',
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Meade_Polaris_90mm_EQ": {
            "brand": "Meade",
            "name": "Polaris 90mm EQ",
            "type": "type_telescope",
            "optical_length": 0,
            "mass": 1500,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": '1.25"',
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Meade_Polaris_80mm_EQ": {
            "brand": "Meade",
            "name": "Polaris 80mm EQ",
            "type": "type_telescope",
            "optical_length": 0,
            "mass": 1300,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": '1.25"',
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Vixen_ED80Sf": {
            "brand": "Vixen",
            "name": "ED80Sf",
            "type": "type_refractor",
            "optical_length": 0,
            "mass": 2800,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "M48",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Vixen_ED81SII": {
            "brand": "Vixen",
            "name": "ED81SII",
            "type": "type_refractor",
            "optical_length": 0,
            "mass": 3200,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "M48",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Vixen_ED103S": {
            "brand": "Vixen",
            "name": "ED103S",
            "type": "type_refractor",
            "optical_length": 0,
            "mass": 4800,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "M48",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Vixen_ED115S_v2": {
            "brand": "Vixen",
            "name": "ED115S v2",
            "type": "type_refractor",
            "optical_length": 0,
            "mass": 6200,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "M48",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Vixen_NA140SSf": {
            "brand": "Vixen",
            "name": "NA140SSf",
            "type": "type_refractor",
            "optical_length": 0,
            "mass": 6000,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "M54",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Vixen_VC200L_v2": {
            "brand": "Vixen",
            "name": "VC200L v2",
            "type": "type_telescope",
            "optical_length": 0,
            "mass": 7000,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "M42",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Vixen_VMC200L_v2": {
            "brand": "Vixen",
            "name": "VMC200L v2",
            "type": "type_telescope",
            "optical_length": 0,
            "mass": 6900,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "M42",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Vixen_R200SS_v2": {
            "brand": "Vixen",
            "name": "R200SS v2",
            "type": "type_telescope",
            "optical_length": 0,
            "mass": 5600,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "M48",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Explore_Scientific_FirstLight_90mm_Mak": {
            "brand": "Explore Scientific",
            "name": "FirstLight 90mm Mak",
            "type": "type_telescope",
            "optical_length": 0,
            "mass": 2000,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": '1.25"',
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Explore_Scientific_FirstLight_114mm_Newton": {
            "brand": "Explore Scientific",
            "name": "FirstLight 114mm Newton",
            "type": "type_telescope",
            "optical_length": 0,
            "mass": 2500,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": '1.25"',
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Explore_Scientific_FirstLight_130mm_Newton": {
            "brand": "Explore Scientific",
            "name": "FirstLight 130mm Newton",
            "type": "type_telescope",
            "optical_length": 0,
            "mass": 3500,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": '2"',
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Explore_Scientific_FirstLight_152mm_Newton": {
            "brand": "Explore Scientific",
            "name": "FirstLight 152mm Newton",
            "type": "type_telescope",
            "optical_length": 0,
            "mass": 5500,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": '2"',
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Explore_Scientific_StarGate_18_Truss_Dob": {
            "brand": "Explore Scientific",
            "name": 'StarGate 18" Truss Dob',
            "type": "type_telescope",
            "optical_length": 0,
            "mass": 25000,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": '2"',
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Explore_Scientific_StarGate_20_Truss_Dob": {
            "brand": "Explore Scientific",
            "name": 'StarGate 20" Truss Dob',
            "type": "type_telescope",
            "optical_length": 0,
            "mass": 32000,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": '2"',
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Explore_Scientific_ED165_FCD100_CF": {
            "brand": "Explore Scientific",
            "name": "ED165 FCD100 CF",
            "type": "type_refractor",
            "optical_length": 0,
            "mass": 14000,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "M68",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Explore_Scientific_ED127_FCD1_CF": {
            "brand": "Explore Scientific",
            "name": "ED127 FCD1 CF",
            "type": "type_refractor",
            "optical_length": 0,
            "mass": 7200,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "M68",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "William_Optics_RedCat_71": {
            "brand": "William Optics",
            "name": "RedCat 71",
            "type": "type_refractor",
            "optical_length": 0,
            "mass": 3200,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "M48",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "William_Optics_SpaceCat_51_v2": {
            "brand": "William Optics",
            "name": "SpaceCat 51 v2",
            "type": "type_refractor",
            "optical_length": 0,
            "mass": 1400,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "M48",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "William_Optics_WhiteCat_71": {
            "brand": "William Optics",
            "name": "WhiteCat 71",
            "type": "type_refractor",
            "optical_length": 0,
            "mass": 3300,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "M48",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "William_Optics_GT71_v2": {
            "brand": "William Optics",
            "name": "GT71 v2",
            "type": "type_refractor",
            "optical_length": 0,
            "mass": 2300,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "M48",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "William_Optics_GT81_v2": {
            "brand": "William Optics",
            "name": "GT81 v2",
            "type": "type_refractor",
            "optical_length": 0,
            "mass": 2900,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "M48",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "William_Optics_GT102_v2": {
            "brand": "William Optics",
            "name": "GT102 v2",
            "type": "type_refractor",
            "optical_length": 0,
            "mass": 4600,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "M48",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "William_Optics_ZenithStar_61_III": {
            "brand": "William Optics",
            "name": "ZenithStar 61 III",
            "type": "type_refractor",
            "optical_length": 0,
            "mass": 1700,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "M48",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "William_Optics_ZenithStar_73_v2": {
            "brand": "William Optics",
            "name": "ZenithStar 73 v2",
            "type": "type_refractor",
            "optical_length": 0,
            "mass": 2200,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "M48",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "William_Optics_ZenithStar_81_v2": {
            "brand": "William Optics",
            "name": "ZenithStar 81 v2",
            "type": "type_refractor",
            "optical_length": 0,
            "mass": 2600,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "M48",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "William_Optics_Pleiades_68_v2": {
            "brand": "William Optics",
            "name": "Pleiades 68 v2",
            "type": "type_refractor",
            "optical_length": 0,
            "mass": 1900,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "M48",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "William_Optics_FluoroStar_91_v2": {
            "brand": "William Optics",
            "name": "FluoroStar 91 v2",
            "type": "type_refractor",
            "optical_length": 0,
            "mass": 3600,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "M48",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "William_Optics_FluoroStar_132_v2": {
            "brand": "William Optics",
            "name": "FluoroStar 132 v2",
            "type": "type_refractor",
            "optical_length": 0,
            "mass": 6300,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "M68",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Askar_FRA300_Pro_v2": {
            "brand": "Askar",
            "name": "FRA300 Pro v2",
            "type": "type_refractor",
            "optical_length": 0,
            "mass": 1900,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "M42",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Askar_FRA400_v2": {
            "brand": "Askar",
            "name": "FRA400 v2",
            "type": "type_refractor",
            "optical_length": 0,
            "mass": 2300,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "M48",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Askar_FRA500_v2": {
            "brand": "Askar",
            "name": "FRA500 v2",
            "type": "type_refractor",
            "optical_length": 0,
            "mass": 3100,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "M48",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Askar_FRA600_v2": {
            "brand": "Askar",
            "name": "FRA600 v2",
            "type": "type_refractor",
            "optical_length": 0,
            "mass": 3600,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "M48",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Askar_65PHQ_v2": {
            "brand": "Askar",
            "name": "65PHQ v2",
            "type": "type_refractor",
            "optical_length": 0,
            "mass": 2300,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "M48",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Askar_80PHQ_v2": {
            "brand": "Askar",
            "name": "80PHQ v2",
            "type": "type_refractor",
            "optical_length": 0,
            "mass": 3600,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "M54",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Askar_107PHQ_v2": {
            "brand": "Askar",
            "name": "107PHQ v2",
            "type": "type_refractor",
            "optical_length": 0,
            "mass": 5100,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "M68",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Askar_130PHQ_v2": {
            "brand": "Askar",
            "name": "130PHQ v2",
            "type": "type_refractor",
            "optical_length": 0,
            "mass": 6100,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "M68",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Askar_151PHQ_v2": {
            "brand": "Askar",
            "name": "151PHQ v2",
            "type": "type_refractor",
            "optical_length": 0,
            "mass": 8600,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "M68",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Askar_V_60Q_v2": {
            "brand": "Askar",
            "name": "V 60Q v2",
            "type": "type_refractor",
            "optical_length": 0,
            "mass": 1700,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "M48",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Askar_V_80Q_v2": {
            "brand": "Askar",
            "name": "V 80Q v2",
            "type": "type_refractor",
            "optical_length": 0,
            "mass": 2300,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "M48",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Askar_FMA_230_v2": {
            "brand": "Askar",
            "name": "FMA 230 v2",
            "type": "type_refractor",
            "optical_length": 0,
            "mass": 1100,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "M42",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Askar_200APO_v2": {
            "brand": "Askar",
            "name": "200APO v2",
            "type": "type_refractor",
            "optical_length": 0,
            "mass": 14200,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "M68",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Askar_71Q": {
            "brand": "Askar",
            "name": "71Q",
            "type": "type_refractor",
            "optical_length": 0,
            "mass": 2400,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "M48",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Askar_55Q": {
            "brand": "Askar",
            "name": "55Q",
            "type": "type_refractor",
            "optical_length": 0,
            "mass": 1500,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "M42",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Sharpstar_61EDPH_III": {
            "brand": "Sharpstar",
            "name": "61EDPH III",
            "type": "type_refractor",
            "optical_length": 0,
            "mass": 2600,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "M48",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Sharpstar_76EDPH_III": {
            "brand": "Sharpstar",
            "name": "76EDPH III",
            "type": "type_refractor",
            "optical_length": 0,
            "mass": 3300,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "M48",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Sharpstar_94EDPH_III": {
            "brand": "Sharpstar",
            "name": "94EDPH III",
            "type": "type_refractor",
            "optical_length": 0,
            "mass": 4600,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "M54",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Sharpstar_100Q": {
            "brand": "Sharpstar",
            "name": "100Q",
            "type": "type_refractor",
            "optical_length": 0,
            "mass": 3800,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "M54",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Sharpstar_120Q": {
            "brand": "Sharpstar",
            "name": "120Q",
            "type": "type_refractor",
            "optical_length": 0,
            "mass": 5500,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "M68",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Sharpstar_140PH_v2": {
            "brand": "Sharpstar",
            "name": "140PH v2",
            "type": "type_refractor",
            "optical_length": 0,
            "mass": 6200,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "M68",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Sharpstar_15028HNT_v2": {
            "brand": "Sharpstar",
            "name": "15028HNT v2",
            "type": "type_telescope",
            "optical_length": 0,
            "mass": 9700,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "M68",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Sharpstar_20032HNT_v2": {
            "brand": "Sharpstar",
            "name": "20032HNT v2",
            "type": "type_telescope",
            "optical_length": 0,
            "mass": 13200,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "M68",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Stellarvue_SV48_Access": {
            "brand": "Stellarvue",
            "name": "SV48 Access",
            "type": "type_refractor",
            "optical_length": 0,
            "mass": 900,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "M42",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Stellarvue_SV60EDS_v2": {
            "brand": "Stellarvue",
            "name": "SV60EDS v2",
            "type": "type_refractor",
            "optical_length": 0,
            "mass": 1300,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "M42",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Stellarvue_SV70T_v2": {
            "brand": "Stellarvue",
            "name": "SV70T v2",
            "type": "type_refractor",
            "optical_length": 0,
            "mass": 1900,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "M48",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Stellarvue_SVX080T_v2": {
            "brand": "Stellarvue",
            "name": "SVX080T v2",
            "type": "type_refractor",
            "optical_length": 0,
            "mass": 2900,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "M48",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Stellarvue_SVX090T_v2": {
            "brand": "Stellarvue",
            "name": "SVX090T v2",
            "type": "type_refractor",
            "optical_length": 0,
            "mass": 3300,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "M48",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Stellarvue_SVX102T_v2": {
            "brand": "Stellarvue",
            "name": "SVX102T v2",
            "type": "type_refractor",
            "optical_length": 0,
            "mass": 4300,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "M48",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Stellarvue_SVX130T_v2": {
            "brand": "Stellarvue",
            "name": "SVX130T v2",
            "type": "type_refractor",
            "optical_length": 0,
            "mass": 7200,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "M68",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Stellarvue_SVX152T_v2": {
            "brand": "Stellarvue",
            "name": "SVX152T v2",
            "type": "type_refractor",
            "optical_length": 0,
            "mass": 10200,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "M68",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Stellarvue_SVX070T_Raptor": {
            "brand": "Stellarvue",
            "name": "SVX070T Raptor",
            "type": "type_refractor",
            "optical_length": 0,
            "mass": 2200,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "M48",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Irix_150mm_f_2_8_Macro_EOS": {
            "brand": "Irix",
            "name": "150mm f/2.8 Macro (EOS)",
            "type": "type_camera_lens",
            "optical_length": 0,
            "mass": 831,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "EOS",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Irix_150mm_f_2_8_Macro_Nikon_F": {
            "brand": "Irix",
            "name": "150mm f/2.8 Macro (Nikon F)",
            "type": "type_camera_lens",
            "optical_length": 0,
            "mass": 831,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "Nikon F",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Irix_11mm_f_4_Firefly_EOS": {
            "brand": "Irix",
            "name": "11mm f/4 Firefly (EOS)",
            "type": "type_camera_lens",
            "optical_length": 0,
            "mass": 535,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "EOS",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Irix_11mm_f_4_Firefly_Nikon_F": {
            "brand": "Irix",
            "name": "11mm f/4 Firefly (Nikon F)",
            "type": "type_camera_lens",
            "optical_length": 0,
            "mass": 535,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "Nikon F",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Irix_15mm_f_2_4_Blackstone_EOS": {
            "brand": "Irix",
            "name": "15mm f/2.4 Blackstone (EOS)",
            "type": "type_camera_lens",
            "optical_length": 0,
            "mass": 562,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "EOS",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Irix_15mm_f_2_4_Blackstone_Nikon_F": {
            "brand": "Irix",
            "name": "15mm f/2.4 Blackstone (Nikon F)",
            "type": "type_camera_lens",
            "optical_length": 0,
            "mass": 562,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "Nikon F",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Irix_45mm_f_1_4_EOS": {
            "brand": "Irix",
            "name": "45mm f/1.4 (EOS)",
            "type": "type_camera_lens",
            "optical_length": 0,
            "mass": 720,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "EOS",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Irix_45mm_f_1_4_Nikon_F": {
            "brand": "Irix",
            "name": "45mm f/1.4 (Nikon F)",
            "type": "type_camera_lens",
            "optical_length": 0,
            "mass": 720,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "Nikon F",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Irix_45mm_f_1_4_Sony_E": {
            "brand": "Irix",
            "name": "45mm f/1.4 (Sony E)",
            "type": "type_camera_lens",
            "optical_length": 0,
            "mass": 720,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "Sony E",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Laowa_15mm_f_2_Zero_D_EOS": {
            "brand": "Laowa",
            "name": "15mm f/2 Zero-D (EOS)",
            "type": "type_camera_lens",
            "optical_length": 0,
            "mass": 500,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "EOS",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Laowa_15mm_f_2_Zero_D_Sony_E": {
            "brand": "Laowa",
            "name": "15mm f/2 Zero-D (Sony E)",
            "type": "type_camera_lens",
            "optical_length": 0,
            "mass": 500,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "Sony E",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Laowa_15mm_f_2_Zero_D_Nikon_Z": {
            "brand": "Laowa",
            "name": "15mm f/2 Zero-D (Nikon Z)",
            "type": "type_camera_lens",
            "optical_length": 0,
            "mass": 500,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "Nikon Z",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Laowa_15mm_f_2_Zero_D_Canon_RF": {
            "brand": "Laowa",
            "name": "15mm f/2 Zero-D (Canon RF)",
            "type": "type_camera_lens",
            "optical_length": 0,
            "mass": 500,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "Canon RF",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Laowa_100mm_f_2_8_2_1_Macro_EOS": {
            "brand": "Laowa",
            "name": "100mm f/2.8 2:1 Macro (EOS)",
            "type": "type_camera_lens",
            "optical_length": 0,
            "mass": 638,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "EOS",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Laowa_100mm_f_2_8_2_1_Macro_Sony_E": {
            "brand": "Laowa",
            "name": "100mm f/2.8 2:1 Macro (Sony E)",
            "type": "type_camera_lens",
            "optical_length": 0,
            "mass": 638,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "Sony E",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Laowa_10_18mm_f_4_5_5_6_Sony_E": {
            "brand": "Laowa",
            "name": "10-18mm f/4.5-5.6 (Sony E)",
            "type": "type_camera_lens",
            "optical_length": 0,
            "mass": 497,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "Sony E",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Laowa_10_18mm_f_4_5_5_6_Nikon_Z": {
            "brand": "Laowa",
            "name": "10-18mm f/4.5-5.6 (Nikon Z)",
            "type": "type_camera_lens",
            "optical_length": 0,
            "mass": 497,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "Nikon Z",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Laowa_12mm_f_2_8_Zero_D_EOS": {
            "brand": "Laowa",
            "name": "12mm f/2.8 Zero-D (EOS)",
            "type": "type_camera_lens",
            "optical_length": 0,
            "mass": 210,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "EOS",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Laowa_12mm_f_2_8_Zero_D_Sony_E": {
            "brand": "Laowa",
            "name": "12mm f/2.8 Zero-D (Sony E)",
            "type": "type_camera_lens",
            "optical_length": 0,
            "mass": 210,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "Sony E",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Laowa_9mm_f_2_8_Zero_D_MFT": {
            "brand": "Laowa",
            "name": "9mm f/2.8 Zero-D (MFT)",
            "type": "type_camera_lens",
            "optical_length": 0,
            "mass": 215,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "MFT",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Laowa_9mm_f_2_8_Zero_D_Fuji_X": {
            "brand": "Laowa",
            "name": "9mm f/2.8 Zero-D (Fuji X)",
            "type": "type_camera_lens",
            "optical_length": 0,
            "mass": 215,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "Fuji X",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Laowa_9mm_f_5_6_FF_RL_Sony_E": {
            "brand": "Laowa",
            "name": "9mm f/5.6 FF RL (Sony E)",
            "type": "type_camera_lens",
            "optical_length": 0,
            "mass": 350,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "Sony E",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Laowa_9mm_f_5_6_FF_RL_Nikon_Z": {
            "brand": "Laowa",
            "name": "9mm f/5.6 FF RL (Nikon Z)",
            "type": "type_camera_lens",
            "optical_length": 0,
            "mass": 350,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "Nikon Z",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Laowa_14mm_f_4_Zero_D_Sony_E": {
            "brand": "Laowa",
            "name": "14mm f/4 Zero-D (Sony E)",
            "type": "type_camera_lens",
            "optical_length": 0,
            "mass": 320,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "Sony E",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Laowa_14mm_f_4_Zero_D_Nikon_Z": {
            "brand": "Laowa",
            "name": "14mm f/4 Zero-D (Nikon Z)",
            "type": "type_camera_lens",
            "optical_length": 0,
            "mass": 320,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "Nikon Z",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Laowa_24mm_f_14_Probe_EOS": {
            "brand": "Laowa",
            "name": "24mm f/14 Probe (EOS)",
            "type": "type_camera_lens",
            "optical_length": 0,
            "mass": 474,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "EOS",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Laowa_65mm_f_2_8_2x_Macro_Sony_E": {
            "brand": "Laowa",
            "name": "65mm f/2.8 2x Macro (Sony E)",
            "type": "type_camera_lens",
            "optical_length": 0,
            "mass": 335,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "Sony E",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Laowa_85mm_f_5_6_2x_Macro_Sony_E": {
            "brand": "Laowa",
            "name": "85mm f/5.6 2x Macro (Sony E)",
            "type": "type_camera_lens",
            "optical_length": 0,
            "mass": 247,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "Sony E",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Meike_85mm_f_1_8_Sony_E": {
            "brand": "Meike",
            "name": "85mm f/1.8 (Sony E)",
            "type": "type_camera_lens",
            "optical_length": 0,
            "mass": 390,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "Sony E",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Meike_85mm_f_1_8_Fuji_X": {
            "brand": "Meike",
            "name": "85mm f/1.8 (Fuji X)",
            "type": "type_camera_lens",
            "optical_length": 0,
            "mass": 390,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "Fuji X",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Meike_85mm_f_1_8_Nikon_Z": {
            "brand": "Meike",
            "name": "85mm f/1.8 (Nikon Z)",
            "type": "type_camera_lens",
            "optical_length": 0,
            "mass": 390,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "Nikon Z",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Meike_85mm_f_1_8_Canon_RF": {
            "brand": "Meike",
            "name": "85mm f/1.8 (Canon RF)",
            "type": "type_camera_lens",
            "optical_length": 0,
            "mass": 390,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "Canon RF",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Meike_25mm_f_1_8_Sony_E": {
            "brand": "Meike",
            "name": "25mm f/1.8 (Sony E)",
            "type": "type_camera_lens",
            "optical_length": 0,
            "mass": 125,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "Sony E",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Meike_25mm_f_1_8_MFT": {
            "brand": "Meike",
            "name": "25mm f/1.8 (MFT)",
            "type": "type_camera_lens",
            "optical_length": 0,
            "mass": 125,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "MFT",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Meike_25mm_f_1_8_Fuji_X": {
            "brand": "Meike",
            "name": "25mm f/1.8 (Fuji X)",
            "type": "type_camera_lens",
            "optical_length": 0,
            "mass": 125,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "Fuji X",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Meike_50mm_f_1_7_Sony_E": {
            "brand": "Meike",
            "name": "50mm f/1.7 (Sony E)",
            "type": "type_camera_lens",
            "optical_length": 0,
            "mass": 310,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "Sony E",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Meike_50mm_f_1_7_Fuji_X": {
            "brand": "Meike",
            "name": "50mm f/1.7 (Fuji X)",
            "type": "type_camera_lens",
            "optical_length": 0,
            "mass": 310,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "Fuji X",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Meike_35mm_f_1_7_Sony_E": {
            "brand": "Meike",
            "name": "35mm f/1.7 (Sony E)",
            "type": "type_camera_lens",
            "optical_length": 0,
            "mass": 156,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "Sony E",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Meike_6_5mm_f_2_0_Circular_Fisheye_MFT": {
            "brand": "Meike",
            "name": "6.5mm f/2.0 Circular Fisheye (MFT)",
            "type": "type_camera_lens",
            "optical_length": 0,
            "mass": 210,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "MFT",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "TTArtisan_50mm_f_1_4_Sony_E": {
            "brand": "TTArtisan",
            "name": "50mm f/1.4 (Sony E)",
            "type": "type_camera_lens",
            "optical_length": 0,
            "mass": 310,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "Sony E",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "TTArtisan_50mm_f_1_4_Fuji_X": {
            "brand": "TTArtisan",
            "name": "50mm f/1.4 (Fuji X)",
            "type": "type_camera_lens",
            "optical_length": 0,
            "mass": 310,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "Fuji X",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "TTArtisan_50mm_f_1_4_Nikon_Z": {
            "brand": "TTArtisan",
            "name": "50mm f/1.4 (Nikon Z)",
            "type": "type_camera_lens",
            "optical_length": 0,
            "mass": 310,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "Nikon Z",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "TTArtisan_35mm_f_1_4_Sony_E": {
            "brand": "TTArtisan",
            "name": "35mm f/1.4 (Sony E)",
            "type": "type_camera_lens",
            "optical_length": 0,
            "mass": 340,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "Sony E",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "TTArtisan_35mm_f_1_4_Fuji_X": {
            "brand": "TTArtisan",
            "name": "35mm f/1.4 (Fuji X)",
            "type": "type_camera_lens",
            "optical_length": 0,
            "mass": 340,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "Fuji X",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "TTArtisan_35mm_f_1_4_Nikon_Z": {
            "brand": "TTArtisan",
            "name": "35mm f/1.4 (Nikon Z)",
            "type": "type_camera_lens",
            "optical_length": 0,
            "mass": 340,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "Nikon Z",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "TTArtisan_23mm_f_1_4_Fuji_X": {
            "brand": "TTArtisan",
            "name": "23mm f/1.4 (Fuji X)",
            "type": "type_camera_lens",
            "optical_length": 0,
            "mass": 240,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "Fuji X",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "TTArtisan_23mm_f_1_4_Sony_E": {
            "brand": "TTArtisan",
            "name": "23mm f/1.4 (Sony E)",
            "type": "type_camera_lens",
            "optical_length": 0,
            "mass": 240,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "Sony E",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "TTArtisan_17mm_f_1_4_MFT": {
            "brand": "TTArtisan",
            "name": "17mm f/1.4 (MFT)",
            "type": "type_camera_lens",
            "optical_length": 0,
            "mass": 268,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "MFT",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "TTArtisan_21mm_f_1_5_Sony_E": {
            "brand": "TTArtisan",
            "name": "21mm f/1.5 (Sony E)",
            "type": "type_camera_lens",
            "optical_length": 0,
            "mass": 480,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "Sony E",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "TTArtisan_90mm_f_1_25_Sony_E": {
            "brand": "TTArtisan",
            "name": "90mm f/1.25 (Sony E)",
            "type": "type_camera_lens",
            "optical_length": 0,
            "mass": 810,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "Sony E",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "TTArtisan_11mm_f_2_8_Fisheye_Sony_E": {
            "brand": "TTArtisan",
            "name": "11mm f/2.8 Fisheye (Sony E)",
            "type": "type_camera_lens",
            "optical_length": 0,
            "mass": 230,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "Sony E",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "TTArtisan_27mm_f_2_8_Sony_E": {
            "brand": "TTArtisan",
            "name": "27mm f/2.8 (Sony E)",
            "type": "type_camera_lens",
            "optical_length": 0,
            "mass": 78,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "Sony E",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "TTArtisan_27mm_f_2_8_Fuji_X": {
            "brand": "TTArtisan",
            "name": "27mm f/2.8 (Fuji X)",
            "type": "type_camera_lens",
            "optical_length": 0,
            "mass": 78,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "Fuji X",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "TTArtisan_27mm_f_2_8_Nikon_Z": {
            "brand": "TTArtisan",
            "name": "27mm f/2.8 (Nikon Z)",
            "type": "type_camera_lens",
            "optical_length": 0,
            "mass": 78,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "Nikon Z",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "TTArtisan_50mm_f_2_Sony_E": {
            "brand": "TTArtisan",
            "name": "50mm f/2 (Sony E)",
            "type": "type_camera_lens",
            "optical_length": 0,
            "mass": 195,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "Sony E",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "TTArtisan_50mm_f_2_Nikon_Z": {
            "brand": "TTArtisan",
            "name": "50mm f/2 (Nikon Z)",
            "type": "type_camera_lens",
            "optical_length": 0,
            "mass": 195,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "Nikon Z",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "TTArtisan_35mm_f_0_95_MFT": {
            "brand": "TTArtisan",
            "name": "35mm f/0.95 (MFT)",
            "type": "type_camera_lens",
            "optical_length": 0,
            "mass": 630,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "MFT",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "TTArtisan_50mm_f_0_95_Sony_E": {
            "brand": "TTArtisan",
            "name": "50mm f/0.95 (Sony E)",
            "type": "type_camera_lens",
            "optical_length": 0,
            "mass": 730,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "Sony E",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Mitakon_85mm_f_1_2_Sony_E": {
            "brand": "Mitakon",
            "name": "85mm f/1.2 (Sony E)",
            "type": "type_camera_lens",
            "optical_length": 0,
            "mass": 690,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "Sony E",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Mitakon_85mm_f_1_2_EOS": {
            "brand": "Mitakon",
            "name": "85mm f/1.2 (EOS)",
            "type": "type_camera_lens",
            "optical_length": 0,
            "mass": 690,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "EOS",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Mitakon_85mm_f_1_2_Nikon_F": {
            "brand": "Mitakon",
            "name": "85mm f/1.2 (Nikon F)",
            "type": "type_camera_lens",
            "optical_length": 0,
            "mass": 690,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "Nikon F",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Mitakon_50mm_f_0_95_Sony_E": {
            "brand": "Mitakon",
            "name": "50mm f/0.95 (Sony E)",
            "type": "type_camera_lens",
            "optical_length": 0,
            "mass": 720,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "Sony E",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Mitakon_50mm_f_0_95_Nikon_Z": {
            "brand": "Mitakon",
            "name": "50mm f/0.95 (Nikon Z)",
            "type": "type_camera_lens",
            "optical_length": 0,
            "mass": 720,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "Nikon Z",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Mitakon_35mm_f_0_95_Sony_E": {
            "brand": "Mitakon",
            "name": "35mm f/0.95 (Sony E)",
            "type": "type_camera_lens",
            "optical_length": 0,
            "mass": 560,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "Sony E",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Mitakon_35mm_f_0_95_MFT": {
            "brand": "Mitakon",
            "name": "35mm f/0.95 (MFT)",
            "type": "type_camera_lens",
            "optical_length": 0,
            "mass": 560,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "MFT",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Mitakon_35mm_f_0_95_Fuji_X": {
            "brand": "Mitakon",
            "name": "35mm f/0.95 (Fuji X)",
            "type": "type_camera_lens",
            "optical_length": 0,
            "mass": 560,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "Fuji X",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Mitakon_20mm_f_2_4_5x_Macro_Sony_E": {
            "brand": "Mitakon",
            "name": "20mm f/2 4.5x Macro (Sony E)",
            "type": "type_camera_lens",
            "optical_length": 0,
            "mass": 345,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "Sony E",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Canon_EF_S_35mm_f_2_8_Macro_IS_STM": {
            "brand": "Canon",
            "name": "EF-S 35mm f/2.8 Macro IS STM",
            "type": "type_camera_lens",
            "optical_length": 0,
            "mass": 190,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "EOS",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Canon_EF_S_60mm_f_2_8_Macro_USM": {
            "brand": "Canon",
            "name": "EF-S 60mm f/2.8 Macro USM",
            "type": "type_camera_lens",
            "optical_length": 0,
            "mass": 335,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "EOS",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Canon_RF_35mm_f_1_8_Macro_IS_STM": {
            "brand": "Canon",
            "name": "RF 35mm f/1.8 Macro IS STM",
            "type": "type_camera_lens",
            "optical_length": 0,
            "mass": 305,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "Canon RF",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Canon_MP_E_65mm_f_2_8_1_5x_Macro": {
            "brand": "Canon",
            "name": "MP-E 65mm f/2.8 1-5x Macro",
            "type": "type_camera_lens",
            "optical_length": 0,
            "mass": 710,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "EOS",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Nikon_Z_MC_105mm_f_2_8_VR_S": {
            "brand": "Nikon",
            "name": "Z MC 105mm f/2.8 VR S",
            "type": "type_camera_lens",
            "optical_length": 0,
            "mass": 630,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "Nikon Z",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Nikon_Z_MC_50mm_f_2_8": {
            "brand": "Nikon",
            "name": "Z MC 50mm f/2.8",
            "type": "type_camera_lens",
            "optical_length": 0,
            "mass": 260,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "Nikon Z",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Nikon_AF_S_Micro_105mm_f_2_8G_VR": {
            "brand": "Nikon",
            "name": "AF-S Micro 105mm f/2.8G VR",
            "type": "type_camera_lens",
            "optical_length": 0,
            "mass": 720,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "Nikon F",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Sony_FE_90mm_f_2_8_Macro_G_OSS": {
            "brand": "Sony",
            "name": "FE 90mm f/2.8 Macro G OSS",
            "type": "type_camera_lens",
            "optical_length": 0,
            "mass": 602,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "Sony E",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Sony_FE_50mm_f_2_8_Macro": {
            "brand": "Sony",
            "name": "FE 50mm f/2.8 Macro",
            "type": "type_camera_lens",
            "optical_length": 0,
            "mass": 236,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "Sony E",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
    }

    @classmethod
    def Celestron_C5_SCT(cls):
        return cls.from_database(cls._DATABASE["Celestron_C5_SCT"])

    @classmethod
    def Celestron_C6_SCT(cls):
        return cls.from_database(cls._DATABASE["Celestron_C6_SCT"])

    @classmethod
    def Celestron_C8_SCT(cls):
        return cls.from_database(cls._DATABASE["Celestron_C8_SCT"])

    @classmethod
    def Celestron_C9_25_SCT(cls):
        return cls.from_database(cls._DATABASE["Celestron_C9_25_SCT"])

    @classmethod
    def Celestron_C11_SCT(cls):
        return cls.from_database(cls._DATABASE["Celestron_C11_SCT"])

    @classmethod
    def Celestron_C14_SCT(cls):
        return cls.from_database(cls._DATABASE["Celestron_C14_SCT"])

    @classmethod
    def Celestron_C6_EdgeHD(cls):
        return cls.from_database(cls._DATABASE["Celestron_C6_EdgeHD"])

    @classmethod
    def Celestron_C8_EdgeHD(cls):
        return cls.from_database(cls._DATABASE["Celestron_C8_EdgeHD"])

    @classmethod
    def Celestron_C9_25_EdgeHD(cls):
        return cls.from_database(cls._DATABASE["Celestron_C9_25_EdgeHD"])

    @classmethod
    def Celestron_C11_EdgeHD(cls):
        return cls.from_database(cls._DATABASE["Celestron_C11_EdgeHD"])

    @classmethod
    def Celestron_C14_EdgeHD(cls):
        return cls.from_database(cls._DATABASE["Celestron_C14_EdgeHD"])

    @classmethod
    def Celestron_NexStar_4SE(cls):
        return cls.from_database(cls._DATABASE["Celestron_NexStar_4SE"])

    @classmethod
    def Celestron_NexStar_5SE(cls):
        return cls.from_database(cls._DATABASE["Celestron_NexStar_5SE"])

    @classmethod
    def Celestron_NexStar_6SE(cls):
        return cls.from_database(cls._DATABASE["Celestron_NexStar_6SE"])

    @classmethod
    def Celestron_NexStar_8SE(cls):
        return cls.from_database(cls._DATABASE["Celestron_NexStar_8SE"])

    @classmethod
    def Celestron_NexStar_Evolution_6(cls):
        return cls.from_database(cls._DATABASE["Celestron_NexStar_Evolution_6"])

    @classmethod
    def Celestron_NexStar_Evolution_8(cls):
        return cls.from_database(cls._DATABASE["Celestron_NexStar_Evolution_8"])

    @classmethod
    def Celestron_CGX_L_1100_SCT(cls):
        return cls.from_database(cls._DATABASE["Celestron_CGX_L_1100_SCT"])

    @classmethod
    def Celestron_CGX_L_1400_SCT(cls):
        return cls.from_database(cls._DATABASE["Celestron_CGX_L_1400_SCT"])

    @classmethod
    def Celestron_Advanced_VX_8_SCT(cls):
        return cls.from_database(cls._DATABASE["Celestron_Advanced_VX_8_SCT"])

    @classmethod
    def Celestron_CPC_800(cls):
        return cls.from_database(cls._DATABASE["Celestron_CPC_800"])

    @classmethod
    def Celestron_CPC_1100(cls):
        return cls.from_database(cls._DATABASE["Celestron_CPC_1100"])

    @classmethod
    def Celestron_CPC_Deluxe_1100_EdgeHD(cls):
        return cls.from_database(cls._DATABASE["Celestron_CPC_Deluxe_1100_EdgeHD"])

    @classmethod
    def Celestron_RASA_8(cls):
        return cls.from_database(cls._DATABASE["Celestron_RASA_8"])

    @classmethod
    def Celestron_RASA_11(cls):
        return cls.from_database(cls._DATABASE["Celestron_RASA_11"])

    @classmethod
    def Celestron_RASA_14(cls):
        return cls.from_database(cls._DATABASE["Celestron_RASA_14"])

    @classmethod
    def Celestron_RASA_36cm(cls):
        return cls.from_database(cls._DATABASE["Celestron_RASA_36cm"])

    @classmethod
    def Sky_Watcher_Esprit_80ED(cls):
        return cls.from_database(cls._DATABASE["Sky_Watcher_Esprit_80ED"])

    @classmethod
    def Sky_Watcher_Esprit_100ED(cls):
        return cls.from_database(cls._DATABASE["Sky_Watcher_Esprit_100ED"])

    @classmethod
    def Sky_Watcher_Esprit_120ED(cls):
        return cls.from_database(cls._DATABASE["Sky_Watcher_Esprit_120ED"])

    @classmethod
    def Sky_Watcher_Esprit_150ED(cls):
        return cls.from_database(cls._DATABASE["Sky_Watcher_Esprit_150ED"])

    @classmethod
    def Sky_Watcher_Evostar_72ED(cls):
        return cls.from_database(cls._DATABASE["Sky_Watcher_Evostar_72ED"])

    @classmethod
    def Sky_Watcher_Evostar_80ED(cls):
        return cls.from_database(cls._DATABASE["Sky_Watcher_Evostar_80ED"])

    @classmethod
    def Sky_Watcher_Evostar_100ED(cls):
        return cls.from_database(cls._DATABASE["Sky_Watcher_Evostar_100ED"])

    @classmethod
    def Sky_Watcher_Evostar_120ED(cls):
        return cls.from_database(cls._DATABASE["Sky_Watcher_Evostar_120ED"])

    @classmethod
    def Sky_Watcher_Evostar_72ED_DS_Pro(cls):
        return cls.from_database(cls._DATABASE["Sky_Watcher_Evostar_72ED_DS_Pro"])

    @classmethod
    def Sky_Watcher_Evostar_80ED_DS_Pro(cls):
        return cls.from_database(cls._DATABASE["Sky_Watcher_Evostar_80ED_DS_Pro"])

    @classmethod
    def Sky_Watcher_Evostar_100ED_DS_Pro(cls):
        return cls.from_database(cls._DATABASE["Sky_Watcher_Evostar_100ED_DS_Pro"])

    @classmethod
    def Sky_Watcher_Evostar_150ED(cls):
        return cls.from_database(cls._DATABASE["Sky_Watcher_Evostar_150ED"])

    @classmethod
    def Sky_Watcher_Quattro_150P(cls):
        return cls.from_database(cls._DATABASE["Sky_Watcher_Quattro_150P"])

    @classmethod
    def Sky_Watcher_Quattro_200P(cls):
        return cls.from_database(cls._DATABASE["Sky_Watcher_Quattro_200P"])

    @classmethod
    def Sky_Watcher_Quattro_250P(cls):
        return cls.from_database(cls._DATABASE["Sky_Watcher_Quattro_250P"])

    @classmethod
    def Sky_Watcher_Quattro_300P(cls):
        return cls.from_database(cls._DATABASE["Sky_Watcher_Quattro_300P"])

    @classmethod
    def Sky_Watcher_150PDS_Newtonian(cls):
        return cls.from_database(cls._DATABASE["Sky_Watcher_150PDS_Newtonian"])

    @classmethod
    def Sky_Watcher_200PDS_Newtonian(cls):
        return cls.from_database(cls._DATABASE["Sky_Watcher_200PDS_Newtonian"])

    @classmethod
    def Sky_Watcher_250PDS_Newtonian(cls):
        return cls.from_database(cls._DATABASE["Sky_Watcher_250PDS_Newtonian"])

    @classmethod
    def Sky_Watcher_Explorer_130P(cls):
        return cls.from_database(cls._DATABASE["Sky_Watcher_Explorer_130P"])

    @classmethod
    def Sky_Watcher_Explorer_150P(cls):
        return cls.from_database(cls._DATABASE["Sky_Watcher_Explorer_150P"])

    @classmethod
    def Sky_Watcher_Explorer_200P(cls):
        return cls.from_database(cls._DATABASE["Sky_Watcher_Explorer_200P"])

    @classmethod
    def Sky_Watcher_Explorer_250P(cls):
        return cls.from_database(cls._DATABASE["Sky_Watcher_Explorer_250P"])

    @classmethod
    def Sky_Watcher_Explorer_300P(cls):
        return cls.from_database(cls._DATABASE["Sky_Watcher_Explorer_300P"])

    @classmethod
    def Sky_Watcher_Skyliner_150P(cls):
        return cls.from_database(cls._DATABASE["Sky_Watcher_Skyliner_150P"])

    @classmethod
    def Sky_Watcher_Skyliner_200P(cls):
        return cls.from_database(cls._DATABASE["Sky_Watcher_Skyliner_200P"])

    @classmethod
    def Sky_Watcher_Skyliner_250P(cls):
        return cls.from_database(cls._DATABASE["Sky_Watcher_Skyliner_250P"])

    @classmethod
    def Sky_Watcher_Skyliner_300P(cls):
        return cls.from_database(cls._DATABASE["Sky_Watcher_Skyliner_300P"])

    @classmethod
    def Sky_Watcher_Skyliner_400P(cls):
        return cls.from_database(cls._DATABASE["Sky_Watcher_Skyliner_400P"])

    @classmethod
    def Sky_Watcher_Heritage_130P(cls):
        return cls.from_database(cls._DATABASE["Sky_Watcher_Heritage_130P"])

    @classmethod
    def Sky_Watcher_Heritage_150P(cls):
        return cls.from_database(cls._DATABASE["Sky_Watcher_Heritage_150P"])

    @classmethod
    def Sky_Watcher_Mak_90(cls):
        return cls.from_database(cls._DATABASE["Sky_Watcher_Mak_90"])

    @classmethod
    def Sky_Watcher_Mak_102(cls):
        return cls.from_database(cls._DATABASE["Sky_Watcher_Mak_102"])

    @classmethod
    def Sky_Watcher_Mak_127(cls):
        return cls.from_database(cls._DATABASE["Sky_Watcher_Mak_127"])

    @classmethod
    def Sky_Watcher_Mak_150(cls):
        return cls.from_database(cls._DATABASE["Sky_Watcher_Mak_150"])

    @classmethod
    def Sky_Watcher_Mak_180(cls):
        return cls.from_database(cls._DATABASE["Sky_Watcher_Mak_180"])

    @classmethod
    def Takahashi_FSQ_85EDP(cls):
        return cls.from_database(cls._DATABASE["Takahashi_FSQ_85EDP"])

    @classmethod
    def Takahashi_FSQ_106ED(cls):
        return cls.from_database(cls._DATABASE["Takahashi_FSQ_106ED"])

    @classmethod
    def Takahashi_FSQ_130ED(cls):
        return cls.from_database(cls._DATABASE["Takahashi_FSQ_130ED"])

    @classmethod
    def Takahashi_FC_76DCU(cls):
        return cls.from_database(cls._DATABASE["Takahashi_FC_76DCU"])

    @classmethod
    def Takahashi_FC_100DC(cls):
        return cls.from_database(cls._DATABASE["Takahashi_FC_100DC"])

    @classmethod
    def Takahashi_FC_100DZ(cls):
        return cls.from_database(cls._DATABASE["Takahashi_FC_100DZ"])

    @classmethod
    def Takahashi_FC_100DF(cls):
        return cls.from_database(cls._DATABASE["Takahashi_FC_100DF"])

    @classmethod
    def Takahashi_FS_60CB(cls):
        return cls.from_database(cls._DATABASE["Takahashi_FS_60CB"])

    @classmethod
    def Takahashi_FS_60Q(cls):
        return cls.from_database(cls._DATABASE["Takahashi_FS_60Q"])

    @classmethod
    def Takahashi_TSA_120(cls):
        return cls.from_database(cls._DATABASE["Takahashi_TSA_120"])

    @classmethod
    def Takahashi_TOA_130NFB(cls):
        return cls.from_database(cls._DATABASE["Takahashi_TOA_130NFB"])

    @classmethod
    def Takahashi_TOA_150(cls):
        return cls.from_database(cls._DATABASE["Takahashi_TOA_150"])

    @classmethod
    def Takahashi_Sky_90(cls):
        return cls.from_database(cls._DATABASE["Takahashi_Sky_90"])

    @classmethod
    def Takahashi_FOA_60(cls):
        return cls.from_database(cls._DATABASE["Takahashi_FOA_60"])

    @classmethod
    def Takahashi_FOA_60Q(cls):
        return cls.from_database(cls._DATABASE["Takahashi_FOA_60Q"])

    @classmethod
    def Takahashi_FS_60CP(cls):
        return cls.from_database(cls._DATABASE["Takahashi_FS_60CP"])

    @classmethod
    def Takahashi_FC_76DS(cls):
        return cls.from_database(cls._DATABASE["Takahashi_FC_76DS"])

    @classmethod
    def Takahashi_FC_76DC(cls):
        return cls.from_database(cls._DATABASE["Takahashi_FC_76DC"])

    @classmethod
    def Takahashi_TSA_102(cls):
        return cls.from_database(cls._DATABASE["Takahashi_TSA_102"])

    @classmethod
    def Takahashi_TOA_130S(cls):
        return cls.from_database(cls._DATABASE["Takahashi_TOA_130S"])

    @classmethod
    def Takahashi_FCT_65(cls):
        return cls.from_database(cls._DATABASE["Takahashi_FCT_65"])

    @classmethod
    def Takahashi_Epsilon_130D(cls):
        return cls.from_database(cls._DATABASE["Takahashi_Epsilon_130D"])

    @classmethod
    def Takahashi_Epsilon_180ED(cls):
        return cls.from_database(cls._DATABASE["Takahashi_Epsilon_180ED"])

    @classmethod
    def Takahashi_Epsilon_200(cls):
        return cls.from_database(cls._DATABASE["Takahashi_Epsilon_200"])

    @classmethod
    def Takahashi_CCA_250(cls):
        return cls.from_database(cls._DATABASE["Takahashi_CCA_250"])

    @classmethod
    def Takahashi_BRC_250(cls):
        return cls.from_database(cls._DATABASE["Takahashi_BRC_250"])

    @classmethod
    def Takahashi_Mewlon_180C(cls):
        return cls.from_database(cls._DATABASE["Takahashi_Mewlon_180C"])

    @classmethod
    def Takahashi_Mewlon_210(cls):
        return cls.from_database(cls._DATABASE["Takahashi_Mewlon_210"])

    @classmethod
    def Takahashi_Mewlon_250CRS(cls):
        return cls.from_database(cls._DATABASE["Takahashi_Mewlon_250CRS"])

    @classmethod
    def Takahashi_Mewlon_300CRS(cls):
        return cls.from_database(cls._DATABASE["Takahashi_Mewlon_300CRS"])

    @classmethod
    def Takahashi_CN_212(cls):
        return cls.from_database(cls._DATABASE["Takahashi_CN_212"])

    @classmethod
    def Takahashi_Mu_300_CRS(cls):
        return cls.from_database(cls._DATABASE["Takahashi_Mu_300_CRS"])

    @classmethod
    def William_Optics_GT71(cls):
        return cls.from_database(cls._DATABASE["William_Optics_GT71"])

    @classmethod
    def William_Optics_GT81(cls):
        return cls.from_database(cls._DATABASE["William_Optics_GT81"])

    @classmethod
    def William_Optics_GT102(cls):
        return cls.from_database(cls._DATABASE["William_Optics_GT102"])

    @classmethod
    def William_Optics_GT153(cls):
        return cls.from_database(cls._DATABASE["William_Optics_GT153"])

    @classmethod
    def William_Optics_RedCat_51(cls):
        return cls.from_database(cls._DATABASE["William_Optics_RedCat_51"])

    @classmethod
    def William_Optics_SpaceCat_51(cls):
        return cls.from_database(cls._DATABASE["William_Optics_SpaceCat_51"])

    @classmethod
    def William_Optics_WhiteCat_51(cls):
        return cls.from_database(cls._DATABASE["William_Optics_WhiteCat_51"])

    @classmethod
    def William_Optics_FluoroStar_91(cls):
        return cls.from_database(cls._DATABASE["William_Optics_FluoroStar_91"])

    @classmethod
    def William_Optics_FluoroStar_132(cls):
        return cls.from_database(cls._DATABASE["William_Optics_FluoroStar_132"])

    @classmethod
    def William_Optics_ZenithStar_61_II(cls):
        return cls.from_database(cls._DATABASE["William_Optics_ZenithStar_61_II"])

    @classmethod
    def William_Optics_ZenithStar_73(cls):
        return cls.from_database(cls._DATABASE["William_Optics_ZenithStar_73"])

    @classmethod
    def William_Optics_ZenithStar_81(cls):
        return cls.from_database(cls._DATABASE["William_Optics_ZenithStar_81"])

    @classmethod
    def William_Optics_ZenithStar_103(cls):
        return cls.from_database(cls._DATABASE["William_Optics_ZenithStar_103"])

    @classmethod
    def William_Optics_Cat_71(cls):
        return cls.from_database(cls._DATABASE["William_Optics_Cat_71"])

    @classmethod
    def William_Optics_Pleiades_68(cls):
        return cls.from_database(cls._DATABASE["William_Optics_Pleiades_68"])

    @classmethod
    def William_Optics_Gran_Turismo_71(cls):
        return cls.from_database(cls._DATABASE["William_Optics_Gran_Turismo_71"])

    @classmethod
    def William_Optics_UniStellar_80(cls):
        return cls.from_database(cls._DATABASE["William_Optics_UniStellar_80"])

    @classmethod
    def Askar_FRA300_Pro(cls):
        return cls.from_database(cls._DATABASE["Askar_FRA300_Pro"])

    @classmethod
    def Askar_FRA400(cls):
        return cls.from_database(cls._DATABASE["Askar_FRA400"])

    @classmethod
    def Askar_FRA500(cls):
        return cls.from_database(cls._DATABASE["Askar_FRA500"])

    @classmethod
    def Askar_FRA600(cls):
        return cls.from_database(cls._DATABASE["Askar_FRA600"])

    @classmethod
    def Askar_103APO(cls):
        return cls.from_database(cls._DATABASE["Askar_103APO"])

    @classmethod
    def Askar_80PHQ(cls):
        return cls.from_database(cls._DATABASE["Askar_80PHQ"])

    @classmethod
    def Askar_65PHQ(cls):
        return cls.from_database(cls._DATABASE["Askar_65PHQ"])

    @classmethod
    def Askar_107PHQ(cls):
        return cls.from_database(cls._DATABASE["Askar_107PHQ"])

    @classmethod
    def Askar_130PHQ(cls):
        return cls.from_database(cls._DATABASE["Askar_130PHQ"])

    @classmethod
    def Askar_151PHQ(cls):
        return cls.from_database(cls._DATABASE["Askar_151PHQ"])

    @classmethod
    def Askar_185APO(cls):
        return cls.from_database(cls._DATABASE["Askar_185APO"])

    @classmethod
    def Askar_V_60Q(cls):
        return cls.from_database(cls._DATABASE["Askar_V_60Q"])

    @classmethod
    def Askar_V_80Q(cls):
        return cls.from_database(cls._DATABASE["Askar_V_80Q"])

    @classmethod
    def Askar_FMA_135(cls):
        return cls.from_database(cls._DATABASE["Askar_FMA_135"])

    @classmethod
    def Askar_FMA_180_Pro(cls):
        return cls.from_database(cls._DATABASE["Askar_FMA_180_Pro"])

    @classmethod
    def Askar_FMA_230(cls):
        return cls.from_database(cls._DATABASE["Askar_FMA_230"])

    @classmethod
    def Askar_200APO(cls):
        return cls.from_database(cls._DATABASE["Askar_200APO"])

    @classmethod
    def Askar_140APO(cls):
        return cls.from_database(cls._DATABASE["Askar_140APO"])

    @classmethod
    def Askar_120APO(cls):
        return cls.from_database(cls._DATABASE["Askar_120APO"])

    @classmethod
    def Askar_ACL200(cls):
        return cls.from_database(cls._DATABASE["Askar_ACL200"])

    @classmethod
    def Sharpstar_61EDPH_II(cls):
        return cls.from_database(cls._DATABASE["Sharpstar_61EDPH_II"])

    @classmethod
    def Sharpstar_76EDPH_II(cls):
        return cls.from_database(cls._DATABASE["Sharpstar_76EDPH_II"])

    @classmethod
    def Sharpstar_94EDPH_II(cls):
        return cls.from_database(cls._DATABASE["Sharpstar_94EDPH_II"])

    @classmethod
    def Sharpstar_140PH(cls):
        return cls.from_database(cls._DATABASE["Sharpstar_140PH"])

    @classmethod
    def Sharpstar_200PH(cls):
        return cls.from_database(cls._DATABASE["Sharpstar_200PH"])

    @classmethod
    def Sharpstar_15028HNT(cls):
        return cls.from_database(cls._DATABASE["Sharpstar_15028HNT"])

    @classmethod
    def Sharpstar_20032HNT(cls):
        return cls.from_database(cls._DATABASE["Sharpstar_20032HNT"])

    @classmethod
    def Sharpstar_25040HNT(cls):
        return cls.from_database(cls._DATABASE["Sharpstar_25040HNT"])

    @classmethod
    def GSO_RC_6(cls):
        return cls.from_database(cls._DATABASE["GSO_RC_6"])

    @classmethod
    def GSO_RC_8(cls):
        return cls.from_database(cls._DATABASE["GSO_RC_8"])

    @classmethod
    def GSO_RC_10(cls):
        return cls.from_database(cls._DATABASE["GSO_RC_10"])

    @classmethod
    def GSO_RC_12(cls):
        return cls.from_database(cls._DATABASE["GSO_RC_12"])

    @classmethod
    def GSO_RC_14(cls):
        return cls.from_database(cls._DATABASE["GSO_RC_14"])

    @classmethod
    def GSO_RC_16(cls):
        return cls.from_database(cls._DATABASE["GSO_RC_16"])

    @classmethod
    def CFF_RC_250_10(cls):
        return cls.from_database(cls._DATABASE["CFF_RC_250_10"])

    @classmethod
    def CFF_RC_300_12(cls):
        return cls.from_database(cls._DATABASE["CFF_RC_300_12"])

    @classmethod
    def TPO_RC_6(cls):
        return cls.from_database(cls._DATABASE["TPO_RC_6"])

    @classmethod
    def TPO_RC_8(cls):
        return cls.from_database(cls._DATABASE["TPO_RC_8"])

    @classmethod
    def TPO_RC_10(cls):
        return cls.from_database(cls._DATABASE["TPO_RC_10"])

    @classmethod
    def TS_Optics_Photoline_72mm_APO(cls):
        return cls.from_database(cls._DATABASE["TS_Optics_Photoline_72mm_APO"])

    @classmethod
    def TS_Optics_Photoline_80mm_APO(cls):
        return cls.from_database(cls._DATABASE["TS_Optics_Photoline_80mm_APO"])

    @classmethod
    def TS_Optics_Photoline_100mm_APO(cls):
        return cls.from_database(cls._DATABASE["TS_Optics_Photoline_100mm_APO"])

    @classmethod
    def TS_Optics_Photoline_115mm_APO(cls):
        return cls.from_database(cls._DATABASE["TS_Optics_Photoline_115mm_APO"])

    @classmethod
    def TS_Optics_Photoline_130mm_APO(cls):
        return cls.from_database(cls._DATABASE["TS_Optics_Photoline_130mm_APO"])

    @classmethod
    def TS_Optics_ONTC_6_f_4_Newton(cls):
        return cls.from_database(cls._DATABASE["TS_Optics_ONTC_6_f_4_Newton"])

    @classmethod
    def TS_Optics_ONTC_8_f_4_Newton(cls):
        return cls.from_database(cls._DATABASE["TS_Optics_ONTC_8_f_4_Newton"])

    @classmethod
    def TS_Optics_ONTC_10_f_4_Newton(cls):
        return cls.from_database(cls._DATABASE["TS_Optics_ONTC_10_f_4_Newton"])

    @classmethod
    def TS_Optics_Ritchey_Chretien_6(cls):
        return cls.from_database(cls._DATABASE["TS_Optics_Ritchey_Chretien_6"])

    @classmethod
    def TS_Optics_Ritchey_Chretien_8(cls):
        return cls.from_database(cls._DATABASE["TS_Optics_Ritchey_Chretien_8"])

    @classmethod
    def TS_Optics_Ritchey_Chretien_10(cls):
        return cls.from_database(cls._DATABASE["TS_Optics_Ritchey_Chretien_10"])

    @classmethod
    def TS_Optics_Ritchey_Chretien_12(cls):
        return cls.from_database(cls._DATABASE["TS_Optics_Ritchey_Chretien_12"])

    @classmethod
    def TS_Optics_PHOTON_6_f_9_Mak_Cass(cls):
        return cls.from_database(cls._DATABASE["TS_Optics_PHOTON_6_f_9_Mak_Cass"])

    @classmethod
    def TS_Optics_CF_APO_80mm(cls):
        return cls.from_database(cls._DATABASE["TS_Optics_CF_APO_80mm"])

    @classmethod
    def TS_Optics_CF_APO_102mm(cls):
        return cls.from_database(cls._DATABASE["TS_Optics_CF_APO_102mm"])

    @classmethod
    def TS_Optics_CF_APO_130mm(cls):
        return cls.from_database(cls._DATABASE["TS_Optics_CF_APO_130mm"])

    @classmethod
    def TS_Optics_CF_APO_152mm(cls):
        return cls.from_database(cls._DATABASE["TS_Optics_CF_APO_152mm"])

    @classmethod
    def TS_Optics_Individual_65mm_Quad(cls):
        return cls.from_database(cls._DATABASE["TS_Optics_Individual_65mm_Quad"])

    @classmethod
    def Explore_Scientific_ED80_FCD100(cls):
        return cls.from_database(cls._DATABASE["Explore_Scientific_ED80_FCD100"])

    @classmethod
    def Explore_Scientific_ED102_FCD100(cls):
        return cls.from_database(cls._DATABASE["Explore_Scientific_ED102_FCD100"])

    @classmethod
    def Explore_Scientific_ED127_FCD100(cls):
        return cls.from_database(cls._DATABASE["Explore_Scientific_ED127_FCD100"])

    @classmethod
    def Explore_Scientific_ED152_FCD100(cls):
        return cls.from_database(cls._DATABASE["Explore_Scientific_ED152_FCD100"])

    @classmethod
    def Explore_Scientific_ED80_Essential(cls):
        return cls.from_database(cls._DATABASE["Explore_Scientific_ED80_Essential"])

    @classmethod
    def Explore_Scientific_ED102_Essential(cls):
        return cls.from_database(cls._DATABASE["Explore_Scientific_ED102_Essential"])

    @classmethod
    def Explore_Scientific_ED127_Essential(cls):
        return cls.from_database(cls._DATABASE["Explore_Scientific_ED127_Essential"])

    @classmethod
    def Explore_Scientific_FCD1_80(cls):
        return cls.from_database(cls._DATABASE["Explore_Scientific_FCD1_80"])

    @classmethod
    def Explore_Scientific_FCD1_102(cls):
        return cls.from_database(cls._DATABASE["Explore_Scientific_FCD1_102"])

    @classmethod
    def Explore_Scientific_FCD100_127_Triplet(cls):
        return cls.from_database(cls._DATABASE["Explore_Scientific_FCD100_127_Triplet"])

    @classmethod
    def Explore_Scientific_DAR152065_6_f_5_Newton(cls):
        return cls.from_database(
            cls._DATABASE["Explore_Scientific_DAR152065_6_f_5_Newton"]
        )

    @classmethod
    def Explore_Scientific_DAR20010001_8_f_5_Newton(cls):
        return cls.from_database(
            cls._DATABASE["Explore_Scientific_DAR20010001_8_f_5_Newton"]
        )

    @classmethod
    def Explore_Scientific_Truss_Dob_10(cls):
        return cls.from_database(cls._DATABASE["Explore_Scientific_Truss_Dob_10"])

    @classmethod
    def Explore_Scientific_Truss_Dob_12(cls):
        return cls.from_database(cls._DATABASE["Explore_Scientific_Truss_Dob_12"])

    @classmethod
    def Explore_Scientific_Truss_Dob_16(cls):
        return cls.from_database(cls._DATABASE["Explore_Scientific_Truss_Dob_16"])

    @classmethod
    def Explore_Scientific_305mm_f_5_Newton(cls):
        return cls.from_database(cls._DATABASE["Explore_Scientific_305mm_f_5_Newton"])

    @classmethod
    def Meade_LX85_ACF_6(cls):
        return cls.from_database(cls._DATABASE["Meade_LX85_ACF_6"])

    @classmethod
    def Meade_LX85_ACF_8(cls):
        return cls.from_database(cls._DATABASE["Meade_LX85_ACF_8"])

    @classmethod
    def Meade_LX200_ACF_8(cls):
        return cls.from_database(cls._DATABASE["Meade_LX200_ACF_8"])

    @classmethod
    def Meade_LX200_ACF_10(cls):
        return cls.from_database(cls._DATABASE["Meade_LX200_ACF_10"])

    @classmethod
    def Meade_LX200_ACF_12(cls):
        return cls.from_database(cls._DATABASE["Meade_LX200_ACF_12"])

    @classmethod
    def Meade_LX200_ACF_14(cls):
        return cls.from_database(cls._DATABASE["Meade_LX200_ACF_14"])

    @classmethod
    def Meade_LX200_ACF_16(cls):
        return cls.from_database(cls._DATABASE["Meade_LX200_ACF_16"])

    @classmethod
    def Meade_LX600_ACF_10(cls):
        return cls.from_database(cls._DATABASE["Meade_LX600_ACF_10"])

    @classmethod
    def Meade_LX600_ACF_12(cls):
        return cls.from_database(cls._DATABASE["Meade_LX600_ACF_12"])

    @classmethod
    def Meade_LX600_ACF_14(cls):
        return cls.from_database(cls._DATABASE["Meade_LX600_ACF_14"])

    @classmethod
    def Meade_ETX_90(cls):
        return cls.from_database(cls._DATABASE["Meade_ETX_90"])

    @classmethod
    def Meade_ETX_125(cls):
        return cls.from_database(cls._DATABASE["Meade_ETX_125"])

    @classmethod
    def Vixen_VC200L(cls):
        return cls.from_database(cls._DATABASE["Vixen_VC200L"])

    @classmethod
    def Vixen_VSD100_F3_8(cls):
        return cls.from_database(cls._DATABASE["Vixen_VSD100_F3_8"])

    @classmethod
    def Vixen_VSD90SS(cls):
        return cls.from_database(cls._DATABASE["Vixen_VSD90SS"])

    @classmethod
    def Vixen_A80Mf(cls):
        return cls.from_database(cls._DATABASE["Vixen_A80Mf"])

    @classmethod
    def Vixen_A80M(cls):
        return cls.from_database(cls._DATABASE["Vixen_A80M"])

    @classmethod
    def Vixen_SD81S(cls):
        return cls.from_database(cls._DATABASE["Vixen_SD81S"])

    @classmethod
    def Vixen_SD103S(cls):
        return cls.from_database(cls._DATABASE["Vixen_SD103S"])

    @classmethod
    def Vixen_SD115S(cls):
        return cls.from_database(cls._DATABASE["Vixen_SD115S"])

    @classmethod
    def Vixen_AX103S(cls):
        return cls.from_database(cls._DATABASE["Vixen_AX103S"])

    @classmethod
    def Vixen_FL55SS(cls):
        return cls.from_database(cls._DATABASE["Vixen_FL55SS"])

    @classmethod
    def Vixen_R200SS(cls):
        return cls.from_database(cls._DATABASE["Vixen_R200SS"])

    @classmethod
    def Vixen_VMC200L(cls):
        return cls.from_database(cls._DATABASE["Vixen_VMC200L"])

    @classmethod
    def PlaneWave_CDK12_5(cls):
        return cls.from_database(cls._DATABASE["PlaneWave_CDK12_5"])

    @classmethod
    def PlaneWave_CDK14(cls):
        return cls.from_database(cls._DATABASE["PlaneWave_CDK14"])

    @classmethod
    def PlaneWave_CDK17(cls):
        return cls.from_database(cls._DATABASE["PlaneWave_CDK17"])

    @classmethod
    def PlaneWave_CDK20(cls):
        return cls.from_database(cls._DATABASE["PlaneWave_CDK20"])

    @classmethod
    def PlaneWave_CDK24(cls):
        return cls.from_database(cls._DATABASE["PlaneWave_CDK24"])

    @classmethod
    def Officina_Stellare_RH200(cls):
        return cls.from_database(cls._DATABASE["Officina_Stellare_RH200"])

    @classmethod
    def Officina_Stellare_RH300(cls):
        return cls.from_database(cls._DATABASE["Officina_Stellare_RH300"])

    @classmethod
    def Officina_Stellare_RiDK_250(cls):
        return cls.from_database(cls._DATABASE["Officina_Stellare_RiDK_250"])

    @classmethod
    def Officina_Stellare_RiDK_300(cls):
        return cls.from_database(cls._DATABASE["Officina_Stellare_RiDK_300"])

    @classmethod
    def Officina_Stellare_RiDK_400(cls):
        return cls.from_database(cls._DATABASE["Officina_Stellare_RiDK_400"])

    @classmethod
    def Officina_Stellare_Ultra_CRC_250(cls):
        return cls.from_database(cls._DATABASE["Officina_Stellare_Ultra_CRC_250"])

    @classmethod
    def Officina_Stellare_Ultra_CRC_300(cls):
        return cls.from_database(cls._DATABASE["Officina_Stellare_Ultra_CRC_300"])

    @classmethod
    def Astro_Physics_130GTX(cls):
        return cls.from_database(cls._DATABASE["Astro_Physics_130GTX"])

    @classmethod
    def Astro_Physics_Stowaway_92mm(cls):
        return cls.from_database(cls._DATABASE["Astro_Physics_Stowaway_92mm"])

    @classmethod
    def Astro_Physics_Traveler_105mm(cls):
        return cls.from_database(cls._DATABASE["Astro_Physics_Traveler_105mm"])

    @classmethod
    def Astro_Physics_StarFire_130_EDF(cls):
        return cls.from_database(cls._DATABASE["Astro_Physics_StarFire_130_EDF"])

    @classmethod
    def Astro_Physics_StarFire_155_EDF(cls):
        return cls.from_database(cls._DATABASE["Astro_Physics_StarFire_155_EDF"])

    @classmethod
    def Astro_Physics_StarFire_175_EDF(cls):
        return cls.from_database(cls._DATABASE["Astro_Physics_StarFire_175_EDF"])

    @classmethod
    def Astro_Physics_AP_92(cls):
        return cls.from_database(cls._DATABASE["Astro_Physics_AP_92"])

    @classmethod
    def Stellarvue_SVX080T(cls):
        return cls.from_database(cls._DATABASE["Stellarvue_SVX080T"])

    @classmethod
    def Stellarvue_SVX102T(cls):
        return cls.from_database(cls._DATABASE["Stellarvue_SVX102T"])

    @classmethod
    def Stellarvue_SVX102T_R(cls):
        return cls.from_database(cls._DATABASE["Stellarvue_SVX102T_R"])

    @classmethod
    def Stellarvue_SVX130T(cls):
        return cls.from_database(cls._DATABASE["Stellarvue_SVX130T"])

    @classmethod
    def Stellarvue_SVX152T(cls):
        return cls.from_database(cls._DATABASE["Stellarvue_SVX152T"])

    @classmethod
    def Stellarvue_SV60EDS(cls):
        return cls.from_database(cls._DATABASE["Stellarvue_SV60EDS"])

    @classmethod
    def Stellarvue_SV70T(cls):
        return cls.from_database(cls._DATABASE["Stellarvue_SV70T"])

    @classmethod
    def Stellarvue_SVX80T_IS(cls):
        return cls.from_database(cls._DATABASE["Stellarvue_SVX80T_IS"])

    @classmethod
    def Stellarvue_SVX090T(cls):
        return cls.from_database(cls._DATABASE["Stellarvue_SVX090T"])

    @classmethod
    def Stellarvue_Access_80(cls):
        return cls.from_database(cls._DATABASE["Stellarvue_Access_80"])

    @classmethod
    def Stellarvue_Access_102(cls):
        return cls.from_database(cls._DATABASE["Stellarvue_Access_102"])

    @classmethod
    def TEC_TEC_110_FL(cls):
        return cls.from_database(cls._DATABASE["TEC_TEC_110_FL"])

    @classmethod
    def TEC_TEC_140_FL(cls):
        return cls.from_database(cls._DATABASE["TEC_TEC_140_FL"])

    @classmethod
    def TEC_TEC_160_FL(cls):
        return cls.from_database(cls._DATABASE["TEC_TEC_160_FL"])

    @classmethod
    def TEC_TEC_180_FL(cls):
        return cls.from_database(cls._DATABASE["TEC_TEC_180_FL"])

    @classmethod
    def TEC_TEC_200_FL(cls):
        return cls.from_database(cls._DATABASE["TEC_TEC_200_FL"])

    @classmethod
    def Borg_55FL(cls):
        return cls.from_database(cls._DATABASE["Borg_55FL"])

    @classmethod
    def Borg_71FL(cls):
        return cls.from_database(cls._DATABASE["Borg_71FL"])

    @classmethod
    def Borg_89ED(cls):
        return cls.from_database(cls._DATABASE["Borg_89ED"])

    @classmethod
    def Borg_107FL(cls):
        return cls.from_database(cls._DATABASE["Borg_107FL"])

    @classmethod
    def Borg_90FL(cls):
        return cls.from_database(cls._DATABASE["Borg_90FL"])

    @classmethod
    def Borg_77EDII(cls):
        return cls.from_database(cls._DATABASE["Borg_77EDII"])

    @classmethod
    def APM_LZOS_130_780(cls):
        return cls.from_database(cls._DATABASE["APM_LZOS_130_780"])

    @classmethod
    def APM_LZOS_115_805(cls):
        return cls.from_database(cls._DATABASE["APM_LZOS_115_805"])

    @classmethod
    def APM_LZOS_152_1200(cls):
        return cls.from_database(cls._DATABASE["APM_LZOS_152_1200"])

    @classmethod
    def APM_LZOS_175_1400(cls):
        return cls.from_database(cls._DATABASE["APM_LZOS_175_1400"])

    @classmethod
    def APM_TMB_80_480(cls):
        return cls.from_database(cls._DATABASE["APM_TMB_80_480"])

    @classmethod
    def APM_TMB_105_650(cls):
        return cls.from_database(cls._DATABASE["APM_TMB_105_650"])

    @classmethod
    def APM_TMB_130_780(cls):
        return cls.from_database(cls._DATABASE["APM_TMB_130_780"])

    @classmethod
    def Orion_EON_130mm_ED(cls):
        return cls.from_database(cls._DATABASE["Orion_EON_130mm_ED"])

    @classmethod
    def Orion_8_f_3_9_Astrograph(cls):
        return cls.from_database(cls._DATABASE["Orion_8_f_3_9_Astrograph"])

    @classmethod
    def Orion_EON_110mm_ED(cls):
        return cls.from_database(cls._DATABASE["Orion_EON_110mm_ED"])

    @classmethod
    def Orion_EON_80mm_ED(cls):
        return cls.from_database(cls._DATABASE["Orion_EON_80mm_ED"])

    @classmethod
    def Orion_XT8_Classic_Dob(cls):
        return cls.from_database(cls._DATABASE["Orion_XT8_Classic_Dob"])

    @classmethod
    def Orion_XT10_Classic_Dob(cls):
        return cls.from_database(cls._DATABASE["Orion_XT10_Classic_Dob"])

    @classmethod
    def Orion_XT12_Classic_Dob(cls):
        return cls.from_database(cls._DATABASE["Orion_XT12_Classic_Dob"])

    @classmethod
    def Orion_SkyQuest_XX12_Dob(cls):
        return cls.from_database(cls._DATABASE["Orion_SkyQuest_XX12_Dob"])

    @classmethod
    def Orion_SkyQuest_XX14_Dob(cls):
        return cls.from_database(cls._DATABASE["Orion_SkyQuest_XX14_Dob"])

    @classmethod
    def Orion_SpaceProbe_130ST(cls):
        return cls.from_database(cls._DATABASE["Orion_SpaceProbe_130ST"])

    @classmethod
    def Bresser_Messier_AR_102xs(cls):
        return cls.from_database(cls._DATABASE["Bresser_Messier_AR_102xs"])

    @classmethod
    def Bresser_Messier_AR_127L(cls):
        return cls.from_database(cls._DATABASE["Bresser_Messier_AR_127L"])

    @classmethod
    def Bresser_Messier_AR_152L(cls):
        return cls.from_database(cls._DATABASE["Bresser_Messier_AR_152L"])

    @classmethod
    def Bresser_Messier_MC_127(cls):
        return cls.from_database(cls._DATABASE["Bresser_Messier_MC_127"])

    @classmethod
    def Bresser_Messier_MC_152(cls):
        return cls.from_database(cls._DATABASE["Bresser_Messier_MC_152"])

    @classmethod
    def Bresser_Messier_NT_150L_6(cls):
        return cls.from_database(cls._DATABASE["Bresser_Messier_NT_150L_6"])

    @classmethod
    def Bresser_Messier_NT_203_8(cls):
        return cls.from_database(cls._DATABASE["Bresser_Messier_NT_203_8"])

    @classmethod
    def Bresser_Messier_NT_254_10(cls):
        return cls.from_database(cls._DATABASE["Bresser_Messier_NT_254_10"])

    @classmethod
    def Bresser_Messier_AR_80(cls):
        return cls.from_database(cls._DATABASE["Bresser_Messier_AR_80"])

    @classmethod
    def Bresser_Messier_AR_90(cls):
        return cls.from_database(cls._DATABASE["Bresser_Messier_AR_90"])

    @classmethod
    def Lacerta_Newton_200_800(cls):
        return cls.from_database(cls._DATABASE["Lacerta_Newton_200_800"])

    @classmethod
    def Lacerta_Newton_250_1000(cls):
        return cls.from_database(cls._DATABASE["Lacerta_Newton_250_1000"])

    @classmethod
    def Lacerta_Newton_200_1000(cls):
        return cls.from_database(cls._DATABASE["Lacerta_Newton_200_1000"])

    @classmethod
    def Lacerta_Newton_300_1200(cls):
        return cls.from_database(cls._DATABASE["Lacerta_Newton_300_1200"])

    @classmethod
    def Omegon_ProED_80(cls):
        return cls.from_database(cls._DATABASE["Omegon_ProED_80"])

    @classmethod
    def Omegon_ProED_100(cls):
        return cls.from_database(cls._DATABASE["Omegon_ProED_100"])

    @classmethod
    def Omegon_ProED_110(cls):
        return cls.from_database(cls._DATABASE["Omegon_ProED_110"])

    @classmethod
    def Omegon_N_200_800(cls):
        return cls.from_database(cls._DATABASE["Omegon_N_200_800"])

    @classmethod
    def Omegon_N_250_1000(cls):
        return cls.from_database(cls._DATABASE["Omegon_N_250_1000"])

    @classmethod
    def Omegon_Pro_APO_94(cls):
        return cls.from_database(cls._DATABASE["Omegon_Pro_APO_94"])

    @classmethod
    def Omegon_Pro_APO_121(cls):
        return cls.from_database(cls._DATABASE["Omegon_Pro_APO_121"])

    @classmethod
    def Omegon_Pro_APO_152(cls):
        return cls.from_database(cls._DATABASE["Omegon_Pro_APO_152"])

    @classmethod
    def Sigma_135mm_f_2_Art(cls):
        return cls.from_database(cls._DATABASE["Sigma_135mm_f_2_Art"])

    @classmethod
    def Sigma_105mm_f_1_4_Art(cls):
        return cls.from_database(cls._DATABASE["Sigma_105mm_f_1_4_Art"])

    @classmethod
    def Sigma_150_600mm_f_5_6_3_DG(cls):
        return cls.from_database(cls._DATABASE["Sigma_150_600mm_f_5_6_3_DG"])

    @classmethod
    def Sigma_14mm_f_1_8_Art(cls):
        return cls.from_database(cls._DATABASE["Sigma_14mm_f_1_8_Art"])

    @classmethod
    def Samyang_Rokinon_135mm_f_2_0_ED_UMC(cls):
        return cls.from_database(cls._DATABASE["Samyang_Rokinon_135mm_f_2_0_ED_UMC"])

    @classmethod
    def Samyang_Rokinon_85mm_f_1_4_UMC(cls):
        return cls.from_database(cls._DATABASE["Samyang_Rokinon_85mm_f_1_4_UMC"])

    @classmethod
    def Samyang_Rokinon_14mm_f_2_8_ED_UMC(cls):
        return cls.from_database(cls._DATABASE["Samyang_Rokinon_14mm_f_2_8_ED_UMC"])

    @classmethod
    def Samyang_Rokinon_24mm_f_1_4_ED_UMC(cls):
        return cls.from_database(cls._DATABASE["Samyang_Rokinon_24mm_f_1_4_ED_UMC"])

    @classmethod
    def Samyang_Rokinon_135mm_f_2_0_Canon_RF(cls):
        return cls.from_database(cls._DATABASE["Samyang_Rokinon_135mm_f_2_0_Canon_RF"])

    @classmethod
    def Samyang_Rokinon_135mm_f_2_0_Sony_E(cls):
        return cls.from_database(cls._DATABASE["Samyang_Rokinon_135mm_f_2_0_Sony_E"])

    @classmethod
    def Samyang_Rokinon_135mm_f_2_0_Nikon_Z(cls):
        return cls.from_database(cls._DATABASE["Samyang_Rokinon_135mm_f_2_0_Nikon_Z"])

    @classmethod
    def SVBony_SV503_70ED(cls):
        return cls.from_database(cls._DATABASE["SVBony_SV503_70ED"])

    @classmethod
    def SVBony_SV503_80ED(cls):
        return cls.from_database(cls._DATABASE["SVBony_SV503_80ED"])

    @classmethod
    def SVBony_SV503_102ED(cls):
        return cls.from_database(cls._DATABASE["SVBony_SV503_102ED"])

    @classmethod
    def SVBony_SV550_80ED(cls):
        return cls.from_database(cls._DATABASE["SVBony_SV550_80ED"])

    @classmethod
    def SVBony_SV550_122ED(cls):
        return cls.from_database(cls._DATABASE["SVBony_SV550_122ED"])

    @classmethod
    def SVBony_SV48(cls):
        return cls.from_database(cls._DATABASE["SVBony_SV48"])

    @classmethod
    def SVBony_SV503_80(cls):
        return cls.from_database(cls._DATABASE["SVBony_SV503_80"])

    @classmethod
    def iOptron_iOptron_RC_6(cls):
        return cls.from_database(cls._DATABASE["iOptron_iOptron_RC_6"])

    @classmethod
    def iOptron_iOptron_RC_8(cls):
        return cls.from_database(cls._DATABASE["iOptron_iOptron_RC_8"])

    @classmethod
    def iOptron_iOptron_80mm_APO(cls):
        return cls.from_database(cls._DATABASE["iOptron_iOptron_80mm_APO"])

    @classmethod
    def iOptron_iOptron_102mm_APO(cls):
        return cls.from_database(cls._DATABASE["iOptron_iOptron_102mm_APO"])

    @classmethod
    def Saxon_Saxon_72ED(cls):
        return cls.from_database(cls._DATABASE["Saxon_Saxon_72ED"])

    @classmethod
    def Saxon_Saxon_80ED(cls):
        return cls.from_database(cls._DATABASE["Saxon_Saxon_80ED"])

    @classmethod
    def Saxon_Saxon_102ED(cls):
        return cls.from_database(cls._DATABASE["Saxon_Saxon_102ED"])

    @classmethod
    def Saxon_Saxon_127_Mak(cls):
        return cls.from_database(cls._DATABASE["Saxon_Saxon_127_Mak"])

    @classmethod
    def Saxon_Saxon_150_Mak(cls):
        return cls.from_database(cls._DATABASE["Saxon_Saxon_150_Mak"])

    @classmethod
    def Saxon_Saxon_200P_Dob(cls):
        return cls.from_database(cls._DATABASE["Saxon_Saxon_200P_Dob"])

    @classmethod
    def Saxon_Saxon_250P_Dob(cls):
        return cls.from_database(cls._DATABASE["Saxon_Saxon_250P_Dob"])

    @classmethod
    def Tecnosky_Tecnosky_60_360_APO(cls):
        return cls.from_database(cls._DATABASE["Tecnosky_Tecnosky_60_360_APO"])

    @classmethod
    def Tecnosky_Tecnosky_80_480_APO(cls):
        return cls.from_database(cls._DATABASE["Tecnosky_Tecnosky_80_480_APO"])

    @classmethod
    def Tecnosky_Tecnosky_102_714_APO(cls):
        return cls.from_database(cls._DATABASE["Tecnosky_Tecnosky_102_714_APO"])

    @classmethod
    def Tecnosky_Tecnosky_130_910_APO(cls):
        return cls.from_database(cls._DATABASE["Tecnosky_Tecnosky_130_910_APO"])

    @classmethod
    def Tecnosky_Tecnosky_RC_6(cls):
        return cls.from_database(cls._DATABASE["Tecnosky_Tecnosky_RC_6"])

    @classmethod
    def Tecnosky_Tecnosky_RC_8(cls):
        return cls.from_database(cls._DATABASE["Tecnosky_Tecnosky_RC_8"])

    @classmethod
    def Tecnosky_Tecnosky_RC_10(cls):
        return cls.from_database(cls._DATABASE["Tecnosky_Tecnosky_RC_10"])

    @classmethod
    def Tecnosky_Tecnosky_RC_12(cls):
        return cls.from_database(cls._DATABASE["Tecnosky_Tecnosky_RC_12"])

    @classmethod
    def KUO_KUO_80_480_APO(cls):
        return cls.from_database(cls._DATABASE["KUO_KUO_80_480_APO"])

    @classmethod
    def KUO_KUO_102_714_APO(cls):
        return cls.from_database(cls._DATABASE["KUO_KUO_102_714_APO"])

    @classmethod
    def KUO_KUO_130_910_APO(cls):
        return cls.from_database(cls._DATABASE["KUO_KUO_130_910_APO"])

    @classmethod
    def KUO_KUO_152_1200_APO(cls):
        return cls.from_database(cls._DATABASE["KUO_KUO_152_1200_APO"])

    @classmethod
    def Long_Perng_LP_66_400_APO(cls):
        return cls.from_database(cls._DATABASE["Long_Perng_LP_66_400_APO"])

    @classmethod
    def Long_Perng_LP_80_480_APO(cls):
        return cls.from_database(cls._DATABASE["Long_Perng_LP_80_480_APO"])

    @classmethod
    def Long_Perng_LP_90_500_APO(cls):
        return cls.from_database(cls._DATABASE["Long_Perng_LP_90_500_APO"])

    @classmethod
    def Long_Perng_LP_110_660_APO(cls):
        return cls.from_database(cls._DATABASE["Long_Perng_LP_110_660_APO"])

    @classmethod
    def Long_Perng_LP_127_952_APO(cls):
        return cls.from_database(cls._DATABASE["Long_Perng_LP_127_952_APO"])

    @classmethod
    def Takahashi_FSQ_85EDX4(cls):
        return cls.from_database(cls._DATABASE["Takahashi_FSQ_85EDX4"])

    @classmethod
    def Takahashi_FSQ_106EDX4(cls):
        return cls.from_database(cls._DATABASE["Takahashi_FSQ_106EDX4"])

    @classmethod
    def William_Optics_Saddle_Cat_51(cls):
        return cls.from_database(cls._DATABASE["William_Optics_Saddle_Cat_51"])

    @classmethod
    def William_Optics_Redcat_71(cls):
        return cls.from_database(cls._DATABASE["William_Optics_Redcat_71"])

    @classmethod
    def William_Optics_GT131(cls):
        return cls.from_database(cls._DATABASE["William_Optics_GT131"])

    @classmethod
    def Askar_FMA_80(cls):
        return cls.from_database(cls._DATABASE["Askar_FMA_80"])

    @classmethod
    def Askar_FMA_107APO(cls):
        return cls.from_database(cls._DATABASE["Askar_FMA_107APO"])

    @classmethod
    def Askar_ACL130(cls):
        return cls.from_database(cls._DATABASE["Askar_ACL130"])

    @classmethod
    def Askar_V_40Q(cls):
        return cls.from_database(cls._DATABASE["Askar_V_40Q"])

    @classmethod
    def Askar_72Q(cls):
        return cls.from_database(cls._DATABASE["Askar_72Q"])

    @classmethod
    def Celestron_StarSense_Explorer_LT_114(cls):
        return cls.from_database(cls._DATABASE["Celestron_StarSense_Explorer_LT_114"])

    @classmethod
    def Celestron_StarSense_Explorer_DX_130(cls):
        return cls.from_database(cls._DATABASE["Celestron_StarSense_Explorer_DX_130"])

    @classmethod
    def Celestron_Inspire_100AZ(cls):
        return cls.from_database(cls._DATABASE["Celestron_Inspire_100AZ"])

    @classmethod
    def Celestron_AstroMaster_130EQ(cls):
        return cls.from_database(cls._DATABASE["Celestron_AstroMaster_130EQ"])

    @classmethod
    def Bresser_Messier_MC_100(cls):
        return cls.from_database(cls._DATABASE["Bresser_Messier_MC_100"])

    @classmethod
    def Bresser_Messier_NT_130(cls):
        return cls.from_database(cls._DATABASE["Bresser_Messier_NT_130"])

    @classmethod
    def Bresser_Arcturus_60_700_AZ(cls):
        return cls.from_database(cls._DATABASE["Bresser_Arcturus_60_700_AZ"])

    @classmethod
    def Bresser_Pollux_150_1400(cls):
        return cls.from_database(cls._DATABASE["Bresser_Pollux_150_1400"])

    @classmethod
    def Bresser_Bresser_Spica_130_1000(cls):
        return cls.from_database(cls._DATABASE["Bresser_Bresser_Spica_130_1000"])

    @classmethod
    def Bresser_Messier_AR_102L(cls):
        return cls.from_database(cls._DATABASE["Bresser_Messier_AR_102L"])

    @classmethod
    def National_Geographic_Nat_Geo_76_700_Newton(cls):
        return cls.from_database(
            cls._DATABASE["National_Geographic_Nat_Geo_76_700_Newton"]
        )

    @classmethod
    def National_Geographic_Nat_Geo_114_900_Newton(cls):
        return cls.from_database(
            cls._DATABASE["National_Geographic_Nat_Geo_114_900_Newton"]
        )

    @classmethod
    def National_Geographic_Nat_Geo_130_650_Newton(cls):
        return cls.from_database(
            cls._DATABASE["National_Geographic_Nat_Geo_130_650_Newton"]
        )

    @classmethod
    def Canon_EF_200mm_f_2_8L_II(cls):
        return cls.from_database(cls._DATABASE["Canon_EF_200mm_f_2_8L_II"])

    @classmethod
    def Canon_EF_135mm_f_2L(cls):
        return cls.from_database(cls._DATABASE["Canon_EF_135mm_f_2L"])

    @classmethod
    def Canon_EF_100mm_f_2_8L_Macro_IS(cls):
        return cls.from_database(cls._DATABASE["Canon_EF_100mm_f_2_8L_Macro_IS"])

    @classmethod
    def Canon_EF_50mm_f_1_4(cls):
        return cls.from_database(cls._DATABASE["Canon_EF_50mm_f_1_4"])

    @classmethod
    def Canon_EF_50mm_f_1_8_STM(cls):
        return cls.from_database(cls._DATABASE["Canon_EF_50mm_f_1_8_STM"])

    @classmethod
    def Canon_EF_85mm_f_1_8(cls):
        return cls.from_database(cls._DATABASE["Canon_EF_85mm_f_1_8"])

    @classmethod
    def Canon_EF_24_70mm_f_2_8L_II(cls):
        return cls.from_database(cls._DATABASE["Canon_EF_24_70mm_f_2_8L_II"])

    @classmethod
    def Canon_EF_70_200mm_f_2_8L_IS_III(cls):
        return cls.from_database(cls._DATABASE["Canon_EF_70_200mm_f_2_8L_IS_III"])

    @classmethod
    def Canon_EF_400mm_f_5_6L(cls):
        return cls.from_database(cls._DATABASE["Canon_EF_400mm_f_5_6L"])

    @classmethod
    def Canon_EF_300mm_f_4L_IS(cls):
        return cls.from_database(cls._DATABASE["Canon_EF_300mm_f_4L_IS"])

    @classmethod
    def Canon_EF_24mm_f_1_4L_II(cls):
        return cls.from_database(cls._DATABASE["Canon_EF_24mm_f_1_4L_II"])

    @classmethod
    def Canon_RF_200mm_f_2_8(cls):
        return cls.from_database(cls._DATABASE["Canon_RF_200mm_f_2_8"])

    @classmethod
    def Canon_RF_135mm_f_1_8L(cls):
        return cls.from_database(cls._DATABASE["Canon_RF_135mm_f_1_8L"])

    @classmethod
    def Canon_RF_85mm_f_1_2L(cls):
        return cls.from_database(cls._DATABASE["Canon_RF_85mm_f_1_2L"])

    @classmethod
    def Canon_RF_50mm_f_1_8_STM(cls):
        return cls.from_database(cls._DATABASE["Canon_RF_50mm_f_1_8_STM"])

    @classmethod
    def Canon_RF_100_400mm_f_5_6_8(cls):
        return cls.from_database(cls._DATABASE["Canon_RF_100_400mm_f_5_6_8"])

    @classmethod
    def Canon_RF_100mm_f_2_8L_Macro_IS(cls):
        return cls.from_database(cls._DATABASE["Canon_RF_100mm_f_2_8L_Macro_IS"])

    @classmethod
    def Nikon_AF_S_200mm_f_2G_ED_VR(cls):
        return cls.from_database(cls._DATABASE["Nikon_AF_S_200mm_f_2G_ED_VR"])

    @classmethod
    def Nikon_AF_S_105mm_f_1_4E_ED(cls):
        return cls.from_database(cls._DATABASE["Nikon_AF_S_105mm_f_1_4E_ED"])

    @classmethod
    def Nikon_AF_S_50mm_f_1_8G(cls):
        return cls.from_database(cls._DATABASE["Nikon_AF_S_50mm_f_1_8G"])

    @classmethod
    def Nikon_AF_S_85mm_f_1_8G(cls):
        return cls.from_database(cls._DATABASE["Nikon_AF_S_85mm_f_1_8G"])

    @classmethod
    def Nikon_AF_S_300mm_f_4E_PF_ED_VR(cls):
        return cls.from_database(cls._DATABASE["Nikon_AF_S_300mm_f_4E_PF_ED_VR"])

    @classmethod
    def Nikon_AF_S_70_200mm_f_2_8E_FL_ED_VR(cls):
        return cls.from_database(cls._DATABASE["Nikon_AF_S_70_200mm_f_2_8E_FL_ED_VR"])

    @classmethod
    def Nikon_Z_135mm_f_1_8_S_Plena(cls):
        return cls.from_database(cls._DATABASE["Nikon_Z_135mm_f_1_8_S_Plena"])

    @classmethod
    def Nikon_Z_50mm_f_1_8_S(cls):
        return cls.from_database(cls._DATABASE["Nikon_Z_50mm_f_1_8_S"])

    @classmethod
    def Nikon_Z_85mm_f_1_8_S(cls):
        return cls.from_database(cls._DATABASE["Nikon_Z_85mm_f_1_8_S"])

    @classmethod
    def Nikon_Z_200_600mm_f_5_6_6_3_VR(cls):
        return cls.from_database(cls._DATABASE["Nikon_Z_200_600mm_f_5_6_6_3_VR"])

    @classmethod
    def Nikon_Z_100_400mm_f_4_5_5_6_VR_S(cls):
        return cls.from_database(cls._DATABASE["Nikon_Z_100_400mm_f_4_5_5_6_VR_S"])

    @classmethod
    def Sony_FE_135mm_f_1_8_GM(cls):
        return cls.from_database(cls._DATABASE["Sony_FE_135mm_f_1_8_GM"])

    @classmethod
    def Sony_FE_200_600mm_f_5_6_6_3_G(cls):
        return cls.from_database(cls._DATABASE["Sony_FE_200_600mm_f_5_6_6_3_G"])

    @classmethod
    def Sony_FE_85mm_f_1_4_GM(cls):
        return cls.from_database(cls._DATABASE["Sony_FE_85mm_f_1_4_GM"])

    @classmethod
    def Sony_FE_50mm_f_1_4_GM(cls):
        return cls.from_database(cls._DATABASE["Sony_FE_50mm_f_1_4_GM"])

    @classmethod
    def Sony_FE_100_400mm_f_4_5_5_6_GM(cls):
        return cls.from_database(cls._DATABASE["Sony_FE_100_400mm_f_4_5_5_6_GM"])

    @classmethod
    def Sony_FE_70_200mm_f_2_8_GM_II(cls):
        return cls.from_database(cls._DATABASE["Sony_FE_70_200mm_f_2_8_GM_II"])

    @classmethod
    def Tokina_opera_50mm_f_1_4_Canon(cls):
        return cls.from_database(cls._DATABASE["Tokina_opera_50mm_f_1_4_Canon"])

    @classmethod
    def Tokina_opera_50mm_f_1_4_Nikon(cls):
        return cls.from_database(cls._DATABASE["Tokina_opera_50mm_f_1_4_Nikon"])

    @classmethod
    def Tokina_ATX_i_11_16mm_f_2_8_Canon(cls):
        return cls.from_database(cls._DATABASE["Tokina_ATX_i_11_16mm_f_2_8_Canon"])

    @classmethod
    def Tokina_ATX_i_11_16mm_f_2_8_Nikon(cls):
        return cls.from_database(cls._DATABASE["Tokina_ATX_i_11_16mm_f_2_8_Nikon"])

    @classmethod
    def Tokina_SZ_500mm_f_8_Reflex_MF(cls):
        return cls.from_database(cls._DATABASE["Tokina_SZ_500mm_f_8_Reflex_MF"])

    @classmethod
    def Tamron_SP_150_600mm_f_5_6_3_G2_Canon(cls):
        return cls.from_database(cls._DATABASE["Tamron_SP_150_600mm_f_5_6_3_G2_Canon"])

    @classmethod
    def Tamron_SP_150_600mm_f_5_6_3_G2_Nikon(cls):
        return cls.from_database(cls._DATABASE["Tamron_SP_150_600mm_f_5_6_3_G2_Nikon"])

    @classmethod
    def Tamron_100_400mm_f_4_5_6_3_Sony_E(cls):
        return cls.from_database(cls._DATABASE["Tamron_100_400mm_f_4_5_6_3_Sony_E"])

    @classmethod
    def Tamron_150_500mm_f_5_6_7_Sony_E(cls):
        return cls.from_database(cls._DATABASE["Tamron_150_500mm_f_5_6_7_Sony_E"])

    @classmethod
    def Sigma_180mm_f_2_8_APO_Macro_Canon(cls):
        return cls.from_database(cls._DATABASE["Sigma_180mm_f_2_8_APO_Macro_Canon"])

    @classmethod
    def Sigma_180mm_f_2_8_APO_Macro_Nikon(cls):
        return cls.from_database(cls._DATABASE["Sigma_180mm_f_2_8_APO_Macro_Nikon"])

    @classmethod
    def Sigma_500mm_f_4_DG_OS_HSM(cls):
        return cls.from_database(cls._DATABASE["Sigma_500mm_f_4_DG_OS_HSM"])

    @classmethod
    def Sigma_60_600mm_f_4_5_6_3_DG_Canon(cls):
        return cls.from_database(cls._DATABASE["Sigma_60_600mm_f_4_5_6_3_DG_Canon"])

    @classmethod
    def Sigma_100_400mm_f_5_6_3_DG_Canon(cls):
        return cls.from_database(cls._DATABASE["Sigma_100_400mm_f_5_6_3_DG_Canon"])

    @classmethod
    def Sigma_150_600mm_f_5_6_3_DG_Nikon(cls):
        return cls.from_database(cls._DATABASE["Sigma_150_600mm_f_5_6_3_DG_Nikon"])

    @classmethod
    def Sigma_150_600mm_f_5_6_3_Sony_E(cls):
        return cls.from_database(cls._DATABASE["Sigma_150_600mm_f_5_6_3_Sony_E"])

    @classmethod
    def Irix_150mm_f_2_8_Macro_Canon(cls):
        return cls.from_database(cls._DATABASE["Irix_150mm_f_2_8_Macro_Canon"])

    @classmethod
    def Irix_150mm_f_2_8_Macro_Nikon(cls):
        return cls.from_database(cls._DATABASE["Irix_150mm_f_2_8_Macro_Nikon"])

    @classmethod
    def Irix_45mm_f_1_4_Canon(cls):
        return cls.from_database(cls._DATABASE["Irix_45mm_f_1_4_Canon"])

    @classmethod
    def Irix_11mm_f_4_Canon(cls):
        return cls.from_database(cls._DATABASE["Irix_11mm_f_4_Canon"])

    @classmethod
    def Russian_Soviet_Jupiter_37A_135mm_f_3_5(cls):
        return cls.from_database(
            cls._DATABASE["Russian_Soviet_Jupiter_37A_135mm_f_3_5"]
        )

    @classmethod
    def Russian_Soviet_MTO_1000A_1000mm_f_10(cls):
        return cls.from_database(cls._DATABASE["Russian_Soviet_MTO_1000A_1000mm_f_10"])

    @classmethod
    def Russian_Soviet_Helios_44_2_58mm_f_2(cls):
        return cls.from_database(cls._DATABASE["Russian_Soviet_Helios_44_2_58mm_f_2"])

    @classmethod
    def Russian_Soviet_Tair_3S_300mm_f_4_5(cls):
        return cls.from_database(cls._DATABASE["Russian_Soviet_Tair_3S_300mm_f_4_5"])

    @classmethod
    def Sky_Watcher_Heritage_76_Mini(cls):
        return cls.from_database(cls._DATABASE["Sky_Watcher_Heritage_76_Mini"])

    @classmethod
    def Sky_Watcher_Heritage_100P(cls):
        return cls.from_database(cls._DATABASE["Sky_Watcher_Heritage_100P"])

    @classmethod
    def Orion_SkyLine_6_Dob(cls):
        return cls.from_database(cls._DATABASE["Orion_SkyLine_6_Dob"])

    @classmethod
    def Orion_SkyLine_8_Dob(cls):
        return cls.from_database(cls._DATABASE["Orion_SkyLine_8_Dob"])

    @classmethod
    def Orion_SkyLine_10_Dob(cls):
        return cls.from_database(cls._DATABASE["Orion_SkyLine_10_Dob"])

    @classmethod
    def Orion_SkyLine_12_Dob(cls):
        return cls.from_database(cls._DATABASE["Orion_SkyLine_12_Dob"])

    @classmethod
    def Explore_Scientific_Ultra_Light_10(cls):
        return cls.from_database(cls._DATABASE["Explore_Scientific_Ultra_Light_10"])

    @classmethod
    def Explore_Scientific_Ultra_Light_12(cls):
        return cls.from_database(cls._DATABASE["Explore_Scientific_Ultra_Light_12"])

    @classmethod
    def Explore_Scientific_Ultra_Light_16(cls):
        return cls.from_database(cls._DATABASE["Explore_Scientific_Ultra_Light_16"])

    @classmethod
    def Sky_Watcher_Heritage_130P_FlexTube(cls):
        return cls.from_database(cls._DATABASE["Sky_Watcher_Heritage_130P_FlexTube"])

    @classmethod
    def Sky_Watcher_Heritage_150P_FlexTube(cls):
        return cls.from_database(cls._DATABASE["Sky_Watcher_Heritage_150P_FlexTube"])

    @classmethod
    def Sky_Watcher_Star_Discovery_130i(cls):
        return cls.from_database(cls._DATABASE["Sky_Watcher_Star_Discovery_130i"])

    @classmethod
    def Sky_Watcher_Star_Discovery_150i(cls):
        return cls.from_database(cls._DATABASE["Sky_Watcher_Star_Discovery_150i"])

    @classmethod
    def Sky_Watcher_Starquest_130P(cls):
        return cls.from_database(cls._DATABASE["Sky_Watcher_Starquest_130P"])

    @classmethod
    def Sky_Watcher_Virtuoso_GTi_130P(cls):
        return cls.from_database(cls._DATABASE["Sky_Watcher_Virtuoso_GTi_130P"])

    @classmethod
    def Sky_Watcher_Virtuoso_GTi_150P(cls):
        return cls.from_database(cls._DATABASE["Sky_Watcher_Virtuoso_GTi_150P"])

    @classmethod
    def Celestron_Omni_XLT_102(cls):
        return cls.from_database(cls._DATABASE["Celestron_Omni_XLT_102"])

    @classmethod
    def Celestron_Omni_XLT_120(cls):
        return cls.from_database(cls._DATABASE["Celestron_Omni_XLT_120"])

    @classmethod
    def Celestron_Omni_XLT_127_SCT(cls):
        return cls.from_database(cls._DATABASE["Celestron_Omni_XLT_127_SCT"])

    @classmethod
    def Celestron_Omni_XLT_150R(cls):
        return cls.from_database(cls._DATABASE["Celestron_Omni_XLT_150R"])

    @classmethod
    def Celestron_Omni_XLT_150(cls):
        return cls.from_database(cls._DATABASE["Celestron_Omni_XLT_150"])

    @classmethod
    def Celestron_StarBright_XLT_C6_A_XLT(cls):
        return cls.from_database(cls._DATABASE["Celestron_StarBright_XLT_C6_A_XLT"])

    @classmethod
    def Celestron_AstroFi_130(cls):
        return cls.from_database(cls._DATABASE["Celestron_AstroFi_130"])

    @classmethod
    def Celestron_FirstScope_76(cls):
        return cls.from_database(cls._DATABASE["Celestron_FirstScope_76"])

    @classmethod
    def Celestron_PowerSeeker_127EQ(cls):
        return cls.from_database(cls._DATABASE["Celestron_PowerSeeker_127EQ"])

    @classmethod
    def Lunt_Solar_LS60THa_60mm_H_alpha(cls):
        return cls.from_database(cls._DATABASE["Lunt_Solar_LS60THa_60mm_H_alpha"])

    @classmethod
    def Lunt_Solar_LS80THa_80mm_H_alpha(cls):
        return cls.from_database(cls._DATABASE["Lunt_Solar_LS80THa_80mm_H_alpha"])

    @classmethod
    def Lunt_Solar_LS100THa_100mm_H_alpha(cls):
        return cls.from_database(cls._DATABASE["Lunt_Solar_LS100THa_100mm_H_alpha"])

    @classmethod
    def Lunt_Solar_LS130THa_130mm_H_alpha(cls):
        return cls.from_database(cls._DATABASE["Lunt_Solar_LS130THa_130mm_H_alpha"])

    @classmethod
    def Lunt_Solar_LS50THa_50mm_H_alpha(cls):
        return cls.from_database(cls._DATABASE["Lunt_Solar_LS50THa_50mm_H_alpha"])

    @classmethod
    def Coronado_PST_40mm(cls):
        return cls.from_database(cls._DATABASE["Coronado_PST_40mm"])

    @classmethod
    def Coronado_SolarMax_II_60(cls):
        return cls.from_database(cls._DATABASE["Coronado_SolarMax_II_60"])

    @classmethod
    def Coronado_SolarMax_II_90(cls):
        return cls.from_database(cls._DATABASE["Coronado_SolarMax_II_90"])

    @classmethod
    def Coronado_SolarMax_III_70(cls):
        return cls.from_database(cls._DATABASE["Coronado_SolarMax_III_70"])

    @classmethod
    def DayStar_Solar_Scout_60mm(cls):
        return cls.from_database(cls._DATABASE["DayStar_Solar_Scout_60mm"])

    @classmethod
    def DayStar_Solar_Scout_80mm(cls):
        return cls.from_database(cls._DATABASE["DayStar_Solar_Scout_80mm"])

    @classmethod
    def Orion_UK_VX6_6_Newt(cls):
        return cls.from_database(cls._DATABASE["Orion_UK_VX6_6_Newt"])

    @classmethod
    def Orion_UK_VX8_8_Newt(cls):
        return cls.from_database(cls._DATABASE["Orion_UK_VX8_8_Newt"])

    @classmethod
    def Orion_UK_VX10_10_Newt(cls):
        return cls.from_database(cls._DATABASE["Orion_UK_VX10_10_Newt"])

    @classmethod
    def Orion_UK_VX12_12_Newt(cls):
        return cls.from_database(cls._DATABASE["Orion_UK_VX12_12_Newt"])

    @classmethod
    def Orion_UK_Europa_200_f_4(cls):
        return cls.from_database(cls._DATABASE["Orion_UK_Europa_200_f_4"])

    @classmethod
    def Orion_UK_ODK_10(cls):
        return cls.from_database(cls._DATABASE["Orion_UK_ODK_10"])

    @classmethod
    def Orion_UK_ODK_12(cls):
        return cls.from_database(cls._DATABASE["Orion_UK_ODK_12"])

    @classmethod
    def Orion_UK_ODK_14(cls):
        return cls.from_database(cls._DATABASE["Orion_UK_ODK_14"])

    @classmethod
    def Orion_UK_ODK_16(cls):
        return cls.from_database(cls._DATABASE["Orion_UK_ODK_16"])

    @classmethod
    def Orion_UK_AG12_12_AG(cls):
        return cls.from_database(cls._DATABASE["Orion_UK_AG12_12_AG"])

    @classmethod
    def SkyVision_SkyVision_T500_20(cls):
        return cls.from_database(cls._DATABASE["SkyVision_SkyVision_T500_20"])

    @classmethod
    def SkyVision_SkyVision_T600_24(cls):
        return cls.from_database(cls._DATABASE["SkyVision_SkyVision_T600_24"])

    @classmethod
    def SkyVision_SkyVision_T700_28(cls):
        return cls.from_database(cls._DATABASE["SkyVision_SkyVision_T700_28"])

    @classmethod
    def SkyVision_SkyVision_T400_16(cls):
        return cls.from_database(cls._DATABASE["SkyVision_SkyVision_T400_16"])

    @classmethod
    def TS_Optics_TS_6_f_6_Newton(cls):
        return cls.from_database(cls._DATABASE["TS_Optics_TS_6_f_6_Newton"])

    @classmethod
    def TS_Optics_TS_8_f_5_Newton(cls):
        return cls.from_database(cls._DATABASE["TS_Optics_TS_8_f_5_Newton"])

    @classmethod
    def TS_Optics_TS_8_f_4_Newton(cls):
        return cls.from_database(cls._DATABASE["TS_Optics_TS_8_f_4_Newton"])

    @classmethod
    def TS_Optics_TS_10_f_4_Newton(cls):
        return cls.from_database(cls._DATABASE["TS_Optics_TS_10_f_4_Newton"])

    @classmethod
    def TS_Optics_TS_10_f_5_Newton(cls):
        return cls.from_database(cls._DATABASE["TS_Optics_TS_10_f_5_Newton"])

    @classmethod
    def TS_Optics_TS_12_f_4_Newton(cls):
        return cls.from_database(cls._DATABASE["TS_Optics_TS_12_f_4_Newton"])

    @classmethod
    def TS_Optics_TS_12_f_5_Dobson(cls):
        return cls.from_database(cls._DATABASE["TS_Optics_TS_12_f_5_Dobson"])

    @classmethod
    def TS_Optics_TS_14_f_4_6_Newton(cls):
        return cls.from_database(cls._DATABASE["TS_Optics_TS_14_f_4_6_Newton"])

    @classmethod
    def Lacerta_72_432_APO(cls):
        return cls.from_database(cls._DATABASE["Lacerta_72_432_APO"])

    @classmethod
    def Lacerta_80_480_APO(cls):
        return cls.from_database(cls._DATABASE["Lacerta_80_480_APO"])

    @classmethod
    def Lacerta_102_714_APO(cls):
        return cls.from_database(cls._DATABASE["Lacerta_102_714_APO"])

    @classmethod
    def Lacerta_130_910_APO(cls):
        return cls.from_database(cls._DATABASE["Lacerta_130_910_APO"])

    @classmethod
    def Vaonis_Stellina(cls):
        return cls.from_database(cls._DATABASE["Vaonis_Stellina"])

    @classmethod
    def Vaonis_Vespera(cls):
        return cls.from_database(cls._DATABASE["Vaonis_Vespera"])

    @classmethod
    def Vaonis_Vespera_Pro(cls):
        return cls.from_database(cls._DATABASE["Vaonis_Vespera_Pro"])

    @classmethod
    def Unistellar_eVscope_2(cls):
        return cls.from_database(cls._DATABASE["Unistellar_eVscope_2"])

    @classmethod
    def Voigtlander_Nokton_50mm_f_1_2_Sony_E(cls):
        return cls.from_database(cls._DATABASE["Voigtlander_Nokton_50mm_f_1_2_Sony_E"])

    @classmethod
    def Voigtlander_APO_Lanthar_110mm_f_2_5_Sony_E(cls):
        return cls.from_database(
            cls._DATABASE["Voigtlander_APO_Lanthar_110mm_f_2_5_Sony_E"]
        )

    @classmethod
    def ID_7Artisans_50mm_f_1_05_Sony_E(cls):
        return cls.from_database(cls._DATABASE["ID_7Artisans_50mm_f_1_05_Sony_E"])

    @classmethod
    def Viltrox_85mm_f_1_8_II_Sony_E(cls):
        return cls.from_database(cls._DATABASE["Viltrox_85mm_f_1_8_II_Sony_E"])

    @classmethod
    def Celestron_NexStar_127SLT(cls):
        return cls.from_database(cls._DATABASE["Celestron_NexStar_127SLT"])

    @classmethod
    def Celestron_NexStar_130SLT(cls):
        return cls.from_database(cls._DATABASE["Celestron_NexStar_130SLT"])

    @classmethod
    def Celestron_Astro_Fi_5_SCT(cls):
        return cls.from_database(cls._DATABASE["Celestron_Astro_Fi_5_SCT"])

    @classmethod
    def Celestron_Astro_Fi_6_SCT(cls):
        return cls.from_database(cls._DATABASE["Celestron_Astro_Fi_6_SCT"])

    @classmethod
    def Celestron_AstroMaster_114EQ(cls):
        return cls.from_database(cls._DATABASE["Celestron_AstroMaster_114EQ"])

    @classmethod
    def Celestron_AstroMaster_70AZ(cls):
        return cls.from_database(cls._DATABASE["Celestron_AstroMaster_70AZ"])

    @classmethod
    def Celestron_AstroMaster_90AZ(cls):
        return cls.from_database(cls._DATABASE["Celestron_AstroMaster_90AZ"])

    @classmethod
    def Celestron_StarSense_Explorer_8_SCT(cls):
        return cls.from_database(cls._DATABASE["Celestron_StarSense_Explorer_8_SCT"])

    @classmethod
    def Celestron_StarSense_Explorer_LT_80AZ(cls):
        return cls.from_database(cls._DATABASE["Celestron_StarSense_Explorer_LT_80AZ"])

    @classmethod
    def Celestron_Advanced_VX_6_SCT(cls):
        return cls.from_database(cls._DATABASE["Celestron_Advanced_VX_6_SCT"])

    @classmethod
    def Celestron_Advanced_VX_9_25_SCT(cls):
        return cls.from_database(cls._DATABASE["Celestron_Advanced_VX_9_25_SCT"])

    @classmethod
    def Celestron_Advanced_VX_11_SCT(cls):
        return cls.from_database(cls._DATABASE["Celestron_Advanced_VX_11_SCT"])

    @classmethod
    def Meade_LightBridge_10_Dob(cls):
        return cls.from_database(cls._DATABASE["Meade_LightBridge_10_Dob"])

    @classmethod
    def Meade_LightBridge_12_Dob(cls):
        return cls.from_database(cls._DATABASE["Meade_LightBridge_12_Dob"])

    @classmethod
    def Meade_LightBridge_16_Dob(cls):
        return cls.from_database(cls._DATABASE["Meade_LightBridge_16_Dob"])

    @classmethod
    def Meade_LightBridge_8_Dob(cls):
        return cls.from_database(cls._DATABASE["Meade_LightBridge_8_Dob"])

    @classmethod
    def Meade_LX90_ACF_8(cls):
        return cls.from_database(cls._DATABASE["Meade_LX90_ACF_8"])

    @classmethod
    def Meade_LX90_ACF_10(cls):
        return cls.from_database(cls._DATABASE["Meade_LX90_ACF_10"])

    @classmethod
    def Meade_LX90_ACF_12(cls):
        return cls.from_database(cls._DATABASE["Meade_LX90_ACF_12"])

    @classmethod
    def Meade_StarNavigator_NG_102mm(cls):
        return cls.from_database(cls._DATABASE["Meade_StarNavigator_NG_102mm"])

    @classmethod
    def Meade_StarNavigator_NG_130mm(cls):
        return cls.from_database(cls._DATABASE["Meade_StarNavigator_NG_130mm"])

    @classmethod
    def Meade_Polaris_127mm_EQ(cls):
        return cls.from_database(cls._DATABASE["Meade_Polaris_127mm_EQ"])

    @classmethod
    def Meade_Polaris_130mm_EQ(cls):
        return cls.from_database(cls._DATABASE["Meade_Polaris_130mm_EQ"])

    @classmethod
    def Meade_S102_102mm_APO(cls):
        return cls.from_database(cls._DATABASE["Meade_S102_102mm_APO"])

    @classmethod
    def Meade_S130_130mm_APO(cls):
        return cls.from_database(cls._DATABASE["Meade_S130_130mm_APO"])

    @classmethod
    def Sky_Watcher_Star_Adventurer_GTi_80ED(cls):
        return cls.from_database(cls._DATABASE["Sky_Watcher_Star_Adventurer_GTi_80ED"])

    @classmethod
    def Sky_Watcher_Starquest_80MC(cls):
        return cls.from_database(cls._DATABASE["Sky_Watcher_Starquest_80MC"])

    @classmethod
    def Sky_Watcher_Heritage_P130_FlexTube(cls):
        return cls.from_database(cls._DATABASE["Sky_Watcher_Heritage_P130_FlexTube"])

    @classmethod
    def Sky_Watcher_Skyliner_200P_FlexTube(cls):
        return cls.from_database(cls._DATABASE["Sky_Watcher_Skyliner_200P_FlexTube"])

    @classmethod
    def Sky_Watcher_Skyliner_250P_FlexTube(cls):
        return cls.from_database(cls._DATABASE["Sky_Watcher_Skyliner_250P_FlexTube"])

    @classmethod
    def Sky_Watcher_Skyliner_300P_FlexTube(cls):
        return cls.from_database(cls._DATABASE["Sky_Watcher_Skyliner_300P_FlexTube"])

    @classmethod
    def Sky_Watcher_Skyliner_350P_FlexTube(cls):
        return cls.from_database(cls._DATABASE["Sky_Watcher_Skyliner_350P_FlexTube"])

    @classmethod
    def Sky_Watcher_Stargate_500P_Truss_Dob(cls):
        return cls.from_database(cls._DATABASE["Sky_Watcher_Stargate_500P_Truss_Dob"])

    @classmethod
    def Sky_Watcher_Stargate_450P_Truss_Dob(cls):
        return cls.from_database(cls._DATABASE["Sky_Watcher_Stargate_450P_Truss_Dob"])

    @classmethod
    def Sky_Watcher_Evostar_150DX(cls):
        return cls.from_database(cls._DATABASE["Sky_Watcher_Evostar_150DX"])

    @classmethod
    def Sky_Watcher_Equinox_80(cls):
        return cls.from_database(cls._DATABASE["Sky_Watcher_Equinox_80"])

    @classmethod
    def Sky_Watcher_Equinox_100(cls):
        return cls.from_database(cls._DATABASE["Sky_Watcher_Equinox_100"])

    @classmethod
    def Sky_Watcher_Equinox_120(cls):
        return cls.from_database(cls._DATABASE["Sky_Watcher_Equinox_120"])

    @classmethod
    def Orion_SpaceProbe_130ST_EQ(cls):
        return cls.from_database(cls._DATABASE["Orion_SpaceProbe_130ST_EQ"])

    @classmethod
    def Orion_StarBlast_4_5_EQ(cls):
        return cls.from_database(cls._DATABASE["Orion_StarBlast_4_5_EQ"])

    @classmethod
    def Orion_StarBlast_6(cls):
        return cls.from_database(cls._DATABASE["Orion_StarBlast_6"])

    @classmethod
    def Orion_AstroView_6_EQ(cls):
        return cls.from_database(cls._DATABASE["Orion_AstroView_6_EQ"])

    @classmethod
    def Orion_SkyQuest_XT6_Classic_Dob(cls):
        return cls.from_database(cls._DATABASE["Orion_SkyQuest_XT6_Classic_Dob"])

    @classmethod
    def Orion_SkyQuest_XX16g_Dob(cls):
        return cls.from_database(cls._DATABASE["Orion_SkyQuest_XX16g_Dob"])

    @classmethod
    def Orion_SkyLine_6_Dob_1(cls):
        return cls.from_database(cls._DATABASE["Orion_SkyLine_6_Dob_1"])

    @classmethod
    def Orion_SkyLine_8_Dob_1(cls):
        return cls.from_database(cls._DATABASE["Orion_SkyLine_8_Dob_1"])

    @classmethod
    def Orion_SkyLine_10_Dob_1(cls):
        return cls.from_database(cls._DATABASE["Orion_SkyLine_10_Dob_1"])

    @classmethod
    def Orion_SkyLine_12_Dob_1(cls):
        return cls.from_database(cls._DATABASE["Orion_SkyLine_12_Dob_1"])

    @classmethod
    def Orion_SkyView_Pro_8(cls):
        return cls.from_database(cls._DATABASE["Orion_SkyView_Pro_8"])

    @classmethod
    def Orion_ED_80T_CF_Apochromat(cls):
        return cls.from_database(cls._DATABASE["Orion_ED_80T_CF_Apochromat"])

    @classmethod
    def Orion_EON_115mm_ED_Apochromat(cls):
        return cls.from_database(cls._DATABASE["Orion_EON_115mm_ED_Apochromat"])

    @classmethod
    def Bresser_Messier_AR_127S(cls):
        return cls.from_database(cls._DATABASE["Bresser_Messier_AR_127S"])

    @classmethod
    def Bresser_Messier_NT_150S_6_f_5(cls):
        return cls.from_database(cls._DATABASE["Bresser_Messier_NT_150S_6_f_5"])

    @classmethod
    def Bresser_Messier_Dobson_8(cls):
        return cls.from_database(cls._DATABASE["Bresser_Messier_Dobson_8"])

    @classmethod
    def Bresser_Messier_Dobson_10(cls):
        return cls.from_database(cls._DATABASE["Bresser_Messier_Dobson_10"])

    @classmethod
    def Bresser_Messier_Dobson_12(cls):
        return cls.from_database(cls._DATABASE["Bresser_Messier_Dobson_12"])

    @classmethod
    def Bresser_Pollux_150_1400_EQ3(cls):
        return cls.from_database(cls._DATABASE["Bresser_Pollux_150_1400_EQ3"])

    @classmethod
    def Bresser_Lyra_70_900_EQ(cls):
        return cls.from_database(cls._DATABASE["Bresser_Lyra_70_900_EQ"])

    @classmethod
    def Bresser_Jupiter_70_700_AZ(cls):
        return cls.from_database(cls._DATABASE["Bresser_Jupiter_70_700_AZ"])

    @classmethod
    def Bresser_Taurus_90_900_NG(cls):
        return cls.from_database(cls._DATABASE["Bresser_Taurus_90_900_NG"])

    @classmethod
    def Vixen_A62SS(cls):
        return cls.from_database(cls._DATABASE["Vixen_A62SS"])

    @classmethod
    def Vixen_A70Lf(cls):
        return cls.from_database(cls._DATABASE["Vixen_A70Lf"])

    @classmethod
    def Vixen_A105M(cls):
        return cls.from_database(cls._DATABASE["Vixen_A105M"])

    @classmethod
    def Vixen_VSD100_F3_8_V2(cls):
        return cls.from_database(cls._DATABASE["Vixen_VSD100_F3_8_V2"])

    @classmethod
    def Vixen_R130Sf(cls):
        return cls.from_database(cls._DATABASE["Vixen_R130Sf"])

    @classmethod
    def Vixen_VMC95L(cls):
        return cls.from_database(cls._DATABASE["Vixen_VMC95L"])

    @classmethod
    def Vixen_VMC110L(cls):
        return cls.from_database(cls._DATABASE["Vixen_VMC110L"])

    @classmethod
    def Vixen_VMC260L(cls):
        return cls.from_database(cls._DATABASE["Vixen_VMC260L"])

    @classmethod
    def Explore_Scientific_AR102_Air_Spaced_Doublet(cls):
        return cls.from_database(
            cls._DATABASE["Explore_Scientific_AR102_Air_Spaced_Doublet"]
        )

    @classmethod
    def Explore_Scientific_AR127_Air_Spaced(cls):
        return cls.from_database(cls._DATABASE["Explore_Scientific_AR127_Air_Spaced"])

    @classmethod
    def Explore_Scientific_AR152_Air_Spaced(cls):
        return cls.from_database(cls._DATABASE["Explore_Scientific_AR152_Air_Spaced"])

    @classmethod
    def Explore_Scientific_FirstLight_130mm_f_4_6_Newton(cls):
        return cls.from_database(
            cls._DATABASE["Explore_Scientific_FirstLight_130mm_f_4_6_Newton"]
        )

    @classmethod
    def Explore_Scientific_FirstLight_150mm_f_5_Newton(cls):
        return cls.from_database(
            cls._DATABASE["Explore_Scientific_FirstLight_150mm_f_5_Newton"]
        )

    @classmethod
    def Explore_Scientific_FirstLight_200mm_f_5_Newton(cls):
        return cls.from_database(
            cls._DATABASE["Explore_Scientific_FirstLight_200mm_f_5_Newton"]
        )

    @classmethod
    def Explore_Scientific_FirstLight_102mm_Mak(cls):
        return cls.from_database(
            cls._DATABASE["Explore_Scientific_FirstLight_102mm_Mak"]
        )

    @classmethod
    def Explore_Scientific_FirstLight_127mm_Mak(cls):
        return cls.from_database(
            cls._DATABASE["Explore_Scientific_FirstLight_127mm_Mak"]
        )

    @classmethod
    def Explore_Scientific_FirstLight_80mm_APO(cls):
        return cls.from_database(
            cls._DATABASE["Explore_Scientific_FirstLight_80mm_APO"]
        )

    @classmethod
    def Explore_Scientific_FirstLight_102mm_APO(cls):
        return cls.from_database(
            cls._DATABASE["Explore_Scientific_FirstLight_102mm_APO"]
        )

    @classmethod
    def Explore_Scientific_ED_APO_80mm_CF(cls):
        return cls.from_database(cls._DATABASE["Explore_Scientific_ED_APO_80mm_CF"])

    @classmethod
    def Explore_Scientific_ED_APO_102mm_CF(cls):
        return cls.from_database(cls._DATABASE["Explore_Scientific_ED_APO_102mm_CF"])

    @classmethod
    def Explore_Scientific_ED_APO_127mm_CF(cls):
        return cls.from_database(cls._DATABASE["Explore_Scientific_ED_APO_127mm_CF"])

    @classmethod
    def Explore_Scientific_ED_APO_152mm_CF(cls):
        return cls.from_database(cls._DATABASE["Explore_Scientific_ED_APO_152mm_CF"])

    @classmethod
    def GSO_Newton_6_f_5(cls):
        return cls.from_database(cls._DATABASE["GSO_Newton_6_f_5"])

    @classmethod
    def GSO_Newton_8_f_4(cls):
        return cls.from_database(cls._DATABASE["GSO_Newton_8_f_4"])

    @classmethod
    def GSO_Newton_8_f_5(cls):
        return cls.from_database(cls._DATABASE["GSO_Newton_8_f_5"])

    @classmethod
    def GSO_Newton_10_f_5(cls):
        return cls.from_database(cls._DATABASE["GSO_Newton_10_f_5"])

    @classmethod
    def GSO_Newton_12_f_5(cls):
        return cls.from_database(cls._DATABASE["GSO_Newton_12_f_5"])

    @classmethod
    def GSO_Newton_16_f_4_5(cls):
        return cls.from_database(cls._DATABASE["GSO_Newton_16_f_4_5"])

    @classmethod
    def GSO_Newton_6_f_8_Dob(cls):
        return cls.from_database(cls._DATABASE["GSO_Newton_6_f_8_Dob"])

    @classmethod
    def GSO_Newton_8_f_6_Dob(cls):
        return cls.from_database(cls._DATABASE["GSO_Newton_8_f_6_Dob"])

    @classmethod
    def GSO_Newton_10_f_6_Dob(cls):
        return cls.from_database(cls._DATABASE["GSO_Newton_10_f_6_Dob"])

    @classmethod
    def GSO_Newton_12_f_5_Dob(cls):
        return cls.from_database(cls._DATABASE["GSO_Newton_12_f_5_Dob"])

    @classmethod
    def GSO_GSO_80ED(cls):
        return cls.from_database(cls._DATABASE["GSO_GSO_80ED"])

    @classmethod
    def GSO_GSO_102ED(cls):
        return cls.from_database(cls._DATABASE["GSO_GSO_102ED"])

    @classmethod
    def TPO_RC_12(cls):
        return cls.from_database(cls._DATABASE["TPO_RC_12"])

    @classmethod
    def TPO_RC_14(cls):
        return cls.from_database(cls._DATABASE["TPO_RC_14"])

    @classmethod
    def TPO_TPO_6_f_4_Newton(cls):
        return cls.from_database(cls._DATABASE["TPO_TPO_6_f_4_Newton"])

    @classmethod
    def TPO_TPO_8_f_4_Newton(cls):
        return cls.from_database(cls._DATABASE["TPO_TPO_8_f_4_Newton"])

    @classmethod
    def TPO_TPO_10_f_4_Newton(cls):
        return cls.from_database(cls._DATABASE["TPO_TPO_10_f_4_Newton"])

    @classmethod
    def TPO_TPO_80mm_ED_APO(cls):
        return cls.from_database(cls._DATABASE["TPO_TPO_80mm_ED_APO"])

    @classmethod
    def TPO_TPO_102mm_ED_APO(cls):
        return cls.from_database(cls._DATABASE["TPO_TPO_102mm_ED_APO"])

    @classmethod
    def TPO_UltraWide_6_f_2_8_Astrograph(cls):
        return cls.from_database(cls._DATABASE["TPO_UltraWide_6_f_2_8_Astrograph"])

    @classmethod
    def Apertura_AD6_Dobsonian(cls):
        return cls.from_database(cls._DATABASE["Apertura_AD6_Dobsonian"])

    @classmethod
    def Zhumell_Z6_Dobsonian(cls):
        return cls.from_database(cls._DATABASE["Zhumell_Z6_Dobsonian"])

    @classmethod
    def Apertura_AD8_Dobsonian(cls):
        return cls.from_database(cls._DATABASE["Apertura_AD8_Dobsonian"])

    @classmethod
    def Zhumell_Z8_Dobsonian(cls):
        return cls.from_database(cls._DATABASE["Zhumell_Z8_Dobsonian"])

    @classmethod
    def Apertura_AD10_Dobsonian(cls):
        return cls.from_database(cls._DATABASE["Apertura_AD10_Dobsonian"])

    @classmethod
    def Zhumell_Z10_Dobsonian(cls):
        return cls.from_database(cls._DATABASE["Zhumell_Z10_Dobsonian"])

    @classmethod
    def Apertura_AD12_Dobsonian(cls):
        return cls.from_database(cls._DATABASE["Apertura_AD12_Dobsonian"])

    @classmethod
    def Zhumell_Z12_Dobsonian(cls):
        return cls.from_database(cls._DATABASE["Zhumell_Z12_Dobsonian"])

    @classmethod
    def Apertura_AD14_Dobsonian(cls):
        return cls.from_database(cls._DATABASE["Apertura_AD14_Dobsonian"])

    @classmethod
    def Zhumell_Z14_Dobsonian(cls):
        return cls.from_database(cls._DATABASE["Zhumell_Z14_Dobsonian"])

    @classmethod
    def Apertura_AD16_Dobsonian(cls):
        return cls.from_database(cls._DATABASE["Apertura_AD16_Dobsonian"])

    @classmethod
    def Zhumell_Z16_Dobsonian(cls):
        return cls.from_database(cls._DATABASE["Zhumell_Z16_Dobsonian"])

    @classmethod
    def Sky_Watcher_SkyMax_102(cls):
        return cls.from_database(cls._DATABASE["Sky_Watcher_SkyMax_102"])

    @classmethod
    def Sky_Watcher_SkyMax_127(cls):
        return cls.from_database(cls._DATABASE["Sky_Watcher_SkyMax_127"])

    @classmethod
    def Sky_Watcher_SkyMax_150_Pro(cls):
        return cls.from_database(cls._DATABASE["Sky_Watcher_SkyMax_150_Pro"])

    @classmethod
    def Sky_Watcher_SkyMax_180_Pro(cls):
        return cls.from_database(cls._DATABASE["Sky_Watcher_SkyMax_180_Pro"])

    @classmethod
    def Vaonis_Hyperia(cls):
        return cls.from_database(cls._DATABASE["Vaonis_Hyperia"])

    @classmethod
    def Unistellar_eQuinox_2(cls):
        return cls.from_database(cls._DATABASE["Unistellar_eQuinox_2"])

    @classmethod
    def Unistellar_Odyssey(cls):
        return cls.from_database(cls._DATABASE["Unistellar_Odyssey"])

    @classmethod
    def Unistellar_Odyssey_Pro(cls):
        return cls.from_database(cls._DATABASE["Unistellar_Odyssey_Pro"])

    @classmethod
    def TeleVue_NP101is(cls):
        return cls.from_database(cls._DATABASE["TeleVue_NP101is"])

    @classmethod
    def TeleVue_NP127fli(cls):
        return cls.from_database(cls._DATABASE["TeleVue_NP127fli"])

    @classmethod
    def TeleVue_TV_60(cls):
        return cls.from_database(cls._DATABASE["TeleVue_TV_60"])

    @classmethod
    def TeleVue_TV_76(cls):
        return cls.from_database(cls._DATABASE["TeleVue_TV_76"])

    @classmethod
    def TeleVue_TV_85(cls):
        return cls.from_database(cls._DATABASE["TeleVue_TV_85"])

    @classmethod
    def TeleVue_TV_102(cls):
        return cls.from_database(cls._DATABASE["TeleVue_TV_102"])

    @classmethod
    def TeleVue_TV_NP127is(cls):
        return cls.from_database(cls._DATABASE["TeleVue_TV_NP127is"])

    @classmethod
    def TeleVue_TV_NP101(cls):
        return cls.from_database(cls._DATABASE["TeleVue_TV_NP101"])

    @classmethod
    def Lunt_Solar_LS60THa(cls):
        return cls.from_database(cls._DATABASE["Lunt_Solar_LS60THa"])

    @classmethod
    def Lunt_Solar_LS80THa(cls):
        return cls.from_database(cls._DATABASE["Lunt_Solar_LS80THa"])

    @classmethod
    def Lunt_Solar_LS100THa(cls):
        return cls.from_database(cls._DATABASE["Lunt_Solar_LS100THa"])

    @classmethod
    def Lunt_Solar_LS130THa(cls):
        return cls.from_database(cls._DATABASE["Lunt_Solar_LS130THa"])

    @classmethod
    def Lunt_Solar_LS152THa(cls):
        return cls.from_database(cls._DATABASE["Lunt_Solar_LS152THa"])

    @classmethod
    def Lunt_Solar_LS50C_Ca_K(cls):
        return cls.from_database(cls._DATABASE["Lunt_Solar_LS50C_Ca_K"])

    @classmethod
    def Lunt_Solar_LS60MT(cls):
        return cls.from_database(cls._DATABASE["Lunt_Solar_LS60MT"])

    @classmethod
    def Lunt_Solar_LS80MT(cls):
        return cls.from_database(cls._DATABASE["Lunt_Solar_LS80MT"])

    @classmethod
    def DayStar_SOLO_60_SE(cls):
        return cls.from_database(cls._DATABASE["DayStar_SOLO_60_SE"])

    @classmethod
    def DayStar_SOLO_60_PE(cls):
        return cls.from_database(cls._DATABASE["DayStar_SOLO_60_PE"])

    @classmethod
    def DayStar_SOLO_80_SE(cls):
        return cls.from_database(cls._DATABASE["DayStar_SOLO_80_SE"])

    @classmethod
    def DayStar_SolaREDi_66(cls):
        return cls.from_database(cls._DATABASE["DayStar_SolaREDi_66"])

    @classmethod
    def DayStar_SolaREDi_127(cls):
        return cls.from_database(cls._DATABASE["DayStar_SolaREDi_127"])

    @classmethod
    def Coronado_PST(cls):
        return cls.from_database(cls._DATABASE["Coronado_PST"])

    @classmethod
    def Coronado_SolarMax_III_90(cls):
        return cls.from_database(cls._DATABASE["Coronado_SolarMax_III_90"])

    @classmethod
    def Coronado_SolarMax_II_60_BF15(cls):
        return cls.from_database(cls._DATABASE["Coronado_SolarMax_II_60_BF15"])

    @classmethod
    def Canon_EF_200mm_f_2_8L_II_USM(cls):
        return cls.from_database(cls._DATABASE["Canon_EF_200mm_f_2_8L_II_USM"])

    @classmethod
    def Canon_EF_50mm_f_1_4_USM(cls):
        return cls.from_database(cls._DATABASE["Canon_EF_50mm_f_1_4_USM"])

    @classmethod
    def Canon_EF_50mm_f_1_2L_USM(cls):
        return cls.from_database(cls._DATABASE["Canon_EF_50mm_f_1_2L_USM"])

    @classmethod
    def Canon_EF_85mm_f_1_4L_IS_USM(cls):
        return cls.from_database(cls._DATABASE["Canon_EF_85mm_f_1_4L_IS_USM"])

    @classmethod
    def Canon_EF_85mm_f_1_8_USM(cls):
        return cls.from_database(cls._DATABASE["Canon_EF_85mm_f_1_8_USM"])

    @classmethod
    def Canon_EF_100mm_f_2_USM(cls):
        return cls.from_database(cls._DATABASE["Canon_EF_100mm_f_2_USM"])

    @classmethod
    def Canon_EF_135mm_f_2L_USM(cls):
        return cls.from_database(cls._DATABASE["Canon_EF_135mm_f_2L_USM"])

    @classmethod
    def Canon_EF_70_200mm_f_2_8L_IS_III_USM(cls):
        return cls.from_database(cls._DATABASE["Canon_EF_70_200mm_f_2_8L_IS_III_USM"])

    @classmethod
    def Canon_EF_70_200mm_f_4L_IS_II_USM(cls):
        return cls.from_database(cls._DATABASE["Canon_EF_70_200mm_f_4L_IS_II_USM"])

    @classmethod
    def Canon_EF_200mm_f_2L_IS_USM(cls):
        return cls.from_database(cls._DATABASE["Canon_EF_200mm_f_2L_IS_USM"])

    @classmethod
    def Canon_EF_300mm_f_2_8L_IS_II_USM(cls):
        return cls.from_database(cls._DATABASE["Canon_EF_300mm_f_2_8L_IS_II_USM"])

    @classmethod
    def Canon_EF_300mm_f_4L_IS_USM(cls):
        return cls.from_database(cls._DATABASE["Canon_EF_300mm_f_4L_IS_USM"])

    @classmethod
    def Canon_EF_400mm_f_2_8L_IS_III_USM(cls):
        return cls.from_database(cls._DATABASE["Canon_EF_400mm_f_2_8L_IS_III_USM"])

    @classmethod
    def Canon_EF_400mm_f_5_6L_USM(cls):
        return cls.from_database(cls._DATABASE["Canon_EF_400mm_f_5_6L_USM"])

    @classmethod
    def Canon_EF_500mm_f_4L_IS_II_USM(cls):
        return cls.from_database(cls._DATABASE["Canon_EF_500mm_f_4L_IS_II_USM"])

    @classmethod
    def Canon_EF_24_70mm_f_2_8L_II_USM(cls):
        return cls.from_database(cls._DATABASE["Canon_EF_24_70mm_f_2_8L_II_USM"])

    @classmethod
    def Canon_EF_16_35mm_f_2_8L_III_USM(cls):
        return cls.from_database(cls._DATABASE["Canon_EF_16_35mm_f_2_8L_III_USM"])

    @classmethod
    def Canon_EF_24mm_f_1_4L_II_USM(cls):
        return cls.from_database(cls._DATABASE["Canon_EF_24mm_f_1_4L_II_USM"])

    @classmethod
    def Canon_EF_14mm_f_2_8L_II_USM(cls):
        return cls.from_database(cls._DATABASE["Canon_EF_14mm_f_2_8L_II_USM"])

    @classmethod
    def Canon_RF_50mm_f_1_2L_USM(cls):
        return cls.from_database(cls._DATABASE["Canon_RF_50mm_f_1_2L_USM"])

    @classmethod
    def Canon_RF_85mm_f_1_2L_USM(cls):
        return cls.from_database(cls._DATABASE["Canon_RF_85mm_f_1_2L_USM"])

    @classmethod
    def Canon_RF_135mm_f_1_8L_IS_USM(cls):
        return cls.from_database(cls._DATABASE["Canon_RF_135mm_f_1_8L_IS_USM"])

    @classmethod
    def Canon_RF_70_200mm_f_2_8L_IS_USM(cls):
        return cls.from_database(cls._DATABASE["Canon_RF_70_200mm_f_2_8L_IS_USM"])

    @classmethod
    def Canon_RF_100_500mm_f_4_5_7_1L_IS_USM(cls):
        return cls.from_database(cls._DATABASE["Canon_RF_100_500mm_f_4_5_7_1L_IS_USM"])

    @classmethod
    def Canon_RF_200_800mm_f_6_3_9_IS_USM(cls):
        return cls.from_database(cls._DATABASE["Canon_RF_200_800mm_f_6_3_9_IS_USM"])

    @classmethod
    def Canon_RF_400mm_f_2_8L_IS_USM(cls):
        return cls.from_database(cls._DATABASE["Canon_RF_400mm_f_2_8L_IS_USM"])

    @classmethod
    def Canon_RF_600mm_f_4L_IS_USM(cls):
        return cls.from_database(cls._DATABASE["Canon_RF_600mm_f_4L_IS_USM"])

    @classmethod
    def Canon_RF_800mm_f_5_6L_IS_USM(cls):
        return cls.from_database(cls._DATABASE["Canon_RF_800mm_f_5_6L_IS_USM"])

    @classmethod
    def Canon_RF_100mm_f_2_8L_Macro_IS_USM(cls):
        return cls.from_database(cls._DATABASE["Canon_RF_100mm_f_2_8L_Macro_IS_USM"])

    @classmethod
    def Canon_RF_24_70mm_f_2_8L_IS_USM(cls):
        return cls.from_database(cls._DATABASE["Canon_RF_24_70mm_f_2_8L_IS_USM"])

    @classmethod
    def Canon_RF_14_35mm_f_4L_IS_USM(cls):
        return cls.from_database(cls._DATABASE["Canon_RF_14_35mm_f_4L_IS_USM"])

    @classmethod
    def Canon_RF_15_35mm_f_2_8L_IS_USM(cls):
        return cls.from_database(cls._DATABASE["Canon_RF_15_35mm_f_2_8L_IS_USM"])

    @classmethod
    def Nikon_AF_S_200mm_f_2G_ED_VR_II(cls):
        return cls.from_database(cls._DATABASE["Nikon_AF_S_200mm_f_2G_ED_VR_II"])

    @classmethod
    def Nikon_AF_S_300mm_f_2_8G_ED_VR_II(cls):
        return cls.from_database(cls._DATABASE["Nikon_AF_S_300mm_f_2_8G_ED_VR_II"])

    @classmethod
    def Nikon_AF_S_500mm_f_4E_FL_ED_VR(cls):
        return cls.from_database(cls._DATABASE["Nikon_AF_S_500mm_f_4E_FL_ED_VR"])

    @classmethod
    def Nikon_AF_S_600mm_f_4E_FL_ED_VR(cls):
        return cls.from_database(cls._DATABASE["Nikon_AF_S_600mm_f_4E_FL_ED_VR"])

    @classmethod
    def Nikon_AF_S_85mm_f_1_4G(cls):
        return cls.from_database(cls._DATABASE["Nikon_AF_S_85mm_f_1_4G"])

    @classmethod
    def Nikon_AF_S_50mm_f_1_4G(cls):
        return cls.from_database(cls._DATABASE["Nikon_AF_S_50mm_f_1_4G"])

    @classmethod
    def Nikon_AF_S_14_24mm_f_2_8G_ED(cls):
        return cls.from_database(cls._DATABASE["Nikon_AF_S_14_24mm_f_2_8G_ED"])

    @classmethod
    def Nikon_AF_S_24_70mm_f_2_8E_ED_VR(cls):
        return cls.from_database(cls._DATABASE["Nikon_AF_S_24_70mm_f_2_8E_ED_VR"])

    @classmethod
    def Nikon_AF_S_180_400mm_f_4E_TC(cls):
        return cls.from_database(cls._DATABASE["Nikon_AF_S_180_400mm_f_4E_TC"])

    @classmethod
    def Nikon_AF_S_200_500mm_f_5_6E_ED_VR(cls):
        return cls.from_database(cls._DATABASE["Nikon_AF_S_200_500mm_f_5_6E_ED_VR"])

    @classmethod
    def Nikon_Z_50mm_f_1_2_S(cls):
        return cls.from_database(cls._DATABASE["Nikon_Z_50mm_f_1_2_S"])

    @classmethod
    def Nikon_Z_85mm_f_1_2_S(cls):
        return cls.from_database(cls._DATABASE["Nikon_Z_85mm_f_1_2_S"])

    @classmethod
    def Nikon_Z_400mm_f_4_5_VR_S(cls):
        return cls.from_database(cls._DATABASE["Nikon_Z_400mm_f_4_5_VR_S"])

    @classmethod
    def Nikon_Z_600mm_f_4_TC_VR_S(cls):
        return cls.from_database(cls._DATABASE["Nikon_Z_600mm_f_4_TC_VR_S"])

    @classmethod
    def Nikon_Z_800mm_f_6_3_VR_S(cls):
        return cls.from_database(cls._DATABASE["Nikon_Z_800mm_f_6_3_VR_S"])

    @classmethod
    def Nikon_Z_70_200mm_f_2_8_VR_S(cls):
        return cls.from_database(cls._DATABASE["Nikon_Z_70_200mm_f_2_8_VR_S"])

    @classmethod
    def Nikon_Z_24_70mm_f_2_8_S(cls):
        return cls.from_database(cls._DATABASE["Nikon_Z_24_70mm_f_2_8_S"])

    @classmethod
    def Nikon_Z_14_24mm_f_2_8_S(cls):
        return cls.from_database(cls._DATABASE["Nikon_Z_14_24mm_f_2_8_S"])

    @classmethod
    def Nikon_Z_180_600mm_f_5_6_6_3_VR(cls):
        return cls.from_database(cls._DATABASE["Nikon_Z_180_600mm_f_5_6_6_3_VR"])

    @classmethod
    def Sony_FE_200_600mm_f_5_6_6_3_G_OSS(cls):
        return cls.from_database(cls._DATABASE["Sony_FE_200_600mm_f_5_6_6_3_G_OSS"])

    @classmethod
    def Sony_FE_400mm_f_2_8_GM_OSS(cls):
        return cls.from_database(cls._DATABASE["Sony_FE_400mm_f_2_8_GM_OSS"])

    @classmethod
    def Sony_FE_600mm_f_4_GM_OSS(cls):
        return cls.from_database(cls._DATABASE["Sony_FE_600mm_f_4_GM_OSS"])

    @classmethod
    def Sony_FE_70_200mm_f_2_8_GM_OSS_II(cls):
        return cls.from_database(cls._DATABASE["Sony_FE_70_200mm_f_2_8_GM_OSS_II"])

    @classmethod
    def Sony_FE_100_400mm_f_4_5_5_6_GM_OSS(cls):
        return cls.from_database(cls._DATABASE["Sony_FE_100_400mm_f_4_5_5_6_GM_OSS"])

    @classmethod
    def Sony_FE_50mm_f_1_2_GM(cls):
        return cls.from_database(cls._DATABASE["Sony_FE_50mm_f_1_2_GM"])

    @classmethod
    def Sony_FE_24_70mm_f_2_8_GM_II(cls):
        return cls.from_database(cls._DATABASE["Sony_FE_24_70mm_f_2_8_GM_II"])

    @classmethod
    def Sony_FE_14mm_f_1_8_GM(cls):
        return cls.from_database(cls._DATABASE["Sony_FE_14mm_f_1_8_GM"])

    @classmethod
    def Sony_FE_20mm_f_1_8_G(cls):
        return cls.from_database(cls._DATABASE["Sony_FE_20mm_f_1_8_G"])

    @classmethod
    def Sony_FE_35mm_f_1_4_GM(cls):
        return cls.from_database(cls._DATABASE["Sony_FE_35mm_f_1_4_GM"])

    @classmethod
    def Sony_FE_300mm_f_2_8_GM_OSS(cls):
        return cls.from_database(cls._DATABASE["Sony_FE_300mm_f_2_8_GM_OSS"])

    @classmethod
    def Sigma_135mm_f_1_8_Art_Sony_E(cls):
        return cls.from_database(cls._DATABASE["Sigma_135mm_f_1_8_Art_Sony_E"])

    @classmethod
    def Sigma_105mm_f_1_4_Art_Sony_E(cls):
        return cls.from_database(cls._DATABASE["Sigma_105mm_f_1_4_Art_Sony_E"])

    @classmethod
    def Sigma_135mm_f_1_8_Art_Nikon_F(cls):
        return cls.from_database(cls._DATABASE["Sigma_135mm_f_1_8_Art_Nikon_F"])

    @classmethod
    def Sigma_105mm_f_1_4_Art_Nikon_F(cls):
        return cls.from_database(cls._DATABASE["Sigma_105mm_f_1_4_Art_Nikon_F"])

    @classmethod
    def Sigma_85mm_f_1_4_Art_EOS(cls):
        return cls.from_database(cls._DATABASE["Sigma_85mm_f_1_4_Art_EOS"])

    @classmethod
    def Sigma_85mm_f_1_4_Art_Sony_E(cls):
        return cls.from_database(cls._DATABASE["Sigma_85mm_f_1_4_Art_Sony_E"])

    @classmethod
    def Sigma_85mm_f_1_4_Art_Nikon_F(cls):
        return cls.from_database(cls._DATABASE["Sigma_85mm_f_1_4_Art_Nikon_F"])

    @classmethod
    def Sigma_40mm_f_1_4_Art_EOS(cls):
        return cls.from_database(cls._DATABASE["Sigma_40mm_f_1_4_Art_EOS"])

    @classmethod
    def Sigma_40mm_f_1_4_Art_Sony_E(cls):
        return cls.from_database(cls._DATABASE["Sigma_40mm_f_1_4_Art_Sony_E"])

    @classmethod
    def Sigma_24mm_f_1_4_Art_EOS(cls):
        return cls.from_database(cls._DATABASE["Sigma_24mm_f_1_4_Art_EOS"])

    @classmethod
    def Sigma_24mm_f_1_4_Art_Sony_E(cls):
        return cls.from_database(cls._DATABASE["Sigma_24mm_f_1_4_Art_Sony_E"])

    @classmethod
    def Sigma_20mm_f_1_4_Art_EOS(cls):
        return cls.from_database(cls._DATABASE["Sigma_20mm_f_1_4_Art_EOS"])

    @classmethod
    def Sigma_20mm_f_1_4_Art_Sony_E(cls):
        return cls.from_database(cls._DATABASE["Sigma_20mm_f_1_4_Art_Sony_E"])

    @classmethod
    def Sigma_50mm_f_1_4_Art_EOS(cls):
        return cls.from_database(cls._DATABASE["Sigma_50mm_f_1_4_Art_EOS"])

    @classmethod
    def Sigma_50mm_f_1_4_Art_Sony_E(cls):
        return cls.from_database(cls._DATABASE["Sigma_50mm_f_1_4_Art_Sony_E"])

    @classmethod
    def Sigma_50mm_f_1_4_Art_Nikon_F(cls):
        return cls.from_database(cls._DATABASE["Sigma_50mm_f_1_4_Art_Nikon_F"])

    @classmethod
    def Sigma_60_600mm_f_4_5_6_3_DG_EOS(cls):
        return cls.from_database(cls._DATABASE["Sigma_60_600mm_f_4_5_6_3_DG_EOS"])

    @classmethod
    def Sigma_60_600mm_f_4_5_6_3_DG_Sony_E(cls):
        return cls.from_database(cls._DATABASE["Sigma_60_600mm_f_4_5_6_3_DG_Sony_E"])

    @classmethod
    def Sigma_150_600mm_f_5_6_3_DG_Sony_E(cls):
        return cls.from_database(cls._DATABASE["Sigma_150_600mm_f_5_6_3_DG_Sony_E"])

    @classmethod
    def Sigma_150_600mm_f_5_6_3_DG_Nikon_F(cls):
        return cls.from_database(cls._DATABASE["Sigma_150_600mm_f_5_6_3_DG_Nikon_F"])

    @classmethod
    def Sigma_100_400mm_f_5_6_3_DG_EOS(cls):
        return cls.from_database(cls._DATABASE["Sigma_100_400mm_f_5_6_3_DG_EOS"])

    @classmethod
    def Sigma_100_400mm_f_5_6_3_DG_Sony_E(cls):
        return cls.from_database(cls._DATABASE["Sigma_100_400mm_f_5_6_3_DG_Sony_E"])

    @classmethod
    def Tamron_SP_150_600mm_f_5_6_3_EOS(cls):
        return cls.from_database(cls._DATABASE["Tamron_SP_150_600mm_f_5_6_3_EOS"])

    @classmethod
    def Tamron_SP_150_600mm_f_5_6_3_Nikon_F(cls):
        return cls.from_database(cls._DATABASE["Tamron_SP_150_600mm_f_5_6_3_Nikon_F"])

    @classmethod
    def Tamron_SP_150_600mm_f_5_6_3_Sony_E(cls):
        return cls.from_database(cls._DATABASE["Tamron_SP_150_600mm_f_5_6_3_Sony_E"])

    @classmethod
    def Tamron_150_500mm_f_5_6_7_Fuji_X(cls):
        return cls.from_database(cls._DATABASE["Tamron_150_500mm_f_5_6_7_Fuji_X"])

    @classmethod
    def Tamron_100_400mm_f_4_5_6_3_EOS(cls):
        return cls.from_database(cls._DATABASE["Tamron_100_400mm_f_4_5_6_3_EOS"])

    @classmethod
    def Tamron_70_180mm_f_2_8_Sony_E(cls):
        return cls.from_database(cls._DATABASE["Tamron_70_180mm_f_2_8_Sony_E"])

    @classmethod
    def Tamron_70_300mm_f_4_5_6_3_Sony_E(cls):
        return cls.from_database(cls._DATABASE["Tamron_70_300mm_f_4_5_6_3_Sony_E"])

    @classmethod
    def Tamron_28_200mm_f_2_8_5_6_Sony_E(cls):
        return cls.from_database(cls._DATABASE["Tamron_28_200mm_f_2_8_5_6_Sony_E"])

    @classmethod
    def Tamron_35_150mm_f_2_2_8_Sony_E(cls):
        return cls.from_database(cls._DATABASE["Tamron_35_150mm_f_2_2_8_Sony_E"])

    @classmethod
    def Tamron_50_400mm_f_4_5_6_3_Sony_E(cls):
        return cls.from_database(cls._DATABASE["Tamron_50_400mm_f_4_5_6_3_Sony_E"])

    @classmethod
    def Samyang_Rokinon_135mm_f_2_0_Nikon_F(cls):
        return cls.from_database(cls._DATABASE["Samyang_Rokinon_135mm_f_2_0_Nikon_F"])

    @classmethod
    def Samyang_Rokinon_85mm_f_1_4_EOS(cls):
        return cls.from_database(cls._DATABASE["Samyang_Rokinon_85mm_f_1_4_EOS"])

    @classmethod
    def Samyang_Rokinon_85mm_f_1_4_Sony_E(cls):
        return cls.from_database(cls._DATABASE["Samyang_Rokinon_85mm_f_1_4_Sony_E"])

    @classmethod
    def Samyang_Rokinon_85mm_f_1_4_Nikon_F(cls):
        return cls.from_database(cls._DATABASE["Samyang_Rokinon_85mm_f_1_4_Nikon_F"])

    @classmethod
    def Samyang_Rokinon_14mm_f_2_8_Sony_E(cls):
        return cls.from_database(cls._DATABASE["Samyang_Rokinon_14mm_f_2_8_Sony_E"])

    @classmethod
    def Samyang_Rokinon_14mm_f_2_8_Nikon_F(cls):
        return cls.from_database(cls._DATABASE["Samyang_Rokinon_14mm_f_2_8_Nikon_F"])

    @classmethod
    def Samyang_Rokinon_24mm_f_1_4_Sony_E(cls):
        return cls.from_database(cls._DATABASE["Samyang_Rokinon_24mm_f_1_4_Sony_E"])

    @classmethod
    def Samyang_Rokinon_24mm_f_1_4_Nikon_F(cls):
        return cls.from_database(cls._DATABASE["Samyang_Rokinon_24mm_f_1_4_Nikon_F"])

    @classmethod
    def Samyang_Rokinon_50mm_f_1_4_EOS(cls):
        return cls.from_database(cls._DATABASE["Samyang_Rokinon_50mm_f_1_4_EOS"])

    @classmethod
    def Samyang_Rokinon_50mm_f_1_4_Sony_E(cls):
        return cls.from_database(cls._DATABASE["Samyang_Rokinon_50mm_f_1_4_Sony_E"])

    @classmethod
    def Samyang_Rokinon_12mm_f_2_0_Sony_E(cls):
        return cls.from_database(cls._DATABASE["Samyang_Rokinon_12mm_f_2_0_Sony_E"])

    @classmethod
    def Samyang_Rokinon_12mm_f_2_0_MFT(cls):
        return cls.from_database(cls._DATABASE["Samyang_Rokinon_12mm_f_2_0_MFT"])

    @classmethod
    def Samyang_Rokinon_12mm_f_2_0_Fuji_X(cls):
        return cls.from_database(cls._DATABASE["Samyang_Rokinon_12mm_f_2_0_Fuji_X"])

    @classmethod
    def Samyang_Rokinon_8mm_f_3_5_Fisheye_EOS(cls):
        return cls.from_database(cls._DATABASE["Samyang_Rokinon_8mm_f_3_5_Fisheye_EOS"])

    @classmethod
    def Samyang_Rokinon_8mm_f_3_5_Fisheye_Nikon_F(cls):
        return cls.from_database(
            cls._DATABASE["Samyang_Rokinon_8mm_f_3_5_Fisheye_Nikon_F"]
        )

    @classmethod
    def Samyang_Rokinon_35mm_f_1_4_EOS(cls):
        return cls.from_database(cls._DATABASE["Samyang_Rokinon_35mm_f_1_4_EOS"])

    @classmethod
    def Samyang_Rokinon_35mm_f_1_4_Sony_E(cls):
        return cls.from_database(cls._DATABASE["Samyang_Rokinon_35mm_f_1_4_Sony_E"])

    @classmethod
    def Samyang_Rokinon_100mm_f_2_8_Macro_EOS(cls):
        return cls.from_database(cls._DATABASE["Samyang_Rokinon_100mm_f_2_8_Macro_EOS"])

    @classmethod
    def Voigtlander_Nokton_25mm_f_0_95_II_MFT(cls):
        return cls.from_database(cls._DATABASE["Voigtlander_Nokton_25mm_f_0_95_II_MFT"])

    @classmethod
    def Voigtlander_Nokton_42_5mm_f_0_95_MFT(cls):
        return cls.from_database(cls._DATABASE["Voigtlander_Nokton_42_5mm_f_0_95_MFT"])

    @classmethod
    def Voigtlander_Macro_APO_Lanthar_65mm_f_2_Sony_E(cls):
        return cls.from_database(
            cls._DATABASE["Voigtlander_Macro_APO_Lanthar_65mm_f_2_Sony_E"]
        )

    @classmethod
    def Voigtlander_Nokton_35mm_f_1_2_Sony_E(cls):
        return cls.from_database(cls._DATABASE["Voigtlander_Nokton_35mm_f_1_2_Sony_E"])

    @classmethod
    def Voigtlander_Nokton_40mm_f_1_2_Sony_E(cls):
        return cls.from_database(cls._DATABASE["Voigtlander_Nokton_40mm_f_1_2_Sony_E"])

    @classmethod
    def Voigtlander_Nokton_50mm_f_1_0_Nikon_Z(cls):
        return cls.from_database(cls._DATABASE["Voigtlander_Nokton_50mm_f_1_0_Nikon_Z"])

    @classmethod
    def Voigtlander_HELIAR_40mm_f_2_8_Sony_E(cls):
        return cls.from_database(cls._DATABASE["Voigtlander_HELIAR_40mm_f_2_8_Sony_E"])

    @classmethod
    def Voigtlander_APO_SKOPAR_90mm_f_2_8_Sony_E(cls):
        return cls.from_database(
            cls._DATABASE["Voigtlander_APO_SKOPAR_90mm_f_2_8_Sony_E"]
        )

    @classmethod
    def Voigtlander_COLOR_SKOPAR_21mm_f_3_5_Sony_E(cls):
        return cls.from_database(
            cls._DATABASE["Voigtlander_COLOR_SKOPAR_21mm_f_3_5_Sony_E"]
        )

    @classmethod
    def Tokina_opera_50mm_f_1_4_EOS(cls):
        return cls.from_database(cls._DATABASE["Tokina_opera_50mm_f_1_4_EOS"])

    @classmethod
    def Tokina_opera_50mm_f_1_4_Nikon_F(cls):
        return cls.from_database(cls._DATABASE["Tokina_opera_50mm_f_1_4_Nikon_F"])

    @classmethod
    def Tokina_AT_X_11_20mm_f_2_8_EOS(cls):
        return cls.from_database(cls._DATABASE["Tokina_AT_X_11_20mm_f_2_8_EOS"])

    @classmethod
    def Tokina_AT_X_11_20mm_f_2_8_Nikon_F(cls):
        return cls.from_database(cls._DATABASE["Tokina_AT_X_11_20mm_f_2_8_Nikon_F"])

    @classmethod
    def Tokina_AT_X_14_20mm_f_2_EOS(cls):
        return cls.from_database(cls._DATABASE["Tokina_AT_X_14_20mm_f_2_EOS"])

    @classmethod
    def Tokina_AT_X_14_20mm_f_2_Nikon_F(cls):
        return cls.from_database(cls._DATABASE["Tokina_AT_X_14_20mm_f_2_Nikon_F"])

    @classmethod
    def Tokina_SZX_400mm_f_8_Reflex(cls):
        return cls.from_database(cls._DATABASE["Tokina_SZX_400mm_f_8_Reflex"])

    @classmethod
    def Tokina_SZ_500mm_f_8_Reflex_Sony_E(cls):
        return cls.from_database(cls._DATABASE["Tokina_SZ_500mm_f_8_Reflex_Sony_E"])

    @classmethod
    def Tokina_atx_m_85mm_f_1_8_Sony_E(cls):
        return cls.from_database(cls._DATABASE["Tokina_atx_m_85mm_f_1_8_Sony_E"])

    @classmethod
    def Tokina_atx_m_33mm_f_1_4_Fuji_X(cls):
        return cls.from_database(cls._DATABASE["Tokina_atx_m_33mm_f_1_4_Fuji_X"])

    @classmethod
    def Tokina_atx_m_23mm_f_1_4_Fuji_X(cls):
        return cls.from_database(cls._DATABASE["Tokina_atx_m_23mm_f_1_4_Fuji_X"])

    @classmethod
    def Tokina_ATX_i_100mm_f_2_8_Macro_EOS(cls):
        return cls.from_database(cls._DATABASE["Tokina_ATX_i_100mm_f_2_8_Macro_EOS"])

    @classmethod
    def ID_7Artisans_35mm_f_0_95_Sony_E(cls):
        return cls.from_database(cls._DATABASE["ID_7Artisans_35mm_f_0_95_Sony_E"])

    @classmethod
    def ID_7Artisans_55mm_f_1_4_Sony_E(cls):
        return cls.from_database(cls._DATABASE["ID_7Artisans_55mm_f_1_4_Sony_E"])

    @classmethod
    def ID_7Artisans_25mm_f_1_8_Sony_E(cls):
        return cls.from_database(cls._DATABASE["ID_7Artisans_25mm_f_1_8_Sony_E"])

    @classmethod
    def ID_7Artisans_35mm_f_1_2_Sony_E(cls):
        return cls.from_database(cls._DATABASE["ID_7Artisans_35mm_f_1_2_Sony_E"])

    @classmethod
    def ID_7Artisans_60mm_f_2_8_Macro_Sony_E(cls):
        return cls.from_database(cls._DATABASE["ID_7Artisans_60mm_f_2_8_Macro_Sony_E"])

    @classmethod
    def ID_7Artisans_12mm_f_2_8_Sony_E(cls):
        return cls.from_database(cls._DATABASE["ID_7Artisans_12mm_f_2_8_Sony_E"])

    @classmethod
    def ID_7Artisans_50mm_f_1_05_Nikon_Z(cls):
        return cls.from_database(cls._DATABASE["ID_7Artisans_50mm_f_1_05_Nikon_Z"])

    @classmethod
    def ID_7Artisans_50mm_f_1_05_Canon_RF(cls):
        return cls.from_database(cls._DATABASE["ID_7Artisans_50mm_f_1_05_Canon_RF"])

    @classmethod
    def ID_7Artisans_35mm_f_0_95_MFT(cls):
        return cls.from_database(cls._DATABASE["ID_7Artisans_35mm_f_0_95_MFT"])

    @classmethod
    def ID_7Artisans_35mm_f_0_95_Fuji_X(cls):
        return cls.from_database(cls._DATABASE["ID_7Artisans_35mm_f_0_95_Fuji_X"])

    @classmethod
    def ID_7Artisans_25mm_f_0_95_MFT(cls):
        return cls.from_database(cls._DATABASE["ID_7Artisans_25mm_f_0_95_MFT"])

    @classmethod
    def ID_7Artisans_55mm_f_1_4_Fuji_X(cls):
        return cls.from_database(cls._DATABASE["ID_7Artisans_55mm_f_1_4_Fuji_X"])

    @classmethod
    def ID_7Artisans_55mm_f_1_4_MFT(cls):
        return cls.from_database(cls._DATABASE["ID_7Artisans_55mm_f_1_4_MFT"])

    @classmethod
    def ID_7Artisans_12mm_f_2_8_EOS(cls):
        return cls.from_database(cls._DATABASE["ID_7Artisans_12mm_f_2_8_EOS"])

    @classmethod
    def Viltrox_85mm_f_1_8_II_Nikon_Z(cls):
        return cls.from_database(cls._DATABASE["Viltrox_85mm_f_1_8_II_Nikon_Z"])

    @classmethod
    def Viltrox_85mm_f_1_8_II_Canon_RF(cls):
        return cls.from_database(cls._DATABASE["Viltrox_85mm_f_1_8_II_Canon_RF"])

    @classmethod
    def Viltrox_85mm_f_1_8_II_Fuji_X(cls):
        return cls.from_database(cls._DATABASE["Viltrox_85mm_f_1_8_II_Fuji_X"])

    @classmethod
    def Viltrox_56mm_f_1_4_Sony_E(cls):
        return cls.from_database(cls._DATABASE["Viltrox_56mm_f_1_4_Sony_E"])

    @classmethod
    def Viltrox_56mm_f_1_4_Fuji_X(cls):
        return cls.from_database(cls._DATABASE["Viltrox_56mm_f_1_4_Fuji_X"])

    @classmethod
    def Viltrox_56mm_f_1_4_Nikon_Z(cls):
        return cls.from_database(cls._DATABASE["Viltrox_56mm_f_1_4_Nikon_Z"])

    @classmethod
    def Viltrox_23mm_f_1_4_Sony_E(cls):
        return cls.from_database(cls._DATABASE["Viltrox_23mm_f_1_4_Sony_E"])

    @classmethod
    def Viltrox_23mm_f_1_4_Fuji_X(cls):
        return cls.from_database(cls._DATABASE["Viltrox_23mm_f_1_4_Fuji_X"])

    @classmethod
    def Viltrox_33mm_f_1_4_Sony_E(cls):
        return cls.from_database(cls._DATABASE["Viltrox_33mm_f_1_4_Sony_E"])

    @classmethod
    def Viltrox_33mm_f_1_4_Fuji_X(cls):
        return cls.from_database(cls._DATABASE["Viltrox_33mm_f_1_4_Fuji_X"])

    @classmethod
    def Viltrox_13mm_f_1_4_Sony_E(cls):
        return cls.from_database(cls._DATABASE["Viltrox_13mm_f_1_4_Sony_E"])

    @classmethod
    def Viltrox_13mm_f_1_4_Fuji_X(cls):
        return cls.from_database(cls._DATABASE["Viltrox_13mm_f_1_4_Fuji_X"])

    @classmethod
    def Viltrox_75mm_f_1_2_Sony_E(cls):
        return cls.from_database(cls._DATABASE["Viltrox_75mm_f_1_2_Sony_E"])

    @classmethod
    def Viltrox_75mm_f_1_2_Fuji_X(cls):
        return cls.from_database(cls._DATABASE["Viltrox_75mm_f_1_2_Fuji_X"])

    @classmethod
    def Viltrox_AF_85mm_f_1_8_EOS(cls):
        return cls.from_database(cls._DATABASE["Viltrox_AF_85mm_f_1_8_EOS"])

    @classmethod
    def Viltrox_AF_56mm_f_1_4_EOS_M(cls):
        return cls.from_database(cls._DATABASE["Viltrox_AF_56mm_f_1_4_EOS_M"])

    @classmethod
    def Viltrox_24mm_f_1_8_Sony_E(cls):
        return cls.from_database(cls._DATABASE["Viltrox_24mm_f_1_8_Sony_E"])

    @classmethod
    def GSO_Dobson_6(cls):
        return cls.from_database(cls._DATABASE["GSO_Dobson_6"])

    @classmethod
    def Orion_IntelliScope_XT6_Dob(cls):
        return cls.from_database(cls._DATABASE["Orion_IntelliScope_XT6_Dob"])

    @classmethod
    def GSO_Dobson_8(cls):
        return cls.from_database(cls._DATABASE["GSO_Dobson_8"])

    @classmethod
    def Orion_IntelliScope_XT8_Dob(cls):
        return cls.from_database(cls._DATABASE["Orion_IntelliScope_XT8_Dob"])

    @classmethod
    def GSO_Dobson_10(cls):
        return cls.from_database(cls._DATABASE["GSO_Dobson_10"])

    @classmethod
    def Orion_IntelliScope_XT10_Dob(cls):
        return cls.from_database(cls._DATABASE["Orion_IntelliScope_XT10_Dob"])

    @classmethod
    def GSO_Dobson_12(cls):
        return cls.from_database(cls._DATABASE["GSO_Dobson_12"])

    @classmethod
    def Orion_IntelliScope_XT12_Dob(cls):
        return cls.from_database(cls._DATABASE["Orion_IntelliScope_XT12_Dob"])

    @classmethod
    def GSO_Dobson_14(cls):
        return cls.from_database(cls._DATABASE["GSO_Dobson_14"])

    @classmethod
    def Orion_IntelliScope_XT14_Dob(cls):
        return cls.from_database(cls._DATABASE["Orion_IntelliScope_XT14_Dob"])

    @classmethod
    def GSO_Dobson_16(cls):
        return cls.from_database(cls._DATABASE["GSO_Dobson_16"])

    @classmethod
    def Orion_IntelliScope_XT16_Dob(cls):
        return cls.from_database(cls._DATABASE["Orion_IntelliScope_XT16_Dob"])

    @classmethod
    def Bresser_Messier_Dobson_6_Truss(cls):
        return cls.from_database(cls._DATABASE["Bresser_Messier_Dobson_6_Truss"])

    @classmethod
    def Bresser_Messier_Dobson_8_Truss(cls):
        return cls.from_database(cls._DATABASE["Bresser_Messier_Dobson_8_Truss"])

    @classmethod
    def Bresser_Messier_Dobson_10_Truss(cls):
        return cls.from_database(cls._DATABASE["Bresser_Messier_Dobson_10_Truss"])

    @classmethod
    def Bresser_Messier_Dobson_12_Truss(cls):
        return cls.from_database(cls._DATABASE["Bresser_Messier_Dobson_12_Truss"])

    @classmethod
    def Bresser_Messier_Dobson_14_Truss(cls):
        return cls.from_database(cls._DATABASE["Bresser_Messier_Dobson_14_Truss"])

    @classmethod
    def Bresser_Messier_Dobson_16_Truss(cls):
        return cls.from_database(cls._DATABASE["Bresser_Messier_Dobson_16_Truss"])

    @classmethod
    def Sky_Watcher_Traditional_Dob_6(cls):
        return cls.from_database(cls._DATABASE["Sky_Watcher_Traditional_Dob_6"])

    @classmethod
    def Sky_Watcher_Traditional_Dob_8(cls):
        return cls.from_database(cls._DATABASE["Sky_Watcher_Traditional_Dob_8"])

    @classmethod
    def Sky_Watcher_Traditional_Dob_10(cls):
        return cls.from_database(cls._DATABASE["Sky_Watcher_Traditional_Dob_10"])

    @classmethod
    def Sky_Watcher_Traditional_Dob_12(cls):
        return cls.from_database(cls._DATABASE["Sky_Watcher_Traditional_Dob_12"])

    @classmethod
    def Celestron_C8_A_XLT_OTA(cls):
        return cls.from_database(cls._DATABASE["Celestron_C8_A_XLT_OTA"])

    @classmethod
    def Celestron_C9_25_A_XLT_OTA(cls):
        return cls.from_database(cls._DATABASE["Celestron_C9_25_A_XLT_OTA"])

    @classmethod
    def Celestron_C11_A_XLT_OTA(cls):
        return cls.from_database(cls._DATABASE["Celestron_C11_A_XLT_OTA"])

    @classmethod
    def Celestron_C14_A_XLT_OTA(cls):
        return cls.from_database(cls._DATABASE["Celestron_C14_A_XLT_OTA"])

    @classmethod
    def Takahashi_Epsilon_160ED(cls):
        return cls.from_database(cls._DATABASE["Takahashi_Epsilon_160ED"])

    @classmethod
    def Takahashi_FS_128(cls):
        return cls.from_database(cls._DATABASE["Takahashi_FS_128"])

    @classmethod
    def Takahashi_Epsilon_130ED(cls):
        return cls.from_database(cls._DATABASE["Takahashi_Epsilon_130ED"])

    @classmethod
    def Omegon_Pro_APO_72_400(cls):
        return cls.from_database(cls._DATABASE["Omegon_Pro_APO_72_400"])

    @classmethod
    def Omegon_Pro_APO_80_500(cls):
        return cls.from_database(cls._DATABASE["Omegon_Pro_APO_80_500"])

    @classmethod
    def Omegon_Pro_APO_100_580(cls):
        return cls.from_database(cls._DATABASE["Omegon_Pro_APO_100_580"])

    @classmethod
    def Omegon_Pro_APO_110_660(cls):
        return cls.from_database(cls._DATABASE["Omegon_Pro_APO_110_660"])

    @classmethod
    def Omegon_Pro_APO_127_793(cls):
        return cls.from_database(cls._DATABASE["Omegon_Pro_APO_127_793"])

    @classmethod
    def Omegon_Pro_APO_152_988(cls):
        return cls.from_database(cls._DATABASE["Omegon_Pro_APO_152_988"])

    @classmethod
    def Omegon_Pro_Newton_200_800_OTA(cls):
        return cls.from_database(cls._DATABASE["Omegon_Pro_Newton_200_800_OTA"])

    @classmethod
    def Omegon_Pro_Newton_250_1000_OTA(cls):
        return cls.from_database(cls._DATABASE["Omegon_Pro_Newton_250_1000_OTA"])

    @classmethod
    def Omegon_Pro_RC_154_1370(cls):
        return cls.from_database(cls._DATABASE["Omegon_Pro_RC_154_1370"])

    @classmethod
    def Omegon_Pro_RC_203_1624(cls):
        return cls.from_database(cls._DATABASE["Omegon_Pro_RC_203_1624"])

    @classmethod
    def Omegon_Pro_RC_254_2000(cls):
        return cls.from_database(cls._DATABASE["Omegon_Pro_RC_254_2000"])

    @classmethod
    def Omegon_Pro_RC_304_2432(cls):
        return cls.from_database(cls._DATABASE["Omegon_Pro_RC_304_2432"])

    @classmethod
    def Omegon_Pro_RC_355_2845(cls):
        return cls.from_database(cls._DATABASE["Omegon_Pro_RC_355_2845"])

    @classmethod
    def TS_Optics_CF_APO_65mm_Quintuplet(cls):
        return cls.from_database(cls._DATABASE["TS_Optics_CF_APO_65mm_Quintuplet"])

    @classmethod
    def TS_Optics_CF_APO_90mm(cls):
        return cls.from_database(cls._DATABASE["TS_Optics_CF_APO_90mm"])

    @classmethod
    def TS_Optics_RC_6_Pro(cls):
        return cls.from_database(cls._DATABASE["TS_Optics_RC_6_Pro"])

    @classmethod
    def TS_Optics_RC_8_Pro(cls):
        return cls.from_database(cls._DATABASE["TS_Optics_RC_8_Pro"])

    @classmethod
    def TS_Optics_RC_10_Pro(cls):
        return cls.from_database(cls._DATABASE["TS_Optics_RC_10_Pro"])

    @classmethod
    def TS_Optics_RC_12_Pro(cls):
        return cls.from_database(cls._DATABASE["TS_Optics_RC_12_Pro"])

    @classmethod
    def TS_Optics_ONTC_12_f_4(cls):
        return cls.from_database(cls._DATABASE["TS_Optics_ONTC_12_f_4"])

    @classmethod
    def TS_Optics_ONTC_14_f_4(cls):
        return cls.from_database(cls._DATABASE["TS_Optics_ONTC_14_f_4"])

    @classmethod
    def TS_Optics_ONTC_16_f_4(cls):
        return cls.from_database(cls._DATABASE["TS_Optics_ONTC_16_f_4"])

    @classmethod
    def TS_Optics_Individual_80mm_Quad(cls):
        return cls.from_database(cls._DATABASE["TS_Optics_Individual_80mm_Quad"])

    @classmethod
    def TS_Optics_Individual_102mm_Quad(cls):
        return cls.from_database(cls._DATABASE["TS_Optics_Individual_102mm_Quad"])

    @classmethod
    def TS_Optics_Individual_115mm_Quad(cls):
        return cls.from_database(cls._DATABASE["TS_Optics_Individual_115mm_Quad"])

    @classmethod
    def TS_Optics_Photoline_152mm_APO(cls):
        return cls.from_database(cls._DATABASE["TS_Optics_Photoline_152mm_APO"])

    @classmethod
    def Celestron_C6_A_XLT_OTA(cls):
        return cls.from_database(cls._DATABASE["Celestron_C6_A_XLT_OTA"])

    @classmethod
    def Celestron_C5_OTA_XLT(cls):
        return cls.from_database(cls._DATABASE["Celestron_C5_OTA_XLT"])

    @classmethod
    def Celestron_C6_OTA(cls):
        return cls.from_database(cls._DATABASE["Celestron_C6_OTA"])

    @classmethod
    def Celestron_C8_OTA(cls):
        return cls.from_database(cls._DATABASE["Celestron_C8_OTA"])

    @classmethod
    def Celestron_C9_25_OTA(cls):
        return cls.from_database(cls._DATABASE["Celestron_C9_25_OTA"])

    @classmethod
    def Celestron_C11_OTA(cls):
        return cls.from_database(cls._DATABASE["Celestron_C11_OTA"])

    @classmethod
    def Celestron_C14_OTA(cls):
        return cls.from_database(cls._DATABASE["Celestron_C14_OTA"])

    @classmethod
    def Celestron_C6_EdgeHD_OTA(cls):
        return cls.from_database(cls._DATABASE["Celestron_C6_EdgeHD_OTA"])

    @classmethod
    def Celestron_C8_EdgeHD_OTA(cls):
        return cls.from_database(cls._DATABASE["Celestron_C8_EdgeHD_OTA"])

    @classmethod
    def Celestron_C9_25_EdgeHD_OTA(cls):
        return cls.from_database(cls._DATABASE["Celestron_C9_25_EdgeHD_OTA"])

    @classmethod
    def Celestron_C11_EdgeHD_OTA(cls):
        return cls.from_database(cls._DATABASE["Celestron_C11_EdgeHD_OTA"])

    @classmethod
    def Celestron_C14_EdgeHD_OTA(cls):
        return cls.from_database(cls._DATABASE["Celestron_C14_EdgeHD_OTA"])

    @classmethod
    def Sky_Watcher_SkyMax_90(cls):
        return cls.from_database(cls._DATABASE["Sky_Watcher_SkyMax_90"])

    @classmethod
    def Sky_Watcher_SkyMax_102_AZ_GTi(cls):
        return cls.from_database(cls._DATABASE["Sky_Watcher_SkyMax_102_AZ_GTi"])

    @classmethod
    def Sky_Watcher_SkyMax_127_AZ_GTi(cls):
        return cls.from_database(cls._DATABASE["Sky_Watcher_SkyMax_127_AZ_GTi"])

    @classmethod
    def Sky_Watcher_Star_Discovery_150P(cls):
        return cls.from_database(cls._DATABASE["Sky_Watcher_Star_Discovery_150P"])

    @classmethod
    def Sky_Watcher_Star_Discovery_200P(cls):
        return cls.from_database(cls._DATABASE["Sky_Watcher_Star_Discovery_200P"])

    @classmethod
    def Sky_Watcher_AZ_EQ5_GT_8_Newton(cls):
        return cls.from_database(cls._DATABASE["Sky_Watcher_AZ_EQ5_GT_8_Newton"])

    @classmethod
    def Sky_Watcher_AZ_EQ6_Pro_8_Newton(cls):
        return cls.from_database(cls._DATABASE["Sky_Watcher_AZ_EQ6_Pro_8_Newton"])

    @classmethod
    def Sky_Watcher_Black_Diamond_ED80(cls):
        return cls.from_database(cls._DATABASE["Sky_Watcher_Black_Diamond_ED80"])

    @classmethod
    def Sky_Watcher_Black_Diamond_ED100(cls):
        return cls.from_database(cls._DATABASE["Sky_Watcher_Black_Diamond_ED100"])

    @classmethod
    def Sky_Watcher_Black_Diamond_ED120(cls):
        return cls.from_database(cls._DATABASE["Sky_Watcher_Black_Diamond_ED120"])

    @classmethod
    def Orion_SpaceProbe_114ST_EQ(cls):
        return cls.from_database(cls._DATABASE["Orion_SpaceProbe_114ST_EQ"])

    @classmethod
    def Orion_StarMax_90mm_Mak(cls):
        return cls.from_database(cls._DATABASE["Orion_StarMax_90mm_Mak"])

    @classmethod
    def Orion_StarMax_127mm_Mak(cls):
        return cls.from_database(cls._DATABASE["Orion_StarMax_127mm_Mak"])

    @classmethod
    def Orion_StarMax_102mm_Mak(cls):
        return cls.from_database(cls._DATABASE["Orion_StarMax_102mm_Mak"])

    @classmethod
    def Orion_AstroView_90mm_EQ(cls):
        return cls.from_database(cls._DATABASE["Orion_AstroView_90mm_EQ"])

    @classmethod
    def Orion_AstroView_120mm_EQ(cls):
        return cls.from_database(cls._DATABASE["Orion_AstroView_120mm_EQ"])

    @classmethod
    def Orion_SkyQuest_XX8g_Dob(cls):
        return cls.from_database(cls._DATABASE["Orion_SkyQuest_XX8g_Dob"])

    @classmethod
    def Orion_SkyQuest_XT4_5_Classic_Dob(cls):
        return cls.from_database(cls._DATABASE["Orion_SkyQuest_XT4_5_Classic_Dob"])

    @classmethod
    def Orion_GoScope_80_Refractor(cls):
        return cls.from_database(cls._DATABASE["Orion_GoScope_80_Refractor"])

    @classmethod
    def Orion_ShortTube_80_Refractor(cls):
        return cls.from_database(cls._DATABASE["Orion_ShortTube_80_Refractor"])

    @classmethod
    def Orion_CT80_Refractor_OTA(cls):
        return cls.from_database(cls._DATABASE["Orion_CT80_Refractor_OTA"])

    @classmethod
    def Orion_ED80T_CF_OTA(cls):
        return cls.from_database(cls._DATABASE["Orion_ED80T_CF_OTA"])

    @classmethod
    def Bresser_Lyra_150_1200_EQ3(cls):
        return cls.from_database(cls._DATABASE["Bresser_Lyra_150_1200_EQ3"])

    @classmethod
    def Bresser_Solarix_76_350_AZ(cls):
        return cls.from_database(cls._DATABASE["Bresser_Solarix_76_350_AZ"])

    @classmethod
    def Bresser_Pollux_150_750_EQ3(cls):
        return cls.from_database(cls._DATABASE["Bresser_Pollux_150_750_EQ3"])

    @classmethod
    def Bresser_National_Geographic_114_500_AZ(cls):
        return cls.from_database(
            cls._DATABASE["Bresser_National_Geographic_114_500_AZ"]
        )

    @classmethod
    def Bresser_National_Geographic_90_1250_Mak(cls):
        return cls.from_database(
            cls._DATABASE["Bresser_National_Geographic_90_1250_Mak"]
        )

    @classmethod
    def Bresser_National_Geographic_130_650_EQ(cls):
        return cls.from_database(
            cls._DATABASE["Bresser_National_Geographic_130_650_EQ"]
        )

    @classmethod
    def Bresser_FirstLight_152_1200_EQ3(cls):
        return cls.from_database(cls._DATABASE["Bresser_FirstLight_152_1200_EQ3"])

    @classmethod
    def Bresser_FirstLight_102_460_Table_Dob(cls):
        return cls.from_database(cls._DATABASE["Bresser_FirstLight_102_460_Table_Dob"])

    @classmethod
    def Meade_ETX_105(cls):
        return cls.from_database(cls._DATABASE["Meade_ETX_105"])

    @classmethod
    def Meade_ETX_80_AT(cls):
        return cls.from_database(cls._DATABASE["Meade_ETX_80_AT"])

    @classmethod
    def Meade_Infinity_70mm_AZ(cls):
        return cls.from_database(cls._DATABASE["Meade_Infinity_70mm_AZ"])

    @classmethod
    def Meade_Infinity_80mm_AZ(cls):
        return cls.from_database(cls._DATABASE["Meade_Infinity_80mm_AZ"])

    @classmethod
    def Meade_Infinity_90mm_AZ(cls):
        return cls.from_database(cls._DATABASE["Meade_Infinity_90mm_AZ"])

    @classmethod
    def Meade_Infinity_102mm_AZ(cls):
        return cls.from_database(cls._DATABASE["Meade_Infinity_102mm_AZ"])

    @classmethod
    def Meade_Polaris_114mm_EQ(cls):
        return cls.from_database(cls._DATABASE["Meade_Polaris_114mm_EQ"])

    @classmethod
    def Meade_Polaris_70mm_EQ(cls):
        return cls.from_database(cls._DATABASE["Meade_Polaris_70mm_EQ"])

    @classmethod
    def Meade_Polaris_90mm_EQ(cls):
        return cls.from_database(cls._DATABASE["Meade_Polaris_90mm_EQ"])

    @classmethod
    def Meade_Polaris_80mm_EQ(cls):
        return cls.from_database(cls._DATABASE["Meade_Polaris_80mm_EQ"])

    @classmethod
    def Vixen_ED80Sf(cls):
        return cls.from_database(cls._DATABASE["Vixen_ED80Sf"])

    @classmethod
    def Vixen_ED81SII(cls):
        return cls.from_database(cls._DATABASE["Vixen_ED81SII"])

    @classmethod
    def Vixen_ED103S(cls):
        return cls.from_database(cls._DATABASE["Vixen_ED103S"])

    @classmethod
    def Vixen_ED115S_v2(cls):
        return cls.from_database(cls._DATABASE["Vixen_ED115S_v2"])

    @classmethod
    def Vixen_NA140SSf(cls):
        return cls.from_database(cls._DATABASE["Vixen_NA140SSf"])

    @classmethod
    def Vixen_VC200L_v2(cls):
        return cls.from_database(cls._DATABASE["Vixen_VC200L_v2"])

    @classmethod
    def Vixen_VMC200L_v2(cls):
        return cls.from_database(cls._DATABASE["Vixen_VMC200L_v2"])

    @classmethod
    def Vixen_R200SS_v2(cls):
        return cls.from_database(cls._DATABASE["Vixen_R200SS_v2"])

    @classmethod
    def Explore_Scientific_FirstLight_90mm_Mak(cls):
        return cls.from_database(
            cls._DATABASE["Explore_Scientific_FirstLight_90mm_Mak"]
        )

    @classmethod
    def Explore_Scientific_FirstLight_114mm_Newton(cls):
        return cls.from_database(
            cls._DATABASE["Explore_Scientific_FirstLight_114mm_Newton"]
        )

    @classmethod
    def Explore_Scientific_FirstLight_130mm_Newton(cls):
        return cls.from_database(
            cls._DATABASE["Explore_Scientific_FirstLight_130mm_Newton"]
        )

    @classmethod
    def Explore_Scientific_FirstLight_152mm_Newton(cls):
        return cls.from_database(
            cls._DATABASE["Explore_Scientific_FirstLight_152mm_Newton"]
        )

    @classmethod
    def Explore_Scientific_StarGate_18_Truss_Dob(cls):
        return cls.from_database(
            cls._DATABASE["Explore_Scientific_StarGate_18_Truss_Dob"]
        )

    @classmethod
    def Explore_Scientific_StarGate_20_Truss_Dob(cls):
        return cls.from_database(
            cls._DATABASE["Explore_Scientific_StarGate_20_Truss_Dob"]
        )

    @classmethod
    def Explore_Scientific_ED165_FCD100_CF(cls):
        return cls.from_database(cls._DATABASE["Explore_Scientific_ED165_FCD100_CF"])

    @classmethod
    def Explore_Scientific_ED127_FCD1_CF(cls):
        return cls.from_database(cls._DATABASE["Explore_Scientific_ED127_FCD1_CF"])

    @classmethod
    def William_Optics_RedCat_71(cls):
        return cls.from_database(cls._DATABASE["William_Optics_RedCat_71"])

    @classmethod
    def William_Optics_SpaceCat_51_v2(cls):
        return cls.from_database(cls._DATABASE["William_Optics_SpaceCat_51_v2"])

    @classmethod
    def William_Optics_WhiteCat_71(cls):
        return cls.from_database(cls._DATABASE["William_Optics_WhiteCat_71"])

    @classmethod
    def William_Optics_GT71_v2(cls):
        return cls.from_database(cls._DATABASE["William_Optics_GT71_v2"])

    @classmethod
    def William_Optics_GT81_v2(cls):
        return cls.from_database(cls._DATABASE["William_Optics_GT81_v2"])

    @classmethod
    def William_Optics_GT102_v2(cls):
        return cls.from_database(cls._DATABASE["William_Optics_GT102_v2"])

    @classmethod
    def William_Optics_ZenithStar_61_III(cls):
        return cls.from_database(cls._DATABASE["William_Optics_ZenithStar_61_III"])

    @classmethod
    def William_Optics_ZenithStar_73_v2(cls):
        return cls.from_database(cls._DATABASE["William_Optics_ZenithStar_73_v2"])

    @classmethod
    def William_Optics_ZenithStar_81_v2(cls):
        return cls.from_database(cls._DATABASE["William_Optics_ZenithStar_81_v2"])

    @classmethod
    def William_Optics_Pleiades_68_v2(cls):
        return cls.from_database(cls._DATABASE["William_Optics_Pleiades_68_v2"])

    @classmethod
    def William_Optics_FluoroStar_91_v2(cls):
        return cls.from_database(cls._DATABASE["William_Optics_FluoroStar_91_v2"])

    @classmethod
    def William_Optics_FluoroStar_132_v2(cls):
        return cls.from_database(cls._DATABASE["William_Optics_FluoroStar_132_v2"])

    @classmethod
    def Askar_FRA300_Pro_v2(cls):
        return cls.from_database(cls._DATABASE["Askar_FRA300_Pro_v2"])

    @classmethod
    def Askar_FRA400_v2(cls):
        return cls.from_database(cls._DATABASE["Askar_FRA400_v2"])

    @classmethod
    def Askar_FRA500_v2(cls):
        return cls.from_database(cls._DATABASE["Askar_FRA500_v2"])

    @classmethod
    def Askar_FRA600_v2(cls):
        return cls.from_database(cls._DATABASE["Askar_FRA600_v2"])

    @classmethod
    def Askar_65PHQ_v2(cls):
        return cls.from_database(cls._DATABASE["Askar_65PHQ_v2"])

    @classmethod
    def Askar_80PHQ_v2(cls):
        return cls.from_database(cls._DATABASE["Askar_80PHQ_v2"])

    @classmethod
    def Askar_107PHQ_v2(cls):
        return cls.from_database(cls._DATABASE["Askar_107PHQ_v2"])

    @classmethod
    def Askar_130PHQ_v2(cls):
        return cls.from_database(cls._DATABASE["Askar_130PHQ_v2"])

    @classmethod
    def Askar_151PHQ_v2(cls):
        return cls.from_database(cls._DATABASE["Askar_151PHQ_v2"])

    @classmethod
    def Askar_V_60Q_v2(cls):
        return cls.from_database(cls._DATABASE["Askar_V_60Q_v2"])

    @classmethod
    def Askar_V_80Q_v2(cls):
        return cls.from_database(cls._DATABASE["Askar_V_80Q_v2"])

    @classmethod
    def Askar_FMA_230_v2(cls):
        return cls.from_database(cls._DATABASE["Askar_FMA_230_v2"])

    @classmethod
    def Askar_200APO_v2(cls):
        return cls.from_database(cls._DATABASE["Askar_200APO_v2"])

    @classmethod
    def Askar_71Q(cls):
        return cls.from_database(cls._DATABASE["Askar_71Q"])

    @classmethod
    def Askar_55Q(cls):
        return cls.from_database(cls._DATABASE["Askar_55Q"])

    @classmethod
    def Sharpstar_61EDPH_III(cls):
        return cls.from_database(cls._DATABASE["Sharpstar_61EDPH_III"])

    @classmethod
    def Sharpstar_76EDPH_III(cls):
        return cls.from_database(cls._DATABASE["Sharpstar_76EDPH_III"])

    @classmethod
    def Sharpstar_94EDPH_III(cls):
        return cls.from_database(cls._DATABASE["Sharpstar_94EDPH_III"])

    @classmethod
    def Sharpstar_100Q(cls):
        return cls.from_database(cls._DATABASE["Sharpstar_100Q"])

    @classmethod
    def Sharpstar_120Q(cls):
        return cls.from_database(cls._DATABASE["Sharpstar_120Q"])

    @classmethod
    def Sharpstar_140PH_v2(cls):
        return cls.from_database(cls._DATABASE["Sharpstar_140PH_v2"])

    @classmethod
    def Sharpstar_15028HNT_v2(cls):
        return cls.from_database(cls._DATABASE["Sharpstar_15028HNT_v2"])

    @classmethod
    def Sharpstar_20032HNT_v2(cls):
        return cls.from_database(cls._DATABASE["Sharpstar_20032HNT_v2"])

    @classmethod
    def Stellarvue_SV48_Access(cls):
        return cls.from_database(cls._DATABASE["Stellarvue_SV48_Access"])

    @classmethod
    def Stellarvue_SV60EDS_v2(cls):
        return cls.from_database(cls._DATABASE["Stellarvue_SV60EDS_v2"])

    @classmethod
    def Stellarvue_SV70T_v2(cls):
        return cls.from_database(cls._DATABASE["Stellarvue_SV70T_v2"])

    @classmethod
    def Stellarvue_SVX080T_v2(cls):
        return cls.from_database(cls._DATABASE["Stellarvue_SVX080T_v2"])

    @classmethod
    def Stellarvue_SVX090T_v2(cls):
        return cls.from_database(cls._DATABASE["Stellarvue_SVX090T_v2"])

    @classmethod
    def Stellarvue_SVX102T_v2(cls):
        return cls.from_database(cls._DATABASE["Stellarvue_SVX102T_v2"])

    @classmethod
    def Stellarvue_SVX130T_v2(cls):
        return cls.from_database(cls._DATABASE["Stellarvue_SVX130T_v2"])

    @classmethod
    def Stellarvue_SVX152T_v2(cls):
        return cls.from_database(cls._DATABASE["Stellarvue_SVX152T_v2"])

    @classmethod
    def Stellarvue_SVX070T_Raptor(cls):
        return cls.from_database(cls._DATABASE["Stellarvue_SVX070T_Raptor"])

    @classmethod
    def Irix_150mm_f_2_8_Macro_EOS(cls):
        return cls.from_database(cls._DATABASE["Irix_150mm_f_2_8_Macro_EOS"])

    @classmethod
    def Irix_150mm_f_2_8_Macro_Nikon_F(cls):
        return cls.from_database(cls._DATABASE["Irix_150mm_f_2_8_Macro_Nikon_F"])

    @classmethod
    def Irix_11mm_f_4_Firefly_EOS(cls):
        return cls.from_database(cls._DATABASE["Irix_11mm_f_4_Firefly_EOS"])

    @classmethod
    def Irix_11mm_f_4_Firefly_Nikon_F(cls):
        return cls.from_database(cls._DATABASE["Irix_11mm_f_4_Firefly_Nikon_F"])

    @classmethod
    def Irix_15mm_f_2_4_Blackstone_EOS(cls):
        return cls.from_database(cls._DATABASE["Irix_15mm_f_2_4_Blackstone_EOS"])

    @classmethod
    def Irix_15mm_f_2_4_Blackstone_Nikon_F(cls):
        return cls.from_database(cls._DATABASE["Irix_15mm_f_2_4_Blackstone_Nikon_F"])

    @classmethod
    def Irix_45mm_f_1_4_EOS(cls):
        return cls.from_database(cls._DATABASE["Irix_45mm_f_1_4_EOS"])

    @classmethod
    def Irix_45mm_f_1_4_Nikon_F(cls):
        return cls.from_database(cls._DATABASE["Irix_45mm_f_1_4_Nikon_F"])

    @classmethod
    def Irix_45mm_f_1_4_Sony_E(cls):
        return cls.from_database(cls._DATABASE["Irix_45mm_f_1_4_Sony_E"])

    @classmethod
    def Laowa_15mm_f_2_Zero_D_EOS(cls):
        return cls.from_database(cls._DATABASE["Laowa_15mm_f_2_Zero_D_EOS"])

    @classmethod
    def Laowa_15mm_f_2_Zero_D_Sony_E(cls):
        return cls.from_database(cls._DATABASE["Laowa_15mm_f_2_Zero_D_Sony_E"])

    @classmethod
    def Laowa_15mm_f_2_Zero_D_Nikon_Z(cls):
        return cls.from_database(cls._DATABASE["Laowa_15mm_f_2_Zero_D_Nikon_Z"])

    @classmethod
    def Laowa_15mm_f_2_Zero_D_Canon_RF(cls):
        return cls.from_database(cls._DATABASE["Laowa_15mm_f_2_Zero_D_Canon_RF"])

    @classmethod
    def Laowa_100mm_f_2_8_2_1_Macro_EOS(cls):
        return cls.from_database(cls._DATABASE["Laowa_100mm_f_2_8_2_1_Macro_EOS"])

    @classmethod
    def Laowa_100mm_f_2_8_2_1_Macro_Sony_E(cls):
        return cls.from_database(cls._DATABASE["Laowa_100mm_f_2_8_2_1_Macro_Sony_E"])

    @classmethod
    def Laowa_10_18mm_f_4_5_5_6_Sony_E(cls):
        return cls.from_database(cls._DATABASE["Laowa_10_18mm_f_4_5_5_6_Sony_E"])

    @classmethod
    def Laowa_10_18mm_f_4_5_5_6_Nikon_Z(cls):
        return cls.from_database(cls._DATABASE["Laowa_10_18mm_f_4_5_5_6_Nikon_Z"])

    @classmethod
    def Laowa_12mm_f_2_8_Zero_D_EOS(cls):
        return cls.from_database(cls._DATABASE["Laowa_12mm_f_2_8_Zero_D_EOS"])

    @classmethod
    def Laowa_12mm_f_2_8_Zero_D_Sony_E(cls):
        return cls.from_database(cls._DATABASE["Laowa_12mm_f_2_8_Zero_D_Sony_E"])

    @classmethod
    def Laowa_9mm_f_2_8_Zero_D_MFT(cls):
        return cls.from_database(cls._DATABASE["Laowa_9mm_f_2_8_Zero_D_MFT"])

    @classmethod
    def Laowa_9mm_f_2_8_Zero_D_Fuji_X(cls):
        return cls.from_database(cls._DATABASE["Laowa_9mm_f_2_8_Zero_D_Fuji_X"])

    @classmethod
    def Laowa_9mm_f_5_6_FF_RL_Sony_E(cls):
        return cls.from_database(cls._DATABASE["Laowa_9mm_f_5_6_FF_RL_Sony_E"])

    @classmethod
    def Laowa_9mm_f_5_6_FF_RL_Nikon_Z(cls):
        return cls.from_database(cls._DATABASE["Laowa_9mm_f_5_6_FF_RL_Nikon_Z"])

    @classmethod
    def Laowa_14mm_f_4_Zero_D_Sony_E(cls):
        return cls.from_database(cls._DATABASE["Laowa_14mm_f_4_Zero_D_Sony_E"])

    @classmethod
    def Laowa_14mm_f_4_Zero_D_Nikon_Z(cls):
        return cls.from_database(cls._DATABASE["Laowa_14mm_f_4_Zero_D_Nikon_Z"])

    @classmethod
    def Laowa_24mm_f_14_Probe_EOS(cls):
        return cls.from_database(cls._DATABASE["Laowa_24mm_f_14_Probe_EOS"])

    @classmethod
    def Laowa_65mm_f_2_8_2x_Macro_Sony_E(cls):
        return cls.from_database(cls._DATABASE["Laowa_65mm_f_2_8_2x_Macro_Sony_E"])

    @classmethod
    def Laowa_85mm_f_5_6_2x_Macro_Sony_E(cls):
        return cls.from_database(cls._DATABASE["Laowa_85mm_f_5_6_2x_Macro_Sony_E"])

    @classmethod
    def Meike_85mm_f_1_8_Sony_E(cls):
        return cls.from_database(cls._DATABASE["Meike_85mm_f_1_8_Sony_E"])

    @classmethod
    def Meike_85mm_f_1_8_Fuji_X(cls):
        return cls.from_database(cls._DATABASE["Meike_85mm_f_1_8_Fuji_X"])

    @classmethod
    def Meike_85mm_f_1_8_Nikon_Z(cls):
        return cls.from_database(cls._DATABASE["Meike_85mm_f_1_8_Nikon_Z"])

    @classmethod
    def Meike_85mm_f_1_8_Canon_RF(cls):
        return cls.from_database(cls._DATABASE["Meike_85mm_f_1_8_Canon_RF"])

    @classmethod
    def Meike_25mm_f_1_8_Sony_E(cls):
        return cls.from_database(cls._DATABASE["Meike_25mm_f_1_8_Sony_E"])

    @classmethod
    def Meike_25mm_f_1_8_MFT(cls):
        return cls.from_database(cls._DATABASE["Meike_25mm_f_1_8_MFT"])

    @classmethod
    def Meike_25mm_f_1_8_Fuji_X(cls):
        return cls.from_database(cls._DATABASE["Meike_25mm_f_1_8_Fuji_X"])

    @classmethod
    def Meike_50mm_f_1_7_Sony_E(cls):
        return cls.from_database(cls._DATABASE["Meike_50mm_f_1_7_Sony_E"])

    @classmethod
    def Meike_50mm_f_1_7_Fuji_X(cls):
        return cls.from_database(cls._DATABASE["Meike_50mm_f_1_7_Fuji_X"])

    @classmethod
    def Meike_35mm_f_1_7_Sony_E(cls):
        return cls.from_database(cls._DATABASE["Meike_35mm_f_1_7_Sony_E"])

    @classmethod
    def Meike_6_5mm_f_2_0_Circular_Fisheye_MFT(cls):
        return cls.from_database(
            cls._DATABASE["Meike_6_5mm_f_2_0_Circular_Fisheye_MFT"]
        )

    @classmethod
    def TTArtisan_50mm_f_1_4_Sony_E(cls):
        return cls.from_database(cls._DATABASE["TTArtisan_50mm_f_1_4_Sony_E"])

    @classmethod
    def TTArtisan_50mm_f_1_4_Fuji_X(cls):
        return cls.from_database(cls._DATABASE["TTArtisan_50mm_f_1_4_Fuji_X"])

    @classmethod
    def TTArtisan_50mm_f_1_4_Nikon_Z(cls):
        return cls.from_database(cls._DATABASE["TTArtisan_50mm_f_1_4_Nikon_Z"])

    @classmethod
    def TTArtisan_35mm_f_1_4_Sony_E(cls):
        return cls.from_database(cls._DATABASE["TTArtisan_35mm_f_1_4_Sony_E"])

    @classmethod
    def TTArtisan_35mm_f_1_4_Fuji_X(cls):
        return cls.from_database(cls._DATABASE["TTArtisan_35mm_f_1_4_Fuji_X"])

    @classmethod
    def TTArtisan_35mm_f_1_4_Nikon_Z(cls):
        return cls.from_database(cls._DATABASE["TTArtisan_35mm_f_1_4_Nikon_Z"])

    @classmethod
    def TTArtisan_23mm_f_1_4_Fuji_X(cls):
        return cls.from_database(cls._DATABASE["TTArtisan_23mm_f_1_4_Fuji_X"])

    @classmethod
    def TTArtisan_23mm_f_1_4_Sony_E(cls):
        return cls.from_database(cls._DATABASE["TTArtisan_23mm_f_1_4_Sony_E"])

    @classmethod
    def TTArtisan_17mm_f_1_4_MFT(cls):
        return cls.from_database(cls._DATABASE["TTArtisan_17mm_f_1_4_MFT"])

    @classmethod
    def TTArtisan_21mm_f_1_5_Sony_E(cls):
        return cls.from_database(cls._DATABASE["TTArtisan_21mm_f_1_5_Sony_E"])

    @classmethod
    def TTArtisan_90mm_f_1_25_Sony_E(cls):
        return cls.from_database(cls._DATABASE["TTArtisan_90mm_f_1_25_Sony_E"])

    @classmethod
    def TTArtisan_11mm_f_2_8_Fisheye_Sony_E(cls):
        return cls.from_database(cls._DATABASE["TTArtisan_11mm_f_2_8_Fisheye_Sony_E"])

    @classmethod
    def TTArtisan_27mm_f_2_8_Sony_E(cls):
        return cls.from_database(cls._DATABASE["TTArtisan_27mm_f_2_8_Sony_E"])

    @classmethod
    def TTArtisan_27mm_f_2_8_Fuji_X(cls):
        return cls.from_database(cls._DATABASE["TTArtisan_27mm_f_2_8_Fuji_X"])

    @classmethod
    def TTArtisan_27mm_f_2_8_Nikon_Z(cls):
        return cls.from_database(cls._DATABASE["TTArtisan_27mm_f_2_8_Nikon_Z"])

    @classmethod
    def TTArtisan_50mm_f_2_Sony_E(cls):
        return cls.from_database(cls._DATABASE["TTArtisan_50mm_f_2_Sony_E"])

    @classmethod
    def TTArtisan_50mm_f_2_Nikon_Z(cls):
        return cls.from_database(cls._DATABASE["TTArtisan_50mm_f_2_Nikon_Z"])

    @classmethod
    def TTArtisan_35mm_f_0_95_MFT(cls):
        return cls.from_database(cls._DATABASE["TTArtisan_35mm_f_0_95_MFT"])

    @classmethod
    def TTArtisan_50mm_f_0_95_Sony_E(cls):
        return cls.from_database(cls._DATABASE["TTArtisan_50mm_f_0_95_Sony_E"])

    @classmethod
    def Mitakon_85mm_f_1_2_Sony_E(cls):
        return cls.from_database(cls._DATABASE["Mitakon_85mm_f_1_2_Sony_E"])

    @classmethod
    def Mitakon_85mm_f_1_2_EOS(cls):
        return cls.from_database(cls._DATABASE["Mitakon_85mm_f_1_2_EOS"])

    @classmethod
    def Mitakon_85mm_f_1_2_Nikon_F(cls):
        return cls.from_database(cls._DATABASE["Mitakon_85mm_f_1_2_Nikon_F"])

    @classmethod
    def Mitakon_50mm_f_0_95_Sony_E(cls):
        return cls.from_database(cls._DATABASE["Mitakon_50mm_f_0_95_Sony_E"])

    @classmethod
    def Mitakon_50mm_f_0_95_Nikon_Z(cls):
        return cls.from_database(cls._DATABASE["Mitakon_50mm_f_0_95_Nikon_Z"])

    @classmethod
    def Mitakon_35mm_f_0_95_Sony_E(cls):
        return cls.from_database(cls._DATABASE["Mitakon_35mm_f_0_95_Sony_E"])

    @classmethod
    def Mitakon_35mm_f_0_95_MFT(cls):
        return cls.from_database(cls._DATABASE["Mitakon_35mm_f_0_95_MFT"])

    @classmethod
    def Mitakon_35mm_f_0_95_Fuji_X(cls):
        return cls.from_database(cls._DATABASE["Mitakon_35mm_f_0_95_Fuji_X"])

    @classmethod
    def Mitakon_20mm_f_2_4_5x_Macro_Sony_E(cls):
        return cls.from_database(cls._DATABASE["Mitakon_20mm_f_2_4_5x_Macro_Sony_E"])

    @classmethod
    def Canon_EF_S_35mm_f_2_8_Macro_IS_STM(cls):
        return cls.from_database(cls._DATABASE["Canon_EF_S_35mm_f_2_8_Macro_IS_STM"])

    @classmethod
    def Canon_EF_S_60mm_f_2_8_Macro_USM(cls):
        return cls.from_database(cls._DATABASE["Canon_EF_S_60mm_f_2_8_Macro_USM"])

    @classmethod
    def Canon_RF_35mm_f_1_8_Macro_IS_STM(cls):
        return cls.from_database(cls._DATABASE["Canon_RF_35mm_f_1_8_Macro_IS_STM"])

    @classmethod
    def Canon_MP_E_65mm_f_2_8_1_5x_Macro(cls):
        return cls.from_database(cls._DATABASE["Canon_MP_E_65mm_f_2_8_1_5x_Macro"])

    @classmethod
    def Nikon_Z_MC_105mm_f_2_8_VR_S(cls):
        return cls.from_database(cls._DATABASE["Nikon_Z_MC_105mm_f_2_8_VR_S"])

    @classmethod
    def Nikon_Z_MC_50mm_f_2_8(cls):
        return cls.from_database(cls._DATABASE["Nikon_Z_MC_50mm_f_2_8"])

    @classmethod
    def Nikon_AF_S_Micro_105mm_f_2_8G_VR(cls):
        return cls.from_database(cls._DATABASE["Nikon_AF_S_Micro_105mm_f_2_8G_VR"])

    @classmethod
    def Sony_FE_90mm_f_2_8_Macro_G_OSS(cls):
        return cls.from_database(cls._DATABASE["Sony_FE_90mm_f_2_8_Macro_G_OSS"])

    @classmethod
    def Sony_FE_50mm_f_2_8_Macro(cls):
        return cls.from_database(cls._DATABASE["Sony_FE_50mm_f_2_8_Macro"])
