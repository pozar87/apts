from ..utils import ConnectionType, Gender
from .abstract import IntermediateOpticalEquipment


class Diagonal(IntermediateOpticalEquipment):
    """
    Class representing a star diagonal.
    """

    def __init__(self, vendor="unknown diagonal", connection_type=ConnectionType.F_1_25, is_erecting=False, t2_output=False, optical_length=0, mass=0):
        super(Diagonal, self).__init__(
            vendor, optical_length=optical_length, mass=mass,
            in_connection_type=connection_type, out_connection_type=connection_type,
            in_gender=Gender.MALE, out_gender=Gender.FEMALE
        )
        self.connection_type = connection_type
        self.is_erecting = is_erecting
        self.t2_output = t2_output

    def register(self, equipment):
        """
        Register diagonal in optical equipment graph.
        """
        super(Diagonal, self).register(equipment)
        if self.t2_output:
            self._register_output(equipment, ConnectionType.T2)

    def __str__(self):
        return f"{self.vendor}"
