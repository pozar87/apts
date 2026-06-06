from ..base import FilterHolder


class OptolongFilterHolder(FilterHolder):
    _DATABASE = {'Optolong_Filter_Drawer_M48': {'brand': 'Optolong', 'name':
        'Filter Drawer (M48)', 'type': 'type_filter_holder',
        'optical_length': 25, 'mass': 210, 'tside_thread': 'M48',
        'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender':
        'Male', 'reversible': False, 'bf_role': ''},
        'Optolong_Filter_Drawer_M54': {'brand': 'Optolong', 'name':
        'Filter Drawer (M54)', 'type': 'type_filter_holder',
        'optical_length': 25, 'mass': 240, 'tside_thread': 'M54',
        'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender':
        'Male', 'reversible': False, 'bf_role': ''}}

    @classmethod
    def Optolong_Filter_Drawer_M48(cls):
        return cls.from_database(cls._DATABASE['Optolong_Filter_Drawer_M48'])

    @classmethod
    def Optolong_Filter_Drawer_M54(cls):
        return cls.from_database(cls._DATABASE['Optolong_Filter_Drawer_M54'])
