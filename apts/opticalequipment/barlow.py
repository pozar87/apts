from .abstract import OpticalEquipment
from ..utils import ConnectionType


class Barlow(OpticalEquipment):
  """
  Class representing Barlow lenses
  """

  def __init__(self, magnification, vendor="unknown barlow", connection_type=ConnectionType.F_1_25, t2_output=False, mass=0, optical_length=0):
    super(Barlow, self).__init__(0, vendor, mass=mass, optical_length=optical_length)
    self.connection_type = connection_type
    self.t2_output = t2_output
    self.magnification = magnification

  def register(self, equipment):
    """
    Register barlow lens in optical equipment graph. Barlow node is build out of three vertices:
    barlow node its input and output. Barlow node is automatically connected with them.
    """
    # Add barlow lens node
    super(Barlow, self)._register(equipment)
    # Add barlow lens output node and connect it to barlow lens
    self._register_output(equipment, self.connection_type)
    # Add barlow lens input node and connect it to barlow lens
    self._register_input(equipment, self.connection_type)
    # Handling optional T2 output
    if self.t2_output:
      self._register_output(equipment, ConnectionType.T2)

  def __str__(self):
    # Format: <vendor> x<magnification>
    return "{} x{}".format(self.get_vendor(), self.magnification)
