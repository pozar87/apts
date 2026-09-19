from typing import ClassVar

from ...constants import OpticalType
from ...units import get_unit_registry
from ..base import IntermediateOpticalEquipment
from .calculations import normalize_reducer_database_entry


class Reducer(IntermediateOpticalEquipment):
    path_layer = 2
    _DATABASE: ClassVar[dict] = {}

    @classmethod
    def normalize_database_entry(cls, entry: dict) -> dict:
        return normalize_reducer_database_entry(
            entry, default_magnification=0.8, parse_magnification=True
        )

    @classmethod
    def from_database(cls, entry):
        norm = cls.normalize_database_entry(entry)
        return cls(
            norm["vendor"],
            magnification=norm["magnification"],
            optical_length=norm["optical_length"],
            mass=norm["mass"],
            required_backfocus=norm["required_backfocus"],
            inputs=norm["inputs"],
            outputs=norm["outputs"],
        )

    def __init__(
        self,
        vendor,
        magnification=0.8,
        optical_length=0,
        mass=0,
        required_backfocus=None,
        inputs=None,
        outputs=None,
        in_connection=None,
        out_connection=None,
        in_connection_type=None,
        out_connection_type=None,
        in_gender=None,
        out_gender=None,
    ):
        super().__init__(
            vendor,
            optical_length=optical_length,
            mass=mass,
            inputs=inputs,
            outputs=outputs,
            in_connection=in_connection,
            out_connection=out_connection,
            in_connection_type=in_connection_type,
            out_connection_type=out_connection_type,
            in_gender=in_gender,
            out_gender=out_gender,
        )
        self._type = OpticalType.REDUCER
        self.magnification = magnification
        self.required_backfocus = (
            required_backfocus * get_unit_registry().mm
            if required_backfocus is not None
            else None
        )


class Flattener(IntermediateOpticalEquipment):
    path_layer = 2
    _DATABASE: ClassVar[dict] = {}

    @classmethod
    def normalize_database_entry(cls, entry: dict) -> dict:
        return normalize_reducer_database_entry(
            entry, default_magnification=1.0, parse_magnification=False
        )

    @classmethod
    def from_database(cls, entry):
        norm = cls.normalize_database_entry(entry)
        return cls(
            norm["vendor"],
            magnification=norm["magnification"],
            optical_length=norm["optical_length"],
            mass=norm["mass"],
            required_backfocus=norm["required_backfocus"],
            inputs=norm["inputs"],
            outputs=norm["outputs"],
        )

    def __init__(
        self,
        vendor,
        magnification=1.0,
        optical_length=0,
        mass=0,
        required_backfocus=None,
        inputs=None,
        outputs=None,
        in_connection=None,
        out_connection=None,
        in_connection_type=None,
        out_connection_type=None,
        in_gender=None,
        out_gender=None,
    ):
        super().__init__(
            vendor,
            optical_length=optical_length,
            mass=mass,
            inputs=inputs,
            outputs=outputs,
            in_connection=in_connection,
            out_connection=out_connection,
            in_connection_type=in_connection_type,
            out_connection_type=out_connection_type,
            in_gender=in_gender,
            out_gender=out_gender,
        )
        self._type = OpticalType.FLATTENER
        self.magnification = magnification
        self.required_backfocus = (
            required_backfocus * get_unit_registry().mm
            if required_backfocus is not None
            else None
        )


class Corrector(IntermediateOpticalEquipment):
    path_layer = 2
    _DATABASE: ClassVar[dict] = {}

    @classmethod
    def normalize_database_entry(cls, entry: dict) -> dict:
        return normalize_reducer_database_entry(
            entry, default_magnification=1.0, parse_magnification=False
        )

    @classmethod
    def from_database(cls, entry):
        norm = cls.normalize_database_entry(entry)
        return cls(
            norm["vendor"],
            magnification=norm["magnification"],
            optical_length=norm["optical_length"],
            mass=norm["mass"],
            required_backfocus=norm["required_backfocus"],
            inputs=norm["inputs"],
            outputs=norm["outputs"],
        )

    def __init__(
        self,
        vendor,
        magnification=1.0,
        optical_length=0,
        mass=0,
        required_backfocus=None,
        inputs=None,
        outputs=None,
        in_connection=None,
        out_connection=None,
        in_connection_type=None,
        out_connection_type=None,
        in_gender=None,
        out_gender=None,
    ):
        super().__init__(
            vendor,
            optical_length=optical_length,
            mass=mass,
            inputs=inputs,
            outputs=outputs,
            in_connection=in_connection,
            out_connection=out_connection,
            in_connection_type=in_connection_type,
            out_connection_type=out_connection_type,
            in_gender=in_gender,
            out_gender=out_gender,
        )
        self._type = OpticalType.CORRECTOR
        self.magnification = magnification
        self.required_backfocus = (
            required_backfocus * get_unit_registry().mm
            if required_backfocus is not None
            else None
        )
