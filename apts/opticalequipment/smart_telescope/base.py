from typing import Any, cast

import numpy

from ...constants import GraphConstants, OpticalType
from ...units import get_unit_registry
from ..telescope import Telescope
from .calculations import (
    calculate_smart_telescope_dynamic_range,
    calculate_smart_telescope_fov_diagonal,
    calculate_smart_telescope_fov_height,
    calculate_smart_telescope_fov_width,
    calculate_smart_telescope_pixel_size,
    normalize_smart_telescope_database_entry,
)


class SmartTelescope(Telescope):
    """
    Class representing a smart telescope, which is a telescope and a camera in one.
    """

    path_layer = 1

    @classmethod
    def normalize_database_entry(cls, entry: dict) -> dict:
        entry = normalize_smart_telescope_database_entry(entry)
        return super().normalize_database_entry(entry)

    @classmethod
    def from_database(cls, entry):
        entry = cls.normalize_database_entry(entry)
        brand = entry.get("brand", "Unknown")
        name = entry.get("name", "Unknown")
        vendor = entry.get("vendor", f"{brand} {name}")
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
            mass=mass,
            outputs=[],  # Smart telescope has no outputs
        )
        # Smart telescope is a closed system, so we don't want any inputs or outputs
        self._inputs = []
        self._outputs = []

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
        sw_mm = self.sensor_width.to("mm").magnitude
        sh_mm = self.sensor_height.to("mm").magnitude
        size_um = calculate_smart_telescope_pixel_size(
            sensor_width_mm=sw_mm,
            sensor_height_mm=sh_mm,
            width=self.width,
            height=self.height,
        )
        return size_um * ureg.micrometer

    def dynamic_range(self) -> float | None:
        """
        Calculates the sensor's dynamic range in stops.
        Formula: DR = log2(Full Well Capacity / Read Noise)
        Source: https://en.wikipedia.org/wiki/Dynamic_range#Digital_photography
        """
        return calculate_smart_telescope_dynamic_range(
            full_well=self.full_well,
            read_noise=self.read_noise,
        )

    def _zoom_divider(self):
        sw = float(self.sensor_width.to("mm").magnitude)
        sh = float(self.sensor_height.to("mm").magnitude)
        diagonal = float(numpy.sqrt(sw**2 + sh**2))
        if diagonal == 0:
            # Unknown sensor size: report a non-finite divider so zoom becomes 0
            # instead of raising ZeroDivisionError.
            return float("inf") * get_unit_registry().mm
        return diagonal * get_unit_registry().mm

    def field_of_view(self, telescope, zoom, barlow_magnification):
        return self.field_of_view_height(telescope, zoom, barlow_magnification)

    def field_of_view_width(self, telescope, zoom, barlow_magnification):
        """
        Calculates horizontal field of view in degrees using the accurate arctan formula.
        """
        f = self.focal_length.to("mm").magnitude
        d = self.sensor_width.to("mm").magnitude
        fov_deg = calculate_smart_telescope_fov_width(
            focal_length_mm=f,
            sensor_width_mm=d,
            barlow_magnification=barlow_magnification,
        )
        return fov_deg * get_unit_registry().deg

    def field_of_view_height(self, telescope, zoom, barlow_magnification):
        """
        Calculates vertical field of view in degrees using the accurate arctan formula.
        """
        f = self.focal_length.to("mm").magnitude
        d = self.sensor_height.to("mm").magnitude
        fov_deg = calculate_smart_telescope_fov_height(
            focal_length_mm=f,
            sensor_height_mm=d,
            barlow_magnification=barlow_magnification,
        )
        return fov_deg * get_unit_registry().deg

    def field_of_view_diagonal(self, telescope, zoom, barlow_magnification):
        """
        Calculates diagonal field of view in degrees using the accurate arctan formula.
        """
        f = self.focal_length.to("mm").magnitude
        sw = self.sensor_width.to("mm").magnitude
        sh = self.sensor_height.to("mm").magnitude
        fov_deg = calculate_smart_telescope_fov_diagonal(
            focal_length_mm=f,
            sensor_width_mm=sw,
            sensor_height_mm=sh,
            barlow_magnification=barlow_magnification,
        )
        return fov_deg * get_unit_registry().deg

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
        super(Telescope, self).register(equipment)
        # Connect telescope node to space node
        equipment.add_edge(GraphConstants.SPACE_ID, self.id())
        # Connect telescope node to the final image node
        equipment.add_edge(self.id(), GraphConstants.IMAGE_ID)

    def __str__(self):
        # Format: <vendor> <aperture>/<focal length>
        return f"{self.get_vendor()} {self.aperture.magnitude}/{self.focal_length.magnitude} ({self.width}x{self.height})"
