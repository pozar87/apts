from typing import ClassVar

from ...utils import ConnectionType
from ..base import IntermediateOpticalEquipment
from .calculations import normalize_barlow_database_entry


class Barlow(IntermediateOpticalEquipment):
    """
    Class representing Barlow lenses.
    """

    path_layer = 2
    _DATABASE: ClassVar[dict] = {}

    @classmethod
    def normalize_database_entry(cls, entry: dict) -> dict:
        return normalize_barlow_database_entry(entry)

    @classmethod
    def from_database(cls, entry: dict):
        normalized = cls.normalize_database_entry(entry)
        return cls(
            magnification=normalized.get("magnification", 2.0),
            vendor=normalized.get("vendor", "unknown barlow"),
            inputs=normalized.get("inputs"),
            outputs=normalized.get("outputs"),
            mass=normalized.get("mass", 0.0),
            optical_length=normalized.get("optical_length", 0.0),
        )

    def __init__(
        self,
        magnification=2.0,
        vendor="unknown barlow",
        optical_length=0.0,
        mass=0.0,
        inputs=None,
        outputs=None,
        in_connection=None,
        out_connection=None,
        in_connection_type=None,
        out_connection_type=None,
        in_gender=None,
        out_gender=None,
        connection_type=None,
    ):
        if isinstance(magnification, str):
            if isinstance(vendor, (int, float)):
                magnification, vendor = vendor, magnification
            else:
                vendor, magnification = magnification, 2.0
        elif isinstance(vendor, (int, float)):
            magnification, vendor = vendor, "unknown barlow"

        if inputs is None and in_connection is None and in_connection_type is None:
            if connection_type:
                in_connection = (connection_type, in_gender)
            else:
                in_connection = ConnectionType.F_1_25

        if outputs is None and out_connection is None and out_connection_type is None:
            if connection_type:
                out_connection = (connection_type, out_gender)
            else:
                out_connection = ConnectionType.F_1_25

        super().__init__(
            vendor=vendor,
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
        self.magnification = magnification

    def __str__(self):
        # Format: <vendor> x<magnification>
        return f"{self.get_vendor()} x{self.magnification}"
