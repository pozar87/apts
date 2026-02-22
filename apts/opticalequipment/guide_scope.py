from .telescope import Telescope
from ..constants import OpticalType

class GuideScope(Telescope):
    @classmethod
    def from_database(cls, entry):
        from ..utils import Utils, Gender
        brand = entry["brand"]
        name = entry["name"]
        vendor = f"{brand} {name}"
        ol = entry.get("optical_length", 0)
        mass = entry.get("mass", 0)
        ct = Utils.map_conn(entry.get("cside_thread"))
        cg = Utils.map_gender(entry.get("cside_gender"))
        aperture, focal_length = Utils.guess_optical_properties(name)
        bf_val = entry.get("bf_role") == "start"
        return cls(
            aperture or 30,
            focal_length or 120,
            vendor=vendor,
            connection_type=ct,
            connection_gender=cg or Gender.FEMALE,
            backfocus=ol if bf_val else None,
            mass=mass,
            optical_length=ol,
        )
    @classmethod
    def from_database(cls, entry):
        from ..utils import Utils, Gender
        brand = entry["brand"]
        name = entry["name"]
        vendor = f"{brand} {name}"
        ol = entry.get("optical_length", 0)
        mass = entry.get("mass", 0)
        ct = Utils.map_conn(entry.get("cside_thread"))
        cg = Utils.map_gender(entry.get("cside_gender"))
        aperture, focal_length = Utils.guess_optical_properties(name)
        bf_val = entry.get("bf_role") == "start"
        return cls(
            aperture or 30,
            focal_length or 120,
            vendor=vendor,
            connection_type=ct,
            connection_gender=cg or Gender.FEMALE,
            backfocus=ol if bf_val else None,
            mass=mass,
            optical_length=ol,
        )
    def __init__(self, aperture, focal_length, vendor="unknown guide scope", connection_type=None, connection_gender=None, mass=0, optical_length=0):
        super(GuideScope, self).__init__(aperture, focal_length, vendor, connection_type=connection_type, connection_gender=connection_gender, mass=mass, optical_length=optical_length)
        self._type = OpticalType.GUIDE_SCOPE

    _DATABASE = {
        'ZWO_30mm_Mini_Guide_Scope': {'brand': 'ZWO', 'name': '30mm Mini Guide Scope', 'type': 'type_guide_scope', 'optical_length': 0, 'mass': 150, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'CS', 'cside_gender': 'Female', 'reversible': False, 'bf_role': ''},
        'ZWO_60mm_Guide_Scope': {'brand': 'ZWO', 'name': '60mm Guide Scope', 'type': 'type_guide_scope', 'optical_length': 0, 'mass': 350, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M42', 'cside_gender': 'Female', 'reversible': False, 'bf_role': ''},
        'ZWO_120mm_Guide_Scope': {'brand': 'ZWO', 'name': '120mm Guide Scope', 'type': 'type_guide_scope', 'optical_length': 0, 'mass': 500, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M42', 'cside_gender': 'Female', 'reversible': False, 'bf_role': ''},
        'SVBony_SV106_50mm_Guide_Scope': {'brand': 'SVBony', 'name': 'SV106 50mm Guide Scope', 'type': 'type_guide_scope', 'optical_length': 0, 'mass': 250, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M42', 'cside_gender': 'Female', 'reversible': False, 'bf_role': ''},
        'SVBony_SV165_30mm_Guide_Scope': {'brand': 'SVBony', 'name': 'SV165 30mm Guide Scope', 'type': 'type_guide_scope', 'optical_length': 0, 'mass': 120, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'CS', 'cside_gender': 'Female', 'reversible': False, 'bf_role': ''},
        'SVBony_SV106_60mm_Guide_Scope': {'brand': 'SVBony', 'name': 'SV106 60mm Guide Scope', 'type': 'type_guide_scope', 'optical_length': 0, 'mass': 300, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M42', 'cside_gender': 'Female', 'reversible': False, 'bf_role': ''},
        'SVBony_SV210_30mm_Guide_Scope': {'brand': 'SVBony', 'name': 'SV210 30mm Guide Scope', 'type': 'type_guide_scope', 'optical_length': 0, 'mass': 100, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'CS', 'cside_gender': 'Female', 'reversible': False, 'bf_role': ''},
        'William_Optics_UniGuide_50mm': {'brand': 'William Optics', 'name': 'UniGuide 50mm', 'type': 'type_guide_scope', 'optical_length': 0, 'mass': 300, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M42', 'cside_gender': 'Female', 'reversible': False, 'bf_role': ''},
        'William_Optics_UniGuide_32mm': {'brand': 'William Optics', 'name': 'UniGuide 32mm', 'type': 'type_guide_scope', 'optical_length': 0, 'mass': 150, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'CS', 'cside_gender': 'Female', 'reversible': False, 'bf_role': ''},
        'QHY_Mini_Guide_Scope_30mm': {'brand': 'QHY', 'name': 'Mini Guide Scope 30mm', 'type': 'type_guide_scope', 'optical_length': 0, 'mass': 130, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'CS', 'cside_gender': 'Female', 'reversible': False, 'bf_role': ''},
        'QHY_Mini_Guide_Scope_60mm': {'brand': 'QHY', 'name': 'Mini Guide Scope 60mm', 'type': 'type_guide_scope', 'optical_length': 0, 'mass': 320, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M42', 'cside_gender': 'Female', 'reversible': False, 'bf_role': ''},
        'Orion_50mm_Guide_Scope': {'brand': 'Orion', 'name': '50mm Guide Scope', 'type': 'type_guide_scope', 'optical_length': 0, 'mass': 280, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M42', 'cside_gender': 'Female', 'reversible': False, 'bf_role': ''},
        'Orion_60mm_Guide_Scope': {'brand': 'Orion', 'name': '60mm Guide Scope', 'type': 'type_guide_scope', 'optical_length': 0, 'mass': 340, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M42', 'cside_gender': 'Female', 'reversible': False, 'bf_role': ''},
        'Player_One_Guide_Scope_30mm': {'brand': 'Player One', 'name': 'Guide Scope 30mm', 'type': 'type_guide_scope', 'optical_length': 0, 'mass': 120, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'CS', 'cside_gender': 'Female', 'reversible': False, 'bf_role': ''},
        'Player_One_Guide_Scope_60mm': {'brand': 'Player One', 'name': 'Guide Scope 60mm', 'type': 'type_guide_scope', 'optical_length': 0, 'mass': 300, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M42', 'cside_gender': 'Female', 'reversible': False, 'bf_role': ''},
        'Altair_60mm_Guide_Scope': {'brand': 'Altair', 'name': '60mm Guide Scope', 'type': 'type_guide_scope', 'optical_length': 0, 'mass': 330, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M42', 'cside_gender': 'Female', 'reversible': False, 'bf_role': ''},
        'Altair_30mm_Guide_Scope': {'brand': 'Altair', 'name': '30mm Guide Scope', 'type': 'type_guide_scope', 'optical_length': 0, 'mass': 140, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'CS', 'cside_gender': 'Female', 'reversible': False, 'bf_role': ''},
        'Omegon_50mm_Guide_Scope': {'brand': 'Omegon', 'name': '50mm Guide Scope', 'type': 'type_guide_scope', 'optical_length': 0, 'mass': 260, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M42', 'cside_gender': 'Female', 'reversible': False, 'bf_role': ''},
        'Omegon_60mm_Guide_Scope': {'brand': 'Omegon', 'name': '60mm Guide Scope', 'type': 'type_guide_scope', 'optical_length': 0, 'mass': 310, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M42', 'cside_gender': 'Female', 'reversible': False, 'bf_role': ''},
        'Lacerta_Micro_Guide_Scope_30mm': {'brand': 'Lacerta', 'name': 'Micro Guide Scope 30mm', 'type': 'type_guide_scope', 'optical_length': 0, 'mass': 130, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'CS', 'cside_gender': 'Female', 'reversible': False, 'bf_role': ''},
        'Lacerta_Guide_Scope_50mm': {'brand': 'Lacerta', 'name': 'Guide Scope 50mm', 'type': 'type_guide_scope', 'optical_length': 0, 'mass': 270, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M42', 'cside_gender': 'Female', 'reversible': False, 'bf_role': ''},
        'TS_Optics_50mm_Guide_Scope': {'brand': 'TS-Optics', 'name': '50mm Guide Scope', 'type': 'type_guide_scope', 'optical_length': 0, 'mass': 260, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M42', 'cside_gender': 'Female', 'reversible': False, 'bf_role': ''},
        'TS_Optics_60mm_Guide_Scope': {'brand': 'TS-Optics', 'name': '60mm Guide Scope', 'type': 'type_guide_scope', 'optical_length': 0, 'mass': 310, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M42', 'cside_gender': 'Female', 'reversible': False, 'bf_role': ''},
        'Bresser_50mm_Guide_Scope': {'brand': 'Bresser', 'name': '50mm Guide Scope', 'type': 'type_guide_scope', 'optical_length': 0, 'mass': 250, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M42', 'cside_gender': 'Female', 'reversible': False, 'bf_role': ''},
        'Celestron_80mm_Guide_Scope': {'brand': 'Celestron', 'name': '80mm Guide Scope', 'type': 'type_guide_scope', 'optical_length': 0, 'mass': 650, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M42', 'cside_gender': 'Female', 'reversible': False, 'bf_role': ''},
        'Explore_Scientific_50mm_Guide_Scope': {'brand': 'Explore Scientific', 'name': '50mm Guide Scope', 'type': 'type_guide_scope', 'optical_length': 0, 'mass': 270, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M42', 'cside_gender': 'Female', 'reversible': False, 'bf_role': ''},
        'SVBony_SV48P_Guide_Scope': {'brand': 'SVBony', 'name': 'SV48P Guide Scope', 'type': 'type_guide_scope', 'optical_length': 0, 'mass': 250, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'CS', 'cside_gender': 'Female', 'reversible': False, 'bf_role': ''},
        'SVBony_SV106_Guide_60mm': {'brand': 'SVBony', 'name': 'SV106 Guide 60mm', 'type': 'type_guide_scope', 'optical_length': 0, 'mass': 300, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M42', 'cside_gender': 'Female', 'reversible': False, 'bf_role': ''},
        'Celestron_50mm_Guide_Scope': {'brand': 'Celestron', 'name': '50mm Guide Scope', 'type': 'type_guide_scope', 'optical_length': 0, 'mass': 280, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M42', 'cside_gender': 'Female', 'reversible': False, 'bf_role': ''},
        'Celestron_60mm_Guide_Scope': {'brand': 'Celestron', 'name': '60mm Guide Scope', 'type': 'type_guide_scope', 'optical_length': 0, 'mass': 340, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M42', 'cside_gender': 'Female', 'reversible': False, 'bf_role': ''},
        'Meade_50mm_Guide_Scope': {'brand': 'Meade', 'name': '50mm Guide Scope', 'type': 'type_guide_scope', 'optical_length': 0, 'mass': 270, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M42', 'cside_gender': 'Female', 'reversible': False, 'bf_role': ''},
        'Starlight_Xpress_Lodestar_Guide_Scope': {'brand': 'Starlight Xpress', 'name': 'Lodestar Guide Scope', 'type': 'type_guide_scope', 'optical_length': 0, 'mass': 300, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M42', 'cside_gender': 'Female', 'reversible': False, 'bf_role': ''},
        'Pegasus_50mm_Guide_Scope': {'brand': 'Pegasus', 'name': '50mm Guide Scope', 'type': 'type_guide_scope', 'optical_length': 0, 'mass': 260, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M42', 'cside_gender': 'Female', 'reversible': False, 'bf_role': ''},
        'Takahashi_GT_40_Guide_Scope': {'brand': 'Takahashi', 'name': 'GT-40 Guide Scope', 'type': 'type_guide_scope', 'optical_length': 0, 'mass': 250, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M42', 'cside_gender': 'Female', 'reversible': False, 'bf_role': ''},
        'Vixen_Guide_Scope_50mm': {'brand': 'Vixen', 'name': 'Guide Scope 50mm', 'type': 'type_guide_scope', 'optical_length': 0, 'mass': 280, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M42', 'cside_gender': 'Female', 'reversible': False, 'bf_role': ''},
        'Saxon_Guide_Scope_50mm': {'brand': 'Saxon', 'name': 'Guide Scope 50mm', 'type': 'type_guide_scope', 'optical_length': 0, 'mass': 250, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M42', 'cside_gender': 'Female', 'reversible': False, 'bf_role': ''},
        'Bresser_Guide_Scope_50mm': {'brand': 'Bresser', 'name': 'Guide Scope 50mm', 'type': 'type_guide_scope', 'optical_length': 0, 'mass': 260, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M42', 'cside_gender': 'Female', 'reversible': False, 'bf_role': ''},
        'iOptron_iGuide_60mm': {'brand': 'iOptron', 'name': 'iGuide 60mm', 'type': 'type_guide_scope', 'optical_length': 0, 'mass': 320, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M42', 'cside_gender': 'Female', 'reversible': False, 'bf_role': ''},
        'Lunt_Solar_Guide_Scope_50mm': {'brand': 'Lunt Solar', 'name': 'Guide Scope 50mm', 'type': 'type_guide_scope', 'optical_length': 0, 'mass': 270, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M42', 'cside_gender': 'Female', 'reversible': False, 'bf_role': ''},
        'National_Geographic_Guide_Scope_50mm': {'brand': 'National Geographic', 'name': 'Guide Scope 50mm', 'type': 'type_guide_scope', 'optical_length': 0, 'mass': 240, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M42', 'cside_gender': 'Female', 'reversible': False, 'bf_role': ''},
        'Askar_FMA135_Guide_Scope': {'brand': 'Askar', 'name': 'FMA135 Guide Scope', 'type': 'type_guide_scope', 'optical_length': 0, 'mass': 600, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M42', 'cside_gender': 'Female', 'reversible': False, 'bf_role': ''},
        'Askar_40mm_Guide_Scope': {'brand': 'Askar', 'name': '40mm Guide Scope', 'type': 'type_guide_scope', 'optical_length': 0, 'mass': 200, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M42', 'cside_gender': 'Female', 'reversible': False, 'bf_role': ''},
        'Askar_32mm_Guide_Scope': {'brand': 'Askar', 'name': '32mm Guide Scope', 'type': 'type_guide_scope', 'optical_length': 0, 'mass': 150, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'CS', 'cside_gender': 'Female', 'reversible': False, 'bf_role': ''},
        'Sharpstar_30mm_Guide_Scope': {'brand': 'Sharpstar', 'name': '30mm Guide Scope', 'type': 'type_guide_scope', 'optical_length': 0, 'mass': 120, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'CS', 'cside_gender': 'Female', 'reversible': False, 'bf_role': ''},
        'Sharpstar_50mm_Guide_Scope': {'brand': 'Sharpstar', 'name': '50mm Guide Scope', 'type': 'type_guide_scope', 'optical_length': 0, 'mass': 250, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M42', 'cside_gender': 'Female', 'reversible': False, 'bf_role': ''},
        'Sharpstar_60mm_Guide_Scope': {'brand': 'Sharpstar', 'name': '60mm Guide Scope', 'type': 'type_guide_scope', 'optical_length': 0, 'mass': 300, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M42', 'cside_gender': 'Female', 'reversible': False, 'bf_role': ''},
        'Starlight_Xpress_SX_Guide_Scope_50mm': {'brand': 'Starlight Xpress', 'name': 'SX Guide Scope 50mm', 'type': 'type_guide_scope', 'optical_length': 0, 'mass': 280, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M42', 'cside_gender': 'Female', 'reversible': False, 'bf_role': ''},
        'Meade_LX85_60mm_Guide_Scope': {'brand': 'Meade', 'name': 'LX85 60mm Guide Scope', 'type': 'type_guide_scope', 'optical_length': 0, 'mass': 320, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M42', 'cside_gender': 'Female', 'reversible': False, 'bf_role': ''},
        'Bresser_60mm_Guide_Scope': {'brand': 'Bresser', 'name': '60mm Guide Scope', 'type': 'type_guide_scope', 'optical_length': 0, 'mass': 310, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M42', 'cside_gender': 'Female', 'reversible': False, 'bf_role': ''},
        'Vixen_Guide_Scope_60mm': {'brand': 'Vixen', 'name': 'Guide Scope 60mm', 'type': 'type_guide_scope', 'optical_length': 0, 'mass': 330, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M42', 'cside_gender': 'Female', 'reversible': False, 'bf_role': ''},
        'APM_Guide_Scope_50mm': {'brand': 'APM', 'name': 'Guide Scope 50mm', 'type': 'type_guide_scope', 'optical_length': 0, 'mass': 250, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M42', 'cside_gender': 'Female', 'reversible': False, 'bf_role': ''},
        'APM_Guide_Scope_60mm': {'brand': 'APM', 'name': 'Guide Scope 60mm', 'type': 'type_guide_scope', 'optical_length': 0, 'mass': 300, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M42', 'cside_gender': 'Female', 'reversible': False, 'bf_role': ''},
        'Stellarvue_SV50_Guide_Scope': {'brand': 'Stellarvue', 'name': 'SV50 Guide Scope', 'type': 'type_guide_scope', 'optical_length': 0, 'mass': 260, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M42', 'cside_gender': 'Female', 'reversible': False, 'bf_role': ''},
        'OGMA_Guide_Scope_30mm': {'brand': 'OGMA', 'name': 'Guide Scope 30mm', 'type': 'type_guide_scope', 'optical_length': 0, 'mass': 120, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'CS', 'cside_gender': 'Female', 'reversible': False, 'bf_role': ''},
        'OGMA_Guide_Scope_60mm': {'brand': 'OGMA', 'name': 'Guide Scope 60mm', 'type': 'type_guide_scope', 'optical_length': 0, 'mass': 300, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M42', 'cside_gender': 'Female', 'reversible': False, 'bf_role': ''},
        'Tecnosky_30mm_Guide_Scope': {'brand': 'Tecnosky', 'name': '30mm Guide Scope', 'type': 'type_guide_scope', 'optical_length': 0, 'mass': 110, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'CS', 'cside_gender': 'Female', 'reversible': False, 'bf_role': ''},
        'Tecnosky_60mm_Guide_Scope': {'brand': 'Tecnosky', 'name': '60mm Guide Scope', 'type': 'type_guide_scope', 'optical_length': 0, 'mass': 310, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M42', 'cside_gender': 'Female', 'reversible': False, 'bf_role': ''},
        'Wanderer_Astro_Guide_Scope_30mm': {'brand': 'Wanderer Astro', 'name': 'Guide Scope 30mm', 'type': 'type_guide_scope', 'optical_length': 0, 'mass': 110, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'CS', 'cside_gender': 'Female', 'reversible': False, 'bf_role': ''},
        'Wanderer_Astro_Guide_Scope_50mm': {'brand': 'Wanderer Astro', 'name': 'Guide Scope 50mm', 'type': 'type_guide_scope', 'optical_length': 0, 'mass': 250, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M42', 'cside_gender': 'Female', 'reversible': False, 'bf_role': ''},
        'Lunt_Solar_Guide_Scope_50mm_Solar': {'brand': 'Lunt Solar', 'name': 'Guide Scope 50mm Solar', 'type': 'type_guide_scope', 'optical_length': 0, 'mass': 280, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M42', 'cside_gender': 'Female', 'reversible': False, 'bf_role': ''},
        'iOptron_Guide_Scope_30mm': {'brand': 'iOptron', 'name': 'Guide Scope 30mm', 'type': 'type_guide_scope', 'optical_length': 0, 'mass': 120, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'CS', 'cside_gender': 'Female', 'reversible': False, 'bf_role': ''},
        'iOptron_Guide_Scope_60mm': {'brand': 'iOptron', 'name': 'Guide Scope 60mm', 'type': 'type_guide_scope', 'optical_length': 0, 'mass': 310, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M42', 'cside_gender': 'Female', 'reversible': False, 'bf_role': ''},
        'Orion_Mini_50mm_Guide_Scope': {'brand': 'Orion', 'name': 'Mini 50mm Guide Scope', 'type': 'type_guide_scope', 'optical_length': 0, 'mass': 260, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M42', 'cside_gender': 'Female', 'reversible': False, 'bf_role': ''},
        'Orion_Deluxe_60mm_Guide_Scope': {'brand': 'Orion', 'name': 'Deluxe 60mm Guide Scope', 'type': 'type_guide_scope', 'optical_length': 0, 'mass': 350, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M42', 'cside_gender': 'Female', 'reversible': False, 'bf_role': ''},
    }

    @classmethod
    def ZWO_30mm_Mini_Guide_Scope(cls):
        return cls.from_database(cls._DATABASE['ZWO_30mm_Mini_Guide_Scope'])

    @classmethod
    def ZWO_60mm_Guide_Scope(cls):
        return cls.from_database(cls._DATABASE['ZWO_60mm_Guide_Scope'])

    @classmethod
    def ZWO_120mm_Guide_Scope(cls):
        return cls.from_database(cls._DATABASE['ZWO_120mm_Guide_Scope'])

    @classmethod
    def SVBony_SV106_50mm_Guide_Scope(cls):
        return cls.from_database(cls._DATABASE['SVBony_SV106_50mm_Guide_Scope'])

    @classmethod
    def SVBony_SV165_30mm_Guide_Scope(cls):
        return cls.from_database(cls._DATABASE['SVBony_SV165_30mm_Guide_Scope'])

    @classmethod
    def SVBony_SV106_60mm_Guide_Scope(cls):
        return cls.from_database(cls._DATABASE['SVBony_SV106_60mm_Guide_Scope'])

    @classmethod
    def SVBony_SV210_30mm_Guide_Scope(cls):
        return cls.from_database(cls._DATABASE['SVBony_SV210_30mm_Guide_Scope'])

    @classmethod
    def William_Optics_UniGuide_50mm(cls):
        return cls.from_database(cls._DATABASE['William_Optics_UniGuide_50mm'])

    @classmethod
    def William_Optics_UniGuide_32mm(cls):
        return cls.from_database(cls._DATABASE['William_Optics_UniGuide_32mm'])

    @classmethod
    def QHY_Mini_Guide_Scope_30mm(cls):
        return cls.from_database(cls._DATABASE['QHY_Mini_Guide_Scope_30mm'])

    @classmethod
    def QHY_Mini_Guide_Scope_60mm(cls):
        return cls.from_database(cls._DATABASE['QHY_Mini_Guide_Scope_60mm'])

    @classmethod
    def Orion_50mm_Guide_Scope(cls):
        return cls.from_database(cls._DATABASE['Orion_50mm_Guide_Scope'])

    @classmethod
    def Orion_60mm_Guide_Scope(cls):
        return cls.from_database(cls._DATABASE['Orion_60mm_Guide_Scope'])

    @classmethod
    def Player_One_Guide_Scope_30mm(cls):
        return cls.from_database(cls._DATABASE['Player_One_Guide_Scope_30mm'])

    @classmethod
    def Player_One_Guide_Scope_60mm(cls):
        return cls.from_database(cls._DATABASE['Player_One_Guide_Scope_60mm'])

    @classmethod
    def Altair_60mm_Guide_Scope(cls):
        return cls.from_database(cls._DATABASE['Altair_60mm_Guide_Scope'])

    @classmethod
    def Altair_30mm_Guide_Scope(cls):
        return cls.from_database(cls._DATABASE['Altair_30mm_Guide_Scope'])

    @classmethod
    def Omegon_50mm_Guide_Scope(cls):
        return cls.from_database(cls._DATABASE['Omegon_50mm_Guide_Scope'])

    @classmethod
    def Omegon_60mm_Guide_Scope(cls):
        return cls.from_database(cls._DATABASE['Omegon_60mm_Guide_Scope'])

    @classmethod
    def Lacerta_Micro_Guide_Scope_30mm(cls):
        return cls.from_database(cls._DATABASE['Lacerta_Micro_Guide_Scope_30mm'])

    @classmethod
    def Lacerta_Guide_Scope_50mm(cls):
        return cls.from_database(cls._DATABASE['Lacerta_Guide_Scope_50mm'])

    @classmethod
    def TS_Optics_50mm_Guide_Scope(cls):
        return cls.from_database(cls._DATABASE['TS_Optics_50mm_Guide_Scope'])

    @classmethod
    def TS_Optics_60mm_Guide_Scope(cls):
        return cls.from_database(cls._DATABASE['TS_Optics_60mm_Guide_Scope'])

    @classmethod
    def Bresser_50mm_Guide_Scope(cls):
        return cls.from_database(cls._DATABASE['Bresser_50mm_Guide_Scope'])

    @classmethod
    def Celestron_80mm_Guide_Scope(cls):
        return cls.from_database(cls._DATABASE['Celestron_80mm_Guide_Scope'])

    @classmethod
    def Explore_Scientific_50mm_Guide_Scope(cls):
        return cls.from_database(cls._DATABASE['Explore_Scientific_50mm_Guide_Scope'])

    @classmethod
    def SVBony_SV48P_Guide_Scope(cls):
        return cls.from_database(cls._DATABASE['SVBony_SV48P_Guide_Scope'])

    @classmethod
    def SVBony_SV106_Guide_60mm(cls):
        return cls.from_database(cls._DATABASE['SVBony_SV106_Guide_60mm'])

    @classmethod
    def Celestron_50mm_Guide_Scope(cls):
        return cls.from_database(cls._DATABASE['Celestron_50mm_Guide_Scope'])

    @classmethod
    def Celestron_60mm_Guide_Scope(cls):
        return cls.from_database(cls._DATABASE['Celestron_60mm_Guide_Scope'])

    @classmethod
    def Meade_50mm_Guide_Scope(cls):
        return cls.from_database(cls._DATABASE['Meade_50mm_Guide_Scope'])

    @classmethod
    def Starlight_Xpress_Lodestar_Guide_Scope(cls):
        return cls.from_database(cls._DATABASE['Starlight_Xpress_Lodestar_Guide_Scope'])

    @classmethod
    def Pegasus_50mm_Guide_Scope(cls):
        return cls.from_database(cls._DATABASE['Pegasus_50mm_Guide_Scope'])

    @classmethod
    def Takahashi_GT_40_Guide_Scope(cls):
        return cls.from_database(cls._DATABASE['Takahashi_GT_40_Guide_Scope'])

    @classmethod
    def Vixen_Guide_Scope_50mm(cls):
        return cls.from_database(cls._DATABASE['Vixen_Guide_Scope_50mm'])

    @classmethod
    def Saxon_Guide_Scope_50mm(cls):
        return cls.from_database(cls._DATABASE['Saxon_Guide_Scope_50mm'])

    @classmethod
    def Bresser_Guide_Scope_50mm(cls):
        return cls.from_database(cls._DATABASE['Bresser_Guide_Scope_50mm'])

    @classmethod
    def iOptron_iGuide_60mm(cls):
        return cls.from_database(cls._DATABASE['iOptron_iGuide_60mm'])

    @classmethod
    def Lunt_Solar_Guide_Scope_50mm(cls):
        return cls.from_database(cls._DATABASE['Lunt_Solar_Guide_Scope_50mm'])

    @classmethod
    def National_Geographic_Guide_Scope_50mm(cls):
        return cls.from_database(cls._DATABASE['National_Geographic_Guide_Scope_50mm'])

    @classmethod
    def Askar_FMA135_Guide_Scope(cls):
        return cls.from_database(cls._DATABASE['Askar_FMA135_Guide_Scope'])

    @classmethod
    def Askar_40mm_Guide_Scope(cls):
        return cls.from_database(cls._DATABASE['Askar_40mm_Guide_Scope'])

    @classmethod
    def Askar_32mm_Guide_Scope(cls):
        return cls.from_database(cls._DATABASE['Askar_32mm_Guide_Scope'])

    @classmethod
    def Sharpstar_30mm_Guide_Scope(cls):
        return cls.from_database(cls._DATABASE['Sharpstar_30mm_Guide_Scope'])

    @classmethod
    def Sharpstar_50mm_Guide_Scope(cls):
        return cls.from_database(cls._DATABASE['Sharpstar_50mm_Guide_Scope'])

    @classmethod
    def Sharpstar_60mm_Guide_Scope(cls):
        return cls.from_database(cls._DATABASE['Sharpstar_60mm_Guide_Scope'])

    @classmethod
    def Starlight_Xpress_SX_Guide_Scope_50mm(cls):
        return cls.from_database(cls._DATABASE['Starlight_Xpress_SX_Guide_Scope_50mm'])

    @classmethod
    def Meade_LX85_60mm_Guide_Scope(cls):
        return cls.from_database(cls._DATABASE['Meade_LX85_60mm_Guide_Scope'])

    @classmethod
    def Bresser_60mm_Guide_Scope(cls):
        return cls.from_database(cls._DATABASE['Bresser_60mm_Guide_Scope'])

    @classmethod
    def Vixen_Guide_Scope_60mm(cls):
        return cls.from_database(cls._DATABASE['Vixen_Guide_Scope_60mm'])

    @classmethod
    def APM_Guide_Scope_50mm(cls):
        return cls.from_database(cls._DATABASE['APM_Guide_Scope_50mm'])

    @classmethod
    def APM_Guide_Scope_60mm(cls):
        return cls.from_database(cls._DATABASE['APM_Guide_Scope_60mm'])

    @classmethod
    def Stellarvue_SV50_Guide_Scope(cls):
        return cls.from_database(cls._DATABASE['Stellarvue_SV50_Guide_Scope'])

    @classmethod
    def OGMA_Guide_Scope_30mm(cls):
        return cls.from_database(cls._DATABASE['OGMA_Guide_Scope_30mm'])

    @classmethod
    def OGMA_Guide_Scope_60mm(cls):
        return cls.from_database(cls._DATABASE['OGMA_Guide_Scope_60mm'])

    @classmethod
    def Tecnosky_30mm_Guide_Scope(cls):
        return cls.from_database(cls._DATABASE['Tecnosky_30mm_Guide_Scope'])

    @classmethod
    def Tecnosky_60mm_Guide_Scope(cls):
        return cls.from_database(cls._DATABASE['Tecnosky_60mm_Guide_Scope'])

    @classmethod
    def Wanderer_Astro_Guide_Scope_30mm(cls):
        return cls.from_database(cls._DATABASE['Wanderer_Astro_Guide_Scope_30mm'])

    @classmethod
    def Wanderer_Astro_Guide_Scope_50mm(cls):
        return cls.from_database(cls._DATABASE['Wanderer_Astro_Guide_Scope_50mm'])

    @classmethod
    def Lunt_Solar_Guide_Scope_50mm_Solar(cls):
        return cls.from_database(cls._DATABASE['Lunt_Solar_Guide_Scope_50mm_Solar'])

    @classmethod
    def iOptron_Guide_Scope_30mm(cls):
        return cls.from_database(cls._DATABASE['iOptron_Guide_Scope_30mm'])

    @classmethod
    def iOptron_Guide_Scope_60mm(cls):
        return cls.from_database(cls._DATABASE['iOptron_Guide_Scope_60mm'])

    @classmethod
    def Orion_Mini_50mm_Guide_Scope(cls):
        return cls.from_database(cls._DATABASE['Orion_Mini_50mm_Guide_Scope'])

    @classmethod
    def Orion_Deluxe_60mm_Guide_Scope(cls):
        return cls.from_database(cls._DATABASE['Orion_Deluxe_60mm_Guide_Scope'])
