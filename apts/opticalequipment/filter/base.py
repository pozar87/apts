from typing import ClassVar

from ...utils import ConnectionType
from ..base import IntermediateOpticalEquipment
from .calculations import normalize_filter_database_entry


class Filter(IntermediateOpticalEquipment):
    """
    Class representing a filter.
    """

    path_layer = 4

    _DATABASE: ClassVar[dict] = {}

    @classmethod
    def normalize_database_entry(cls, entry: dict) -> dict:
        normalized = normalize_filter_database_entry(entry)
        return super().normalize_database_entry(normalized)

    @classmethod
    def from_database(cls, entry: dict):
        normalized = cls.normalize_database_entry(entry)
        return cls(
            normalized["name"],
            vendor=normalized["vendor"],
            connection_type=normalized["connection_type"],
            transmission=normalized["transmission"],
            optical_length=normalized["optical_length"],
            mass=normalized["mass"],
            inputs=normalized["inputs"],
            outputs=normalized["outputs"],
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
        inputs=None,
        outputs=None,
    ):
        super().__init__(
            vendor,
            optical_length=optical_length,
            mass=mass,
            in_connection=in_connection or connection_type,
            out_connection=out_connection or connection_type,
            inputs=inputs,
            outputs=outputs,
        )
        self.name = name
        self.transmission = transmission

    def __str__(self):
        return f"{self.name} ({self.vendor})"
