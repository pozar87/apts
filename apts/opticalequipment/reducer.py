from .abstract import IntermediateOpticalEquipment
from ..constants import OpticalType
from ..units import get_unit_registry
from ..utils import Gender, ConnectionType

class Reducer(IntermediateOpticalEquipment):
    def __init__(
        self, vendor, magnification=0.8, optical_length=0, mass=0, required_backfocus=None,
        in_connection_type=None, out_connection_type=None, in_gender=Gender.MALE, out_gender=Gender.FEMALE
    ):
        super(Reducer, self).__init__(
            vendor, optical_length=optical_length, mass=mass,
            in_connection_type=in_connection_type, out_connection_type=out_connection_type,
            in_gender=in_gender, out_gender=out_gender
        )
        self._type = OpticalType.REDUCER
        self.magnification = magnification
        self.required_backfocus = (
            required_backfocus * get_unit_registry().mm
            if required_backfocus is not None
            else None
        )

    @classmethod
    def SharpStar_0_8x(cls):
        return cls("SharpStar 0.8x Reducer/Flattener", magnification=0.8, optical_length=45, mass=300, required_backfocus=55, in_connection_type=ConnectionType.M63, out_connection_type=ConnectionType.M48)

    @classmethod
    def Celestron_0_63x(cls):
        return cls("Celestron 0.63x Reducer/Corrector", magnification=0.63, mass=250, required_backfocus=105, in_connection_type=ConnectionType.SC, out_connection_type=ConnectionType.SC)

class Flattener(IntermediateOpticalEquipment):
    def __init__(
        self, vendor, magnification=1.0, optical_length=0, mass=0, required_backfocus=None,
        in_connection_type=None, out_connection_type=None, in_gender=Gender.MALE, out_gender=Gender.FEMALE
    ):
        super(Flattener, self).__init__(
            vendor, optical_length=optical_length, mass=mass,
            in_connection_type=in_connection_type, out_connection_type=out_connection_type,
            in_gender=in_gender, out_gender=out_gender
        )
        self._type = OpticalType.FLATTENER
        self.magnification = magnification
        self.required_backfocus = (
            required_backfocus * get_unit_registry().mm
            if required_backfocus is not None
            else None
        )

class Corrector(IntermediateOpticalEquipment):
    def __init__(
        self, vendor, magnification=1.0, optical_length=0, mass=0, required_backfocus=None,
        in_connection_type=None, out_connection_type=None, in_gender=Gender.MALE, out_gender=Gender.FEMALE
    ):
        super(Corrector, self).__init__(
            vendor, optical_length=optical_length, mass=mass,
            in_connection_type=in_connection_type, out_connection_type=out_connection_type,
            in_gender=in_gender, out_gender=out_gender
        )
        self._type = OpticalType.CORRECTOR
        self.magnification = magnification
        self.required_backfocus = (
            required_backfocus * get_unit_registry().mm
            if required_backfocus is not None
            else None
        )
