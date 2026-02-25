from ..base import Flattener, Corrector

class GsoFlattener(Flattener):
    _DATABASE = {'GSO_2_Field_Flattener': {'brand': 'GSO', 'name': '2" Field Flattener', 'type': 'type_flattener', 'optical_length': 0, 'mass': 250, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Female', 'reversible': False, 'bf_role': 'start'}}

    @classmethod
    def GSO_2_Field_Flattener(cls):
        return cls.from_database(cls._DATABASE['GSO_2_Field_Flattener'])

class GsoCorrector(Corrector):
    _DATABASE = {'GSO_Coma_Corrector_M48': {'brand': 'GSO', 'name': 'Coma Corrector (M48)', 'type': 'type_corrector', 'optical_length': 0, 'mass': 230, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Female', 'reversible': False, 'bf_role': 'start'}}

    @classmethod
    def GSO_Coma_Corrector_M48(cls):
        return cls.from_database(cls._DATABASE['GSO_Coma_Corrector_M48'])