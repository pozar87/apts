from ..base import Telescope

class BresserTelescope(Telescope):
    _DATABASE = {'Bresser_Messier_AR_102xs': {'brand': 'Bresser', 'name': 'Messier AR-102xs', 'type': 'type_refractor', 'optical_length': 0, 'mass': 2800, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Bresser_Messier_AR_127L': {'brand': 'Bresser', 'name': 'Messier AR-127L', 'type': 'type_refractor', 'optical_length': 0, 'mass': 5000, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Bresser_Messier_AR_152L': {'brand': 'Bresser', 'name': 'Messier AR-152L', 'type': 'type_refractor', 'optical_length': 0, 'mass': 7000, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Bresser_Messier_MC_127': {'brand': 'Bresser', 'name': 'Messier MC-127', 'type': 'type_telescope', 'optical_length': 0, 'mass': 3200, 'tside_thread': '', 'tside_gender': '', 'cside_thread': '1.25"', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Bresser_Messier_MC_152': {'brand': 'Bresser', 'name': 'Messier MC-152', 'type': 'type_telescope', 'optical_length': 0, 'mass': 5500, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'SC (Schmidt-Cassegrain)', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Bresser_Messier_NT_150L_6': {'brand': 'Bresser', 'name': 'Messier NT-150L (6")', 'type': 'type_telescope', 'optical_length': 0, 'mass': 5000, 'tside_thread': '', 'tside_gender': '', 'cside_thread': '2"', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Bresser_Messier_NT_203_8': {'brand': 'Bresser', 'name': 'Messier NT-203 (8")', 'type': 'type_telescope', 'optical_length': 0, 'mass': 8000, 'tside_thread': '', 'tside_gender': '', 'cside_thread': '2"', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Bresser_Messier_NT_254_10': {'brand': 'Bresser', 'name': 'Messier NT-254 (10")', 'type': 'type_telescope', 'optical_length': 0, 'mass': 12000, 'tside_thread': '', 'tside_gender': '', 'cside_thread': '2"', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Bresser_Messier_AR_80': {'brand': 'Bresser', 'name': 'Messier AR-80', 'type': 'type_refractor', 'optical_length': 0, 'mass': 2000, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Bresser_Messier_AR_90': {'brand': 'Bresser', 'name': 'Messier AR-90', 'type': 'type_refractor', 'optical_length': 0, 'mass': 2300, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Bresser_Messier_MC_100': {'brand': 'Bresser', 'name': 'Messier MC-100', 'type': 'type_telescope', 'optical_length': 0, 'mass': 3000, 'tside_thread': '', 'tside_gender': '', 'cside_thread': '1.25"', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Bresser_Messier_NT_130': {'brand': 'Bresser', 'name': 'Messier NT-130', 'type': 'type_telescope', 'optical_length': 0, 'mass': 4200, 'tside_thread': '', 'tside_gender': '', 'cside_thread': '2"', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Bresser_Arcturus_60_700_AZ': {'brand': 'Bresser', 'name': 'Arcturus 60/700 AZ', 'type': 'type_telescope', 'optical_length': 0, 'mass': 1200, 'tside_thread': '', 'tside_gender': '', 'cside_thread': '1.25"', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Bresser_Pollux_150_1400': {'brand': 'Bresser', 'name': 'Pollux 150/1400', 'type': 'type_telescope', 'optical_length': 0, 'mass': 5500, 'tside_thread': '', 'tside_gender': '', 'cside_thread': '2"', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Bresser_Bresser_Spica_130_1000': {'brand': 'Bresser', 'name': 'Bresser Spica 130/1000', 'type': 'type_telescope', 'optical_length': 0, 'mass': 4500, 'tside_thread': '', 'tside_gender': '', 'cside_thread': '2"', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Bresser_Messier_AR_102L': {'brand': 'Bresser', 'name': 'Messier AR-102L', 'type': 'type_refractor', 'optical_length': 0, 'mass': 3800, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Bresser_Messier_AR_127S': {'brand': 'Bresser', 'name': 'Messier AR-127S', 'type': 'type_refractor', 'optical_length': 0, 'mass': 4500, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Bresser_Messier_NT_150S_6_f_5': {'brand': 'Bresser', 'name': 'Messier NT-150S (6" f/5)', 'type': 'type_telescope', 'optical_length': 0, 'mass': 5200, 'tside_thread': '', 'tside_gender': '', 'cside_thread': '2"', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Bresser_Messier_Dobson_8': {'brand': 'Bresser', 'name': 'Messier Dobson 8"', 'type': 'type_telescope', 'optical_length': 0, 'mass': 7000, 'tside_thread': '', 'tside_gender': '', 'cside_thread': '2"', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Bresser_Messier_Dobson_10': {'brand': 'Bresser', 'name': 'Messier Dobson 10"', 'type': 'type_telescope', 'optical_length': 0, 'mass': 10000, 'tside_thread': '', 'tside_gender': '', 'cside_thread': '2"', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Bresser_Messier_Dobson_12': {'brand': 'Bresser', 'name': 'Messier Dobson 12"', 'type': 'type_telescope', 'optical_length': 0, 'mass': 14000, 'tside_thread': '', 'tside_gender': '', 'cside_thread': '2"', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Bresser_Pollux_150_1400_EQ3': {'brand': 'Bresser', 'name': 'Pollux 150/1400 EQ3', 'type': 'type_telescope', 'optical_length': 0, 'mass': 4000, 'tside_thread': '', 'tside_gender': '', 'cside_thread': '2"', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Bresser_Lyra_70_900_EQ': {'brand': 'Bresser', 'name': 'Lyra 70/900 EQ', 'type': 'type_refractor', 'optical_length': 0, 'mass': 1200, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Bresser_Jupiter_70_700_AZ': {'brand': 'Bresser', 'name': 'Jupiter 70/700 AZ', 'type': 'type_refractor', 'optical_length': 0, 'mass': 1000, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Bresser_Taurus_90_900_NG': {'brand': 'Bresser', 'name': 'Taurus 90/900 NG', 'type': 'type_refractor', 'optical_length': 0, 'mass': 2200, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Bresser_Messier_Dobson_6_Truss': {'brand': 'Bresser', 'name': 'Messier Dobson 6" Truss', 'type': 'type_telescope', 'optical_length': 0, 'mass': 4500, 'tside_thread': '', 'tside_gender': '', 'cside_thread': '2"', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Bresser_Messier_Dobson_8_Truss': {'brand': 'Bresser', 'name': 'Messier Dobson 8" Truss', 'type': 'type_telescope', 'optical_length': 0, 'mass': 6800, 'tside_thread': '', 'tside_gender': '', 'cside_thread': '2"', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Bresser_Messier_Dobson_10_Truss': {'brand': 'Bresser', 'name': 'Messier Dobson 10" Truss', 'type': 'type_telescope', 'optical_length': 0, 'mass': 9200, 'tside_thread': '', 'tside_gender': '', 'cside_thread': '2"', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Bresser_Messier_Dobson_12_Truss': {'brand': 'Bresser', 'name': 'Messier Dobson 12" Truss', 'type': 'type_telescope', 'optical_length': 0, 'mass': 12500, 'tside_thread': '', 'tside_gender': '', 'cside_thread': '2"', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Bresser_Messier_Dobson_14_Truss': {'brand': 'Bresser', 'name': 'Messier Dobson 14" Truss', 'type': 'type_telescope', 'optical_length': 0, 'mass': 17000, 'tside_thread': '', 'tside_gender': '', 'cside_thread': '2"', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Bresser_Messier_Dobson_16_Truss': {'brand': 'Bresser', 'name': 'Messier Dobson 16" Truss', 'type': 'type_telescope', 'optical_length': 0, 'mass': 24000, 'tside_thread': '', 'tside_gender': '', 'cside_thread': '2"', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Bresser_Lyra_150_1200_EQ3': {'brand': 'Bresser', 'name': 'Lyra 150/1200 EQ3', 'type': 'type_refractor', 'optical_length': 0, 'mass': 4200, 'tside_thread': '', 'tside_gender': '', 'cside_thread': '2"', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Bresser_Solarix_76_350_AZ': {'brand': 'Bresser', 'name': 'Solarix 76/350 AZ', 'type': 'type_telescope', 'optical_length': 0, 'mass': 1000, 'tside_thread': '', 'tside_gender': '', 'cside_thread': '1.25"', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Bresser_Pollux_150_750_EQ3': {'brand': 'Bresser', 'name': 'Pollux 150/750 EQ3', 'type': 'type_telescope', 'optical_length': 0, 'mass': 3800, 'tside_thread': '', 'tside_gender': '', 'cside_thread': '2"', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Bresser_National_Geographic_114_500_AZ': {'brand': 'Bresser', 'name': 'National Geographic 114/500 AZ', 'type': 'type_telescope', 'optical_length': 0, 'mass': 2200, 'tside_thread': '', 'tside_gender': '', 'cside_thread': '1.25"', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Bresser_National_Geographic_90_1250_Mak': {'brand': 'Bresser', 'name': 'National Geographic 90/1250 Mak', 'type': 'type_telescope', 'optical_length': 0, 'mass': 2000, 'tside_thread': '', 'tside_gender': '', 'cside_thread': '1.25"', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Bresser_National_Geographic_130_650_EQ': {'brand': 'Bresser', 'name': 'National Geographic 130/650 EQ', 'type': 'type_telescope', 'optical_length': 0, 'mass': 3200, 'tside_thread': '', 'tside_gender': '', 'cside_thread': '2"', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Bresser_FirstLight_152_1200_EQ3': {'brand': 'Bresser', 'name': 'FirstLight 152/1200 EQ3', 'type': 'type_telescope', 'optical_length': 0, 'mass': 5200, 'tside_thread': '', 'tside_gender': '', 'cside_thread': '2"', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Bresser_FirstLight_102_460_Table_Dob': {'brand': 'Bresser', 'name': 'FirstLight 102/460 (Table Dob)', 'type': 'type_telescope', 'optical_length': 0, 'mass': 1800, 'tside_thread': '', 'tside_gender': '', 'cside_thread': '1.25"', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}}

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
    def Bresser_Messier_NT_254_10(cls):
        return cls.from_database(cls._DATABASE['Bresser_Messier_NT_254_10'])

    @classmethod
    def Bresser_Messier_AR_80(cls):
        return cls.from_database(cls._DATABASE['Bresser_Messier_AR_80'])

    @classmethod
    def Bresser_Messier_AR_90(cls):
        return cls.from_database(cls._DATABASE['Bresser_Messier_AR_90'])

    @classmethod
    def Bresser_Messier_MC_100(cls):
        return cls.from_database(cls._DATABASE['Bresser_Messier_MC_100'])

    @classmethod
    def Bresser_Messier_NT_130(cls):
        return cls.from_database(cls._DATABASE['Bresser_Messier_NT_130'])

    @classmethod
    def Bresser_Arcturus_60_700_AZ(cls):
        return cls.from_database(cls._DATABASE['Bresser_Arcturus_60_700_AZ'])

    @classmethod
    def Bresser_Pollux_150_1400(cls):
        return cls.from_database(cls._DATABASE['Bresser_Pollux_150_1400'])

    @classmethod
    def Bresser_Bresser_Spica_130_1000(cls):
        return cls.from_database(cls._DATABASE['Bresser_Bresser_Spica_130_1000'])

    @classmethod
    def Bresser_Messier_AR_102L(cls):
        return cls.from_database(cls._DATABASE['Bresser_Messier_AR_102L'])

    @classmethod
    def Bresser_Messier_AR_127S(cls):
        return cls.from_database(cls._DATABASE['Bresser_Messier_AR_127S'])

    @classmethod
    def Bresser_Messier_NT_150S_6_f_5(cls):
        return cls.from_database(cls._DATABASE['Bresser_Messier_NT_150S_6_f_5'])

    @classmethod
    def Bresser_Messier_Dobson_8(cls):
        return cls.from_database(cls._DATABASE['Bresser_Messier_Dobson_8'])

    @classmethod
    def Bresser_Messier_Dobson_10(cls):
        return cls.from_database(cls._DATABASE['Bresser_Messier_Dobson_10'])

    @classmethod
    def Bresser_Messier_Dobson_12(cls):
        return cls.from_database(cls._DATABASE['Bresser_Messier_Dobson_12'])

    @classmethod
    def Bresser_Pollux_150_1400_EQ3(cls):
        return cls.from_database(cls._DATABASE['Bresser_Pollux_150_1400_EQ3'])

    @classmethod
    def Bresser_Lyra_70_900_EQ(cls):
        return cls.from_database(cls._DATABASE['Bresser_Lyra_70_900_EQ'])

    @classmethod
    def Bresser_Jupiter_70_700_AZ(cls):
        return cls.from_database(cls._DATABASE['Bresser_Jupiter_70_700_AZ'])

    @classmethod
    def Bresser_Taurus_90_900_NG(cls):
        return cls.from_database(cls._DATABASE['Bresser_Taurus_90_900_NG'])

    @classmethod
    def Bresser_Messier_Dobson_6_Truss(cls):
        return cls.from_database(cls._DATABASE['Bresser_Messier_Dobson_6_Truss'])

    @classmethod
    def Bresser_Messier_Dobson_8_Truss(cls):
        return cls.from_database(cls._DATABASE['Bresser_Messier_Dobson_8_Truss'])

    @classmethod
    def Bresser_Messier_Dobson_10_Truss(cls):
        return cls.from_database(cls._DATABASE['Bresser_Messier_Dobson_10_Truss'])

    @classmethod
    def Bresser_Messier_Dobson_12_Truss(cls):
        return cls.from_database(cls._DATABASE['Bresser_Messier_Dobson_12_Truss'])

    @classmethod
    def Bresser_Messier_Dobson_14_Truss(cls):
        return cls.from_database(cls._DATABASE['Bresser_Messier_Dobson_14_Truss'])

    @classmethod
    def Bresser_Messier_Dobson_16_Truss(cls):
        return cls.from_database(cls._DATABASE['Bresser_Messier_Dobson_16_Truss'])

    @classmethod
    def Bresser_Lyra_150_1200_EQ3(cls):
        return cls.from_database(cls._DATABASE['Bresser_Lyra_150_1200_EQ3'])

    @classmethod
    def Bresser_Solarix_76_350_AZ(cls):
        return cls.from_database(cls._DATABASE['Bresser_Solarix_76_350_AZ'])

    @classmethod
    def Bresser_Pollux_150_750_EQ3(cls):
        return cls.from_database(cls._DATABASE['Bresser_Pollux_150_750_EQ3'])

    @classmethod
    def Bresser_National_Geographic_114_500_AZ(cls):
        return cls.from_database(cls._DATABASE['Bresser_National_Geographic_114_500_AZ'])

    @classmethod
    def Bresser_National_Geographic_90_1250_Mak(cls):
        return cls.from_database(cls._DATABASE['Bresser_National_Geographic_90_1250_Mak'])

    @classmethod
    def Bresser_National_Geographic_130_650_EQ(cls):
        return cls.from_database(cls._DATABASE['Bresser_National_Geographic_130_650_EQ'])

    @classmethod
    def Bresser_FirstLight_152_1200_EQ3(cls):
        return cls.from_database(cls._DATABASE['Bresser_FirstLight_152_1200_EQ3'])

    @classmethod
    def Bresser_FirstLight_102_460_Table_Dob(cls):
        return cls.from_database(cls._DATABASE['Bresser_FirstLight_102_460_Table_Dob'])