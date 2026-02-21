from .abstract import IntermediateOpticalEquipment
from ..constants import OpticalType
from ..utils import ConnectionType

class FilterWheel(IntermediateOpticalEquipment):
    def __init__(self, vendor, optical_length=0, mass=0, in_connection_type=None, out_connection_type=None, in_gender=None, out_gender=None):
        super(FilterWheel, self).__init__(
            vendor, optical_length=optical_length, mass=mass,
            in_connection_type=in_connection_type, out_connection_type=out_connection_type,
            in_gender=in_gender, out_gender=out_gender
        )
        self._type = OpticalType.FILTER_WHEEL

    @classmethod
    def ZWO_EFW_8x31(cls):
        return cls("ZWO EFW 8x31mm", optical_length=20, mass=400, in_connection_type=ConnectionType.M42, out_connection_type=ConnectionType.M42)

    @classmethod
    def QHY_CFW3_M(cls):
        return cls("QHY CFW3-M", optical_length=17, mass=500, in_connection_type=ConnectionType.M42, out_connection_type=ConnectionType.M42)

class FilterHolder(IntermediateOpticalEquipment):
    def __init__(self, vendor, optical_length=0, mass=0, in_connection_type=None, out_connection_type=None, in_gender=None, out_gender=None):
        super(FilterHolder, self).__init__(
            vendor, optical_length=optical_length, mass=mass,
            in_connection_type=in_connection_type, out_connection_type=out_connection_type,
            in_gender=in_gender, out_gender=out_gender
        )
        self._type = OpticalType.FILTER_HOLDER
