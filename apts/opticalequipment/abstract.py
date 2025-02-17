import uuid

from ..constants import OpticalType
from ..utils import ConnectionType, ureg


class OpticalEqipment:
  """
  Basic class for optical equipment
  """

  _SEPARATOR = "_"
  OUT = "out"
  IN = "in"

  def __init__(self, focal_length, vendor):
    self._id = str(uuid.uuid4())
    self._type = OpticalType.OPTICAL

    self.focal_length = focal_length * ureg.mm
    self.vendor = vendor

  def get_name(self):
    return str(self.__class__.__name__)

  def type(self):
    return self._type

  def label(self):
    return str(self)

  def id(self):
    return self._id

  def in_id(self, connection_type):
    return self._SEPARATOR.join([self._id, connection_type.name, self.IN])

  def out_id(self, connection_type):
    return self._SEPARATOR.join([self._id, connection_type.name, self.OUT])

  @staticmethod
  def get_parent_id(name : str):
    return name.split(OpticalEqipment._SEPARATOR)[0]

  def _register(self, equipment):
    # Register equipment node
    equipment.add_vertex(self.id(), self)

  def _register_output(self, equipment, connection_type=ConnectionType.F_1_25):
    # Add output node
    equipment.add_vertex(self.out_id(
      connection_type), node_type=OpticalType.OUTPUT, connection_type=connection_type)
    # Connect node to its output
    equipment.add_edge(self.id(), self.out_id(connection_type))

  def _register_input(self, equipment, connection_type=ConnectionType.F_1_25):
    # Add input node
    equipment.add_vertex(self.in_id(
      connection_type), node_type=OpticalType.INPUT, connection_type=connection_type)
    # Connect node to its input
    equipment.add_edge(self.in_id(connection_type), self.id())

  def __str__(self):
    # Format: <vendor>
    return "{} f={}".format(self.vendor, self.focal_length)


class OutputOpticalEqipment(OpticalEqipment):

  def __init__(self, focal_length, vendor):
    super(OutputOpticalEqipment, self).__init__(focal_length, vendor)

  def exit_pupil(self, telescop, zoom):
    return telescop.aperture / zoom

  def brightness(self, telescop, zoom):
    return (self.exit_pupil(telescop, zoom) / (7 * ureg.mm)) ** 2 * 100
