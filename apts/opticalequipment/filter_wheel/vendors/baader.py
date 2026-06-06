from ..base import FilterWheel, FilterHolder


class BaaderFilterWheel(FilterWheel):
    _DATABASE = {'Baader_SteelTrack_Filter_Wheel': {'brand': 'Baader',
        'name': 'SteelTrack Filter Wheel', 'type': 'type_filter_wheel',
        'optical_length': 20, 'mass': 450, 'tside_thread': 'M48',
        'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender':
        'Male', 'reversible': False, 'bf_role': ''}}

    @classmethod
    def Baader_SteelTrack_Filter_Wheel(cls):
        return cls.from_database(cls._DATABASE[
            'Baader_SteelTrack_Filter_Wheel'])


class BaaderFilterHolder(FilterHolder):
    _DATABASE = {'Baader_Filter_Slider_M48': {'brand': 'Baader', 'name':
        'Filter Slider (M48)', 'type': 'type_filter_holder',
        'optical_length': 8, 'mass': 150, 'tside_thread': 'M48',
        'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender':
        'Male', 'reversible': False, 'bf_role': ''},
        'Baader_Filter_Slider_M54': {'brand': 'Baader', 'name':
        'Filter Slider (M54)', 'type': 'type_filter_holder',
        'optical_length': 8, 'mass': 170, 'tside_thread': 'M54',
        'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender':
        'Male', 'reversible': False, 'bf_role': ''},
        'Baader_Filter_Slider_M42': {'brand': 'Baader', 'name':
        'Filter Slider (M42)', 'type': 'type_filter_holder',
        'optical_length': 8, 'mass': 130, 'tside_thread': 'M42',
        'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender':
        'Male', 'reversible': False, 'bf_role': ''},
        'Baader_2_Filter_Holder': {'brand': 'Baader', 'name':
        '2" Filter Holder', 'type': 'type_filter_holder', 'optical_length':
        10, 'mass': 100, 'tside_thread': '2"', 'tside_gender': 'Male',
        'cside_thread': '2"', 'cside_gender': 'Female', 'reversible': False,
        'bf_role': ''}}

    @classmethod
    def Baader_Filter_Slider_M48(cls):
        return cls.from_database(cls._DATABASE['Baader_Filter_Slider_M48'])

    @classmethod
    def Baader_Filter_Slider_M54(cls):
        return cls.from_database(cls._DATABASE['Baader_Filter_Slider_M54'])

    @classmethod
    def Baader_Filter_Slider_M42(cls):
        return cls.from_database(cls._DATABASE['Baader_Filter_Slider_M42'])

    @classmethod
    def Baader_2_Filter_Holder(cls):
        return cls.from_database(cls._DATABASE['Baader_2_Filter_Holder'])
