from .abstract import IntermediateOpticalEquipment
from ..constants import OpticalType

class AntiTilt(IntermediateOpticalEquipment):
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
        super(AntiTilt, self).__init__(
            vendor, optical_length=optical_length, mass=mass,
            in_connection_type=in_connection_type, out_connection_type=out_connection_type,
            in_gender=in_gender, out_gender=out_gender
        )
        self._type = OpticalType.ANTI_TILT

    _DATABASE = {
        'ZWO_M54_Tilt_Adjuster': {'brand': 'ZWO', 'name': 'M54 Tilt Adjuster', 'type': 'type_anti_tilt', 'optical_length': 11, 'mass': 50, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''},
        'ZWO_Anti_tilt_Plate_6_bolt_5mm': {'brand': 'ZWO', 'name': 'Anti-tilt Plate (6-bolt, 5mm)', 'type': 'type_anti_tilt', 'optical_length': 5, 'mass': 30, 'tside_thread': 'ZWO 6-bolt', 'tside_gender': 'Female', 'cside_thread': 'ZWO 6-bolt', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''},
        'Baader_Anti_tilt_Adapter_M42': {'brand': 'Baader', 'name': 'Anti-tilt Adapter (M42)', 'type': 'type_anti_tilt', 'optical_length': 5, 'mass': 60, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''},
        'Baader_Anti_tilt_Adapter_M48': {'brand': 'Baader', 'name': 'Anti-tilt Adapter (M48)', 'type': 'type_anti_tilt', 'optical_length': 5, 'mass': 70, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''},
        'Baader_Anti_tilt_Adapter_M54': {'brand': 'Baader', 'name': 'Anti-tilt Adapter (M54)', 'type': 'type_anti_tilt', 'optical_length': 5, 'mass': 80, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''},
        'Baader_Anti_tilt_Adapter_M68': {'brand': 'Baader', 'name': 'Anti-tilt Adapter (M68)', 'type': 'type_anti_tilt', 'optical_length': 5, 'mass': 100, 'tside_thread': 'M68', 'tside_gender': 'Female', 'cside_thread': 'M68', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''},
        'Wanderer_Astro_ETA_Electronic_Tilt_Adjuster_M54': {'brand': 'Wanderer Astro', 'name': 'ETA Electronic Tilt Adjuster (M54)', 'type': 'type_anti_tilt', 'optical_length': 11, 'mass': 150, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''},
        'Wanderer_Astro_ETA_Electronic_Tilt_Adjuster_M48': {'brand': 'Wanderer Astro', 'name': 'ETA Electronic Tilt Adjuster (M48)', 'type': 'type_anti_tilt', 'optical_length': 11, 'mass': 140, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''},
        'Wanderer_Astro_ETA_Electronic_Tilt_Adjuster_M68': {'brand': 'Wanderer Astro', 'name': 'ETA Electronic Tilt Adjuster (M68)', 'type': 'type_anti_tilt', 'optical_length': 11, 'mass': 170, 'tside_thread': 'M68', 'tside_gender': 'Female', 'cside_thread': 'M68', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''},
        'Player_One_Tilt_Adjuster_M42': {'brand': 'Player One', 'name': 'Tilt Adjuster (M42)', 'type': 'type_anti_tilt', 'optical_length': 8, 'mass': 40, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''},
        'Player_One_Tilt_Adjuster_M54': {'brand': 'Player One', 'name': 'Tilt Adjuster (M54)', 'type': 'type_anti_tilt', 'optical_length': 10, 'mass': 60, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''},
        'QHY_Tilt_Adjuster_M54': {'brand': 'QHY', 'name': 'Tilt Adjuster (M54)', 'type': 'type_anti_tilt', 'optical_length': 10, 'mass': 70, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''},
        'TS_Optics_Tilt_Adjuster_M48': {'brand': 'TS-Optics', 'name': 'Tilt Adjuster (M48)', 'type': 'type_anti_tilt', 'optical_length': 6, 'mass': 50, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''},
        'TS_Optics_Tilt_Adjuster_M54': {'brand': 'TS-Optics', 'name': 'Tilt Adjuster (M54)', 'type': 'type_anti_tilt', 'optical_length': 6, 'mass': 60, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''},
        'Gerd_Neumann_Tilt_Plate_M48': {'brand': 'Gerd Neumann', 'name': 'Tilt Plate (M48)', 'type': 'type_anti_tilt', 'optical_length': 4, 'mass': 45, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''},
        'Gerd_Neumann_Tilt_Plate_M54': {'brand': 'Gerd Neumann', 'name': 'Tilt Plate (M54)', 'type': 'type_anti_tilt', 'optical_length': 4, 'mass': 55, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''},
        'Gerd_Neumann_Tilt_Plate_M68': {'brand': 'Gerd Neumann', 'name': 'Tilt Plate (M68)', 'type': 'type_anti_tilt', 'optical_length': 4, 'mass': 70, 'tside_thread': 'M68', 'tside_gender': 'Female', 'cside_thread': 'M68', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''},
        'Askar_Tilt_Adjuster_M48': {'brand': 'Askar', 'name': 'Tilt Adjuster (M48)', 'type': 'type_anti_tilt', 'optical_length': 6, 'mass': 50, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''},
        'Askar_Tilt_Adjuster_M54': {'brand': 'Askar', 'name': 'Tilt Adjuster (M54)', 'type': 'type_anti_tilt', 'optical_length': 8, 'mass': 60, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''},
        'Sharpstar_Tilt_Adjuster_M48': {'brand': 'Sharpstar', 'name': 'Tilt Adjuster (M48)', 'type': 'type_anti_tilt', 'optical_length': 6, 'mass': 45, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''},
        'Sharpstar_Tilt_Adjuster_M54': {'brand': 'Sharpstar', 'name': 'Tilt Adjuster (M54)', 'type': 'type_anti_tilt', 'optical_length': 8, 'mass': 55, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''},
        'Altair_Tilt_Adjuster_M42': {'brand': 'Altair', 'name': 'Tilt Adjuster (M42)', 'type': 'type_anti_tilt', 'optical_length': 5, 'mass': 40, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''},
        'Altair_Tilt_Adjuster_M48': {'brand': 'Altair', 'name': 'Tilt Adjuster (M48)', 'type': 'type_anti_tilt', 'optical_length': 6, 'mass': 50, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''},
        'Omegon_Tilt_Adjuster_M42': {'brand': 'Omegon', 'name': 'Tilt Adjuster (M42)', 'type': 'type_anti_tilt', 'optical_length': 5, 'mass': 38, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''},
        'Omegon_Tilt_Adjuster_M48': {'brand': 'Omegon', 'name': 'Tilt Adjuster (M48)', 'type': 'type_anti_tilt', 'optical_length': 6, 'mass': 48, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''},
        'SVBony_Tilt_Adjuster_M42': {'brand': 'SVBony', 'name': 'Tilt Adjuster (M42)', 'type': 'type_anti_tilt', 'optical_length': 5, 'mass': 35, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''},
        'Celestron_Tilt_Adjuster_SC': {'brand': 'Celestron', 'name': 'Tilt Adjuster (SC)', 'type': 'type_anti_tilt', 'optical_length': 8, 'mass': 70, 'tside_thread': 'SC (Schmidt-Cassegrain)', 'tside_gender': 'Female', 'cside_thread': 'SC (Schmidt-Cassegrain)', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''},
        'Explore_Scientific_Tilt_Adjuster_M48': {'brand': 'Explore Scientific', 'name': 'Tilt Adjuster (M48)', 'type': 'type_anti_tilt', 'optical_length': 6, 'mass': 50, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''},
        'APM_Tilt_Adjuster_M54': {'brand': 'APM', 'name': 'Tilt Adjuster (M54)', 'type': 'type_anti_tilt', 'optical_length': 8, 'mass': 55, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''},
        'Stellarvue_Tilt_Plate_M48': {'brand': 'Stellarvue', 'name': 'Tilt Plate (M48)', 'type': 'type_anti_tilt', 'optical_length': 5, 'mass': 45, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''},
        'Stellarvue_Tilt_Plate_M68': {'brand': 'Stellarvue', 'name': 'Tilt Plate (M68)', 'type': 'type_anti_tilt', 'optical_length': 5, 'mass': 60, 'tside_thread': 'M68', 'tside_gender': 'Female', 'cside_thread': 'M68', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''},
        'Takahashi_Tilt_Adjuster_M54': {'brand': 'Takahashi', 'name': 'Tilt Adjuster (M54)', 'type': 'type_anti_tilt', 'optical_length': 8, 'mass': 55, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''},
        'Takahashi_Tilt_Adjuster_M82': {'brand': 'Takahashi', 'name': 'Tilt Adjuster (M82)', 'type': 'type_anti_tilt', 'optical_length': 8, 'mass': 70, 'tside_thread': 'M82', 'tside_gender': 'Female', 'cside_thread': 'M82', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''},
        'Moonlite_Tilt_Adjuster_M42': {'brand': 'Moonlite', 'name': 'Tilt Adjuster (M42)', 'type': 'type_anti_tilt', 'optical_length': 5, 'mass': 40, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''},
        'Moonlite_Tilt_Adjuster_M48': {'brand': 'Moonlite', 'name': 'Tilt Adjuster (M48)', 'type': 'type_anti_tilt', 'optical_length': 6, 'mass': 50, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''},
    }

    @classmethod
    def ZWO_M54_Tilt_Adjuster(cls):
        return cls.from_database(cls._DATABASE['ZWO_M54_Tilt_Adjuster'])

    @classmethod
    def ZWO_Anti_tilt_Plate_6_bolt_5mm(cls):
        return cls.from_database(cls._DATABASE['ZWO_Anti_tilt_Plate_6_bolt_5mm'])

    @classmethod
    def Baader_Anti_tilt_Adapter_M42(cls):
        return cls.from_database(cls._DATABASE['Baader_Anti_tilt_Adapter_M42'])

    @classmethod
    def Baader_Anti_tilt_Adapter_M48(cls):
        return cls.from_database(cls._DATABASE['Baader_Anti_tilt_Adapter_M48'])

    @classmethod
    def Baader_Anti_tilt_Adapter_M54(cls):
        return cls.from_database(cls._DATABASE['Baader_Anti_tilt_Adapter_M54'])

    @classmethod
    def Baader_Anti_tilt_Adapter_M68(cls):
        return cls.from_database(cls._DATABASE['Baader_Anti_tilt_Adapter_M68'])

    @classmethod
    def Wanderer_Astro_ETA_Electronic_Tilt_Adjuster_M54(cls):
        return cls.from_database(cls._DATABASE['Wanderer_Astro_ETA_Electronic_Tilt_Adjuster_M54'])

    @classmethod
    def Wanderer_Astro_ETA_Electronic_Tilt_Adjuster_M48(cls):
        return cls.from_database(cls._DATABASE['Wanderer_Astro_ETA_Electronic_Tilt_Adjuster_M48'])

    @classmethod
    def Wanderer_Astro_ETA_Electronic_Tilt_Adjuster_M68(cls):
        return cls.from_database(cls._DATABASE['Wanderer_Astro_ETA_Electronic_Tilt_Adjuster_M68'])

    @classmethod
    def Player_One_Tilt_Adjuster_M42(cls):
        return cls.from_database(cls._DATABASE['Player_One_Tilt_Adjuster_M42'])

    @classmethod
    def Player_One_Tilt_Adjuster_M54(cls):
        return cls.from_database(cls._DATABASE['Player_One_Tilt_Adjuster_M54'])

    @classmethod
    def QHY_Tilt_Adjuster_M54(cls):
        return cls.from_database(cls._DATABASE['QHY_Tilt_Adjuster_M54'])

    @classmethod
    def TS_Optics_Tilt_Adjuster_M48(cls):
        return cls.from_database(cls._DATABASE['TS_Optics_Tilt_Adjuster_M48'])

    @classmethod
    def TS_Optics_Tilt_Adjuster_M54(cls):
        return cls.from_database(cls._DATABASE['TS_Optics_Tilt_Adjuster_M54'])

    @classmethod
    def Gerd_Neumann_Tilt_Plate_M48(cls):
        return cls.from_database(cls._DATABASE['Gerd_Neumann_Tilt_Plate_M48'])

    @classmethod
    def Gerd_Neumann_Tilt_Plate_M54(cls):
        return cls.from_database(cls._DATABASE['Gerd_Neumann_Tilt_Plate_M54'])

    @classmethod
    def Gerd_Neumann_Tilt_Plate_M68(cls):
        return cls.from_database(cls._DATABASE['Gerd_Neumann_Tilt_Plate_M68'])

    @classmethod
    def Askar_Tilt_Adjuster_M48(cls):
        return cls.from_database(cls._DATABASE['Askar_Tilt_Adjuster_M48'])

    @classmethod
    def Askar_Tilt_Adjuster_M54(cls):
        return cls.from_database(cls._DATABASE['Askar_Tilt_Adjuster_M54'])

    @classmethod
    def Sharpstar_Tilt_Adjuster_M48(cls):
        return cls.from_database(cls._DATABASE['Sharpstar_Tilt_Adjuster_M48'])

    @classmethod
    def Sharpstar_Tilt_Adjuster_M54(cls):
        return cls.from_database(cls._DATABASE['Sharpstar_Tilt_Adjuster_M54'])

    @classmethod
    def Altair_Tilt_Adjuster_M42(cls):
        return cls.from_database(cls._DATABASE['Altair_Tilt_Adjuster_M42'])

    @classmethod
    def Altair_Tilt_Adjuster_M48(cls):
        return cls.from_database(cls._DATABASE['Altair_Tilt_Adjuster_M48'])

    @classmethod
    def Omegon_Tilt_Adjuster_M42(cls):
        return cls.from_database(cls._DATABASE['Omegon_Tilt_Adjuster_M42'])

    @classmethod
    def Omegon_Tilt_Adjuster_M48(cls):
        return cls.from_database(cls._DATABASE['Omegon_Tilt_Adjuster_M48'])

    @classmethod
    def SVBony_Tilt_Adjuster_M42(cls):
        return cls.from_database(cls._DATABASE['SVBony_Tilt_Adjuster_M42'])

    @classmethod
    def Celestron_Tilt_Adjuster_SC(cls):
        return cls.from_database(cls._DATABASE['Celestron_Tilt_Adjuster_SC'])

    @classmethod
    def Explore_Scientific_Tilt_Adjuster_M48(cls):
        return cls.from_database(cls._DATABASE['Explore_Scientific_Tilt_Adjuster_M48'])

    @classmethod
    def APM_Tilt_Adjuster_M54(cls):
        return cls.from_database(cls._DATABASE['APM_Tilt_Adjuster_M54'])

    @classmethod
    def Stellarvue_Tilt_Plate_M48(cls):
        return cls.from_database(cls._DATABASE['Stellarvue_Tilt_Plate_M48'])

    @classmethod
    def Stellarvue_Tilt_Plate_M68(cls):
        return cls.from_database(cls._DATABASE['Stellarvue_Tilt_Plate_M68'])

    @classmethod
    def Takahashi_Tilt_Adjuster_M54(cls):
        return cls.from_database(cls._DATABASE['Takahashi_Tilt_Adjuster_M54'])

    @classmethod
    def Takahashi_Tilt_Adjuster_M82(cls):
        return cls.from_database(cls._DATABASE['Takahashi_Tilt_Adjuster_M82'])

    @classmethod
    def Moonlite_Tilt_Adjuster_M42(cls):
        return cls.from_database(cls._DATABASE['Moonlite_Tilt_Adjuster_M42'])

    @classmethod
    def Moonlite_Tilt_Adjuster_M48(cls):
        return cls.from_database(cls._DATABASE['Moonlite_Tilt_Adjuster_M48'])
