from ..base import Rotator


class PegasusRotator(Rotator):
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
    }

    @classmethod
    def Pegasus_Falcon_Rotator_M42(cls):
        return cls.from_database(cls._DATABASE['Pegasus_Falcon_Rotator_M42'])

    @classmethod
    def Pegasus_Falcon_Rotator_M48(cls):
        return cls.from_database(cls._DATABASE['Pegasus_Falcon_Rotator_M48'])

    @classmethod
    def Pegasus_Falcon_Rotator_M54(cls):
        return cls.from_database(cls._DATABASE['Pegasus_Falcon_Rotator_M54'])

    @classmethod
    def Pegasus_Falcon_Rotator_M68(cls):
        return cls.from_database(cls._DATABASE['Pegasus_Falcon_Rotator_M68'])
