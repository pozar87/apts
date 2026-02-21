from .abstract import IntermediateOpticalEquipment
from ..constants import OpticalType
from ..units import get_unit_registry

class Reducer(IntermediateOpticalEquipment):
    def __init__(
        self, vendor, magnification=0.8, optical_length=0, mass=0, required_backfocus=None,
        in_connection_type=None, out_connection_type=None, in_gender=None, out_gender=None
    ):
        super(Reducer, self).__init__(
            vendor, optical_length=optical_length, mass=mass,
            in_connection_type=in_connection_type, out_connection_type=out_connection_type
        )
        self._type = OpticalType.REDUCER
        self.magnification = magnification
        self.required_backfocus = (
            required_backfocus * get_unit_registry().mm
            if required_backfocus is not None
            else None
        )
        self.in_gender = in_gender
        self.out_gender = out_gender

    def register(self, equipment):
        super(Reducer, self)._register(equipment)
        if self.in_connection_type:
            self._register_input(equipment, self.in_connection_type, self.in_gender)
        if self.out_connection_type:
            self._register_output(equipment, self.out_connection_type, self.out_gender)

class Flattener(IntermediateOpticalEquipment):
    def __init__(
        self, vendor, magnification=1.0, optical_length=0, mass=0, required_backfocus=None,
        in_connection_type=None, out_connection_type=None, in_gender=None, out_gender=None
    ):
        super(Flattener, self).__init__(
            vendor, optical_length=optical_length, mass=mass,
            in_connection_type=in_connection_type, out_connection_type=out_connection_type
        )
        self._type = OpticalType.FLATTENER
        self.magnification = magnification
        self.required_backfocus = (
            required_backfocus * get_unit_registry().mm
            if required_backfocus is not None
            else None
        )
        self.in_gender = in_gender
        self.out_gender = out_gender

    def register(self, equipment):
        super(Flattener, self)._register(equipment)
        if self.in_connection_type:
            self._register_input(equipment, self.in_connection_type, self.in_gender)
        if self.out_connection_type:
            self._register_output(equipment, self.out_connection_type, self.out_gender)

class Corrector(IntermediateOpticalEquipment):
    def __init__(
        self, vendor, magnification=1.0, optical_length=0, mass=0, required_backfocus=None,
        in_connection_type=None, out_connection_type=None, in_gender=None, out_gender=None
    ):
        super(Corrector, self).__init__(
            vendor, optical_length=optical_length, mass=mass,
            in_connection_type=in_connection_type, out_connection_type=out_connection_type
        )
        self._type = OpticalType.CORRECTOR
        self.magnification = magnification
        self.required_backfocus = (
            required_backfocus * get_unit_registry().mm
            if required_backfocus is not None
            else None
        )
        self.in_gender = in_gender
        self.out_gender = out_gender

    def register(self, equipment):
        super(Corrector, self)._register(equipment)
        if self.in_connection_type:
            self._register_input(equipment, self.in_connection_type, self.in_gender)
        if self.out_connection_type:
            self._register_output(equipment, self.out_connection_type, self.out_gender)
