from typing import Any, cast

import numpy

from ...constants import GraphConstants, OpticalType
from ...units import get_unit_registry
from ...utils import ConnectionType
from ..base import OutputOpticalEquipment


class Camera(OutputOpticalEquipment):
    path_layer = 5
    _DATABASE = {}

    @classmethod
    def from_database(cls, entry):
        from .calculations import normalize_camera_database_entry

        entry = normalize_camera_database_entry(entry)
        brand = entry.get("brand", "Unknown")
        name = entry.get("name", "Unknown")
        vendor = f"{brand} {name}"
        ol = entry.get("optical_length", 0)
        mass = entry.get("mass", 0)
        sw = entry["sensor_width_mm"]
        sh = entry["sensor_height_mm"]
        w = entry["width"]
        h = entry["height"]
        inputs = entry["inputs"]

        return cls(
            sw,
            sh,
            w,
            h,
            vendor=vendor,
            inputs=inputs,
            backfocus=ol,
            mass=mass,
            optical_length=ol,
            pixel_size=entry.get("pixel_size_um"),
            read_noise=entry.get("read_noise_e"),
            full_well=entry.get("full_well_e"),
            quantum_efficiency=entry.get("quantum_efficiency_pct"),
        )

    "\n  Class representing DSLR camera mounted via T2 adapter\n  "

    def __init__(
        self,
        sensor_width: float,
        sensor_height: float,
        width: int,
        height: int,
        vendor: str = "unknown camera",
        inputs: list | None = None,
        pixel_size: float | None = None,
        read_noise: float | None = None,
        full_well: float | None = None,
        quantum_efficiency: float | None = None,
        backfocus: float | None = None,
        mass: float = 0,
        optical_length: float = 0,
        connection_type=None,
        connection_gender=None,
    ):
        if inputs is None:
            if connection_type:
                inputs = [(connection_type, connection_gender)]
            else:
                inputs = [ConnectionType.T2]

        if not isinstance(inputs, list):
            inputs = [inputs]
        super().__init__(
            0, vendor, mass=mass, optical_length=optical_length, inputs=inputs
        )
        self.sensor_width = cast(Any, sensor_width * get_unit_registry().mm)
        self.sensor_height = cast(Any, sensor_height * get_unit_registry().mm)
        self.width = width
        self.height = height
        self.read_noise = read_noise
        self.full_well = full_well
        self.quantum_efficiency = quantum_efficiency
        self.backfocus = (
            cast(Any, backfocus * get_unit_registry().mm)
            if backfocus is not None
            else None
        )
        if pixel_size is not None:
            self._pixel_size = cast(Any, pixel_size * get_unit_registry().micrometer)
        else:
            self._pixel_size = None

    @property
    def connection_type(self):
        return self._inputs[0][0] if self._inputs else None

    @property
    def connection_gender(self):
        return self._inputs[0][1] if self._inputs else None

    def pixel_size(self) -> Any:
        from ...optics.calculations import calculate_pixel_size
        ureg = get_unit_registry()
        pixel_size_um = self._pixel_size.to("micrometer").magnitude if self._pixel_size is not None else None
        sensor_width_mm = self.sensor_width.to("mm").magnitude
        sensor_height_mm = self.sensor_height.to("mm").magnitude
        size_um = calculate_pixel_size(
            pixel_size_um=pixel_size_um,
            sensor_width_mm=sensor_width_mm,
            sensor_height_mm=sensor_height_mm,
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
        from ...optics.calculations import calculate_dynamic_range
        return calculate_dynamic_range(self.full_well, self.read_noise)

    def _zoom_divider(self):
        return numpy.sqrt(self.sensor_width**2 + self.sensor_height**2)

    def field_of_view_width(self, telescope, zoom, barlow_magnification):
        """
        Calculates horizontal field of view in degrees using the accurate arctan formula.
        """
        from ...optics.calculations import calculate_camera_field_of_view
        f_eff_mm = (telescope.focal_length * barlow_magnification).to("mm").magnitude
        d_mm = self.sensor_width.to("mm").magnitude
        fov_deg = calculate_camera_field_of_view(d_mm, f_eff_mm)
        return fov_deg * get_unit_registry().deg

    def field_of_view_height(self, telescope, zoom, barlow_magnification):
        """
        Calculates vertical field of view in degrees using the accurate arctan formula.
        """
        from ...optics.calculations import calculate_camera_field_of_view
        f_eff_mm = (telescope.focal_length * barlow_magnification).to("mm").magnitude
        d_mm = self.sensor_height.to("mm").magnitude
        fov_deg = calculate_camera_field_of_view(d_mm, f_eff_mm)
        return fov_deg * get_unit_registry().deg

    def field_of_view_diagonal(self, telescope, zoom, barlow_magnification):
        """
        Calculates diagonal field of view in degrees using the accurate arctan formula.
        """
        from ...optics.calculations import calculate_camera_field_of_view
        f_eff_mm = (telescope.focal_length * barlow_magnification).to("mm").magnitude
        d_mm = numpy.sqrt(
            self.sensor_width.to("mm").magnitude ** 2
            + self.sensor_height.to("mm").magnitude ** 2
        )
        fov_deg = calculate_camera_field_of_view(d_mm, f_eff_mm)
        return fov_deg * get_unit_registry().deg

    def field_of_view(self, telescope, zoom, barlow_magnification):
        return self.field_of_view_height(telescope, zoom, barlow_magnification)

    def output_type(self):
        return OpticalType.IMAGE

    def register(self, equipment):
        super().register(equipment)
        equipment.add_edge(self.id(), GraphConstants.IMAGE_ID)

    def is_visual_output(self):
        return False

    def __str__(self):
        return "{} {}x{}".format(
            self.vendor, self.sensor_width.magnitude, self.sensor_height.magnitude
        )
