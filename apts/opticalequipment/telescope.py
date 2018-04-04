import numpy

from .abstract import OpticalEqipment
from ..utils import ConnectionType, Constants, ureg


class Telescope(OpticalEqipment):
  """
  Class representing telescope
  """

  def __init__(self, aperture, focal_length, vendor="unknown telescope", connection_type=ConnectionType.F_1_25,
               t2_output=False):
    super(Telescope, self).__init__(focal_length, vendor)
    self.aperture = aperture * ureg.mm
    self.connection_type = connection_type
    self.t2_output = t2_output

  def speed(self):
    return self.aperture / self.focal_length

  def max_range(self):
    return 2 + 5 * numpy.log10(self.aperture.magnitude)

  def min_useful_zoom(self):
    return self.aperture / 6

  def max_useful_zoom(self):
    return self.aperture.magnitude * 2

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
    equipment.add_edge(Constants.SPACE_ID, self.id())
    # Handling optional T2 output
    if self.t2_output:
      self._register_output(equipment, ConnectionType.T2)

  def __str__(self):
    # Format: <vendor> <aperture>/<focal length>
    return "{} {}/{}".format(self.vendor, self.aperture.magnitude, self.focal_length.magnitude)
