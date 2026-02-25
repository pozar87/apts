from ...abstract import IntermediateOpticalEquipment
from ....constants import OpticalType
from ....units import get_unit_registry
from ....utils import Gender
from ..base import Reducer, Flattener, Corrector

class VixenReducer(Reducer):
    _DATABASE = {'Vixen_SD_Reducer_HD': {'brand': 'Vixen', 'name': 'SD Reducer HD', 'type': 'type_reducer', 'optical_length': 0, 'mass': 250, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Female', 'reversible': False, 'bf_role': 'start'}}

    @classmethod
    def Vixen_SD_Reducer_HD(cls):
        return cls.from_database(cls._DATABASE['Vixen_SD_Reducer_HD'])

class VixenFlattener(Flattener):
    _DATABASE = {'Vixen_SD_Flattener_HD': {'brand': 'Vixen', 'name': 'SD Flattener HD', 'type': 'type_flattener', 'optical_length': 0, 'mass': 230, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Female', 'reversible': False, 'bf_role': 'start'}}

    @classmethod
    def Vixen_SD_Flattener_HD(cls):
        return cls.from_database(cls._DATABASE['Vixen_SD_Flattener_HD'])

class VixenCorrector(Corrector):
    _DATABASE = {'Vixen_Corrector_PH': {'brand': 'Vixen', 'name': 'Corrector PH', 'type': 'type_corrector', 'optical_length': 0, 'mass': 250, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Female', 'reversible': False, 'bf_role': 'start'}}

    @classmethod
    def Vixen_Corrector_PH(cls):
        return cls.from_database(cls._DATABASE['Vixen_Corrector_PH'])