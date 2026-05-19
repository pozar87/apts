from ...utils import ConnectionType, Gender
from ..abstract import IntermediateOpticalEquipment


class Filter(IntermediateOpticalEquipment):
    """
    Class representing a filter.
    """

    _DATABASE = {}

    @classmethod
    def from_database(cls, entry):
        from ...utils import map_conn
        brand = entry.get("brand", "Unknown")
        name = entry.get("name", "Unknown")
        vendor = f"{brand} {name}"
        tt = map_conn(entry.get("tside_thread"))
        # Filters usually have the same thread on both sides or are just glass.
        # Defaulting to 1.25" if not specified.
        conn = tt or ConnectionType.F_1_25
        trans = entry.get("transmission", 1.0)
        ol = entry.get("optical_length", 0)
        mass = entry.get("mass", 0)
        return cls(
            name,
            vendor=vendor,
            connection_type=conn,
            transmission=trans,
            optical_length=ol,
            mass=mass,
        )

    def __init__(
        self,
        name,
        vendor="unknown filter",
        connection_type=ConnectionType.F_1_25,
        transmission=1.0,
        optical_length=0,
        mass=0,
    ):
        super(Filter, self).__init__(
            vendor,
            optical_length=optical_length,
            mass=mass,
            in_connection_type=connection_type,
            out_connection_type=connection_type,
            in_gender=Gender.MALE,
            out_gender=Gender.FEMALE,
        )
        self.name = name
        self.transmission = transmission

    def register(self, equipment):
        """
        Register filter in optical equipment graph.
        """
        super(Filter, self).register(equipment)

    def __str__(self):
        return f"{self.name} ({self.vendor})"
