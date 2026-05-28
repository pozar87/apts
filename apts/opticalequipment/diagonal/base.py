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
        from ...utils import map_conn, map_gender, Gender

        brand = entry["brand"]
        name = entry["name"]
        vendor = f"{brand} {name}"
        ol = entry.get("optical_length", 0)
        mass = entry.get("mass", 0)
        tt = map_conn(entry.get("tside_thread"))
        tg = map_gender(entry.get("tside_gender"))
        ct = map_conn(entry.get("cside_thread"))
        cg = map_gender(entry.get("cside_gender"))
        return cls(
            vendor,
            optical_length=ol,
            mass=mass,
            in_connection_type=tt,
            out_connection_type=ct,
            in_gender=tg or Gender.MALE,
            out_gender=cg or Gender.FEMALE,
        )

    """
    Class representing a star diagonal.
    """

    def __init__(
        self,
        vendor="unknown diagonal",
        connection_type=ConnectionType.F_1_25,
        is_erecting=False,
        t2_output=False,
        optical_length=0.0,
        mass=0.0,
        in_connection_type=None,
        out_connection_type=None,
        in_gender=None,
        out_gender=None,
    ):
        super(Diagonal, self).__init__(
            vendor,
            optical_length=optical_length,
            mass=mass,
            in_connection_type=in_connection_type or connection_type,
            out_connection_type=out_connection_type or connection_type,
            in_gender=in_gender or Gender.MALE,
            out_gender=out_gender or Gender.FEMALE,
        )
        self.connection_type = connection_type or in_connection_type
        self.is_erecting = is_erecting
        self.t2_output = t2_output

        if self.t2_output:
            self.add_output(ConnectionType.T2, Gender.MALE)

    def register(self, equipment):
        """
        Register diagonal in optical equipment graph.
        """
        super(Diagonal, self).register(equipment)

    def __str__(self):
        return f"{self.vendor}"

    _DATABASE = {}
