from ..base import Telescope

class SharpstarTelescope(Telescope):
    _DATABASE = {
        "Sharpstar_61EDPH_II": {
            "brand": "Sharpstar",
            "name": "61EDPH II",
            "type": "type_refractor",
            "optical_length": 0,
            "mass": 1500,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "M48",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
            "aperture_mm": 61,
            "focal_length_mm": 335,
            "central_obstruction_mm": 0,
        },
        "Sharpstar_61EDPH_III": {
            "brand": "Sharpstar",
            "name": "61EDPH III",
            "type": "type_refractor",
            "optical_length": 0,
            "mass": 1480,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "M48",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
            "aperture_mm": 61,
            "focal_length_mm": 360,
            "central_obstruction_mm": 0,
        },
        "Sharpstar_76EDPH_II": {
            "brand": "Sharpstar",
            "name": "76EDPH II",
            "type": "type_refractor",
            "optical_length": 0,
            "mass": 2300,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "M48",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
            "aperture_mm": 76,
            "focal_length_mm": 418,
            "central_obstruction_mm": 0,
        },
        "Sharpstar_94EDPH_II": {
            "brand": "Sharpstar",
            "name": "94EDPH II",
            "type": "type_refractor",
            "optical_length": 0,
            "mass": 3300,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "M54",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
            "aperture_mm": 94,
            "focal_length_mm": 517,
            "central_obstruction_mm": 0,
        },
        "Sharpstar_140PH": {
            "brand": "Sharpstar",
            "name": "140PH",
            "type": "type_refractor",
            "optical_length": 0,
            "mass": 10100,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "M68",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
            "aperture_mm": 140,
            "focal_length_mm": 910,
            "central_obstruction_mm": 0,
        },
        "Sharpstar_13028HNT": {
            "brand": "Sharpstar",
            "name": "13028HNT",
            "type": "newtonian_reflector",
            "optical_length": 0,
            "mass": 3200,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "M48",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
            "aperture_mm": 130,
            "focal_length_mm": 364,
            "central_obstruction_mm": 65,
        },
        "Sharpstar_15028HNT": {
            "brand": "Sharpstar",
            "name": "15028HNT",
            "type": "newtonian_reflector",
            "optical_length": 0,
            "mass": 4450,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "M68",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
            "aperture_mm": 150,
            "focal_length_mm": 420,
            "central_obstruction_mm": 70,
        },
        "Sharpstar_20032HNT": {
            "brand": "Sharpstar",
            "name": "20032HNT",
            "type": "newtonian_reflector",
            "optical_length": 0,
            "mass": 8000,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "M68",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
            "aperture_mm": 200,
            "focal_length_mm": 640,
            "central_obstruction_mm": 90,
        },
    }

    @classmethod
    def Sharpstar_61EDPH_II(cls):
        return cls.from_database(cls._DATABASE['Sharpstar_61EDPH_II'])

    @classmethod
    def Sharpstar_61EDPH_III(cls):
        return cls.from_database(cls._DATABASE['Sharpstar_61EDPH_III'])

    @classmethod
    def Sharpstar_76EDPH_II(cls):
        return cls.from_database(cls._DATABASE['Sharpstar_76EDPH_II'])

    @classmethod
    def Sharpstar_94EDPH_II(cls):
        return cls.from_database(cls._DATABASE['Sharpstar_94EDPH_II'])

    @classmethod
    def Sharpstar_140PH(cls):
        return cls.from_database(cls._DATABASE['Sharpstar_140PH'])

    @classmethod
    def Sharpstar_13028HNT(cls):
        return cls.from_database(cls._DATABASE['Sharpstar_13028HNT'])

    @classmethod
    def Sharpstar_15028HNT(cls):
        return cls.from_database(cls._DATABASE['Sharpstar_15028HNT'])

    @classmethod
    def Sharpstar_20032HNT(cls):
        return cls.from_database(cls._DATABASE['Sharpstar_20032HNT'])
