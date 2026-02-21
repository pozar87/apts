from .abstract import IntermediateOpticalEquipment
from ..constants import OpticalType
from ..utils import ConnectionType

class Rotator(IntermediateOpticalEquipment):
    def __init__(self, vendor, optical_length=0, mass=0, in_connection_type=None, out_connection_type=None, in_gender=None, out_gender=None):
        super(Rotator, self).__init__(
            vendor, optical_length=optical_length, mass=mass,
            in_connection_type=in_connection_type, out_connection_type=out_connection_type,
            in_gender=in_gender, out_gender=out_gender
        )
        self._type = OpticalType.ROTATOR

    @classmethod
    def Pegasus_Falcon(cls):
        return cls("Pegasus Falcon Rotator", optical_length=18, mass=700, in_connection_type=ConnectionType.M54, out_connection_type=ConnectionType.M54)

    @classmethod
    def Wanderer_Rotator_M54(cls):
        return cls("Wanderer Rotator M54", optical_length=10, mass=400, in_connection_type=ConnectionType.M54, out_connection_type=ConnectionType.M54)
