from .abstract import IntermediateOpticalEquipment
from ..constants import OpticalType


class OAG(IntermediateOpticalEquipment):
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

    def __init__(
        self,
        vendor,
        optical_length=0,
        mass=0,
        in_connection_type=None,
        out_connection_type=None,
        in_gender=None,
        out_gender=None,
    ):
        super(OAG, self).__init__(
            vendor,
            optical_length=optical_length,
            mass=mass,
            in_connection_type=in_connection_type,
            out_connection_type=out_connection_type,
            in_gender=in_gender,
            out_gender=out_gender,
        )
        self._type = OpticalType.OAG

    _DATABASE = {
        "ZWO_OAG_M48_M42": {
            "brand": "ZWO",
            "name": "OAG (M48→M42)",
            "type": "type_oag",
            "optical_length": 16.5,
            "mass": 195,
            "tside_thread": "M48",
            "tside_gender": "Female",
            "cside_thread": "M42",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "ZWO_OAG_M54_M54": {
            "brand": "ZWO",
            "name": "OAG (M54→M54)",
            "type": "type_oag",
            "optical_length": 19.5,
            "mass": 300,
            "tside_thread": "M54",
            "tside_gender": "Female",
            "cside_thread": "M54",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "ZWO_OAG_L_M68_M54": {
            "brand": "ZWO",
            "name": "OAG-L (M68→M54)",
            "type": "type_oag",
            "optical_length": 22.5,
            "mass": 380,
            "tside_thread": "M68",
            "tside_gender": "Female",
            "cside_thread": "M54",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "QHY_OAG_M_M48_M42": {
            "brand": "QHY",
            "name": "OAG-M (M48→M42)",
            "type": "type_oag",
            "optical_length": 18,
            "mass": 250,
            "tside_thread": "M48",
            "tside_gender": "Female",
            "cside_thread": "M42",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "QHY_OAG_S_M42": {
            "brand": "QHY",
            "name": "OAG-S (M42)",
            "type": "type_oag",
            "optical_length": 14,
            "mass": 180,
            "tside_thread": "M42",
            "tside_gender": "Female",
            "cside_thread": "M42",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "QHY_OAG_L_M54": {
            "brand": "QHY",
            "name": "OAG-L (M54)",
            "type": "type_oag",
            "optical_length": 21,
            "mass": 350,
            "tside_thread": "M54",
            "tside_gender": "Female",
            "cside_thread": "M54",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Player_One_OAG_M42": {
            "brand": "Player One",
            "name": "OAG (M42)",
            "type": "type_oag",
            "optical_length": 16.5,
            "mass": 180,
            "tside_thread": "M42",
            "tside_gender": "Female",
            "cside_thread": "M42",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Player_One_OAG_L_M54": {
            "brand": "Player One",
            "name": "OAG-L (M54)",
            "type": "type_oag",
            "optical_length": 20,
            "mass": 300,
            "tside_thread": "M54",
            "tside_gender": "Female",
            "cside_thread": "M54",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Celestron_OAG_SCT": {
            "brand": "Celestron",
            "name": "OAG (SCT)",
            "type": "type_oag",
            "optical_length": 19,
            "mass": 200,
            "tside_thread": "SC (Schmidt-Cassegrain)",
            "tside_gender": "Female",
            "cside_thread": "M42",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Lacerta_OAG_M48": {
            "brand": "Lacerta",
            "name": "OAG (M48)",
            "type": "type_oag",
            "optical_length": 17,
            "mass": 200,
            "tside_thread": "M48",
            "tside_gender": "Female",
            "cside_thread": "M42",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Orion_Thin_OAG_M48": {
            "brand": "Orion",
            "name": "Thin OAG (M48)",
            "type": "type_oag",
            "optical_length": 12,
            "mass": 170,
            "tside_thread": "M48",
            "tside_gender": "Female",
            "cside_thread": "M42",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Starlight_Xpress_Lodestar_OAG": {
            "brand": "Starlight Xpress",
            "name": "Lodestar OAG",
            "type": "type_oag",
            "optical_length": 15,
            "mass": 160,
            "tside_thread": "M42",
            "tside_gender": "Female",
            "cside_thread": "M42",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Pegasus_OAG_M42": {
            "brand": "Pegasus",
            "name": "OAG (M42)",
            "type": "type_oag",
            "optical_length": 16,
            "mass": 175,
            "tside_thread": "M42",
            "tside_gender": "Female",
            "cside_thread": "M42",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Pegasus_OAG_M54": {
            "brand": "Pegasus",
            "name": "OAG (M54)",
            "type": "type_oag",
            "optical_length": 19,
            "mass": 280,
            "tside_thread": "M54",
            "tside_gender": "Female",
            "cside_thread": "M54",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Baader_FlipMirror_OAG": {
            "brand": "Baader",
            "name": "FlipMirror OAG",
            "type": "type_oag",
            "optical_length": 20,
            "mass": 300,
            "tside_thread": "M48",
            "tside_gender": "Female",
            "cside_thread": "M42",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "SVBony_OAG_M42": {
            "brand": "SVBony",
            "name": "OAG (M42)",
            "type": "type_oag",
            "optical_length": 15,
            "mass": 150,
            "tside_thread": "M42",
            "tside_gender": "Female",
            "cside_thread": "M42",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "TS_Optics_OAG_M48": {
            "brand": "TS-Optics",
            "name": "OAG (M48)",
            "type": "type_oag",
            "optical_length": 17,
            "mass": 190,
            "tside_thread": "M48",
            "tside_gender": "Female",
            "cside_thread": "M42",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "TS_Optics_OAG_M54": {
            "brand": "TS-Optics",
            "name": "OAG (M54)",
            "type": "type_oag",
            "optical_length": 20,
            "mass": 280,
            "tside_thread": "M54",
            "tside_gender": "Female",
            "cside_thread": "M54",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "OGMA_OAG_M42": {
            "brand": "OGMA",
            "name": "OAG (M42)",
            "type": "type_oag",
            "optical_length": 16,
            "mass": 165,
            "tside_thread": "M42",
            "tside_gender": "Female",
            "cside_thread": "M42",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Altair_OAG_M42": {
            "brand": "Altair",
            "name": "OAG (M42)",
            "type": "type_oag",
            "optical_length": 16,
            "mass": 170,
            "tside_thread": "M42",
            "tside_gender": "Female",
            "cside_thread": "M42",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Altair_OAG_M54": {
            "brand": "Altair",
            "name": "OAG (M54)",
            "type": "type_oag",
            "optical_length": 19,
            "mass": 280,
            "tside_thread": "M54",
            "tside_gender": "Female",
            "cside_thread": "M54",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Moravian_OAG_M54": {
            "brand": "Moravian",
            "name": "OAG (M54)",
            "type": "type_oag",
            "optical_length": 18,
            "mass": 260,
            "tside_thread": "M54",
            "tside_gender": "Female",
            "cside_thread": "M54",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Rising_Cam_OAG_M42": {
            "brand": "Rising Cam",
            "name": "OAG (M42)",
            "type": "type_oag",
            "optical_length": 15,
            "mass": 160,
            "tside_thread": "M42",
            "tside_gender": "Female",
            "cside_thread": "M42",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "ToupTek_OAG_M42": {
            "brand": "ToupTek",
            "name": "OAG (M42)",
            "type": "type_oag",
            "optical_length": 16,
            "mass": 170,
            "tside_thread": "M42",
            "tside_gender": "Female",
            "cside_thread": "M42",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Omegon_OAG_M42": {
            "brand": "Omegon",
            "name": "OAG (M42)",
            "type": "type_oag",
            "optical_length": 15,
            "mass": 165,
            "tside_thread": "M42",
            "tside_gender": "Female",
            "cside_thread": "M42",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Wanderer_Astro_OAG_M42": {
            "brand": "Wanderer Astro",
            "name": "OAG (M42)",
            "type": "type_oag",
            "optical_length": 16,
            "mass": 170,
            "tside_thread": "M42",
            "tside_gender": "Female",
            "cside_thread": "M42",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Wanderer_Astro_OAG_M54": {
            "brand": "Wanderer Astro",
            "name": "OAG (M54)",
            "type": "type_oag",
            "optical_length": 19,
            "mass": 280,
            "tside_thread": "M54",
            "tside_gender": "Female",
            "cside_thread": "M54",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Askar_OAG_M48": {
            "brand": "Askar",
            "name": "OAG (M48)",
            "type": "type_oag",
            "optical_length": 17,
            "mass": 195,
            "tside_thread": "M48",
            "tside_gender": "Female",
            "cside_thread": "M42",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Askar_OAG_M54": {
            "brand": "Askar",
            "name": "OAG (M54)",
            "type": "type_oag",
            "optical_length": 20,
            "mass": 290,
            "tside_thread": "M54",
            "tside_gender": "Female",
            "cside_thread": "M54",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Sharpstar_OAG_M48": {
            "brand": "Sharpstar",
            "name": "OAG (M48)",
            "type": "type_oag",
            "optical_length": 17,
            "mass": 185,
            "tside_thread": "M48",
            "tside_gender": "Female",
            "cside_thread": "M42",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Sharpstar_OAG_M54": {
            "brand": "Sharpstar",
            "name": "OAG (M54)",
            "type": "type_oag",
            "optical_length": 20,
            "mass": 280,
            "tside_thread": "M54",
            "tside_gender": "Female",
            "cside_thread": "M54",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Altair_Deluxe_OAG_M48": {
            "brand": "Altair",
            "name": "Deluxe OAG (M48)",
            "type": "type_oag",
            "optical_length": 17,
            "mass": 200,
            "tside_thread": "M48",
            "tside_gender": "Female",
            "cside_thread": "M42",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Altair_Deluxe_OAG_M54": {
            "brand": "Altair",
            "name": "Deluxe OAG (M54)",
            "type": "type_oag",
            "optical_length": 20,
            "mass": 290,
            "tside_thread": "M54",
            "tside_gender": "Female",
            "cside_thread": "M54",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Omegon_OAG_M48": {
            "brand": "Omegon",
            "name": "OAG (M48)",
            "type": "type_oag",
            "optical_length": 17,
            "mass": 190,
            "tside_thread": "M48",
            "tside_gender": "Female",
            "cside_thread": "M42",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Meade_OAG_SCT": {
            "brand": "Meade",
            "name": "OAG (SCT)",
            "type": "type_oag",
            "optical_length": 19,
            "mass": 210,
            "tside_thread": "SC (Schmidt-Cassegrain)",
            "tside_gender": "Female",
            "cside_thread": "M42",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Explore_Scientific_OAG_M48": {
            "brand": "Explore Scientific",
            "name": "OAG (M48)",
            "type": "type_oag",
            "optical_length": 17,
            "mass": 200,
            "tside_thread": "M48",
            "tside_gender": "Female",
            "cside_thread": "M42",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "APM_OAG_M48": {
            "brand": "APM",
            "name": "OAG (M48)",
            "type": "type_oag",
            "optical_length": 17,
            "mass": 200,
            "tside_thread": "M48",
            "tside_gender": "Female",
            "cside_thread": "M42",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Vixen_OAG_M42": {
            "brand": "Vixen",
            "name": "OAG (M42)",
            "type": "type_oag",
            "optical_length": 16,
            "mass": 180,
            "tside_thread": "M42",
            "tside_gender": "Female",
            "cside_thread": "M42",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Bresser_OAG_M42": {
            "brand": "Bresser",
            "name": "OAG (M42)",
            "type": "type_oag",
            "optical_length": 15,
            "mass": 160,
            "tside_thread": "M42",
            "tside_gender": "Female",
            "cside_thread": "M42",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
    }

    @classmethod
    def ZWO_OAG_M48_M42(cls):
        return cls.from_database(cls._DATABASE["ZWO_OAG_M48_M42"])

    @classmethod
    def ZWO_OAG_M54_M54(cls):
        return cls.from_database(cls._DATABASE["ZWO_OAG_M54_M54"])

    @classmethod
    def ZWO_OAG_L_M68_M54(cls):
        return cls.from_database(cls._DATABASE["ZWO_OAG_L_M68_M54"])

    @classmethod
    def QHY_OAG_M_M48_M42(cls):
        return cls.from_database(cls._DATABASE["QHY_OAG_M_M48_M42"])

    @classmethod
    def QHY_OAG_S_M42(cls):
        return cls.from_database(cls._DATABASE["QHY_OAG_S_M42"])

    @classmethod
    def QHY_OAG_L_M54(cls):
        return cls.from_database(cls._DATABASE["QHY_OAG_L_M54"])

    @classmethod
    def Player_One_OAG_M42(cls):
        return cls.from_database(cls._DATABASE["Player_One_OAG_M42"])

    @classmethod
    def Player_One_OAG_L_M54(cls):
        return cls.from_database(cls._DATABASE["Player_One_OAG_L_M54"])

    @classmethod
    def Celestron_OAG_SCT(cls):
        return cls.from_database(cls._DATABASE["Celestron_OAG_SCT"])

    @classmethod
    def Lacerta_OAG_M48(cls):
        return cls.from_database(cls._DATABASE["Lacerta_OAG_M48"])

    @classmethod
    def Orion_Thin_OAG_M48(cls):
        return cls.from_database(cls._DATABASE["Orion_Thin_OAG_M48"])

    @classmethod
    def Starlight_Xpress_Lodestar_OAG(cls):
        return cls.from_database(cls._DATABASE["Starlight_Xpress_Lodestar_OAG"])

    @classmethod
    def Pegasus_OAG_M42(cls):
        return cls.from_database(cls._DATABASE["Pegasus_OAG_M42"])

    @classmethod
    def Pegasus_OAG_M54(cls):
        return cls.from_database(cls._DATABASE["Pegasus_OAG_M54"])

    @classmethod
    def Baader_FlipMirror_OAG(cls):
        return cls.from_database(cls._DATABASE["Baader_FlipMirror_OAG"])

    @classmethod
    def SVBony_OAG_M42(cls):
        return cls.from_database(cls._DATABASE["SVBony_OAG_M42"])

    @classmethod
    def TS_Optics_OAG_M48(cls):
        return cls.from_database(cls._DATABASE["TS_Optics_OAG_M48"])

    @classmethod
    def TS_Optics_OAG_M54(cls):
        return cls.from_database(cls._DATABASE["TS_Optics_OAG_M54"])

    @classmethod
    def OGMA_OAG_M42(cls):
        return cls.from_database(cls._DATABASE["OGMA_OAG_M42"])

    @classmethod
    def Altair_OAG_M42(cls):
        return cls.from_database(cls._DATABASE["Altair_OAG_M42"])

    @classmethod
    def Altair_OAG_M54(cls):
        return cls.from_database(cls._DATABASE["Altair_OAG_M54"])

    @classmethod
    def Moravian_OAG_M54(cls):
        return cls.from_database(cls._DATABASE["Moravian_OAG_M54"])

    @classmethod
    def Rising_Cam_OAG_M42(cls):
        return cls.from_database(cls._DATABASE["Rising_Cam_OAG_M42"])

    @classmethod
    def ToupTek_OAG_M42(cls):
        return cls.from_database(cls._DATABASE["ToupTek_OAG_M42"])

    @classmethod
    def Omegon_OAG_M42(cls):
        return cls.from_database(cls._DATABASE["Omegon_OAG_M42"])

    @classmethod
    def Wanderer_Astro_OAG_M42(cls):
        return cls.from_database(cls._DATABASE["Wanderer_Astro_OAG_M42"])

    @classmethod
    def Wanderer_Astro_OAG_M54(cls):
        return cls.from_database(cls._DATABASE["Wanderer_Astro_OAG_M54"])

    @classmethod
    def Askar_OAG_M48(cls):
        return cls.from_database(cls._DATABASE["Askar_OAG_M48"])

    @classmethod
    def Askar_OAG_M54(cls):
        return cls.from_database(cls._DATABASE["Askar_OAG_M54"])

    @classmethod
    def Sharpstar_OAG_M48(cls):
        return cls.from_database(cls._DATABASE["Sharpstar_OAG_M48"])

    @classmethod
    def Sharpstar_OAG_M54(cls):
        return cls.from_database(cls._DATABASE["Sharpstar_OAG_M54"])

    @classmethod
    def Altair_Deluxe_OAG_M48(cls):
        return cls.from_database(cls._DATABASE["Altair_Deluxe_OAG_M48"])

    @classmethod
    def Altair_Deluxe_OAG_M54(cls):
        return cls.from_database(cls._DATABASE["Altair_Deluxe_OAG_M54"])

    @classmethod
    def Omegon_OAG_M48(cls):
        return cls.from_database(cls._DATABASE["Omegon_OAG_M48"])

    @classmethod
    def Meade_OAG_SCT(cls):
        return cls.from_database(cls._DATABASE["Meade_OAG_SCT"])

    @classmethod
    def Explore_Scientific_OAG_M48(cls):
        return cls.from_database(cls._DATABASE["Explore_Scientific_OAG_M48"])

    @classmethod
    def APM_OAG_M48(cls):
        return cls.from_database(cls._DATABASE["APM_OAG_M48"])

    @classmethod
    def Vixen_OAG_M42(cls):
        return cls.from_database(cls._DATABASE["Vixen_OAG_M42"])

    @classmethod
    def Bresser_OAG_M42(cls):
        return cls.from_database(cls._DATABASE["Bresser_OAG_M42"])
