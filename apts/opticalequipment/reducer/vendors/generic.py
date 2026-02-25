from ..base import Reducer, Flattener

class GenericReducer(Reducer):
    _DATABASE = {'Generic_0_63x_M42': {'brand': 'Generic', 'name': '0.63x (M42)', 'type': 'type_reducer', 'optical_length': 0, 'mass': 200, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Female', 'reversible': False, 'bf_role': 'start'}, 'Generic_0_63x_M48': {'brand': 'Generic', 'name': '0.63x (M48)', 'type': 'type_reducer', 'optical_length': 0, 'mass': 200, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Female', 'reversible': False, 'bf_role': 'start'}, 'Generic_0_63x_M54': {'brand': 'Generic', 'name': '0.63x (M54)', 'type': 'type_reducer', 'optical_length': 0, 'mass': 200, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Female', 'reversible': False, 'bf_role': 'start'}, 'Generic_0_63x_M68': {'brand': 'Generic', 'name': '0.63x (M68)', 'type': 'type_reducer', 'optical_length': 0, 'mass': 200, 'tside_thread': 'M68', 'tside_gender': 'Female', 'cside_thread': 'M68', 'cside_gender': 'Female', 'reversible': False, 'bf_role': 'start'}, 'Generic_0_72x_M42': {'brand': 'Generic', 'name': '0.72x (M42)', 'type': 'type_reducer', 'optical_length': 0, 'mass': 250, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Female', 'reversible': False, 'bf_role': 'start'}, 'Generic_0_72x_M48': {'brand': 'Generic', 'name': '0.72x (M48)', 'type': 'type_reducer', 'optical_length': 0, 'mass': 250, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Female', 'reversible': False, 'bf_role': 'start'}, 'Generic_0_72x_M54': {'brand': 'Generic', 'name': '0.72x (M54)', 'type': 'type_reducer', 'optical_length': 0, 'mass': 250, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Female', 'reversible': False, 'bf_role': 'start'}, 'Generic_0_72x_M68': {'brand': 'Generic', 'name': '0.72x (M68)', 'type': 'type_reducer', 'optical_length': 0, 'mass': 250, 'tside_thread': 'M68', 'tside_gender': 'Female', 'cside_thread': 'M68', 'cside_gender': 'Female', 'reversible': False, 'bf_role': 'start'}, 'Generic_0_79x_M42': {'brand': 'Generic', 'name': '0.79x (M42)', 'type': 'type_reducer', 'optical_length': 0, 'mass': 230, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Female', 'reversible': False, 'bf_role': 'start'}, 'Generic_0_79x_M48': {'brand': 'Generic', 'name': '0.79x (M48)', 'type': 'type_reducer', 'optical_length': 0, 'mass': 230, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Female', 'reversible': False, 'bf_role': 'start'}, 'Generic_0_79x_M54': {'brand': 'Generic', 'name': '0.79x (M54)', 'type': 'type_reducer', 'optical_length': 0, 'mass': 230, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Female', 'reversible': False, 'bf_role': 'start'}, 'Generic_0_79x_M68': {'brand': 'Generic', 'name': '0.79x (M68)', 'type': 'type_reducer', 'optical_length': 0, 'mass': 230, 'tside_thread': 'M68', 'tside_gender': 'Female', 'cside_thread': 'M68', 'cside_gender': 'Female', 'reversible': False, 'bf_role': 'start'}, 'Generic_0_85x_M42': {'brand': 'Generic', 'name': '0.85x (M42)', 'type': 'type_reducer', 'optical_length': 0, 'mass': 210, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Female', 'reversible': False, 'bf_role': 'start'}, 'Generic_0_85x_M48': {'brand': 'Generic', 'name': '0.85x (M48)', 'type': 'type_reducer', 'optical_length': 0, 'mass': 210, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Female', 'reversible': False, 'bf_role': 'start'}, 'Generic_0_85x_M54': {'brand': 'Generic', 'name': '0.85x (M54)', 'type': 'type_reducer', 'optical_length': 0, 'mass': 210, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Female', 'reversible': False, 'bf_role': 'start'}, 'Generic_0_85x_M68': {'brand': 'Generic', 'name': '0.85x (M68)', 'type': 'type_reducer', 'optical_length': 0, 'mass': 210, 'tside_thread': 'M68', 'tside_gender': 'Female', 'cside_thread': 'M68', 'cside_gender': 'Female', 'reversible': False, 'bf_role': 'start'}}

    @classmethod
    def Generic_0_63x_M42(cls):
        return cls.from_database(cls._DATABASE['Generic_0_63x_M42'])

    @classmethod
    def Generic_0_63x_M48(cls):
        return cls.from_database(cls._DATABASE['Generic_0_63x_M48'])

    @classmethod
    def Generic_0_63x_M54(cls):
        return cls.from_database(cls._DATABASE['Generic_0_63x_M54'])

    @classmethod
    def Generic_0_63x_M68(cls):
        return cls.from_database(cls._DATABASE['Generic_0_63x_M68'])

    @classmethod
    def Generic_0_72x_M42(cls):
        return cls.from_database(cls._DATABASE['Generic_0_72x_M42'])

    @classmethod
    def Generic_0_72x_M48(cls):
        return cls.from_database(cls._DATABASE['Generic_0_72x_M48'])

    @classmethod
    def Generic_0_72x_M54(cls):
        return cls.from_database(cls._DATABASE['Generic_0_72x_M54'])

    @classmethod
    def Generic_0_72x_M68(cls):
        return cls.from_database(cls._DATABASE['Generic_0_72x_M68'])

    @classmethod
    def Generic_0_79x_M42(cls):
        return cls.from_database(cls._DATABASE['Generic_0_79x_M42'])

    @classmethod
    def Generic_0_79x_M48(cls):
        return cls.from_database(cls._DATABASE['Generic_0_79x_M48'])

    @classmethod
    def Generic_0_79x_M54(cls):
        return cls.from_database(cls._DATABASE['Generic_0_79x_M54'])

    @classmethod
    def Generic_0_79x_M68(cls):
        return cls.from_database(cls._DATABASE['Generic_0_79x_M68'])

    @classmethod
    def Generic_0_85x_M42(cls):
        return cls.from_database(cls._DATABASE['Generic_0_85x_M42'])

    @classmethod
    def Generic_0_85x_M48(cls):
        return cls.from_database(cls._DATABASE['Generic_0_85x_M48'])

    @classmethod
    def Generic_0_85x_M54(cls):
        return cls.from_database(cls._DATABASE['Generic_0_85x_M54'])

    @classmethod
    def Generic_0_85x_M68(cls):
        return cls.from_database(cls._DATABASE['Generic_0_85x_M68'])

