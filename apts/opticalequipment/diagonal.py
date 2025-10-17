from ..utils import ConnectionType
from .abstract import IntermediateOpticalEquipment


class Diagonal(IntermediateOpticalEquipment):
    """
    Class representing a star diagonal.
    """

    def __init__(self, vendor="unknown diagonal", connection_type=ConnectionType.F_1_25):
        super(Diagonal, self).__init__(vendor)
        self.connection_type = connection_type

    def register(self, equipment):
        """
        Register diagonal in optical equipment graph.
        """
        super(Diagonal, self)._register(equipment, self.connection_type, self.connection_type)

    def __str__(self):
        return f"{self.vendor}"