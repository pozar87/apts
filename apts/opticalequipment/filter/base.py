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

    @staticmethod
    def _genders_for_connection_type(connection_type):
        """
        Determine input/output genders based on the connection type convention.

        For push-fit connections (F_1_25, F_2):
          - Telescope OUTPUT is FEMALE (receiver), Eyepiece INPUT is MALE (barrel)
          - So a filter between them needs IN=MALE (to go into telescope), OUT=FEMALE (to receive eyepiece)

        For threaded connections (T2, M42, M48, etc.):
          - Telescope OUTPUT is MALE (thread), Camera INPUT is FEMALE (receiver)
          - So a filter between them needs IN=FEMALE, OUT=MALE
        """
        if connection_type in (ConnectionType.F_1_25, ConnectionType.F_2):
            return Gender.MALE, Gender.FEMALE
        else:
            return Gender.FEMALE, Gender.MALE

    def __init__(
        self,
        name,
        vendor="unknown filter",
        connection_type=ConnectionType.F_1_25,
        transmission=1.0,
        optical_length=0,
        mass=0,
    ):
        in_gender, out_gender = self._genders_for_connection_type(connection_type)
        super(Filter, self).__init__(
            vendor,
            optical_length=optical_length,
            mass=mass,
            in_connection_type=connection_type,
            out_connection_type=connection_type,
            in_gender=in_gender,
            out_gender=out_gender,
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
