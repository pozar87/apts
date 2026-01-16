import math
import numpy

from .telescope import Telescope
from ..constants import GraphConstants, OpticalType
from ..units import get_unit_registry


class SmartTelescope(Telescope):
    """
    Class representing a smart telescope, which is a telescope and a camera in one.
    """

    def __init__(
        self,
        aperture,
        focal_length,
        sensor_width,
        sensor_height,
        width,
        height,
        vendor="unknown smart telescope",
    ):
        super().__init__(
            aperture, focal_length, vendor, telescope_type=None, t2_output=False
        )
        ureg = get_unit_registry()
        self.sensor_width = sensor_width * ureg.mm
        self.sensor_height = sensor_height * ureg.mm
        self.width = width
        self.height = height

    @property
    def magnification(self):
        return 1.0

    def output_type(self):
        return OpticalType.IMAGE

    def is_visual_output(self):
        return False

    def pixel_size(self):
        return numpy.sqrt(self.sensor_width ** 2 + self.sensor_height ** 2) / math.sqrt(self.width ** 2 + self.height ** 2)

    def fov(self):
        """
        Calculate the field of view for the smart telescope.
        """
        return self.sensor_height * 3438 / self.focal_length / 60 * get_unit_registry().deg

    def exit_pupil(self):
        return numpy.nan * get_unit_registry().mm

    def brightness(self):
        return numpy.nan * get_unit_registry().dimensionless

    def register(self, equipment):
        """
        Register a smart telescope in the optical equipment graph.
        A smart telescope is a direct connection from SPACE to IMAGE.
        """
        # Register the telescope node itself
        super(Telescope, self)._register(equipment)
        # Connect telescope node to space node
        equipment.add_edge(GraphConstants.SPACE_ID, self.id())
        # Connect telescope node to the final image node
        equipment.add_edge(self.id(), GraphConstants.IMAGE_ID)

    def __str__(self):
        # Format: <vendor> <aperture>/<focal length>
        return "{} {}/{} ({}x{})".format(
            self.get_vendor(),
            self.aperture.magnitude,
            self.focal_length.magnitude,
            self.width,
            self.height,
        )
