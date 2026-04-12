from ..base import Focuser


class JMIFocuser(Focuser):
    _DATABASE = {
        "JMI_EV_1C_Focuser": {'brand': 'JMI', 'name': 'EV-1C Focuser', 'type': 'type_focuser', 'optical_length': 0, 'mass': 200, 'tside_thread': '', 'tside_gender': '', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''},
        "JMI_EV_2C_Focuser": {'brand': 'JMI', 'name': 'EV-2C Focuser', 'type': 'type_focuser', 'optical_length': 0, 'mass': 250, 'tside_thread': '', 'tside_gender': '', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''},
        "JMI_NGF_DX1_Focuser": {'brand': 'JMI', 'name': 'NGF-DX1 Focuser', 'type': 'type_focuser', 'optical_length': 0, 'mass': 600, 'tside_thread': '', 'tside_gender': '', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''},
    }

    @classmethod
    def JMI_EV_1C_Focuser(cls):
        return cls.from_database(cls._DATABASE["JMI_EV_1C_Focuser"])

    @classmethod
    def JMI_EV_2C_Focuser(cls):
        return cls.from_database(cls._DATABASE["JMI_EV_2C_Focuser"])

    @classmethod
    def JMI_NGF_DX1_Focuser(cls):
        return cls.from_database(cls._DATABASE["JMI_NGF_DX1_Focuser"])
