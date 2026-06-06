from ..base import FilterHolder


class IdasFilterHolder(FilterHolder):
    _DATABASE = {'IDAS_Filter_Holder_M48': {'brand': 'IDAS', 'name':
        'Filter Holder (M48)', 'type': 'type_filter_holder',
        'optical_length': 8, 'mass': 120, 'tside_thread': 'M48',
        'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender':
        'Male', 'reversible': False, 'bf_role': ''}}

    @classmethod
    def IDAS_Filter_Holder_M48(cls):
        return cls.from_database(cls._DATABASE['IDAS_Filter_Holder_M48'])
