from ..base import OAG


class OgmaOAG(OAG):
    _DATABASE = {'OGMA_OAG_M42': {'brand': 'OGMA', 'name': 'OAG (M42)',
        'type': 'type_oag', 'optical_length': 16, 'mass': 165,
        'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread':
        'M42', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}}

    @classmethod
    def OGMA_OAG_M42(cls):
        return cls.from_database(cls._DATABASE['OGMA_OAG_M42'])
