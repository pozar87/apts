from ..base import Diagonal

class AstroPhysicsDiagonal(Diagonal):
    _DATABASE = {
        "Astro_Physics_MaxBright_Diagonal_2": {
            "brand": "Astro-Physics",
            "name": 'MaxBright Diagonal (2")',
            "type": "type_diagonal",
            "optical_length": 0,
            "mass": 700,
            "tside_thread": '2"',
            "tside_gender": "Male",
            "cside_thread": '2"',
            "cside_gender": "Female",
            "reversible": False,
            "bf_role": "",
        },
    }

    @classmethod
    def Astro_Physics_MaxBright_Diagonal_2(cls):
        return cls.from_database(cls._DATABASE["Astro_Physics_MaxBright_Diagonal_2"])
