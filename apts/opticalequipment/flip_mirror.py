from .abstract import IntermediateOpticalEquipment
from ..constants import OpticalType

class FlipMirror(IntermediateOpticalEquipment):
    @classmethod
    def from_database(cls, entry):
        from ..utils import Utils, Gender
        brand = entry["brand"]
        name = entry["name"]
        vendor = f"{brand} {name}"
        ol = entry.get("optical_length", 0)
        mass = entry.get("mass", 0)
        tt = Utils.map_conn(entry.get("tside_thread"))
        tg = Utils.map_gender(entry.get("tside_gender"))
        ct = Utils.map_conn(entry.get("cside_thread"))
        cg = Utils.map_gender(entry.get("cside_gender"))
        return cls(
            vendor,
            optical_length=ol,
            mass=mass,
            in_connection_type=tt,
            out_connection_type=ct,
            in_gender=tg or Gender.MALE,
            out_gender=cg or Gender.FEMALE,
        )
    @classmethod
    def from_database(cls, entry):
        from ..utils import Utils, Gender
        brand = entry["brand"]
        name = entry["name"]
        vendor = f"{brand} {name}"
        ol = entry.get("optical_length", 0)
        mass = entry.get("mass", 0)
        tt = Utils.map_conn(entry.get("tside_thread"))
        tg = Utils.map_gender(entry.get("tside_gender"))
        ct = Utils.map_conn(entry.get("cside_thread"))
        cg = Utils.map_gender(entry.get("cside_gender"))
        return cls(
            vendor,
            optical_length=ol,
            mass=mass,
            in_connection_type=tt,
            out_connection_type=ct,
            in_gender=tg or Gender.MALE,
            out_gender=cg or Gender.FEMALE,
        )
    def __init__(self, vendor, optical_length=0, mass=0, in_connection_type=None, out_connection_type=None, in_gender=None, out_gender=None):
        super(FlipMirror, self).__init__(
            vendor, optical_length=optical_length, mass=mass,
            in_connection_type=in_connection_type, out_connection_type=out_connection_type,
            in_gender=in_gender, out_gender=out_gender
        )
        self._type = OpticalType.FLIP_MIRROR

    _DATABASE = {
        'Baader_Flipmirror_II': {'brand': 'Baader', 'name': 'Flipmirror II', 'type': 'type_flip_mirror', 'optical_length': 0, 'mass': 600, 'tside_thread': '2"', 'tside_gender': 'Female', 'cside_thread': '1.25"', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''},
        'GSO_Flip_Mirror': {'brand': 'GSO', 'name': 'Flip Mirror', 'type': 'type_flip_mirror', 'optical_length': 0, 'mass': 500, 'tside_thread': '2"', 'tside_gender': 'Female', 'cside_thread': '1.25"', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''},
        'Orion_Flip_Mirror': {'brand': 'Orion', 'name': 'Flip Mirror', 'type': 'type_flip_mirror', 'optical_length': 0, 'mass': 520, 'tside_thread': '2"', 'tside_gender': 'Female', 'cside_thread': '1.25"', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''},
        'Celestron_Flip_Mirror': {'brand': 'Celestron', 'name': 'Flip Mirror', 'type': 'type_flip_mirror', 'optical_length': 0, 'mass': 480, 'tside_thread': '1.25"', 'tside_gender': 'Female', 'cside_thread': '1.25"', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''},
        'Meade_Flip_Mirror': {'brand': 'Meade', 'name': 'Flip Mirror', 'type': 'type_flip_mirror', 'optical_length': 0, 'mass': 500, 'tside_thread': '2"', 'tside_gender': 'Female', 'cside_thread': '1.25"', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''},
        'TS_Optics_Flip_Mirror': {'brand': 'TS-Optics', 'name': 'Flip Mirror', 'type': 'type_flip_mirror', 'optical_length': 0, 'mass': 480, 'tside_thread': '2"', 'tside_gender': 'Female', 'cside_thread': '1.25"', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''},
        'William_Optics_Flip_Mirror': {'brand': 'William Optics', 'name': 'Flip Mirror', 'type': 'type_flip_mirror', 'optical_length': 0, 'mass': 550, 'tside_thread': '2"', 'tside_gender': 'Female', 'cside_thread': '1.25"', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''},
        'Sky_Watcher_Flip_Mirror': {'brand': 'Sky-Watcher', 'name': 'Flip Mirror', 'type': 'type_flip_mirror', 'optical_length': 0, 'mass': 470, 'tside_thread': '2"', 'tside_gender': 'Female', 'cside_thread': '1.25"', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''},
        'Explore_Scientific_Flip_Mirror': {'brand': 'Explore Scientific', 'name': 'Flip Mirror', 'type': 'type_flip_mirror', 'optical_length': 0, 'mass': 500, 'tside_thread': '2"', 'tside_gender': 'Female', 'cside_thread': '1.25"', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''},
        'Bresser_Flip_Mirror': {'brand': 'Bresser', 'name': 'Flip Mirror', 'type': 'type_flip_mirror', 'optical_length': 0, 'mass': 470, 'tside_thread': '2"', 'tside_gender': 'Female', 'cside_thread': '1.25"', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''},
        'Omegon_Flip_Mirror': {'brand': 'Omegon', 'name': 'Flip Mirror', 'type': 'type_flip_mirror', 'optical_length': 0, 'mass': 490, 'tside_thread': '2"', 'tside_gender': 'Female', 'cside_thread': '1.25"', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''},
        'SVBony_SV211_Flip_Mirror': {'brand': 'SVBony', 'name': 'SV211 Flip Mirror', 'type': 'type_flip_mirror', 'optical_length': 0, 'mass': 460, 'tside_thread': '2"', 'tside_gender': 'Female', 'cside_thread': '1.25"', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''},
        'Lacerta_Flip_Mirror': {'brand': 'Lacerta', 'name': 'Flip Mirror', 'type': 'type_flip_mirror', 'optical_length': 0, 'mass': 500, 'tside_thread': '2"', 'tside_gender': 'Female', 'cside_thread': '1.25"', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''},
        'Saxon_Flip_Mirror': {'brand': 'Saxon', 'name': 'Flip Mirror', 'type': 'type_flip_mirror', 'optical_length': 0, 'mass': 450, 'tside_thread': '2"', 'tside_gender': 'Female', 'cside_thread': '1.25"', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''},
        'National_Geographic_Flip_Mirror': {'brand': 'National Geographic', 'name': 'Flip Mirror', 'type': 'type_flip_mirror', 'optical_length': 0, 'mass': 420, 'tside_thread': '2"', 'tside_gender': 'Female', 'cside_thread': '1.25"', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''},
        'Lacerta_Flipmirror': {'brand': 'Lacerta', 'name': 'Flipmirror', 'type': 'type_flip_mirror', 'optical_length': 0, 'mass': 490, 'tside_thread': '2"', 'tside_gender': 'Female', 'cside_thread': '1.25"', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''},
        'APM_Flipmirror': {'brand': 'APM', 'name': 'Flipmirror', 'type': 'type_flip_mirror', 'optical_length': 0, 'mass': 510, 'tside_thread': '2"', 'tside_gender': 'Female', 'cside_thread': '1.25"', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''},
        'Altair_Flipmirror': {'brand': 'Altair', 'name': 'Flipmirror', 'type': 'type_flip_mirror', 'optical_length': 0, 'mass': 480, 'tside_thread': '2"', 'tside_gender': 'Female', 'cside_thread': '1.25"', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''},
        'Explore_Scientific_Flipmirror': {'brand': 'Explore Scientific', 'name': 'Flipmirror', 'type': 'type_flip_mirror', 'optical_length': 0, 'mass': 500, 'tside_thread': '2"', 'tside_gender': 'Female', 'cside_thread': '1.25"', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''},
        'Vixen_Flipmirror': {'brand': 'Vixen', 'name': 'Flipmirror', 'type': 'type_flip_mirror', 'optical_length': 0, 'mass': 460, 'tside_thread': '2"', 'tside_gender': 'Female', 'cside_thread': '1.25"', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''},
        'SVBony_SV123_Flipmirror': {'brand': 'SVBony', 'name': 'SV123 Flipmirror', 'type': 'type_flip_mirror', 'optical_length': 0, 'mass': 400, 'tside_thread': '2"', 'tside_gender': 'Female', 'cside_thread': '1.25"', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''},
    }

    @classmethod
    def Baader_Flipmirror_II(cls):
        return cls.from_database(cls._DATABASE['Baader_Flipmirror_II'])

    @classmethod
    def GSO_Flip_Mirror(cls):
        return cls.from_database(cls._DATABASE['GSO_Flip_Mirror'])

    @classmethod
    def Orion_Flip_Mirror(cls):
        return cls.from_database(cls._DATABASE['Orion_Flip_Mirror'])

    @classmethod
    def Celestron_Flip_Mirror(cls):
        return cls.from_database(cls._DATABASE['Celestron_Flip_Mirror'])

    @classmethod
    def Meade_Flip_Mirror(cls):
        return cls.from_database(cls._DATABASE['Meade_Flip_Mirror'])

    @classmethod
    def TS_Optics_Flip_Mirror(cls):
        return cls.from_database(cls._DATABASE['TS_Optics_Flip_Mirror'])

    @classmethod
    def William_Optics_Flip_Mirror(cls):
        return cls.from_database(cls._DATABASE['William_Optics_Flip_Mirror'])

    @classmethod
    def Sky_Watcher_Flip_Mirror(cls):
        return cls.from_database(cls._DATABASE['Sky_Watcher_Flip_Mirror'])

    @classmethod
    def Explore_Scientific_Flip_Mirror(cls):
        return cls.from_database(cls._DATABASE['Explore_Scientific_Flip_Mirror'])

    @classmethod
    def Bresser_Flip_Mirror(cls):
        return cls.from_database(cls._DATABASE['Bresser_Flip_Mirror'])

    @classmethod
    def Omegon_Flip_Mirror(cls):
        return cls.from_database(cls._DATABASE['Omegon_Flip_Mirror'])

    @classmethod
    def SVBony_SV211_Flip_Mirror(cls):
        return cls.from_database(cls._DATABASE['SVBony_SV211_Flip_Mirror'])

    @classmethod
    def Lacerta_Flip_Mirror(cls):
        return cls.from_database(cls._DATABASE['Lacerta_Flip_Mirror'])

    @classmethod
    def Saxon_Flip_Mirror(cls):
        return cls.from_database(cls._DATABASE['Saxon_Flip_Mirror'])

    @classmethod
    def National_Geographic_Flip_Mirror(cls):
        return cls.from_database(cls._DATABASE['National_Geographic_Flip_Mirror'])

    @classmethod
    def Lacerta_Flipmirror(cls):
        return cls.from_database(cls._DATABASE['Lacerta_Flipmirror'])

    @classmethod
    def APM_Flipmirror(cls):
        return cls.from_database(cls._DATABASE['APM_Flipmirror'])

    @classmethod
    def Altair_Flipmirror(cls):
        return cls.from_database(cls._DATABASE['Altair_Flipmirror'])

    @classmethod
    def Explore_Scientific_Flipmirror(cls):
        return cls.from_database(cls._DATABASE['Explore_Scientific_Flipmirror'])

    @classmethod
    def Vixen_Flipmirror(cls):
        return cls.from_database(cls._DATABASE['Vixen_Flipmirror'])

    @classmethod
    def SVBony_SV123_Flipmirror(cls):
        return cls.from_database(cls._DATABASE['SVBony_SV123_Flipmirror'])
