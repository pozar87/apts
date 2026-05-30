from ..abstract import IntermediateOpticalEquipment
from ...constants import OpticalType


class FlipMirror(IntermediateOpticalEquipment):
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
        return cls(
            vendor,
            optical_length=ol,
            mass=mass,
            in_connection=(tt, tg) if tt else None,
            out_connection=(ct, cg) if ct else None,
        )

    def __init__(
        self,
        vendor,
        optical_length=0,
        mass=0,
        in_connection=None,
        out_connection=None,
        diagonal_connection=None,
    ):
        super(FlipMirror, self).__init__(
            vendor,
            optical_length=optical_length,
            mass=mass,
            in_connection=in_connection,
            out_connection=out_connection,
        )
        self._type = OpticalType.FLIP_MIRROR
        if diagonal_connection:
            if isinstance(diagonal_connection, tuple):
                self.add_output(*diagonal_connection)
            else:
                self.add_output(diagonal_connection)
        else:
            from ...utils import ConnectionType
            self.add_output(ConnectionType.F_1_25)

    @property
    def diagonal_connection_type(self):
        return self._outputs[1][0] if len(self._outputs) > 1 else None

    @property
    def diagonal_gender(self):
        return self._outputs[1][1] if len(self._outputs) > 1 else None

    def register(self, equipment):
        super(FlipMirror, self).register(equipment)

    _DATABASE = {}
