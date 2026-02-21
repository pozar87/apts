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
    ):
        super(Telescope, self).__init__(focal_length, vendor, mass=mass, optical_length=optical_length)
        self.aperture = aperture * get_unit_registry().mm
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
        :return: range in magnitude
        """
        return 7.7 + 5 * numpy.log10(self.aperture.to("cm").magnitude)

    def light_grasp_ratio(self, other_aperture):
        """
        Calculate the light grasp ratio between two telescopes.
        :param other_aperture: aperture in mm
        :return: ratio between telescope and other aperture
        """
        other_aperture *= get_unit_registry().mm
        return self.aperture**2 / other_aperture**2

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
