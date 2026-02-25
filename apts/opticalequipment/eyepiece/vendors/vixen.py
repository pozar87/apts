from ..base import Eyepiece

class VixenEyepiece(Eyepiece):
    _DATABASE = {'Vixen_SSW_3_5mm': {'brand': 'Vixen', 'name': 'SSW 3.5mm', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 270, 'tside_thread': '1.25"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}, 'Vixen_SSW_5mm': {'brand': 'Vixen', 'name': 'SSW 5mm', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 275, 'tside_thread': '1.25"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}, 'Vixen_SSW_7mm': {'brand': 'Vixen', 'name': 'SSW 7mm', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 280, 'tside_thread': '1.25"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}, 'Vixen_SSW_10mm': {'brand': 'Vixen', 'name': 'SSW 10mm', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 285, 'tside_thread': '1.25"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}, 'Vixen_SSW_14mm': {'brand': 'Vixen', 'name': 'SSW 14mm', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 290, 'tside_thread': '1.25"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}, 'Vixen_SLV_2_5mm': {'brand': 'Vixen', 'name': 'SLV 2.5mm', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 180, 'tside_thread': '1.25"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}, 'Vixen_SLV_4mm': {'brand': 'Vixen', 'name': 'SLV 4mm', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 185, 'tside_thread': '1.25"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}, 'Vixen_SLV_6mm': {'brand': 'Vixen', 'name': 'SLV 6mm', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 190, 'tside_thread': '1.25"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}, 'Vixen_SLV_9mm': {'brand': 'Vixen', 'name': 'SLV 9mm', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 195, 'tside_thread': '1.25"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}, 'Vixen_SLV_10mm': {'brand': 'Vixen', 'name': 'SLV 10mm', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 200, 'tside_thread': '1.25"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}, 'Vixen_SLV_12mm': {'brand': 'Vixen', 'name': 'SLV 12mm', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 210, 'tside_thread': '1.25"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}, 'Vixen_SLV_15mm': {'brand': 'Vixen', 'name': 'SLV 15mm', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 220, 'tside_thread': '1.25"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}, 'Vixen_SLV_20mm': {'brand': 'Vixen', 'name': 'SLV 20mm', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 240, 'tside_thread': '1.25"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}, 'Vixen_SLV_25mm': {'brand': 'Vixen', 'name': 'SLV 25mm', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 260, 'tside_thread': '1.25"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}, 'Vixen_NLV_4mm': {'brand': 'Vixen', 'name': 'NLV 4mm', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 140, 'tside_thread': '1.25"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}, 'Vixen_NLV_5mm': {'brand': 'Vixen', 'name': 'NLV 5mm', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 142, 'tside_thread': '1.25"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}, 'Vixen_NLV_6mm': {'brand': 'Vixen', 'name': 'NLV 6mm', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 145, 'tside_thread': '1.25"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}, 'Vixen_NLV_8mm': {'brand': 'Vixen', 'name': 'NLV 8mm', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 150, 'tside_thread': '1.25"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}, 'Vixen_NLV_10mm': {'brand': 'Vixen', 'name': 'NLV 10mm', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 155, 'tside_thread': '1.25"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}, 'Vixen_NLV_12mm': {'brand': 'Vixen', 'name': 'NLV 12mm', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 160, 'tside_thread': '1.25"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}, 'Vixen_NLV_15mm': {'brand': 'Vixen', 'name': 'NLV 15mm', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 170, 'tside_thread': '1.25"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}, 'Vixen_NLV_20mm': {'brand': 'Vixen', 'name': 'NLV 20mm', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 180, 'tside_thread': '1.25"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}, 'Vixen_NLV_25mm': {'brand': 'Vixen', 'name': 'NLV 25mm', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 200, 'tside_thread': '1.25"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}, 'Vixen_LVW_3_5mm': {'brand': 'Vixen', 'name': 'LVW 3.5mm', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 280, 'tside_thread': '1.25"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}, 'Vixen_LVW_5mm': {'brand': 'Vixen', 'name': 'LVW 5mm', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 285, 'tside_thread': '1.25"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}, 'Vixen_LVW_8mm': {'brand': 'Vixen', 'name': 'LVW 8mm', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 295, 'tside_thread': '1.25"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}, 'Vixen_LVW_13mm': {'brand': 'Vixen', 'name': 'LVW 13mm', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 350, 'tside_thread': '2"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}, 'Vixen_LVW_17mm': {'brand': 'Vixen', 'name': 'LVW 17mm', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 380, 'tside_thread': '2"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}, 'Vixen_LVW_22mm': {'brand': 'Vixen', 'name': 'LVW 22mm', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 420, 'tside_thread': '2"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}, 'Vixen_LVW_30mm': {'brand': 'Vixen', 'name': 'LVW 30mm', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 580, 'tside_thread': '2"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}, 'Vixen_LVW_42mm': {'brand': 'Vixen', 'name': 'LVW 42mm', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 800, 'tside_thread': '2"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}, 'Vixen_NLV_Zoom_8_24mm': {'brand': 'Vixen', 'name': 'NLV Zoom 8-24mm', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 300, 'tside_thread': '1.25"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}, 'Vixen_NPL_Plossl_2_5mm': {'brand': 'Vixen', 'name': 'NPL Plossl 2.5mm', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 130, 'tside_thread': '1.25"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}, 'Vixen_NPL_Plossl_4mm': {'brand': 'Vixen', 'name': 'NPL Plossl 4mm', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 135, 'tside_thread': '1.25"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}, 'Vixen_NPL_Plossl_5mm': {'brand': 'Vixen', 'name': 'NPL Plossl 5mm', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 140, 'tside_thread': '1.25"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}, 'Vixen_NPL_Plossl_6mm': {'brand': 'Vixen', 'name': 'NPL Plossl 6mm', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 145, 'tside_thread': '1.25"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}, 'Vixen_NPL_Plossl_8mm': {'brand': 'Vixen', 'name': 'NPL Plossl 8mm', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 155, 'tside_thread': '1.25"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}, 'Vixen_NPL_Plossl_10mm': {'brand': 'Vixen', 'name': 'NPL Plossl 10mm', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 165, 'tside_thread': '1.25"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}, 'Vixen_NPL_Plossl_12mm': {'brand': 'Vixen', 'name': 'NPL Plossl 12mm', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 175, 'tside_thread': '1.25"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}, 'Vixen_NPL_Plossl_15mm': {'brand': 'Vixen', 'name': 'NPL Plossl 15mm', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 190, 'tside_thread': '1.25"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}, 'Vixen_NPL_Plossl_18mm': {'brand': 'Vixen', 'name': 'NPL Plossl 18mm', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 210, 'tside_thread': '1.25"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}, 'Vixen_NPL_Plossl_25mm': {'brand': 'Vixen', 'name': 'NPL Plossl 25mm', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 250, 'tside_thread': '1.25"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}, 'Vixen_HR_1_6mm': {'brand': 'Vixen', 'name': 'HR 1.6mm', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 200, 'tside_thread': '1.25"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}, 'Vixen_HR_2mm': {'brand': 'Vixen', 'name': 'HR 2mm', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 205, 'tside_thread': '1.25"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}, 'Vixen_HR_2_4mm': {'brand': 'Vixen', 'name': 'HR 2.4mm', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 210, 'tside_thread': '1.25"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}, 'Vixen_HR_3_4mm': {'brand': 'Vixen', 'name': 'HR 3.4mm', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 215, 'tside_thread': '1.25"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}}

    @classmethod
    def Vixen_SSW_3_5mm(cls):
        return cls.from_database(cls._DATABASE['Vixen_SSW_3_5mm'])

    @classmethod
    def Vixen_SSW_5mm(cls):
        return cls.from_database(cls._DATABASE['Vixen_SSW_5mm'])

    @classmethod
    def Vixen_SSW_7mm(cls):
        return cls.from_database(cls._DATABASE['Vixen_SSW_7mm'])

    @classmethod
    def Vixen_SSW_10mm(cls):
        return cls.from_database(cls._DATABASE['Vixen_SSW_10mm'])

    @classmethod
    def Vixen_SSW_14mm(cls):
        return cls.from_database(cls._DATABASE['Vixen_SSW_14mm'])

    @classmethod
    def Vixen_SLV_2_5mm(cls):
        return cls.from_database(cls._DATABASE['Vixen_SLV_2_5mm'])

    @classmethod
    def Vixen_SLV_4mm(cls):
        return cls.from_database(cls._DATABASE['Vixen_SLV_4mm'])

    @classmethod
    def Vixen_SLV_6mm(cls):
        return cls.from_database(cls._DATABASE['Vixen_SLV_6mm'])

    @classmethod
    def Vixen_SLV_9mm(cls):
        return cls.from_database(cls._DATABASE['Vixen_SLV_9mm'])

    @classmethod
    def Vixen_SLV_10mm(cls):
        return cls.from_database(cls._DATABASE['Vixen_SLV_10mm'])

    @classmethod
    def Vixen_SLV_12mm(cls):
        return cls.from_database(cls._DATABASE['Vixen_SLV_12mm'])

    @classmethod
    def Vixen_SLV_15mm(cls):
        return cls.from_database(cls._DATABASE['Vixen_SLV_15mm'])

    @classmethod
    def Vixen_SLV_20mm(cls):
        return cls.from_database(cls._DATABASE['Vixen_SLV_20mm'])

    @classmethod
    def Vixen_SLV_25mm(cls):
        return cls.from_database(cls._DATABASE['Vixen_SLV_25mm'])

    @classmethod
    def Vixen_NLV_4mm(cls):
        return cls.from_database(cls._DATABASE['Vixen_NLV_4mm'])

    @classmethod
    def Vixen_NLV_5mm(cls):
        return cls.from_database(cls._DATABASE['Vixen_NLV_5mm'])

    @classmethod
    def Vixen_NLV_6mm(cls):
        return cls.from_database(cls._DATABASE['Vixen_NLV_6mm'])

    @classmethod
    def Vixen_NLV_8mm(cls):
        return cls.from_database(cls._DATABASE['Vixen_NLV_8mm'])

    @classmethod
    def Vixen_NLV_10mm(cls):
        return cls.from_database(cls._DATABASE['Vixen_NLV_10mm'])

    @classmethod
    def Vixen_NLV_12mm(cls):
        return cls.from_database(cls._DATABASE['Vixen_NLV_12mm'])

    @classmethod
    def Vixen_NLV_15mm(cls):
        return cls.from_database(cls._DATABASE['Vixen_NLV_15mm'])

    @classmethod
    def Vixen_NLV_20mm(cls):
        return cls.from_database(cls._DATABASE['Vixen_NLV_20mm'])

    @classmethod
    def Vixen_NLV_25mm(cls):
        return cls.from_database(cls._DATABASE['Vixen_NLV_25mm'])

    @classmethod
    def Vixen_LVW_3_5mm(cls):
        return cls.from_database(cls._DATABASE['Vixen_LVW_3_5mm'])

    @classmethod
    def Vixen_LVW_5mm(cls):
        return cls.from_database(cls._DATABASE['Vixen_LVW_5mm'])

    @classmethod
    def Vixen_LVW_8mm(cls):
        return cls.from_database(cls._DATABASE['Vixen_LVW_8mm'])

    @classmethod
    def Vixen_LVW_13mm(cls):
        return cls.from_database(cls._DATABASE['Vixen_LVW_13mm'])

    @classmethod
    def Vixen_LVW_17mm(cls):
        return cls.from_database(cls._DATABASE['Vixen_LVW_17mm'])

    @classmethod
    def Vixen_LVW_22mm(cls):
        return cls.from_database(cls._DATABASE['Vixen_LVW_22mm'])

    @classmethod
    def Vixen_LVW_30mm(cls):
        return cls.from_database(cls._DATABASE['Vixen_LVW_30mm'])

    @classmethod
    def Vixen_LVW_42mm(cls):
        return cls.from_database(cls._DATABASE['Vixen_LVW_42mm'])

    @classmethod
    def Vixen_NLV_Zoom_8_24mm(cls):
        return cls.from_database(cls._DATABASE['Vixen_NLV_Zoom_8_24mm'])

    @classmethod
    def Vixen_NPL_Plossl_2_5mm(cls):
        return cls.from_database(cls._DATABASE['Vixen_NPL_Plossl_2_5mm'])

    @classmethod
    def Vixen_NPL_Plossl_4mm(cls):
        return cls.from_database(cls._DATABASE['Vixen_NPL_Plossl_4mm'])

    @classmethod
    def Vixen_NPL_Plossl_5mm(cls):
        return cls.from_database(cls._DATABASE['Vixen_NPL_Plossl_5mm'])

    @classmethod
    def Vixen_NPL_Plossl_6mm(cls):
        return cls.from_database(cls._DATABASE['Vixen_NPL_Plossl_6mm'])

    @classmethod
    def Vixen_NPL_Plossl_8mm(cls):
        return cls.from_database(cls._DATABASE['Vixen_NPL_Plossl_8mm'])

    @classmethod
    def Vixen_NPL_Plossl_10mm(cls):
        return cls.from_database(cls._DATABASE['Vixen_NPL_Plossl_10mm'])

    @classmethod
    def Vixen_NPL_Plossl_12mm(cls):
        return cls.from_database(cls._DATABASE['Vixen_NPL_Plossl_12mm'])

    @classmethod
    def Vixen_NPL_Plossl_15mm(cls):
        return cls.from_database(cls._DATABASE['Vixen_NPL_Plossl_15mm'])

    @classmethod
    def Vixen_NPL_Plossl_18mm(cls):
        return cls.from_database(cls._DATABASE['Vixen_NPL_Plossl_18mm'])

    @classmethod
    def Vixen_NPL_Plossl_25mm(cls):
        return cls.from_database(cls._DATABASE['Vixen_NPL_Plossl_25mm'])

    @classmethod
    def Vixen_HR_1_6mm(cls):
        return cls.from_database(cls._DATABASE['Vixen_HR_1_6mm'])

    @classmethod
    def Vixen_HR_2mm(cls):
        return cls.from_database(cls._DATABASE['Vixen_HR_2mm'])

    @classmethod
    def Vixen_HR_2_4mm(cls):
        return cls.from_database(cls._DATABASE['Vixen_HR_2_4mm'])

    @classmethod
    def Vixen_HR_3_4mm(cls):
        return cls.from_database(cls._DATABASE['Vixen_HR_3_4mm'])