from ..base import FilterWheel, FilterHolder


class LacertaFilterWheel(FilterWheel):
    _DATABASE = {'Lacerta_Filter_Wheel_M42': {'brand': 'Lacerta', 'name':
        'Filter Wheel (M42)', 'type': 'type_filter_wheel', 'optical_length':
        20, 'mass': 350, 'tside_thread': 'M42', 'tside_gender': 'Female',
        'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': False,
        'bf_role': ''}, 'Lacerta_Filter_Wheel_M54': {'brand': 'Lacerta',
        'name': 'Filter Wheel (M54)', 'type': 'type_filter_wheel',
        'optical_length': 20, 'mass': 550, 'tside_thread': 'M54',
        'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender':
        'Male', 'reversible': False, 'bf_role': ''},
        'Lacerta_Filter_Wheel_5x_M42': {'brand': 'Lacerta', 'name':
        'Filter Wheel 5x (M42)', 'type': 'type_filter_wheel',
        'optical_length': 18, 'mass': 280, 'tside_thread': 'M42',
        'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender':
        'Male', 'reversible': False, 'bf_role': ''},
        'Lacerta_Filter_Wheel_7x_M48': {'brand': 'Lacerta', 'name':
        'Filter Wheel 7x (M48)', 'type': 'type_filter_wheel',
        'optical_length': 20, 'mass': 440, 'tside_thread': 'M48',
        'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender':
        'Male', 'reversible': False, 'bf_role': ''},
        'Lacerta_Filter_Wheel_7x_M54': {'brand': 'Lacerta', 'name':
        'Filter Wheel 7x (M54)', 'type': 'type_filter_wheel',
        'optical_length': 20, 'mass': 550, 'tside_thread': 'M54',
        'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender':
        'Male', 'reversible': False, 'bf_role': ''}}

    @classmethod
    def Lacerta_Filter_Wheel_M42(cls):
        return cls.from_database(cls._DATABASE['Lacerta_Filter_Wheel_M42'])

    @classmethod
    def Lacerta_Filter_Wheel_M54(cls):
        return cls.from_database(cls._DATABASE['Lacerta_Filter_Wheel_M54'])

    @classmethod
    def Lacerta_Filter_Wheel_5x_M42(cls):
        return cls.from_database(cls._DATABASE['Lacerta_Filter_Wheel_5x_M42'])

    @classmethod
    def Lacerta_Filter_Wheel_7x_M48(cls):
        return cls.from_database(cls._DATABASE['Lacerta_Filter_Wheel_7x_M48'])

    @classmethod
    def Lacerta_Filter_Wheel_7x_M54(cls):
        return cls.from_database(cls._DATABASE['Lacerta_Filter_Wheel_7x_M54'])


class LacertaFilterHolder(FilterHolder):
    _DATABASE = {'Lacerta_Filter_Drawer_M48': {'brand': 'Lacerta', 'name':
        'Filter Drawer (M48)', 'type': 'type_filter_holder',
        'optical_length': 25, 'mass': 200, 'tside_thread': 'M48',
        'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender':
        'Male', 'reversible': False, 'bf_role': ''},
        'Lacerta_Filter_Drawer_M54': {'brand': 'Lacerta', 'name':
        'Filter Drawer (M54)', 'type': 'type_filter_holder',
        'optical_length': 25, 'mass': 230, 'tside_thread': 'M54',
        'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender':
        'Male', 'reversible': False, 'bf_role': ''}}

    @classmethod
    def Lacerta_Filter_Drawer_M48(cls):
        return cls.from_database(cls._DATABASE['Lacerta_Filter_Drawer_M48'])

    @classmethod
    def Lacerta_Filter_Drawer_M54(cls):
        return cls.from_database(cls._DATABASE['Lacerta_Filter_Drawer_M54'])
