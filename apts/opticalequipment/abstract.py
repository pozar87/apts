import uuid

import numpy as np  # For np.nan

from ..constants import OpticalType
from ..i18n import gettext_
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

    def get_vendor(self):
        import logging

        logger = logging.getLogger(__name__)
        translated = gettext_(self.vendor)
        logger.debug(f"Translating vendor: '{self.vendor}' -> '{translated}'")
        return translated

    def get_name(self):
        return gettext_(str(self.__class__.__name__))

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
    def get_parent_id(name: str):
        return name.split(OpticalEquipment._SEPARATOR)[0]

    def _register(self, equipment):
        # Register equipment node
        equipment.add_vertex(self.id(), self)

    def _register_output(self, equipment, connection_type=ConnectionType.F_1_25):
        # Add output node
        equipment.add_vertex(
            self.out_id(connection_type),
            node_type=OpticalType.OUTPUT,
            connection_type=connection_type,
        )
        # Connect node to its output
        equipment.add_edge(self.id(), self.out_id(connection_type))

    def _register_input(self, equipment, connection_type=ConnectionType.F_1_25):
        # Add input node
        equipment.add_vertex(
            self.in_id(connection_type),
            node_type=OpticalType.INPUT,
            connection_type=connection_type,
        )
        # Connect node to its input
        equipment.add_edge(self.in_id(connection_type), self.id())

    def __str__(self):
        # Format: <vendor>
        return "{} f={}".format(self.get_vendor(), self.focal_length)


class IntermediateOpticalEquipment(OpticalEquipment):
    def __init__(self, vendor):
        super(IntermediateOpticalEquipment, self).__init__(
            focal_length=0, vendor=vendor
        )

    def _register(self, equipment, in_connection_type, out_connection_type):  # type: ignore
        super(IntermediateOpticalEquipment, self)._register(equipment)
        self._register_input(equipment, in_connection_type)
        self._register_output(equipment, out_connection_type)


class OutputOpticalEqipment(OpticalEquipment):
    def __init__(self, focal_length, vendor):
        super(OutputOpticalEqipment, self).__init__(focal_length, vendor)

    def is_visual_output(self) -> bool:
        """Indicates if the output is primarily for visual observation."""
        return True  # Default for eyepieces etc.

    def exit_pupil(self, telescop, zoom):
        ureg = get_unit_registry()
        # Default unit for exit pupil if telescope aperture is problematic
        default_mm_unit = ureg.mm

        # Validate telescop.aperture
        aperture = getattr(telescop, "aperture", None)
        if (
            aperture is None
            or not hasattr(aperture, "units")
            or not hasattr(aperture, "magnitude")
            or np.isnan(float(aperture.magnitude))
        ):
            return np.nan * default_mm_unit  # Aperture is invalid

        aperture_units = aperture.units

        # Validate zoom
        zoom_magnitude = getattr(zoom, "magnitude", np.nan)
        if (
            not hasattr(zoom, "units")
            or np.isnan(float(zoom_magnitude))
            or zoom_magnitude == 0
        ):
            return np.nan * aperture_units

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
        except Exception:  # Catch any error during division (e.g., unexpected Pint issue, DimensionalityError)
            return np.nan * aperture_units

    def brightness(self, telescop, zoom):
        ureg = get_unit_registry()
        if not self.is_visual_output():
            return np.nan * ureg.dimensionless

        # Validate zoom (early exit if zoom is fundamentally bad or NaN)
        zoom_magnitude = getattr(zoom, "magnitude", np.nan)
        if (
            not hasattr(zoom, "units")
            or np.isnan(float(zoom_magnitude))
            or zoom_magnitude == 0
        ):
            # If zoom is 0, exit pupil is infinite/undefined. NaN is appropriate.
            return np.nan * ureg.dimensionless

        ep_val = self.exit_pupil(telescop, zoom)  # This is now robust

        # After calling exit_pupil, ep_val should always be a Quantity.
        # Check if its magnitude is NaN (this means exit_pupil determined a NaN result).
        ep_magnitude = getattr(ep_val, "magnitude", np.nan)
        if not hasattr(ep_val, "units") or np.isnan(float(ep_magnitude)):
            return np.nan * ureg.dimensionless

        try:
            # ep_val should have length units (e.g., mm, inch) from robust exit_pupil.
            ep_mm = ep_val.to(ureg.mm)  # pyright: ignore
        except Exception:  # Catch Pint conversion errors (e.g., DimensionalityError if ep_val wasn't length)
            return np.nan * ureg.dimensionless

        # Check if ep_mm.magnitude became NaN after conversion or if units are missing
        ep_mm_magnitude = getattr(ep_mm, "magnitude", np.nan)
        if not hasattr(ep_mm, "units") or np.isnan(float(ep_mm_magnitude)):
            return np.nan * ureg.dimensionless

        seven_mm = 7 * ureg.mm

        # Avoid division by zero if seven_mm is somehow misconfigured
        seven_mm_magnitude = getattr(seven_mm, "magnitude", 0)
        if seven_mm_magnitude == 0:
            return np.nan * ureg.dimensionless

        ratio = (
            ep_mm / seven_mm
        )  # ep_mm and seven_mm are both mm, ratio is dimensionless Q

        # Check if ratio.magnitude is NaN or if units are unexpectedly missing
        ratio_magnitude = getattr(ratio, "magnitude", np.nan)
        if not hasattr(ratio, "units") or np.isnan(float(ratio_magnitude)):
            return np.nan * ureg.dimensionless

        # Final calculation. Result should be a dimensionless Quantity.
        # The explicit `* ureg.dimensionless` ensures it.
        return (ratio**2) * 100 * ureg.dimensionless
