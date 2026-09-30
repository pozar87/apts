from typing import ClassVar

from ...constants import OpticalType
from ..base import IntermediateOpticalEquipment


class Adapter(IntermediateOpticalEquipment):
    _DATABASE: ClassVar[dict] = {}

    @classmethod
    def from_database(cls, entry):
        from .calculations import normalize_adapter_database_entry

        entry = normalize_adapter_database_entry(entry)
        vendor = entry["vendor"]
        ol = entry["optical_length"]
        mass = entry["mass"]
        inputs = entry["inputs"]
        outputs = entry["outputs"]

        return cls(vendor, optical_length=ol, mass=mass, inputs=inputs, outputs=outputs)

    def __init__(
        self,
        vendor,
        optical_length=0.0,
        mass=0.0,
        inputs=None,
        outputs=None,
        in_connection=None,
        out_connection=None,
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
        self._type = OpticalType.ADAPTER


class Spacer(IntermediateOpticalEquipment):
    _DATABASE: ClassVar[dict] = {}

    @classmethod
    def from_database(cls, entry):
        from .calculations import normalize_adapter_database_entry

        entry = normalize_adapter_database_entry(entry)
        vendor = entry["vendor"]
        ol = entry["optical_length"]
        mass = entry["mass"]
        inputs = entry["inputs"]
        outputs = entry["outputs"]

        return cls(vendor, optical_length=ol, mass=mass, inputs=inputs, outputs=outputs)

    def __init__(
        self,
        vendor,
        optical_length=0.0,
        mass=0.0,
        inputs=None,
        outputs=None,
        in_connection=None,
        out_connection=None,
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
        self._type = OpticalType.SPACER
