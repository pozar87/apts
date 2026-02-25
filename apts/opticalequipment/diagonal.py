from ..utils import ConnectionType, Gender
from .abstract import IntermediateOpticalEquipment


class Diagonal(IntermediateOpticalEquipment):
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

    """
    Class representing a star diagonal.
    """

    def __init__(
        self,
        vendor="unknown diagonal",
        connection_type=ConnectionType.F_1_25,
        is_erecting=False,
        t2_output=False,
        optical_length=0,
        mass=0,
        in_connection_type=None,
        out_connection_type=None,
        in_gender=None,
        out_gender=None,
    ):
        super(Diagonal, self).__init__(
            vendor,
            optical_length=optical_length,
            mass=mass,
            in_connection_type=in_connection_type or connection_type,
            out_connection_type=out_connection_type or connection_type,
            in_gender=in_gender or Gender.MALE,
            out_gender=out_gender or Gender.FEMALE,
        )
        self.connection_type = connection_type or in_connection_type
        self.is_erecting = is_erecting
        self.t2_output = t2_output

    def register(self, equipment):
        """
        Register diagonal in optical equipment graph.
        """
        super(Diagonal, self).register(equipment)
        if self.t2_output:
            self._register_output(equipment, ConnectionType.T2, Gender.MALE)

    def __str__(self):
        return f"{self.vendor}"

    _DATABASE = {
        "Baader_T_2_Star_Diagonal_1_25": {
            "brand": "Baader",
            "name": 'T-2 Star Diagonal (1.25")',
            "type": "type_diagonal",
            "optical_length": 0,
            "mass": 200,
            "tside_thread": '1.25"',
            "tside_gender": "Female",
            "cside_thread": '1.25"',
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Baader_Clicklock_Diagonal_2": {
            "brand": "Baader",
            "name": 'Clicklock Diagonal (2")',
            "type": "type_diagonal",
            "optical_length": 0,
            "mass": 500,
            "tside_thread": '2"',
            "tside_gender": "Female",
            "cside_thread": '2"',
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Baader_Prism_Diagonal_2": {
            "brand": "Baader",
            "name": 'Prism Diagonal (2")',
            "type": "type_diagonal",
            "optical_length": 0,
            "mass": 600,
            "tside_thread": '2"',
            "tside_gender": "Female",
            "cside_thread": '2"',
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Baader_Zeiss_Prism_Diagonal_1_25": {
            "brand": "Baader",
            "name": 'Zeiss Prism Diagonal (1.25")',
            "type": "type_diagonal",
            "optical_length": 0,
            "mass": 300,
            "tside_thread": '1.25"',
            "tside_gender": "Female",
            "cside_thread": '1.25"',
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Baader_Zeiss_Prism_Diagonal_2": {
            "brand": "Baader",
            "name": 'Zeiss Prism Diagonal (2")',
            "type": "type_diagonal",
            "optical_length": 0,
            "mass": 700,
            "tside_thread": '2"',
            "tside_gender": "Female",
            "cside_thread": '2"',
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "TeleVue_Everbrite_Diagonal_1_25": {
            "brand": "TeleVue",
            "name": 'Everbrite Diagonal (1.25")',
            "type": "type_diagonal",
            "optical_length": 0,
            "mass": 180,
            "tside_thread": '1.25"',
            "tside_gender": "Female",
            "cside_thread": '1.25"',
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "TeleVue_Everbrite_Diagonal_2": {
            "brand": "TeleVue",
            "name": 'Everbrite Diagonal (2")',
            "type": "type_diagonal",
            "optical_length": 0,
            "mass": 450,
            "tside_thread": '2"',
            "tside_gender": "Female",
            "cside_thread": '2"',
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Celestron_Dielectric_Diagonal_1_25": {
            "brand": "Celestron",
            "name": 'Dielectric Diagonal (1.25")',
            "type": "type_diagonal",
            "optical_length": 0,
            "mass": 150,
            "tside_thread": '1.25"',
            "tside_gender": "Female",
            "cside_thread": '1.25"',
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Celestron_Dielectric_Diagonal_2": {
            "brand": "Celestron",
            "name": 'Dielectric Diagonal (2")',
            "type": "type_diagonal",
            "optical_length": 0,
            "mass": 400,
            "tside_thread": '2"',
            "tside_gender": "Female",
            "cside_thread": '2"',
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Celestron_XLT_Diagonal_1_25": {
            "brand": "Celestron",
            "name": 'XLT Diagonal (1.25")',
            "type": "type_diagonal",
            "optical_length": 0,
            "mass": 160,
            "tside_thread": '1.25"',
            "tside_gender": "Female",
            "cside_thread": '1.25"',
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Celestron_XLT_Diagonal_2": {
            "brand": "Celestron",
            "name": 'XLT Diagonal (2")',
            "type": "type_diagonal",
            "optical_length": 0,
            "mass": 420,
            "tside_thread": '2"',
            "tside_gender": "Female",
            "cside_thread": '2"',
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Celestron_Mirror_Diagonal_1_25": {
            "brand": "Celestron",
            "name": 'Mirror Diagonal (1.25")',
            "type": "type_diagonal",
            "optical_length": 0,
            "mass": 120,
            "tside_thread": '1.25"',
            "tside_gender": "Female",
            "cside_thread": '1.25"',
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Celestron_Mirror_Diagonal_2": {
            "brand": "Celestron",
            "name": 'Mirror Diagonal (2")',
            "type": "type_diagonal",
            "optical_length": 0,
            "mass": 350,
            "tside_thread": '2"',
            "tside_gender": "Female",
            "cside_thread": '2"',
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "William_Optics_Dielectric_Diagonal_2": {
            "brand": "William Optics",
            "name": 'Dielectric Diagonal (2")',
            "type": "type_diagonal",
            "optical_length": 0,
            "mass": 500,
            "tside_thread": '2"',
            "tside_gender": "Female",
            "cside_thread": '2"',
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "William_Optics_Dielectric_Diagonal_1_25": {
            "brand": "William Optics",
            "name": 'Dielectric Diagonal (1.25")',
            "type": "type_diagonal",
            "optical_length": 0,
            "mass": 250,
            "tside_thread": '1.25"',
            "tside_gender": "Female",
            "cside_thread": '1.25"',
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Sky_Watcher_Silver_Diamond_Diagonal_1_25": {
            "brand": "Sky-Watcher",
            "name": 'Silver Diamond Diagonal (1.25")',
            "type": "type_diagonal",
            "optical_length": 0,
            "mass": 180,
            "tside_thread": '1.25"',
            "tside_gender": "Female",
            "cside_thread": '1.25"',
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Sky_Watcher_Silver_Diamond_Diagonal_2": {
            "brand": "Sky-Watcher",
            "name": 'Silver Diamond Diagonal (2")',
            "type": "type_diagonal",
            "optical_length": 0,
            "mass": 450,
            "tside_thread": '2"',
            "tside_gender": "Female",
            "cside_thread": '2"',
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Sky_Watcher_Ultra_HD_Diagonal_2": {
            "brand": "Sky-Watcher",
            "name": 'Ultra HD Diagonal (2")',
            "type": "type_diagonal",
            "optical_length": 0,
            "mass": 600,
            "tside_thread": '2"',
            "tside_gender": "Female",
            "cside_thread": '2"',
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Orion_Quartz_Mirror_Diagonal_1_25": {
            "brand": "Orion",
            "name": 'Quartz Mirror Diagonal (1.25")',
            "type": "type_diagonal",
            "optical_length": 0,
            "mass": 160,
            "tside_thread": '1.25"',
            "tside_gender": "Female",
            "cside_thread": '1.25"',
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Orion_Quartz_Mirror_Diagonal_2": {
            "brand": "Orion",
            "name": 'Quartz Mirror Diagonal (2")',
            "type": "type_diagonal",
            "optical_length": 0,
            "mass": 430,
            "tside_thread": '2"',
            "tside_gender": "Female",
            "cside_thread": '2"',
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Meade_Dielectric_Diagonal_1_25": {
            "brand": "Meade",
            "name": 'Dielectric Diagonal (1.25")',
            "type": "type_diagonal",
            "optical_length": 0,
            "mass": 140,
            "tside_thread": '1.25"',
            "tside_gender": "Female",
            "cside_thread": '1.25"',
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Meade_Dielectric_Diagonal_2": {
            "brand": "Meade",
            "name": 'Dielectric Diagonal (2")',
            "type": "type_diagonal",
            "optical_length": 0,
            "mass": 380,
            "tside_thread": '2"',
            "tside_gender": "Female",
            "cside_thread": '2"',
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "GSO_Erecting_Prism_1_25": {
            "brand": "GSO",
            "name": 'Erecting Prism (1.25")',
            "type": "type_diagonal",
            "optical_length": 0,
            "mass": 120,
            "tside_thread": '1.25"',
            "tside_gender": "Female",
            "cside_thread": '1.25"',
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "GSO_Mirror_Diagonal_2": {
            "brand": "GSO",
            "name": 'Mirror Diagonal (2")',
            "type": "type_diagonal",
            "optical_length": 0,
            "mass": 350,
            "tside_thread": '2"',
            "tside_gender": "Female",
            "cside_thread": '2"',
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Explore_Scientific_Diagonal_1_25": {
            "brand": "Explore Scientific",
            "name": 'Diagonal (1.25")',
            "type": "type_diagonal",
            "optical_length": 0,
            "mass": 130,
            "tside_thread": '1.25"',
            "tside_gender": "Female",
            "cside_thread": '1.25"',
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Explore_Scientific_Diagonal_2": {
            "brand": "Explore Scientific",
            "name": 'Diagonal (2")',
            "type": "type_diagonal",
            "optical_length": 0,
            "mass": 380,
            "tside_thread": '2"',
            "tside_gender": "Female",
            "cside_thread": '2"',
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Omegon_Dielectric_Diagonal_2": {
            "brand": "Omegon",
            "name": 'Dielectric Diagonal (2")',
            "type": "type_diagonal",
            "optical_length": 0,
            "mass": 400,
            "tside_thread": '2"',
            "tside_gender": "Female",
            "cside_thread": '2"',
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Bresser_Dielectric_Diagonal_2": {
            "brand": "Bresser",
            "name": 'Dielectric Diagonal (2")',
            "type": "type_diagonal",
            "optical_length": 0,
            "mass": 380,
            "tside_thread": '2"',
            "tside_gender": "Female",
            "cside_thread": '2"',
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Lacerta_Dielectric_Diagonal_2": {
            "brand": "Lacerta",
            "name": 'Dielectric Diagonal (2")',
            "type": "type_diagonal",
            "optical_length": 0,
            "mass": 420,
            "tside_thread": '2"',
            "tside_gender": "Female",
            "cside_thread": '2"',
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "SVBony_SV188P_Diagonal_1_25": {
            "brand": "SVBony",
            "name": 'SV188P Diagonal (1.25")',
            "type": "type_diagonal",
            "optical_length": 0,
            "mass": 130,
            "tside_thread": '1.25"',
            "tside_gender": "Female",
            "cside_thread": '1.25"',
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "SVBony_SV199P_Diagonal_2": {
            "brand": "SVBony",
            "name": 'SV199P Diagonal (2")',
            "type": "type_diagonal",
            "optical_length": 0,
            "mass": 350,
            "tside_thread": '2"',
            "tside_gender": "Female",
            "cside_thread": '2"',
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "TS_Optics_Dielectric_Diagonal_2": {
            "brand": "TS-Optics",
            "name": 'Dielectric Diagonal (2")',
            "type": "type_diagonal",
            "optical_length": 0,
            "mass": 400,
            "tside_thread": '2"',
            "tside_gender": "Female",
            "cside_thread": '2"',
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "TS_Optics_Dielectric_Diagonal_1_25": {
            "brand": "TS-Optics",
            "name": 'Dielectric Diagonal (1.25")',
            "type": "type_diagonal",
            "optical_length": 0,
            "mass": 170,
            "tside_thread": '1.25"',
            "tside_gender": "Female",
            "cside_thread": '1.25"',
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "National_Geographic_Mirror_Diagonal_1_25": {
            "brand": "National Geographic",
            "name": 'Mirror Diagonal (1.25")',
            "type": "type_diagonal",
            "optical_length": 0,
            "mass": 80,
            "tside_thread": '1.25"',
            "tside_gender": "Female",
            "cside_thread": '1.25"',
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Saxon_Mirror_Diagonal_1_25": {
            "brand": "Saxon",
            "name": 'Mirror Diagonal (1.25")',
            "type": "type_diagonal",
            "optical_length": 0,
            "mass": 90,
            "tside_thread": '1.25"',
            "tside_gender": "Female",
            "cside_thread": '1.25"',
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Saxon_Dielectric_Diagonal_2": {
            "brand": "Saxon",
            "name": 'Dielectric Diagonal (2")',
            "type": "type_diagonal",
            "optical_length": 0,
            "mass": 350,
            "tside_thread": '2"',
            "tside_gender": "Female",
            "cside_thread": '2"',
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Omegon_Mirror_Diagonal_1_25": {
            "brand": "Omegon",
            "name": 'Mirror Diagonal (1.25")',
            "type": "type_diagonal",
            "optical_length": 0,
            "mass": 100,
            "tside_thread": '1.25"',
            "tside_gender": "Female",
            "cside_thread": '1.25"',
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Vixen_Dielectric_Diagonal_1_25": {
            "brand": "Vixen",
            "name": 'Dielectric Diagonal (1.25")',
            "type": "type_diagonal",
            "optical_length": 0,
            "mass": 200,
            "tside_thread": '1.25"',
            "tside_gender": "Female",
            "cside_thread": '1.25"',
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Vixen_Dielectric_Diagonal_2": {
            "brand": "Vixen",
            "name": 'Dielectric Diagonal (2")',
            "type": "type_diagonal",
            "optical_length": 0,
            "mass": 480,
            "tside_thread": '2"',
            "tside_gender": "Female",
            "cside_thread": '2"',
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Vixen_SSW_Diagonal_2": {
            "brand": "Vixen",
            "name": 'SSW Diagonal (2")',
            "type": "type_diagonal",
            "optical_length": 0,
            "mass": 520,
            "tside_thread": '2"',
            "tside_gender": "Female",
            "cside_thread": '2"',
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Takahashi_Diagonal_1_25": {
            "brand": "Takahashi",
            "name": 'Diagonal (1.25")',
            "type": "type_diagonal",
            "optical_length": 0,
            "mass": 250,
            "tside_thread": '1.25"',
            "tside_gender": "Female",
            "cside_thread": '1.25"',
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Takahashi_Diagonal_2": {
            "brand": "Takahashi",
            "name": 'Diagonal (2")',
            "type": "type_diagonal",
            "optical_length": 0,
            "mass": 500,
            "tside_thread": '2"',
            "tside_gender": "Female",
            "cside_thread": '2"',
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Vixen_Enhanced_Aluminum_Diagonal_1_25": {
            "brand": "Vixen",
            "name": 'Enhanced Aluminum Diagonal (1.25")',
            "type": "type_diagonal",
            "optical_length": 0,
            "mass": 120,
            "tside_thread": '1.25"',
            "tside_gender": "Female",
            "cside_thread": '1.25"',
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Vixen_Enhanced_Aluminum_Diagonal_2": {
            "brand": "Vixen",
            "name": 'Enhanced Aluminum Diagonal (2")',
            "type": "type_diagonal",
            "optical_length": 0,
            "mass": 300,
            "tside_thread": '2"',
            "tside_gender": "Female",
            "cside_thread": '2"',
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Orion_Dielectric_Diagonal_1_25": {
            "brand": "Orion",
            "name": 'Dielectric Diagonal (1.25")',
            "type": "type_diagonal",
            "optical_length": 0,
            "mass": 160,
            "tside_thread": '1.25"',
            "tside_gender": "Female",
            "cside_thread": '1.25"',
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Orion_Dielectric_Diagonal_2": {
            "brand": "Orion",
            "name": 'Dielectric Diagonal (2")',
            "type": "type_diagonal",
            "optical_length": 0,
            "mass": 400,
            "tside_thread": '2"',
            "tside_gender": "Female",
            "cside_thread": '2"',
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Orion_Mirror_Diagonal_1_25": {
            "brand": "Orion",
            "name": 'Mirror Diagonal (1.25")',
            "type": "type_diagonal",
            "optical_length": 0,
            "mass": 100,
            "tside_thread": '1.25"',
            "tside_gender": "Female",
            "cside_thread": '1.25"',
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Orion_Mirror_Diagonal_2": {
            "brand": "Orion",
            "name": 'Mirror Diagonal (2")',
            "type": "type_diagonal",
            "optical_length": 0,
            "mass": 280,
            "tside_thread": '2"',
            "tside_gender": "Female",
            "cside_thread": '2"',
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Altair_Dielectric_Diagonal_1_25": {
            "brand": "Altair",
            "name": 'Dielectric Diagonal (1.25")',
            "type": "type_diagonal",
            "optical_length": 0,
            "mass": 140,
            "tside_thread": '1.25"',
            "tside_gender": "Female",
            "cside_thread": '1.25"',
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Altair_Dielectric_Diagonal_2": {
            "brand": "Altair",
            "name": 'Dielectric Diagonal (2")',
            "type": "type_diagonal",
            "optical_length": 0,
            "mass": 380,
            "tside_thread": '2"',
            "tside_gender": "Female",
            "cside_thread": '2"',
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "APM_Dielectric_Diagonal_1_25": {
            "brand": "APM",
            "name": 'Dielectric Diagonal (1.25")',
            "type": "type_diagonal",
            "optical_length": 0,
            "mass": 130,
            "tside_thread": '1.25"',
            "tside_gender": "Female",
            "cside_thread": '1.25"',
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "APM_Dielectric_Diagonal_2": {
            "brand": "APM",
            "name": 'Dielectric Diagonal (2")',
            "type": "type_diagonal",
            "optical_length": 0,
            "mass": 360,
            "tside_thread": '2"',
            "tside_gender": "Female",
            "cside_thread": '2"',
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Bresser_Mirror_Diagonal_1_25": {
            "brand": "Bresser",
            "name": 'Mirror Diagonal (1.25")',
            "type": "type_diagonal",
            "optical_length": 0,
            "mass": 100,
            "tside_thread": '1.25"',
            "tside_gender": "Female",
            "cside_thread": '1.25"',
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Bresser_Mirror_Diagonal_2": {
            "brand": "Bresser",
            "name": 'Mirror Diagonal (2")',
            "type": "type_diagonal",
            "optical_length": 0,
            "mass": 280,
            "tside_thread": '2"',
            "tside_gender": "Female",
            "cside_thread": '2"',
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "SVBony_Mirror_Diagonal_1_25": {
            "brand": "SVBony",
            "name": 'Mirror Diagonal (1.25")',
            "type": "type_diagonal",
            "optical_length": 0,
            "mass": 80,
            "tside_thread": '1.25"',
            "tside_gender": "Female",
            "cside_thread": '1.25"',
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "SVBony_Mirror_Diagonal_2": {
            "brand": "SVBony",
            "name": 'Mirror Diagonal (2")',
            "type": "type_diagonal",
            "optical_length": 0,
            "mass": 250,
            "tside_thread": '2"',
            "tside_gender": "Female",
            "cside_thread": '2"',
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Stellarvue_Dielectric_Diagonal_1_25": {
            "brand": "Stellarvue",
            "name": 'Dielectric Diagonal (1.25")',
            "type": "type_diagonal",
            "optical_length": 0,
            "mass": 140,
            "tside_thread": '1.25"',
            "tside_gender": "Female",
            "cside_thread": '1.25"',
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Stellarvue_Dielectric_Diagonal_2": {
            "brand": "Stellarvue",
            "name": 'Dielectric Diagonal (2")',
            "type": "type_diagonal",
            "optical_length": 0,
            "mass": 380,
            "tside_thread": '2"',
            "tside_gender": "Female",
            "cside_thread": '2"',
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Vixen_Dielectric_Diagonal_1_25_v2": {
            "brand": "Vixen",
            "name": 'Dielectric Diagonal (1.25")(v2)',
            "type": "type_diagonal",
            "optical_length": 0,
            "mass": 160,
            "tside_thread": '1.25"',
            "tside_gender": "Female",
            "cside_thread": '1.25"',
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Vixen_Dielectric_Diagonal_2_v2": {
            "brand": "Vixen",
            "name": 'Dielectric Diagonal (2")(v2)',
            "type": "type_diagonal",
            "optical_length": 0,
            "mass": 430,
            "tside_thread": '2"',
            "tside_gender": "Female",
            "cside_thread": '2"',
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Takahashi_Star_Diagonal_1_25": {
            "brand": "Takahashi",
            "name": 'Star Diagonal (1.25")',
            "type": "type_diagonal",
            "optical_length": 0,
            "mass": 250,
            "tside_thread": '1.25"',
            "tside_gender": "Female",
            "cside_thread": '1.25"',
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Takahashi_Star_Diagonal_2": {
            "brand": "Takahashi",
            "name": 'Star Diagonal (2")',
            "type": "type_diagonal",
            "optical_length": 0,
            "mass": 550,
            "tside_thread": '2"',
            "tside_gender": "Female",
            "cside_thread": '2"',
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Astro_Physics_MaxBright_Diagonal_2": {
            "brand": "Astro-Physics",
            "name": 'MaxBright Diagonal (2")',
            "type": "type_diagonal",
            "optical_length": 0,
            "mass": 700,
            "tside_thread": '2"',
            "tside_gender": "Female",
            "cside_thread": '2"',
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "TeleVue_Star_Diagonal_2": {
            "brand": "TeleVue",
            "name": 'Star Diagonal (2")',
            "type": "type_diagonal",
            "optical_length": 0,
            "mass": 500,
            "tside_thread": '2"',
            "tside_gender": "Female",
            "cside_thread": '2"',
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "TS_Optics_Dielectric_Diagonal_1_25_v2": {
            "brand": "TS-Optics",
            "name": 'Dielectric Diagonal (1.25") (v2)',
            "type": "type_diagonal",
            "optical_length": 0,
            "mass": 125,
            "tside_thread": '1.25"',
            "tside_gender": "Female",
            "cside_thread": '1.25"',
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "TS_Optics_Dielectric_Diagonal_2_v2": {
            "brand": "TS-Optics",
            "name": 'Dielectric Diagonal (2") (v2)',
            "type": "type_diagonal",
            "optical_length": 0,
            "mass": 355,
            "tside_thread": '2"',
            "tside_gender": "Female",
            "cside_thread": '2"',
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Omegon_Dielectric_Diagonal_1_25_v2": {
            "brand": "Omegon",
            "name": 'Dielectric Diagonal (1.25") (v2)',
            "type": "type_diagonal",
            "optical_length": 0,
            "mass": 155,
            "tside_thread": '1.25"',
            "tside_gender": "Female",
            "cside_thread": '1.25"',
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Omegon_Dielectric_Diagonal_2_v2": {
            "brand": "Omegon",
            "name": 'Dielectric Diagonal (2") (v2)',
            "type": "type_diagonal",
            "optical_length": 0,
            "mass": 405,
            "tside_thread": '2"',
            "tside_gender": "Female",
            "cside_thread": '2"',
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
    }

    @classmethod
    def Baader_T_2_Star_Diagonal_1_25(cls):
        return cls.from_database(cls._DATABASE["Baader_T_2_Star_Diagonal_1_25"])

    @classmethod
    def Baader_Clicklock_Diagonal_2(cls):
        return cls.from_database(cls._DATABASE["Baader_Clicklock_Diagonal_2"])

    @classmethod
    def Baader_Prism_Diagonal_2(cls):
        return cls.from_database(cls._DATABASE["Baader_Prism_Diagonal_2"])

    @classmethod
    def Baader_Zeiss_Prism_Diagonal_1_25(cls):
        return cls.from_database(cls._DATABASE["Baader_Zeiss_Prism_Diagonal_1_25"])

    @classmethod
    def Baader_Zeiss_Prism_Diagonal_2(cls):
        return cls.from_database(cls._DATABASE["Baader_Zeiss_Prism_Diagonal_2"])

    @classmethod
    def TeleVue_Everbrite_Diagonal_1_25(cls):
        return cls.from_database(cls._DATABASE["TeleVue_Everbrite_Diagonal_1_25"])

    @classmethod
    def TeleVue_Everbrite_Diagonal_2(cls):
        return cls.from_database(cls._DATABASE["TeleVue_Everbrite_Diagonal_2"])

    @classmethod
    def Celestron_Dielectric_Diagonal_1_25(cls):
        return cls.from_database(cls._DATABASE["Celestron_Dielectric_Diagonal_1_25"])

    @classmethod
    def Celestron_Dielectric_Diagonal_2(cls):
        return cls.from_database(cls._DATABASE["Celestron_Dielectric_Diagonal_2"])

    @classmethod
    def Celestron_XLT_Diagonal_1_25(cls):
        return cls.from_database(cls._DATABASE["Celestron_XLT_Diagonal_1_25"])

    @classmethod
    def Celestron_XLT_Diagonal_2(cls):
        return cls.from_database(cls._DATABASE["Celestron_XLT_Diagonal_2"])

    @classmethod
    def Celestron_Mirror_Diagonal_1_25(cls):
        return cls.from_database(cls._DATABASE["Celestron_Mirror_Diagonal_1_25"])

    @classmethod
    def Celestron_Mirror_Diagonal_2(cls):
        return cls.from_database(cls._DATABASE["Celestron_Mirror_Diagonal_2"])

    @classmethod
    def William_Optics_Dielectric_Diagonal_2(cls):
        return cls.from_database(cls._DATABASE["William_Optics_Dielectric_Diagonal_2"])

    @classmethod
    def William_Optics_Dielectric_Diagonal_1_25(cls):
        return cls.from_database(
            cls._DATABASE["William_Optics_Dielectric_Diagonal_1_25"]
        )

    @classmethod
    def Sky_Watcher_Silver_Diamond_Diagonal_1_25(cls):
        return cls.from_database(
            cls._DATABASE["Sky_Watcher_Silver_Diamond_Diagonal_1_25"]
        )

    @classmethod
    def Sky_Watcher_Silver_Diamond_Diagonal_2(cls):
        return cls.from_database(cls._DATABASE["Sky_Watcher_Silver_Diamond_Diagonal_2"])

    @classmethod
    def Sky_Watcher_Ultra_HD_Diagonal_2(cls):
        return cls.from_database(cls._DATABASE["Sky_Watcher_Ultra_HD_Diagonal_2"])

    @classmethod
    def Orion_Quartz_Mirror_Diagonal_1_25(cls):
        return cls.from_database(cls._DATABASE["Orion_Quartz_Mirror_Diagonal_1_25"])

    @classmethod
    def Orion_Quartz_Mirror_Diagonal_2(cls):
        return cls.from_database(cls._DATABASE["Orion_Quartz_Mirror_Diagonal_2"])

    @classmethod
    def Meade_Dielectric_Diagonal_1_25(cls):
        return cls.from_database(cls._DATABASE["Meade_Dielectric_Diagonal_1_25"])

    @classmethod
    def Meade_Dielectric_Diagonal_2(cls):
        return cls.from_database(cls._DATABASE["Meade_Dielectric_Diagonal_2"])

    @classmethod
    def GSO_Erecting_Prism_1_25(cls):
        return cls.from_database(cls._DATABASE["GSO_Erecting_Prism_1_25"])

    @classmethod
    def GSO_Mirror_Diagonal_2(cls):
        return cls.from_database(cls._DATABASE["GSO_Mirror_Diagonal_2"])

    @classmethod
    def Explore_Scientific_Diagonal_1_25(cls):
        return cls.from_database(cls._DATABASE["Explore_Scientific_Diagonal_1_25"])

    @classmethod
    def Explore_Scientific_Diagonal_2(cls):
        return cls.from_database(cls._DATABASE["Explore_Scientific_Diagonal_2"])

    @classmethod
    def Omegon_Dielectric_Diagonal_2(cls):
        return cls.from_database(cls._DATABASE["Omegon_Dielectric_Diagonal_2"])

    @classmethod
    def Bresser_Dielectric_Diagonal_2(cls):
        return cls.from_database(cls._DATABASE["Bresser_Dielectric_Diagonal_2"])

    @classmethod
    def Lacerta_Dielectric_Diagonal_2(cls):
        return cls.from_database(cls._DATABASE["Lacerta_Dielectric_Diagonal_2"])

    @classmethod
    def SVBony_SV188P_Diagonal_1_25(cls):
        return cls.from_database(cls._DATABASE["SVBony_SV188P_Diagonal_1_25"])

    @classmethod
    def SVBony_SV199P_Diagonal_2(cls):
        return cls.from_database(cls._DATABASE["SVBony_SV199P_Diagonal_2"])

    @classmethod
    def TS_Optics_Dielectric_Diagonal_2(cls):
        return cls.from_database(cls._DATABASE["TS_Optics_Dielectric_Diagonal_2"])

    @classmethod
    def TS_Optics_Dielectric_Diagonal_1_25(cls):
        return cls.from_database(cls._DATABASE["TS_Optics_Dielectric_Diagonal_1_25"])

    @classmethod
    def National_Geographic_Mirror_Diagonal_1_25(cls):
        return cls.from_database(
            cls._DATABASE["National_Geographic_Mirror_Diagonal_1_25"]
        )

    @classmethod
    def Saxon_Mirror_Diagonal_1_25(cls):
        return cls.from_database(cls._DATABASE["Saxon_Mirror_Diagonal_1_25"])

    @classmethod
    def Saxon_Dielectric_Diagonal_2(cls):
        return cls.from_database(cls._DATABASE["Saxon_Dielectric_Diagonal_2"])

    @classmethod
    def Omegon_Mirror_Diagonal_1_25(cls):
        return cls.from_database(cls._DATABASE["Omegon_Mirror_Diagonal_1_25"])

    @classmethod
    def Vixen_Dielectric_Diagonal_1_25(cls):
        return cls.from_database(cls._DATABASE["Vixen_Dielectric_Diagonal_1_25"])

    @classmethod
    def Vixen_Dielectric_Diagonal_2(cls):
        return cls.from_database(cls._DATABASE["Vixen_Dielectric_Diagonal_2"])

    @classmethod
    def Vixen_SSW_Diagonal_2(cls):
        return cls.from_database(cls._DATABASE["Vixen_SSW_Diagonal_2"])

    @classmethod
    def Takahashi_Diagonal_1_25(cls):
        return cls.from_database(cls._DATABASE["Takahashi_Diagonal_1_25"])

    @classmethod
    def Takahashi_Diagonal_2(cls):
        return cls.from_database(cls._DATABASE["Takahashi_Diagonal_2"])

    @classmethod
    def Vixen_Enhanced_Aluminum_Diagonal_1_25(cls):
        return cls.from_database(cls._DATABASE["Vixen_Enhanced_Aluminum_Diagonal_1_25"])

    @classmethod
    def Vixen_Enhanced_Aluminum_Diagonal_2(cls):
        return cls.from_database(cls._DATABASE["Vixen_Enhanced_Aluminum_Diagonal_2"])

    @classmethod
    def Orion_Dielectric_Diagonal_1_25(cls):
        return cls.from_database(cls._DATABASE["Orion_Dielectric_Diagonal_1_25"])

    @classmethod
    def Orion_Dielectric_Diagonal_2(cls):
        return cls.from_database(cls._DATABASE["Orion_Dielectric_Diagonal_2"])

    @classmethod
    def Orion_Mirror_Diagonal_1_25(cls):
        return cls.from_database(cls._DATABASE["Orion_Mirror_Diagonal_1_25"])

    @classmethod
    def Orion_Mirror_Diagonal_2(cls):
        return cls.from_database(cls._DATABASE["Orion_Mirror_Diagonal_2"])

    @classmethod
    def Altair_Dielectric_Diagonal_1_25(cls):
        return cls.from_database(cls._DATABASE["Altair_Dielectric_Diagonal_1_25"])

    @classmethod
    def Altair_Dielectric_Diagonal_2(cls):
        return cls.from_database(cls._DATABASE["Altair_Dielectric_Diagonal_2"])

    @classmethod
    def APM_Dielectric_Diagonal_1_25(cls):
        return cls.from_database(cls._DATABASE["APM_Dielectric_Diagonal_1_25"])

    @classmethod
    def APM_Dielectric_Diagonal_2(cls):
        return cls.from_database(cls._DATABASE["APM_Dielectric_Diagonal_2"])

    @classmethod
    def Bresser_Mirror_Diagonal_1_25(cls):
        return cls.from_database(cls._DATABASE["Bresser_Mirror_Diagonal_1_25"])

    @classmethod
    def Bresser_Mirror_Diagonal_2(cls):
        return cls.from_database(cls._DATABASE["Bresser_Mirror_Diagonal_2"])

    @classmethod
    def SVBony_Mirror_Diagonal_1_25(cls):
        return cls.from_database(cls._DATABASE["SVBony_Mirror_Diagonal_1_25"])

    @classmethod
    def SVBony_Mirror_Diagonal_2(cls):
        return cls.from_database(cls._DATABASE["SVBony_Mirror_Diagonal_2"])

    @classmethod
    def Stellarvue_Dielectric_Diagonal_1_25(cls):
        return cls.from_database(cls._DATABASE["Stellarvue_Dielectric_Diagonal_1_25"])

    @classmethod
    def Stellarvue_Dielectric_Diagonal_2(cls):
        return cls.from_database(cls._DATABASE["Stellarvue_Dielectric_Diagonal_2"])

    @classmethod
    def Vixen_Dielectric_Diagonal_1_25_v2(cls):
        return cls.from_database(cls._DATABASE["Vixen_Dielectric_Diagonal_1_25_v2"])

    @classmethod
    def Vixen_Dielectric_Diagonal_2_v2(cls):
        return cls.from_database(cls._DATABASE["Vixen_Dielectric_Diagonal_2_v2"])

    @classmethod
    def Takahashi_Star_Diagonal_1_25(cls):
        return cls.from_database(cls._DATABASE["Takahashi_Star_Diagonal_1_25"])

    @classmethod
    def Takahashi_Star_Diagonal_2(cls):
        return cls.from_database(cls._DATABASE["Takahashi_Star_Diagonal_2"])

    @classmethod
    def Astro_Physics_MaxBright_Diagonal_2(cls):
        return cls.from_database(cls._DATABASE["Astro_Physics_MaxBright_Diagonal_2"])

    @classmethod
    def TeleVue_Star_Diagonal_2(cls):
        return cls.from_database(cls._DATABASE["TeleVue_Star_Diagonal_2"])

    @classmethod
    def TS_Optics_Dielectric_Diagonal_1_25_v2(cls):
        return cls.from_database(cls._DATABASE["TS_Optics_Dielectric_Diagonal_1_25_v2"])

    @classmethod
    def TS_Optics_Dielectric_Diagonal_2_v2(cls):
        return cls.from_database(cls._DATABASE["TS_Optics_Dielectric_Diagonal_2_v2"])

    @classmethod
    def Omegon_Dielectric_Diagonal_1_25_v2(cls):
        return cls.from_database(cls._DATABASE["Omegon_Dielectric_Diagonal_1_25_v2"])

    @classmethod
    def Omegon_Dielectric_Diagonal_2_v2(cls):
        return cls.from_database(cls._DATABASE["Omegon_Dielectric_Diagonal_2_v2"])
