from ..base import FilterWheel


class OmegonFilterWheel(FilterWheel):
    _DATABASE = {'Omegon_Filter_Wheel_5x1_25_M42': {'brand': 'Omegon',
        'name': 'Filter Wheel 5x1.25" (M42)', 'type': 'type_filter_wheel',
        'optical_length': 18, 'mass': 300, 'tside_thread': 'M42',
        'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender':
        'Male', 'reversible': False, 'bf_role': ''},
        'Omegon_Filter_Wheel_7x2_M54': {'brand': 'Omegon', 'name':
        'Filter Wheel 7x2" (M54)', 'type': 'type_filter_wheel',
        'optical_length': 20, 'mass': 550, 'tside_thread': 'M54',
        'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender':
        'Male', 'reversible': False, 'bf_role': ''},
        'Omegon_Filter_Wheel_5x_M42': {'brand': 'Omegon', 'name':
        'Filter Wheel 5x (M42)', 'type': 'type_filter_wheel',
        'optical_length': 18, 'mass': 280, 'tside_thread': 'M42',
        'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender':
        'Male', 'reversible': False, 'bf_role': ''},
        'Omegon_Filter_Wheel_7x_M48': {'brand': 'Omegon', 'name':
        'Filter Wheel 7x (M48)', 'type': 'type_filter_wheel',
        'optical_length': 20, 'mass': 430, 'tside_thread': 'M48',
        'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender':
        'Male', 'reversible': False, 'bf_role': ''}}

    @classmethod
    def Omegon_Filter_Wheel_5x1_25_M42(cls):
        return cls.from_database(cls._DATABASE[
            'Omegon_Filter_Wheel_5x1_25_M42'])

    @classmethod
    def Omegon_Filter_Wheel_7x2_M54(cls):
        return cls.from_database(cls._DATABASE['Omegon_Filter_Wheel_7x2_M54'])

    @classmethod
    def Omegon_Filter_Wheel_5x_M42(cls):
        return cls.from_database(cls._DATABASE['Omegon_Filter_Wheel_5x_M42'])

    @classmethod
    def Omegon_Filter_Wheel_7x_M48(cls):
        return cls.from_database(cls._DATABASE['Omegon_Filter_Wheel_7x_M48'])
