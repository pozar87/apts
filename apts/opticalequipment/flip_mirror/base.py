from typing import ClassVar

from ...constants import OpticalType
from ..base import IntermediateOpticalEquipment
from .calculations import normalize_flip_mirror_database_entry


class FlipMirror(IntermediateOpticalEquipment):
    _DATABASE: ClassVar[dict] = {}

    @classmethod
    def normalize_database_entry(cls, entry: dict) -> dict:
        norm_entry = normalize_flip_mirror_database_entry(entry)
        return super().normalize_database_entry(norm_entry)

    @classmethod
    def normalize_database_entry(cls, entry: dict) -> dict:
        norm_entry = normalize_flip_mirror_database_entry(entry)
        return super().normalize_database_entry(norm_entry)

    @classmethod
    def from_database(cls, entry):
        normalized = cls.normalize_database_entry(entry)
        return cls(
            vendor=normalized["vendor"],
            optical_length=normalized.get("optical_length", 0),
            mass=normalized.get("mass", 0),
            inputs=normalized.get("inputs"),
            outputs=normalized.get("outputs"),
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
        diagonal_connection=None,
    ):
        super().__init__(
            vendor,
            optical_length=optical_length,
            mass=mass,
            inputs=inputs,
            outputs=outputs,
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
        super().register(equipment)

    _DATABASE: ClassVar[dict] = {}
