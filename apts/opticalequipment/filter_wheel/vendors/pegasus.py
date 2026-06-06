from ..base import FilterWheel, FilterHolder


class PegasusFilterWheel(FilterWheel):
    _DATABASE = {'Pegasus_Indigo_Filter_Wheel_M42': {'brand': 'Pegasus',
        'name': 'Indigo Filter Wheel (M42)', 'type': 'type_filter_wheel',
        'optical_length': 19.6, 'mass': 400, 'tside_thread': 'M42',
        'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender':
        'Male', 'reversible': False, 'bf_role': ''},
        'Pegasus_Indigo_Filter_Wheel_M54': {'brand': 'Pegasus', 'name':
        'Indigo Filter Wheel (M54)', 'type': 'type_filter_wheel',
        'optical_length': 19.6, 'mass': 500, 'tside_thread': 'M54',
        'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender':
        'Male', 'reversible': False, 'bf_role': ''}}

    @classmethod
    def Pegasus_Indigo_Filter_Wheel_M42(cls):
        return cls.from_database(cls._DATABASE[
            'Pegasus_Indigo_Filter_Wheel_M42'])

    @classmethod
    def Pegasus_Indigo_Filter_Wheel_M54(cls):
        return cls.from_database(cls._DATABASE[
            'Pegasus_Indigo_Filter_Wheel_M54'])


class PegasusFilterHolder(FilterHolder):
    _DATABASE = {'Pegasus_Filter_Drawer_M48': {'brand': 'Pegasus', 'name':
        'Filter Drawer (M48)', 'type': 'type_filter_holder',
        'optical_length': 25, 'mass': 200, 'tside_thread': 'M48',
        'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender':
        'Male', 'reversible': False, 'bf_role': ''},
        'Pegasus_Filter_Drawer_M54': {'brand': 'Pegasus', 'name':
        'Filter Drawer (M54)', 'type': 'type_filter_holder',
        'optical_length': 25, 'mass': 230, 'tside_thread': 'M54',
        'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender':
        'Male', 'reversible': False, 'bf_role': ''}}

    @classmethod
    def Pegasus_Filter_Drawer_M48(cls):
        return cls.from_database(cls._DATABASE['Pegasus_Filter_Drawer_M48'])

    @classmethod
    def Pegasus_Filter_Drawer_M54(cls):
        return cls.from_database(cls._DATABASE['Pegasus_Filter_Drawer_M54'])
