from ..base import Rotator


class TakahashiRotator(Rotator):
    _DATABASE = {'Takahashi_Camera_Rotator_S_M54': {'brand': 'Takahashi',
        'name': 'Camera Rotator S (M54)', 'type': 'type_rotator',
        'optical_length': 10, 'mass': 120, 'tside_thread': 'M54',
        'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender':
        'Male', 'reversible': False, 'bf_role': ''},
        'Takahashi_Camera_Rotator_M_M72': {'brand': 'Takahashi', 'name':
        'Camera Rotator M (M72)', 'type': 'type_rotator', 'optical_length':
        12, 'mass': 200, 'tside_thread': 'M72', 'tside_gender': 'Female',
        'cside_thread': 'M72', 'cside_gender': 'Male', 'reversible': False,
        'bf_role': ''}, 'Takahashi_Camera_Rotator_M82': {'brand':
        'Takahashi', 'name': 'Camera Rotator (M82)', 'type': 'type_rotator',
        'optical_length': 12, 'mass': 300, 'tside_thread': 'M82',
        'tside_gender': 'Female', 'cside_thread': 'M82', 'cside_gender':
        'Male', 'reversible': False, 'bf_role': ''},
        'Takahashi_Camera_Rotator_M92': {'brand': 'Takahashi', 'name':
        'Camera Rotator (M92)', 'type': 'type_rotator', 'optical_length': 
        14, 'mass': 350, 'tside_thread': 'M92', 'tside_gender': 'Female',
        'cside_thread': 'M92', 'cside_gender': 'Male', 'reversible': False,
        'bf_role': ''}}

    @classmethod
    def Takahashi_Camera_Rotator_S_M54(cls):
        return cls.from_database(cls._DATABASE[
            'Takahashi_Camera_Rotator_S_M54'])

    @classmethod
    def Takahashi_Camera_Rotator_M_M72(cls):
        return cls.from_database(cls._DATABASE[
            'Takahashi_Camera_Rotator_M_M72'])

    @classmethod
    def Takahashi_Camera_Rotator_M82(cls):
        return cls.from_database(cls._DATABASE['Takahashi_Camera_Rotator_M82'])

    @classmethod
    def Takahashi_Camera_Rotator_M92(cls):
        return cls.from_database(cls._DATABASE['Takahashi_Camera_Rotator_M92'])
