from ...utils import ConnectionType
from ..base import OpticalEquipment
from .calculations import normalize_barlow_database_entry


class Barlow(OpticalEquipment):
    @classmethod
    def normalize_database_entry(cls, entry: dict) -> dict:
        normalized = normalize_barlow_database_entry(entry)
        return super(Barlow, cls).normalize_database_entry(normalized)

    @classmethod
    def from_database(cls, entry: dict):
        normalized = cls.normalize_database_entry(entry)
        return cls(
            normalized["magnification"],
            vendor=normalized.get("vendor", "unknown barlow"),
            inputs=normalized.get("inputs"),
            outputs=normalized.get("outputs"),
            mass=normalized.get("mass", 0.0),
            optical_length=normalized.get("optical_length", 0.0),
        )

    """
    Class representing Barlow lenses
    """

    path_layer = 2

    def __init__(
        self,
        magnification,
        vendor="unknown barlow",
        inputs=None,
        outputs=None,
        mass=0.0,
        optical_length=0.0,
        connection_type=None,
        in_gender=None,
        out_gender=None,
    ):
        if inputs is None:
            if connection_type:
                inputs = [(connection_type, in_gender)]
            else:
                inputs = [ConnectionType.F_1_25]
        if outputs is None:
            if connection_type:
                outputs = [(connection_type, out_gender)]
            else:
                outputs = [ConnectionType.F_1_25]

        super(Barlow, self).__init__(
            0,
            vendor,
            mass=mass,
            optical_length=optical_length,
            inputs=inputs,
            outputs=outputs,
        )
        self.magnification = magnification

    @property
    def connection_type(self):
        return self._inputs[0][0] if self._inputs else None

    @property
    def in_gender(self):
        return self._inputs[0][1] if self._inputs else None

    @property
    def out_gender(self):
        return self._outputs[0][1] if self._outputs else None

    def register(self, equipment):
        """
        Register barlow lens in optical equipment graph. Barlow node is build out of three vertices:
        barlow node its input and output. Barlow node is automatically connected with them.
        """
        # Add barlow lens node
        super(Barlow, self).register(equipment)

    def __str__(self):
        # Format: <vendor> x<magnification>
        return "{} x{}".format(self.get_vendor(), self.magnification)

    _DATABASE = {}
