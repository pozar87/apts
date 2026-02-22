from .abstract import IntermediateOpticalEquipment
from ..constants import OpticalType
from ..units import get_unit_registry
from ..utils import Gender, ConnectionType

class Reducer(IntermediateOpticalEquipment):
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
        mag = Utils.extract_number(name, suffix="x") or 0.8
        return cls(
            vendor,
            magnification=mag,
            optical_length=ol,
            mass=mass,
            required_backfocus=55,
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
        mag = Utils.extract_number(name, suffix="x") or 0.8
        return cls(
            vendor,
            magnification=mag,
            optical_length=ol,
            mass=mass,
            required_backfocus=55,
            in_connection_type=tt,
            out_connection_type=ct,
            in_gender=tg or Gender.MALE,
            out_gender=cg or Gender.FEMALE,
        )
    def __init__(
        self, vendor, magnification=0.8, optical_length=0, mass=0, required_backfocus=None,
        in_connection_type=None, out_connection_type=None, in_gender=Gender.MALE, out_gender=Gender.FEMALE
    ):
        super(Reducer, self).__init__(
            vendor, optical_length=optical_length, mass=mass,
            in_connection_type=in_connection_type, out_connection_type=out_connection_type,
            in_gender=in_gender, out_gender=out_gender
        )
        self._type = OpticalType.REDUCER
        self.magnification = magnification
        self.required_backfocus = (
            required_backfocus * get_unit_registry().mm
            if required_backfocus is not None
            else None
        )



    _DATABASE = {
        'Celestron_f_6_3_Reducer_Corrector': {'brand': 'Celestron', 'name': 'f/6.3 Reducer/Corrector', 'type': 'type_reducer', 'optical_length': 0, 'mass': 200, 'tside_thread': 'SC (Schmidt-Cassegrain)', 'tside_gender': 'Female', 'cside_thread': 'SC (Schmidt-Cassegrain)', 'cside_gender': 'Female', 'reversible': False, 'bf_role': 'start'},
        'Celestron_0_7x_EdgeHD_Reducer_C6_C8_C9_25': {'brand': 'Celestron', 'name': '0.7x EdgeHD Reducer (C6/C8/C9.25)', 'type': 'type_reducer', 'optical_length': 0, 'mass': 300, 'tside_thread': 'SC (Schmidt-Cassegrain)', 'tside_gender': 'Female', 'cside_thread': 'SC (Schmidt-Cassegrain)', 'cside_gender': 'Female', 'reversible': False, 'bf_role': 'start'},
        'Celestron_0_7x_EdgeHD_Reducer_C11_C14': {'brand': 'Celestron', 'name': '0.7x EdgeHD Reducer (C11/C14)', 'type': 'type_reducer', 'optical_length': 0, 'mass': 400, 'tside_thread': 'SC (Schmidt-Cassegrain)', 'tside_gender': 'Female', 'cside_thread': 'SC (Schmidt-Cassegrain)', 'cside_gender': 'Female', 'reversible': False, 'bf_role': 'start'},
        'Celestron_f_7_Reducer_NexStar': {'brand': 'Celestron', 'name': 'f/7 Reducer (NexStar)', 'type': 'type_reducer', 'optical_length': 0, 'mass': 150, 'tside_thread': 'SC (Schmidt-Cassegrain)', 'tside_gender': 'Female', 'cside_thread': 'SC (Schmidt-Cassegrain)', 'cside_gender': 'Female', 'reversible': False, 'bf_role': 'start'},
        'Celestron_0_63x_Reducer_Meade_compat': {'brand': 'Celestron', 'name': '0.63x Reducer (Meade compat.)', 'type': 'type_reducer', 'optical_length': 0, 'mass': 200, 'tside_thread': 'SC (Schmidt-Cassegrain)', 'tside_gender': 'Female', 'cside_thread': 'SC (Schmidt-Cassegrain)', 'cside_gender': 'Female', 'reversible': False, 'bf_role': 'start'},
        'Sky_Watcher_0_85x_Reducer_Esprit': {'brand': 'Sky-Watcher', 'name': '0.85x Reducer (Esprit)', 'type': 'type_reducer', 'optical_length': 0, 'mass': 250, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Female', 'reversible': False, 'bf_role': 'start'},
        'Sky_Watcher_0_77x_Reducer_Evostar': {'brand': 'Sky-Watcher', 'name': '0.77x Reducer (Evostar)', 'type': 'type_reducer', 'optical_length': 0, 'mass': 200, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Female', 'reversible': False, 'bf_role': 'start'},
        'Sky_Watcher_0_85x_Reducer_Flattener_ED': {'brand': 'Sky-Watcher', 'name': '0.85x Reducer/Flattener (ED)', 'type': 'type_reducer', 'optical_length': 0, 'mass': 220, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Female', 'reversible': False, 'bf_role': 'start'},
        'Takahashi_QE_0_73x_Reducer_FSQ': {'brand': 'Takahashi', 'name': 'QE 0.73x Reducer (FSQ)', 'type': 'type_reducer', 'optical_length': 0, 'mass': 350, 'tside_thread': 'M82', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Female', 'reversible': False, 'bf_role': 'start'},
        'Takahashi_645_Reducer_0_72x_FSQ': {'brand': 'Takahashi', 'name': '645 Reducer 0.72x (FSQ)', 'type': 'type_reducer', 'optical_length': 0, 'mass': 500, 'tside_thread': 'M82', 'tside_gender': 'Female', 'cside_thread': 'M82', 'cside_gender': 'Female', 'reversible': False, 'bf_role': 'start'},
        'Takahashi_TOA_35_Reducer_0_7x': {'brand': 'Takahashi', 'name': 'TOA-35 Reducer 0.7x', 'type': 'type_reducer', 'optical_length': 0, 'mass': 400, 'tside_thread': 'M72', 'tside_gender': 'Female', 'cside_thread': 'M72', 'cside_gender': 'Female', 'reversible': False, 'bf_role': 'start'},
        'Takahashi_FC_35_Reducer_0_66x': {'brand': 'Takahashi', 'name': 'FC-35 Reducer 0.66x', 'type': 'type_reducer', 'optical_length': 0, 'mass': 250, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Female', 'reversible': False, 'bf_role': 'start'},
        'Takahashi_Multi_Reducer_0_85x_S_FS_60': {'brand': 'Takahashi', 'name': 'Multi Reducer 0.85x-S (FS-60)', 'type': 'type_reducer', 'optical_length': 0, 'mass': 200, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Female', 'reversible': False, 'bf_role': 'start'},
        'Takahashi_Multi_Reducer_0_85x_M_FCT_65': {'brand': 'Takahashi', 'name': 'Multi Reducer 0.85x-M (FCT-65)', 'type': 'type_reducer', 'optical_length': 0, 'mass': 200, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Female', 'reversible': False, 'bf_role': 'start'},
        'Takahashi_Multi_Reducer_0_85x_L_FC_76': {'brand': 'Takahashi', 'name': 'Multi Reducer 0.85x-L (FC-76)', 'type': 'type_reducer', 'optical_length': 0, 'mass': 200, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Female', 'reversible': False, 'bf_role': 'start'},
        'Takahashi_76D_Reducer_FC_76_FC_100': {'brand': 'Takahashi', 'name': '76D Reducer (FC-76/FC-100)', 'type': 'type_reducer', 'optical_length': 0, 'mass': 190, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Female', 'reversible': False, 'bf_role': 'start'},
        'Takahashi_Focal_Reducer_C_0_72x_FS_60': {'brand': 'Takahashi', 'name': 'Focal Reducer-C 0.72x (FS-60)', 'type': 'type_reducer', 'optical_length': 0, 'mass': 180, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Female', 'reversible': False, 'bf_role': 'start'},
        'Takahashi_Flattener_Reducer_SKY_90': {'brand': 'Takahashi', 'name': 'Flattener-Reducer (SKY-90)', 'type': 'type_reducer', 'optical_length': 0, 'mass': 200, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Female', 'reversible': False, 'bf_role': 'start'},
        'Takahashi_Reducer_Corrector_0_8x_Mewlon': {'brand': 'Takahashi', 'name': 'Reducer-Corrector 0.8x (Mewlon)', 'type': 'type_reducer', 'optical_length': 0, 'mass': 350, 'tside_thread': 'M72', 'tside_gender': 'Female', 'cside_thread': 'M72', 'cside_gender': 'Female', 'reversible': False, 'bf_role': 'start'},
        'Takahashi_Reducer_CR_0_73x_CCA_Mewlon_CRS': {'brand': 'Takahashi', 'name': 'Reducer-CR 0.73x (CCA/Mewlon CRS)', 'type': 'type_reducer', 'optical_length': 0, 'mass': 500, 'tside_thread': 'M92', 'tside_gender': 'Female', 'cside_thread': 'M82', 'cside_gender': 'Female', 'reversible': False, 'bf_role': 'start'},
        'Takahashi_F3_Reducer_0_6x_FSQ_106ED': {'brand': 'Takahashi', 'name': 'F3 Reducer 0.6x (FSQ-106ED)', 'type': 'type_reducer', 'optical_length': 0, 'mass': 600, 'tside_thread': 'M82', 'tside_gender': 'Female', 'cside_thread': 'M82', 'cside_gender': 'Female', 'reversible': False, 'bf_role': 'start'},
        'Takahashi_645_Reducer_CA_0_72x_CCA_250': {'brand': 'Takahashi', 'name': '645 Reducer-CA 0.72x (CCA-250)', 'type': 'type_reducer', 'optical_length': 0, 'mass': 700, 'tside_thread': 'M92', 'tside_gender': 'Female', 'cside_thread': 'M82', 'cside_gender': 'Female', 'reversible': False, 'bf_role': 'start'},
        'Starizona_SCT_Corrector_IV_0_63x': {'brand': 'Starizona', 'name': 'SCT Corrector IV (0.63x)', 'type': 'type_reducer', 'optical_length': 0, 'mass': 300, 'tside_thread': 'SC (Schmidt-Cassegrain)', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Female', 'reversible': False, 'bf_role': 'start'},
        'Starizona_HyperStar_C8_0_2x': {'brand': 'Starizona', 'name': 'HyperStar C8 (0.2x)', 'type': 'type_reducer', 'optical_length': 0, 'mass': 400, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M42', 'cside_gender': 'Female', 'reversible': False, 'bf_role': ''},
        'Starizona_HyperStar_C11_0_2x': {'brand': 'Starizona', 'name': 'HyperStar C11 (0.2x)', 'type': 'type_reducer', 'optical_length': 0, 'mass': 500, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M48', 'cside_gender': 'Female', 'reversible': False, 'bf_role': ''},
        'Starizona_HyperStar_C14_0_2x': {'brand': 'Starizona', 'name': 'HyperStar C14 (0.2x)', 'type': 'type_reducer', 'optical_length': 0, 'mass': 600, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M48', 'cside_gender': 'Female', 'reversible': False, 'bf_role': ''},
        'Starizona_Night_Owl_0_4x': {'brand': 'Starizona', 'name': 'Night Owl 0.4x', 'type': 'type_reducer', 'optical_length': 0, 'mass': 600, 'tside_thread': 'SC (Schmidt-Cassegrain)', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Female', 'reversible': False, 'bf_role': 'start'},
        'Starizona_Apex_ED_0_65x_M42': {'brand': 'Starizona', 'name': 'Apex ED 0.65x (M42)', 'type': 'type_reducer', 'optical_length': 0, 'mass': 250, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Female', 'reversible': False, 'bf_role': 'start'},
        'Baader_Alan_Gee_II_Telecompressor': {'brand': 'Baader', 'name': 'Alan Gee II Telecompressor', 'type': 'type_reducer', 'optical_length': 0, 'mass': 200, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Female', 'reversible': False, 'bf_role': 'start'},
        'Riccardi_APO_Reducer_0_75x_M72': {'brand': 'Riccardi', 'name': 'APO Reducer 0.75x (M72)', 'type': 'type_reducer', 'optical_length': 19.8, 'mass': 500, 'tside_thread': 'M72', 'tside_gender': 'Female', 'cside_thread': 'M68', 'cside_gender': 'Female', 'reversible': False, 'bf_role': 'start'},
        'Riccardi_Reducer_0_72x_M82': {'brand': 'Riccardi', 'name': 'Reducer 0.72x (M82)', 'type': 'type_reducer', 'optical_length': 0, 'mass': 550, 'tside_thread': 'M82', 'tside_gender': 'Female', 'cside_thread': 'M68', 'cside_gender': 'Female', 'reversible': False, 'bf_role': 'start'},
        'Riccardi_Reducer_0_75x_M68': {'brand': 'Riccardi', 'name': 'Reducer 0.75x (M68)', 'type': 'type_reducer', 'optical_length': 0, 'mass': 480, 'tside_thread': 'M68', 'tside_gender': 'Female', 'cside_thread': 'M68', 'cside_gender': 'Female', 'reversible': False, 'bf_role': 'start'},
        'William_Optics_Reducer_Flat_0_8x': {'brand': 'William Optics', 'name': 'Reducer Flat 0.8x', 'type': 'type_reducer', 'optical_length': 0, 'mass': 300, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Female', 'reversible': False, 'bf_role': 'start'},
        'William_Optics_AFR_IV_0_8x': {'brand': 'William Optics', 'name': 'AFR-IV 0.8x', 'type': 'type_reducer', 'optical_length': 0, 'mass': 320, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Female', 'reversible': False, 'bf_role': 'start'},
        'Askar_0_7x_Reducer_FRA_series': {'brand': 'Askar', 'name': '0.7x Reducer (FRA series)', 'type': 'type_reducer', 'optical_length': 0, 'mass': 200, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Female', 'reversible': False, 'bf_role': 'start'},
        'Askar_103APO_Reducer_0_6x': {'brand': 'Askar', 'name': '103APO Reducer 0.6x', 'type': 'type_reducer', 'optical_length': 0, 'mass': 300, 'tside_thread': 'M68', 'tside_gender': 'Female', 'cside_thread': 'M68', 'cside_gender': 'Female', 'reversible': False, 'bf_role': 'start'},
        'Askar_151PHQ_Reducer_0_7x': {'brand': 'Askar', 'name': '151PHQ Reducer 0.7x', 'type': 'type_reducer', 'optical_length': 0, 'mass': 350, 'tside_thread': 'M68', 'tside_gender': 'Female', 'cside_thread': 'M68', 'cside_gender': 'Female', 'reversible': False, 'bf_role': 'start'},
        'Askar_0_76x_Reducer_PHQ': {'brand': 'Askar', 'name': '0.76x Reducer (PHQ)', 'type': 'type_reducer', 'optical_length': 0, 'mass': 280, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Female', 'reversible': False, 'bf_role': 'start'},
        'Sharpstar_0_8x_Reducer_EDPH': {'brand': 'Sharpstar', 'name': '0.8x Reducer (EDPH)', 'type': 'type_reducer', 'optical_length': 0, 'mass': 250, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Female', 'reversible': False, 'bf_role': 'start'},
        'Sharpstar_0_7x_Reducer_EDPH': {'brand': 'Sharpstar', 'name': '0.7x Reducer (EDPH)', 'type': 'type_reducer', 'optical_length': 0, 'mass': 260, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Female', 'reversible': False, 'bf_role': 'start'},
        'TS_Optics_TSRED3_0_79x_Reducer': {'brand': 'TS-Optics', 'name': 'TSRED3 0.79x Reducer', 'type': 'type_reducer', 'optical_length': 0, 'mass': 300, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Female', 'reversible': False, 'bf_role': 'start'},
        'TS_Optics_0_8x_Reducer_M48': {'brand': 'TS-Optics', 'name': '0.8x Reducer (M48)', 'type': 'type_reducer', 'optical_length': 0, 'mass': 200, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Female', 'reversible': False, 'bf_role': 'start'},
        'TS_Optics_TSRED2_0_6x_Reducer': {'brand': 'TS-Optics', 'name': 'TSRED2 0.6x Reducer', 'type': 'type_reducer', 'optical_length': 0, 'mass': 280, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Female', 'reversible': False, 'bf_role': 'start'},
        'TeleVue_0_8x_Reducer': {'brand': 'TeleVue', 'name': '0.8x Reducer', 'type': 'type_reducer', 'optical_length': 0, 'mass': 200, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Female', 'reversible': False, 'bf_role': 'start'},
        'TeleVue_TRF_2008_0_8x': {'brand': 'TeleVue', 'name': 'TRF-2008 0.8x', 'type': 'type_reducer', 'optical_length': 0, 'mass': 250, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Female', 'reversible': False, 'bf_role': 'start'},
        'Explore_Scientific_0_7x_Reducer': {'brand': 'Explore Scientific', 'name': '0.7x Reducer', 'type': 'type_reducer', 'optical_length': 0, 'mass': 280, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Female', 'reversible': False, 'bf_role': 'start'},
        'Astro_Physics_CCDT67_Telecompressor': {'brand': 'Astro-Physics', 'name': 'CCDT67 Telecompressor', 'type': 'type_reducer', 'optical_length': 0, 'mass': 200, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Female', 'reversible': False, 'bf_role': 'start'},
        'Astro_Physics_0_67x_Reducer_130GTX': {'brand': 'Astro-Physics', 'name': '0.67x Reducer (130GTX)', 'type': 'type_reducer', 'optical_length': 0, 'mass': 300, 'tside_thread': 'M68', 'tside_gender': 'Female', 'cside_thread': 'M68', 'cside_gender': 'Female', 'reversible': False, 'bf_role': 'start'},
        'Astro_Physics_0_72x_Reducer': {'brand': 'Astro-Physics', 'name': '0.72x Reducer', 'type': 'type_reducer', 'optical_length': 0, 'mass': 320, 'tside_thread': 'M68', 'tside_gender': 'Female', 'cside_thread': 'M68', 'cside_gender': 'Female', 'reversible': False, 'bf_role': 'start'},
        'Meade_f_6_3_Reducer_Corrector': {'brand': 'Meade', 'name': 'f/6.3 Reducer/Corrector', 'type': 'type_reducer', 'optical_length': 0, 'mass': 200, 'tside_thread': 'SC (Schmidt-Cassegrain)', 'tside_gender': 'Female', 'cside_thread': 'SC (Schmidt-Cassegrain)', 'cside_gender': 'Female', 'reversible': False, 'bf_role': 'start'},
        'Meade_f_3_3_Reducer': {'brand': 'Meade', 'name': 'f/3.3 Reducer', 'type': 'type_reducer', 'optical_length': 0, 'mass': 300, 'tside_thread': 'SC (Schmidt-Cassegrain)', 'tside_gender': 'Female', 'cside_thread': 'SC (Schmidt-Cassegrain)', 'cside_gender': 'Female', 'reversible': False, 'bf_role': 'start'},
        'APM_Riccardi_Design_0_75x': {'brand': 'APM', 'name': 'Riccardi-Design 0.75x', 'type': 'type_reducer', 'optical_length': 0, 'mass': 450, 'tside_thread': 'M72', 'tside_gender': 'Female', 'cside_thread': 'M68', 'cside_gender': 'Female', 'reversible': False, 'bf_role': 'start'},
        'Lacerta_0_8x_Reducer_M48': {'brand': 'Lacerta', 'name': '0.8x Reducer (M48)', 'type': 'type_reducer', 'optical_length': 0, 'mass': 220, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Female', 'reversible': False, 'bf_role': 'start'},
        'Stellarvue_SFFR_72_130_Reducer': {'brand': 'Stellarvue', 'name': 'SFFR.72-130 Reducer', 'type': 'type_reducer', 'optical_length': 0, 'mass': 350, 'tside_thread': 'M68', 'tside_gender': 'Female', 'cside_thread': 'M68', 'cside_gender': 'Female', 'reversible': False, 'bf_role': 'start'},
        'Stellarvue_SVR102_Reducer_0_72x': {'brand': 'Stellarvue', 'name': 'SVR102 Reducer 0.72x', 'type': 'type_reducer', 'optical_length': 0, 'mass': 280, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Female', 'reversible': False, 'bf_role': 'start'},
        'Borg_Reducer_0_72x_M57': {'brand': 'Borg', 'name': 'Reducer 0.72x (M57)', 'type': 'type_reducer', 'optical_length': 0, 'mass': 200, 'tside_thread': 'M56', 'tside_gender': 'Female', 'cside_thread': 'M56', 'cside_gender': 'Female', 'reversible': False, 'bf_role': 'start'},
        'Vixen_SD_Reducer_HD': {'brand': 'Vixen', 'name': 'SD Reducer HD', 'type': 'type_reducer', 'optical_length': 0, 'mass': 250, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Female', 'reversible': False, 'bf_role': 'start'},
        'Orion_0_85x_Reducer': {'brand': 'Orion', 'name': '0.85x Reducer', 'type': 'type_reducer', 'optical_length': 0, 'mass': 220, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Female', 'reversible': False, 'bf_role': 'start'},
        'Omegon_0_8x_Reducer_M48': {'brand': 'Omegon', 'name': '0.8x Reducer (M48)', 'type': 'type_reducer', 'optical_length': 0, 'mass': 220, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Female', 'reversible': False, 'bf_role': 'start'},
        'SVBony_SV196_0_8x_Reducer': {'brand': 'SVBony', 'name': 'SV196 0.8x Reducer', 'type': 'type_reducer', 'optical_length': 0, 'mass': 220, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Female', 'reversible': False, 'bf_role': 'start'},
        'Saxon_0_85x_Reducer_M48': {'brand': 'Saxon', 'name': '0.85x Reducer (M48)', 'type': 'type_reducer', 'optical_length': 0, 'mass': 200, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Female', 'reversible': False, 'bf_role': 'start'},
        'Altair_0_8x_Reducer_M48': {'brand': 'Altair', 'name': '0.8x Reducer (M48)', 'type': 'type_reducer', 'optical_length': 0, 'mass': 250, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Female', 'reversible': False, 'bf_role': 'start'},
        'Sky_Watcher_0_9x_Reducer_Esprit_150': {'brand': 'Sky-Watcher', 'name': '0.9x Reducer (Esprit 150)', 'type': 'type_reducer', 'optical_length': 0, 'mass': 300, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Female', 'reversible': False, 'bf_role': 'start'},
        'Celestron_EdgeHD_0_7x_Reducer_C8': {'brand': 'Celestron', 'name': 'EdgeHD 0.7x Reducer (C8)', 'type': 'type_reducer', 'optical_length': 0, 'mass': 300, 'tside_thread': 'SC (Schmidt-Cassegrain)', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Female', 'reversible': False, 'bf_role': 'start'},
        'Meade_Series_4000_0_33x_Reducer': {'brand': 'Meade', 'name': 'Series 4000 0.33x Reducer', 'type': 'type_reducer', 'optical_length': 0, 'mass': 150, 'tside_thread': 'SC (Schmidt-Cassegrain)', 'tside_gender': 'Female', 'cside_thread': 'SC (Schmidt-Cassegrain)', 'cside_gender': 'Female', 'reversible': False, 'bf_role': 'start'},
        'Askar_0_7x_Reducer_65PHQ': {'brand': 'Askar', 'name': '0.7x Reducer (65PHQ)', 'type': 'type_reducer', 'optical_length': 0, 'mass': 200, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Female', 'reversible': False, 'bf_role': 'start'},
        'Askar_0_76x_Reducer_80PHQ': {'brand': 'Askar', 'name': '0.76x Reducer (80PHQ)', 'type': 'type_reducer', 'optical_length': 0, 'mass': 250, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Female', 'reversible': False, 'bf_role': 'start'},
        'Askar_0_7x_Reducer_107PHQ': {'brand': 'Askar', 'name': '0.7x Reducer (107PHQ)', 'type': 'type_reducer', 'optical_length': 0, 'mass': 300, 'tside_thread': 'M68', 'tside_gender': 'Female', 'cside_thread': 'M68', 'cside_gender': 'Female', 'reversible': False, 'bf_role': 'start'},
        'Askar_0_6x_Reducer_FRA400': {'brand': 'Askar', 'name': '0.6x Reducer (FRA400)', 'type': 'type_reducer', 'optical_length': 0, 'mass': 220, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Female', 'reversible': False, 'bf_role': 'start'},
        'Sharpstar_0_74x_Reducer_94EDPH': {'brand': 'Sharpstar', 'name': '0.74x Reducer (94EDPH)', 'type': 'type_reducer', 'optical_length': 0, 'mass': 280, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Female', 'reversible': False, 'bf_role': 'start'},
        'Sharpstar_0_8x_Reducer_140PH': {'brand': 'Sharpstar', 'name': '0.8x Reducer (140PH)', 'type': 'type_reducer', 'optical_length': 0, 'mass': 350, 'tside_thread': 'M68', 'tside_gender': 'Female', 'cside_thread': 'M68', 'cside_gender': 'Female', 'reversible': False, 'bf_role': 'start'},
        'Stellarvue_SVR80_102_Reducer': {'brand': 'Stellarvue', 'name': 'SVR80-102 Reducer', 'type': 'type_reducer', 'optical_length': 0, 'mass': 260, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Female', 'reversible': False, 'bf_role': 'start'},
        'TS_Optics_TSRED4_0_67x_Reducer': {'brand': 'TS-Optics', 'name': 'TSRED4 0.67x Reducer', 'type': 'type_reducer', 'optical_length': 0, 'mass': 300, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Female', 'reversible': False, 'bf_role': 'start'},
        'Explore_Scientific_0_7x_Reducer_2': {'brand': 'Explore Scientific', 'name': '0.7x Reducer (2")', 'type': 'type_reducer', 'optical_length': 0, 'mass': 300, 'tside_thread': '2"', 'tside_gender': 'Female', 'cside_thread': '2"', 'cside_gender': 'Female', 'reversible': False, 'bf_role': 'start'},
        'William_Optics_Flat61R': {'brand': 'William Optics', 'name': 'Flat61R', 'type': 'type_reducer', 'optical_length': 0, 'mass': 200, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Female', 'reversible': False, 'bf_role': 'start'},
        'William_Optics_RedCat_Reducer_0_8x': {'brand': 'William Optics', 'name': 'RedCat Reducer 0.8x', 'type': 'type_reducer', 'optical_length': 0, 'mass': 200, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Female', 'reversible': False, 'bf_role': 'start'},
        'Generic_0_63x_M42': {'brand': 'Generic', 'name': '0.63x (M42)', 'type': 'type_reducer', 'optical_length': 0, 'mass': 200, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Female', 'reversible': False, 'bf_role': 'start'},
        'Generic_0_63x_M48': {'brand': 'Generic', 'name': '0.63x (M48)', 'type': 'type_reducer', 'optical_length': 0, 'mass': 200, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Female', 'reversible': False, 'bf_role': 'start'},
        'Generic_0_63x_M54': {'brand': 'Generic', 'name': '0.63x (M54)', 'type': 'type_reducer', 'optical_length': 0, 'mass': 200, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Female', 'reversible': False, 'bf_role': 'start'},
        'Generic_0_63x_M68': {'brand': 'Generic', 'name': '0.63x (M68)', 'type': 'type_reducer', 'optical_length': 0, 'mass': 200, 'tside_thread': 'M68', 'tside_gender': 'Female', 'cside_thread': 'M68', 'cside_gender': 'Female', 'reversible': False, 'bf_role': 'start'},
        'Generic_0_72x_M42': {'brand': 'Generic', 'name': '0.72x (M42)', 'type': 'type_reducer', 'optical_length': 0, 'mass': 250, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Female', 'reversible': False, 'bf_role': 'start'},
        'Generic_0_72x_M48': {'brand': 'Generic', 'name': '0.72x (M48)', 'type': 'type_reducer', 'optical_length': 0, 'mass': 250, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Female', 'reversible': False, 'bf_role': 'start'},
        'Generic_0_72x_M54': {'brand': 'Generic', 'name': '0.72x (M54)', 'type': 'type_reducer', 'optical_length': 0, 'mass': 250, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Female', 'reversible': False, 'bf_role': 'start'},
        'Generic_0_72x_M68': {'brand': 'Generic', 'name': '0.72x (M68)', 'type': 'type_reducer', 'optical_length': 0, 'mass': 250, 'tside_thread': 'M68', 'tside_gender': 'Female', 'cside_thread': 'M68', 'cside_gender': 'Female', 'reversible': False, 'bf_role': 'start'},
        'Generic_0_79x_M42': {'brand': 'Generic', 'name': '0.79x (M42)', 'type': 'type_reducer', 'optical_length': 0, 'mass': 230, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Female', 'reversible': False, 'bf_role': 'start'},
        'Generic_0_79x_M48': {'brand': 'Generic', 'name': '0.79x (M48)', 'type': 'type_reducer', 'optical_length': 0, 'mass': 230, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Female', 'reversible': False, 'bf_role': 'start'},
        'Generic_0_79x_M54': {'brand': 'Generic', 'name': '0.79x (M54)', 'type': 'type_reducer', 'optical_length': 0, 'mass': 230, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Female', 'reversible': False, 'bf_role': 'start'},
        'Generic_0_79x_M68': {'brand': 'Generic', 'name': '0.79x (M68)', 'type': 'type_reducer', 'optical_length': 0, 'mass': 230, 'tside_thread': 'M68', 'tside_gender': 'Female', 'cside_thread': 'M68', 'cside_gender': 'Female', 'reversible': False, 'bf_role': 'start'},
        'Generic_0_85x_M42': {'brand': 'Generic', 'name': '0.85x (M42)', 'type': 'type_reducer', 'optical_length': 0, 'mass': 210, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Female', 'reversible': False, 'bf_role': 'start'},
        'Generic_0_85x_M48': {'brand': 'Generic', 'name': '0.85x (M48)', 'type': 'type_reducer', 'optical_length': 0, 'mass': 210, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Female', 'reversible': False, 'bf_role': 'start'},
        'Generic_0_85x_M54': {'brand': 'Generic', 'name': '0.85x (M54)', 'type': 'type_reducer', 'optical_length': 0, 'mass': 210, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Female', 'reversible': False, 'bf_role': 'start'},
        'Generic_0_85x_M68': {'brand': 'Generic', 'name': '0.85x (M68)', 'type': 'type_reducer', 'optical_length': 0, 'mass': 210, 'tside_thread': 'M68', 'tside_gender': 'Female', 'cside_thread': 'M68', 'cside_gender': 'Female', 'reversible': False, 'bf_role': 'start'},
        'Astro_Physics_92mm_Reducer_0_72x': {'brand': 'Astro-Physics', 'name': '92mm Reducer 0.72x', 'type': 'type_reducer', 'optical_length': 0, 'mass': 250, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Female', 'reversible': False, 'bf_role': 'start'},
        'Astro_Physics_Quad_TCC_4_Reducer': {'brand': 'Astro-Physics', 'name': 'Quad TCC (4" Reducer)', 'type': 'type_reducer', 'optical_length': 0, 'mass': 700, 'tside_thread': 'M68', 'tside_gender': 'Female', 'cside_thread': 'M68', 'cside_gender': 'Female', 'reversible': False, 'bf_role': 'start'},
        'Astro_Physics_27TVPH_Reducer_0_75x': {'brand': 'Astro-Physics', 'name': '27TVPH Reducer 0.75x', 'type': 'type_reducer', 'optical_length': 0, 'mass': 350, 'tside_thread': 'M68', 'tside_gender': 'Female', 'cside_thread': 'M68', 'cside_gender': 'Female', 'reversible': False, 'bf_role': 'start'},
        'TeleVue_TV_76_Reducer_0_8x': {'brand': 'TeleVue', 'name': 'TV-76 Reducer 0.8x', 'type': 'type_reducer', 'optical_length': 0, 'mass': 180, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Female', 'reversible': False, 'bf_role': 'start'},
        'TeleVue_TV_85_Reducer_0_8x': {'brand': 'TeleVue', 'name': 'TV-85 Reducer 0.8x', 'type': 'type_reducer', 'optical_length': 0, 'mass': 200, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Female', 'reversible': False, 'bf_role': 'start'},
        'Stellarvue_SVR80_Reducer_0_8x': {'brand': 'Stellarvue', 'name': 'SVR80 Reducer 0.8x', 'type': 'type_reducer', 'optical_length': 0, 'mass': 260, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Female', 'reversible': False, 'bf_role': 'start'},
        'Stellarvue_SFFR_72_80_Reducer': {'brand': 'Stellarvue', 'name': 'SFFR.72-80 Reducer', 'type': 'type_reducer', 'optical_length': 0, 'mass': 280, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Female', 'reversible': False, 'bf_role': 'start'},
        'Stellarvue_SFFR_72_102_Reducer': {'brand': 'Stellarvue', 'name': 'SFFR.72-102 Reducer', 'type': 'type_reducer', 'optical_length': 0, 'mass': 300, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Female', 'reversible': False, 'bf_role': 'start'},
        'TEC_TEC_140_Reducer_0_72x': {'brand': 'TEC', 'name': 'TEC-140 Reducer 0.72x', 'type': 'type_reducer', 'optical_length': 0, 'mass': 350, 'tside_thread': 'M68', 'tside_gender': 'Female', 'cside_thread': 'M68', 'cside_gender': 'Female', 'reversible': False, 'bf_role': 'start'},
        'TEC_TEC_180_Reducer_0_72x': {'brand': 'TEC', 'name': 'TEC-180 Reducer 0.72x', 'type': 'type_reducer', 'optical_length': 0, 'mass': 450, 'tside_thread': 'M68', 'tside_gender': 'Female', 'cside_thread': 'M68', 'cside_gender': 'Female', 'reversible': False, 'bf_role': 'start'},
        'Borg_0_85x_Reducer_M57': {'brand': 'Borg', 'name': '0.85x Reducer (M57)', 'type': 'type_reducer', 'optical_length': 0, 'mass': 200, 'tside_thread': 'M56', 'tside_gender': 'Female', 'cside_thread': 'M56', 'cside_gender': 'Female', 'reversible': False, 'bf_role': 'start'},
        'PlaneWave_0_66x_Reducer_CDK14': {'brand': 'PlaneWave', 'name': '0.66x Reducer (CDK14)', 'type': 'type_reducer', 'optical_length': 0, 'mass': 900, 'tside_thread': 'M117', 'tside_gender': 'Female', 'cside_thread': 'M117', 'cside_gender': 'Female', 'reversible': False, 'bf_role': 'start'},
        'Officina_Stellare_RC_Corrector_0_75x_M68': {'brand': 'Officina Stellare', 'name': 'RC Corrector 0.75x (M68)', 'type': 'type_reducer', 'optical_length': 0, 'mass': 500, 'tside_thread': 'M68', 'tside_gender': 'Female', 'cside_thread': 'M68', 'cside_gender': 'Female', 'reversible': False, 'bf_role': 'start'},
        'Altair_Lightwave_0_8x_Reducer': {'brand': 'Altair', 'name': 'Lightwave 0.8x Reducer', 'type': 'type_reducer', 'optical_length': 0, 'mass': 220, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Female', 'reversible': False, 'bf_role': 'start'},
        'Altair_0_6x_Reducer_M48': {'brand': 'Altair', 'name': '0.6x Reducer (M48)', 'type': 'type_reducer', 'optical_length': 0, 'mass': 280, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Female', 'reversible': False, 'bf_role': 'start'},
        'SVBony_0_8x_Reducer_M42': {'brand': 'SVBony', 'name': '0.8x Reducer (M42)', 'type': 'type_reducer', 'optical_length': 0, 'mass': 150, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Female', 'reversible': False, 'bf_role': 'start'},
        'Bresser_0_8x_Reducer_M48': {'brand': 'Bresser', 'name': '0.8x Reducer (M48)', 'type': 'type_reducer', 'optical_length': 0, 'mass': 200, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Female', 'reversible': False, 'bf_role': 'start'},
        'Lacerta_0_72x_Reducer_M48': {'brand': 'Lacerta', 'name': '0.72x Reducer (M48)', 'type': 'type_reducer', 'optical_length': 0, 'mass': 250, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Female', 'reversible': False, 'bf_role': 'start'},
        'Tecnosky_0_8x_Reducer_M48': {'brand': 'Tecnosky', 'name': '0.8x Reducer (M48)', 'type': 'type_reducer', 'optical_length': 0, 'mass': 220, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Female', 'reversible': False, 'bf_role': 'start'},
        'CFF_0_65x_Reducer_M117': {'brand': 'CFF', 'name': '0.65x Reducer (M117)', 'type': 'type_reducer', 'optical_length': 0, 'mass': 500, 'tside_thread': 'M117', 'tside_gender': 'Female', 'cside_thread': 'M117', 'cside_gender': 'Female', 'reversible': False, 'bf_role': 'start'},
        'Long_Perng_0_79x_Reducer_M48': {'brand': 'Long Perng', 'name': '0.79x Reducer (M48)', 'type': 'type_reducer', 'optical_length': 0, 'mass': 200, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Female', 'reversible': False, 'bf_role': 'start'},
        'Orion_0_5x_Focal_Reducer': {'brand': 'Orion', 'name': '0.5x Focal Reducer', 'type': 'type_reducer', 'optical_length': 0, 'mass': 300, 'tside_thread': '1.25"', 'tside_gender': 'Female', 'cside_thread': '1.25"', 'cside_gender': 'Female', 'reversible': False, 'bf_role': 'start'},
    }

    @classmethod
    def Celestron_f_6_3_Reducer_Corrector(cls):
        return cls.from_database(cls._DATABASE['Celestron_f_6_3_Reducer_Corrector'])

    @classmethod
    def Celestron_0_7x_EdgeHD_Reducer_C6_C8_C9_25(cls):
        return cls.from_database(cls._DATABASE['Celestron_0_7x_EdgeHD_Reducer_C6_C8_C9_25'])

    @classmethod
    def Celestron_0_7x_EdgeHD_Reducer_C11_C14(cls):
        return cls.from_database(cls._DATABASE['Celestron_0_7x_EdgeHD_Reducer_C11_C14'])

    @classmethod
    def Celestron_f_7_Reducer_NexStar(cls):
        return cls.from_database(cls._DATABASE['Celestron_f_7_Reducer_NexStar'])

    @classmethod
    def Celestron_0_63x_Reducer_Meade_compat(cls):
        return cls.from_database(cls._DATABASE['Celestron_0_63x_Reducer_Meade_compat'])

    @classmethod
    def Sky_Watcher_0_85x_Reducer_Esprit(cls):
        return cls.from_database(cls._DATABASE['Sky_Watcher_0_85x_Reducer_Esprit'])

    @classmethod
    def Sky_Watcher_0_77x_Reducer_Evostar(cls):
        return cls.from_database(cls._DATABASE['Sky_Watcher_0_77x_Reducer_Evostar'])

    @classmethod
    def Sky_Watcher_0_85x_Reducer_Flattener_ED(cls):
        return cls.from_database(cls._DATABASE['Sky_Watcher_0_85x_Reducer_Flattener_ED'])

    @classmethod
    def Takahashi_QE_0_73x_Reducer_FSQ(cls):
        return cls.from_database(cls._DATABASE['Takahashi_QE_0_73x_Reducer_FSQ'])

    @classmethod
    def Takahashi_645_Reducer_0_72x_FSQ(cls):
        return cls.from_database(cls._DATABASE['Takahashi_645_Reducer_0_72x_FSQ'])

    @classmethod
    def Takahashi_TOA_35_Reducer_0_7x(cls):
        return cls.from_database(cls._DATABASE['Takahashi_TOA_35_Reducer_0_7x'])

    @classmethod
    def Takahashi_FC_35_Reducer_0_66x(cls):
        return cls.from_database(cls._DATABASE['Takahashi_FC_35_Reducer_0_66x'])

    @classmethod
    def Takahashi_Multi_Reducer_0_85x_S_FS_60(cls):
        return cls.from_database(cls._DATABASE['Takahashi_Multi_Reducer_0_85x_S_FS_60'])

    @classmethod
    def Takahashi_Multi_Reducer_0_85x_M_FCT_65(cls):
        return cls.from_database(cls._DATABASE['Takahashi_Multi_Reducer_0_85x_M_FCT_65'])

    @classmethod
    def Takahashi_Multi_Reducer_0_85x_L_FC_76(cls):
        return cls.from_database(cls._DATABASE['Takahashi_Multi_Reducer_0_85x_L_FC_76'])

    @classmethod
    def Takahashi_76D_Reducer_FC_76_FC_100(cls):
        return cls.from_database(cls._DATABASE['Takahashi_76D_Reducer_FC_76_FC_100'])

    @classmethod
    def Takahashi_Focal_Reducer_C_0_72x_FS_60(cls):
        return cls.from_database(cls._DATABASE['Takahashi_Focal_Reducer_C_0_72x_FS_60'])

    @classmethod
    def Takahashi_Flattener_Reducer_SKY_90(cls):
        return cls.from_database(cls._DATABASE['Takahashi_Flattener_Reducer_SKY_90'])

    @classmethod
    def Takahashi_Reducer_Corrector_0_8x_Mewlon(cls):
        return cls.from_database(cls._DATABASE['Takahashi_Reducer_Corrector_0_8x_Mewlon'])

    @classmethod
    def Takahashi_Reducer_CR_0_73x_CCA_Mewlon_CRS(cls):
        return cls.from_database(cls._DATABASE['Takahashi_Reducer_CR_0_73x_CCA_Mewlon_CRS'])

    @classmethod
    def Takahashi_F3_Reducer_0_6x_FSQ_106ED(cls):
        return cls.from_database(cls._DATABASE['Takahashi_F3_Reducer_0_6x_FSQ_106ED'])

    @classmethod
    def Takahashi_645_Reducer_CA_0_72x_CCA_250(cls):
        return cls.from_database(cls._DATABASE['Takahashi_645_Reducer_CA_0_72x_CCA_250'])

    @classmethod
    def Starizona_SCT_Corrector_IV_0_63x(cls):
        return cls.from_database(cls._DATABASE['Starizona_SCT_Corrector_IV_0_63x'])

    @classmethod
    def Starizona_HyperStar_C8_0_2x(cls):
        return cls.from_database(cls._DATABASE['Starizona_HyperStar_C8_0_2x'])

    @classmethod
    def Starizona_HyperStar_C11_0_2x(cls):
        return cls.from_database(cls._DATABASE['Starizona_HyperStar_C11_0_2x'])

    @classmethod
    def Starizona_HyperStar_C14_0_2x(cls):
        return cls.from_database(cls._DATABASE['Starizona_HyperStar_C14_0_2x'])

    @classmethod
    def Starizona_Night_Owl_0_4x(cls):
        return cls.from_database(cls._DATABASE['Starizona_Night_Owl_0_4x'])

    @classmethod
    def Starizona_Apex_ED_0_65x_M42(cls):
        return cls.from_database(cls._DATABASE['Starizona_Apex_ED_0_65x_M42'])

    @classmethod
    def Baader_Alan_Gee_II_Telecompressor(cls):
        return cls.from_database(cls._DATABASE['Baader_Alan_Gee_II_Telecompressor'])

    @classmethod
    def Riccardi_APO_Reducer_0_75x_M72(cls):
        return cls.from_database(cls._DATABASE['Riccardi_APO_Reducer_0_75x_M72'])

    @classmethod
    def Riccardi_Reducer_0_72x_M82(cls):
        return cls.from_database(cls._DATABASE['Riccardi_Reducer_0_72x_M82'])

    @classmethod
    def Riccardi_Reducer_0_75x_M68(cls):
        return cls.from_database(cls._DATABASE['Riccardi_Reducer_0_75x_M68'])

    @classmethod
    def William_Optics_Reducer_Flat_0_8x(cls):
        return cls.from_database(cls._DATABASE['William_Optics_Reducer_Flat_0_8x'])

    @classmethod
    def William_Optics_AFR_IV_0_8x(cls):
        return cls.from_database(cls._DATABASE['William_Optics_AFR_IV_0_8x'])

    @classmethod
    def Askar_0_7x_Reducer_FRA_series(cls):
        return cls.from_database(cls._DATABASE['Askar_0_7x_Reducer_FRA_series'])

    @classmethod
    def Askar_103APO_Reducer_0_6x(cls):
        return cls.from_database(cls._DATABASE['Askar_103APO_Reducer_0_6x'])

    @classmethod
    def Askar_151PHQ_Reducer_0_7x(cls):
        return cls.from_database(cls._DATABASE['Askar_151PHQ_Reducer_0_7x'])

    @classmethod
    def Askar_0_76x_Reducer_PHQ(cls):
        return cls.from_database(cls._DATABASE['Askar_0_76x_Reducer_PHQ'])

    @classmethod
    def Sharpstar_0_8x_Reducer_EDPH(cls):
        return cls.from_database(cls._DATABASE['Sharpstar_0_8x_Reducer_EDPH'])

    @classmethod
    def Sharpstar_0_7x_Reducer_EDPH(cls):
        return cls.from_database(cls._DATABASE['Sharpstar_0_7x_Reducer_EDPH'])

    @classmethod
    def TS_Optics_TSRED3_0_79x_Reducer(cls):
        return cls.from_database(cls._DATABASE['TS_Optics_TSRED3_0_79x_Reducer'])

    @classmethod
    def TS_Optics_0_8x_Reducer_M48(cls):
        return cls.from_database(cls._DATABASE['TS_Optics_0_8x_Reducer_M48'])

    @classmethod
    def TS_Optics_TSRED2_0_6x_Reducer(cls):
        return cls.from_database(cls._DATABASE['TS_Optics_TSRED2_0_6x_Reducer'])

    @classmethod
    def TeleVue_0_8x_Reducer(cls):
        return cls.from_database(cls._DATABASE['TeleVue_0_8x_Reducer'])

    @classmethod
    def TeleVue_TRF_2008_0_8x(cls):
        return cls.from_database(cls._DATABASE['TeleVue_TRF_2008_0_8x'])

    @classmethod
    def Explore_Scientific_0_7x_Reducer(cls):
        return cls.from_database(cls._DATABASE['Explore_Scientific_0_7x_Reducer'])

    @classmethod
    def Astro_Physics_CCDT67_Telecompressor(cls):
        return cls.from_database(cls._DATABASE['Astro_Physics_CCDT67_Telecompressor'])

    @classmethod
    def Astro_Physics_0_67x_Reducer_130GTX(cls):
        return cls.from_database(cls._DATABASE['Astro_Physics_0_67x_Reducer_130GTX'])

    @classmethod
    def Astro_Physics_0_72x_Reducer(cls):
        return cls.from_database(cls._DATABASE['Astro_Physics_0_72x_Reducer'])

    @classmethod
    def Meade_f_6_3_Reducer_Corrector(cls):
        return cls.from_database(cls._DATABASE['Meade_f_6_3_Reducer_Corrector'])

    @classmethod
    def Meade_f_3_3_Reducer(cls):
        return cls.from_database(cls._DATABASE['Meade_f_3_3_Reducer'])

    @classmethod
    def APM_Riccardi_Design_0_75x(cls):
        return cls.from_database(cls._DATABASE['APM_Riccardi_Design_0_75x'])

    @classmethod
    def Lacerta_0_8x_Reducer_M48(cls):
        return cls.from_database(cls._DATABASE['Lacerta_0_8x_Reducer_M48'])

    @classmethod
    def Stellarvue_SFFR_72_130_Reducer(cls):
        return cls.from_database(cls._DATABASE['Stellarvue_SFFR_72_130_Reducer'])

    @classmethod
    def Stellarvue_SVR102_Reducer_0_72x(cls):
        return cls.from_database(cls._DATABASE['Stellarvue_SVR102_Reducer_0_72x'])

    @classmethod
    def Borg_Reducer_0_72x_M57(cls):
        return cls.from_database(cls._DATABASE['Borg_Reducer_0_72x_M57'])

    @classmethod
    def Vixen_SD_Reducer_HD(cls):
        return cls.from_database(cls._DATABASE['Vixen_SD_Reducer_HD'])

    @classmethod
    def Orion_0_85x_Reducer(cls):
        return cls.from_database(cls._DATABASE['Orion_0_85x_Reducer'])

    @classmethod
    def Omegon_0_8x_Reducer_M48(cls):
        return cls.from_database(cls._DATABASE['Omegon_0_8x_Reducer_M48'])

    @classmethod
    def SVBony_SV196_0_8x_Reducer(cls):
        return cls.from_database(cls._DATABASE['SVBony_SV196_0_8x_Reducer'])

    @classmethod
    def Saxon_0_85x_Reducer_M48(cls):
        return cls.from_database(cls._DATABASE['Saxon_0_85x_Reducer_M48'])

    @classmethod
    def Altair_0_8x_Reducer_M48(cls):
        return cls.from_database(cls._DATABASE['Altair_0_8x_Reducer_M48'])

    @classmethod
    def Sky_Watcher_0_9x_Reducer_Esprit_150(cls):
        return cls.from_database(cls._DATABASE['Sky_Watcher_0_9x_Reducer_Esprit_150'])

    @classmethod
    def Celestron_EdgeHD_0_7x_Reducer_C8(cls):
        return cls.from_database(cls._DATABASE['Celestron_EdgeHD_0_7x_Reducer_C8'])

    @classmethod
    def Meade_Series_4000_0_33x_Reducer(cls):
        return cls.from_database(cls._DATABASE['Meade_Series_4000_0_33x_Reducer'])

    @classmethod
    def Askar_0_7x_Reducer_65PHQ(cls):
        return cls.from_database(cls._DATABASE['Askar_0_7x_Reducer_65PHQ'])

    @classmethod
    def Askar_0_76x_Reducer_80PHQ(cls):
        return cls.from_database(cls._DATABASE['Askar_0_76x_Reducer_80PHQ'])

    @classmethod
    def Askar_0_7x_Reducer_107PHQ(cls):
        return cls.from_database(cls._DATABASE['Askar_0_7x_Reducer_107PHQ'])

    @classmethod
    def Askar_0_6x_Reducer_FRA400(cls):
        return cls.from_database(cls._DATABASE['Askar_0_6x_Reducer_FRA400'])

    @classmethod
    def Sharpstar_0_74x_Reducer_94EDPH(cls):
        return cls.from_database(cls._DATABASE['Sharpstar_0_74x_Reducer_94EDPH'])

    @classmethod
    def Sharpstar_0_8x_Reducer_140PH(cls):
        return cls.from_database(cls._DATABASE['Sharpstar_0_8x_Reducer_140PH'])

    @classmethod
    def Stellarvue_SVR80_102_Reducer(cls):
        return cls.from_database(cls._DATABASE['Stellarvue_SVR80_102_Reducer'])

    @classmethod
    def TS_Optics_TSRED4_0_67x_Reducer(cls):
        return cls.from_database(cls._DATABASE['TS_Optics_TSRED4_0_67x_Reducer'])

    @classmethod
    def Explore_Scientific_0_7x_Reducer_2(cls):
        return cls.from_database(cls._DATABASE['Explore_Scientific_0_7x_Reducer_2'])

    @classmethod
    def William_Optics_Flat61R(cls):
        return cls.from_database(cls._DATABASE['William_Optics_Flat61R'])

    @classmethod
    def William_Optics_RedCat_Reducer_0_8x(cls):
        return cls.from_database(cls._DATABASE['William_Optics_RedCat_Reducer_0_8x'])

    @classmethod
    def Generic_0_63x_M42(cls):
        return cls.from_database(cls._DATABASE['Generic_0_63x_M42'])

    @classmethod
    def Generic_0_63x_M48(cls):
        return cls.from_database(cls._DATABASE['Generic_0_63x_M48'])

    @classmethod
    def Generic_0_63x_M54(cls):
        return cls.from_database(cls._DATABASE['Generic_0_63x_M54'])

    @classmethod
    def Generic_0_63x_M68(cls):
        return cls.from_database(cls._DATABASE['Generic_0_63x_M68'])

    @classmethod
    def Generic_0_72x_M42(cls):
        return cls.from_database(cls._DATABASE['Generic_0_72x_M42'])

    @classmethod
    def Generic_0_72x_M48(cls):
        return cls.from_database(cls._DATABASE['Generic_0_72x_M48'])

    @classmethod
    def Generic_0_72x_M54(cls):
        return cls.from_database(cls._DATABASE['Generic_0_72x_M54'])

    @classmethod
    def Generic_0_72x_M68(cls):
        return cls.from_database(cls._DATABASE['Generic_0_72x_M68'])

    @classmethod
    def Generic_0_79x_M42(cls):
        return cls.from_database(cls._DATABASE['Generic_0_79x_M42'])

    @classmethod
    def Generic_0_79x_M48(cls):
        return cls.from_database(cls._DATABASE['Generic_0_79x_M48'])

    @classmethod
    def Generic_0_79x_M54(cls):
        return cls.from_database(cls._DATABASE['Generic_0_79x_M54'])

    @classmethod
    def Generic_0_79x_M68(cls):
        return cls.from_database(cls._DATABASE['Generic_0_79x_M68'])

    @classmethod
    def Generic_0_85x_M42(cls):
        return cls.from_database(cls._DATABASE['Generic_0_85x_M42'])

    @classmethod
    def Generic_0_85x_M48(cls):
        return cls.from_database(cls._DATABASE['Generic_0_85x_M48'])

    @classmethod
    def Generic_0_85x_M54(cls):
        return cls.from_database(cls._DATABASE['Generic_0_85x_M54'])

    @classmethod
    def Generic_0_85x_M68(cls):
        return cls.from_database(cls._DATABASE['Generic_0_85x_M68'])

    @classmethod
    def Astro_Physics_92mm_Reducer_0_72x(cls):
        return cls.from_database(cls._DATABASE['Astro_Physics_92mm_Reducer_0_72x'])

    @classmethod
    def Astro_Physics_Quad_TCC_4_Reducer(cls):
        return cls.from_database(cls._DATABASE['Astro_Physics_Quad_TCC_4_Reducer'])

    @classmethod
    def Astro_Physics_27TVPH_Reducer_0_75x(cls):
        return cls.from_database(cls._DATABASE['Astro_Physics_27TVPH_Reducer_0_75x'])

    @classmethod
    def TeleVue_TV_76_Reducer_0_8x(cls):
        return cls.from_database(cls._DATABASE['TeleVue_TV_76_Reducer_0_8x'])

    @classmethod
    def TeleVue_TV_85_Reducer_0_8x(cls):
        return cls.from_database(cls._DATABASE['TeleVue_TV_85_Reducer_0_8x'])

    @classmethod
    def Stellarvue_SVR80_Reducer_0_8x(cls):
        return cls.from_database(cls._DATABASE['Stellarvue_SVR80_Reducer_0_8x'])

    @classmethod
    def Stellarvue_SFFR_72_80_Reducer(cls):
        return cls.from_database(cls._DATABASE['Stellarvue_SFFR_72_80_Reducer'])

    @classmethod
    def Stellarvue_SFFR_72_102_Reducer(cls):
        return cls.from_database(cls._DATABASE['Stellarvue_SFFR_72_102_Reducer'])

    @classmethod
    def TEC_TEC_140_Reducer_0_72x(cls):
        return cls.from_database(cls._DATABASE['TEC_TEC_140_Reducer_0_72x'])

    @classmethod
    def TEC_TEC_180_Reducer_0_72x(cls):
        return cls.from_database(cls._DATABASE['TEC_TEC_180_Reducer_0_72x'])

    @classmethod
    def Borg_0_85x_Reducer_M57(cls):
        return cls.from_database(cls._DATABASE['Borg_0_85x_Reducer_M57'])

    @classmethod
    def PlaneWave_0_66x_Reducer_CDK14(cls):
        return cls.from_database(cls._DATABASE['PlaneWave_0_66x_Reducer_CDK14'])

    @classmethod
    def Officina_Stellare_RC_Corrector_0_75x_M68(cls):
        return cls.from_database(cls._DATABASE['Officina_Stellare_RC_Corrector_0_75x_M68'])

    @classmethod
    def Altair_Lightwave_0_8x_Reducer(cls):
        return cls.from_database(cls._DATABASE['Altair_Lightwave_0_8x_Reducer'])

    @classmethod
    def Altair_0_6x_Reducer_M48(cls):
        return cls.from_database(cls._DATABASE['Altair_0_6x_Reducer_M48'])

    @classmethod
    def SVBony_0_8x_Reducer_M42(cls):
        return cls.from_database(cls._DATABASE['SVBony_0_8x_Reducer_M42'])

    @classmethod
    def Bresser_0_8x_Reducer_M48(cls):
        return cls.from_database(cls._DATABASE['Bresser_0_8x_Reducer_M48'])

    @classmethod
    def Lacerta_0_72x_Reducer_M48(cls):
        return cls.from_database(cls._DATABASE['Lacerta_0_72x_Reducer_M48'])

    @classmethod
    def Tecnosky_0_8x_Reducer_M48(cls):
        return cls.from_database(cls._DATABASE['Tecnosky_0_8x_Reducer_M48'])

    @classmethod
    def CFF_0_65x_Reducer_M117(cls):
        return cls.from_database(cls._DATABASE['CFF_0_65x_Reducer_M117'])

    @classmethod
    def Long_Perng_0_79x_Reducer_M48(cls):
        return cls.from_database(cls._DATABASE['Long_Perng_0_79x_Reducer_M48'])

    @classmethod
    def Orion_0_5x_Focal_Reducer(cls):
        return cls.from_database(cls._DATABASE['Orion_0_5x_Focal_Reducer'])

class Flattener(IntermediateOpticalEquipment):
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
        mag = 1.0
        return cls(
            vendor,
            magnification=mag,
            optical_length=ol,
            mass=mass,
            required_backfocus=55,
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
        mag = 1.0
        return cls(
            vendor,
            magnification=mag,
            optical_length=ol,
            mass=mass,
            required_backfocus=55,
            in_connection_type=tt,
            out_connection_type=ct,
            in_gender=tg or Gender.MALE,
            out_gender=cg or Gender.FEMALE,
        )
    def __init__(
        self, vendor, magnification=1.0, optical_length=0, mass=0, required_backfocus=None,
        in_connection_type=None, out_connection_type=None, in_gender=Gender.MALE, out_gender=Gender.FEMALE
    ):
        super(Flattener, self).__init__(
            vendor, optical_length=optical_length, mass=mass,
            in_connection_type=in_connection_type, out_connection_type=out_connection_type,
            in_gender=in_gender, out_gender=out_gender
        )
        self._type = OpticalType.FLATTENER
        self.magnification = magnification
        self.required_backfocus = (
            required_backfocus * get_unit_registry().mm
            if required_backfocus is not None
            else None
        )


    _DATABASE = {
        'Sky_Watcher_Evostar_Flattener': {'brand': 'Sky-Watcher', 'name': 'Evostar Flattener', 'type': 'type_flattener', 'optical_length': 0, 'mass': 200, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Female', 'reversible': False, 'bf_role': 'start'},
        'Sky_Watcher_Esprit_Flattener': {'brand': 'Sky-Watcher', 'name': 'Esprit Flattener', 'type': 'type_flattener', 'optical_length': 0, 'mass': 250, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Female', 'reversible': False, 'bf_role': 'start'},
        'Takahashi_Flattener_1_01x_FSQ': {'brand': 'Takahashi', 'name': 'Flattener 1.01x (FSQ)', 'type': 'type_flattener', 'optical_length': 0, 'mass': 300, 'tside_thread': 'M82', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Female', 'reversible': False, 'bf_role': 'start'},
        'Takahashi_TOA_35FL_Flattener': {'brand': 'Takahashi', 'name': 'TOA-35FL Flattener', 'type': 'type_flattener', 'optical_length': 0, 'mass': 350, 'tside_thread': 'M72', 'tside_gender': 'Female', 'cside_thread': 'M72', 'cside_gender': 'Female', 'reversible': False, 'bf_role': 'start'},
        'Takahashi_FC_Flattener': {'brand': 'Takahashi', 'name': 'FC Flattener', 'type': 'type_flattener', 'optical_length': 0, 'mass': 200, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Female', 'reversible': False, 'bf_role': 'start'},
        'Takahashi_Multi_Flattener_1_04x_FC_FS': {'brand': 'Takahashi', 'name': 'Multi Flattener 1.04x (FC/FS)', 'type': 'type_flattener', 'optical_length': 0, 'mass': 110, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Female', 'reversible': False, 'bf_role': 'start'},
        'Takahashi_Flattener_0_93x_FOA_60': {'brand': 'Takahashi', 'name': 'Flattener 0.93x (FOA-60)', 'type': 'type_flattener', 'optical_length': 0, 'mass': 150, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Female', 'reversible': False, 'bf_role': 'start'},
        'Takahashi_TOA_645_FL_Flattener_TOA_130': {'brand': 'Takahashi', 'name': 'TOA-645 FL Flattener (TOA-130)', 'type': 'type_flattener', 'optical_length': 0, 'mass': 400, 'tside_thread': 'M72', 'tside_gender': 'Female', 'cside_thread': 'M72', 'cside_gender': 'Female', 'reversible': False, 'bf_role': 'start'},
        'Takahashi_TOA_645_FL_Flattener_TOA_150': {'brand': 'Takahashi', 'name': 'TOA-645 FL Flattener (TOA-150)', 'type': 'type_flattener', 'optical_length': 0, 'mass': 500, 'tside_thread': 'M92', 'tside_gender': 'Female', 'cside_thread': 'M92', 'cside_gender': 'Female', 'reversible': False, 'bf_role': 'start'},
        'Riccardi_Flattener_M54': {'brand': 'Riccardi', 'name': 'Flattener (M54)', 'type': 'type_flattener', 'optical_length': 0, 'mass': 300, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Female', 'reversible': False, 'bf_role': 'start'},
        'William_Optics_Flat68_III': {'brand': 'William Optics', 'name': 'Flat68 III', 'type': 'type_flattener', 'optical_length': 0, 'mass': 250, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Female', 'reversible': False, 'bf_role': 'start'},
        'William_Optics_P_FLAT_68': {'brand': 'William Optics', 'name': 'P-FLAT 68', 'type': 'type_flattener', 'optical_length': 0, 'mass': 280, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Female', 'reversible': False, 'bf_role': 'start'},
        'William_Optics_P_FLAT_73': {'brand': 'William Optics', 'name': 'P-FLAT 73', 'type': 'type_flattener', 'optical_length': 0, 'mass': 290, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Female', 'reversible': False, 'bf_role': 'start'},
        'Askar_Full_frame_Flattener': {'brand': 'Askar', 'name': 'Full-frame Flattener', 'type': 'type_flattener', 'optical_length': 0, 'mass': 250, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Female', 'reversible': False, 'bf_role': 'start'},
        'Askar_2_Flattener_M48': {'brand': 'Askar', 'name': '2" Flattener (M48)', 'type': 'type_flattener', 'optical_length': 0, 'mass': 230, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Female', 'reversible': False, 'bf_role': 'start'},
        'Sharpstar_2_Field_Flattener': {'brand': 'Sharpstar', 'name': '2" Field Flattener', 'type': 'type_flattener', 'optical_length': 0, 'mass': 300, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Female', 'reversible': False, 'bf_role': 'start'},
        'TS_Optics_Flattener_2_M48': {'brand': 'TS-Optics', 'name': 'Flattener 2" (M48)', 'type': 'type_flattener', 'optical_length': 0, 'mass': 280, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Female', 'reversible': False, 'bf_role': 'start'},
        'TS_Optics_TSFlat2_M48': {'brand': 'TS-Optics', 'name': 'TSFlat2 (M48)', 'type': 'type_flattener', 'optical_length': 0, 'mass': 200, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Female', 'reversible': False, 'bf_role': 'start'},
        'TS_Optics_RC_Flattener_M68': {'brand': 'TS-Optics', 'name': 'RC Flattener (M68)', 'type': 'type_flattener', 'optical_length': 0, 'mass': 350, 'tside_thread': 'M68', 'tside_gender': 'Female', 'cside_thread': 'M68', 'cside_gender': 'Female', 'reversible': False, 'bf_role': 'start'},
        'Explore_Scientific_ED_Field_Flattener': {'brand': 'Explore Scientific', 'name': 'ED Field Flattener', 'type': 'type_flattener', 'optical_length': 0, 'mass': 250, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Female', 'reversible': False, 'bf_role': 'start'},
        'Astro_Physics_160FFAPO5_Flattener': {'brand': 'Astro-Physics', 'name': '160FFAPO5 Flattener', 'type': 'type_flattener', 'optical_length': 0, 'mass': 350, 'tside_thread': 'M68', 'tside_gender': 'Female', 'cside_thread': 'M68', 'cside_gender': 'Female', 'reversible': False, 'bf_role': 'start'},
        'Stellarvue_SVF25_Flattener': {'brand': 'Stellarvue', 'name': 'SVF25 Flattener', 'type': 'type_flattener', 'optical_length': 0, 'mass': 250, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Female', 'reversible': False, 'bf_role': 'start'},
        'Vixen_SD_Flattener_HD': {'brand': 'Vixen', 'name': 'SD Flattener HD', 'type': 'type_flattener', 'optical_length': 0, 'mass': 230, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Female', 'reversible': False, 'bf_role': 'start'},
        'Orion_Field_Flattener_M48': {'brand': 'Orion', 'name': 'Field Flattener (M48)', 'type': 'type_flattener', 'optical_length': 0, 'mass': 200, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Female', 'reversible': False, 'bf_role': 'start'},
        'Omegon_Field_Flattener_M48': {'brand': 'Omegon', 'name': 'Field Flattener (M48)', 'type': 'type_flattener', 'optical_length': 0, 'mass': 200, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Female', 'reversible': False, 'bf_role': 'start'},
        'Bresser_Field_Flattener_M48': {'brand': 'Bresser', 'name': 'Field Flattener (M48)', 'type': 'type_flattener', 'optical_length': 0, 'mass': 200, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Female', 'reversible': False, 'bf_role': 'start'},
        'Lacerta_2_Flattener_M48': {'brand': 'Lacerta', 'name': '2" Flattener (M48)', 'type': 'type_flattener', 'optical_length': 0, 'mass': 250, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Female', 'reversible': False, 'bf_role': 'start'},
        'GSO_2_Field_Flattener': {'brand': 'GSO', 'name': '2" Field Flattener', 'type': 'type_flattener', 'optical_length': 0, 'mass': 250, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Female', 'reversible': False, 'bf_role': 'start'},
        'Altair_Lightwave_Flattener_M48': {'brand': 'Altair', 'name': 'Lightwave Flattener (M48)', 'type': 'type_flattener', 'optical_length': 0, 'mass': 230, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Female', 'reversible': False, 'bf_role': 'start'},
        'Stellarvue_SVF25_78_Flattener': {'brand': 'Stellarvue', 'name': 'SVF25-78 Flattener', 'type': 'type_flattener', 'optical_length': 0, 'mass': 230, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Female', 'reversible': False, 'bf_role': 'start'},
        'Borg_Flattener_1_08x_M57': {'brand': 'Borg', 'name': 'Flattener 1.08x (M57)', 'type': 'type_flattener', 'optical_length': 0, 'mass': 180, 'tside_thread': 'M56', 'tside_gender': 'Female', 'cside_thread': 'M56', 'cside_gender': 'Female', 'reversible': False, 'bf_role': 'start'},
        'TS_Optics_TSFlat3_M54': {'brand': 'TS-Optics', 'name': 'TSFlat3 (M54)', 'type': 'type_flattener', 'optical_length': 0, 'mass': 250, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Female', 'reversible': False, 'bf_role': 'start'},
        'TS_Optics_TSFlat4_M68': {'brand': 'TS-Optics', 'name': 'TSFlat4 (M68)', 'type': 'type_flattener', 'optical_length': 0, 'mass': 350, 'tside_thread': 'M68', 'tside_gender': 'Female', 'cside_thread': 'M68', 'cside_gender': 'Female', 'reversible': False, 'bf_role': 'start'},
        'Generic_1_0x_Flattener_M42': {'brand': 'Generic', 'name': '1.0x Flattener (M42)', 'type': 'type_flattener', 'optical_length': 0, 'mass': 180, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Female', 'reversible': False, 'bf_role': 'start'},
        'Generic_1_0x_Flattener_M48': {'brand': 'Generic', 'name': '1.0x Flattener (M48)', 'type': 'type_flattener', 'optical_length': 0, 'mass': 180, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Female', 'reversible': False, 'bf_role': 'start'},
        'Generic_1_0x_Flattener_M54': {'brand': 'Generic', 'name': '1.0x Flattener (M54)', 'type': 'type_flattener', 'optical_length': 0, 'mass': 180, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Female', 'reversible': False, 'bf_role': 'start'},
        'Generic_1_0x_Flattener_M68': {'brand': 'Generic', 'name': '1.0x Flattener (M68)', 'type': 'type_flattener', 'optical_length': 0, 'mass': 180, 'tside_thread': 'M68', 'tside_gender': 'Female', 'cside_thread': 'M68', 'cside_gender': 'Female', 'reversible': False, 'bf_role': 'start'},
        'Astro_Physics_130GTX_Flattener': {'brand': 'Astro-Physics', 'name': '130GTX Flattener', 'type': 'type_flattener', 'optical_length': 0, 'mass': 280, 'tside_thread': 'M68', 'tside_gender': 'Female', 'cside_thread': 'M68', 'cside_gender': 'Female', 'reversible': False, 'bf_role': 'start'},
        'TeleVue_NP101_Flattener': {'brand': 'TeleVue', 'name': 'NP101 Flattener', 'type': 'type_flattener', 'optical_length': 0, 'mass': 250, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Female', 'reversible': False, 'bf_role': 'start'},
        'TeleVue_NP127_Flattener': {'brand': 'TeleVue', 'name': 'NP127 Flattener', 'type': 'type_flattener', 'optical_length': 0, 'mass': 280, 'tside_thread': 'M68', 'tside_gender': 'Female', 'cside_thread': 'M68', 'cside_gender': 'Female', 'reversible': False, 'bf_role': 'start'},
        'Stellarvue_SVF50_Flattener': {'brand': 'Stellarvue', 'name': 'SVF50 Flattener', 'type': 'type_flattener', 'optical_length': 0, 'mass': 220, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Female', 'reversible': False, 'bf_role': 'start'},
        'Stellarvue_SFF_Flattener_M68': {'brand': 'Stellarvue', 'name': 'SFF Flattener (M68)', 'type': 'type_flattener', 'optical_length': 0, 'mass': 280, 'tside_thread': 'M68', 'tside_gender': 'Female', 'cside_thread': 'M68', 'cside_gender': 'Female', 'reversible': False, 'bf_role': 'start'},
        'TEC_TEC_110_Flattener': {'brand': 'TEC', 'name': 'TEC-110 Flattener', 'type': 'type_flattener', 'optical_length': 0, 'mass': 280, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Female', 'reversible': False, 'bf_role': 'start'},
        'TEC_TEC_160_Flattener': {'brand': 'TEC', 'name': 'TEC-160 Flattener', 'type': 'type_flattener', 'optical_length': 0, 'mass': 400, 'tside_thread': 'M68', 'tside_gender': 'Female', 'cside_thread': 'M68', 'cside_gender': 'Female', 'reversible': False, 'bf_role': 'start'},
        'Borg_Multi_Flattener_M57': {'brand': 'Borg', 'name': 'Multi Flattener (M57)', 'type': 'type_flattener', 'optical_length': 0, 'mass': 250, 'tside_thread': 'M56', 'tside_gender': 'Female', 'cside_thread': 'M56', 'cside_gender': 'Female', 'reversible': False, 'bf_role': 'start'},
        'Borg_1_08x_Flattener_89ED': {'brand': 'Borg', 'name': '1.08x Flattener (89ED)', 'type': 'type_flattener', 'optical_length': 0, 'mass': 200, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Female', 'reversible': False, 'bf_role': 'start'},
        'Altair_Lightwave_Flattener': {'brand': 'Altair', 'name': 'Lightwave Flattener', 'type': 'type_flattener', 'optical_length': 0, 'mass': 200, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Female', 'reversible': False, 'bf_role': 'start'},
        'SVBony_SV193_Field_Flattener': {'brand': 'SVBony', 'name': 'SV193 Field Flattener', 'type': 'type_flattener', 'optical_length': 0, 'mass': 180, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Female', 'reversible': False, 'bf_role': 'start'},
        'Tecnosky_Field_Flattener_M48': {'brand': 'Tecnosky', 'name': 'Field Flattener (M48)', 'type': 'type_flattener', 'optical_length': 0, 'mass': 200, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Female', 'reversible': False, 'bf_role': 'start'},
        'Long_Perng_Field_Flattener_M48': {'brand': 'Long Perng', 'name': 'Field Flattener (M48)', 'type': 'type_flattener', 'optical_length': 0, 'mass': 180, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Female', 'reversible': False, 'bf_role': 'start'},
        'Meade_Series_6000_Field_Flattener': {'brand': 'Meade', 'name': 'Series 6000 Field Flattener', 'type': 'type_flattener', 'optical_length': 0, 'mass': 280, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Female', 'reversible': False, 'bf_role': 'start'},
    }

    @classmethod
    def Sky_Watcher_Evostar_Flattener(cls):
        return cls.from_database(cls._DATABASE['Sky_Watcher_Evostar_Flattener'])

    @classmethod
    def Sky_Watcher_Esprit_Flattener(cls):
        return cls.from_database(cls._DATABASE['Sky_Watcher_Esprit_Flattener'])

    @classmethod
    def Takahashi_Flattener_1_01x_FSQ(cls):
        return cls.from_database(cls._DATABASE['Takahashi_Flattener_1_01x_FSQ'])

    @classmethod
    def Takahashi_TOA_35FL_Flattener(cls):
        return cls.from_database(cls._DATABASE['Takahashi_TOA_35FL_Flattener'])

    @classmethod
    def Takahashi_FC_Flattener(cls):
        return cls.from_database(cls._DATABASE['Takahashi_FC_Flattener'])

    @classmethod
    def Takahashi_Multi_Flattener_1_04x_FC_FS(cls):
        return cls.from_database(cls._DATABASE['Takahashi_Multi_Flattener_1_04x_FC_FS'])

    @classmethod
    def Takahashi_Flattener_0_93x_FOA_60(cls):
        return cls.from_database(cls._DATABASE['Takahashi_Flattener_0_93x_FOA_60'])

    @classmethod
    def Takahashi_TOA_645_FL_Flattener_TOA_130(cls):
        return cls.from_database(cls._DATABASE['Takahashi_TOA_645_FL_Flattener_TOA_130'])

    @classmethod
    def Takahashi_TOA_645_FL_Flattener_TOA_150(cls):
        return cls.from_database(cls._DATABASE['Takahashi_TOA_645_FL_Flattener_TOA_150'])

    @classmethod
    def Riccardi_Flattener_M54(cls):
        return cls.from_database(cls._DATABASE['Riccardi_Flattener_M54'])

    @classmethod
    def William_Optics_Flat68_III(cls):
        return cls.from_database(cls._DATABASE['William_Optics_Flat68_III'])

    @classmethod
    def William_Optics_P_FLAT_68(cls):
        return cls.from_database(cls._DATABASE['William_Optics_P_FLAT_68'])

    @classmethod
    def William_Optics_P_FLAT_73(cls):
        return cls.from_database(cls._DATABASE['William_Optics_P_FLAT_73'])

    @classmethod
    def Askar_Full_frame_Flattener(cls):
        return cls.from_database(cls._DATABASE['Askar_Full_frame_Flattener'])

    @classmethod
    def Askar_2_Flattener_M48(cls):
        return cls.from_database(cls._DATABASE['Askar_2_Flattener_M48'])

    @classmethod
    def Sharpstar_2_Field_Flattener(cls):
        return cls.from_database(cls._DATABASE['Sharpstar_2_Field_Flattener'])

    @classmethod
    def TS_Optics_Flattener_2_M48(cls):
        return cls.from_database(cls._DATABASE['TS_Optics_Flattener_2_M48'])

    @classmethod
    def TS_Optics_TSFlat2_M48(cls):
        return cls.from_database(cls._DATABASE['TS_Optics_TSFlat2_M48'])

    @classmethod
    def TS_Optics_RC_Flattener_M68(cls):
        return cls.from_database(cls._DATABASE['TS_Optics_RC_Flattener_M68'])

    @classmethod
    def Explore_Scientific_ED_Field_Flattener(cls):
        return cls.from_database(cls._DATABASE['Explore_Scientific_ED_Field_Flattener'])

    @classmethod
    def Astro_Physics_160FFAPO5_Flattener(cls):
        return cls.from_database(cls._DATABASE['Astro_Physics_160FFAPO5_Flattener'])

    @classmethod
    def Stellarvue_SVF25_Flattener(cls):
        return cls.from_database(cls._DATABASE['Stellarvue_SVF25_Flattener'])

    @classmethod
    def Vixen_SD_Flattener_HD(cls):
        return cls.from_database(cls._DATABASE['Vixen_SD_Flattener_HD'])

    @classmethod
    def Orion_Field_Flattener_M48(cls):
        return cls.from_database(cls._DATABASE['Orion_Field_Flattener_M48'])

    @classmethod
    def Omegon_Field_Flattener_M48(cls):
        return cls.from_database(cls._DATABASE['Omegon_Field_Flattener_M48'])

    @classmethod
    def Bresser_Field_Flattener_M48(cls):
        return cls.from_database(cls._DATABASE['Bresser_Field_Flattener_M48'])

    @classmethod
    def Lacerta_2_Flattener_M48(cls):
        return cls.from_database(cls._DATABASE['Lacerta_2_Flattener_M48'])

    @classmethod
    def GSO_2_Field_Flattener(cls):
        return cls.from_database(cls._DATABASE['GSO_2_Field_Flattener'])

    @classmethod
    def Altair_Lightwave_Flattener_M48(cls):
        return cls.from_database(cls._DATABASE['Altair_Lightwave_Flattener_M48'])

    @classmethod
    def Stellarvue_SVF25_78_Flattener(cls):
        return cls.from_database(cls._DATABASE['Stellarvue_SVF25_78_Flattener'])

    @classmethod
    def Borg_Flattener_1_08x_M57(cls):
        return cls.from_database(cls._DATABASE['Borg_Flattener_1_08x_M57'])

    @classmethod
    def TS_Optics_TSFlat3_M54(cls):
        return cls.from_database(cls._DATABASE['TS_Optics_TSFlat3_M54'])

    @classmethod
    def TS_Optics_TSFlat4_M68(cls):
        return cls.from_database(cls._DATABASE['TS_Optics_TSFlat4_M68'])

    @classmethod
    def Generic_1_0x_Flattener_M42(cls):
        return cls.from_database(cls._DATABASE['Generic_1_0x_Flattener_M42'])

    @classmethod
    def Generic_1_0x_Flattener_M48(cls):
        return cls.from_database(cls._DATABASE['Generic_1_0x_Flattener_M48'])

    @classmethod
    def Generic_1_0x_Flattener_M54(cls):
        return cls.from_database(cls._DATABASE['Generic_1_0x_Flattener_M54'])

    @classmethod
    def Generic_1_0x_Flattener_M68(cls):
        return cls.from_database(cls._DATABASE['Generic_1_0x_Flattener_M68'])

    @classmethod
    def Astro_Physics_130GTX_Flattener(cls):
        return cls.from_database(cls._DATABASE['Astro_Physics_130GTX_Flattener'])

    @classmethod
    def TeleVue_NP101_Flattener(cls):
        return cls.from_database(cls._DATABASE['TeleVue_NP101_Flattener'])

    @classmethod
    def TeleVue_NP127_Flattener(cls):
        return cls.from_database(cls._DATABASE['TeleVue_NP127_Flattener'])

    @classmethod
    def Stellarvue_SVF50_Flattener(cls):
        return cls.from_database(cls._DATABASE['Stellarvue_SVF50_Flattener'])

    @classmethod
    def Stellarvue_SFF_Flattener_M68(cls):
        return cls.from_database(cls._DATABASE['Stellarvue_SFF_Flattener_M68'])

    @classmethod
    def TEC_TEC_110_Flattener(cls):
        return cls.from_database(cls._DATABASE['TEC_TEC_110_Flattener'])

    @classmethod
    def TEC_TEC_160_Flattener(cls):
        return cls.from_database(cls._DATABASE['TEC_TEC_160_Flattener'])

    @classmethod
    def Borg_Multi_Flattener_M57(cls):
        return cls.from_database(cls._DATABASE['Borg_Multi_Flattener_M57'])

    @classmethod
    def Borg_1_08x_Flattener_89ED(cls):
        return cls.from_database(cls._DATABASE['Borg_1_08x_Flattener_89ED'])

    @classmethod
    def Altair_Lightwave_Flattener(cls):
        return cls.from_database(cls._DATABASE['Altair_Lightwave_Flattener'])

    @classmethod
    def SVBony_SV193_Field_Flattener(cls):
        return cls.from_database(cls._DATABASE['SVBony_SV193_Field_Flattener'])

    @classmethod
    def Tecnosky_Field_Flattener_M48(cls):
        return cls.from_database(cls._DATABASE['Tecnosky_Field_Flattener_M48'])

    @classmethod
    def Long_Perng_Field_Flattener_M48(cls):
        return cls.from_database(cls._DATABASE['Long_Perng_Field_Flattener_M48'])

    @classmethod
    def Meade_Series_6000_Field_Flattener(cls):
        return cls.from_database(cls._DATABASE['Meade_Series_6000_Field_Flattener'])

class Corrector(IntermediateOpticalEquipment):
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
        mag = 1.0
        return cls(
            vendor,
            magnification=mag,
            optical_length=ol,
            mass=mass,
            required_backfocus=55,
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
        mag = 1.0
        return cls(
            vendor,
            magnification=mag,
            optical_length=ol,
            mass=mass,
            required_backfocus=55,
            in_connection_type=tt,
            out_connection_type=ct,
            in_gender=tg or Gender.MALE,
            out_gender=cg or Gender.FEMALE,
        )
    def __init__(
        self, vendor, magnification=1.0, optical_length=0, mass=0, required_backfocus=None,
        in_connection_type=None, out_connection_type=None, in_gender=Gender.MALE, out_gender=Gender.FEMALE
    ):
        super(Corrector, self).__init__(
            vendor, optical_length=optical_length, mass=mass,
            in_connection_type=in_connection_type, out_connection_type=out_connection_type,
            in_gender=in_gender, out_gender=out_gender
        )
        self._type = OpticalType.CORRECTOR
        self.magnification = magnification
        self.required_backfocus = (
            required_backfocus * get_unit_registry().mm
            if required_backfocus is not None
            else None
        )

    _DATABASE = {
        'Sky_Watcher_Quattro_Coma_Corrector': {'brand': 'Sky-Watcher', 'name': 'Quattro Coma Corrector', 'type': 'type_corrector', 'optical_length': 0, 'mass': 300, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Female', 'reversible': False, 'bf_role': 'start'},
        'Sky_Watcher_Coma_Corrector_F_5_Newton': {'brand': 'Sky-Watcher', 'name': 'Coma Corrector (F/5 Newton)', 'type': 'type_corrector', 'optical_length': 0, 'mass': 280, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Female', 'reversible': False, 'bf_role': 'start'},
        'Takahashi_Epsilon_Corrector': {'brand': 'Takahashi', 'name': 'Epsilon Corrector', 'type': 'type_corrector', 'optical_length': 0, 'mass': 300, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Female', 'reversible': False, 'bf_role': 'start'},
        'Baader_MPCC_Mark_III': {'brand': 'Baader', 'name': 'MPCC Mark III', 'type': 'type_corrector', 'optical_length': 0, 'mass': 200, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Female', 'reversible': False, 'bf_role': 'start'},
        'Baader_RCC_I_Coma_Corrector': {'brand': 'Baader', 'name': 'RCC I (Coma Corrector)', 'type': 'type_corrector', 'optical_length': 0, 'mass': 300, 'tside_thread': 'M68', 'tside_gender': 'Female', 'cside_thread': 'M68', 'cside_gender': 'Female', 'reversible': False, 'bf_role': 'start'},
        'Baader_3_RCC_for_RC_telescopes': {'brand': 'Baader', 'name': '3" RCC (for RC telescopes)', 'type': 'type_corrector', 'optical_length': 0, 'mass': 500, 'tside_thread': 'M68', 'tside_gender': 'Female', 'cside_thread': 'M68', 'cside_gender': 'Female', 'reversible': False, 'bf_role': 'start'},
        'Askar_Color_Magic_Corrector': {'brand': 'Askar', 'name': 'Color-Magic Corrector', 'type': 'type_corrector', 'optical_length': 0, 'mass': 200, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Female', 'reversible': False, 'bf_role': 'start'},
        'Sharpstar_HNT_Corrector': {'brand': 'Sharpstar', 'name': 'HNT Corrector', 'type': 'type_corrector', 'optical_length': 0, 'mass': 350, 'tside_thread': 'M68', 'tside_gender': 'Female', 'cside_thread': 'M68', 'cside_gender': 'Female', 'reversible': False, 'bf_role': 'start'},
        'TS_Optics_GPU_3_Coma_Corrector': {'brand': 'TS-Optics', 'name': 'GPU-3 Coma Corrector', 'type': 'type_corrector', 'optical_length': 0, 'mass': 250, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Female', 'reversible': False, 'bf_role': 'start'},
        'TS_Optics_Wynne_Corrector_3': {'brand': 'TS-Optics', 'name': 'Wynne Corrector 3"', 'type': 'type_corrector', 'optical_length': 0, 'mass': 500, 'tside_thread': 'M68', 'tside_gender': 'Female', 'cside_thread': 'M68', 'cside_gender': 'Female', 'reversible': False, 'bf_role': 'start'},
        'TS_Optics_Riccardi_Design_1x_M54': {'brand': 'TS-Optics', 'name': 'Riccardi-Design 1x (M54)', 'type': 'type_corrector', 'optical_length': 0, 'mass': 300, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Female', 'reversible': False, 'bf_role': 'start'},
        'TeleVue_Paracorr_Type_2': {'brand': 'TeleVue', 'name': 'Paracorr Type 2', 'type': 'type_corrector', 'optical_length': 0, 'mass': 400, 'tside_thread': '2"', 'tside_gender': 'Female', 'cside_thread': '2"', 'cside_gender': 'Female', 'reversible': False, 'bf_role': 'start'},
        'TeleVue_Big_Paracorr_Type_2': {'brand': 'TeleVue', 'name': 'Big Paracorr Type 2', 'type': 'type_corrector', 'optical_length': 0, 'mass': 600, 'tside_thread': '2"', 'tside_gender': 'Female', 'cside_thread': '2"', 'cside_gender': 'Female', 'reversible': False, 'bf_role': 'start'},
        'Explore_Scientific_HR_Coma_Corrector': {'brand': 'Explore Scientific', 'name': 'HR Coma Corrector', 'type': 'type_corrector', 'optical_length': 0, 'mass': 350, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Female', 'reversible': False, 'bf_role': 'start'},
        'APM_Comacorr_1x_M48': {'brand': 'APM', 'name': 'Comacorr 1x (M48)', 'type': 'type_corrector', 'optical_length': 0, 'mass': 250, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Female', 'reversible': False, 'bf_role': 'start'},
        'Lacerta_GPU_3_CC_1x': {'brand': 'Lacerta', 'name': 'GPU-3 CC 1x', 'type': 'type_corrector', 'optical_length': 0, 'mass': 250, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Female', 'reversible': False, 'bf_role': 'start'},
        'SVBony_SV193_Coma_Corrector': {'brand': 'SVBony', 'name': 'SV193 Coma Corrector', 'type': 'type_corrector', 'optical_length': 0, 'mass': 200, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Female', 'reversible': False, 'bf_role': 'start'},
        'GSO_Coma_Corrector_M48': {'brand': 'GSO', 'name': 'Coma Corrector (M48)', 'type': 'type_corrector', 'optical_length': 0, 'mass': 230, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Female', 'reversible': False, 'bf_role': 'start'},
        'Vixen_Corrector_PH': {'brand': 'Vixen', 'name': 'Corrector PH', 'type': 'type_corrector', 'optical_length': 0, 'mass': 250, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Female', 'reversible': False, 'bf_role': 'start'},
        'Baader_MPCC_III_1_1': {'brand': 'Baader', 'name': 'MPCC III (1:1)', 'type': 'type_corrector', 'optical_length': 0, 'mass': 200, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Female', 'reversible': False, 'bf_role': 'start'},
        'PlaneWave_CDK12_5_Corrector': {'brand': 'PlaneWave', 'name': 'CDK12.5 Corrector', 'type': 'type_corrector', 'optical_length': 0, 'mass': 600, 'tside_thread': 'M117', 'tside_gender': 'Female', 'cside_thread': 'M117', 'cside_gender': 'Female', 'reversible': False, 'bf_role': 'start'},
        'PlaneWave_CDK14_Corrector': {'brand': 'PlaneWave', 'name': 'CDK14 Corrector', 'type': 'type_corrector', 'optical_length': 0, 'mass': 700, 'tside_thread': 'M117', 'tside_gender': 'Female', 'cside_thread': 'M117', 'cside_gender': 'Female', 'reversible': False, 'bf_role': 'start'},
        'PlaneWave_CDK17_Corrector': {'brand': 'PlaneWave', 'name': 'CDK17 Corrector', 'type': 'type_corrector', 'optical_length': 0, 'mass': 800, 'tside_thread': 'M117', 'tside_gender': 'Female', 'cside_thread': 'M117', 'cside_gender': 'Female', 'reversible': False, 'bf_role': 'start'},
        'PlaneWave_CDK20_Corrector': {'brand': 'PlaneWave', 'name': 'CDK20 Corrector', 'type': 'type_corrector', 'optical_length': 0, 'mass': 1000, 'tside_thread': 'M117', 'tside_gender': 'Female', 'cside_thread': 'M117', 'cside_gender': 'Female', 'reversible': False, 'bf_role': 'start'},
        'Officina_Stellare_RC_Corrector_1x_M84': {'brand': 'Officina Stellare', 'name': 'RC Corrector 1x (M84)', 'type': 'type_corrector', 'optical_length': 0, 'mass': 600, 'tside_thread': 'M84', 'tside_gender': 'Female', 'cside_thread': 'M84', 'cside_gender': 'Female', 'reversible': False, 'bf_role': 'start'},
        'Officina_Stellare_Wynne_Corrector_M68': {'brand': 'Officina Stellare', 'name': 'Wynne Corrector (M68)', 'type': 'type_corrector', 'optical_length': 0, 'mass': 450, 'tside_thread': 'M68', 'tside_gender': 'Female', 'cside_thread': 'M68', 'cside_gender': 'Female', 'reversible': False, 'bf_role': 'start'},
        'Omegon_Coma_Corrector_M48': {'brand': 'Omegon', 'name': 'Coma Corrector (M48)', 'type': 'type_corrector', 'optical_length': 0, 'mass': 220, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Female', 'reversible': False, 'bf_role': 'start'},
        'SVBony_SV116_Coma_Corrector': {'brand': 'SVBony', 'name': 'SV116 Coma Corrector', 'type': 'type_corrector', 'optical_length': 0, 'mass': 200, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Female', 'reversible': False, 'bf_role': 'start'},
        'Lacerta_Wynne_Corrector_3_M68': {'brand': 'Lacerta', 'name': 'Wynne Corrector 3" (M68)', 'type': 'type_corrector', 'optical_length': 0, 'mass': 480, 'tside_thread': 'M68', 'tside_gender': 'Female', 'cside_thread': 'M68', 'cside_gender': 'Female', 'reversible': False, 'bf_role': 'start'},
        'Tecnosky_Wynne_Corrector_M68': {'brand': 'Tecnosky', 'name': 'Wynne Corrector (M68)', 'type': 'type_corrector', 'optical_length': 0, 'mass': 400, 'tside_thread': 'M68', 'tside_gender': 'Female', 'cside_thread': 'M68', 'cside_gender': 'Female', 'reversible': False, 'bf_role': 'start'},
        'CFF_RC_Corrector_1x_M117': {'brand': 'CFF', 'name': 'RC Corrector 1x (M117)', 'type': 'type_corrector', 'optical_length': 0, 'mass': 600, 'tside_thread': 'M117', 'tside_gender': 'Female', 'cside_thread': 'M117', 'cside_gender': 'Female', 'reversible': False, 'bf_role': 'start'},
        'Orion_Coma_Corrector_M48': {'brand': 'Orion', 'name': 'Coma Corrector (M48)', 'type': 'type_corrector', 'optical_length': 0, 'mass': 240, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Female', 'reversible': False, 'bf_role': 'start'},
        'Orion_SkyGlow_Broadband_Filter': {'brand': 'Orion', 'name': 'SkyGlow Broadband Filter', 'type': 'type_corrector', 'optical_length': 0, 'mass': 50, 'tside_thread': '2"', 'tside_gender': 'Female', 'cside_thread': '2"', 'cside_gender': 'Female', 'reversible': False, 'bf_role': 'start'},
        'Meade_Series_6000_Coma_Corrector': {'brand': 'Meade', 'name': 'Series 6000 Coma Corrector', 'type': 'type_corrector', 'optical_length': 0, 'mass': 300, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Female', 'reversible': False, 'bf_role': 'start'},
    }

    @classmethod
    def Sky_Watcher_Quattro_Coma_Corrector(cls):
        return cls.from_database(cls._DATABASE['Sky_Watcher_Quattro_Coma_Corrector'])

    @classmethod
    def Sky_Watcher_Coma_Corrector_F_5_Newton(cls):
        return cls.from_database(cls._DATABASE['Sky_Watcher_Coma_Corrector_F_5_Newton'])

    @classmethod
    def Takahashi_Epsilon_Corrector(cls):
        return cls.from_database(cls._DATABASE['Takahashi_Epsilon_Corrector'])

    @classmethod
    def Baader_MPCC_Mark_III(cls):
        return cls.from_database(cls._DATABASE['Baader_MPCC_Mark_III'])

    @classmethod
    def Baader_RCC_I_Coma_Corrector(cls):
        return cls.from_database(cls._DATABASE['Baader_RCC_I_Coma_Corrector'])

    @classmethod
    def Baader_3_RCC_for_RC_telescopes(cls):
        return cls.from_database(cls._DATABASE['Baader_3_RCC_for_RC_telescopes'])

    @classmethod
    def Askar_Color_Magic_Corrector(cls):
        return cls.from_database(cls._DATABASE['Askar_Color_Magic_Corrector'])

    @classmethod
    def Sharpstar_HNT_Corrector(cls):
        return cls.from_database(cls._DATABASE['Sharpstar_HNT_Corrector'])

    @classmethod
    def TS_Optics_GPU_3_Coma_Corrector(cls):
        return cls.from_database(cls._DATABASE['TS_Optics_GPU_3_Coma_Corrector'])

    @classmethod
    def TS_Optics_Wynne_Corrector_3(cls):
        return cls.from_database(cls._DATABASE['TS_Optics_Wynne_Corrector_3'])

    @classmethod
    def TS_Optics_Riccardi_Design_1x_M54(cls):
        return cls.from_database(cls._DATABASE['TS_Optics_Riccardi_Design_1x_M54'])

    @classmethod
    def TeleVue_Paracorr_Type_2(cls):
        return cls.from_database(cls._DATABASE['TeleVue_Paracorr_Type_2'])

    @classmethod
    def TeleVue_Big_Paracorr_Type_2(cls):
        return cls.from_database(cls._DATABASE['TeleVue_Big_Paracorr_Type_2'])

    @classmethod
    def Explore_Scientific_HR_Coma_Corrector(cls):
        return cls.from_database(cls._DATABASE['Explore_Scientific_HR_Coma_Corrector'])

    @classmethod
    def APM_Comacorr_1x_M48(cls):
        return cls.from_database(cls._DATABASE['APM_Comacorr_1x_M48'])

    @classmethod
    def Lacerta_GPU_3_CC_1x(cls):
        return cls.from_database(cls._DATABASE['Lacerta_GPU_3_CC_1x'])

    @classmethod
    def SVBony_SV193_Coma_Corrector(cls):
        return cls.from_database(cls._DATABASE['SVBony_SV193_Coma_Corrector'])

    @classmethod
    def GSO_Coma_Corrector_M48(cls):
        return cls.from_database(cls._DATABASE['GSO_Coma_Corrector_M48'])

    @classmethod
    def Vixen_Corrector_PH(cls):
        return cls.from_database(cls._DATABASE['Vixen_Corrector_PH'])

    @classmethod
    def Baader_MPCC_III_1_1(cls):
        return cls.from_database(cls._DATABASE['Baader_MPCC_III_1_1'])

    @classmethod
    def PlaneWave_CDK12_5_Corrector(cls):
        return cls.from_database(cls._DATABASE['PlaneWave_CDK12_5_Corrector'])

    @classmethod
    def PlaneWave_CDK14_Corrector(cls):
        return cls.from_database(cls._DATABASE['PlaneWave_CDK14_Corrector'])

    @classmethod
    def PlaneWave_CDK17_Corrector(cls):
        return cls.from_database(cls._DATABASE['PlaneWave_CDK17_Corrector'])

    @classmethod
    def PlaneWave_CDK20_Corrector(cls):
        return cls.from_database(cls._DATABASE['PlaneWave_CDK20_Corrector'])

    @classmethod
    def Officina_Stellare_RC_Corrector_1x_M84(cls):
        return cls.from_database(cls._DATABASE['Officina_Stellare_RC_Corrector_1x_M84'])

    @classmethod
    def Officina_Stellare_Wynne_Corrector_M68(cls):
        return cls.from_database(cls._DATABASE['Officina_Stellare_Wynne_Corrector_M68'])

    @classmethod
    def Omegon_Coma_Corrector_M48(cls):
        return cls.from_database(cls._DATABASE['Omegon_Coma_Corrector_M48'])

    @classmethod
    def SVBony_SV116_Coma_Corrector(cls):
        return cls.from_database(cls._DATABASE['SVBony_SV116_Coma_Corrector'])

    @classmethod
    def Lacerta_Wynne_Corrector_3_M68(cls):
        return cls.from_database(cls._DATABASE['Lacerta_Wynne_Corrector_3_M68'])

    @classmethod
    def Tecnosky_Wynne_Corrector_M68(cls):
        return cls.from_database(cls._DATABASE['Tecnosky_Wynne_Corrector_M68'])

    @classmethod
    def CFF_RC_Corrector_1x_M117(cls):
        return cls.from_database(cls._DATABASE['CFF_RC_Corrector_1x_M117'])

    @classmethod
    def Orion_Coma_Corrector_M48(cls):
        return cls.from_database(cls._DATABASE['Orion_Coma_Corrector_M48'])

    @classmethod
    def Orion_SkyGlow_Broadband_Filter(cls):
        return cls.from_database(cls._DATABASE['Orion_SkyGlow_Broadband_Filter'])

    @classmethod
    def Meade_Series_6000_Coma_Corrector(cls):
        return cls.from_database(cls._DATABASE['Meade_Series_6000_Coma_Corrector'])
