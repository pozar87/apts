from ..base import OAG


class ZwoOAG(OAG):
    _DATABASE = {'ZWO_OAG_M48_M42': {'brand': 'ZWO', 'name':
        'OAG (M48→M42)', 'type': 'type_oag', 'optical_length': 16.5, 'mass':
        195, 'tside_thread': 'M48', 'tside_gender': 'Female',
        'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': False,
        'bf_role': ''}, 'ZWO_OAG_M54_M54': {'brand': 'ZWO', 'name':
        'OAG (M54→M54)', 'type': 'type_oag', 'optical_length': 19.5, 'mass':
        300, 'tside_thread': 'M54', 'tside_gender': 'Female',
        'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': False,
        'bf_role': ''}, 'ZWO_OAG_L_M68_M54': {'brand': 'ZWO', 'name':
        'OAG-L (M68→M54)', 'type': 'type_oag', 'optical_length': 22.5,
        'mass': 380, 'tside_thread': 'M68', 'tside_gender': 'Female',
        'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': False,
        'bf_role': ''}}

    @classmethod
    def ZWO_OAG_M48_M42(cls):
        return cls.from_database(cls._DATABASE['ZWO_OAG_M48_M42'])

    @classmethod
    def ZWO_OAG_M54_M54(cls):
        return cls.from_database(cls._DATABASE['ZWO_OAG_M54_M54'])

    @classmethod
    def ZWO_OAG_L_M68_M54(cls):
        return cls.from_database(cls._DATABASE['ZWO_OAG_L_M68_M54'])
