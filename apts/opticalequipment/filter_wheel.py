from .abstract import IntermediateOpticalEquipment
from ..constants import OpticalType
from ..utils import ConnectionType

class FilterWheel(IntermediateOpticalEquipment):
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
    def __init__(self, vendor, optical_length=0, mass=0, in_connection_type=None, out_connection_type=None, in_gender=None, out_gender=None):
        super(FilterWheel, self).__init__(
            vendor, optical_length=optical_length, mass=mass,
            in_connection_type=in_connection_type, out_connection_type=out_connection_type,
            in_gender=in_gender, out_gender=out_gender
        )
        self._type = OpticalType.FILTER_WHEEL



    _DATABASE = {
        'ZWO_EFW_Mini_5x1_25': {'brand': 'ZWO', 'name': 'EFW Mini 5x1.25"', 'type': 'type_filter_wheel', 'optical_length': 20, 'mass': 265, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''},
        'ZWO_EFW_8x1_25': {'brand': 'ZWO', 'name': 'EFW 8x1.25"', 'type': 'type_filter_wheel', 'optical_length': 20, 'mass': 380, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''},
        'ZWO_EFW_7x36mm': {'brand': 'ZWO', 'name': 'EFW 7x36mm', 'type': 'type_filter_wheel', 'optical_length': 20, 'mass': 400, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''},
        'ZWO_EFW_5x2_M48': {'brand': 'ZWO', 'name': 'EFW 5x2" (M48)', 'type': 'type_filter_wheel', 'optical_length': 20, 'mass': 550, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''},
        'ZWO_EFW_5x2_M54': {'brand': 'ZWO', 'name': 'EFW 5x2" (M54)', 'type': 'type_filter_wheel', 'optical_length': 20, 'mass': 600, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''},
        'ZWO_EFW_7x2_M54': {'brand': 'ZWO', 'name': 'EFW 7x2" (M54)', 'type': 'type_filter_wheel', 'optical_length': 20, 'mass': 700, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''},
        'ZWO_EFW_7x50mm_M54': {'brand': 'ZWO', 'name': 'EFW 7x50mm (M54)', 'type': 'type_filter_wheel', 'optical_length': 20, 'mass': 700, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''},
        'QHY_CFW3S_Small': {'brand': 'QHY', 'name': 'CFW3S Small', 'type': 'type_filter_wheel', 'optical_length': 20, 'mass': 450, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''},
        'QHY_CFW3M_Medium': {'brand': 'QHY', 'name': 'CFW3M Medium', 'type': 'type_filter_wheel', 'optical_length': 20, 'mass': 600, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''},
        'QHY_CFW3L_Large': {'brand': 'QHY', 'name': 'CFW3L Large', 'type': 'type_filter_wheel', 'optical_length': 20, 'mass': 850, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''},
        'QHY_CFW3XL_Extra_Large': {'brand': 'QHY', 'name': 'CFW3XL Extra Large', 'type': 'type_filter_wheel', 'optical_length': 22, 'mass': 1000, 'tside_thread': 'M68', 'tside_gender': 'Female', 'cside_thread': 'M68', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''},
        'QHY_CFW3S_US_Ultra_Slim': {'brand': 'QHY', 'name': 'CFW3S-US Ultra Slim', 'type': 'type_filter_wheel', 'optical_length': 14, 'mass': 350, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''},
        'Player_One_Xena_M_M42': {'brand': 'Player One', 'name': 'Xena-M (M42)', 'type': 'type_filter_wheel', 'optical_length': 20, 'mass': 350, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''},
        'Player_One_Xena_L_M54': {'brand': 'Player One', 'name': 'Xena-L (M54)', 'type': 'type_filter_wheel', 'optical_length': 21, 'mass': 600, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''},
        'Player_One_Xena_XL_M68': {'brand': 'Player One', 'name': 'Xena-XL (M68)', 'type': 'type_filter_wheel', 'optical_length': 22, 'mass': 800, 'tside_thread': 'M68', 'tside_gender': 'Female', 'cside_thread': 'M68', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''},
        'Pegasus_Indigo_Filter_Wheel_M42': {'brand': 'Pegasus', 'name': 'Indigo Filter Wheel (M42)', 'type': 'type_filter_wheel', 'optical_length': 19.6, 'mass': 400, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''},
        'Pegasus_Indigo_Filter_Wheel_M54': {'brand': 'Pegasus', 'name': 'Indigo Filter Wheel (M54)', 'type': 'type_filter_wheel', 'optical_length': 19.6, 'mass': 500, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''},
        'Atik_EFW2_M42': {'brand': 'Atik', 'name': 'EFW2 (M42)', 'type': 'type_filter_wheel', 'optical_length': 20, 'mass': 350, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''},
        'Atik_EFW3_M54': {'brand': 'Atik', 'name': 'EFW3 (M54)', 'type': 'type_filter_wheel', 'optical_length': 20, 'mass': 550, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''},
        'Starlight_Xpress_SX_Mini_Wheel': {'brand': 'Starlight Xpress', 'name': 'SX Mini Wheel', 'type': 'type_filter_wheel', 'optical_length': 20, 'mass': 300, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''},
        'Starlight_Xpress_SX_USB_Wheel_M54': {'brand': 'Starlight Xpress', 'name': 'SX USB Wheel (M54)', 'type': 'type_filter_wheel', 'optical_length': 21, 'mass': 600, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''},
        'Moravian_IFW_Internal_FW': {'brand': 'Moravian', 'name': 'IFW (Internal FW)', 'type': 'type_filter_wheel', 'optical_length': 0, 'mass': 300, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''},
        'SVBony_SV305_FW_1_25': {'brand': 'SVBony', 'name': 'SV305 FW 1.25"', 'type': 'type_filter_wheel', 'optical_length': 18, 'mass': 200, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''},
        'Baader_SteelTrack_Filter_Wheel': {'brand': 'Baader', 'name': 'SteelTrack Filter Wheel', 'type': 'type_filter_wheel', 'optical_length': 20, 'mass': 450, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''},
        'OGMA_OGC_FW7_M42': {'brand': 'OGMA', 'name': 'OGC-FW7 (M42)', 'type': 'type_filter_wheel', 'optical_length': 20, 'mass': 380, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''},
        'Lacerta_Filter_Wheel_M42': {'brand': 'Lacerta', 'name': 'Filter Wheel (M42)', 'type': 'type_filter_wheel', 'optical_length': 20, 'mass': 350, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''},
        'Lacerta_Filter_Wheel_M54': {'brand': 'Lacerta', 'name': 'Filter Wheel (M54)', 'type': 'type_filter_wheel', 'optical_length': 20, 'mass': 550, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''},
        'Altair_Filter_Wheel_5x1_25_M42': {'brand': 'Altair', 'name': 'Filter Wheel 5x1.25" (M42)', 'type': 'type_filter_wheel', 'optical_length': 18, 'mass': 320, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''},
        'Altair_Filter_Wheel_7x2_M54': {'brand': 'Altair', 'name': 'Filter Wheel 7x2" (M54)', 'type': 'type_filter_wheel', 'optical_length': 20, 'mass': 600, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''},
        'ToupTek_Filter_Wheel_5x1_25_M42': {'brand': 'ToupTek', 'name': 'Filter Wheel 5x1.25" (M42)', 'type': 'type_filter_wheel', 'optical_length': 18, 'mass': 300, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''},
        'ToupTek_Filter_Wheel_7x2_M54': {'brand': 'ToupTek', 'name': 'Filter Wheel 7x2" (M54)', 'type': 'type_filter_wheel', 'optical_length': 20, 'mass': 550, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''},
        'Rising_Cam_Filter_Wheel_5x1_25_M42': {'brand': 'Rising Cam', 'name': 'Filter Wheel 5x1.25" (M42)', 'type': 'type_filter_wheel', 'optical_length': 18, 'mass': 280, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''},
        'Omegon_Filter_Wheel_5x1_25_M42': {'brand': 'Omegon', 'name': 'Filter Wheel 5x1.25" (M42)', 'type': 'type_filter_wheel', 'optical_length': 18, 'mass': 300, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''},
        'Omegon_Filter_Wheel_7x2_M54': {'brand': 'Omegon', 'name': 'Filter Wheel 7x2" (M54)', 'type': 'type_filter_wheel', 'optical_length': 20, 'mass': 550, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''},
        'FLI_CFW_2_7_M54': {'brand': 'FLI', 'name': 'CFW-2-7 (M54)', 'type': 'type_filter_wheel', 'optical_length': 20, 'mass': 600, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''},
        'FLI_CFW_3_10_M68': {'brand': 'FLI', 'name': 'CFW-3-10 (M68)', 'type': 'type_filter_wheel', 'optical_length': 22, 'mass': 800, 'tside_thread': 'M68', 'tside_gender': 'Female', 'cside_thread': 'M68', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''},
        'FLI_Atlas_M54': {'brand': 'FLI', 'name': 'Atlas (M54)', 'type': 'type_filter_wheel', 'optical_length': 20, 'mass': 700, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''},
        'SBIG_FW5_8300_M42': {'brand': 'SBIG', 'name': 'FW5-8300 (M42)', 'type': 'type_filter_wheel', 'optical_length': 18, 'mass': 350, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''},
        'SBIG_FW8_STT_M54': {'brand': 'SBIG', 'name': 'FW8-STT (M54)', 'type': 'type_filter_wheel', 'optical_length': 20, 'mass': 600, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''},
        'SBIG_FW7_STX_M68': {'brand': 'SBIG', 'name': 'FW7-STX (M68)', 'type': 'type_filter_wheel', 'optical_length': 22, 'mass': 800, 'tside_thread': 'M68', 'tside_gender': 'Female', 'cside_thread': 'M68', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''},
        'Player_One_Xena_S_M42': {'brand': 'Player One', 'name': 'Xena-S (M42)', 'type': 'type_filter_wheel', 'optical_length': 18, 'mass': 280, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''},
        'Wanderer_Astro_FilterWheel_M42': {'brand': 'Wanderer Astro', 'name': 'FilterWheel (M42)', 'type': 'type_filter_wheel', 'optical_length': 19, 'mass': 300, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''},
        'Wanderer_Astro_FilterWheel_M48': {'brand': 'Wanderer Astro', 'name': 'FilterWheel (M48)', 'type': 'type_filter_wheel', 'optical_length': 19, 'mass': 380, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''},
        'Wanderer_Astro_FilterWheel_M54': {'brand': 'Wanderer Astro', 'name': 'FilterWheel (M54)', 'type': 'type_filter_wheel', 'optical_length': 20, 'mass': 500, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''},
        'Wanderer_Astro_FilterWheel_M68': {'brand': 'Wanderer Astro', 'name': 'FilterWheel (M68)', 'type': 'type_filter_wheel', 'optical_length': 21, 'mass': 600, 'tside_thread': 'M68', 'tside_gender': 'Female', 'cside_thread': 'M68', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''},
        'Askar_Filter_Wheel_5x_M42': {'brand': 'Askar', 'name': 'Filter Wheel 5x (M42)', 'type': 'type_filter_wheel', 'optical_length': 19, 'mass': 310, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''},
        'Askar_Filter_Wheel_7x_M48': {'brand': 'Askar', 'name': 'Filter Wheel 7x (M48)', 'type': 'type_filter_wheel', 'optical_length': 20, 'mass': 450, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''},
        'Askar_Filter_Wheel_7x_M54': {'brand': 'Askar', 'name': 'Filter Wheel 7x (M54)', 'type': 'type_filter_wheel', 'optical_length': 20, 'mass': 550, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''},
        'Sharpstar_Filter_Wheel_5x_M42': {'brand': 'Sharpstar', 'name': 'Filter Wheel 5x (M42)', 'type': 'type_filter_wheel', 'optical_length': 18, 'mass': 290, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''},
        'Sharpstar_Filter_Wheel_7x_M48': {'brand': 'Sharpstar', 'name': 'Filter Wheel 7x (M48)', 'type': 'type_filter_wheel', 'optical_length': 20, 'mass': 440, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''},
        'Altair_Filter_Wheel_5x_M42': {'brand': 'Altair', 'name': 'Filter Wheel 5x (M42)', 'type': 'type_filter_wheel', 'optical_length': 19, 'mass': 300, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''},
        'Altair_Filter_Wheel_7x_M48': {'brand': 'Altair', 'name': 'Filter Wheel 7x (M48)', 'type': 'type_filter_wheel', 'optical_length': 20, 'mass': 450, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''},
        'Altair_Filter_Wheel_7x_M54': {'brand': 'Altair', 'name': 'Filter Wheel 7x (M54)', 'type': 'type_filter_wheel', 'optical_length': 20, 'mass': 550, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''},
        'Omegon_Filter_Wheel_5x_M42': {'brand': 'Omegon', 'name': 'Filter Wheel 5x (M42)', 'type': 'type_filter_wheel', 'optical_length': 18, 'mass': 280, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''},
        'Omegon_Filter_Wheel_7x_M48': {'brand': 'Omegon', 'name': 'Filter Wheel 7x (M48)', 'type': 'type_filter_wheel', 'optical_length': 20, 'mass': 430, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''},
        'Lacerta_Filter_Wheel_5x_M42': {'brand': 'Lacerta', 'name': 'Filter Wheel 5x (M42)', 'type': 'type_filter_wheel', 'optical_length': 18, 'mass': 280, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''},
        'Lacerta_Filter_Wheel_7x_M48': {'brand': 'Lacerta', 'name': 'Filter Wheel 7x (M48)', 'type': 'type_filter_wheel', 'optical_length': 20, 'mass': 440, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''},
        'Lacerta_Filter_Wheel_7x_M54': {'brand': 'Lacerta', 'name': 'Filter Wheel 7x (M54)', 'type': 'type_filter_wheel', 'optical_length': 20, 'mass': 550, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''},
        'Bresser_Filter_Wheel_5x_M42': {'brand': 'Bresser', 'name': 'Filter Wheel 5x (M42)', 'type': 'type_filter_wheel', 'optical_length': 18, 'mass': 260, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''},
        'Bresser_Filter_Wheel_7x_M48': {'brand': 'Bresser', 'name': 'Filter Wheel 7x (M48)', 'type': 'type_filter_wheel', 'optical_length': 19, 'mass': 410, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''},
        'OGMA_OGC_FW5_M48': {'brand': 'OGMA', 'name': 'OGC-FW5 (M48)', 'type': 'type_filter_wheel', 'optical_length': 20, 'mass': 420, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''},
        'OGMA_OGC_FW9_M54': {'brand': 'OGMA', 'name': 'OGC-FW9 (M54)', 'type': 'type_filter_wheel', 'optical_length': 21, 'mass': 600, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''},
        'Vixen_Filter_Wheel_5x_M42': {'brand': 'Vixen', 'name': 'Filter Wheel 5x (M42)', 'type': 'type_filter_wheel', 'optical_length': 18, 'mass': 280, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''},
        'Explore_Scientific_Filter_Wheel_5x_M42': {'brand': 'Explore Scientific', 'name': 'Filter Wheel 5x (M42)', 'type': 'type_filter_wheel', 'optical_length': 18, 'mass': 290, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''},
        'Explore_Scientific_Filter_Wheel_7x_M48': {'brand': 'Explore Scientific', 'name': 'Filter Wheel 7x (M48)', 'type': 'type_filter_wheel', 'optical_length': 20, 'mass': 450, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''},
        'SVBony_SV222_FW_5x1_25_M42': {'brand': 'SVBony', 'name': 'SV222 FW 5x1.25" (M42)', 'type': 'type_filter_wheel', 'optical_length': 18, 'mass': 220, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''},
        'SVBony_SV222_FW_7x_M48': {'brand': 'SVBony', 'name': 'SV222 FW 7x (M48)', 'type': 'type_filter_wheel', 'optical_length': 20, 'mass': 380, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''},
        'Orion_Nautilus_5x_M42': {'brand': 'Orion', 'name': 'Nautilus 5x (M42)', 'type': 'type_filter_wheel', 'optical_length': 19, 'mass': 300, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''},
        'Orion_Nautilus_7x_M48': {'brand': 'Orion', 'name': 'Nautilus 7x (M48)', 'type': 'type_filter_wheel', 'optical_length': 20, 'mass': 450, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''},
        'Meade_Series_6000_FW_M42': {'brand': 'Meade', 'name': 'Series 6000 FW (M42)', 'type': 'type_filter_wheel', 'optical_length': 19, 'mass': 320, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''},
        'Celestron_Filter_Wheel_5x_M42': {'brand': 'Celestron', 'name': 'Filter Wheel 5x (M42)', 'type': 'type_filter_wheel', 'optical_length': 18, 'mass': 280, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''},
        'Celestron_Filter_Wheel_7x_M48': {'brand': 'Celestron', 'name': 'Filter Wheel 7x (M48)', 'type': 'type_filter_wheel', 'optical_length': 20, 'mass': 440, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''},
        'Rising_Cam_Filter_Wheel_5x_M42': {'brand': 'Rising Cam', 'name': 'Filter Wheel 5x (M42)', 'type': 'type_filter_wheel', 'optical_length': 18, 'mass': 270, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''},
        'Rising_Cam_Filter_Wheel_7x_M48': {'brand': 'Rising Cam', 'name': 'Filter Wheel 7x (M48)', 'type': 'type_filter_wheel', 'optical_length': 20, 'mass': 420, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''},
        'Starlight_Xpress_SX_Maxi_Wheel_M68': {'brand': 'Starlight Xpress', 'name': 'SX Maxi Wheel (M68)', 'type': 'type_filter_wheel', 'optical_length': 22, 'mass': 700, 'tside_thread': 'M68', 'tside_gender': 'Female', 'cside_thread': 'M68', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''},
        'Moravian_EFW_2H_M42': {'brand': 'Moravian', 'name': 'EFW-2H (M42)', 'type': 'type_filter_wheel', 'optical_length': 18, 'mass': 350, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''},
        'Moravian_EFW_3H_M54': {'brand': 'Moravian', 'name': 'EFW-3H (M54)', 'type': 'type_filter_wheel', 'optical_length': 20, 'mass': 550, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''},
        'FLI_CenterLine_M42': {'brand': 'FLI', 'name': 'CenterLine (M42)', 'type': 'type_filter_wheel', 'optical_length': 18, 'mass': 400, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''},
        'FLI_CenterLine_M68': {'brand': 'FLI', 'name': 'CenterLine (M68)', 'type': 'type_filter_wheel', 'optical_length': 22, 'mass': 750, 'tside_thread': 'M68', 'tside_gender': 'Female', 'cside_thread': 'M68', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''},
    }

    @classmethod
    def ZWO_EFW_Mini_5x1_25(cls):
        return cls.from_database(cls._DATABASE['ZWO_EFW_Mini_5x1_25'])

    @classmethod
    def ZWO_EFW_8x1_25(cls):
        return cls.from_database(cls._DATABASE['ZWO_EFW_8x1_25'])

    @classmethod
    def ZWO_EFW_7x36mm(cls):
        return cls.from_database(cls._DATABASE['ZWO_EFW_7x36mm'])

    @classmethod
    def ZWO_EFW_5x2_M48(cls):
        return cls.from_database(cls._DATABASE['ZWO_EFW_5x2_M48'])

    @classmethod
    def ZWO_EFW_5x2_M54(cls):
        return cls.from_database(cls._DATABASE['ZWO_EFW_5x2_M54'])

    @classmethod
    def ZWO_EFW_7x2_M54(cls):
        return cls.from_database(cls._DATABASE['ZWO_EFW_7x2_M54'])

    @classmethod
    def ZWO_EFW_7x50mm_M54(cls):
        return cls.from_database(cls._DATABASE['ZWO_EFW_7x50mm_M54'])

    @classmethod
    def QHY_CFW3S_Small(cls):
        return cls.from_database(cls._DATABASE['QHY_CFW3S_Small'])

    @classmethod
    def QHY_CFW3M_Medium(cls):
        return cls.from_database(cls._DATABASE['QHY_CFW3M_Medium'])

    @classmethod
    def QHY_CFW3L_Large(cls):
        return cls.from_database(cls._DATABASE['QHY_CFW3L_Large'])

    @classmethod
    def QHY_CFW3XL_Extra_Large(cls):
        return cls.from_database(cls._DATABASE['QHY_CFW3XL_Extra_Large'])

    @classmethod
    def QHY_CFW3S_US_Ultra_Slim(cls):
        return cls.from_database(cls._DATABASE['QHY_CFW3S_US_Ultra_Slim'])

    @classmethod
    def Player_One_Xena_M_M42(cls):
        return cls.from_database(cls._DATABASE['Player_One_Xena_M_M42'])

    @classmethod
    def Player_One_Xena_L_M54(cls):
        return cls.from_database(cls._DATABASE['Player_One_Xena_L_M54'])

    @classmethod
    def Player_One_Xena_XL_M68(cls):
        return cls.from_database(cls._DATABASE['Player_One_Xena_XL_M68'])

    @classmethod
    def Pegasus_Indigo_Filter_Wheel_M42(cls):
        return cls.from_database(cls._DATABASE['Pegasus_Indigo_Filter_Wheel_M42'])

    @classmethod
    def Pegasus_Indigo_Filter_Wheel_M54(cls):
        return cls.from_database(cls._DATABASE['Pegasus_Indigo_Filter_Wheel_M54'])

    @classmethod
    def Atik_EFW2_M42(cls):
        return cls.from_database(cls._DATABASE['Atik_EFW2_M42'])

    @classmethod
    def Atik_EFW3_M54(cls):
        return cls.from_database(cls._DATABASE['Atik_EFW3_M54'])

    @classmethod
    def Starlight_Xpress_SX_Mini_Wheel(cls):
        return cls.from_database(cls._DATABASE['Starlight_Xpress_SX_Mini_Wheel'])

    @classmethod
    def Starlight_Xpress_SX_USB_Wheel_M54(cls):
        return cls.from_database(cls._DATABASE['Starlight_Xpress_SX_USB_Wheel_M54'])

    @classmethod
    def Moravian_IFW_Internal_FW(cls):
        return cls.from_database(cls._DATABASE['Moravian_IFW_Internal_FW'])

    @classmethod
    def SVBony_SV305_FW_1_25(cls):
        return cls.from_database(cls._DATABASE['SVBony_SV305_FW_1_25'])

    @classmethod
    def Baader_SteelTrack_Filter_Wheel(cls):
        return cls.from_database(cls._DATABASE['Baader_SteelTrack_Filter_Wheel'])

    @classmethod
    def OGMA_OGC_FW7_M42(cls):
        return cls.from_database(cls._DATABASE['OGMA_OGC_FW7_M42'])

    @classmethod
    def Lacerta_Filter_Wheel_M42(cls):
        return cls.from_database(cls._DATABASE['Lacerta_Filter_Wheel_M42'])

    @classmethod
    def Lacerta_Filter_Wheel_M54(cls):
        return cls.from_database(cls._DATABASE['Lacerta_Filter_Wheel_M54'])

    @classmethod
    def Altair_Filter_Wheel_5x1_25_M42(cls):
        return cls.from_database(cls._DATABASE['Altair_Filter_Wheel_5x1_25_M42'])

    @classmethod
    def Altair_Filter_Wheel_7x2_M54(cls):
        return cls.from_database(cls._DATABASE['Altair_Filter_Wheel_7x2_M54'])

    @classmethod
    def ToupTek_Filter_Wheel_5x1_25_M42(cls):
        return cls.from_database(cls._DATABASE['ToupTek_Filter_Wheel_5x1_25_M42'])

    @classmethod
    def ToupTek_Filter_Wheel_7x2_M54(cls):
        return cls.from_database(cls._DATABASE['ToupTek_Filter_Wheel_7x2_M54'])

    @classmethod
    def Rising_Cam_Filter_Wheel_5x1_25_M42(cls):
        return cls.from_database(cls._DATABASE['Rising_Cam_Filter_Wheel_5x1_25_M42'])

    @classmethod
    def Omegon_Filter_Wheel_5x1_25_M42(cls):
        return cls.from_database(cls._DATABASE['Omegon_Filter_Wheel_5x1_25_M42'])

    @classmethod
    def Omegon_Filter_Wheel_7x2_M54(cls):
        return cls.from_database(cls._DATABASE['Omegon_Filter_Wheel_7x2_M54'])

    @classmethod
    def FLI_CFW_2_7_M54(cls):
        return cls.from_database(cls._DATABASE['FLI_CFW_2_7_M54'])

    @classmethod
    def FLI_CFW_3_10_M68(cls):
        return cls.from_database(cls._DATABASE['FLI_CFW_3_10_M68'])

    @classmethod
    def FLI_Atlas_M54(cls):
        return cls.from_database(cls._DATABASE['FLI_Atlas_M54'])

    @classmethod
    def SBIG_FW5_8300_M42(cls):
        return cls.from_database(cls._DATABASE['SBIG_FW5_8300_M42'])

    @classmethod
    def SBIG_FW8_STT_M54(cls):
        return cls.from_database(cls._DATABASE['SBIG_FW8_STT_M54'])

    @classmethod
    def SBIG_FW7_STX_M68(cls):
        return cls.from_database(cls._DATABASE['SBIG_FW7_STX_M68'])

    @classmethod
    def Player_One_Xena_S_M42(cls):
        return cls.from_database(cls._DATABASE['Player_One_Xena_S_M42'])

    @classmethod
    def Wanderer_Astro_FilterWheel_M42(cls):
        return cls.from_database(cls._DATABASE['Wanderer_Astro_FilterWheel_M42'])

    @classmethod
    def Wanderer_Astro_FilterWheel_M48(cls):
        return cls.from_database(cls._DATABASE['Wanderer_Astro_FilterWheel_M48'])

    @classmethod
    def Wanderer_Astro_FilterWheel_M54(cls):
        return cls.from_database(cls._DATABASE['Wanderer_Astro_FilterWheel_M54'])

    @classmethod
    def Wanderer_Astro_FilterWheel_M68(cls):
        return cls.from_database(cls._DATABASE['Wanderer_Astro_FilterWheel_M68'])

    @classmethod
    def Askar_Filter_Wheel_5x_M42(cls):
        return cls.from_database(cls._DATABASE['Askar_Filter_Wheel_5x_M42'])

    @classmethod
    def Askar_Filter_Wheel_7x_M48(cls):
        return cls.from_database(cls._DATABASE['Askar_Filter_Wheel_7x_M48'])

    @classmethod
    def Askar_Filter_Wheel_7x_M54(cls):
        return cls.from_database(cls._DATABASE['Askar_Filter_Wheel_7x_M54'])

    @classmethod
    def Sharpstar_Filter_Wheel_5x_M42(cls):
        return cls.from_database(cls._DATABASE['Sharpstar_Filter_Wheel_5x_M42'])

    @classmethod
    def Sharpstar_Filter_Wheel_7x_M48(cls):
        return cls.from_database(cls._DATABASE['Sharpstar_Filter_Wheel_7x_M48'])

    @classmethod
    def Altair_Filter_Wheel_5x_M42(cls):
        return cls.from_database(cls._DATABASE['Altair_Filter_Wheel_5x_M42'])

    @classmethod
    def Altair_Filter_Wheel_7x_M48(cls):
        return cls.from_database(cls._DATABASE['Altair_Filter_Wheel_7x_M48'])

    @classmethod
    def Altair_Filter_Wheel_7x_M54(cls):
        return cls.from_database(cls._DATABASE['Altair_Filter_Wheel_7x_M54'])

    @classmethod
    def Omegon_Filter_Wheel_5x_M42(cls):
        return cls.from_database(cls._DATABASE['Omegon_Filter_Wheel_5x_M42'])

    @classmethod
    def Omegon_Filter_Wheel_7x_M48(cls):
        return cls.from_database(cls._DATABASE['Omegon_Filter_Wheel_7x_M48'])

    @classmethod
    def Lacerta_Filter_Wheel_5x_M42(cls):
        return cls.from_database(cls._DATABASE['Lacerta_Filter_Wheel_5x_M42'])

    @classmethod
    def Lacerta_Filter_Wheel_7x_M48(cls):
        return cls.from_database(cls._DATABASE['Lacerta_Filter_Wheel_7x_M48'])

    @classmethod
    def Lacerta_Filter_Wheel_7x_M54(cls):
        return cls.from_database(cls._DATABASE['Lacerta_Filter_Wheel_7x_M54'])

    @classmethod
    def Bresser_Filter_Wheel_5x_M42(cls):
        return cls.from_database(cls._DATABASE['Bresser_Filter_Wheel_5x_M42'])

    @classmethod
    def Bresser_Filter_Wheel_7x_M48(cls):
        return cls.from_database(cls._DATABASE['Bresser_Filter_Wheel_7x_M48'])

    @classmethod
    def OGMA_OGC_FW5_M48(cls):
        return cls.from_database(cls._DATABASE['OGMA_OGC_FW5_M48'])

    @classmethod
    def OGMA_OGC_FW9_M54(cls):
        return cls.from_database(cls._DATABASE['OGMA_OGC_FW9_M54'])

    @classmethod
    def Vixen_Filter_Wheel_5x_M42(cls):
        return cls.from_database(cls._DATABASE['Vixen_Filter_Wheel_5x_M42'])

    @classmethod
    def Explore_Scientific_Filter_Wheel_5x_M42(cls):
        return cls.from_database(cls._DATABASE['Explore_Scientific_Filter_Wheel_5x_M42'])

    @classmethod
    def Explore_Scientific_Filter_Wheel_7x_M48(cls):
        return cls.from_database(cls._DATABASE['Explore_Scientific_Filter_Wheel_7x_M48'])

    @classmethod
    def SVBony_SV222_FW_5x1_25_M42(cls):
        return cls.from_database(cls._DATABASE['SVBony_SV222_FW_5x1_25_M42'])

    @classmethod
    def SVBony_SV222_FW_7x_M48(cls):
        return cls.from_database(cls._DATABASE['SVBony_SV222_FW_7x_M48'])

    @classmethod
    def Orion_Nautilus_5x_M42(cls):
        return cls.from_database(cls._DATABASE['Orion_Nautilus_5x_M42'])

    @classmethod
    def Orion_Nautilus_7x_M48(cls):
        return cls.from_database(cls._DATABASE['Orion_Nautilus_7x_M48'])

    @classmethod
    def Meade_Series_6000_FW_M42(cls):
        return cls.from_database(cls._DATABASE['Meade_Series_6000_FW_M42'])

    @classmethod
    def Celestron_Filter_Wheel_5x_M42(cls):
        return cls.from_database(cls._DATABASE['Celestron_Filter_Wheel_5x_M42'])

    @classmethod
    def Celestron_Filter_Wheel_7x_M48(cls):
        return cls.from_database(cls._DATABASE['Celestron_Filter_Wheel_7x_M48'])

    @classmethod
    def Rising_Cam_Filter_Wheel_5x_M42(cls):
        return cls.from_database(cls._DATABASE['Rising_Cam_Filter_Wheel_5x_M42'])

    @classmethod
    def Rising_Cam_Filter_Wheel_7x_M48(cls):
        return cls.from_database(cls._DATABASE['Rising_Cam_Filter_Wheel_7x_M48'])

    @classmethod
    def Starlight_Xpress_SX_Maxi_Wheel_M68(cls):
        return cls.from_database(cls._DATABASE['Starlight_Xpress_SX_Maxi_Wheel_M68'])

    @classmethod
    def Moravian_EFW_2H_M42(cls):
        return cls.from_database(cls._DATABASE['Moravian_EFW_2H_M42'])

    @classmethod
    def Moravian_EFW_3H_M54(cls):
        return cls.from_database(cls._DATABASE['Moravian_EFW_3H_M54'])

    @classmethod
    def FLI_CenterLine_M42(cls):
        return cls.from_database(cls._DATABASE['FLI_CenterLine_M42'])

    @classmethod
    def FLI_CenterLine_M68(cls):
        return cls.from_database(cls._DATABASE['FLI_CenterLine_M68'])

