import uuid
from typing import Any, cast

import numpy as np  # For np.nan

from ..constants import OpticalType
from ..i18n import gettext_
from ..units import get_unit_registry
from ..utils import ConnectionType


class OpticalEquipment:

    _DATABASE: dict[Any, Any] = {}
    path_layer: int = 3

    @classmethod
    def normalize_database_entry(cls, entry: dict) -> dict: 
        """ 
        Normalizes a database entry by ensuring it has consistent keys and guessed properties. 
        Default implementation just returns the entry as-is. 
        """ 
        # Round all float values to 2 decimal places for cleaner display 
        for key, value in entry.items(): 
            if isinstance(value, float): 
                entry[key] = round(value, 2) 

        return entry 

    @classmethod 
    def get_database_entries(cls) -> list: 
        """ 
        Returns all database entries for this class, normalized. 
        """ 
        if not hasattr(cls, "_DATABASE"): 
            return [] 
        if isinstance(cls._DATABASE, dict): 
            return [cls.normalize_database_entry(e) for e in cast(dict, cls._DATABASE).values()] 
        return [cls.normalize_database_entry(e) for e in cast(list, cls._DATABASE)] 

    """
    Basic class for optical equipment
    """

    _SEPARATOR = "_"
    OUT = "out"
    IN = "in"

    def __init__(
        self,
        focal_length: float,
        vendor: str,
        optical_length: float = 0,
        mass: float = 0,
        inputs: list | None = None,
        outputs: list | None = None,
    ):
        if np.isnan(focal_length):
            raise ValueError("focal_length cannot be NaN")
        self._id = str(uuid.uuid4())
        self._type = OpticalType.OPTICAL

        self.focal_length = cast(Any, focal_length * get_unit_registry().mm)
        self.vendor = vendor
        self.optical_length = cast(Any, (optical_length or 0) * get_unit_registry().mm)
        self.mass = cast(Any, (mass or 0) * get_unit_registry().gram)
        self.attached_equipment = []
        self._inputs = []
        self._outputs = []

        if inputs:
            if not isinstance(inputs, list):
                inputs = [inputs]
            for inp in inputs:
                if isinstance(inp, tuple):
                    self.add_input(*inp)
                else:
                    self.add_input(inp)

        if outputs:
            if not isinstance(outputs, list):
                outputs = [outputs]
            for outp in outputs:
                if isinstance(outp, tuple):
                    self.add_output(*outp)
                else:
                    self.add_output(outp)

    def add_input(self, connection_type, gender=None):
        """
        Add an input port to this equipment.
        """
        from ..utils import get_default_gender

        if gender is None:
            gender = get_default_gender(connection_type, is_input=True)
        self._inputs.append((connection_type, gender))

    def add_output(self, connection_type, gender=None):
        """
        Add an output port to this equipment.
        """
        from ..utils import get_default_gender

        if gender is None:
            gender = get_default_gender(connection_type, is_input=False)
        self._outputs.append((connection_type, gender))

    def attach(self, equipment: "OpticalEquipment"):
        """
        Attach supporting equipment to this piece of equipment.
        """
        if equipment not in self.attached_equipment:
            self.attached_equipment.append(equipment)

    def collect_all_attached(self, all_equipment: set):
        """
        Collect all attached equipment recursively.
        """
        if self in all_equipment:
            return
        all_equipment.add(self)
        for att in self.attached_equipment:
            att.collect_all_attached(all_equipment)

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

    def dynamic_range(self) -> float | None:
        """
        Calculates the dynamic range of the equipment sensor in stops.
        Formula: log2(full_well / read_noise)
        """
        import numpy

        full_well = getattr(self, "full_well", None)
        read_noise = getattr(self, "read_noise", None)

        if full_well is not None and read_noise is not None and read_noise > 0:
            return float(numpy.log2(float(full_well) / float(read_noise)))
        return None

    def label(self):
        return str(self)

    def id(self):
        return self._id

    def in_id(self, connection_type, gender=None):
        from ..utils import get_default_gender

        if gender is None:
            gender = get_default_gender(connection_type, is_input=True)
        parts = [self._id, connection_type.name, str(gender), self.IN]
        return self._SEPARATOR.join(parts)

    def out_id(self, connection_type, gender=None):
        from ..utils import get_default_gender

        if gender is None:
            gender = get_default_gender(connection_type, is_input=False)
        parts = [self._id, connection_type.name, str(gender), self.OUT]
        return self._SEPARATOR.join(parts)

    @staticmethod
    def get_parent_id(name: str):
        return name.split(OpticalEquipment._SEPARATOR)[0]

    def register(self, equipment):
        """
        Register this equipment in the optical graph.
        """
        self._register(equipment)

    def _register(self, equipment):
        # Register equipment node
        equipment.add_vertex(self.id(), self)

        # Register all inputs
        for connection_type, gender in self._inputs:
            self._register_input(equipment, connection_type, gender)

        # Register all outputs
        for connection_type, gender in self._outputs:
            self._register_output(equipment, connection_type, gender)

        # Register attached equipment
        for att in self.attached_equipment:
            att.register(equipment)
            # Add mechanical edge
            equipment.add_edge(self.id(), att.id())

    def _register_output(
        self, equipment, connection_type=ConnectionType.F_1_25, gender=None
    ):
        # Add output node
        equipment.add_vertex(
            self.out_id(connection_type, gender),
            node_type=OpticalType.OUTPUT,
            connection_type=connection_type,
            connection_gender=gender,
        )
        # Connect node to its output
        equipment.add_edge(self.id(), self.out_id(connection_type, gender))

    def _register_input(
        self, equipment, connection_type=ConnectionType.F_1_25, gender=None
    ):
        # Add input node
        equipment.add_vertex(
            self.in_id(connection_type, gender),
            node_type=OpticalType.INPUT,
            connection_type=connection_type,
            connection_gender=gender,
        )
        # Connect node to its input
        equipment.add_edge(self.in_id(connection_type, gender), self.id())

    def __str__(self):
        # Format: <vendor>
        return "{} f={}".format(self.get_vendor(), self.focal_length)


