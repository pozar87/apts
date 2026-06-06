from ..base import FilterWheel


class BresserFilterWheel(FilterWheel):
    _DATABASE = {'Bresser_Filter_Wheel_5x_M42': {'brand': 'Bresser', 'name':
        'Filter Wheel 5x (M42)', 'type': 'type_filter_wheel',
        'optical_length': 18, 'mass': 260, 'tside_thread': 'M42',
        'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender':
        'Male', 'reversible': False, 'bf_role': ''},
        'Bresser_Filter_Wheel_7x_M48': {'brand': 'Bresser', 'name':
        'Filter Wheel 7x (M48)', 'type': 'type_filter_wheel',
        'optical_length': 19, 'mass': 410, 'tside_thread': 'M48',
        'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender':
        'Male', 'reversible': False, 'bf_role': ''}}

    @classmethod
    def Bresser_Filter_Wheel_5x_M42(cls):
        return cls.from_database(cls._DATABASE['Bresser_Filter_Wheel_5x_M42'])

    @classmethod
    def Bresser_Filter_Wheel_7x_M48(cls):
        return cls.from_database(cls._DATABASE['Bresser_Filter_Wheel_7x_M48'])
