from ..base import Reducer, Flattener

class BorgReducer(Reducer):
    _DATABASE = {'Borg_Reducer_0_72x_M57': {'brand': 'Borg', 'name': 'Reducer 0.72x (M57)', 'type': 'type_reducer', 'optical_length': 0, 'mass': 200, 'tside_thread': 'M56', 'tside_gender': 'Female', 'cside_thread': 'M56', 'cside_gender': 'Female', 'reversible': False, 'bf_role': 'start'}, 'Borg_0_85x_Reducer_M57': {'brand': 'Borg', 'name': '0.85x Reducer (M57)', 'type': 'type_reducer', 'optical_length': 0, 'mass': 200, 'tside_thread': 'M56', 'tside_gender': 'Female', 'cside_thread': 'M56', 'cside_gender': 'Female', 'reversible': False, 'bf_role': 'start'}}

    @classmethod
    def Borg_Reducer_0_72x_M57(cls):
        return cls.from_database(cls._DATABASE['Borg_Reducer_0_72x_M57'])

    @classmethod
    def Borg_0_85x_Reducer_M57(cls):
        return cls.from_database(cls._DATABASE['Borg_0_85x_Reducer_M57'])

class BorgFlattener(Flattener):
    _DATABASE = {'Borg_Flattener_1_08x_M57': {'brand': 'Borg', 'name': 'Flattener 1.08x (M57)', 'type': 'type_flattener', 'optical_length': 0, 'mass': 180, 'tside_thread': 'M56', 'tside_gender': 'Female', 'cside_thread': 'M56', 'cside_gender': 'Female', 'reversible': False, 'bf_role': 'start'}, 'Borg_Multi_Flattener_M57': {'brand': 'Borg', 'name': 'Multi Flattener (M57)', 'type': 'type_flattener', 'optical_length': 0, 'mass': 250, 'tside_thread': 'M56', 'tside_gender': 'Female', 'cside_thread': 'M56', 'cside_gender': 'Female', 'reversible': False, 'bf_role': 'start'}, 'Borg_1_08x_Flattener_89ED': {'brand': 'Borg', 'name': '1.08x Flattener (89ED)', 'type': 'type_flattener', 'optical_length': 0, 'mass': 200, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Female', 'reversible': False, 'bf_role': 'start'}}

    @classmethod
    def Borg_Flattener_1_08x_M57(cls):
        return cls.from_database(cls._DATABASE['Borg_Flattener_1_08x_M57'])

    @classmethod
    def Borg_Multi_Flattener_M57(cls):
        return cls.from_database(cls._DATABASE['Borg_Multi_Flattener_M57'])

    @classmethod
    def Borg_1_08x_Flattener_89ED(cls):
        return cls.from_database(cls._DATABASE['Borg_1_08x_Flattener_89ED'])