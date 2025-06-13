import uuid
import numpy as np # For np.nan

from ..constants import OpticalType
from ..utils import ConnectionType, ureg


class OpticalEquipment:
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
    return name.split(OpticalEquipment._SEPARATOR)[0]

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


class OutputOpticalEqipment(OpticalEquipment):

  def __init__(self, focal_length, vendor):
    super(OutputOpticalEqipment, self).__init__(focal_length, vendor)

  def is_visual_output(self):
    """Indicates if the output is primarily for visual observation."""
    return True # Default for eyepieces etc.

  def exit_pupil(self, telescop, zoom):
    # Ensure zoom is not zero and is a Quantity to prevent division by zero or type errors
    if not hasattr(zoom, 'magnitude') or zoom.magnitude == 0:
        # Return a zero Quantity or NaN Quantity if zoom is invalid
        # For exit pupil calculation, perhaps a large value or NaN is more appropriate
        # to indicate an issue, as zero exit pupil is physically unlikely with valid zoom.
        # However, to prevent issues in brightness, let's ensure it results in zero/NaN brightness.
        # Let's return a value that would lead to zero or NaN brightness.
        # A very large number for zoom would make exit pupil very small.
        # Or, more directly, handle this in brightness.
        # For now, let's assume zoom is valid if it's not zero.
        # The original code didn't have this check, let's proceed with caution.
        # If zoom can be non-Quantity, that's another issue. For now, assume it's a Quantity.
        return telescop.aperture / zoom # This line remains, but its usage in brightness will be safer.

  def brightness(self, telescop, zoom):
    if not self.is_visual_output():
        return np.nan * ureg.dimensionless # Return NaN Quantity

    # Ensure zoom is a Quantity and its magnitude is not zero
    if not hasattr(zoom, 'magnitude') or not hasattr(zoom, 'units') or zoom.magnitude == 0:
        return np.nan * ureg.dimensionless # Or 0.0 * ureg.dimensionless if preferred for zero zoom

    ep_val = self.exit_pupil(telescop, zoom)

    # Ensure ep_val is a Quantity (it should be if aperture and zoom are)
    if not hasattr(ep_val, 'units'):
        # This case should ideally not be reached if inputs are correct
        return np.nan * ureg.dimensionless

    # Ensure telescope.aperture is a Quantity with units
    if not hasattr(telescop.aperture, 'units'):
        # This indicates an issue with telescope object's aperture
        return np.nan * ureg.dimensionless

    try:
        ep_mm = ep_val.to(ureg.mm)
    except Exception: # Broad exception for any Pint conversion error
        return np.nan * ureg.dimensionless # Failed to convert exit pupil to mm

    seven_mm = 7 * ureg.mm
    # seven_mm.magnitude cannot be zero unless ureg.mm is redefined, which is unlikely.

    # Ratio will be dimensionless if ep_mm and seven_mm are compatible (both lengths)
    # Pint handles unit cancellation automatically.
    ratio = ep_mm / seven_mm

    # The result of (ratio ** 2) is a dimensionless Quantity.
    # Multiplying by 100 keeps it a dimensionless Quantity.
    # Ensure the result is explicitly dimensionless for safety, though Pint should handle it.
    return (ratio ** 2) * 100 * ureg.dimensionless
