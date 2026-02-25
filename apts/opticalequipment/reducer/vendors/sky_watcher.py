from ...abstract import IntermediateOpticalEquipment
from ....constants import OpticalType
from ....units import get_unit_registry
from ....utils import Gender
from ..base import Reducer, Flattener, Corrector

class Sky_watcherReducer(Reducer):
    _DATABASE = {'Sky_Watcher_0_85x_Reducer_Esprit': {'brand': 'Sky-Watcher', 'name': '0.85x Reducer (Esprit)', 'type': 'type_reducer', 'optical_length': 0, 'mass': 250, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Female', 'reversible': False, 'bf_role': 'start'}, 'Sky_Watcher_0_77x_Reducer_Evostar': {'brand': 'Sky-Watcher', 'name': '0.77x Reducer (Evostar)', 'type': 'type_reducer', 'optical_length': 0, 'mass': 200, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Female', 'reversible': False, 'bf_role': 'start'}, 'Sky_Watcher_0_85x_Reducer_Flattener_ED': {'brand': 'Sky-Watcher', 'name': '0.85x Reducer/Flattener (ED)', 'type': 'type_reducer', 'optical_length': 0, 'mass': 220, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Female', 'reversible': False, 'bf_role': 'start'}, 'Sky_Watcher_0_9x_Reducer_Esprit_150': {'brand': 'Sky-Watcher', 'name': '0.9x Reducer (Esprit 150)', 'type': 'type_reducer', 'optical_length': 0, 'mass': 300, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Female', 'reversible': False, 'bf_role': 'start'}}

    @classmethod
    def Sky_Watcher_0_85x_Reducer_Esprit(cls):
        return cls.from_database(cls._DATABASE['Sky_Watcher_0_85x_Reducer_Esprit'])

    @classmethod
    def Sky_Watcher_0_77x_Reducer_Evostar(cls):
        return cls.from_database(cls._DATABASE['Sky_Watcher_0_77x_Reducer_Evostar'])

    @classmethod
    def Sky_Watcher_0_85x_Reducer_Flattener_ED(cls):
        return cls.from_database(cls._DATABASE['Sky_Watcher_0_85x_Reducer_Flattener_ED'])

    @classmethod
    def Sky_Watcher_0_9x_Reducer_Esprit_150(cls):
        return cls.from_database(cls._DATABASE['Sky_Watcher_0_9x_Reducer_Esprit_150'])

class Sky_watcherFlattener(Flattener):
    _DATABASE = {'Sky_Watcher_Evostar_Flattener': {'brand': 'Sky-Watcher', 'name': 'Evostar Flattener', 'type': 'type_flattener', 'optical_length': 0, 'mass': 200, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Female', 'reversible': False, 'bf_role': 'start'}, 'Sky_Watcher_Esprit_Flattener': {'brand': 'Sky-Watcher', 'name': 'Esprit Flattener', 'type': 'type_flattener', 'optical_length': 0, 'mass': 250, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Female', 'reversible': False, 'bf_role': 'start'}}

    @classmethod
    def Sky_Watcher_Evostar_Flattener(cls):
        return cls.from_database(cls._DATABASE['Sky_Watcher_Evostar_Flattener'])

    @classmethod
    def Sky_Watcher_Esprit_Flattener(cls):
        return cls.from_database(cls._DATABASE['Sky_Watcher_Esprit_Flattener'])

class Sky_watcherCorrector(Corrector):
    _DATABASE = {'Sky_Watcher_Quattro_Coma_Corrector': {'brand': 'Sky-Watcher', 'name': 'Quattro Coma Corrector', 'type': 'type_corrector', 'optical_length': 0, 'mass': 300, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Female', 'reversible': False, 'bf_role': 'start'}, 'Sky_Watcher_Coma_Corrector_F_5_Newton': {'brand': 'Sky-Watcher', 'name': 'Coma Corrector (F/5 Newton)', 'type': 'type_corrector', 'optical_length': 0, 'mass': 280, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Female', 'reversible': False, 'bf_role': 'start'}}

    @classmethod
    def Sky_Watcher_Quattro_Coma_Corrector(cls):
        return cls.from_database(cls._DATABASE['Sky_Watcher_Quattro_Coma_Corrector'])

    @classmethod
    def Sky_Watcher_Coma_Corrector_F_5_Newton(cls):
        return cls.from_database(cls._DATABASE['Sky_Watcher_Coma_Corrector_F_5_Newton'])