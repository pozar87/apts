from .abstract import IntermediateOpticalEquipment
from ..constants import OpticalType

class FlipMirror(IntermediateOpticalEquipment):
    def __init__(self, vendor, optical_length=0, mass=0, in_connection_type=None, out_connection_type=None, in_gender=None, out_gender=None):
        super(FlipMirror, self).__init__(vendor, optical_length=optical_length, mass=mass, in_connection_type=in_connection_type, out_connection_type=out_connection_type)
        self._type = OpticalType.FLIP_MIRROR
        self.in_gender = in_gender
        self.out_gender = out_gender

    def register(self, equipment):
        super(FlipMirror, self)._register(equipment)
        if self.in_connection_type:
            self._register_input(equipment, self.in_connection_type, self.in_gender)
        if self.out_connection_type:
            self._register_output(equipment, self.out_connection_type, self.out_gender)