class FilterHolder(IntermediateOpticalEquipment):
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
    def __init__(self, vendor, optical_length=0, mass=0, in_connection_type=None, out_connection_type=None, in_gender=None, out_gender=None):
        super(FilterHolder, self).__init__(
            vendor, optical_length=optical_length, mass=mass,
            in_connection_type=in_connection_type, out_connection_type=out_connection_type,
            in_gender=in_gender, out_gender=out_gender
        )
        self._type = OpticalType.FILTER_HOLDER

    _DATABASE = {
        'ZWO_Filter_Drawer_M48': {'brand': 'ZWO', 'name': 'Filter Drawer (M48)', 'type': 'type_filter_holder', 'optical_length': 26.5, 'mass': 220, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''},
        'ZWO_Filter_Drawer_M54': {'brand': 'ZWO', 'name': 'Filter Drawer (M54)', 'type': 'type_filter_holder', 'optical_length': 26.5, 'mass': 250, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''},
        'ZWO_Filter_Drawer_EOS_EF': {'brand': 'ZWO', 'name': 'Filter Drawer EOS-EF', 'type': 'type_filter_holder', 'optical_length': 26.5, 'mass': 230, 'tside_thread': 'EOS', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''},
        'Baader_Filter_Slider_M48': {'brand': 'Baader', 'name': 'Filter Slider (M48)', 'type': 'type_filter_holder', 'optical_length': 8, 'mass': 150, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''},
        'Baader_Filter_Slider_M54': {'brand': 'Baader', 'name': 'Filter Slider (M54)', 'type': 'type_filter_holder', 'optical_length': 8, 'mass': 170, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''},
        'Baader_Filter_Slider_M42': {'brand': 'Baader', 'name': 'Filter Slider (M42)', 'type': 'type_filter_holder', 'optical_length': 8, 'mass': 130, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''},
        'Baader_2_Filter_Holder': {'brand': 'Baader', 'name': '2" Filter Holder', 'type': 'type_filter_holder', 'optical_length': 10, 'mass': 100, 'tside_thread': '2"', 'tside_gender': 'Female', 'cside_thread': '2"', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''},
        'TS_Optics_Filter_Drawer_M48': {'brand': 'TS-Optics', 'name': 'Filter Drawer (M48)', 'type': 'type_filter_holder', 'optical_length': 25, 'mass': 200, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''},
        'TS_Optics_Filter_Drawer_M54': {'brand': 'TS-Optics', 'name': 'Filter Drawer (M54)', 'type': 'type_filter_holder', 'optical_length': 25, 'mass': 230, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''},
        'Celestron_Filter_Slide_1_25': {'brand': 'Celestron', 'name': 'Filter Slide 1.25"', 'type': 'type_filter_holder', 'optical_length': 8, 'mass': 100, 'tside_thread': '1.25"', 'tside_gender': 'Female', 'cside_thread': '1.25"', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''},
        'Astronomik_Filter_Drawer_M48': {'brand': 'Astronomik', 'name': 'Filter Drawer (M48)', 'type': 'type_filter_holder', 'optical_length': 25, 'mass': 200, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''},
        'Astronomik_Filter_Drawer_M54': {'brand': 'Astronomik', 'name': 'Filter Drawer (M54)', 'type': 'type_filter_holder', 'optical_length': 25, 'mass': 230, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''},
        'IDAS_Filter_Holder_M48': {'brand': 'IDAS', 'name': 'Filter Holder (M48)', 'type': 'type_filter_holder', 'optical_length': 8, 'mass': 120, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''},
        'Optolong_Filter_Drawer_M48': {'brand': 'Optolong', 'name': 'Filter Drawer (M48)', 'type': 'type_filter_holder', 'optical_length': 25, 'mass': 210, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''},
        'Optolong_Filter_Drawer_M54': {'brand': 'Optolong', 'name': 'Filter Drawer (M54)', 'type': 'type_filter_holder', 'optical_length': 25, 'mass': 240, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''},
        'Pegasus_Filter_Drawer_M48': {'brand': 'Pegasus', 'name': 'Filter Drawer (M48)', 'type': 'type_filter_holder', 'optical_length': 25, 'mass': 200, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''},
        'Pegasus_Filter_Drawer_M54': {'brand': 'Pegasus', 'name': 'Filter Drawer (M54)', 'type': 'type_filter_holder', 'optical_length': 25, 'mass': 230, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''},
        'Player_One_Filter_Drawer_M48': {'brand': 'Player One', 'name': 'Filter Drawer (M48)', 'type': 'type_filter_holder', 'optical_length': 25, 'mass': 190, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''},
        'Player_One_Filter_Drawer_M54': {'brand': 'Player One', 'name': 'Filter Drawer (M54)', 'type': 'type_filter_holder', 'optical_length': 25, 'mass': 220, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''},
        'Altair_Filter_Drawer_M48': {'brand': 'Altair', 'name': 'Filter Drawer (M48)', 'type': 'type_filter_holder', 'optical_length': 25, 'mass': 200, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''},
        'Altair_Filter_Drawer_M54': {'brand': 'Altair', 'name': 'Filter Drawer (M54)', 'type': 'type_filter_holder', 'optical_length': 25, 'mass': 230, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''},
        'SVBony_Filter_Drawer_M42': {'brand': 'SVBony', 'name': 'Filter Drawer (M42)', 'type': 'type_filter_holder', 'optical_length': 20, 'mass': 150, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''},
        'Lacerta_Filter_Drawer_M48': {'brand': 'Lacerta', 'name': 'Filter Drawer (M48)', 'type': 'type_filter_holder', 'optical_length': 25, 'mass': 200, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''},
        'Lacerta_Filter_Drawer_M54': {'brand': 'Lacerta', 'name': 'Filter Drawer (M54)', 'type': 'type_filter_holder', 'optical_length': 25, 'mass': 230, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''},
    }

    @classmethod
    def ZWO_Filter_Drawer_M48(cls):
        return cls.from_database(cls._DATABASE['ZWO_Filter_Drawer_M48'])

    @classmethod
    def ZWO_Filter_Drawer_M54(cls):
        return cls.from_database(cls._DATABASE['ZWO_Filter_Drawer_M54'])

    @classmethod
    def ZWO_Filter_Drawer_EOS_EF(cls):
        return cls.from_database(cls._DATABASE['ZWO_Filter_Drawer_EOS_EF'])

    @classmethod
    def Baader_Filter_Slider_M48(cls):
        return cls.from_database(cls._DATABASE['Baader_Filter_Slider_M48'])

    @classmethod
    def Baader_Filter_Slider_M54(cls):
        return cls.from_database(cls._DATABASE['Baader_Filter_Slider_M54'])

    @classmethod
    def Baader_Filter_Slider_M42(cls):
        return cls.from_database(cls._DATABASE['Baader_Filter_Slider_M42'])

    @classmethod
    def Baader_2_Filter_Holder(cls):
        return cls.from_database(cls._DATABASE['Baader_2_Filter_Holder'])

    @classmethod
    def TS_Optics_Filter_Drawer_M48(cls):
        return cls.from_database(cls._DATABASE['TS_Optics_Filter_Drawer_M48'])

    @classmethod
    def TS_Optics_Filter_Drawer_M54(cls):
        return cls.from_database(cls._DATABASE['TS_Optics_Filter_Drawer_M54'])

    @classmethod
    def Celestron_Filter_Slide_1_25(cls):
        return cls.from_database(cls._DATABASE['Celestron_Filter_Slide_1_25'])

    @classmethod
    def Astronomik_Filter_Drawer_M48(cls):
        return cls.from_database(cls._DATABASE['Astronomik_Filter_Drawer_M48'])

    @classmethod
    def Astronomik_Filter_Drawer_M54(cls):
        return cls.from_database(cls._DATABASE['Astronomik_Filter_Drawer_M54'])

    @classmethod
    def IDAS_Filter_Holder_M48(cls):
        return cls.from_database(cls._DATABASE['IDAS_Filter_Holder_M48'])

    @classmethod
    def Optolong_Filter_Drawer_M48(cls):
        return cls.from_database(cls._DATABASE['Optolong_Filter_Drawer_M48'])

    @classmethod
    def Optolong_Filter_Drawer_M54(cls):
        return cls.from_database(cls._DATABASE['Optolong_Filter_Drawer_M54'])

    @classmethod
    def Pegasus_Filter_Drawer_M48(cls):
        return cls.from_database(cls._DATABASE['Pegasus_Filter_Drawer_M48'])

    @classmethod
    def Pegasus_Filter_Drawer_M54(cls):
        return cls.from_database(cls._DATABASE['Pegasus_Filter_Drawer_M54'])

    @classmethod
    def Player_One_Filter_Drawer_M48(cls):
        return cls.from_database(cls._DATABASE['Player_One_Filter_Drawer_M48'])

    @classmethod
    def Player_One_Filter_Drawer_M54(cls):
        return cls.from_database(cls._DATABASE['Player_One_Filter_Drawer_M54'])

    @classmethod
    def Altair_Filter_Drawer_M48(cls):
        return cls.from_database(cls._DATABASE['Altair_Filter_Drawer_M48'])

    @classmethod
    def Altair_Filter_Drawer_M54(cls):
        return cls.from_database(cls._DATABASE['Altair_Filter_Drawer_M54'])

    @classmethod
    def SVBony_Filter_Drawer_M42(cls):
        return cls.from_database(cls._DATABASE['SVBony_Filter_Drawer_M42'])

    @classmethod
    def Lacerta_Filter_Drawer_M48(cls):
        return cls.from_database(cls._DATABASE['Lacerta_Filter_Drawer_M48'])

    @classmethod
    def Lacerta_Filter_Drawer_M54(cls):
        return cls.from_database(cls._DATABASE['Lacerta_Filter_Drawer_M54'])
