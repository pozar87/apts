from ..base import OAG


class LacertaOAG(OAG):
    _DATABASE = {'Lacerta_OAG_M48': {'brand': 'Lacerta', 'name':
        'OAG (M48)', 'type': 'type_oag', 'optical_length': 17, 'mass': 200,
        'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread':
        'M42', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}}

    @classmethod
    def Lacerta_OAG_M48(cls):
        return cls.from_database(cls._DATABASE['Lacerta_OAG_M48'])
