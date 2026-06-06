from ..base import FilterWheel


class MeadeFilterWheel(FilterWheel):
    _DATABASE = {'Meade_Series_6000_FW_M42': {'brand': 'Meade', 'name':
        'Series 6000 FW (M42)', 'type': 'type_filter_wheel',
        'optical_length': 19, 'mass': 320, 'tside_thread': 'M42',
        'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender':
        'Male', 'reversible': False, 'bf_role': ''}}

    @classmethod
    def Meade_Series_6000_FW_M42(cls):
        return cls.from_database(cls._DATABASE['Meade_Series_6000_FW_M42'])