class GenericFlattener(Flattener):
    _DATABASE = {'Generic_1_0x_Flattener_M42': {'brand': 'Generic', 'name': '1.0x Flattener (M42)', 'type': 'type_flattener', 'optical_length': 0, 'mass': 180, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Female', 'reversible': False, 'bf_role': 'start'}, 'Generic_1_0x_Flattener_M48': {'brand': 'Generic', 'name': '1.0x Flattener (M48)', 'type': 'type_flattener', 'optical_length': 0, 'mass': 180, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Female', 'reversible': False, 'bf_role': 'start'}, 'Generic_1_0x_Flattener_M54': {'brand': 'Generic', 'name': '1.0x Flattener (M54)', 'type': 'type_flattener', 'optical_length': 0, 'mass': 180, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Female', 'reversible': False, 'bf_role': 'start'}, 'Generic_1_0x_Flattener_M68': {'brand': 'Generic', 'name': '1.0x Flattener (M68)', 'type': 'type_flattener', 'optical_length': 0, 'mass': 180, 'tside_thread': 'M68', 'tside_gender': 'Female', 'cside_thread': 'M68', 'cside_gender': 'Female', 'reversible': False, 'bf_role': 'start'}}

    @classmethod
    def Generic_1_0x_Flattener_M42(cls):
        return cls.from_database(cls._DATABASE['Generic_1_0x_Flattener_M42'])

    @classmethod
    def Generic_1_0x_Flattener_M48(cls):
        return cls.from_database(cls._DATABASE['Generic_1_0x_Flattener_M48'])

    @classmethod
    def Generic_1_0x_Flattener_M54(cls):
        return cls.from_database(cls._DATABASE['Generic_1_0x_Flattener_M54'])

    @classmethod
    def Generic_1_0x_Flattener_M68(cls):
        return cls.from_database(cls._DATABASE['Generic_1_0x_Flattener_M68'])