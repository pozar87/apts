import math
import numpy
from typing import Any, cast

from .telescope import Telescope
from ..constants import GraphConstants, OpticalType
from ..units import get_unit_registry


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
            pixel_size=entry.get("pixel_size_um"),
            read_noise=entry.get("read_noise_e"),
            quantum_efficiency=entry.get("quantum_efficiency_pct"),
            full_well=entry.get("full_well_e"),
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
        pixel_size=None,
        read_noise=None,
        quantum_efficiency=None,
        full_well=None,
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
        self.sensor_width = cast(Any, sensor_width * ureg.mm)
        self.sensor_height = cast(Any, sensor_height * ureg.mm)
        self.width = width
        self.height = height
        self.read_noise = read_noise
        self.quantum_efficiency = quantum_efficiency
        self.full_well = full_well
        if pixel_size is not None:
            self._pixel_size = cast(Any, pixel_size * ureg.micrometer)
        else:
            self._pixel_size = None

    @property
    def magnification(self):
        return 1.0

    def output_type(self):
        return OpticalType.IMAGE

    def is_visual_output(self):
        return False

    def pixel_size(self):
        if hasattr(self, "_pixel_size") and self._pixel_size is not None:
            return self._pixel_size
        ureg = get_unit_registry()
        size_mm = numpy.sqrt(self.sensor_width**2 + self.sensor_height**2) / math.sqrt(
            self.width**2 + self.height**2
        )
        return size_mm.to(ureg.micrometer)

    def _zoom_divider(self):
        return numpy.sqrt(self.sensor_width**2 + self.sensor_height**2)

    def field_of_view_width(self, telescope, zoom, barlow_magnification):
        """
        Calculates horizontal field of view in degrees using the accurate arctan formula.
        """
        f = (self.focal_length * barlow_magnification).to("mm").magnitude
        d = self.sensor_width.to("mm").magnitude
        if f == 0:
            return 0 * get_unit_registry().deg
        return 2 * numpy.degrees(numpy.arctan(d / (2 * f))) * get_unit_registry().deg

    def field_of_view_height(self, telescope, zoom, barlow_magnification):
        """
        Calculates vertical field of view in degrees using the accurate arctan formula.
        """
        f = (self.focal_length * barlow_magnification).to("mm").magnitude
        d = self.sensor_height.to("mm").magnitude
        if f == 0:
            return 0 * get_unit_registry().deg
        return 2 * numpy.degrees(numpy.arctan(d / (2 * f))) * get_unit_registry().deg

    def field_of_view_diagonal(self, telescope, zoom, barlow_magnification):
        """
        Calculates diagonal field of view in degrees using the accurate arctan formula.
        """
        f = (self.focal_length * barlow_magnification).to("mm").magnitude
        d = numpy.sqrt(
            self.sensor_width.to("mm").magnitude**2
            + self.sensor_height.to("mm").magnitude**2
        )
        if f == 0:
            return 0 * get_unit_registry().deg
        return 2 * numpy.degrees(numpy.arctan(d / (2 * f))) * get_unit_registry().deg

    def fov(self) -> Any:
        """
        Calculate the field of view for the smart telescope in degrees using the accurate arctan formula.
        """
        return self.field_of_view_height(self, 1.0, 1.0)

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
