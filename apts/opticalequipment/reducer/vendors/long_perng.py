from ..base import Reducer, Flattener

class Long_perngReducer(Reducer):
    _DATABASE = {'Long_Perng_0_79x_Reducer_M48': {'brand': 'Long Perng', 'name': '0.79x Reducer (M48)', 'type': 'type_reducer', 'optical_length': 0, 'mass': 200, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Female', 'reversible': False, 'bf_role': 'start'}}

    @classmethod
    def Long_Perng_0_79x_Reducer_M48(cls):
        return cls.from_database(cls._DATABASE['Long_Perng_0_79x_Reducer_M48'])

class Long_perngFlattener(Flattener):
    _DATABASE = {'Long_Perng_Field_Flattener_M48': {'brand': 'Long Perng', 'name': 'Field Flattener (M48)', 'type': 'type_flattener', 'optical_length': 0, 'mass': 180, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Female', 'reversible': False, 'bf_role': 'start'}}

    @classmethod
    def Long_Perng_Field_Flattener_M48(cls):
        return cls.from_database(cls._DATABASE['Long_Perng_Field_Flattener_M48'])