from ..base import IntermediateOpticalEquipment
from ...constants import OpticalType
from .calculations import normalize_anti_tilt_database_entry


class AntiTilt(IntermediateOpticalEquipment):
    @classmethod
    def from_database(cls, entry):
        normalized = normalize_anti_tilt_database_entry(entry)
        return cls(
            normalized["vendor"],
            optical_length=normalized["optical_length"],
            mass=normalized["mass"],
            inputs=normalized["inputs"],
            outputs=normalized["outputs"],
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
        super(AntiTilt, self).__init__(
            vendor,
            optical_length=optical_length,
            mass=mass,
            inputs=inputs,
            outputs=outputs,
            in_connection=in_connection,
            out_connection=out_connection,
        )
        self._type = OpticalType.ANTI_TILT

    _DATABASE = {}
