from .abstract import IntermediateOpticalEquipment
from ..constants import OpticalType
from ..utils import ConnectionType

class Adapter(IntermediateOpticalEquipment):
    def __init__(self, vendor, optical_length=0, mass=0, in_connection_type=None, out_connection_type=None, in_gender=None, out_gender=None):
        super(Adapter, self).__init__(
            vendor, optical_length=optical_length, mass=mass,
            in_connection_type=in_connection_type, out_connection_type=out_connection_type,
            in_gender=in_gender, out_gender=out_gender
        )
        self._type = OpticalType.ADAPTER

    @classmethod
    def ZWO_M42_M42_11mm(cls):
        return cls("ZWO M42-M42 11mm Adapter", optical_length=11, in_connection_type=ConnectionType.M42, out_connection_type=ConnectionType.M42)

class Spacer(IntermediateOpticalEquipment):
    def __init__(self, vendor, optical_length=0, mass=0, in_connection_type=None, out_connection_type=None, in_gender=None, out_gender=None):
        super(Spacer, self).__init__(
            vendor, optical_length=optical_length, mass=mass,
            in_connection_type=in_connection_type, out_connection_type=out_connection_type,
            in_gender=in_gender, out_gender=out_gender
        )
        self._type = OpticalType.SPACER

    @classmethod
    def M42_20mm_Spacer(cls):
        return cls("Generic M42 20mm Spacer", optical_length=20, in_connection_type=ConnectionType.M42, out_connection_type=ConnectionType.M42)
