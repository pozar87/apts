from ..abstract import IntermediateOpticalEquipment
from ...utils import ConnectionType, Gender


class Diagonal(IntermediateOpticalEquipment):
    @classmethod
    def normalize_database_entry(cls, entry: dict) -> dict:
        from ...utils import map_conn, map_gender, Gender
        entry = entry.copy()
        if "in_connection_type" not in entry and "tside_thread" in entry:
            entry["in_connection_type"] = map_conn(entry.get("tside_thread")).value
        if "out_connection_type" not in entry and "cside_thread" in entry:
            entry["out_connection_type"] = map_conn(entry.get("cside_thread")).value
        if "in_gender" not in entry and "tside_gender" in entry:
            entry["in_gender"] = (map_gender(entry.get("tside_gender")) or Gender.MALE).value
        if "out_gender" not in entry and "cside_gender" in entry:
            entry["out_gender"] = (map_gender(entry.get("cside_gender")) or Gender.MALE).value
        return super(Diagonal, cls).normalize_database_entry(entry)

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
            from ...utils import map_conn, map_gender
            inputs = [(map_conn(c), map_gender(g)) if isinstance(c, str) else (c, g) for c, g in inputs]

        outputs = entry.get("outputs")
        if outputs is None:
            outputs = [(ct, cg)] if ct else []
            if entry.get("t2_output", False):
                from ...utils import Gender
                outputs.append((ConnectionType.T2, Gender.MALE))
        else:
            from ...utils import map_conn, map_gender
            outputs = [(map_conn(c), map_gender(g)) if isinstance(c, str) else (c, g) for c, g in outputs]

        return cls(
            vendor,
            optical_length=ol,
            mass=mass,
            inputs=inputs,
            outputs=outputs,
        )

    """
    Class representing a star diagonal.
    """

    path_layer = 2

    def __init__(
        self,
        vendor="unknown diagonal",
        is_erecting=False,
        optical_length=0.0,
        mass=0.0,
        inputs=None,
        outputs=None,
        in_connection=None,
        out_connection=None,
        connection_type=None,
        in_gender=None,
        out_gender=None,
    ):
        if inputs is None and in_connection is None:
            if connection_type:
                in_connection = (connection_type, in_gender)
            else:
                in_connection = ConnectionType.F_1_25

        if outputs is None and out_connection is None:
            if connection_type:
                out_connection = (connection_type, out_gender)
            else:
                out_connection = ConnectionType.F_1_25

        super(Diagonal, self).__init__(
            vendor,
            optical_length=optical_length,
            mass=mass,
            inputs=inputs,
            outputs=outputs,
            in_connection=in_connection,
            out_connection=out_connection,
        )
        self.is_erecting = is_erecting

    @property
    def connection_type(self):
        return self.in_connection_type

    def register(self, equipment):
        """
        Register diagonal in optical equipment graph.
        """
        super(Diagonal, self).register(equipment)

    def __str__(self):
        return f"{self.vendor}"

    _DATABASE = {}
