from .abstract import OpticalEquipment
from ..utils import ConnectionType, Gender


class Barlow(OpticalEquipment):
  """
  Class representing Barlow lenses
  """

  def __init__(self, magnification, vendor="unknown barlow", connection_type=ConnectionType.F_1_25, in_gender=Gender.MALE, out_gender=Gender.FEMALE, t2_output=False, mass=0, optical_length=0):
    super(Barlow, self).__init__(0, vendor, mass=mass, optical_length=optical_length)
    self.connection_type = connection_type
    self.in_gender = in_gender
    self.out_gender = out_gender
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
    self._register_output(equipment, self.connection_type, self.out_gender)
    # Add barlow lens input node and connect it to barlow lens
    self._register_input(equipment, self.connection_type, self.in_gender)
    # Handling optional T2 output
    if self.t2_output:
      self._register_output(equipment, ConnectionType.T2)

  def __str__(self):
    # Format: <vendor> x<magnification>
    return "{} x{}".format(self.get_vendor(), self.magnification)

  @classmethod
  def Celestron_Omni_2x(cls):
    return cls(2.0, "Celestron Omni", connection_type=ConnectionType.F_1_25)

  @classmethod
  def TeleVue_Powermate_2x(cls):
    return cls(2.0, "Tele Vue Powermate", connection_type=ConnectionType.F_2, mass=500)

  @classmethod
  def TeleVue_Powermate_4x(cls):
    return cls(4.0, "Tele Vue Powermate", connection_type=ConnectionType.F_2, mass=500)
