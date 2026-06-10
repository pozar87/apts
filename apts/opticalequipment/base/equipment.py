import uuid
from typing import Any, cast

import numpy as np

from ...constants import OpticalType
from ...i18n import gettext_
from ...units import get_unit_registry
from ...utils import ConnectionType


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
            return [
                cls.normalize_database_entry(e)
                for e in cast(dict, cls._DATABASE).values()
            ]
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
        from ...utils import get_default_gender

        if gender is None:
            gender = get_default_gender(connection_type, is_input=True)
        self._inputs.append((connection_type, gender))

    def add_output(self, connection_type, gender=None):
        """
        Add an output port to this equipment.
        """
        from ...utils import get_default_gender

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
        from ...utils import get_default_gender

        if gender is None:
            gender = get_default_gender(connection_type, is_input=True)
        parts = [self._id, connection_type.name, str(gender), self.IN]
        return self._SEPARATOR.join(parts)

    def out_id(self, connection_type, gender=None):
        from ...utils import get_default_gender

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
