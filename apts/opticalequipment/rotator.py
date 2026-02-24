from .abstract import IntermediateOpticalEquipment
from ..constants import OpticalType


class Rotator(IntermediateOpticalEquipment):
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
        super(Rotator, self).__init__(
            vendor,
            optical_length=optical_length,
            mass=mass,
            in_connection_type=in_connection_type,
            out_connection_type=out_connection_type,
            in_gender=in_gender,
            out_gender=out_gender,
        )
        self._type = OpticalType.ROTATOR

    _DATABASE = {
        "Pegasus_Falcon_Rotator_M42": {
            "brand": "Pegasus",
            "name": "Falcon Rotator (M42)",
            "type": "type_rotator",
            "optical_length": 11,
            "mass": 250,
            "tside_thread": "M42",
            "tside_gender": "Female",
            "cside_thread": "M42",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Pegasus_Falcon_Rotator_M48": {
            "brand": "Pegasus",
            "name": "Falcon Rotator (M48)",
            "type": "type_rotator",
            "optical_length": 12.5,
            "mass": 300,
            "tside_thread": "M48",
            "tside_gender": "Female",
            "cside_thread": "M48",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Pegasus_Falcon_Rotator_M54": {
            "brand": "Pegasus",
            "name": "Falcon Rotator (M54)",
            "type": "type_rotator",
            "optical_length": 12,
            "mass": 320,
            "tside_thread": "M54",
            "tside_gender": "Female",
            "cside_thread": "M54",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Pegasus_Falcon_Rotator_M68": {
            "brand": "Pegasus",
            "name": "Falcon Rotator (M68)",
            "type": "type_rotator",
            "optical_length": 12,
            "mass": 350,
            "tside_thread": "M68",
            "tside_gender": "Female",
            "cside_thread": "M68",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "ZWO_EAF_Rotator_M42": {
            "brand": "ZWO",
            "name": "EAF + Rotator (M42)",
            "type": "type_rotator",
            "optical_length": 12,
            "mass": 250,
            "tside_thread": "M42",
            "tside_gender": "Female",
            "cside_thread": "M42",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "ARCO_2_Camera_Rotator_M48": {
            "brand": "ARCO",
            "name": '2" Camera Rotator (M48)',
            "type": "type_rotator",
            "optical_length": 12,
            "mass": 400,
            "tside_thread": "M48",
            "tside_gender": "Female",
            "cside_thread": "M48",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "ARCO_2_Camera_Rotator_M54": {
            "brand": "ARCO",
            "name": '2" Camera Rotator (M54)',
            "type": "type_rotator",
            "optical_length": 12,
            "mass": 420,
            "tside_thread": "M54",
            "tside_gender": "Female",
            "cside_thread": "M54",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "ARCO_2_Camera_Rotator_M68": {
            "brand": "ARCO",
            "name": '2" Camera Rotator (M68)',
            "type": "type_rotator",
            "optical_length": 12,
            "mass": 450,
            "tside_thread": "M68",
            "tside_gender": "Female",
            "cside_thread": "M68",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Player_One_Ares_Rotator_M54": {
            "brand": "Player One",
            "name": "Ares Rotator (M54)",
            "type": "type_rotator",
            "optical_length": 11,
            "mass": 250,
            "tside_thread": "M54",
            "tside_gender": "Female",
            "cside_thread": "M54",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Optec_Gemini_Rotator_M68": {
            "brand": "Optec",
            "name": "Gemini Rotator (M68)",
            "type": "type_rotator",
            "optical_length": 12,
            "mass": 500,
            "tside_thread": "M68",
            "tside_gender": "Female",
            "cside_thread": "M68",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Optec_Gemini_Rotator_M54": {
            "brand": "Optec",
            "name": "Gemini Rotator (M54)",
            "type": "type_rotator",
            "optical_length": 12,
            "mass": 450,
            "tside_thread": "M54",
            "tside_gender": "Female",
            "cside_thread": "M54",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "PrimaLuce_EAGLE_Rotator_M48": {
            "brand": "PrimaLuce",
            "name": "EAGLE Rotator (M48)",
            "type": "type_rotator",
            "optical_length": 12,
            "mass": 350,
            "tside_thread": "M48",
            "tside_gender": "Female",
            "cside_thread": "M48",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "PrimaLuce_EAGLE_Rotator_M54": {
            "brand": "PrimaLuce",
            "name": "EAGLE Rotator (M54)",
            "type": "type_rotator",
            "optical_length": 12,
            "mass": 380,
            "tside_thread": "M54",
            "tside_gender": "Female",
            "cside_thread": "M54",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Lacerta_Rotator_M42": {
            "brand": "Lacerta",
            "name": "Rotator (M42)",
            "type": "type_rotator",
            "optical_length": 11,
            "mass": 200,
            "tside_thread": "M42",
            "tside_gender": "Female",
            "cside_thread": "M42",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Lacerta_Rotator_M48": {
            "brand": "Lacerta",
            "name": "Rotator (M48)",
            "type": "type_rotator",
            "optical_length": 12,
            "mass": 280,
            "tside_thread": "M48",
            "tside_gender": "Female",
            "cside_thread": "M48",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "TS_Optics_TSRot2_M54": {
            "brand": "TS-Optics",
            "name": "TSRot2 (M54)",
            "type": "type_rotator",
            "optical_length": 12,
            "mass": 320,
            "tside_thread": "M54",
            "tside_gender": "Female",
            "cside_thread": "M54",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Wanderer_Astro_Field_Rotator_M48": {
            "brand": "Wanderer Astro",
            "name": "Field Rotator (M48)",
            "type": "type_rotator",
            "optical_length": 11,
            "mass": 300,
            "tside_thread": "M48",
            "tside_gender": "Female",
            "cside_thread": "M48",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Wanderer_Astro_Field_Rotator_M54": {
            "brand": "Wanderer Astro",
            "name": "Field Rotator (M54)",
            "type": "type_rotator",
            "optical_length": 11,
            "mass": 320,
            "tside_thread": "M54",
            "tside_gender": "Female",
            "cside_thread": "M54",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Wanderer_Astro_Rotator_Mini_V2_M54": {
            "brand": "Wanderer Astro",
            "name": "Rotator Mini V2 (M54)",
            "type": "type_rotator",
            "optical_length": 10,
            "mass": 420,
            "tside_thread": "M54",
            "tside_gender": "Female",
            "cside_thread": "M54",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Wanderer_Astro_Rotator_Lite_V2_M68": {
            "brand": "Wanderer Astro",
            "name": "Rotator Lite V2 (M68)",
            "type": "type_rotator",
            "optical_length": 12,
            "mass": 550,
            "tside_thread": "M68",
            "tside_gender": "Female",
            "cside_thread": "M68",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Wanderer_Astro_Rotator_Pro_V2_M92": {
            "brand": "Wanderer Astro",
            "name": "Rotator Pro V2 (M92)",
            "type": "type_rotator",
            "optical_length": 16,
            "mass": 900,
            "tside_thread": "M92",
            "tside_gender": "Female",
            "cside_thread": "M92",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Takahashi_Camera_Rotator_S_M54": {
            "brand": "Takahashi",
            "name": "Camera Rotator S (M54)",
            "type": "type_rotator",
            "optical_length": 10,
            "mass": 120,
            "tside_thread": "M54",
            "tside_gender": "Female",
            "cside_thread": "M54",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Takahashi_Camera_Rotator_M_M72": {
            "brand": "Takahashi",
            "name": "Camera Rotator M (M72)",
            "type": "type_rotator",
            "optical_length": 12,
            "mass": 200,
            "tside_thread": "M72",
            "tside_gender": "Female",
            "cside_thread": "M72",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Takahashi_Camera_Rotator_M82": {
            "brand": "Takahashi",
            "name": "Camera Rotator (M82)",
            "type": "type_rotator",
            "optical_length": 12,
            "mass": 300,
            "tside_thread": "M82",
            "tside_gender": "Female",
            "cside_thread": "M82",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Takahashi_Camera_Rotator_M92": {
            "brand": "Takahashi",
            "name": "Camera Rotator (M92)",
            "type": "type_rotator",
            "optical_length": 14,
            "mass": 350,
            "tside_thread": "M92",
            "tside_gender": "Female",
            "cside_thread": "M92",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Starlight_Instruments_Rotator_M42": {
            "brand": "Starlight Instruments",
            "name": "Rotator (M42)",
            "type": "type_rotator",
            "optical_length": 10,
            "mass": 200,
            "tside_thread": "M42",
            "tside_gender": "Female",
            "cside_thread": "M42",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Starlight_Instruments_Rotator_M48": {
            "brand": "Starlight Instruments",
            "name": "Rotator (M48)",
            "type": "type_rotator",
            "optical_length": 11,
            "mass": 250,
            "tside_thread": "M48",
            "tside_gender": "Female",
            "cside_thread": "M48",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Starlight_Instruments_Rotator_M54": {
            "brand": "Starlight Instruments",
            "name": "Rotator (M54)",
            "type": "type_rotator",
            "optical_length": 12,
            "mass": 300,
            "tside_thread": "M54",
            "tside_gender": "Female",
            "cside_thread": "M54",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Moonlite_Rotator_M42": {
            "brand": "Moonlite",
            "name": "Rotator (M42)",
            "type": "type_rotator",
            "optical_length": 11,
            "mass": 220,
            "tside_thread": "M42",
            "tside_gender": "Female",
            "cside_thread": "M42",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Moonlite_Rotator_M48": {
            "brand": "Moonlite",
            "name": "Rotator (M48)",
            "type": "type_rotator",
            "optical_length": 11,
            "mass": 270,
            "tside_thread": "M48",
            "tside_gender": "Female",
            "cside_thread": "M48",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "ASToptics_Rotator_M42": {
            "brand": "ASToptics",
            "name": "Rotator (M42)",
            "type": "type_rotator",
            "optical_length": 10,
            "mass": 200,
            "tside_thread": "M42",
            "tside_gender": "Female",
            "cside_thread": "M42",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "ASToptics_Rotator_M48": {
            "brand": "ASToptics",
            "name": "Rotator (M48)",
            "type": "type_rotator",
            "optical_length": 11,
            "mass": 250,
            "tside_thread": "M48",
            "tside_gender": "Female",
            "cside_thread": "M48",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "ASToptics_Rotator_M54": {
            "brand": "ASToptics",
            "name": "Rotator (M54)",
            "type": "type_rotator",
            "optical_length": 12,
            "mass": 300,
            "tside_thread": "M54",
            "tside_gender": "Female",
            "cside_thread": "M54",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Wanderer_Astro_Field_Rotator_M42": {
            "brand": "Wanderer Astro",
            "name": "Field Rotator (M42)",
            "type": "type_rotator",
            "optical_length": 10,
            "mass": 250,
            "tside_thread": "M42",
            "tside_gender": "Female",
            "cside_thread": "M42",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Askar_Rotator_M48": {
            "brand": "Askar",
            "name": "Rotator (M48)",
            "type": "type_rotator",
            "optical_length": 11,
            "mass": 280,
            "tside_thread": "M48",
            "tside_gender": "Female",
            "cside_thread": "M48",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Askar_Rotator_M54": {
            "brand": "Askar",
            "name": "Rotator (M54)",
            "type": "type_rotator",
            "optical_length": 12,
            "mass": 310,
            "tside_thread": "M54",
            "tside_gender": "Female",
            "cside_thread": "M54",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Sharpstar_Rotator_M48": {
            "brand": "Sharpstar",
            "name": "Rotator (M48)",
            "type": "type_rotator",
            "optical_length": 11,
            "mass": 270,
            "tside_thread": "M48",
            "tside_gender": "Female",
            "cside_thread": "M48",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Sharpstar_Rotator_M54": {
            "brand": "Sharpstar",
            "name": "Rotator (M54)",
            "type": "type_rotator",
            "optical_length": 12,
            "mass": 300,
            "tside_thread": "M54",
            "tside_gender": "Female",
            "cside_thread": "M54",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Altair_Field_Rotator_M42": {
            "brand": "Altair",
            "name": "Field Rotator (M42)",
            "type": "type_rotator",
            "optical_length": 10,
            "mass": 240,
            "tside_thread": "M42",
            "tside_gender": "Female",
            "cside_thread": "M42",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Altair_Field_Rotator_M48": {
            "brand": "Altair",
            "name": "Field Rotator (M48)",
            "type": "type_rotator",
            "optical_length": 11,
            "mass": 280,
            "tside_thread": "M48",
            "tside_gender": "Female",
            "cside_thread": "M48",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Omegon_Field_Rotator_M42": {
            "brand": "Omegon",
            "name": "Field Rotator (M42)",
            "type": "type_rotator",
            "optical_length": 10,
            "mass": 230,
            "tside_thread": "M42",
            "tside_gender": "Female",
            "cside_thread": "M42",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Omegon_Field_Rotator_M48": {
            "brand": "Omegon",
            "name": "Field Rotator (M48)",
            "type": "type_rotator",
            "optical_length": 11,
            "mass": 270,
            "tside_thread": "M48",
            "tside_gender": "Female",
            "cside_thread": "M48",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Vixen_Rotator_M42": {
            "brand": "Vixen",
            "name": "Rotator (M42)",
            "type": "type_rotator",
            "optical_length": 10,
            "mass": 220,
            "tside_thread": "M42",
            "tside_gender": "Female",
            "cside_thread": "M42",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Vixen_Rotator_M54": {
            "brand": "Vixen",
            "name": "Rotator (M54)",
            "type": "type_rotator",
            "optical_length": 12,
            "mass": 310,
            "tside_thread": "M54",
            "tside_gender": "Female",
            "cside_thread": "M54",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "ZWO_EAF_Rotator_M54": {
            "brand": "ZWO",
            "name": "EAF + Rotator (M54)",
            "type": "type_rotator",
            "optical_length": 12,
            "mass": 280,
            "tside_thread": "M54",
            "tside_gender": "Female",
            "cside_thread": "M54",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "QHY_Camera_Rotator_M42": {
            "brand": "QHY",
            "name": "Camera Rotator (M42)",
            "type": "type_rotator",
            "optical_length": 10,
            "mass": 200,
            "tside_thread": "M42",
            "tside_gender": "Female",
            "cside_thread": "M42",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "QHY_Camera_Rotator_M54": {
            "brand": "QHY",
            "name": "Camera Rotator (M54)",
            "type": "type_rotator",
            "optical_length": 12,
            "mass": 280,
            "tside_thread": "M54",
            "tside_gender": "Female",
            "cside_thread": "M54",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "More_Blue_Camera_Rotator_M56": {
            "brand": "More Blue",
            "name": "Camera Rotator (M56)",
            "type": "type_rotator",
            "optical_length": 10,
            "mass": 180,
            "tside_thread": "M56",
            "tside_gender": "Female",
            "cside_thread": "M56",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "More_Blue_Camera_Rotator_M72": {
            "brand": "More Blue",
            "name": "Camera Rotator (M72)",
            "type": "type_rotator",
            "optical_length": 12,
            "mass": 250,
            "tside_thread": "M72",
            "tside_gender": "Female",
            "cside_thread": "M72",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "PrimaLuce_EAGLE_Rotator_M68": {
            "brand": "PrimaLuce",
            "name": "EAGLE Rotator (M68)",
            "type": "type_rotator",
            "optical_length": 12,
            "mass": 420,
            "tside_thread": "M68",
            "tside_gender": "Female",
            "cside_thread": "M68",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
    }

    @classmethod
    def Pegasus_Falcon_Rotator_M42(cls):
        return cls.from_database(cls._DATABASE["Pegasus_Falcon_Rotator_M42"])

    @classmethod
    def Pegasus_Falcon_Rotator_M48(cls):
        return cls.from_database(cls._DATABASE["Pegasus_Falcon_Rotator_M48"])

    @classmethod
    def Pegasus_Falcon_Rotator_M54(cls):
        return cls.from_database(cls._DATABASE["Pegasus_Falcon_Rotator_M54"])

    @classmethod
    def Pegasus_Falcon_Rotator_M68(cls):
        return cls.from_database(cls._DATABASE["Pegasus_Falcon_Rotator_M68"])

    @classmethod
    def ZWO_EAF_Rotator_M42(cls):
        return cls.from_database(cls._DATABASE["ZWO_EAF_Rotator_M42"])

    @classmethod
    def ARCO_2_Camera_Rotator_M48(cls):
        return cls.from_database(cls._DATABASE["ARCO_2_Camera_Rotator_M48"])

    @classmethod
    def ARCO_2_Camera_Rotator_M54(cls):
        return cls.from_database(cls._DATABASE["ARCO_2_Camera_Rotator_M54"])

    @classmethod
    def ARCO_2_Camera_Rotator_M68(cls):
        return cls.from_database(cls._DATABASE["ARCO_2_Camera_Rotator_M68"])

    @classmethod
    def Player_One_Ares_Rotator_M54(cls):
        return cls.from_database(cls._DATABASE["Player_One_Ares_Rotator_M54"])

    @classmethod
    def Optec_Gemini_Rotator_M68(cls):
        return cls.from_database(cls._DATABASE["Optec_Gemini_Rotator_M68"])

    @classmethod
    def Optec_Gemini_Rotator_M54(cls):
        return cls.from_database(cls._DATABASE["Optec_Gemini_Rotator_M54"])

    @classmethod
    def PrimaLuce_EAGLE_Rotator_M48(cls):
        return cls.from_database(cls._DATABASE["PrimaLuce_EAGLE_Rotator_M48"])

    @classmethod
    def PrimaLuce_EAGLE_Rotator_M54(cls):
        return cls.from_database(cls._DATABASE["PrimaLuce_EAGLE_Rotator_M54"])

    @classmethod
    def Lacerta_Rotator_M42(cls):
        return cls.from_database(cls._DATABASE["Lacerta_Rotator_M42"])

    @classmethod
    def Lacerta_Rotator_M48(cls):
        return cls.from_database(cls._DATABASE["Lacerta_Rotator_M48"])

    @classmethod
    def TS_Optics_TSRot2_M54(cls):
        return cls.from_database(cls._DATABASE["TS_Optics_TSRot2_M54"])

    @classmethod
    def Wanderer_Astro_Field_Rotator_M48(cls):
        return cls.from_database(cls._DATABASE["Wanderer_Astro_Field_Rotator_M48"])

    @classmethod
    def Wanderer_Astro_Field_Rotator_M54(cls):
        return cls.from_database(cls._DATABASE["Wanderer_Astro_Field_Rotator_M54"])

    @classmethod
    def Wanderer_Astro_Rotator_Mini_V2_M54(cls):
        return cls.from_database(cls._DATABASE["Wanderer_Astro_Rotator_Mini_V2_M54"])

    @classmethod
    def Wanderer_Astro_Rotator_Lite_V2_M68(cls):
        return cls.from_database(cls._DATABASE["Wanderer_Astro_Rotator_Lite_V2_M68"])

    @classmethod
    def Wanderer_Astro_Rotator_Pro_V2_M92(cls):
        return cls.from_database(cls._DATABASE["Wanderer_Astro_Rotator_Pro_V2_M92"])

    @classmethod
    def Takahashi_Camera_Rotator_S_M54(cls):
        return cls.from_database(cls._DATABASE["Takahashi_Camera_Rotator_S_M54"])

    @classmethod
    def Takahashi_Camera_Rotator_M_M72(cls):
        return cls.from_database(cls._DATABASE["Takahashi_Camera_Rotator_M_M72"])

    @classmethod
    def Takahashi_Camera_Rotator_M82(cls):
        return cls.from_database(cls._DATABASE["Takahashi_Camera_Rotator_M82"])

    @classmethod
    def Takahashi_Camera_Rotator_M92(cls):
        return cls.from_database(cls._DATABASE["Takahashi_Camera_Rotator_M92"])

    @classmethod
    def Starlight_Instruments_Rotator_M42(cls):
        return cls.from_database(cls._DATABASE["Starlight_Instruments_Rotator_M42"])

    @classmethod
    def Starlight_Instruments_Rotator_M48(cls):
        return cls.from_database(cls._DATABASE["Starlight_Instruments_Rotator_M48"])

    @classmethod
    def Starlight_Instruments_Rotator_M54(cls):
        return cls.from_database(cls._DATABASE["Starlight_Instruments_Rotator_M54"])

    @classmethod
    def Moonlite_Rotator_M42(cls):
        return cls.from_database(cls._DATABASE["Moonlite_Rotator_M42"])

    @classmethod
    def Moonlite_Rotator_M48(cls):
        return cls.from_database(cls._DATABASE["Moonlite_Rotator_M48"])

    @classmethod
    def ASToptics_Rotator_M42(cls):
        return cls.from_database(cls._DATABASE["ASToptics_Rotator_M42"])

    @classmethod
    def ASToptics_Rotator_M48(cls):
        return cls.from_database(cls._DATABASE["ASToptics_Rotator_M48"])

    @classmethod
    def ASToptics_Rotator_M54(cls):
        return cls.from_database(cls._DATABASE["ASToptics_Rotator_M54"])

    @classmethod
    def Wanderer_Astro_Field_Rotator_M42(cls):
        return cls.from_database(cls._DATABASE["Wanderer_Astro_Field_Rotator_M42"])

    @classmethod
    def Askar_Rotator_M48(cls):
        return cls.from_database(cls._DATABASE["Askar_Rotator_M48"])

    @classmethod
    def Askar_Rotator_M54(cls):
        return cls.from_database(cls._DATABASE["Askar_Rotator_M54"])

    @classmethod
    def Sharpstar_Rotator_M48(cls):
        return cls.from_database(cls._DATABASE["Sharpstar_Rotator_M48"])

    @classmethod
    def Sharpstar_Rotator_M54(cls):
        return cls.from_database(cls._DATABASE["Sharpstar_Rotator_M54"])

    @classmethod
    def Altair_Field_Rotator_M42(cls):
        return cls.from_database(cls._DATABASE["Altair_Field_Rotator_M42"])

    @classmethod
    def Altair_Field_Rotator_M48(cls):
        return cls.from_database(cls._DATABASE["Altair_Field_Rotator_M48"])

    @classmethod
    def Omegon_Field_Rotator_M42(cls):
        return cls.from_database(cls._DATABASE["Omegon_Field_Rotator_M42"])

    @classmethod
    def Omegon_Field_Rotator_M48(cls):
        return cls.from_database(cls._DATABASE["Omegon_Field_Rotator_M48"])

    @classmethod
    def Vixen_Rotator_M42(cls):
        return cls.from_database(cls._DATABASE["Vixen_Rotator_M42"])

    @classmethod
    def Vixen_Rotator_M54(cls):
        return cls.from_database(cls._DATABASE["Vixen_Rotator_M54"])

    @classmethod
    def ZWO_EAF_Rotator_M54(cls):
        return cls.from_database(cls._DATABASE["ZWO_EAF_Rotator_M54"])

    @classmethod
    def QHY_Camera_Rotator_M42(cls):
        return cls.from_database(cls._DATABASE["QHY_Camera_Rotator_M42"])

    @classmethod
    def QHY_Camera_Rotator_M54(cls):
        return cls.from_database(cls._DATABASE["QHY_Camera_Rotator_M54"])

    @classmethod
    def More_Blue_Camera_Rotator_M56(cls):
        return cls.from_database(cls._DATABASE["More_Blue_Camera_Rotator_M56"])

    @classmethod
    def More_Blue_Camera_Rotator_M72(cls):
        return cls.from_database(cls._DATABASE["More_Blue_Camera_Rotator_M72"])

    @classmethod
    def PrimaLuce_EAGLE_Rotator_M68(cls):
        return cls.from_database(cls._DATABASE["PrimaLuce_EAGLE_Rotator_M68"])
