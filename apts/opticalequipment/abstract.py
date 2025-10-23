import uuid
import numpy as np # For np.nan

from ..constants import OpticalType
from ..units import get_unit_registry
from ..utils import ConnectionType


class OpticalEquipment:
  """
  Basic class for optical equipment
  """

  _SEPARATOR = "_"
  OUT = "out"
  IN = "in"

  def __init__(self, focal_length, vendor):
    if np.isnan(focal_length):
        raise ValueError("focal_length cannot be NaN")
    self._id = str(uuid.uuid4())
    self._type = OpticalType.OPTICAL

    self.focal_length = focal_length * get_unit_registry().mm
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


class IntermediateOpticalEquipment(OpticalEquipment):
    def __init__(self, vendor):
        super(IntermediateOpticalEquipment, self).__init__(focal_length=0, vendor=vendor)

    def _register(self, equipment, in_connection_type, out_connection_type):
        super(IntermediateOpticalEquipment, self)._register(equipment)
        self._register_input(equipment, in_connection_type)
        self._register_output(equipment, out_connection_type)


class OutputOpticalEqipment(OpticalEquipment):

  def __init__(self, focal_length, vendor):
    super(OutputOpticalEqipment, self).__init__(focal_length, vendor)

  def is_visual_output(self):
    """Indicates if the output is primarily for visual observation."""
    return True # Default for eyepieces etc.

  def exit_pupil(self, telescop, zoom):
      ureg = get_unit_registry()
      # Default unit for exit pupil if telescope aperture is problematic
      default_mm_unit = ureg.mm

      # Validate telescop.aperture
      if not hasattr(telescop, 'aperture') or \
         not hasattr(telescop.aperture, 'units') or \
         (hasattr(telescop.aperture, 'magnitude') and np.isnan(telescop.aperture.magnitude)):
          return np.nan * default_mm_unit # Aperture is invalid

      aperture_units = telescop.aperture.units

      # Validate zoom
      if not hasattr(zoom, 'magnitude') or \
         not hasattr(zoom, 'units') or \
         np.isnan(zoom.magnitude) or \
         zoom.magnitude == 0:
          return np.nan * aperture_units # Zoom is invalid or zero, use aperture's units for consistency

      # If zoom is not dimensionless, Pint's division rules will typically handle it
      # by raising a DimensionalityError or producing a result with unexpected units.
      # A specific check could be: if not zoom.dimensionless: return np.nan * aperture_units
      # However, we rely on the try-except and dimensionality check below for broader safety.

      try:
          result = telescop.aperture / zoom
          # Ensure result has the same dimensionality as aperture (length)
          # This is a safeguard; Pint should ensure this if zoom is dimensionless.
          # If zoom has units, this check becomes more critical.
          if result.dimensionality != telescop.aperture.dimensionality:
               return np.nan * aperture_units
          return result
      except Exception: # Catch any error during division (e.g., unexpected Pint issue, DimensionalityError)
          return np.nan * aperture_units

  def brightness(self, telescop, zoom):
    ureg = get_unit_registry()
    if not self.is_visual_output():
        return np.nan * ureg.dimensionless

    # Validate zoom (early exit if zoom is fundamentally bad or NaN)
    if not hasattr(zoom, 'magnitude') or \
       not hasattr(zoom, 'units') or \
       np.isnan(zoom.magnitude) or \
       zoom.magnitude == 0:
        # If zoom is 0, exit pupil is infinite/undefined. NaN is appropriate.
        return np.nan * ureg.dimensionless

    ep_val = self.exit_pupil(telescop, zoom) # This is now robust

    # After calling exit_pupil, ep_val should always be a Quantity.
    # Check if its magnitude is NaN (this means exit_pupil determined a NaN result).
    if not hasattr(ep_val, 'units') or \
       (hasattr(ep_val, 'magnitude') and np.isnan(ep_val.magnitude)):
        return np.nan * ureg.dimensionless

    try:
        # ep_val should have length units (e.g., mm, inch) from robust exit_pupil.
        ep_mm = ep_val.to(ureg.mm)
    except Exception: # Catch Pint conversion errors (e.g., DimensionalityError if ep_val wasn't length)
        return np.nan * ureg.dimensionless

    # Check if ep_mm.magnitude became NaN after conversion or if units are missing
    if not hasattr(ep_mm, 'units') or \
       (hasattr(ep_mm, 'magnitude') and np.isnan(ep_mm.magnitude)):
        return np.nan * ureg.dimensionless

    seven_mm = 7 * ureg.mm

    # Avoid division by zero if seven_mm is somehow misconfigured
    if not hasattr(seven_mm, 'magnitude') or seven_mm.magnitude == 0: # Added hasattr check for magnitude
        return np.nan * ureg.dimensionless

    ratio = ep_mm / seven_mm # ep_mm and seven_mm are both mm, ratio is dimensionless Q

    # Check if ratio.magnitude is NaN or if units are unexpectedly missing
    if not hasattr(ratio, 'units') or \
       (hasattr(ratio, 'magnitude') and np.isnan(ratio.magnitude)):
        return np.nan * ureg.dimensionless

    # Final calculation. Result should be a dimensionless Quantity.
    # The explicit `* ureg.dimensionless` ensures it.
    return (ratio ** 2) * 100 * ureg.dimensionless
