from ..base import IntermediateOpticalEquipment
from ...constants import OpticalType
from .calculations import normalize_oag_database_entry


class OAG(IntermediateOpticalEquipment):
    _DATABASE = {}

    @classmethod
    def normalize_database_entry(cls, entry: dict) -> dict:
        norm_entry = normalize_oag_database_entry(entry)
        return super().normalize_database_entry(norm_entry)

    @classmethod
    def from_database(cls, entry):
        norm = normalize_oag_database_entry(entry)
        return cls(
            vendor=norm["vendor"],
            optical_length=norm.get("optical_length", 0),
            mass=norm.get("mass", 0),
            inputs=norm.get("inputs"),
            outputs=norm.get("outputs"),
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
        guide_connection=None,
    ):
        super(OAG, self).__init__(
            vendor,
            optical_length=optical_length,
            mass=mass,
            inputs=inputs,
            outputs=outputs,
            in_connection=in_connection,
            out_connection=out_connection,
        )
        self._type = OpticalType.OAG
        if guide_connection:
            if isinstance(guide_connection, tuple):
                self.add_output(*guide_connection)
            else:
                self.add_output(guide_connection)
        else:
            from ...utils import ConnectionType
            self.add_output(ConnectionType.M42)

    @property
    def guide_connection_type(self):
        return self._outputs[1][0] if len(self._outputs) > 1 else None

    @property
    def guide_gender(self):
        return self._outputs[1][1] if len(self._outputs) > 1 else None

    def register(self, equipment):
        super(OAG, self).register(equipment)
