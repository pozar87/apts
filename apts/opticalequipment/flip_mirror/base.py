from ..abstract import IntermediateOpticalEquipment
from ...constants import OpticalType


class FlipMirror(IntermediateOpticalEquipment):
    @classmethod
    def from_database(cls, entry):
        from ...utils import Utils, Gender

        brand = entry["brand"]
        name = entry["name"]
        vendor = f"{brand} {name}"
        ol = entry.get("optical_length", 0)
        mass = entry.get("mass", 0)
        tt = Utils.map_conn(entry.get("tside_thread"))
        tg = Utils.map_gender(entry.get("tside_gender"))
        ct = Utils.map_conn(entry.get("cside_thread"))
        cg = Utils.map_gender(entry.get("cside_gender"))
        return cls(
            vendor,
            optical_length=ol,
            mass=mass,
            in_connection_type=tt,
            out_connection_type=ct,
            in_gender=tg or Gender.MALE,
            out_gender=cg or Gender.FEMALE,
        )

    def __init__(
        self,
        vendor,
        optical_length=0,
        mass=0,
        in_connection_type=None,
        out_connection_type=None,
        in_gender=None,
        out_gender=None,
        diagonal_connection_type=None,
        diagonal_gender=None,
    ):
        super(FlipMirror, self).__init__(
            vendor,
            optical_length=optical_length,
            mass=mass,
            in_connection_type=in_connection_type,
            out_connection_type=out_connection_type,
            in_gender=in_gender,
            out_gender=out_gender,
        )
        self._type = OpticalType.FLIP_MIRROR
        from ...utils import ConnectionType, Gender
        self.diagonal_connection_type = diagonal_connection_type or ConnectionType.F_1_25
        self.diagonal_gender = diagonal_gender or Gender.FEMALE

    def register(self, equipment):
        super(FlipMirror, self).register(equipment)
        # Add additional diagonal output
        self._register_output(equipment, self.diagonal_connection_type, self.diagonal_gender)

    _DATABASE = {}
