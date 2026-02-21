from ..utils import ConnectionType
from .abstract import IntermediateOpticalEquipment


class Filter(IntermediateOpticalEquipment):
    """
    Class representing a filter.
    """

    def __init__(
        self,
        name,
        vendor="unknown filter",
        connection_type=ConnectionType.F_1_25,
        transmission=1.0,
        optical_length=0,
        mass=0
    ):
        super(Filter, self).__init__(vendor, optical_length=optical_length, mass=mass, in_connection_type=connection_type, out_connection_type=connection_type)
        self.name = name
        self.transmission = transmission

    def register(self, equipment):
        """
        Register filter in optical equipment graph.
        """
        super(Filter, self).register(equipment)

    def __str__(self):
        return f"{self.name} ({self.vendor})"
