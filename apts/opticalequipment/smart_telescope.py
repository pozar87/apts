import math
import numpy
from typing import Any

from .telescope import Telescope
from ..constants import GraphConstants, OpticalType
from ..units import get_unit_registry, ureg


class SmartTelescope(Telescope):
    """
    Class representing a smart telescope, which is a telescope and a camera in one.
    """

    @classmethod
    def from_database(cls, entry):
        brand = entry["brand"]
        name = entry["name"]
        vendor = f"{brand} {name}"
        aperture = entry["aperture"]
        focal_length = entry["focal_length"]
        sensor_width = entry["sensor_width"]
        sensor_height = entry["sensor_height"]
        width = entry["width"]
        height = entry["height"]
        mass = entry.get("mass", 0)
        return cls(
            aperture,
            focal_length,
            sensor_width,
            sensor_height,
            width,
            height,
            vendor=vendor,
            mass=mass,
        )

    def __init__(
        self,
        aperture,
        focal_length,
        sensor_width,
        sensor_height,
        width,
        height,
        vendor="unknown smart telescope",
        mass=0,
    ):
        super().__init__(
            aperture,
            focal_length,
            vendor,
            telescope_type=None,
            t2_output=False,
            mass=mass,
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
        return numpy.sqrt(self.sensor_width**2 + self.sensor_height**2) / math.sqrt(
            self.width**2 + self.height**2
        )

    def fov(self) -> Any:
        """
        Calculate the field of view for the smart telescope in degrees using the accurate arctan formula.
        """
        return (
            2
            * numpy.degrees(
                numpy.arctan(
                    self.sensor_height.magnitude / (2 * self.focal_length.magnitude)
                )
            )
            * get_unit_registry().deg
        )

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
