from ..utils import ConnectionType, Gender
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
        super(Filter, self).__init__(
            vendor, optical_length=optical_length, mass=mass,
            in_connection_type=connection_type, out_connection_type=connection_type,
            in_gender=Gender.MALE, out_gender=Gender.FEMALE
        )
        self.name = name
        self.transmission = transmission

    def register(self, equipment):
        """
        Register filter in optical equipment graph.
        """
        super(Filter, self).register(equipment)

    def __str__(self):
        return f"{self.name} ({self.vendor})"

    @classmethod
    def Optolong_L_Pro_2_inch(cls):
        return cls("L-Pro", "Optolong", connection_type=ConnectionType.F_2, transmission=0.9)

    @classmethod
    def Baader_UHC_S_1_25_inch(cls):
        return cls("UHC-S", "Baader", connection_type=ConnectionType.F_1_25, transmission=0.95)
