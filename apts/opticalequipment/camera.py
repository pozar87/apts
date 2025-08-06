import math

import numpy

from .abstract import OutputOpticalEqipment
from ..constants import GraphConstants
from ..units import ureg
from ..utils import ConnectionType


class Camera(OutputOpticalEqipment):
  """
  Class representing DSLR camera mounted via T2 adapter
  """

  def __init__(self, sensor_width, sensor_height, width, height, vendor="unknown camera",
               connection_type=ConnectionType.T2):
    super(Camera, self).__init__(0, vendor)
    self.connection_type = connection_type
    self.sensor_width = sensor_width * ureg.mm
    self.sensor_height = sensor_height * ureg.mm
    self.width = width
    self.height = height

  def pixel_size(self):
    return numpy.sqrt(self.sensor_width ** 2 + self.sensor_height ** 2) / math.sqrt(self.width ** 2 + self.height ** 2)

  def _zoom_divider(self):
    return numpy.sqrt(self.sensor_width ** 2 + self.sensor_height ** 2)

  def field_of_view(self, telescop, zoom, barlow_magnification):
    return self.sensor_height * 3438 / (telescop.focal_length * barlow_magnification) / 60 * ureg.deg

  def output_type(self):
    return GraphConstants.IMAGE_ID

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
