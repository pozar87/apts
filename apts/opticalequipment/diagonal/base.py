from ...utils import ConnectionType
from ..base import IntermediateOpticalEquipment
from .calculations import normalize_diagonal_database_entry


class Diagonal(IntermediateOpticalEquipment):
    """
    Class representing a star diagonal.
    """

    path_layer = 2

    @classmethod
    def normalize_database_entry(cls, entry: dict) -> dict:
        norm_entry = normalize_diagonal_database_entry(entry)
        return super().normalize_database_entry(norm_entry)

    @classmethod
    def from_database(cls, entry):
        norm = normalize_diagonal_database_entry(entry)
        return cls(
            vendor=norm["vendor"],
            is_erecting=norm.get("is_erecting", False),
            optical_length=norm.get("optical_length", 0),
            mass=norm.get("mass", 0),
            inputs=norm.get("inputs"),
            outputs=norm.get("outputs"),
        )

    def __init__(
        self,
        vendor="unknown diagonal",
        is_erecting=False,
        optical_length=0.0,
        mass=0.0,
        inputs=None,
        outputs=None,
        in_connection=None,
        out_connection=None,
        connection_type=None,
        in_gender=None,
        out_gender=None,
    ):
        if inputs is None and in_connection is None:
            if connection_type:
                in_connection = (connection_type, in_gender)
            else:
                in_connection = ConnectionType.F_1_25

        if outputs is None and out_connection is None:
            if connection_type:
                out_connection = (connection_type, out_gender)
            else:
                out_connection = ConnectionType.F_1_25

        super().__init__(
            vendor,
            optical_length=optical_length,
            mass=mass,
            inputs=inputs,
            outputs=outputs,
            in_connection=in_connection,
            out_connection=out_connection,
        )
        self.is_erecting = is_erecting

    @property
    def connection_type(self):
        return self.in_connection_type

    def register(self, equipment):
        """
        Register diagonal in optical equipment graph.
        """
        super().register(equipment)

    def __str__(self):
        return f"{self.vendor}"

    _DATABASE = {}
