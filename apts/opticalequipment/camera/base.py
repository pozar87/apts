import numpy
import math
from typing import Any
from ..abstract import OutputOpticalEqipment
from ...constants import GraphConstants, OpticalType
from ...units import get_unit_registry
from ...utils import ConnectionType, Gender

class Camera(OutputOpticalEqipment):

    @classmethod
    def from_database(cls, entry):
        from ...utils import Utils, Gender
        brand = entry['brand']
        name = entry['name']
        vendor = f'{brand} {name}'
        ol = entry.get('optical_length', 0)
        mass = entry.get('mass', 0)
        tt = Utils.map_conn(entry.get('tside_thread'))
        tg = Utils.map_gender(entry.get('tside_gender'))
        sw, sh = (23.5, 15.7)
        w, h = (6000, 4000)
        if 'full frame' in name.lower() or '36x24' in name.lower():
            sw, sh = (35.9, 23.9)
            w, h = (8256, 5504)
        elif '4/3' in name.lower() or 'micro four thirds' in name.lower():
            sw, sh = (17.3, 13.0)
            w, h = (4656, 3520)
        return cls(sw, sh, w, h, vendor=vendor, connection_type=tt, connection_gender=tg or Gender.FEMALE, backfocus=ol, mass=mass, optical_length=ol)
    '\n  Class representing DSLR camera mounted via T2 adapter\n  '

    def __init__(self, sensor_width, sensor_height, width, height, vendor='unknown camera', connection_type=ConnectionType.T2, connection_gender=Gender.FEMALE, pixel_size=None, read_noise=None, full_well=None, quantum_efficiency=None, backfocus=None, mass=0, optical_length=0):
        super(Camera, self).__init__(0, vendor, mass=mass, optical_length=optical_length)
        self.connection_type = connection_type
        self.connection_gender = connection_gender
        self.sensor_width = sensor_width * get_unit_registry().mm
        self.sensor_height = sensor_height * get_unit_registry().mm
        self.width = width
        self.height = height
        self.read_noise = read_noise
        self.full_well = full_well
        self.quantum_efficiency = quantum_efficiency
        self.backfocus = backfocus * get_unit_registry().mm if backfocus is not None else None
        if pixel_size is not None:
            self._pixel_size = pixel_size * get_unit_registry().micrometer
        else:
            self._pixel_size = None

    def pixel_size(self) -> Any:
        if self._pixel_size is not None:
            return self._pixel_size
        return numpy.sqrt(self.sensor_width ** 2 + self.sensor_height ** 2) / math.sqrt(self.width ** 2 + self.height ** 2)

    def _zoom_divider(self):
        return numpy.sqrt(self.sensor_width ** 2 + self.sensor_height ** 2)

    def field_of_view_width(self, telescope, zoom, barlow_magnification):
        """
        Calculates horizontal field of view in degrees using the accurate arctan formula.
        """
        f = (telescope.focal_length * barlow_magnification).to('mm').magnitude
        d = self.sensor_width.to('mm').magnitude
        if f == 0:
            return 0 * get_unit_registry().deg
        return 2 * numpy.degrees(numpy.arctan(d / (2 * f))) * get_unit_registry().deg

    def field_of_view_height(self, telescope, zoom, barlow_magnification):
        """
        Calculates vertical field of view in degrees using the accurate arctan formula.
        """
        f = (telescope.focal_length * barlow_magnification).to('mm').magnitude
        d = self.sensor_height.to('mm').magnitude
        if f == 0:
            return 0 * get_unit_registry().deg
        return 2 * numpy.degrees(numpy.arctan(d / (2 * f))) * get_unit_registry().deg

    def field_of_view_diagonal(self, telescope, zoom, barlow_magnification):
        """
        Calculates diagonal field of view in degrees using the accurate arctan formula.
        """
        f = (telescope.focal_length * barlow_magnification).to('mm').magnitude
        d = numpy.sqrt(self.sensor_width.to('mm').magnitude ** 2 + self.sensor_height.to('mm').magnitude ** 2)
        if f == 0:
            return 0 * get_unit_registry().deg
        return 2 * numpy.degrees(numpy.arctan(d / (2 * f))) * get_unit_registry().deg

    def field_of_view(self, telescope, zoom, barlow_magnification):
        return self.field_of_view_height(telescope, zoom, barlow_magnification)

    def output_type(self):
        return OpticalType.IMAGE

    def register(self, equipment):
        super(Camera, self)._register(equipment)
        self._register_input(equipment, self.connection_type, self.connection_gender)
        equipment.add_edge(self.id(), GraphConstants.IMAGE_ID)

    def is_visual_output(self):
        return False

    def __str__(self):
        return '{} {}x{}'.format(self.vendor, self.sensor_width.magnitude, self.sensor_height.magnitude)