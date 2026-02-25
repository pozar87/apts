from ....utils import Gender
from ..base import Camera

class NikonCamera(Camera):
    _DATABASE = {'Nikon_D810A': {'brand': 'Nikon', 'name': 'D810A', 'type': 'type_dslr', 'optical_length': 46.5, 'mass': 980, 'tside_thread': 'Nikon F', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'Nikon_D750': {'brand': 'Nikon', 'name': 'D750', 'type': 'type_dslr', 'optical_length': 46.5, 'mass': 840, 'tside_thread': 'Nikon F', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'Nikon_D5600': {'brand': 'Nikon', 'name': 'D5600', 'type': 'type_dslr', 'optical_length': 46.5, 'mass': 465, 'tside_thread': 'Nikon F', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'Nikon_D7500': {'brand': 'Nikon', 'name': 'D7500', 'type': 'type_dslr', 'optical_length': 46.5, 'mass': 640, 'tside_thread': 'Nikon F', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'Nikon_D3400': {'brand': 'Nikon', 'name': 'D3400', 'type': 'type_dslr', 'optical_length': 46.5, 'mass': 395, 'tside_thread': 'Nikon F', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'Nikon_D5300': {'brand': 'Nikon', 'name': 'D5300', 'type': 'type_dslr', 'optical_length': 46.5, 'mass': 480, 'tside_thread': 'Nikon F', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'Nikon_D7200': {'brand': 'Nikon', 'name': 'D7200', 'type': 'type_dslr', 'optical_length': 46.5, 'mass': 675, 'tside_thread': 'Nikon F', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'Nikon_D810': {'brand': 'Nikon', 'name': 'D810', 'type': 'type_dslr', 'optical_length': 46.5, 'mass': 880, 'tside_thread': 'Nikon F', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'Nikon_D850': {'brand': 'Nikon', 'name': 'D850', 'type': 'type_dslr', 'optical_length': 46.5, 'mass': 1005, 'tside_thread': 'Nikon F', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'Nikon_D610': {'brand': 'Nikon', 'name': 'D610', 'type': 'type_dslr', 'optical_length': 46.5, 'mass': 760, 'tside_thread': 'Nikon F', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'Nikon_D5500': {'brand': 'Nikon', 'name': 'D5500', 'type': 'type_dslr', 'optical_length': 46.5, 'mass': 470, 'tside_thread': 'Nikon F', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'Nikon_D3300': {'brand': 'Nikon', 'name': 'D3300', 'type': 'type_dslr', 'optical_length': 46.5, 'mass': 410, 'tside_thread': 'Nikon F', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'Nikon_D500': {'brand': 'Nikon', 'name': 'D500', 'type': 'type_dslr', 'optical_length': 46.5, 'mass': 860, 'tside_thread': 'Nikon F', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'Nikon_Z5': {'brand': 'Nikon', 'name': 'Z5', 'type': 'type_dslr', 'optical_length': 16, 'mass': 675, 'tside_thread': 'Nikon Z', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'Nikon_Z6': {'brand': 'Nikon', 'name': 'Z6', 'type': 'type_dslr', 'optical_length': 16, 'mass': 675, 'tside_thread': 'Nikon Z', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'Nikon_Z6_II': {'brand': 'Nikon', 'name': 'Z6 II', 'type': 'type_dslr', 'optical_length': 16, 'mass': 705, 'tside_thread': 'Nikon Z', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'Nikon_Z6_III': {'brand': 'Nikon', 'name': 'Z6 III', 'type': 'type_dslr', 'optical_length': 16, 'mass': 760, 'tside_thread': 'Nikon Z', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'Nikon_Z7': {'brand': 'Nikon', 'name': 'Z7', 'type': 'type_dslr', 'optical_length': 16, 'mass': 675, 'tside_thread': 'Nikon Z', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'Nikon_Z7_II': {'brand': 'Nikon', 'name': 'Z7 II', 'type': 'type_dslr', 'optical_length': 16, 'mass': 705, 'tside_thread': 'Nikon Z', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'Nikon_Z8': {'brand': 'Nikon', 'name': 'Z8', 'type': 'type_dslr', 'optical_length': 16, 'mass': 910, 'tside_thread': 'Nikon Z', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'Nikon_Z9': {'brand': 'Nikon', 'name': 'Z9', 'type': 'type_dslr', 'optical_length': 16, 'mass': 1340, 'tside_thread': 'Nikon Z', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'Nikon_Z30': {'brand': 'Nikon', 'name': 'Z30', 'type': 'type_dslr', 'optical_length': 16, 'mass': 405, 'tside_thread': 'Nikon Z', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'Nikon_Z50': {'brand': 'Nikon', 'name': 'Z50', 'type': 'type_dslr', 'optical_length': 16, 'mass': 450, 'tside_thread': 'Nikon Z', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'Nikon_Zf': {'brand': 'Nikon', 'name': 'Zf', 'type': 'type_dslr', 'optical_length': 16, 'mass': 710, 'tside_thread': 'Nikon Z', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'Nikon_Zfc': {'brand': 'Nikon', 'name': 'Zfc', 'type': 'type_dslr', 'optical_length': 16, 'mass': 445, 'tside_thread': 'Nikon Z', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'Nikon_D780': {'brand': 'Nikon', 'name': 'D780', 'type': 'type_dslr', 'optical_length': 46.5, 'mass': 840, 'tside_thread': 'Nikon F', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'Nikon_D7000': {'brand': 'Nikon', 'name': 'D7000', 'type': 'type_dslr', 'optical_length': 46.5, 'mass': 690, 'tside_thread': 'Nikon F', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'Nikon_D5100': {'brand': 'Nikon', 'name': 'D5100', 'type': 'type_dslr', 'optical_length': 46.5, 'mass': 510, 'tside_thread': 'Nikon F', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'Nikon_D3500': {'brand': 'Nikon', 'name': 'D3500', 'type': 'type_dslr', 'optical_length': 46.5, 'mass': 415, 'tside_thread': 'Nikon F', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'Nikon_D40': {'brand': 'Nikon', 'name': 'D40', 'type': 'type_dslr', 'optical_length': 46.5, 'mass': 475, 'tside_thread': 'Nikon F', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'Nikon_D60': {'brand': 'Nikon', 'name': 'D60', 'type': 'type_dslr', 'optical_length': 46.5, 'mass': 580, 'tside_thread': 'Nikon F', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'Nikon_D70': {'brand': 'Nikon', 'name': 'D70', 'type': 'type_dslr', 'optical_length': 46.5, 'mass': 600, 'tside_thread': 'Nikon F', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'Nikon_D80': {'brand': 'Nikon', 'name': 'D80', 'type': 'type_dslr', 'optical_length': 46.5, 'mass': 625, 'tside_thread': 'Nikon F', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'Nikon_D90': {'brand': 'Nikon', 'name': 'D90', 'type': 'type_dslr', 'optical_length': 46.5, 'mass': 620, 'tside_thread': 'Nikon F', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'Nikon_D200': {'brand': 'Nikon', 'name': 'D200', 'type': 'type_dslr', 'optical_length': 46.5, 'mass': 830, 'tside_thread': 'Nikon F', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'Nikon_D300': {'brand': 'Nikon', 'name': 'D300', 'type': 'type_dslr', 'optical_length': 46.5, 'mass': 825, 'tside_thread': 'Nikon F', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'Nikon_D7100': {'brand': 'Nikon', 'name': 'D7100', 'type': 'type_dslr', 'optical_length': 46.5, 'mass': 675, 'tside_thread': 'Nikon F', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'Nikon_D5000': {'brand': 'Nikon', 'name': 'D5000', 'type': 'type_dslr', 'optical_length': 46.5, 'mass': 560, 'tside_thread': 'Nikon F', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'Nikon_D3200': {'brand': 'Nikon', 'name': 'D3200', 'type': 'type_dslr', 'optical_length': 46.5, 'mass': 455, 'tside_thread': 'Nikon F', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'Nikon_D5200': {'brand': 'Nikon', 'name': 'D5200', 'type': 'type_dslr', 'optical_length': 46.5, 'mass': 505, 'tside_thread': 'Nikon F', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'Nikon_D600': {'brand': 'Nikon', 'name': 'D600', 'type': 'type_dslr', 'optical_length': 46.5, 'mass': 760, 'tside_thread': 'Nikon F', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'Nikon_D4': {'brand': 'Nikon', 'name': 'D4', 'type': 'type_dslr', 'optical_length': 46.5, 'mass': 1340, 'tside_thread': 'Nikon F', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'Nikon_D4S': {'brand': 'Nikon', 'name': 'D4S', 'type': 'type_dslr', 'optical_length': 46.5, 'mass': 1350, 'tside_thread': 'Nikon F', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'Nikon_D5': {'brand': 'Nikon', 'name': 'D5', 'type': 'type_dslr', 'optical_length': 46.5, 'mass': 1405, 'tside_thread': 'Nikon F', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'Nikon_D70s': {'brand': 'Nikon', 'name': 'D70s', 'type': 'type_dslr', 'optical_length': 46.5, 'mass': 610, 'tside_thread': 'Nikon F', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'Nikon_D50': {'brand': 'Nikon', 'name': 'D50', 'type': 'type_dslr', 'optical_length': 46.5, 'mass': 540, 'tside_thread': 'Nikon F', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'Nikon_D3100': {'brand': 'Nikon', 'name': 'D3100', 'type': 'type_dslr', 'optical_length': 46.5, 'mass': 455, 'tside_thread': 'Nikon F', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'Nikon_D3000': {'brand': 'Nikon', 'name': 'D3000', 'type': 'type_dslr', 'optical_length': 46.5, 'mass': 485, 'tside_thread': 'Nikon F', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'Nikon_Df': {'brand': 'Nikon', 'name': 'Df', 'type': 'type_dslr', 'optical_length': 46.5, 'mass': 765, 'tside_thread': 'Nikon F', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}}

    @classmethod
    def Nikon_D850(cls):
        """
        Factory method for Nikon D850 camera.
        Sensor: Full Frame
        """
        entry = cls._DATABASE['Nikon_D850']
        from ....utils import Utils
        vendor = f"{entry['brand']} {entry['name']}"
        ol = entry.get('optical_length', 0)
        mass = entry.get('mass', 0)
        tt = Utils.map_conn(entry.get('tside_thread'))
        tg = Utils.map_gender(entry.get('tside_gender'))
        return cls(35.9, 23.9, 8256, 5504, vendor=vendor, connection_type=tt, connection_gender=tg or Gender.FEMALE, pixel_size=4.35, read_noise=1.1, full_well=48000, quantum_efficiency=54, backfocus=ol, mass=mass, optical_length=ol)

    @classmethod
    def Nikon_D810A(cls):
        return cls.from_database(cls._DATABASE['Nikon_D810A'])

    @classmethod
    def Nikon_D750(cls):
        return cls.from_database(cls._DATABASE['Nikon_D750'])

    @classmethod
    def Nikon_D5600(cls):
        return cls.from_database(cls._DATABASE['Nikon_D5600'])

    @classmethod
    def Nikon_D7500(cls):
        return cls.from_database(cls._DATABASE['Nikon_D7500'])

    @classmethod
    def Nikon_D3400(cls):
        return cls.from_database(cls._DATABASE['Nikon_D3400'])

    @classmethod
    def Nikon_D5300(cls):
        return cls.from_database(cls._DATABASE['Nikon_D5300'])

    @classmethod
    def Nikon_D7200(cls):
        return cls.from_database(cls._DATABASE['Nikon_D7200'])

    @classmethod
    def Nikon_D810(cls):
        return cls.from_database(cls._DATABASE['Nikon_D810'])

    @classmethod
    def Nikon_D610(cls):
        return cls.from_database(cls._DATABASE['Nikon_D610'])

    @classmethod
    def Nikon_D5500(cls):
        return cls.from_database(cls._DATABASE['Nikon_D5500'])

    @classmethod
    def Nikon_D3300(cls):
        return cls.from_database(cls._DATABASE['Nikon_D3300'])

    @classmethod
    def Nikon_D500(cls):
        return cls.from_database(cls._DATABASE['Nikon_D500'])

    @classmethod
    def Nikon_Z5(cls):
        return cls.from_database(cls._DATABASE['Nikon_Z5'])

    @classmethod
    def Nikon_Z6(cls):
        return cls.from_database(cls._DATABASE['Nikon_Z6'])

    @classmethod
    def Nikon_Z6_II(cls):
        return cls.from_database(cls._DATABASE['Nikon_Z6_II'])

    @classmethod
    def Nikon_Z6_III(cls):
        return cls.from_database(cls._DATABASE['Nikon_Z6_III'])

    @classmethod
    def Nikon_Z7(cls):
        return cls.from_database(cls._DATABASE['Nikon_Z7'])

    @classmethod
    def Nikon_Z7_II(cls):
        return cls.from_database(cls._DATABASE['Nikon_Z7_II'])

    @classmethod
    def Nikon_Z8(cls):
        return cls.from_database(cls._DATABASE['Nikon_Z8'])

    @classmethod
    def Nikon_Z9(cls):
        return cls.from_database(cls._DATABASE['Nikon_Z9'])

    @classmethod
    def Nikon_Z30(cls):
        return cls.from_database(cls._DATABASE['Nikon_Z30'])

    @classmethod
    def Nikon_Z50(cls):
        return cls.from_database(cls._DATABASE['Nikon_Z50'])

    @classmethod
    def Nikon_Zf(cls):
        return cls.from_database(cls._DATABASE['Nikon_Zf'])

    @classmethod
    def Nikon_Zfc(cls):
        return cls.from_database(cls._DATABASE['Nikon_Zfc'])

    @classmethod
    def Nikon_D780(cls):
        return cls.from_database(cls._DATABASE['Nikon_D780'])

    @classmethod
    def Nikon_D7000(cls):
        return cls.from_database(cls._DATABASE['Nikon_D7000'])

    @classmethod
    def Nikon_D5100(cls):
        return cls.from_database(cls._DATABASE['Nikon_D5100'])

    @classmethod
    def Nikon_D3500(cls):
        return cls.from_database(cls._DATABASE['Nikon_D3500'])

    @classmethod
    def Nikon_D40(cls):
        return cls.from_database(cls._DATABASE['Nikon_D40'])

    @classmethod
    def Nikon_D60(cls):
        return cls.from_database(cls._DATABASE['Nikon_D60'])

    @classmethod
    def Nikon_D70(cls):
        return cls.from_database(cls._DATABASE['Nikon_D70'])

    @classmethod
    def Nikon_D80(cls):
        return cls.from_database(cls._DATABASE['Nikon_D80'])

    @classmethod
    def Nikon_D90(cls):
        return cls.from_database(cls._DATABASE['Nikon_D90'])

    @classmethod
    def Nikon_D200(cls):
        return cls.from_database(cls._DATABASE['Nikon_D200'])

    @classmethod
    def Nikon_D300(cls):
        return cls.from_database(cls._DATABASE['Nikon_D300'])

    @classmethod
    def Nikon_D7100(cls):
        return cls.from_database(cls._DATABASE['Nikon_D7100'])

    @classmethod
    def Nikon_D5000(cls):
        return cls.from_database(cls._DATABASE['Nikon_D5000'])

    @classmethod
    def Nikon_D3200(cls):
        return cls.from_database(cls._DATABASE['Nikon_D3200'])

    @classmethod
    def Nikon_D5200(cls):
        return cls.from_database(cls._DATABASE['Nikon_D5200'])

    @classmethod
    def Nikon_D600(cls):
        return cls.from_database(cls._DATABASE['Nikon_D600'])

    @classmethod
    def Nikon_D4(cls):
        return cls.from_database(cls._DATABASE['Nikon_D4'])

    @classmethod
    def Nikon_D4S(cls):
        return cls.from_database(cls._DATABASE['Nikon_D4S'])

    @classmethod
    def Nikon_D5(cls):
        return cls.from_database(cls._DATABASE['Nikon_D5'])

    @classmethod
    def Nikon_D70s(cls):
        return cls.from_database(cls._DATABASE['Nikon_D70s'])

    @classmethod
    def Nikon_D50(cls):
        return cls.from_database(cls._DATABASE['Nikon_D50'])

    @classmethod
    def Nikon_D3100(cls):
        return cls.from_database(cls._DATABASE['Nikon_D3100'])

    @classmethod
    def Nikon_D3000(cls):
        return cls.from_database(cls._DATABASE['Nikon_D3000'])

    @classmethod
    def Nikon_Df(cls):
        return cls.from_database(cls._DATABASE['Nikon_Df'])