import math

import numpy

from .abstract import OutputOpticalEqipment
from ..constants import GraphConstants, OpticalType
from ..units import get_unit_registry
from ..utils import ConnectionType


class Camera(OutputOpticalEqipment):
  """
  Class representing DSLR camera mounted via T2 adapter
  """

  def __init__(self, sensor_width, sensor_height, width, height, vendor="unknown camera",
               connection_type=ConnectionType.T2, pixel_size=None, read_noise=None,
               full_well=None, quantum_efficiency=None):
    super(Camera, self).__init__(0, vendor)
    self.connection_type = connection_type
    self.sensor_width = sensor_width * get_unit_registry().mm
    self.sensor_height = sensor_height * get_unit_registry().mm
    self.width = width
    self.height = height
    self.read_noise = read_noise
    self.full_well = full_well
    self.quantum_efficiency = quantum_efficiency
    if pixel_size is not None:
      self._pixel_size = pixel_size * get_unit_registry().micrometer
    else:
      self._pixel_size = None

  def pixel_size(self):
    if self._pixel_size is not None:
      return self._pixel_size
    return numpy.sqrt(self.sensor_width ** 2 + self.sensor_height ** 2) / math.sqrt(
      self.width ** 2 + self.height ** 2)

  def _zoom_divider(self):
    return numpy.sqrt(self.sensor_width ** 2 + self.sensor_height ** 2)

  def field_of_view(self, telescop, zoom, barlow_magnification):
    return self.sensor_height * 3438 / (telescop.focal_length * barlow_magnification) / 60 * get_unit_registry().deg

  def output_type(self):
    return OpticalType.IMAGE

  def register(self, equipment):
    # Add camera node
    super(Camera, self)._register(equipment)
    # Add camera input node and connect it to camera
    self._register_input(equipment, self.connection_type)
    # Connect camera with output image node
    equipment.add_edge(self.id(), GraphConstants.IMAGE_ID)

  def is_visual_output(self):
    return False

  def __str__(self):
    # Format: <vendor> <width>x<height>
    return "{} {}x{}".format(self.vendor, self.sensor_width.magnitude, self.sensor_height.magnitude)

  @classmethod
  def ZWO_ASI2600MC_PRO(cls):
    """
    Factory method for ZWO ASI2600MC Pro camera.
    Sensor: Sony IMX571 (APS-C)
    """
    return cls(
      23.5, 15.7, 6248, 4176, "ZWO ASI2600MC Pro",
      pixel_size=3.76, read_noise=1.0, full_well=50000, quantum_efficiency=80
    )

  @classmethod
  def ZWO_ASI1600MM_PRO(cls):
    """
    Factory method for ZWO ASI1600MM Pro camera.
    Sensor: Panasonic MN34230 (4/3")
    """
    return cls(
      17.7, 13.4, 4656, 3520, "ZWO ASI1600MM Pro",
      pixel_size=3.8, read_noise=1.2, full_well=20000, quantum_efficiency=60
    )

  @classmethod
  def Nikon_D850(cls):
    """
    Factory method for Nikon D850 camera.
    Sensor: Full Frame
    """
    return cls(
      35.9, 23.9, 8256, 5504, "Nikon D850",
      pixel_size=4.35, read_noise=1.1, full_well=48000, quantum_efficiency=54
    )

  @classmethod
  def ZWO_ASI533MC_PRO(cls):
    """
    Factory method for ZWO ASI533MC Pro camera.
    Sensor: Sony IMX533 (1" Square)
    """
    return cls(
      11.31, 11.31, 3008, 3008, "ZWO ASI533MC Pro",
      pixel_size=3.76, read_noise=1.0, full_well=50000, quantum_efficiency=80
    )
