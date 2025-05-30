from .abstract import OutputOpticalEqipment
from ..constants import GraphConstants

from ..utils import ureg, ConnectionType

class Eyepiece(OutputOpticalEqipment):
  """
  Class representing ocular
  """

  def __init__(self, focal_length, vendor="unknown ocular", field_of_view=70, connection_type=ConnectionType.F_1_25):
    super(Eyepiece, self).__init__(focal_length, vendor)
    self._connection_type = connection_type
    self._field_of_view = field_of_view * ureg.deg

  def _zoom_divider(self):
    return self.focal_length

  def field_of_view(self, telescop, zoom, barlow_magnification):
    return self._field_of_view / zoom

  def output_type(self):
    return GraphConstants.EYE_ID

  def register(self, equipment):
    """
    Register ocular in optical equipment graph. Ocular node is build out of two vertices:
    ocular node and its input. Ocular node is automatically connected with output IMAGE node.
    """
    # Add ocular node
    super(Eyepiece, self)._register(equipment)
    # Add ocular input node and connect it to ocular
    self._register_input(equipment, self._connection_type)
    # Connect ocular with output eye node
    equipment.add_edge(self.id(), GraphConstants.EYE_ID)

  def __str__(self):
    return "{} f={}".format(self.vendor, self.focal_length.magnitude)
    # Format: <vendor> f=<focal_length>
