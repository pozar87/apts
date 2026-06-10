from ..base import IntermediateOpticalEquipment
from ...constants import OpticalType


class FilterWheel(IntermediateOpticalEquipment):
    _DATABASE = {}

    @classmethod
    def from_database(cls, entry):
        from ...utils import map_conn, map_gender

        brand = entry["brand"]
        name = entry["name"]
        vendor = f"{brand} {name}"
        ol = entry.get("optical_length", 0)
        mass = entry.get("mass", 0)
        tt = map_conn(entry.get("tside_thread"))
        tg = map_gender(entry.get("tside_gender"))
        ct = map_conn(entry.get("cside_thread"))
        cg = map_gender(entry.get("cside_gender"))

        inputs = entry.get("inputs")
        if inputs is None:
            inputs = [(tt, tg)] if tt else []
        else:
            inputs = [(map_conn(c), map_gender(g)) if isinstance(c, str) else (c, g) for c, g in inputs]

        outputs = entry.get("outputs")
        if outputs is None:
            outputs = [(ct, cg)] if ct else []
        else:
            outputs = [(map_conn(c), map_gender(g)) if isinstance(c, str) else (c, g) for c, g in outputs]

        return cls(
            vendor,
            optical_length=ol,
            mass=mass,
            inputs=inputs,
            outputs=outputs,
        )

    def __init__(
        self,
        vendor,
        optical_length=0,
        mass=0,
        inputs=None,
        outputs=None,
        in_connection=None,
        out_connection=None,
    ):
        super(FilterWheel, self).__init__(
            vendor,
            optical_length=optical_length,
            mass=mass,
            inputs=inputs,
            outputs=outputs,
            in_connection=in_connection,
            out_connection=out_connection,
        )
        self._type = OpticalType.FILTER_WHEEL
        self.filters = []

    def add_filter(self, filter):
        """
        Add a filter to the filter wheel.
        """
        self.filters.append(filter)
        self.attach(filter)

    def register(self, equipment):
        super(FilterWheel, self).register(equipment)
        for f in self.filters:
            # Connect filter wheel node to filter input
            # This allows the optical path to go: Wheel_IN -> Wheel_Node -> Filter_IN -> Filter_Node -> Filter_OUT -> Wheel_OUT
            equipment.add_edge(self.id(), f.in_id(f.in_connection_type, f.in_gender))
            # Connect filter output to filter wheel output
            equipment.add_edge(f.out_id(f.out_connection_type, f.out_gender), self.out_id(self.out_connection_type, self.out_gender))


class FilterHolder(IntermediateOpticalEquipment):
    _DATABASE = {}

    @classmethod
    def from_database(cls, entry):
        from ...utils import map_conn, map_gender

        brand = entry["brand"]
        name = entry["name"]
        vendor = f"{brand} {name}"
        ol = entry.get("optical_length", 0)
        mass = entry.get("mass", 0)
        tt = map_conn(entry.get("tside_thread"))
        tg = map_gender(entry.get("tside_gender"))
        ct = map_conn(entry.get("cside_thread"))
        cg = map_gender(entry.get("cside_gender"))

        inputs = entry.get("inputs")
        if inputs is None:
            inputs = [(tt, tg)] if tt else []
        else:
            inputs = [(map_conn(c), map_gender(g)) if isinstance(c, str) else (c, g) for c, g in inputs]

        outputs = entry.get("outputs")
        if outputs is None:
            outputs = [(ct, cg)] if ct else []
        else:
            outputs = [(map_conn(c), map_gender(g)) if isinstance(c, str) else (c, g) for c, g in outputs]

        return cls(
            vendor,
            optical_length=ol,
            mass=mass,
            inputs=inputs,
            outputs=outputs,
        )

    def __init__(
        self,
        vendor,
        optical_length=0,
        mass=0,
        inputs=None,
        outputs=None,
        in_connection=None,
        out_connection=None,
    ):
        super(FilterHolder, self).__init__(
            vendor,
            optical_length=optical_length,
            mass=mass,
            inputs=inputs,
            outputs=outputs,
            in_connection=in_connection,
            out_connection=out_connection,
        )
        self._type = OpticalType.FILTER_HOLDER
        self.filters = []

    def add_filter(self, filter):
        """
        Add a filter to the filter holder.
        """
        self.filters.append(filter)
        self.attach(filter)

    def register(self, equipment):
        super(FilterHolder, self).register(equipment)
        for f in self.filters:
            # Connect filter holder node to filter input
            equipment.add_edge(self.id(), f.in_id(f.in_connection_type, f.in_gender))
            # Connect filter output to filter holder output
            equipment.add_edge(f.out_id(f.out_connection_type, f.out_gender), self.out_id(self.out_connection_type, self.out_gender))
