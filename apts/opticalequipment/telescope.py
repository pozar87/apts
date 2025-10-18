import numpy

from .abstract import OpticalEquipment
from ..units import get_unit_registry
from ..utils import ConnectionType
from ..constants import GraphConstants


from enum import Enum


class TelescopeType(Enum):
    REFRACTOR = "refractor"
    REFLECTOR = "reflector"
    CATADIOPTRIC = "catadioptric"


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
        telescope_type: TelescopeType = TelescopeType.REFRACTOR,
    ):
        super(Telescope, self).__init__(focal_length, vendor)
        self.aperture = aperture * get_unit_registry().mm
        self.connection_type = connection_type
        self.t2_output = t2_output
        self.telescope_type = telescope_type

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
        return self.aperture / 6

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
        self._register_output(equipment, self.connection_type)
        # Connect telescope node to space node
        equipment.add_edge(GraphConstants.SPACE_ID, self.id())
        # Handling optional T2 output
        if self.t2_output:
            self._register_output(equipment, ConnectionType.T2)

    def __str__(self):
        # Format: <vendor> <aperture>/<focal length>
        return "{} {}/{}".format(
            self.vendor,
            self.aperture.magnitude,
            self.focal_length.magnitude,
        )
