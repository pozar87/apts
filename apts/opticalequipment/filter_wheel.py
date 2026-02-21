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


class FilterHolder(IntermediateOpticalEquipment):
    def __init__(self, vendor, optical_length=0, mass=0, in_connection_type=None, out_connection_type=None, in_gender=None, out_gender=None):
        super(FilterHolder, self).__init__(
            vendor, optical_length=optical_length, mass=mass,
            in_connection_type=in_connection_type, out_connection_type=out_connection_type,
            in_gender=in_gender, out_gender=out_gender
        )
        self._type = OpticalType.FILTER_HOLDER