class IntermediateOpticalEquipment(OpticalEquipment):
    """
    Base class for intermediate optical equipment like Barlows, Diagonals, Filters, etc.
    """

    def __init__(
        self,
        vendor,
        optical_length=0.0,
        mass=0.0,
        in_connection=None,
        out_connection=None,
        # Legacy arguments for backward compatibility
        in_connection_type=None,
        out_connection_type=None,
        in_gender=None,
        out_gender=None,
        inputs=None,
        outputs=None,
    ):
        # Merge legacy arguments into new ones
        if in_connection is None:
            if in_connection_type is not None:
                in_connection = (in_connection_type, in_gender)
        if out_connection is None:
            if out_connection_type is not None:
                out_connection = (out_connection_type, out_gender)

        super(IntermediateOpticalEquipment, self).__init__(
            focal_length=0.0,
            vendor=vendor,
            optical_length=optical_length,
            mass=mass,
            inputs=inputs,
            outputs=outputs,
        )

        if in_connection:
            if isinstance(in_connection, tuple):
                self.add_input(*in_connection)
            else:
                self.add_input(in_connection)

        if out_connection:
            if isinstance(out_connection, tuple):
                self.add_output(*out_connection)
            else:
                self.add_output(out_connection)

    @property
    def in_connection_type(self):
        return self._inputs[0][0] if self._inputs else None

    @property
    def in_gender(self):
        return self._inputs[0][1] if self._inputs else None

    @property
    def out_connection_type(self):
        return self._outputs[0][0] if self._outputs else None

    @property
    def out_gender(self):
        return self._outputs[0][1] if self._outputs else None


class OutputOpticalEquipment(OpticalEquipment):
    def __init__(
        self,
        focal_length,
        vendor,
        optical_length=0.0,
        mass=0.0,
        inputs=None,
        outputs=None,
        connection_type=None,
        connection_gender=None,
    ):
        if inputs is None:
            if connection_type is not None:
                inputs = [(connection_type, connection_gender)]
        super().__init__(
            focal_length,
            vendor,
            optical_length=optical_length,
            mass=mass,
            inputs=inputs,
            outputs=outputs,
        )

    def is_visual_output(self) -> bool:
        """Indicates if the output is primarily for visual observation."""
        return True  # Default for eyepieces etc.

    def field_of_view(self, telescope, zoom, barlow_magnification):
        """Calculates field of view."""
        raise NotImplementedError("Subclasses must implement field_of_view")

    def field_of_view_width(self, telescope, zoom, barlow_magnification):
        """Calculates horizontal field of view."""
        return self.field_of_view(telescope, zoom, barlow_magnification)

    def field_of_view_height(self, telescope, zoom, barlow_magnification):
        """Calculates vertical field of view."""
        return self.field_of_view(telescope, zoom, barlow_magnification)

    def field_of_view_diagonal(self, telescope, zoom, barlow_magnification):
        """Calculates diagonal field of view."""
        return self.field_of_view(telescope, zoom, barlow_magnification)

    def _zoom_divider(self) -> Any:
        """Returns the zoom divider for this equipment."""
        raise NotImplementedError("Subclasses must implement _zoom_divider")

    def exit_pupil(self, telescope, zoom):
        ureg = get_unit_registry()
        # Default unit for exit pupil if telescope aperture is problematic
        default_mm_unit = ureg.mm

        # Validate telescope.aperture
        aperture = getattr(telescope, "aperture", None)
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
            result = telescope.aperture / zoom
            # Ensure result has the same dimensionality as aperture (length)
            # This is a safeguard; Pint should ensure this if zoom is dimensionless.
            # If zoom has units, this check becomes more critical.
            if result.dimensionality != telescope.aperture.dimensionality:
                return np.nan * aperture_units
            return result
        except Exception:  # Catch any error during division (e.g., unexpected Pint issue, DimensionalityError)
            return np.nan * aperture_units

    def brightness(self, telescope, zoom):
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

        ep_val = self.exit_pupil(telescope, zoom)  # This is now robust

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
