from ..base import Reducer, Flattener

class RiccardiReducer(Reducer):
    _DATABASE = {'Riccardi_APO_Reducer_0_75x_M72': {'brand': 'Riccardi', 'name': 'APO Reducer 0.75x (M72)', 'type': 'type_reducer', 'optical_length': 19.8, 'mass': 500, 'tside_thread': 'M72', 'tside_gender': 'Female', 'cside_thread': 'M68', 'cside_gender': 'Female', 'reversible': False, 'bf_role': 'start'}, 'Riccardi_Reducer_0_72x_M82': {'brand': 'Riccardi', 'name': 'Reducer 0.72x (M82)', 'type': 'type_reducer', 'optical_length': 0, 'mass': 550, 'tside_thread': 'M82', 'tside_gender': 'Female', 'cside_thread': 'M68', 'cside_gender': 'Female', 'reversible': False, 'bf_role': 'start'}, 'Riccardi_Reducer_0_75x_M68': {'brand': 'Riccardi', 'name': 'Reducer 0.75x (M68)', 'type': 'type_reducer', 'optical_length': 0, 'mass': 480, 'tside_thread': 'M68', 'tside_gender': 'Female', 'cside_thread': 'M68', 'cside_gender': 'Female', 'reversible': False, 'bf_role': 'start'}}

    @classmethod
    def Riccardi_APO_Reducer_0_75x_M72(cls):
        return cls.from_database(cls._DATABASE['Riccardi_APO_Reducer_0_75x_M72'])

    @classmethod
    def Riccardi_Reducer_0_72x_M82(cls):
        return cls.from_database(cls._DATABASE['Riccardi_Reducer_0_72x_M82'])

    @classmethod
    def Riccardi_Reducer_0_75x_M68(cls):
        return cls.from_database(cls._DATABASE['Riccardi_Reducer_0_75x_M68'])

class RiccardiFlattener(Flattener):
    _DATABASE = {'Riccardi_Flattener_M54': {'brand': 'Riccardi', 'name': 'Flattener (M54)', 'type': 'type_flattener', 'optical_length': 0, 'mass': 300, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Female', 'reversible': False, 'bf_role': 'start'}}

    @classmethod
    def Riccardi_Flattener_M54(cls):
        return cls.from_database(cls._DATABASE['Riccardi_Flattener_M54'])