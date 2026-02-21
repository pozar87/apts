from .abstract import IntermediateOpticalEquipment
from ..constants import OpticalType
from ..utils import ConnectionType

class OAG(IntermediateOpticalEquipment):
    def __init__(self, vendor, optical_length=0, mass=0, in_connection_type=None, out_connection_type=None, in_gender=None, out_gender=None):
        super(OAG, self).__init__(
            vendor, optical_length=optical_length, mass=mass,
            in_connection_type=in_connection_type, out_connection_type=out_connection_type,
            in_gender=in_gender, out_gender=out_gender
        )
        self._type = OpticalType.OAG

    @classmethod
    def ZWO_OAG(cls):
        return cls("ZWO OAG", optical_length=16.5, mass=200, in_connection_type=ConnectionType.M48, out_connection_type=ConnectionType.M42)

    @classmethod
    def ZWO_OAG_L(cls):
        return cls("ZWO OAG-L", optical_length=17.5, mass=300, in_connection_type=ConnectionType.M68, out_connection_type=ConnectionType.M42)
