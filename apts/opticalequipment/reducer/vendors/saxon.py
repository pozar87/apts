from ..base import Reducer

class SaxonReducer(Reducer):
    _DATABASE = {'Saxon_0_85x_Reducer_M48': {'brand': 'Saxon', 'name': '0.85x Reducer (M48)', 'type': 'type_reducer', 'optical_length': 0, 'mass': 200, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Female', 'reversible': False, 'bf_role': 'start'}}

    @classmethod
    def Saxon_0_85x_Reducer_M48(cls):
        return cls.from_database(cls._DATABASE['Saxon_0_85x_Reducer_M48'])