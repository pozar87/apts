from ..base import Telescope

class BresserTelescope(Telescope):
    _DATABASE = {
        "Bresser_Messier_AR_102xs": {
            "brand": "Bresser",
            "name": "Messier AR-102xs",
            "type": "type_refractor",
            "optical_length": 0,
            "mass": 2800,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "M48",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
            "aperture_mm": 102,
            "focal_length_mm": 460,
            "central_obstruction_mm": 0,
        },
        "Bresser_Messier_AR_127L": {
            "brand": "Bresser",
            "name": "Messier AR-127L",
            "type": "type_refractor",
            "optical_length": 0,
            "mass": 7900,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "M48",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
            "aperture_mm": 127,
            "focal_length_mm": 1200,
            "central_obstruction_mm": 0,
        },
        "Bresser_Messier_AR_152L": {
            "brand": "Bresser",
            "name": "Messier AR-152L",
            "type": "type_refractor",
            "optical_length": 0,
            "mass": 11100,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "M48",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
            "aperture_mm": 152,
            "focal_length_mm": 1200,
            "central_obstruction_mm": 0,
        },
        "Bresser_Messier_AR_152S": {
            "brand": "Bresser",
            "name": "Messier AR-152S",
            "type": "type_refractor",
            "optical_length": 0,
            "mass": 10600,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "M48",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
            "aperture_mm": 152,
            "focal_length_mm": 760,
            "central_obstruction_mm": 0,
        },
        "Bresser_Messier_MC_127": {
            "brand": "Bresser",
            "name": "Messier MC-127",
            "type": "maksutov_cassegrain",
            "optical_length": 0,
            "mass": 3400,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "1.25\"",
            "cside_gender": "Female",
            "reversible": False,
            "bf_role": "",
            "aperture_mm": 127,
            "focal_length_mm": 1900,
            "central_obstruction_mm": 35,
        },
        "Bresser_Messier_MC_152": {
            "brand": "Bresser",
            "name": "Messier MC-152",
            "type": "maksutov_cassegrain",
            "optical_length": 0,
            "mass": 6500,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "SC (Schmidt-Cassegrain)",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
            "aperture_mm": 152,
            "focal_length_mm": 1900,
            "central_obstruction_mm": 45,
        },
        "Bresser_Messier_NT_150L_6": {
            "brand": "Bresser",
            "name": "Messier NT-150L (6\")",
            "type": "newtonian_reflector",
            "optical_length": 0,
            "mass": 6500,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "2\"",
            "cside_gender": "Female",
            "reversible": False,
            "bf_role": "",
            "aperture_mm": 150,
            "focal_length_mm": 1200,
            "central_obstruction_mm": 45,
        },
        "Bresser_Messier_NT_203_8": {
            "brand": "Bresser",
            "name": "Messier NT-203 (8\")",
            "type": "newtonian_reflector",
            "optical_length": 0,
            "mass": 11500,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "2\"",
            "cside_gender": "Female",
            "reversible": False,
            "bf_role": "",
            "aperture_mm": 203,
            "focal_length_mm": 1000,
            "central_obstruction_mm": 60,
        },
        "Bresser_Messier_NT_203s_8": {
            "brand": "Bresser",
            "name": "Messier NT-203s (8\")",
            "type": "newtonian_reflector",
            "optical_length": 0,
            "mass": 8700,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "2.5\"",
            "cside_gender": "Female",
            "reversible": False,
            "bf_role": "",
            "aperture_mm": 203,
            "focal_length_mm": 800,
            "central_obstruction_mm": 85,
        },
        "Bresser_Messier_NT_254_10": {
            "brand": "Bresser",
            "name": "Messier NT-254 (10\")",
            "type": "newtonian_reflector",
            "optical_length": 0,
            "mass": 16400,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "2.5\"",
            "cside_gender": "Female",
            "reversible": False,
            "bf_role": "",
            "aperture_mm": 254,
            "focal_length_mm": 1270,
            "central_obstruction_mm": 74,
        },
    }

    @classmethod
    def Bresser_Messier_AR_102xs(cls):
        return cls.from_database(cls._DATABASE['Bresser_Messier_AR_102xs'])

    @classmethod
    def Bresser_Messier_AR_127L(cls):
        return cls.from_database(cls._DATABASE['Bresser_Messier_AR_127L'])

    @classmethod
    def Bresser_Messier_AR_152L(cls):
        return cls.from_database(cls._DATABASE['Bresser_Messier_AR_152L'])

    @classmethod
    def Bresser_Messier_AR_152S(cls):
        return cls.from_database(cls._DATABASE['Bresser_Messier_AR_152S'])

    @classmethod
    def Bresser_Messier_MC_127(cls):
        return cls.from_database(cls._DATABASE['Bresser_Messier_MC_127'])

    @classmethod
    def Bresser_Messier_MC_152(cls):
        return cls.from_database(cls._DATABASE['Bresser_Messier_MC_152'])

    @classmethod
    def Bresser_Messier_NT_150L_6(cls):
        return cls.from_database(cls._DATABASE['Bresser_Messier_NT_150L_6'])

    @classmethod
    def Bresser_Messier_NT_203_8(cls):
        return cls.from_database(cls._DATABASE['Bresser_Messier_NT_203_8'])

    @classmethod
    def Bresser_Messier_NT_203s_8(cls):
        return cls.from_database(cls._DATABASE['Bresser_Messier_NT_203s_8'])

    @classmethod
    def Bresser_Messier_NT_254_10(cls):
        return cls.from_database(cls._DATABASE['Bresser_Messier_NT_254_10'])
