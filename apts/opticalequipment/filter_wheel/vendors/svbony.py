from ..base import FilterWheel, FilterHolder


class SvbonyFilterWheel(FilterWheel):
    _DATABASE = {'SVBony_SV305_FW_1_25': {'brand': 'SVBony', 'name':
        'SV305 FW 1.25"', 'type': 'type_filter_wheel', 'optical_length': 18,
        'mass': 200, 'tside_thread': 'M42', 'tside_gender': 'Female',
        'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': False,
        'bf_role': ''}, 'SVBony_SV222_FW_5x1_25_M42': {'brand': 'SVBony',
        'name': 'SV222 FW 5x1.25" (M42)', 'type': 'type_filter_wheel',
        'optical_length': 18, 'mass': 220, 'tside_thread': 'M42',
        'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender':
        'Male', 'reversible': False, 'bf_role': ''},
        'SVBony_SV222_FW_7x_M48': {'brand': 'SVBony', 'name':
        'SV222 FW 7x (M48)', 'type': 'type_filter_wheel', 'optical_length':
        20, 'mass': 380, 'tside_thread': 'M48', 'tside_gender': 'Female',
        'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': False,
        'bf_role': ''}}

    @classmethod
    def SVBony_SV305_FW_1_25(cls):
        return cls.from_database(cls._DATABASE['SVBony_SV305_FW_1_25'])

    @classmethod
    def SVBony_SV222_FW_5x1_25_M42(cls):
        return cls.from_database(cls._DATABASE['SVBony_SV222_FW_5x1_25_M42'])

    @classmethod
    def SVBony_SV222_FW_7x_M48(cls):
        return cls.from_database(cls._DATABASE['SVBony_SV222_FW_7x_M48'])


class SvbonyFilterHolder(FilterHolder):
    _DATABASE = {'SVBony_Filter_Drawer_M42': {'brand': 'SVBony', 'name':
        'Filter Drawer (M42)', 'type': 'type_filter_holder',
        'optical_length': 20, 'mass': 150, 'tside_thread': 'M42',
        'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender':
        'Male', 'reversible': False, 'bf_role': ''}}

    @classmethod
    def SVBony_Filter_Drawer_M42(cls):
        return cls.from_database(cls._DATABASE['SVBony_Filter_Drawer_M42'])
