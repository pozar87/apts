from ...utils import ConnectionType, Gender
from ..abstract import IntermediateOpticalEquipment


class Filter(IntermediateOpticalEquipment):
    """
    Class representing a filter.
    """

    path_layer = 4

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
        in_connection=None,
        out_connection=None,
    ):
        super(Filter, self).__init__(
            vendor,
            optical_length=optical_length,
            mass=mass,
            in_connection=in_connection or connection_type,
            out_connection=out_connection or connection_type,
        )
        self.name = name
        self.transmission = transmission


    def __str__(self):
        return f"{self.name} ({self.vendor})"
