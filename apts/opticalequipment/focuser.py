from .abstract import IntermediateOpticalEquipment
from ..constants import OpticalType

class Focuser(IntermediateOpticalEquipment):
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
        super(Focuser, self).__init__(
            vendor, optical_length=optical_length, mass=mass,
            in_connection_type=in_connection_type, out_connection_type=out_connection_type,
            in_gender=in_gender, out_gender=out_gender
        )
        self._type = OpticalType.FOCUSER

    _DATABASE = {
        'ZWO_EAF': {'brand': 'ZWO', 'name': 'EAF', 'type': 'type_focuser', 'optical_length': 0, 'mass': 115, 'tside_thread': '', 'tside_gender': '', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''},
        'ZWO_EAF_v2': {'brand': 'ZWO', 'name': 'EAF v2', 'type': 'type_focuser', 'optical_length': 0, 'mass': 120, 'tside_thread': '', 'tside_gender': '', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''},
        'Pegasus_FocusCube_3': {'brand': 'Pegasus', 'name': 'FocusCube 3', 'type': 'type_focuser', 'optical_length': 0, 'mass': 115, 'tside_thread': '', 'tside_gender': '', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''},
        'Pegasus_FocusCube_2': {'brand': 'Pegasus', 'name': 'FocusCube 2', 'type': 'type_focuser', 'optical_length': 0, 'mass': 100, 'tside_thread': '', 'tside_gender': '', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''},
        'Pegasus_NYX_Focuser': {'brand': 'Pegasus', 'name': 'NYX Focuser', 'type': 'type_focuser', 'optical_length': 0, 'mass': 300, 'tside_thread': '', 'tside_gender': '', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''},
        'Baader_Steeldrive_II': {'brand': 'Baader', 'name': 'Steeldrive II', 'type': 'type_focuser', 'optical_length': 0, 'mass': 350, 'tside_thread': '', 'tside_gender': '', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''},
        'Baader_Diamond_Steeltrack': {'brand': 'Baader', 'name': 'Diamond Steeltrack', 'type': 'type_focuser', 'optical_length': 0, 'mass': 600, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''},
        'Moonlite_CS_2_Focuser': {'brand': 'Moonlite', 'name': 'CS 2" Focuser', 'type': 'type_focuser', 'optical_length': 0, 'mass': 800, 'tside_thread': '', 'tside_gender': '', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''},
        'Moonlite_CSL_2_5_Focuser': {'brand': 'Moonlite', 'name': 'CSL 2.5" Focuser', 'type': 'type_focuser', 'optical_length': 0, 'mass': 1100, 'tside_thread': '', 'tside_gender': '', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''},
        'Moonlite_NightCrawler_3_Focuser': {'brand': 'Moonlite', 'name': 'NightCrawler 3" Focuser', 'type': 'type_focuser', 'optical_length': 0, 'mass': 1500, 'tside_thread': '', 'tside_gender': '', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''},
        'MicroTouch_WR35_Focuser': {'brand': 'MicroTouch', 'name': 'WR35 Focuser', 'type': 'type_focuser', 'optical_length': 0, 'mass': 200, 'tside_thread': '', 'tside_gender': '', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''},
        'PrimaLuce_ESATTO_2': {'brand': 'PrimaLuce', 'name': 'ESATTO 2"', 'type': 'type_focuser', 'optical_length': 50, 'mass': 670, 'tside_thread': 'M56', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''},
        'PrimaLuce_ESATTO_3': {'brand': 'PrimaLuce', 'name': 'ESATTO 3"', 'type': 'type_focuser', 'optical_length': 58, 'mass': 1300, 'tside_thread': 'SC (Schmidt-Cassegrain)', 'tside_gender': 'Female', 'cside_thread': 'M68', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''},
        'PrimaLuce_SESTO_SENSO_2': {'brand': 'PrimaLuce', 'name': 'SESTO SENSO 2', 'type': 'type_focuser', 'optical_length': 0, 'mass': 180, 'tside_thread': '', 'tside_gender': '', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''},
        'PrimaLuce_GIOTTO': {'brand': 'PrimaLuce', 'name': 'GIOTTO', 'type': 'type_focuser', 'optical_length': 0, 'mass': 250, 'tside_thread': '', 'tside_gender': '', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''},
        'Lacerta_MFOC_Focuser': {'brand': 'Lacerta', 'name': 'MFOC Focuser', 'type': 'type_focuser', 'optical_length': 0, 'mass': 200, 'tside_thread': '', 'tside_gender': '', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''},
        'Starlight_Instruments_Feather_Touch_2': {'brand': 'Starlight Instruments', 'name': 'Feather Touch 2"', 'type': 'type_focuser', 'optical_length': 0, 'mass': 700, 'tside_thread': '', 'tside_gender': '', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''},
        'Starlight_Instruments_Feather_Touch_2_5': {'brand': 'Starlight Instruments', 'name': 'Feather Touch 2.5"', 'type': 'type_focuser', 'optical_length': 0, 'mass': 900, 'tside_thread': '', 'tside_gender': '', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''},
        'Starlight_Instruments_Feather_Touch_3': {'brand': 'Starlight Instruments', 'name': 'Feather Touch 3"', 'type': 'type_focuser', 'optical_length': 0, 'mass': 1200, 'tside_thread': '', 'tside_gender': '', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''},
        'Starlight_Instruments_Feather_Touch_3_5': {'brand': 'Starlight Instruments', 'name': 'Feather Touch 3.5"', 'type': 'type_focuser', 'optical_length': 0, 'mass': 1500, 'tside_thread': '', 'tside_gender': '', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''},
        'Starlight_Instruments_Feather_Touch_4': {'brand': 'Starlight Instruments', 'name': 'Feather Touch 4"', 'type': 'type_focuser', 'optical_length': 0, 'mass': 1800, 'tside_thread': '', 'tside_gender': '', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''},
        'Optec_TCF_S': {'brand': 'Optec', 'name': 'TCF-S', 'type': 'type_focuser', 'optical_length': 0, 'mass': 200, 'tside_thread': '', 'tside_gender': '', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''},
        'Optec_TCF_S3': {'brand': 'Optec', 'name': 'TCF-S3', 'type': 'type_focuser', 'optical_length': 0, 'mass': 250, 'tside_thread': '', 'tside_gender': '', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''},
        'Rigel_Systems_nFocus': {'brand': 'Rigel Systems', 'name': 'nFocus', 'type': 'type_focuser', 'optical_length': 0, 'mass': 120, 'tside_thread': '', 'tside_gender': '', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''},
        'Wanderer_Astro_WandererFocuser': {'brand': 'Wanderer Astro', 'name': 'WandererFocuser', 'type': 'type_focuser', 'optical_length': 0, 'mass': 130, 'tside_thread': '', 'tside_gender': '', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''},
        'Lacerta_2_Micro_Focuser': {'brand': 'Lacerta', 'name': '2" Micro Focuser', 'type': 'type_focuser', 'optical_length': 0, 'mass': 500, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''},
        'Lacerta_2_5_Micro_Focuser': {'brand': 'Lacerta', 'name': '2.5" Micro Focuser', 'type': 'type_focuser', 'optical_length': 0, 'mass': 700, 'tside_thread': 'M68', 'tside_gender': 'Female', 'cside_thread': 'M68', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''},
        'GSO_2_Crayford_Focuser': {'brand': 'GSO', 'name': '2" Crayford Focuser', 'type': 'type_focuser', 'optical_length': 0, 'mass': 600, 'tside_thread': '', 'tside_gender': '', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''},
        'GSO_2_Dual_Speed_Focuser': {'brand': 'GSO', 'name': '2" Dual-Speed Focuser', 'type': 'type_focuser', 'optical_length': 0, 'mass': 650, 'tside_thread': '', 'tside_gender': '', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''},
        'Sky_Watcher_2_Crayford_Focuser': {'brand': 'Sky-Watcher', 'name': '2" Crayford Focuser', 'type': 'type_focuser', 'optical_length': 0, 'mass': 550, 'tside_thread': '', 'tside_gender': '', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''},
        'Sky_Watcher_2_Dual_Speed_Focuser': {'brand': 'Sky-Watcher', 'name': '2" Dual-Speed Focuser', 'type': 'type_focuser', 'optical_length': 0, 'mass': 620, 'tside_thread': '', 'tside_gender': '', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''},
        'Celestron_2_Crayford_Focuser': {'brand': 'Celestron', 'name': '2" Crayford Focuser', 'type': 'type_focuser', 'optical_length': 0, 'mass': 500, 'tside_thread': '', 'tside_gender': '', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''},
        'Orion_2_Crayford_Focuser': {'brand': 'Orion', 'name': '2" Crayford Focuser', 'type': 'type_focuser', 'optical_length': 0, 'mass': 550, 'tside_thread': '', 'tside_gender': '', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''},
        'TS_Optics_2_Crayford_Focuser': {'brand': 'TS-Optics', 'name': '2" Crayford Focuser', 'type': 'type_focuser', 'optical_length': 0, 'mass': 580, 'tside_thread': '', 'tside_gender': '', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''},
        'TS_Optics_3_Rack_Pinion_Focuser': {'brand': 'TS-Optics', 'name': '3" Rack & Pinion Focuser', 'type': 'type_focuser', 'optical_length': 0, 'mass': 1000, 'tside_thread': 'M68', 'tside_gender': 'Female', 'cside_thread': 'M68', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''},
        'Moonlite_CR2_Focuser_2': {'brand': 'Moonlite', 'name': 'CR2 Focuser (2")', 'type': 'type_focuser', 'optical_length': 0, 'mass': 750, 'tside_thread': '', 'tside_gender': '', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''},
        'JMI_EV_1C_Focuser': {'brand': 'JMI', 'name': 'EV-1C Focuser', 'type': 'type_focuser', 'optical_length': 0, 'mass': 200, 'tside_thread': '', 'tside_gender': '', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''},
        'JMI_EV_2C_Focuser': {'brand': 'JMI', 'name': 'EV-2C Focuser', 'type': 'type_focuser', 'optical_length': 0, 'mass': 250, 'tside_thread': '', 'tside_gender': '', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''},
        'JMI_NGF_DX1_Focuser': {'brand': 'JMI', 'name': 'NGF-DX1 Focuser', 'type': 'type_focuser', 'optical_length': 0, 'mass': 600, 'tside_thread': '', 'tside_gender': '', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''},
        'Optec_Leo_Focuser': {'brand': 'Optec', 'name': 'Leo Focuser', 'type': 'type_focuser', 'optical_length': 0, 'mass': 350, 'tside_thread': '', 'tside_gender': '', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''},
        'Optec_FastFocus_FSQ': {'brand': 'Optec', 'name': 'FastFocus FSQ', 'type': 'type_focuser', 'optical_length': 0, 'mass': 150, 'tside_thread': '', 'tside_gender': '', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''},
        'QHY_Q_Focuser': {'brand': 'QHY', 'name': 'Q-Focuser', 'type': 'type_focuser', 'optical_length': 0, 'mass': 180, 'tside_thread': '', 'tside_gender': '', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''},
        'Player_One_Electronic_Focuser': {'brand': 'Player One', 'name': 'Electronic Focuser', 'type': 'type_focuser', 'optical_length': 0, 'mass': 130, 'tside_thread': '', 'tside_gender': '', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''},
        'Altair_Starwave_Auto_Focuser': {'brand': 'Altair', 'name': 'Starwave Auto Focuser', 'type': 'type_focuser', 'optical_length': 0, 'mass': 170, 'tside_thread': '', 'tside_gender': '', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''},
        'SVBony_SV231_Electronic_Focuser': {'brand': 'SVBony', 'name': 'SV231 Electronic Focuser', 'type': 'type_focuser', 'optical_length': 0, 'mass': 120, 'tside_thread': '', 'tside_gender': '', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''},
        'iOptron_iEAF_Electronic_Focuser': {'brand': 'iOptron', 'name': 'iEAF Electronic Focuser', 'type': 'type_focuser', 'optical_length': 0, 'mass': 160, 'tside_thread': '', 'tside_gender': '', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''},
        'ASToptics_Electronic_Focuser': {'brand': 'ASToptics', 'name': 'Electronic Focuser', 'type': 'type_focuser', 'optical_length': 0, 'mass': 140, 'tside_thread': '', 'tside_gender': '', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''},
    }

    @classmethod
    def ZWO_EAF(cls):
        return cls.from_database(cls._DATABASE['ZWO_EAF'])

    @classmethod
    def ZWO_EAF_v2(cls):
        return cls.from_database(cls._DATABASE['ZWO_EAF_v2'])

    @classmethod
    def Pegasus_FocusCube_3(cls):
        return cls.from_database(cls._DATABASE['Pegasus_FocusCube_3'])

    @classmethod
    def Pegasus_FocusCube_2(cls):
        return cls.from_database(cls._DATABASE['Pegasus_FocusCube_2'])

    @classmethod
    def Pegasus_NYX_Focuser(cls):
        return cls.from_database(cls._DATABASE['Pegasus_NYX_Focuser'])

    @classmethod
    def Baader_Steeldrive_II(cls):
        return cls.from_database(cls._DATABASE['Baader_Steeldrive_II'])

    @classmethod
    def Baader_Diamond_Steeltrack(cls):
        return cls.from_database(cls._DATABASE['Baader_Diamond_Steeltrack'])

    @classmethod
    def Moonlite_CS_2_Focuser(cls):
        return cls.from_database(cls._DATABASE['Moonlite_CS_2_Focuser'])

    @classmethod
    def Moonlite_CSL_2_5_Focuser(cls):
        return cls.from_database(cls._DATABASE['Moonlite_CSL_2_5_Focuser'])

    @classmethod
    def Moonlite_NightCrawler_3_Focuser(cls):
        return cls.from_database(cls._DATABASE['Moonlite_NightCrawler_3_Focuser'])

    @classmethod
    def MicroTouch_WR35_Focuser(cls):
        return cls.from_database(cls._DATABASE['MicroTouch_WR35_Focuser'])

    @classmethod
    def PrimaLuce_ESATTO_2(cls):
        return cls.from_database(cls._DATABASE['PrimaLuce_ESATTO_2'])

    @classmethod
    def PrimaLuce_ESATTO_3(cls):
        return cls.from_database(cls._DATABASE['PrimaLuce_ESATTO_3'])

    @classmethod
    def PrimaLuce_SESTO_SENSO_2(cls):
        return cls.from_database(cls._DATABASE['PrimaLuce_SESTO_SENSO_2'])

    @classmethod
    def PrimaLuce_GIOTTO(cls):
        return cls.from_database(cls._DATABASE['PrimaLuce_GIOTTO'])

    @classmethod
    def Lacerta_MFOC_Focuser(cls):
        return cls.from_database(cls._DATABASE['Lacerta_MFOC_Focuser'])

    @classmethod
    def Starlight_Instruments_Feather_Touch_2(cls):
        return cls.from_database(cls._DATABASE['Starlight_Instruments_Feather_Touch_2'])

    @classmethod
    def Starlight_Instruments_Feather_Touch_2_5(cls):
        return cls.from_database(cls._DATABASE['Starlight_Instruments_Feather_Touch_2_5'])

    @classmethod
    def Starlight_Instruments_Feather_Touch_3(cls):
        return cls.from_database(cls._DATABASE['Starlight_Instruments_Feather_Touch_3'])

    @classmethod
    def Starlight_Instruments_Feather_Touch_3_5(cls):
        return cls.from_database(cls._DATABASE['Starlight_Instruments_Feather_Touch_3_5'])

    @classmethod
    def Starlight_Instruments_Feather_Touch_4(cls):
        return cls.from_database(cls._DATABASE['Starlight_Instruments_Feather_Touch_4'])

    @classmethod
    def Optec_TCF_S(cls):
        return cls.from_database(cls._DATABASE['Optec_TCF_S'])

    @classmethod
    def Optec_TCF_S3(cls):
        return cls.from_database(cls._DATABASE['Optec_TCF_S3'])

    @classmethod
    def Rigel_Systems_nFocus(cls):
        return cls.from_database(cls._DATABASE['Rigel_Systems_nFocus'])

    @classmethod
    def Wanderer_Astro_WandererFocuser(cls):
        return cls.from_database(cls._DATABASE['Wanderer_Astro_WandererFocuser'])

    @classmethod
    def Lacerta_2_Micro_Focuser(cls):
        return cls.from_database(cls._DATABASE['Lacerta_2_Micro_Focuser'])

    @classmethod
    def Lacerta_2_5_Micro_Focuser(cls):
        return cls.from_database(cls._DATABASE['Lacerta_2_5_Micro_Focuser'])

    @classmethod
    def GSO_2_Crayford_Focuser(cls):
        return cls.from_database(cls._DATABASE['GSO_2_Crayford_Focuser'])

    @classmethod
    def GSO_2_Dual_Speed_Focuser(cls):
        return cls.from_database(cls._DATABASE['GSO_2_Dual_Speed_Focuser'])

    @classmethod
    def Sky_Watcher_2_Crayford_Focuser(cls):
        return cls.from_database(cls._DATABASE['Sky_Watcher_2_Crayford_Focuser'])

    @classmethod
    def Sky_Watcher_2_Dual_Speed_Focuser(cls):
        return cls.from_database(cls._DATABASE['Sky_Watcher_2_Dual_Speed_Focuser'])

    @classmethod
    def Celestron_2_Crayford_Focuser(cls):
        return cls.from_database(cls._DATABASE['Celestron_2_Crayford_Focuser'])

    @classmethod
    def Orion_2_Crayford_Focuser(cls):
        return cls.from_database(cls._DATABASE['Orion_2_Crayford_Focuser'])

    @classmethod
    def TS_Optics_2_Crayford_Focuser(cls):
        return cls.from_database(cls._DATABASE['TS_Optics_2_Crayford_Focuser'])

    @classmethod
    def TS_Optics_3_Rack_Pinion_Focuser(cls):
        return cls.from_database(cls._DATABASE['TS_Optics_3_Rack_Pinion_Focuser'])

    @classmethod
    def Moonlite_CR2_Focuser_2(cls):
        return cls.from_database(cls._DATABASE['Moonlite_CR2_Focuser_2'])

    @classmethod
    def JMI_EV_1C_Focuser(cls):
        return cls.from_database(cls._DATABASE['JMI_EV_1C_Focuser'])

    @classmethod
    def JMI_EV_2C_Focuser(cls):
        return cls.from_database(cls._DATABASE['JMI_EV_2C_Focuser'])

    @classmethod
    def JMI_NGF_DX1_Focuser(cls):
        return cls.from_database(cls._DATABASE['JMI_NGF_DX1_Focuser'])

    @classmethod
    def Optec_Leo_Focuser(cls):
        return cls.from_database(cls._DATABASE['Optec_Leo_Focuser'])

    @classmethod
    def Optec_FastFocus_FSQ(cls):
        return cls.from_database(cls._DATABASE['Optec_FastFocus_FSQ'])

    @classmethod
    def QHY_Q_Focuser(cls):
        return cls.from_database(cls._DATABASE['QHY_Q_Focuser'])

    @classmethod
    def Player_One_Electronic_Focuser(cls):
        return cls.from_database(cls._DATABASE['Player_One_Electronic_Focuser'])

    @classmethod
    def Altair_Starwave_Auto_Focuser(cls):
        return cls.from_database(cls._DATABASE['Altair_Starwave_Auto_Focuser'])

    @classmethod
    def SVBony_SV231_Electronic_Focuser(cls):
        return cls.from_database(cls._DATABASE['SVBony_SV231_Electronic_Focuser'])

    @classmethod
    def iOptron_iEAF_Electronic_Focuser(cls):
        return cls.from_database(cls._DATABASE['iOptron_iEAF_Electronic_Focuser'])

    @classmethod
    def ASToptics_Electronic_Focuser(cls):
        return cls.from_database(cls._DATABASE['ASToptics_Electronic_Focuser'])
