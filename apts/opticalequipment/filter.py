from ..utils import ConnectionType
from .abstract import IntermediateOpticalEquipment


class Filter(IntermediateOpticalEquipment):
    """
    Class representing a filter.
    """

    def __init__(self, name, vendor="unknown filter", connection_type=ConnectionType.F_1_25):
        super(Filter, self).__init__(vendor)
        self.connection_type = connection_type
        self.name = name

    def register(self, equipment):
        """
        Register filter in optical equipment graph.
        """
        super(Filter, self)._register(equipment, self.connection_type, self.connection_type)

    def __str__(self):
        return f"{self.name} ({self.vendor})"
