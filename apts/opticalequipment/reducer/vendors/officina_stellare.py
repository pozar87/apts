from ...abstract import IntermediateOpticalEquipment
from ....constants import OpticalType
from ....units import get_unit_registry
from ....utils import Gender
from ..base import Reducer, Flattener, Corrector

class Officina_stellareReducer(Reducer):
    _DATABASE = {'Officina_Stellare_RC_Corrector_0_75x_M68': {'brand': 'Officina Stellare', 'name': 'RC Corrector 0.75x (M68)', 'type': 'type_reducer', 'optical_length': 0, 'mass': 500, 'tside_thread': 'M68', 'tside_gender': 'Female', 'cside_thread': 'M68', 'cside_gender': 'Female', 'reversible': False, 'bf_role': 'start'}}

    @classmethod
    def Officina_Stellare_RC_Corrector_0_75x_M68(cls):
        return cls.from_database(cls._DATABASE['Officina_Stellare_RC_Corrector_0_75x_M68'])

class Officina_stellareCorrector(Corrector):
    _DATABASE = {'Officina_Stellare_RC_Corrector_1x_M84': {'brand': 'Officina Stellare', 'name': 'RC Corrector 1x (M84)', 'type': 'type_corrector', 'optical_length': 0, 'mass': 600, 'tside_thread': 'M84', 'tside_gender': 'Female', 'cside_thread': 'M84', 'cside_gender': 'Female', 'reversible': False, 'bf_role': 'start'}, 'Officina_Stellare_Wynne_Corrector_M68': {'brand': 'Officina Stellare', 'name': 'Wynne Corrector (M68)', 'type': 'type_corrector', 'optical_length': 0, 'mass': 450, 'tside_thread': 'M68', 'tside_gender': 'Female', 'cside_thread': 'M68', 'cside_gender': 'Female', 'reversible': False, 'bf_role': 'start'}}

    @classmethod
    def Officina_Stellare_RC_Corrector_1x_M84(cls):
        return cls.from_database(cls._DATABASE['Officina_Stellare_RC_Corrector_1x_M84'])

    @classmethod
    def Officina_Stellare_Wynne_Corrector_M68(cls):
        return cls.from_database(cls._DATABASE['Officina_Stellare_Wynne_Corrector_M68'])