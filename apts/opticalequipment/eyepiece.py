from .abstract import OutputOpticalEqipment
from ..constants import GraphConstants, OpticalType

from ..units import get_unit_registry
from ..utils import ConnectionType, Gender


class Eyepiece(OutputOpticalEqipment):
    @classmethod
    def from_database(cls, entry):
        from ..utils import Utils, Gender

        brand = entry["brand"]
        name = entry["name"]
        vendor = f"{brand} {name}"
        tt = Utils.map_conn(entry.get("tside_thread"))
        tg = Utils.map_gender(entry.get("tside_gender"))
        fl = Utils.extract_number(name) or 20
        return cls(
            fl, vendor=vendor, connection_type=tt, connection_gender=tg or Gender.MALE
        )
        from ..utils import Utils, Gender

        brand = entry["brand"]
        name = entry["name"]
        vendor = f"{brand} {name}"
        tt = Utils.map_conn(entry.get("tside_thread"))
        tg = Utils.map_gender(entry.get("tside_gender"))
        fl = Utils.extract_number(name) or 20
        return cls(
            fl, vendor=vendor, connection_type=tt, connection_gender=tg or Gender.MALE
        )

    """
  Class representing ocular
  """

    def __init__(
        self,
        focal_length,
        vendor="unknown ocular",
        field_of_view=70,
        connection_type=ConnectionType.F_1_25,
        connection_gender=Gender.MALE,
        mass=0,
        optical_length=0,
    ):
        super(Eyepiece, self).__init__(
            focal_length, vendor, mass=mass, optical_length=optical_length
        )
        self._connection_type = connection_type
        self._connection_gender = connection_gender
        self._field_of_view = field_of_view * get_unit_registry().deg

    def _zoom_divider(self):
        return self.focal_length

    def field_of_view(self, telescop, zoom, barlow_magnification):
        return self._field_of_view / zoom

    def output_type(self):
        return OpticalType.VISUAL

    def register(self, equipment):
        """
        Register ocular in optical equipment graph. Ocular node is build out of two vertices:
        ocular node and its input. Ocular node is automatically connected with output IMAGE node.
        """
        # Add ocular node
        super(Eyepiece, self)._register(equipment)
        # Add ocular input node and connect it to ocular
        self._register_input(equipment, self._connection_type, self._connection_gender)
        # Connect ocular with output eye node
        equipment.add_edge(self.id(), GraphConstants.EYE_ID)

    def __str__(self):
        return "{} f={}".format(self.get_vendor(), self.focal_length.magnitude)
        # Format: <vendor> f=<focal_length>

    _DATABASE = {
        "TeleVue_Ethos_3_7mm": {
            "brand": "TeleVue",
            "name": "Ethos 3.7mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 335,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "TeleVue_Ethos_6mm": {
            "brand": "TeleVue",
            "name": "Ethos 6mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 340,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "TeleVue_Ethos_8mm": {
            "brand": "TeleVue",
            "name": "Ethos 8mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 350,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "TeleVue_Ethos_10mm": {
            "brand": "TeleVue",
            "name": "Ethos 10mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 356,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "TeleVue_Ethos_13mm": {
            "brand": "TeleVue",
            "name": "Ethos 13mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 590,
            "tside_thread": '2"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "TeleVue_Ethos_17mm": {
            "brand": "TeleVue",
            "name": "Ethos 17mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 600,
            "tside_thread": '2"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "TeleVue_Ethos_21mm": {
            "brand": "TeleVue",
            "name": "Ethos 21mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 620,
            "tside_thread": '2"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "TeleVue_Nagler_3_5mm": {
            "brand": "TeleVue",
            "name": "Nagler 3.5mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 175,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "TeleVue_Nagler_5mm": {
            "brand": "TeleVue",
            "name": "Nagler 5mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 180,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "TeleVue_Nagler_7mm": {
            "brand": "TeleVue",
            "name": "Nagler 7mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 190,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "TeleVue_Nagler_9mm": {
            "brand": "TeleVue",
            "name": "Nagler 9mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 200,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "TeleVue_Nagler_11mm": {
            "brand": "TeleVue",
            "name": "Nagler 11mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 210,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "TeleVue_Nagler_13mm": {
            "brand": "TeleVue",
            "name": "Nagler 13mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 240,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "TeleVue_Nagler_16mm": {
            "brand": "TeleVue",
            "name": "Nagler 16mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 430,
            "tside_thread": '2"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "TeleVue_Nagler_22mm": {
            "brand": "TeleVue",
            "name": "Nagler 22mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 550,
            "tside_thread": '2"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "TeleVue_Nagler_31mm": {
            "brand": "TeleVue",
            "name": "Nagler 31mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 850,
            "tside_thread": '2"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "TeleVue_Delos_3_5mm": {
            "brand": "TeleVue",
            "name": "Delos 3.5mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 195,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "TeleVue_Delos_6mm": {
            "brand": "TeleVue",
            "name": "Delos 6mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 215,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "TeleVue_Delos_8mm": {
            "brand": "TeleVue",
            "name": "Delos 8mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 230,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "TeleVue_Delos_10mm": {
            "brand": "TeleVue",
            "name": "Delos 10mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 250,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "TeleVue_Delos_12mm": {
            "brand": "TeleVue",
            "name": "Delos 12mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 265,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "TeleVue_Delos_14mm": {
            "brand": "TeleVue",
            "name": "Delos 14mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 280,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "TeleVue_Delos_17_3mm": {
            "brand": "TeleVue",
            "name": "Delos 17.3mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 310,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "TeleVue_Panoptic_15mm": {
            "brand": "TeleVue",
            "name": "Panoptic 15mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 260,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "TeleVue_Panoptic_19mm": {
            "brand": "TeleVue",
            "name": "Panoptic 19mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 310,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "TeleVue_Panoptic_22mm": {
            "brand": "TeleVue",
            "name": "Panoptic 22mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 350,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "TeleVue_Panoptic_24mm": {
            "brand": "TeleVue",
            "name": "Panoptic 24mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 380,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "TeleVue_Panoptic_27mm": {
            "brand": "TeleVue",
            "name": "Panoptic 27mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 430,
            "tside_thread": '2"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "TeleVue_Panoptic_35mm": {
            "brand": "TeleVue",
            "name": "Panoptic 35mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 750,
            "tside_thread": '2"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "TeleVue_Panoptic_41mm": {
            "brand": "TeleVue",
            "name": "Panoptic 41mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 850,
            "tside_thread": '2"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "TeleVue_Plossl_8mm": {
            "brand": "TeleVue",
            "name": "Plossl 8mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 130,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "TeleVue_Plossl_11mm": {
            "brand": "TeleVue",
            "name": "Plossl 11mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 135,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "TeleVue_Plossl_15mm": {
            "brand": "TeleVue",
            "name": "Plossl 15mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 140,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "TeleVue_Plossl_20mm": {
            "brand": "TeleVue",
            "name": "Plossl 20mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 150,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "TeleVue_Plossl_25mm": {
            "brand": "TeleVue",
            "name": "Plossl 25mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 160,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "TeleVue_Plossl_32mm": {
            "brand": "TeleVue",
            "name": "Plossl 32mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 180,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "TeleVue_Plossl_40mm": {
            "brand": "TeleVue",
            "name": "Plossl 40mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 200,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "TeleVue_Radian_3mm": {
            "brand": "TeleVue",
            "name": "Radian 3mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 195,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "TeleVue_Radian_4mm": {
            "brand": "TeleVue",
            "name": "Radian 4mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 195,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "TeleVue_Radian_5mm": {
            "brand": "TeleVue",
            "name": "Radian 5mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 195,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "TeleVue_Radian_6mm": {
            "brand": "TeleVue",
            "name": "Radian 6mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 195,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "TeleVue_Radian_8mm": {
            "brand": "TeleVue",
            "name": "Radian 8mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 195,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "TeleVue_Radian_10mm": {
            "brand": "TeleVue",
            "name": "Radian 10mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 195,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "TeleVue_Radian_12mm": {
            "brand": "TeleVue",
            "name": "Radian 12mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 195,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "TeleVue_Radian_14mm": {
            "brand": "TeleVue",
            "name": "Radian 14mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 195,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "TeleVue_Radian_18mm": {
            "brand": "TeleVue",
            "name": "Radian 18mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 195,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Baader_Hyperion_5mm": {
            "brand": "Baader",
            "name": "Hyperion 5mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 170,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Baader_Hyperion_8mm": {
            "brand": "Baader",
            "name": "Hyperion 8mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 180,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Baader_Hyperion_10mm": {
            "brand": "Baader",
            "name": "Hyperion 10mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 190,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Baader_Hyperion_13mm": {
            "brand": "Baader",
            "name": "Hyperion 13mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 200,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Baader_Hyperion_17mm": {
            "brand": "Baader",
            "name": "Hyperion 17mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 220,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Baader_Hyperion_21mm": {
            "brand": "Baader",
            "name": "Hyperion 21mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 240,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Baader_Hyperion_24mm": {
            "brand": "Baader",
            "name": "Hyperion 24mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 260,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Baader_Hyperion_36mm": {
            "brand": "Baader",
            "name": "Hyperion 36mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 400,
            "tside_thread": '2"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Baader_Morpheus_4_5mm": {
            "brand": "Baader",
            "name": "Morpheus 4.5mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 200,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Baader_Morpheus_6_5mm": {
            "brand": "Baader",
            "name": "Morpheus 6.5mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 220,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Baader_Morpheus_9mm": {
            "brand": "Baader",
            "name": "Morpheus 9mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 230,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Baader_Morpheus_12_5mm": {
            "brand": "Baader",
            "name": "Morpheus 12.5mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 250,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Baader_Morpheus_14mm": {
            "brand": "Baader",
            "name": "Morpheus 14mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 260,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Baader_Morpheus_17_5mm": {
            "brand": "Baader",
            "name": "Morpheus 17.5mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 280,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Baader_Classic_Ortho_6mm": {
            "brand": "Baader",
            "name": "Classic Ortho 6mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 80,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Baader_Classic_Ortho_10mm": {
            "brand": "Baader",
            "name": "Classic Ortho 10mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 85,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Baader_Classic_Ortho_18mm": {
            "brand": "Baader",
            "name": "Classic Ortho 18mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 90,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Explore_Scientific_4_5mm_82": {
            "brand": "Explore Scientific",
            "name": "4.5mm 82°",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 190,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Explore_Scientific_6_5mm_82": {
            "brand": "Explore Scientific",
            "name": "6.5mm 82°",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 200,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Explore_Scientific_8_8mm_82": {
            "brand": "Explore Scientific",
            "name": "8.8mm 82°",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 210,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Explore_Scientific_11mm_82": {
            "brand": "Explore Scientific",
            "name": "11mm 82°",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 220,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Explore_Scientific_14mm_82": {
            "brand": "Explore Scientific",
            "name": "14mm 82°",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 240,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Explore_Scientific_18mm_82": {
            "brand": "Explore Scientific",
            "name": "18mm 82°",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 280,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Explore_Scientific_24mm_82": {
            "brand": "Explore Scientific",
            "name": "24mm 82°",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 400,
            "tside_thread": '2"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Explore_Scientific_30mm_82": {
            "brand": "Explore Scientific",
            "name": "30mm 82°",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 550,
            "tside_thread": '2"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Explore_Scientific_5_5mm_62": {
            "brand": "Explore Scientific",
            "name": "5.5mm 62°",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 120,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Explore_Scientific_9mm_62": {
            "brand": "Explore Scientific",
            "name": "9mm 62°",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 130,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Explore_Scientific_14mm_62": {
            "brand": "Explore Scientific",
            "name": "14mm 62°",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 150,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Explore_Scientific_20mm_62": {
            "brand": "Explore Scientific",
            "name": "20mm 62°",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 170,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Explore_Scientific_26mm_62": {
            "brand": "Explore Scientific",
            "name": "26mm 62°",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 200,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Explore_Scientific_32mm_62": {
            "brand": "Explore Scientific",
            "name": "32mm 62°",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 300,
            "tside_thread": '2"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Explore_Scientific_40mm_62": {
            "brand": "Explore Scientific",
            "name": "40mm 62°",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 500,
            "tside_thread": '2"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Explore_Scientific_5_5mm_100": {
            "brand": "Explore Scientific",
            "name": "5.5mm 100°",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 280,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Explore_Scientific_9mm_100": {
            "brand": "Explore Scientific",
            "name": "9mm 100°",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 300,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Explore_Scientific_14mm_100": {
            "brand": "Explore Scientific",
            "name": "14mm 100°",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 550,
            "tside_thread": '2"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Explore_Scientific_20mm_100": {
            "brand": "Explore Scientific",
            "name": "20mm 100°",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 800,
            "tside_thread": '2"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Explore_Scientific_25mm_100": {
            "brand": "Explore Scientific",
            "name": "25mm 100°",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 900,
            "tside_thread": '2"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Explore_Scientific_16mm_68": {
            "brand": "Explore Scientific",
            "name": "16mm 68°",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 230,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Explore_Scientific_20mm_68": {
            "brand": "Explore Scientific",
            "name": "20mm 68°",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 260,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Explore_Scientific_24mm_68": {
            "brand": "Explore Scientific",
            "name": "24mm 68°",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 300,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Explore_Scientific_28mm_68": {
            "brand": "Explore Scientific",
            "name": "28mm 68°",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 350,
            "tside_thread": '2"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Explore_Scientific_34mm_68": {
            "brand": "Explore Scientific",
            "name": "34mm 68°",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 550,
            "tside_thread": '2"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Explore_Scientific_40mm_68": {
            "brand": "Explore Scientific",
            "name": "40mm 68°",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 700,
            "tside_thread": '2"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Celestron_Luminos_7mm": {
            "brand": "Celestron",
            "name": "Luminos 7mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 250,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Celestron_Luminos_10mm": {
            "brand": "Celestron",
            "name": "Luminos 10mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 260,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Celestron_Luminos_15mm": {
            "brand": "Celestron",
            "name": "Luminos 15mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 400,
            "tside_thread": '2"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Celestron_Luminos_19mm": {
            "brand": "Celestron",
            "name": "Luminos 19mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 420,
            "tside_thread": '2"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Celestron_Luminos_23mm": {
            "brand": "Celestron",
            "name": "Luminos 23mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 450,
            "tside_thread": '2"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Celestron_Luminos_31mm": {
            "brand": "Celestron",
            "name": "Luminos 31mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 700,
            "tside_thread": '2"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Celestron_X_Cel_LX_2_3mm": {
            "brand": "Celestron",
            "name": "X-Cel LX 2.3mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 120,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Celestron_X_Cel_LX_5mm": {
            "brand": "Celestron",
            "name": "X-Cel LX 5mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 130,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Celestron_X_Cel_LX_7mm": {
            "brand": "Celestron",
            "name": "X-Cel LX 7mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 140,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Celestron_X_Cel_LX_9mm": {
            "brand": "Celestron",
            "name": "X-Cel LX 9mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 150,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Celestron_X_Cel_LX_12mm": {
            "brand": "Celestron",
            "name": "X-Cel LX 12mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 165,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Celestron_X_Cel_LX_18mm": {
            "brand": "Celestron",
            "name": "X-Cel LX 18mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 180,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Celestron_X_Cel_LX_25mm": {
            "brand": "Celestron",
            "name": "X-Cel LX 25mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 200,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Celestron_Plossl_6mm": {
            "brand": "Celestron",
            "name": "Plossl 6mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 100,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Celestron_Plossl_8mm": {
            "brand": "Celestron",
            "name": "Plossl 8mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 105,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Celestron_Plossl_10mm": {
            "brand": "Celestron",
            "name": "Plossl 10mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 110,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Celestron_Plossl_15mm": {
            "brand": "Celestron",
            "name": "Plossl 15mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 120,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Celestron_Plossl_17mm": {
            "brand": "Celestron",
            "name": "Plossl 17mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 125,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Celestron_Plossl_20mm": {
            "brand": "Celestron",
            "name": "Plossl 20mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 130,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Celestron_Plossl_25mm": {
            "brand": "Celestron",
            "name": "Plossl 25mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 140,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Celestron_Plossl_32mm": {
            "brand": "Celestron",
            "name": "Plossl 32mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 160,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Celestron_Plossl_40mm": {
            "brand": "Celestron",
            "name": "Plossl 40mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 200,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Pentax_XW_3_5mm": {
            "brand": "Pentax",
            "name": "XW 3.5mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 260,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Pentax_XW_5mm": {
            "brand": "Pentax",
            "name": "XW 5mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 265,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Pentax_XW_7mm": {
            "brand": "Pentax",
            "name": "XW 7mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 270,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Pentax_XW_10mm": {
            "brand": "Pentax",
            "name": "XW 10mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 280,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Pentax_XW_14mm": {
            "brand": "Pentax",
            "name": "XW 14mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 290,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Pentax_XW_20mm": {
            "brand": "Pentax",
            "name": "XW 20mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 310,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Pentax_XW_30mm": {
            "brand": "Pentax",
            "name": "XW 30mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 530,
            "tside_thread": '2"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Pentax_XW_40mm": {
            "brand": "Pentax",
            "name": "XW 40mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 680,
            "tside_thread": '2"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Nikon_NAV_SW_10mm": {
            "brand": "Nikon",
            "name": "NAV-SW 10mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 600,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Nikon_NAV_SW_12_5mm": {
            "brand": "Nikon",
            "name": "NAV-SW 12.5mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 620,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Nikon_NAV_SW_17mm": {
            "brand": "Nikon",
            "name": "NAV-SW 17mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 640,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Nikon_NAV_HW_12_5mm": {
            "brand": "Nikon",
            "name": "NAV-HW 12.5mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 650,
            "tside_thread": '2"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Vixen_SSW_3_5mm": {
            "brand": "Vixen",
            "name": "SSW 3.5mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 270,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Vixen_SSW_5mm": {
            "brand": "Vixen",
            "name": "SSW 5mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 275,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Vixen_SSW_7mm": {
            "brand": "Vixen",
            "name": "SSW 7mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 280,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Vixen_SSW_10mm": {
            "brand": "Vixen",
            "name": "SSW 10mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 285,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Vixen_SSW_14mm": {
            "brand": "Vixen",
            "name": "SSW 14mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 290,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Vixen_SLV_2_5mm": {
            "brand": "Vixen",
            "name": "SLV 2.5mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 180,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Vixen_SLV_4mm": {
            "brand": "Vixen",
            "name": "SLV 4mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 185,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Vixen_SLV_6mm": {
            "brand": "Vixen",
            "name": "SLV 6mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 190,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Vixen_SLV_9mm": {
            "brand": "Vixen",
            "name": "SLV 9mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 195,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Vixen_SLV_10mm": {
            "brand": "Vixen",
            "name": "SLV 10mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 200,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Vixen_SLV_12mm": {
            "brand": "Vixen",
            "name": "SLV 12mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 210,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Vixen_SLV_15mm": {
            "brand": "Vixen",
            "name": "SLV 15mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 220,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Vixen_SLV_20mm": {
            "brand": "Vixen",
            "name": "SLV 20mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 240,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Vixen_SLV_25mm": {
            "brand": "Vixen",
            "name": "SLV 25mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 260,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Vixen_NLV_4mm": {
            "brand": "Vixen",
            "name": "NLV 4mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 140,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Vixen_NLV_5mm": {
            "brand": "Vixen",
            "name": "NLV 5mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 142,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Vixen_NLV_6mm": {
            "brand": "Vixen",
            "name": "NLV 6mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 145,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Vixen_NLV_8mm": {
            "brand": "Vixen",
            "name": "NLV 8mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 150,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Vixen_NLV_10mm": {
            "brand": "Vixen",
            "name": "NLV 10mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 155,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Vixen_NLV_12mm": {
            "brand": "Vixen",
            "name": "NLV 12mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 160,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Vixen_NLV_15mm": {
            "brand": "Vixen",
            "name": "NLV 15mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 170,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Vixen_NLV_20mm": {
            "brand": "Vixen",
            "name": "NLV 20mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 180,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Vixen_NLV_25mm": {
            "brand": "Vixen",
            "name": "NLV 25mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 200,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Meade_Series_5000_HD_60_5_5mm": {
            "brand": "Meade",
            "name": "Series 5000 HD-60 5.5mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 200,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Meade_Series_5000_HD_60_8_8mm": {
            "brand": "Meade",
            "name": "Series 5000 HD-60 8.8mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 210,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Meade_Series_5000_HD_60_14mm": {
            "brand": "Meade",
            "name": "Series 5000 HD-60 14mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 230,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Meade_Series_5000_HD_60_18mm": {
            "brand": "Meade",
            "name": "Series 5000 HD-60 18mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 250,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Meade_Series_5000_HD_60_24mm": {
            "brand": "Meade",
            "name": "Series 5000 HD-60 24mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 300,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Meade_Series_5000_HD_60_32mm": {
            "brand": "Meade",
            "name": "Series 5000 HD-60 32mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 500,
            "tside_thread": '2"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Meade_Series_5000_HD_60_40mm": {
            "brand": "Meade",
            "name": "Series 5000 HD-60 40mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 700,
            "tside_thread": '2"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Meade_Series_5000_UWA_5_5mm": {
            "brand": "Meade",
            "name": "Series 5000 UWA 5.5mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 250,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Meade_Series_5000_UWA_8_8mm": {
            "brand": "Meade",
            "name": "Series 5000 UWA 8.8mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 260,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Meade_Series_5000_UWA_14mm": {
            "brand": "Meade",
            "name": "Series 5000 UWA 14mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 280,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Meade_Series_5000_UWA_18mm": {
            "brand": "Meade",
            "name": "Series 5000 UWA 18mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 300,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Meade_Series_5000_UWA_24mm": {
            "brand": "Meade",
            "name": "Series 5000 UWA 24mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 350,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Meade_Series_4000_Plossl_6_4mm": {
            "brand": "Meade",
            "name": "Series 4000 Plossl 6.4mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 100,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Meade_Series_4000_Plossl_9_7mm": {
            "brand": "Meade",
            "name": "Series 4000 Plossl 9.7mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 110,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Meade_Series_4000_Plossl_12_4mm": {
            "brand": "Meade",
            "name": "Series 4000 Plossl 12.4mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 120,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Meade_Series_4000_Plossl_15mm": {
            "brand": "Meade",
            "name": "Series 4000 Plossl 15mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 125,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Meade_Series_4000_Plossl_20mm": {
            "brand": "Meade",
            "name": "Series 4000 Plossl 20mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 135,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Meade_Series_4000_Plossl_26mm": {
            "brand": "Meade",
            "name": "Series 4000 Plossl 26mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 155,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Meade_Series_4000_Plossl_32mm": {
            "brand": "Meade",
            "name": "Series 4000 Plossl 32mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 170,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Meade_Series_4000_Plossl_40mm": {
            "brand": "Meade",
            "name": "Series 4000 Plossl 40mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 200,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "William_Optics_SWAN_3_5mm": {
            "brand": "William Optics",
            "name": "SWAN 3.5mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 170,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "William_Optics_SWAN_7mm": {
            "brand": "William Optics",
            "name": "SWAN 7mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 185,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "William_Optics_SWAN_11mm": {
            "brand": "William Optics",
            "name": "SWAN 11mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 200,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "William_Optics_SWAN_16mm": {
            "brand": "William Optics",
            "name": "SWAN 16mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 230,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "William_Optics_SWAN_20mm": {
            "brand": "William Optics",
            "name": "SWAN 20mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 250,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "William_Optics_SWAN_33mm": {
            "brand": "William Optics",
            "name": "SWAN 33mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 500,
            "tside_thread": '2"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "William_Optics_UWAN_3mm": {
            "brand": "William Optics",
            "name": "UWAN 3mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 200,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "William_Optics_UWAN_6mm": {
            "brand": "William Optics",
            "name": "UWAN 6mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 210,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "William_Optics_UWAN_10mm": {
            "brand": "William Optics",
            "name": "UWAN 10mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 230,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "William_Optics_UWAN_15mm": {
            "brand": "William Optics",
            "name": "UWAN 15mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 250,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "William_Optics_UWAN_20mm": {
            "brand": "William Optics",
            "name": "UWAN 20mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 270,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "William_Optics_SPL_3mm": {
            "brand": "William Optics",
            "name": "SPL 3mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 160,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "William_Optics_SPL_6mm": {
            "brand": "William Optics",
            "name": "SPL 6mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 165,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "William_Optics_SPL_10mm": {
            "brand": "William Optics",
            "name": "SPL 10mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 175,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "William_Optics_SPL_15mm": {
            "brand": "William Optics",
            "name": "SPL 15mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 185,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "William_Optics_SPL_20mm": {
            "brand": "William Optics",
            "name": "SPL 20mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 195,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "APM_XWA_3_5mm_100": {
            "brand": "APM",
            "name": "XWA 3.5mm 100°",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 320,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "APM_XWA_7mm_100": {
            "brand": "APM",
            "name": "XWA 7mm 100°",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 340,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "APM_XWA_9mm_100": {
            "brand": "APM",
            "name": "XWA 9mm 100°",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 360,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "APM_XWA_13mm_100": {
            "brand": "APM",
            "name": "XWA 13mm 100°",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 380,
            "tside_thread": '2"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "APM_XWA_20mm_100": {
            "brand": "APM",
            "name": "XWA 20mm 100°",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 600,
            "tside_thread": '2"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "APM_HDC_4mm": {
            "brand": "APM",
            "name": "HDC 4mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 140,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "APM_HDC_6mm": {
            "brand": "APM",
            "name": "HDC 6mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 145,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "APM_HDC_9mm": {
            "brand": "APM",
            "name": "HDC 9mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 150,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "APM_HDC_12mm": {
            "brand": "APM",
            "name": "HDC 12mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 160,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "APM_HDC_18mm": {
            "brand": "APM",
            "name": "HDC 18mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 180,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "APM_HDC_25mm": {
            "brand": "APM",
            "name": "HDC 25mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 210,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Sky_Watcher_Aero_ED_2mm": {
            "brand": "Sky-Watcher",
            "name": "Aero ED 2mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 180,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Sky_Watcher_Aero_ED_3_5mm": {
            "brand": "Sky-Watcher",
            "name": "Aero ED 3.5mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 190,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Sky_Watcher_Aero_ED_5mm": {
            "brand": "Sky-Watcher",
            "name": "Aero ED 5mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 200,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Sky_Watcher_Aero_ED_7mm": {
            "brand": "Sky-Watcher",
            "name": "Aero ED 7mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 210,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Sky_Watcher_Aero_ED_9mm": {
            "brand": "Sky-Watcher",
            "name": "Aero ED 9mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 220,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Sky_Watcher_Aero_ED_11mm": {
            "brand": "Sky-Watcher",
            "name": "Aero ED 11mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 230,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Sky_Watcher_Aero_ED_15mm": {
            "brand": "Sky-Watcher",
            "name": "Aero ED 15mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 250,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Sky_Watcher_Aero_ED_20mm": {
            "brand": "Sky-Watcher",
            "name": "Aero ED 20mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 280,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Sky_Watcher_Nirvana_UWA_15mm": {
            "brand": "Sky-Watcher",
            "name": "Nirvana UWA 15mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 350,
            "tside_thread": '2"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Sky_Watcher_Nirvana_UWA_20mm": {
            "brand": "Sky-Watcher",
            "name": "Nirvana UWA 20mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 400,
            "tside_thread": '2"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Sky_Watcher_Nirvana_UWA_23mm": {
            "brand": "Sky-Watcher",
            "name": "Nirvana UWA 23mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 450,
            "tside_thread": '2"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Sky_Watcher_Nirvana_UWA_31mm": {
            "brand": "Sky-Watcher",
            "name": "Nirvana UWA 31mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 550,
            "tside_thread": '2"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Sky_Watcher_Super_Plossl_6mm": {
            "brand": "Sky-Watcher",
            "name": "Super Plossl 6mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 90,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Sky_Watcher_Super_Plossl_10mm": {
            "brand": "Sky-Watcher",
            "name": "Super Plossl 10mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 95,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Sky_Watcher_Super_Plossl_15mm": {
            "brand": "Sky-Watcher",
            "name": "Super Plossl 15mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 100,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Sky_Watcher_Super_Plossl_20mm": {
            "brand": "Sky-Watcher",
            "name": "Super Plossl 20mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 110,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Sky_Watcher_Super_Plossl_25mm": {
            "brand": "Sky-Watcher",
            "name": "Super Plossl 25mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 120,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Sky_Watcher_Super_Plossl_32mm": {
            "brand": "Sky-Watcher",
            "name": "Super Plossl 32mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 150,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "SVBony_SV131_4mm_68": {
            "brand": "SVBony",
            "name": "SV131 4mm 68°",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 110,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "SVBony_SV131_6mm_68": {
            "brand": "SVBony",
            "name": "SV131 6mm 68°",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 115,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "SVBony_SV131_9mm_68": {
            "brand": "SVBony",
            "name": "SV131 9mm 68°",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 120,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "SVBony_SV131_12mm_68": {
            "brand": "SVBony",
            "name": "SV131 12mm 68°",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 130,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "SVBony_SV131_15mm_68": {
            "brand": "SVBony",
            "name": "SV131 15mm 68°",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 140,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "SVBony_SV131_20mm_68": {
            "brand": "SVBony",
            "name": "SV131 20mm 68°",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 160,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "SVBony_SV131_25mm_68": {
            "brand": "SVBony",
            "name": "SV131 25mm 68°",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 180,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "SVBony_SV190_3_2mm_82": {
            "brand": "SVBony",
            "name": "SV190 3.2mm 82°",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 150,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "SVBony_SV190_5mm_82": {
            "brand": "SVBony",
            "name": "SV190 5mm 82°",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 155,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "SVBony_SV190_7mm_82": {
            "brand": "SVBony",
            "name": "SV190 7mm 82°",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 160,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "SVBony_SV190_9mm_82": {
            "brand": "SVBony",
            "name": "SV190 9mm 82°",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 170,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "SVBony_SV190_11mm_82": {
            "brand": "SVBony",
            "name": "SV190 11mm 82°",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 180,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "SVBony_SV190_15mm_82": {
            "brand": "SVBony",
            "name": "SV190 15mm 82°",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 200,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "SVBony_SV190_20mm_82": {
            "brand": "SVBony",
            "name": "SV190 20mm 82°",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 220,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Orion_Stratus_5mm": {
            "brand": "Orion",
            "name": "Stratus 5mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 130,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Orion_Stratus_7mm": {
            "brand": "Orion",
            "name": "Stratus 7mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 135,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Orion_Stratus_10mm": {
            "brand": "Orion",
            "name": "Stratus 10mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 145,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Orion_Stratus_12_5mm": {
            "brand": "Orion",
            "name": "Stratus 12.5mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 155,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Orion_Stratus_15mm": {
            "brand": "Orion",
            "name": "Stratus 15mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 165,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Orion_Stratus_18mm": {
            "brand": "Orion",
            "name": "Stratus 18mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 180,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Orion_Stratus_20mm": {
            "brand": "Orion",
            "name": "Stratus 20mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 190,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Orion_Stratus_25mm": {
            "brand": "Orion",
            "name": "Stratus 25mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 210,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Orion_Edge_On_Planetary_6mm": {
            "brand": "Orion",
            "name": "Edge-On Planetary 6mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 120,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Orion_Edge_On_Planetary_9mm": {
            "brand": "Orion",
            "name": "Edge-On Planetary 9mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 125,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Orion_Edge_On_Planetary_12mm": {
            "brand": "Orion",
            "name": "Edge-On Planetary 12mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 135,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Orion_Edge_On_Planetary_15mm": {
            "brand": "Orion",
            "name": "Edge-On Planetary 15mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 145,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Orion_Edge_On_Planetary_20mm": {
            "brand": "Orion",
            "name": "Edge-On Planetary 20mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 165,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Orion_Edge_On_Planetary_25mm": {
            "brand": "Orion",
            "name": "Edge-On Planetary 25mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 180,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Omegon_Panorama_II_5mm": {
            "brand": "Omegon",
            "name": "Panorama II 5mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 130,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Omegon_Panorama_II_7mm": {
            "brand": "Omegon",
            "name": "Panorama II 7mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 140,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Omegon_Panorama_II_9mm": {
            "brand": "Omegon",
            "name": "Panorama II 9mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 150,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Omegon_Panorama_II_12mm": {
            "brand": "Omegon",
            "name": "Panorama II 12mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 160,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Omegon_Panorama_II_15mm": {
            "brand": "Omegon",
            "name": "Panorama II 15mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 175,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Omegon_Panorama_II_20mm": {
            "brand": "Omegon",
            "name": "Panorama II 20mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 200,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Omegon_Panorama_II_25mm": {
            "brand": "Omegon",
            "name": "Panorama II 25mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 230,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Omegon_Panorama_II_30mm": {
            "brand": "Omegon",
            "name": "Panorama II 30mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 450,
            "tside_thread": '2"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Omegon_Cronus_WA_4mm": {
            "brand": "Omegon",
            "name": "Cronus WA 4mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 90,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Omegon_Cronus_WA_6mm": {
            "brand": "Omegon",
            "name": "Cronus WA 6mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 95,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Omegon_Cronus_WA_9mm": {
            "brand": "Omegon",
            "name": "Cronus WA 9mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 100,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Omegon_Cronus_WA_12_5mm": {
            "brand": "Omegon",
            "name": "Cronus WA 12.5mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 110,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Omegon_Cronus_WA_17mm": {
            "brand": "Omegon",
            "name": "Cronus WA 17mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 125,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Omegon_Cronus_WA_25mm": {
            "brand": "Omegon",
            "name": "Cronus WA 25mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 150,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "TS_Optics_Planetary_HR_2_5mm": {
            "brand": "TS-Optics",
            "name": "Planetary HR 2.5mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 140,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "TS_Optics_Planetary_HR_3_2mm": {
            "brand": "TS-Optics",
            "name": "Planetary HR 3.2mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 145,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "TS_Optics_Planetary_HR_4mm": {
            "brand": "TS-Optics",
            "name": "Planetary HR 4mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 150,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "TS_Optics_Planetary_HR_5mm": {
            "brand": "TS-Optics",
            "name": "Planetary HR 5mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 155,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "TS_Optics_Planetary_HR_7mm": {
            "brand": "TS-Optics",
            "name": "Planetary HR 7mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 165,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "TS_Optics_Planetary_HR_9mm": {
            "brand": "TS-Optics",
            "name": "Planetary HR 9mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 175,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "TS_Optics_UWA_82_5_5mm": {
            "brand": "TS-Optics",
            "name": "UWA 82° 5.5mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 190,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "TS_Optics_UWA_82_7mm": {
            "brand": "TS-Optics",
            "name": "UWA 82° 7mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 200,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "TS_Optics_UWA_82_10mm": {
            "brand": "TS-Optics",
            "name": "UWA 82° 10mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 210,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "TS_Optics_UWA_82_15mm": {
            "brand": "TS-Optics",
            "name": "UWA 82° 15mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 230,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "TS_Optics_UWA_82_20mm": {
            "brand": "TS-Optics",
            "name": "UWA 82° 20mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 260,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "TS_Optics_UWA_82_30mm": {
            "brand": "TS-Optics",
            "name": "UWA 82° 30mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 550,
            "tside_thread": '2"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Bresser_LER_5mm_70": {
            "brand": "Bresser",
            "name": "LER 5mm 70°",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 100,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Bresser_LER_9mm_70": {
            "brand": "Bresser",
            "name": "LER 9mm 70°",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 110,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Bresser_LER_12mm_70": {
            "brand": "Bresser",
            "name": "LER 12mm 70°",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 120,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Bresser_LER_15mm_70": {
            "brand": "Bresser",
            "name": "LER 15mm 70°",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 130,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Bresser_LER_20mm_70": {
            "brand": "Bresser",
            "name": "LER 20mm 70°",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 150,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Bresser_LER_25mm_70": {
            "brand": "Bresser",
            "name": "LER 25mm 70°",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 170,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Bresser_LER_32mm_70": {
            "brand": "Bresser",
            "name": "LER 32mm 70°",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 200,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Lacerta_LER_5mm_72": {
            "brand": "Lacerta",
            "name": "LER 5mm 72°",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 120,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Lacerta_LER_7mm_72": {
            "brand": "Lacerta",
            "name": "LER 7mm 72°",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 130,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Lacerta_LER_10mm_72": {
            "brand": "Lacerta",
            "name": "LER 10mm 72°",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 140,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Lacerta_LER_15mm_72": {
            "brand": "Lacerta",
            "name": "LER 15mm 72°",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 160,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Lacerta_LER_20mm_72": {
            "brand": "Lacerta",
            "name": "LER 20mm 72°",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 180,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Lacerta_LER_25mm_72": {
            "brand": "Lacerta",
            "name": "LER 25mm 72°",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 200,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "GSO_Plossl_6mm": {
            "brand": "GSO",
            "name": "Plossl 6mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 90,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "GSO_Plossl_8mm": {
            "brand": "GSO",
            "name": "Plossl 8mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 95,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "GSO_Plossl_10mm": {
            "brand": "GSO",
            "name": "Plossl 10mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 100,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "GSO_Plossl_12_5mm": {
            "brand": "GSO",
            "name": "Plossl 12.5mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 110,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "GSO_Plossl_15mm": {
            "brand": "GSO",
            "name": "Plossl 15mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 120,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "GSO_Plossl_20mm": {
            "brand": "GSO",
            "name": "Plossl 20mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 130,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "GSO_Plossl_25mm": {
            "brand": "GSO",
            "name": "Plossl 25mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 145,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "GSO_Plossl_32mm": {
            "brand": "GSO",
            "name": "Plossl 32mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 160,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "GSO_Plossl_40mm": {
            "brand": "GSO",
            "name": "Plossl 40mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 200,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "GSO_SuperView_7mm": {
            "brand": "GSO",
            "name": "SuperView 7mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 200,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "GSO_SuperView_9mm": {
            "brand": "GSO",
            "name": "SuperView 9mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 210,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "GSO_SuperView_12mm": {
            "brand": "GSO",
            "name": "SuperView 12mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 225,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "GSO_SuperView_15mm": {
            "brand": "GSO",
            "name": "SuperView 15mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 240,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "GSO_SuperView_20mm": {
            "brand": "GSO",
            "name": "SuperView 20mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 260,
            "tside_thread": '2"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "GSO_SuperView_30mm": {
            "brand": "GSO",
            "name": "SuperView 30mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 500,
            "tside_thread": '2"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Masuyama_5mm_85": {
            "brand": "Masuyama",
            "name": "5mm 85°",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 160,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Masuyama_8mm_85": {
            "brand": "Masuyama",
            "name": "8mm 85°",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 165,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Masuyama_10mm_85": {
            "brand": "Masuyama",
            "name": "10mm 85°",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 170,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Masuyama_15mm_85": {
            "brand": "Masuyama",
            "name": "15mm 85°",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 180,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Masuyama_20mm_85": {
            "brand": "Masuyama",
            "name": "20mm 85°",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 200,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Masuyama_25mm_85": {
            "brand": "Masuyama",
            "name": "25mm 85°",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 220,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Masuyama_32mm_85": {
            "brand": "Masuyama",
            "name": "32mm 85°",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 280,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Agena_Starguider_5mm_60": {
            "brand": "Agena",
            "name": "Starguider 5mm 60°",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 110,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Agena_Starguider_7mm_60": {
            "brand": "Agena",
            "name": "Starguider 7mm 60°",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 115,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Agena_Starguider_9mm_60": {
            "brand": "Agena",
            "name": "Starguider 9mm 60°",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 120,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Agena_Starguider_12mm_60": {
            "brand": "Agena",
            "name": "Starguider 12mm 60°",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 130,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Agena_Starguider_15mm_60": {
            "brand": "Agena",
            "name": "Starguider 15mm 60°",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 145,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Agena_Starguider_20mm_60": {
            "brand": "Agena",
            "name": "Starguider 20mm 60°",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 160,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Agena_Starguider_25mm_60": {
            "brand": "Agena",
            "name": "Starguider 25mm 60°",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 180,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Stellarvue_Optimus_3_5mm_82": {
            "brand": "Stellarvue",
            "name": "Optimus 3.5mm 82°",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 200,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Stellarvue_Optimus_5mm_82": {
            "brand": "Stellarvue",
            "name": "Optimus 5mm 82°",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 210,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Stellarvue_Optimus_7mm_82": {
            "brand": "Stellarvue",
            "name": "Optimus 7mm 82°",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 220,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Stellarvue_Optimus_9mm_82": {
            "brand": "Stellarvue",
            "name": "Optimus 9mm 82°",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 230,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Stellarvue_Optimus_13mm_82": {
            "brand": "Stellarvue",
            "name": "Optimus 13mm 82°",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 250,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Stellarvue_Optimus_20mm_82": {
            "brand": "Stellarvue",
            "name": "Optimus 20mm 82°",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 280,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Celestron_Ultima_Duo_5mm": {
            "brand": "Celestron",
            "name": "Ultima Duo 5mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 160,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Celestron_Ultima_Duo_8mm": {
            "brand": "Celestron",
            "name": "Ultima Duo 8mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 170,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Celestron_Ultima_Duo_10mm": {
            "brand": "Celestron",
            "name": "Ultima Duo 10mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 180,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Celestron_Ultima_Duo_13mm": {
            "brand": "Celestron",
            "name": "Ultima Duo 13mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 195,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Celestron_Ultima_Duo_15mm": {
            "brand": "Celestron",
            "name": "Ultima Duo 15mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 210,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Celestron_Ultima_Duo_17mm": {
            "brand": "Celestron",
            "name": "Ultima Duo 17mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 225,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Celestron_Ultima_Duo_21mm": {
            "brand": "Celestron",
            "name": "Ultima Duo 21mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 250,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Celestron_Ultima_Duo_25mm": {
            "brand": "Celestron",
            "name": "Ultima Duo 25mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 280,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Meade_Series_6000_MWA_4_7mm": {
            "brand": "Meade",
            "name": "Series 6000 MWA 4.7mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 180,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Meade_Series_6000_MWA_6_7mm": {
            "brand": "Meade",
            "name": "Series 6000 MWA 6.7mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 190,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Meade_Series_6000_MWA_9_5mm": {
            "brand": "Meade",
            "name": "Series 6000 MWA 9.5mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 200,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Meade_Series_6000_MWA_14mm": {
            "brand": "Meade",
            "name": "Series 6000 MWA 14mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 220,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Meade_Series_6000_MWA_18mm": {
            "brand": "Meade",
            "name": "Series 6000 MWA 18mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 250,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Meade_Series_6000_MWA_24_5mm": {
            "brand": "Meade",
            "name": "Series 6000 MWA 24.5mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 300,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Takahashi_Abbe_Ortho_2_8mm": {
            "brand": "Takahashi",
            "name": "Abbe Ortho 2.8mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 250,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Takahashi_Abbe_Ortho_5mm": {
            "brand": "Takahashi",
            "name": "Abbe Ortho 5mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 200,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Takahashi_Abbe_Ortho_7_5mm": {
            "brand": "Takahashi",
            "name": "Abbe Ortho 7.5mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 210,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Takahashi_Abbe_Ortho_10mm": {
            "brand": "Takahashi",
            "name": "Abbe Ortho 10mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 220,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Takahashi_Abbe_Ortho_15mm": {
            "brand": "Takahashi",
            "name": "Abbe Ortho 15mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 240,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Takahashi_Abbe_Ortho_20mm": {
            "brand": "Takahashi",
            "name": "Abbe Ortho 20mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 260,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Takahashi_Abbe_Ortho_25mm": {
            "brand": "Takahashi",
            "name": "Abbe Ortho 25mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 290,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Takahashi_TOE_12_5mm": {
            "brand": "Takahashi",
            "name": "TOE 12.5mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 300,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Takahashi_TOE_20mm": {
            "brand": "Takahashi",
            "name": "TOE 20mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 350,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Takahashi_TOE_25mm": {
            "brand": "Takahashi",
            "name": "TOE 25mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 400,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Astro_Physics_MaxView_10mm": {
            "brand": "Astro-Physics",
            "name": "MaxView 10mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 200,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Astro_Physics_MaxView_15mm": {
            "brand": "Astro-Physics",
            "name": "MaxView 15mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 230,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Astro_Physics_MaxView_20mm": {
            "brand": "Astro-Physics",
            "name": "MaxView 20mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 250,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Astro_Physics_MaxView_25mm": {
            "brand": "Astro-Physics",
            "name": "MaxView 25mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 280,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Lunt_H_alpha_7_5mm": {
            "brand": "Lunt",
            "name": "H-alpha 7.5mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 150,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Lunt_H_alpha_12mm": {
            "brand": "Lunt",
            "name": "H-alpha 12mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 160,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Lunt_H_alpha_16mm": {
            "brand": "Lunt",
            "name": "H-alpha 16mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 170,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Lunt_H_alpha_19mm": {
            "brand": "Lunt",
            "name": "H-alpha 19mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 190,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Lunt_H_alpha_27mm": {
            "brand": "Lunt",
            "name": "H-alpha 27mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 250,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Generic_Plossl_4mm": {
            "brand": "Generic",
            "name": "Plossl 4mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 70,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Generic_Plossl_6mm": {
            "brand": "Generic",
            "name": "Plossl 6mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 75,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Generic_Plossl_8mm": {
            "brand": "Generic",
            "name": "Plossl 8mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 80,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Generic_Plossl_10mm": {
            "brand": "Generic",
            "name": "Plossl 10mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 85,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Generic_Plossl_12_5mm": {
            "brand": "Generic",
            "name": "Plossl 12.5mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 90,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Generic_Plossl_15mm": {
            "brand": "Generic",
            "name": "Plossl 15mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 95,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Generic_Plossl_20mm": {
            "brand": "Generic",
            "name": "Plossl 20mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 105,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Generic_Plossl_25mm": {
            "brand": "Generic",
            "name": "Plossl 25mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 115,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Generic_Plossl_30mm": {
            "brand": "Generic",
            "name": "Plossl 30mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 130,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Generic_Plossl_40mm": {
            "brand": "Generic",
            "name": "Plossl 40mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 160,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Generic_Wide_Angle_66_6mm": {
            "brand": "Generic",
            "name": "Wide Angle 66° 6mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 120,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Generic_Wide_Angle_66_9mm": {
            "brand": "Generic",
            "name": "Wide Angle 66° 9mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 130,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Generic_Wide_Angle_66_12mm": {
            "brand": "Generic",
            "name": "Wide Angle 66° 12mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 140,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Generic_Wide_Angle_66_15mm": {
            "brand": "Generic",
            "name": "Wide Angle 66° 15mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 150,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Generic_Wide_Angle_66_20mm": {
            "brand": "Generic",
            "name": "Wide Angle 66° 20mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 170,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Generic_Wide_Angle_66_25mm": {
            "brand": "Generic",
            "name": "Wide Angle 66° 25mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 190,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Sky_Watcher_Plossl_6mm": {
            "brand": "Sky-Watcher",
            "name": "Plossl 6mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 90,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Sky_Watcher_Plossl_9mm": {
            "brand": "Sky-Watcher",
            "name": "Plossl 9mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 95,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Sky_Watcher_Plossl_12mm": {
            "brand": "Sky-Watcher",
            "name": "Plossl 12mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 100,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Sky_Watcher_Plossl_15mm": {
            "brand": "Sky-Watcher",
            "name": "Plossl 15mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 105,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Sky_Watcher_Plossl_20mm": {
            "brand": "Sky-Watcher",
            "name": "Plossl 20mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 115,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Sky_Watcher_Plossl_25mm": {
            "brand": "Sky-Watcher",
            "name": "Plossl 25mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 125,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Lacerta_ED_4mm_82": {
            "brand": "Lacerta",
            "name": "ED 4mm 82°",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 170,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Lacerta_ED_6mm_82": {
            "brand": "Lacerta",
            "name": "ED 6mm 82°",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 175,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Lacerta_ED_9mm_82": {
            "brand": "Lacerta",
            "name": "ED 9mm 82°",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 185,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Lacerta_ED_12mm_82": {
            "brand": "Lacerta",
            "name": "ED 12mm 82°",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 195,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Lacerta_ED_15mm_82": {
            "brand": "Lacerta",
            "name": "ED 15mm 82°",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 210,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Lacerta_ED_20mm_82": {
            "brand": "Lacerta",
            "name": "ED 20mm 82°",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 240,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "TeleVue_DeLite_4mm": {
            "brand": "TeleVue",
            "name": "DeLite 4mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 180,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "TeleVue_DeLite_5mm": {
            "brand": "TeleVue",
            "name": "DeLite 5mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 185,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "TeleVue_DeLite_7mm": {
            "brand": "TeleVue",
            "name": "DeLite 7mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 190,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "TeleVue_DeLite_9mm": {
            "brand": "TeleVue",
            "name": "DeLite 9mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 195,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "TeleVue_DeLite_11mm": {
            "brand": "TeleVue",
            "name": "DeLite 11mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 200,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "TeleVue_DeLite_13mm": {
            "brand": "TeleVue",
            "name": "DeLite 13mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 210,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "TeleVue_DeLite_15mm": {
            "brand": "TeleVue",
            "name": "DeLite 15mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 215,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "TeleVue_DeLite_18_2mm": {
            "brand": "TeleVue",
            "name": "DeLite 18.2mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 230,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Kasai_Wide_View_5mm_84": {
            "brand": "Kasai",
            "name": "Wide View 5mm 84°",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 180,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Kasai_Wide_View_7_5mm_84": {
            "brand": "Kasai",
            "name": "Wide View 7.5mm 84°",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 190,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Kasai_Wide_View_10mm_84": {
            "brand": "Kasai",
            "name": "Wide View 10mm 84°",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 200,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Kasai_Wide_View_14mm_84": {
            "brand": "Kasai",
            "name": "Wide View 14mm 84°",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 220,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Kasai_Wide_View_20mm_84": {
            "brand": "Kasai",
            "name": "Wide View 20mm 84°",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 250,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "TMB_Planetary_II_2_5mm_58": {
            "brand": "TMB",
            "name": "Planetary II 2.5mm 58°",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 120,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "TMB_Planetary_II_3_2mm_58": {
            "brand": "TMB",
            "name": "Planetary II 3.2mm 58°",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 125,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "TMB_Planetary_II_4mm_58": {
            "brand": "TMB",
            "name": "Planetary II 4mm 58°",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 130,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "TMB_Planetary_II_5mm_58": {
            "brand": "TMB",
            "name": "Planetary II 5mm 58°",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 135,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "TMB_Planetary_II_6mm_58": {
            "brand": "TMB",
            "name": "Planetary II 6mm 58°",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 140,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "TMB_Planetary_II_7mm_58": {
            "brand": "TMB",
            "name": "Planetary II 7mm 58°",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 145,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "TMB_Planetary_II_8mm_58": {
            "brand": "TMB",
            "name": "Planetary II 8mm 58°",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 150,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "TMB_Planetary_II_9mm_58": {
            "brand": "TMB",
            "name": "Planetary II 9mm 58°",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 155,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "MaxVision_3_5mm_82": {
            "brand": "MaxVision",
            "name": "3.5mm 82°",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 160,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "MaxVision_5mm_82": {
            "brand": "MaxVision",
            "name": "5mm 82°",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 165,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "MaxVision_7mm_82": {
            "brand": "MaxVision",
            "name": "7mm 82°",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 170,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "MaxVision_10mm_82": {
            "brand": "MaxVision",
            "name": "10mm 82°",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 180,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "MaxVision_15mm_82": {
            "brand": "MaxVision",
            "name": "15mm 82°",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 200,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "MaxVision_20mm_82": {
            "brand": "MaxVision",
            "name": "20mm 82°",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 220,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Celestron_Omni_Plossl_4mm": {
            "brand": "Celestron",
            "name": "Omni Plossl 4mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 90,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Celestron_Omni_Plossl_6mm": {
            "brand": "Celestron",
            "name": "Omni Plossl 6mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 95,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Celestron_Omni_Plossl_9mm": {
            "brand": "Celestron",
            "name": "Omni Plossl 9mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 100,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Celestron_Omni_Plossl_12_5mm": {
            "brand": "Celestron",
            "name": "Omni Plossl 12.5mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 110,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Celestron_Omni_Plossl_15mm": {
            "brand": "Celestron",
            "name": "Omni Plossl 15mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 115,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Celestron_Omni_Plossl_20mm": {
            "brand": "Celestron",
            "name": "Omni Plossl 20mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 125,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Celestron_Omni_Plossl_25mm": {
            "brand": "Celestron",
            "name": "Omni Plossl 25mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 135,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Celestron_Omni_Plossl_32mm": {
            "brand": "Celestron",
            "name": "Omni Plossl 32mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 155,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Celestron_Omni_Plossl_40mm": {
            "brand": "Celestron",
            "name": "Omni Plossl 40mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 195,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Meade_Super_Plossl_6_4mm": {
            "brand": "Meade",
            "name": "Super Plossl 6.4mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 95,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Meade_Super_Plossl_9_7mm": {
            "brand": "Meade",
            "name": "Super Plossl 9.7mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 100,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Meade_Super_Plossl_12_4mm": {
            "brand": "Meade",
            "name": "Super Plossl 12.4mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 110,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Meade_Super_Plossl_15mm": {
            "brand": "Meade",
            "name": "Super Plossl 15mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 115,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Meade_Super_Plossl_20mm": {
            "brand": "Meade",
            "name": "Super Plossl 20mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 125,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Meade_Super_Plossl_25mm": {
            "brand": "Meade",
            "name": "Super Plossl 25mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 135,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Meade_Super_Plossl_32mm": {
            "brand": "Meade",
            "name": "Super Plossl 32mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 155,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Meade_Super_Plossl_40mm": {
            "brand": "Meade",
            "name": "Super Plossl 40mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 195,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Meade_Super_Plossl_56mm": {
            "brand": "Meade",
            "name": "Super Plossl 56mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 250,
            "tside_thread": '2"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Orion_Sirius_Plossl_6_3mm": {
            "brand": "Orion",
            "name": "Sirius Plossl 6.3mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 95,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Orion_Sirius_Plossl_7_5mm": {
            "brand": "Orion",
            "name": "Sirius Plossl 7.5mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 100,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Orion_Sirius_Plossl_10mm": {
            "brand": "Orion",
            "name": "Sirius Plossl 10mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 105,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Orion_Sirius_Plossl_12_5mm": {
            "brand": "Orion",
            "name": "Sirius Plossl 12.5mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 110,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Orion_Sirius_Plossl_17mm": {
            "brand": "Orion",
            "name": "Sirius Plossl 17mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 120,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Orion_Sirius_Plossl_20mm": {
            "brand": "Orion",
            "name": "Sirius Plossl 20mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 125,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Orion_Sirius_Plossl_25mm": {
            "brand": "Orion",
            "name": "Sirius Plossl 25mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 135,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Orion_Sirius_Plossl_32mm": {
            "brand": "Orion",
            "name": "Sirius Plossl 32mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 155,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Orion_Sirius_Plossl_40mm": {
            "brand": "Orion",
            "name": "Sirius Plossl 40mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 200,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Pentax_XF_6_5mm": {
            "brand": "Pentax",
            "name": "XF 6.5mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 230,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Pentax_XF_8_5mm": {
            "brand": "Pentax",
            "name": "XF 8.5mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 240,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Pentax_XF_12mm": {
            "brand": "Pentax",
            "name": "XF 12mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 260,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Brandon_8mm": {
            "brand": "Brandon",
            "name": "8mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 130,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Brandon_12mm": {
            "brand": "Brandon",
            "name": "12mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 140,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Brandon_16mm": {
            "brand": "Brandon",
            "name": "16mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 150,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Brandon_24mm": {
            "brand": "Brandon",
            "name": "24mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 170,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Brandon_32mm": {
            "brand": "Brandon",
            "name": "32mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 200,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Fujiyama_HD_Ortho_4mm": {
            "brand": "Fujiyama",
            "name": "HD Ortho 4mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 110,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Fujiyama_HD_Ortho_5mm": {
            "brand": "Fujiyama",
            "name": "HD Ortho 5mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 115,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Fujiyama_HD_Ortho_6mm": {
            "brand": "Fujiyama",
            "name": "HD Ortho 6mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 120,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Fujiyama_HD_Ortho_7mm": {
            "brand": "Fujiyama",
            "name": "HD Ortho 7mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 125,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Fujiyama_HD_Ortho_9mm": {
            "brand": "Fujiyama",
            "name": "HD Ortho 9mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 130,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Fujiyama_HD_Ortho_12_5mm": {
            "brand": "Fujiyama",
            "name": "HD Ortho 12.5mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 140,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Fujiyama_HD_Ortho_18mm": {
            "brand": "Fujiyama",
            "name": "HD Ortho 18mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 160,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Fujiyama_HD_Ortho_25mm": {
            "brand": "Fujiyama",
            "name": "HD Ortho 25mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 180,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "William_Optics_Pleiades_3mm_55": {
            "brand": "William Optics",
            "name": "Pleiades 3mm 55°",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 170,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "William_Optics_Pleiades_6mm_55": {
            "brand": "William Optics",
            "name": "Pleiades 6mm 55°",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 180,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "William_Optics_Pleiades_10mm_55": {
            "brand": "William Optics",
            "name": "Pleiades 10mm 55°",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 195,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "William_Optics_Pleiades_15mm_55": {
            "brand": "William Optics",
            "name": "Pleiades 15mm 55°",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 215,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "William_Optics_Pleiades_20mm_55": {
            "brand": "William Optics",
            "name": "Pleiades 20mm 55°",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 240,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Saxon_Plossl_4mm": {
            "brand": "Saxon",
            "name": "Plossl 4mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 100,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Saxon_Plossl_6mm": {
            "brand": "Saxon",
            "name": "Plossl 6mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 105,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Saxon_Plossl_9mm": {
            "brand": "Saxon",
            "name": "Plossl 9mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 110,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Saxon_Plossl_12_5mm": {
            "brand": "Saxon",
            "name": "Plossl 12.5mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 120,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Saxon_Plossl_16mm": {
            "brand": "Saxon",
            "name": "Plossl 16mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 130,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Saxon_Plossl_20mm": {
            "brand": "Saxon",
            "name": "Plossl 20mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 140,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Saxon_Plossl_25mm": {
            "brand": "Saxon",
            "name": "Plossl 25mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 160,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "National_Geographic_Plossl_4mm": {
            "brand": "National Geographic",
            "name": "Plossl 4mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 95,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "National_Geographic_Plossl_6mm": {
            "brand": "National Geographic",
            "name": "Plossl 6mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 100,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "National_Geographic_Plossl_9mm": {
            "brand": "National Geographic",
            "name": "Plossl 9mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 105,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "National_Geographic_Plossl_12_5mm": {
            "brand": "National Geographic",
            "name": "Plossl 12.5mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 115,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "National_Geographic_Plossl_20mm": {
            "brand": "National Geographic",
            "name": "Plossl 20mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 130,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "National_Geographic_Plossl_25mm": {
            "brand": "National Geographic",
            "name": "Plossl 25mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 145,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "National_Geographic_Plossl_32mm": {
            "brand": "National Geographic",
            "name": "Plossl 32mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 170,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Omegon_Super_Plossl_4mm": {
            "brand": "Omegon",
            "name": "Super Plossl 4mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 110,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Omegon_Super_Plossl_6mm": {
            "brand": "Omegon",
            "name": "Super Plossl 6mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 115,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Omegon_Super_Plossl_9mm": {
            "brand": "Omegon",
            "name": "Super Plossl 9mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 120,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Omegon_Super_Plossl_12mm": {
            "brand": "Omegon",
            "name": "Super Plossl 12mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 130,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Omegon_Super_Plossl_16mm": {
            "brand": "Omegon",
            "name": "Super Plossl 16mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 140,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Omegon_Super_Plossl_20mm": {
            "brand": "Omegon",
            "name": "Super Plossl 20mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 155,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Omegon_Super_Plossl_25mm": {
            "brand": "Omegon",
            "name": "Super Plossl 25mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 170,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Omegon_Super_Plossl_32mm": {
            "brand": "Omegon",
            "name": "Super Plossl 32mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 200,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Vixen_LVW_3_5mm": {
            "brand": "Vixen",
            "name": "LVW 3.5mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 280,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Vixen_LVW_5mm": {
            "brand": "Vixen",
            "name": "LVW 5mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 285,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Vixen_LVW_8mm": {
            "brand": "Vixen",
            "name": "LVW 8mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 295,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Vixen_LVW_13mm": {
            "brand": "Vixen",
            "name": "LVW 13mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 350,
            "tside_thread": '2"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Vixen_LVW_17mm": {
            "brand": "Vixen",
            "name": "LVW 17mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 380,
            "tside_thread": '2"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Vixen_LVW_22mm": {
            "brand": "Vixen",
            "name": "LVW 22mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 420,
            "tside_thread": '2"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Vixen_LVW_30mm": {
            "brand": "Vixen",
            "name": "LVW 30mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 580,
            "tside_thread": '2"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Vixen_LVW_42mm": {
            "brand": "Vixen",
            "name": "LVW 42mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 800,
            "tside_thread": '2"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Bresser_Plossl_2_5mm": {
            "brand": "Bresser",
            "name": "Plossl 2.5mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 100,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Bresser_Plossl_4mm": {
            "brand": "Bresser",
            "name": "Plossl 4mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 105,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Bresser_Plossl_6mm": {
            "brand": "Bresser",
            "name": "Plossl 6mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 110,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Bresser_Plossl_8mm": {
            "brand": "Bresser",
            "name": "Plossl 8mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 115,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Bresser_Plossl_12_5mm": {
            "brand": "Bresser",
            "name": "Plossl 12.5mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 125,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Bresser_Plossl_20mm": {
            "brand": "Bresser",
            "name": "Plossl 20mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 140,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Bresser_Plossl_25mm": {
            "brand": "Bresser",
            "name": "Plossl 25mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 155,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Bresser_Plossl_32mm": {
            "brand": "Bresser",
            "name": "Plossl 32mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 175,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Lacerta_Plossl_6mm": {
            "brand": "Lacerta",
            "name": "Plossl 6mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 130,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Lacerta_Plossl_9mm": {
            "brand": "Lacerta",
            "name": "Plossl 9mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 135,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Lacerta_Plossl_12_5mm": {
            "brand": "Lacerta",
            "name": "Plossl 12.5mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 145,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Lacerta_Plossl_20mm": {
            "brand": "Lacerta",
            "name": "Plossl 20mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 165,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Lacerta_Plossl_25mm": {
            "brand": "Lacerta",
            "name": "Plossl 25mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 180,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Lacerta_Plossl_40mm": {
            "brand": "Lacerta",
            "name": "Plossl 40mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 250,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "GSO_Wide_Field_4mm_70": {
            "brand": "GSO",
            "name": "Wide Field 4mm 70°",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 85,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "GSO_Wide_Field_6mm_70": {
            "brand": "GSO",
            "name": "Wide Field 6mm 70°",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 90,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "GSO_Wide_Field_10mm_70": {
            "brand": "GSO",
            "name": "Wide Field 10mm 70°",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 100,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "GSO_Wide_Field_15mm_70": {
            "brand": "GSO",
            "name": "Wide Field 15mm 70°",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 110,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "GSO_Wide_Field_20mm_70": {
            "brand": "GSO",
            "name": "Wide Field 20mm 70°",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 120,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "GSO_Wide_Field_25mm_70": {
            "brand": "GSO",
            "name": "Wide Field 25mm 70°",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 135,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Celestron_Ultima_Edge_3_2mm": {
            "brand": "Celestron",
            "name": "Ultima Edge 3.2mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 200,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Celestron_Ultima_Edge_5mm": {
            "brand": "Celestron",
            "name": "Ultima Edge 5mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 210,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Celestron_Ultima_Edge_8mm": {
            "brand": "Celestron",
            "name": "Ultima Edge 8mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 220,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Celestron_Ultima_Edge_12mm": {
            "brand": "Celestron",
            "name": "Ultima Edge 12mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 240,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Celestron_Ultima_Edge_16mm": {
            "brand": "Celestron",
            "name": "Ultima Edge 16mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 260,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Masuyama_12_5mm_85": {
            "brand": "Masuyama",
            "name": "12.5mm 85°",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 180,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Docter_Noblex_UWF_10mm": {
            "brand": "Docter/Noblex",
            "name": "UWF 10mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 200,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Docter_Noblex_UWF_12_5mm": {
            "brand": "Docter/Noblex",
            "name": "UWF 12.5mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 220,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Docter_Noblex_UWF_17mm": {
            "brand": "Docter/Noblex",
            "name": "UWF 17mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 270,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Kokusai_Kohki_Ortho_5mm": {
            "brand": "Kokusai Kohki",
            "name": "Ortho 5mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 140,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Kokusai_Kohki_Ortho_8mm": {
            "brand": "Kokusai Kohki",
            "name": "Ortho 8mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 155,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Kokusai_Kohki_Ortho_12mm": {
            "brand": "Kokusai Kohki",
            "name": "Ortho 12mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 170,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Kokusai_Kohki_Ortho_18mm": {
            "brand": "Kokusai Kohki",
            "name": "Ortho 18mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 200,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Kokusai_Kohki_Ortho_25mm": {
            "brand": "Kokusai Kohki",
            "name": "Ortho 25mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 240,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Takahashi_TPL_2_5mm": {
            "brand": "Takahashi",
            "name": "TPL 2.5mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 130,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Takahashi_TPL_3_6mm": {
            "brand": "Takahashi",
            "name": "TPL 3.6mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 135,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Takahashi_TPL_5mm": {
            "brand": "Takahashi",
            "name": "TPL 5mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 145,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Takahashi_TPL_6_4mm": {
            "brand": "Takahashi",
            "name": "TPL 6.4mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 150,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Takahashi_TPL_8mm": {
            "brand": "Takahashi",
            "name": "TPL 8mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 160,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Takahashi_TPL_12_5mm": {
            "brand": "Takahashi",
            "name": "TPL 12.5mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 180,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Takahashi_TPL_18mm": {
            "brand": "Takahashi",
            "name": "TPL 18mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 200,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Takahashi_TPL_25mm": {
            "brand": "Takahashi",
            "name": "TPL 25mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 230,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Takahashi_TPL_40mm": {
            "brand": "Takahashi",
            "name": "TPL 40mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 350,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Takahashi_Abbe_Ortho_4mm": {
            "brand": "Takahashi",
            "name": "Abbe Ortho 4mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 120,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Takahashi_Abbe_Ortho_6mm": {
            "brand": "Takahashi",
            "name": "Abbe Ortho 6mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 130,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Takahashi_Abbe_Ortho_9mm": {
            "brand": "Takahashi",
            "name": "Abbe Ortho 9mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 145,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Takahashi_Abbe_Ortho_12_5mm": {
            "brand": "Takahashi",
            "name": "Abbe Ortho 12.5mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 160,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Takahashi_Abbe_Ortho_18mm": {
            "brand": "Takahashi",
            "name": "Abbe Ortho 18mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 180,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Takahashi_Abbe_Ortho_32mm": {
            "brand": "Takahashi",
            "name": "Abbe Ortho 32mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 260,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Zeiss_Abbe_Ortho_4mm": {
            "brand": "Zeiss",
            "name": "Abbe Ortho 4mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 250,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Zeiss_Abbe_Ortho_6mm": {
            "brand": "Zeiss",
            "name": "Abbe Ortho 6mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 260,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Zeiss_Abbe_Ortho_10mm": {
            "brand": "Zeiss",
            "name": "Abbe Ortho 10mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 280,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Zeiss_Abbe_Ortho_16mm": {
            "brand": "Zeiss",
            "name": "Abbe Ortho 16mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 320,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Zeiss_Abbe_Ortho_25mm": {
            "brand": "Zeiss",
            "name": "Abbe Ortho 25mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 380,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Leica_ASPH_10mm": {
            "brand": "Leica",
            "name": "ASPH 10mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 350,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Leica_ASPH_17_5mm": {
            "brand": "Leica",
            "name": "ASPH 17.5mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 380,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Leica_ASPH_25mm": {
            "brand": "Leica",
            "name": "ASPH 25mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 410,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Leica_ASPH_30mm": {
            "brand": "Leica",
            "name": "ASPH 30mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 450,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Antares_Speers_WALER_4_7mm": {
            "brand": "Antares",
            "name": "Speers-WALER 4.7mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 100,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Antares_Speers_WALER_7_5mm": {
            "brand": "Antares",
            "name": "Speers-WALER 7.5mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 110,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Antares_Speers_WALER_10mm": {
            "brand": "Antares",
            "name": "Speers-WALER 10mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 120,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Antares_Speers_WALER_15mm": {
            "brand": "Antares",
            "name": "Speers-WALER 15mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 135,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Antares_Speers_WALER_20mm": {
            "brand": "Antares",
            "name": "Speers-WALER 20mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 155,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Antares_Speers_WALER_25mm": {
            "brand": "Antares",
            "name": "Speers-WALER 25mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 175,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Antares_Speers_WALER_32mm": {
            "brand": "Antares",
            "name": "Speers-WALER 32mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 200,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "GSO_Wide_Field_8mm_70": {
            "brand": "GSO",
            "name": "Wide Field 8mm 70°",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 120,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "GSO_Wide_Field_30mm_70": {
            "brand": "GSO",
            "name": "Wide Field 30mm 70°",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 220,
            "tside_thread": '2"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "GSO_Wide_Field_42mm_70": {
            "brand": "GSO",
            "name": "Wide Field 42mm 70°",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 350,
            "tside_thread": '2"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Celestron_Omni_4mm": {
            "brand": "Celestron",
            "name": "Omni 4mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 80,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Celestron_Omni_6mm": {
            "brand": "Celestron",
            "name": "Omni 6mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 85,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Celestron_Omni_9mm": {
            "brand": "Celestron",
            "name": "Omni 9mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 90,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Celestron_Omni_12mm": {
            "brand": "Celestron",
            "name": "Omni 12mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 100,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Celestron_Omni_15mm": {
            "brand": "Celestron",
            "name": "Omni 15mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 110,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Celestron_Omni_20mm": {
            "brand": "Celestron",
            "name": "Omni 20mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 120,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Celestron_Omni_25mm": {
            "brand": "Celestron",
            "name": "Omni 25mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 130,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Celestron_Omni_32mm": {
            "brand": "Celestron",
            "name": "Omni 32mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 155,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Celestron_Omni_40mm": {
            "brand": "Celestron",
            "name": "Omni 40mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 185,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Celestron_E_Lux_6_5mm": {
            "brand": "Celestron",
            "name": "E-Lux 6.5mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 95,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Celestron_E_Lux_10mm": {
            "brand": "Celestron",
            "name": "E-Lux 10mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 105,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Celestron_E_Lux_13mm": {
            "brand": "Celestron",
            "name": "E-Lux 13mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 115,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Celestron_E_Lux_20mm": {
            "brand": "Celestron",
            "name": "E-Lux 20mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 130,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Celestron_E_Lux_25mm": {
            "brand": "Celestron",
            "name": "E-Lux 25mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 145,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Celestron_E_Lux_32mm": {
            "brand": "Celestron",
            "name": "E-Lux 32mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 170,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Celestron_E_Lux_40mm": {
            "brand": "Celestron",
            "name": "E-Lux 40mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 200,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Orion_DeepView_20mm": {
            "brand": "Orion",
            "name": "DeepView 20mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 260,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Orion_DeepView_28mm": {
            "brand": "Orion",
            "name": "DeepView 28mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 400,
            "tside_thread": '2"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Orion_DeepView_35mm": {
            "brand": "Orion",
            "name": "DeepView 35mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 550,
            "tside_thread": '2"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Orion_DeepView_42mm": {
            "brand": "Orion",
            "name": "DeepView 42mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 700,
            "tside_thread": '2"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Orion_Q70_20mm": {
            "brand": "Orion",
            "name": "Q70 20mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 280,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Orion_Q70_26mm": {
            "brand": "Orion",
            "name": "Q70 26mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 350,
            "tside_thread": '2"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Orion_Q70_32mm": {
            "brand": "Orion",
            "name": "Q70 32mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 500,
            "tside_thread": '2"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Orion_Q70_38mm": {
            "brand": "Orion",
            "name": "Q70 38mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 650,
            "tside_thread": '2"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Orion_Expanse_6mm": {
            "brand": "Orion",
            "name": "Expanse 6mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 120,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Orion_Expanse_9mm": {
            "brand": "Orion",
            "name": "Expanse 9mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 130,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Orion_Expanse_15mm": {
            "brand": "Orion",
            "name": "Expanse 15mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 150,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Orion_Expanse_20mm": {
            "brand": "Orion",
            "name": "Expanse 20mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 170,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Orion_Sirius_Plossl_6mm": {
            "brand": "Orion",
            "name": "Sirius Plossl 6mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 85,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Meade_Super_Plossl_4_7mm": {
            "brand": "Meade",
            "name": "Super Plossl 4.7mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 95,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Meade_Super_Plossl_8_8mm": {
            "brand": "Meade",
            "name": "Super Plossl 8.8mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 108,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Meade_Super_Plossl_17_8mm": {
            "brand": "Meade",
            "name": "Super Plossl 17.8mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 132,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Meade_Super_Plossl_26mm": {
            "brand": "Meade",
            "name": "Super Plossl 26mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 150,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Meade_Series_5000_MWA_5mm": {
            "brand": "Meade",
            "name": "Series 5000 MWA 5mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 260,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Meade_Series_5000_MWA_10mm": {
            "brand": "Meade",
            "name": "Series 5000 MWA 10mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 280,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Meade_Series_5000_MWA_15mm": {
            "brand": "Meade",
            "name": "Series 5000 MWA 15mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 310,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Meade_Series_5000_MWA_21mm": {
            "brand": "Meade",
            "name": "Series 5000 MWA 21mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 350,
            "tside_thread": '2"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Meade_Series_5000_MWA_28mm": {
            "brand": "Meade",
            "name": "Series 5000 MWA 28mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 500,
            "tside_thread": '2"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Omegon_SWA_4_5mm_70": {
            "brand": "Omegon",
            "name": "SWA 4.5mm 70°",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 130,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Omegon_SWA_6_5mm_70": {
            "brand": "Omegon",
            "name": "SWA 6.5mm 70°",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 140,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Omegon_SWA_9mm_70": {
            "brand": "Omegon",
            "name": "SWA 9mm 70°",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 155,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Omegon_SWA_12mm_70": {
            "brand": "Omegon",
            "name": "SWA 12mm 70°",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 170,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Omegon_SWA_15mm_70": {
            "brand": "Omegon",
            "name": "SWA 15mm 70°",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 190,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Omegon_SWA_20mm_70": {
            "brand": "Omegon",
            "name": "SWA 20mm 70°",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 220,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Omegon_LE_Planetary_3mm": {
            "brand": "Omegon",
            "name": "LE Planetary 3mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 120,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Omegon_LE_Planetary_5mm": {
            "brand": "Omegon",
            "name": "LE Planetary 5mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 130,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Omegon_LE_Planetary_7mm": {
            "brand": "Omegon",
            "name": "LE Planetary 7mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 140,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Omegon_LE_Planetary_10mm": {
            "brand": "Omegon",
            "name": "LE Planetary 10mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 155,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Omegon_LE_Planetary_14mm": {
            "brand": "Omegon",
            "name": "LE Planetary 14mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 170,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Omegon_LE_Planetary_19mm": {
            "brand": "Omegon",
            "name": "LE Planetary 19mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 190,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Omegon_LE_Planetary_25mm": {
            "brand": "Omegon",
            "name": "LE Planetary 25mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 220,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Bresser_Plossl_6_5mm": {
            "brand": "Bresser",
            "name": "Plossl 6.5mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 80,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Bresser_Plossl_10mm": {
            "brand": "Bresser",
            "name": "Plossl 10mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 90,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Bresser_Plossl_15mm": {
            "brand": "Bresser",
            "name": "Plossl 15mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 105,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Bresser_Plossl_40mm": {
            "brand": "Bresser",
            "name": "Plossl 40mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 180,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Bresser_Wide_Angle_5mm_70": {
            "brand": "Bresser",
            "name": "Wide Angle 5mm 70°",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 110,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Bresser_Wide_Angle_8mm_70": {
            "brand": "Bresser",
            "name": "Wide Angle 8mm 70°",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 120,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Bresser_Wide_Angle_12mm_70": {
            "brand": "Bresser",
            "name": "Wide Angle 12mm 70°",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 135,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Bresser_Wide_Angle_15mm_70": {
            "brand": "Bresser",
            "name": "Wide Angle 15mm 70°",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 150,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Bresser_Wide_Angle_20mm_70": {
            "brand": "Bresser",
            "name": "Wide Angle 20mm 70°",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 175,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Bresser_Wide_Angle_25mm_70": {
            "brand": "Bresser",
            "name": "Wide Angle 25mm 70°",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 200,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "SVBony_SV154_Plossl_4mm": {
            "brand": "SVBony",
            "name": "SV154 Plossl 4mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 70,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "SVBony_SV154_Plossl_6_3mm": {
            "brand": "SVBony",
            "name": "SV154 Plossl 6.3mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 75,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "SVBony_SV154_Plossl_10mm": {
            "brand": "SVBony",
            "name": "SV154 Plossl 10mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 82,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "SVBony_SV154_Plossl_12_5mm": {
            "brand": "SVBony",
            "name": "SV154 Plossl 12.5mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 90,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "SVBony_SV154_Plossl_17mm": {
            "brand": "SVBony",
            "name": "SV154 Plossl 17mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 100,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "SVBony_SV154_Plossl_20mm": {
            "brand": "SVBony",
            "name": "SV154 Plossl 20mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 110,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "SVBony_SV154_Plossl_25mm": {
            "brand": "SVBony",
            "name": "SV154 Plossl 25mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 125,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "SVBony_SV154_Plossl_32mm": {
            "brand": "SVBony",
            "name": "SV154 Plossl 32mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 145,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "SVBony_SV154_Plossl_40mm": {
            "brand": "SVBony",
            "name": "SV154 Plossl 40mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 175,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "SVBony_SV213_TMB_3mm": {
            "brand": "SVBony",
            "name": "SV213 TMB 3mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 85,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "SVBony_SV213_TMB_4mm": {
            "brand": "SVBony",
            "name": "SV213 TMB 4mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 88,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "SVBony_SV213_TMB_5mm": {
            "brand": "SVBony",
            "name": "SV213 TMB 5mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 92,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "SVBony_SV213_TMB_6mm": {
            "brand": "SVBony",
            "name": "SV213 TMB 6mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 95,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "SVBony_SV213_TMB_7mm": {
            "brand": "SVBony",
            "name": "SV213 TMB 7mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 100,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "SVBony_SV213_TMB_8mm": {
            "brand": "SVBony",
            "name": "SV213 TMB 8mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 105,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "SVBony_SV213_TMB_9mm": {
            "brand": "SVBony",
            "name": "SV213 TMB 9mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 110,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "SVBony_SV213_TMB_10mm": {
            "brand": "SVBony",
            "name": "SV213 TMB 10mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 115,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "SVBony_SV213_TMB_12_5mm": {
            "brand": "SVBony",
            "name": "SV213 TMB 12.5mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 125,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Lacerta_SWMA_100_5mm": {
            "brand": "Lacerta",
            "name": "SWMA 100° 5mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 260,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Lacerta_SWMA_100_7mm": {
            "brand": "Lacerta",
            "name": "SWMA 100° 7mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 280,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Lacerta_SWMA_100_9mm": {
            "brand": "Lacerta",
            "name": "SWMA 100° 9mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 300,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Lacerta_SWMA_100_14mm": {
            "brand": "Lacerta",
            "name": "SWMA 100° 14mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 400,
            "tside_thread": '2"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Lacerta_SWMA_100_20mm": {
            "brand": "Lacerta",
            "name": "SWMA 100° 20mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 550,
            "tside_thread": '2"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Lacerta_Plossl_10mm": {
            "brand": "Lacerta",
            "name": "Plossl 10mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 90,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Lacerta_Plossl_15mm": {
            "brand": "Lacerta",
            "name": "Plossl 15mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 100,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Lacerta_Plossl_32mm": {
            "brand": "Lacerta",
            "name": "Plossl 32mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 150,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "TS_Optics_WA_72_5mm": {
            "brand": "TS-Optics",
            "name": "WA 72° 5mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 140,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "TS_Optics_WA_72_7mm": {
            "brand": "TS-Optics",
            "name": "WA 72° 7mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 150,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "TS_Optics_WA_72_10mm": {
            "brand": "TS-Optics",
            "name": "WA 72° 10mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 160,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "TS_Optics_WA_72_15mm": {
            "brand": "TS-Optics",
            "name": "WA 72° 15mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 175,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "TS_Optics_WA_72_20mm": {
            "brand": "TS-Optics",
            "name": "WA 72° 20mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 195,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "TS_Optics_WA_72_25mm": {
            "brand": "TS-Optics",
            "name": "WA 72° 25mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 220,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "TS_Optics_Expanse_4mm_70": {
            "brand": "TS-Optics",
            "name": "Expanse 4mm 70°",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 130,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "TS_Optics_Expanse_6mm_70": {
            "brand": "TS-Optics",
            "name": "Expanse 6mm 70°",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 135,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "TS_Optics_Expanse_8mm_70": {
            "brand": "TS-Optics",
            "name": "Expanse 8mm 70°",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 140,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "TS_Optics_Expanse_10mm_70": {
            "brand": "TS-Optics",
            "name": "Expanse 10mm 70°",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 150,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "TS_Optics_Expanse_13mm_70": {
            "brand": "TS-Optics",
            "name": "Expanse 13mm 70°",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 160,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "TS_Optics_Expanse_17mm_70": {
            "brand": "TS-Optics",
            "name": "Expanse 17mm 70°",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 175,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "TS_Optics_Expanse_22mm_70": {
            "brand": "TS-Optics",
            "name": "Expanse 22mm 70°",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 200,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "TS_Optics_Plossl_4mm": {
            "brand": "TS-Optics",
            "name": "Plossl 4mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 80,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "TS_Optics_Plossl_6_3mm": {
            "brand": "TS-Optics",
            "name": "Plossl 6.3mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 85,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "TS_Optics_Plossl_10mm": {
            "brand": "TS-Optics",
            "name": "Plossl 10mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 95,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "TS_Optics_Plossl_15mm": {
            "brand": "TS-Optics",
            "name": "Plossl 15mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 105,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "TS_Optics_Plossl_20mm": {
            "brand": "TS-Optics",
            "name": "Plossl 20mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 115,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "TS_Optics_Plossl_25mm": {
            "brand": "TS-Optics",
            "name": "Plossl 25mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 130,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "TS_Optics_Plossl_32mm": {
            "brand": "TS-Optics",
            "name": "Plossl 32mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 155,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "TS_Optics_Plossl_40mm": {
            "brand": "TS-Optics",
            "name": "Plossl 40mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 185,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Explore_Scientific_9mm_120": {
            "brand": "Explore Scientific",
            "name": "9mm 120°",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 500,
            "tside_thread": '2"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Explore_Scientific_10mm_52": {
            "brand": "Explore Scientific",
            "name": "10mm 52°",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 100,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Explore_Scientific_15mm_52": {
            "brand": "Explore Scientific",
            "name": "15mm 52°",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 110,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Explore_Scientific_20mm_52": {
            "brand": "Explore Scientific",
            "name": "20mm 52°",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 125,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Explore_Scientific_25mm_52": {
            "brand": "Explore Scientific",
            "name": "25mm 52°",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 140,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Explore_Scientific_40mm_52": {
            "brand": "Explore Scientific",
            "name": "40mm 52°",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 200,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "APM_UFF_10mm": {
            "brand": "APM",
            "name": "UFF 10mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 250,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "APM_UFF_15mm": {
            "brand": "APM",
            "name": "UFF 15mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 280,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "APM_UFF_18mm": {
            "brand": "APM",
            "name": "UFF 18mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 300,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "APM_UFF_24mm": {
            "brand": "APM",
            "name": "UFF 24mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 450,
            "tside_thread": '2"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "APM_UFF_30mm": {
            "brand": "APM",
            "name": "UFF 30mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 600,
            "tside_thread": '2"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "APM_Plossl_6_5mm": {
            "brand": "APM",
            "name": "Plossl 6.5mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 100,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "APM_Plossl_10mm": {
            "brand": "APM",
            "name": "Plossl 10mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 110,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "APM_Plossl_15mm": {
            "brand": "APM",
            "name": "Plossl 15mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 125,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "APM_Plossl_20mm": {
            "brand": "APM",
            "name": "Plossl 20mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 140,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "APM_Plossl_25mm": {
            "brand": "APM",
            "name": "Plossl 25mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 155,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "APM_Plossl_32mm": {
            "brand": "APM",
            "name": "Plossl 32mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 180,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "APM_Plossl_40mm": {
            "brand": "APM",
            "name": "Plossl 40mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 210,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Stellarvue_Optimus_3_5mm": {
            "brand": "Stellarvue",
            "name": "Optimus 3.5mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 190,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Stellarvue_Optimus_5mm": {
            "brand": "Stellarvue",
            "name": "Optimus 5mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 200,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Stellarvue_Optimus_7mm": {
            "brand": "Stellarvue",
            "name": "Optimus 7mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 210,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Stellarvue_Optimus_10mm": {
            "brand": "Stellarvue",
            "name": "Optimus 10mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 225,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Stellarvue_Optimus_14mm": {
            "brand": "Stellarvue",
            "name": "Optimus 14mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 250,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Stellarvue_Optimus_19mm": {
            "brand": "Stellarvue",
            "name": "Optimus 19mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 280,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Stellarvue_Optimus_28mm": {
            "brand": "Stellarvue",
            "name": "Optimus 28mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 450,
            "tside_thread": '2"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Meade_Series_4000_8_24mm_Zoom": {
            "brand": "Meade",
            "name": "Series 4000 8-24mm Zoom",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 350,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Baader_Hyperion_Mark_IV_8_24mm_Zoom": {
            "brand": "Baader",
            "name": "Hyperion Mark IV 8-24mm Zoom",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 400,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Celestron_8_24mm_Zoom": {
            "brand": "Celestron",
            "name": "8-24mm Zoom",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 280,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Sky_Watcher_7_2_21_5mm_Zoom": {
            "brand": "Sky-Watcher",
            "name": "7.2-21.5mm Zoom",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 300,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Orion_8_24mm_Zoom": {
            "brand": "Orion",
            "name": "8-24mm Zoom",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 250,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "SVBony_SV135_7_21mm_Zoom": {
            "brand": "SVBony",
            "name": "SV135 7-21mm Zoom",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 180,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Explore_Scientific_8_24mm_68_Zoom": {
            "brand": "Explore Scientific",
            "name": "8-24mm 68° Zoom",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 320,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Pentax_XF_6_5_19_5mm_Zoom": {
            "brand": "Pentax",
            "name": "XF 6.5-19.5mm Zoom",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 390,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Nikon_Fieldscope_Zoom_13_40mm": {
            "brand": "Nikon",
            "name": "Fieldscope Zoom 13-40mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 350,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Vixen_NLV_Zoom_8_24mm": {
            "brand": "Vixen",
            "name": "NLV Zoom 8-24mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 300,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Sky_Watcher_Starguider_Dual_ED_2_5mm": {
            "brand": "Sky-Watcher",
            "name": "Starguider Dual ED 2.5mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 170,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Sky_Watcher_Starguider_Dual_ED_3_2mm": {
            "brand": "Sky-Watcher",
            "name": "Starguider Dual ED 3.2mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 175,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Sky_Watcher_Starguider_Dual_ED_4mm": {
            "brand": "Sky-Watcher",
            "name": "Starguider Dual ED 4mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 180,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Sky_Watcher_Starguider_Dual_ED_5mm": {
            "brand": "Sky-Watcher",
            "name": "Starguider Dual ED 5mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 185,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Sky_Watcher_Starguider_Dual_ED_6mm": {
            "brand": "Sky-Watcher",
            "name": "Starguider Dual ED 6mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 192,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Sky_Watcher_Starguider_Dual_ED_8mm": {
            "brand": "Sky-Watcher",
            "name": "Starguider Dual ED 8mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 200,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Sky_Watcher_Starguider_Dual_ED_10mm": {
            "brand": "Sky-Watcher",
            "name": "Starguider Dual ED 10mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 210,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Sky_Watcher_Starguider_Dual_ED_15mm": {
            "brand": "Sky-Watcher",
            "name": "Starguider Dual ED 15mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 235,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Sky_Watcher_Starguider_Dual_ED_20mm": {
            "brand": "Sky-Watcher",
            "name": "Starguider Dual ED 20mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 265,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Sky_Watcher_Starguider_Dual_ED_25mm": {
            "brand": "Sky-Watcher",
            "name": "Starguider Dual ED 25mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 290,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Agena_SWA_4mm_70": {
            "brand": "Agena",
            "name": "SWA 4mm 70°",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 130,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Agena_SWA_6mm_70": {
            "brand": "Agena",
            "name": "SWA 6mm 70°",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 140,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Agena_SWA_9mm_70": {
            "brand": "Agena",
            "name": "SWA 9mm 70°",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 150,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Agena_SWA_12mm_70": {
            "brand": "Agena",
            "name": "SWA 12mm 70°",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 165,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Agena_SWA_15mm_70": {
            "brand": "Agena",
            "name": "SWA 15mm 70°",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 180,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Agena_SWA_20mm_70": {
            "brand": "Agena",
            "name": "SWA 20mm 70°",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 200,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Agena_SWA_25mm_70": {
            "brand": "Agena",
            "name": "SWA 25mm 70°",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 225,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Agena_SWA_32mm_70": {
            "brand": "Agena",
            "name": "SWA 32mm 70°",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 260,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Agena_EWA_3_5mm_82": {
            "brand": "Agena",
            "name": "EWA 3.5mm 82°",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 200,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Agena_EWA_5mm_82": {
            "brand": "Agena",
            "name": "EWA 5mm 82°",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 210,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Agena_EWA_7mm_82": {
            "brand": "Agena",
            "name": "EWA 7mm 82°",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 220,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Agena_EWA_9mm_82": {
            "brand": "Agena",
            "name": "EWA 9mm 82°",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 230,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Agena_EWA_13mm_82": {
            "brand": "Agena",
            "name": "EWA 13mm 82°",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 250,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Agena_EWA_16mm_82": {
            "brand": "Agena",
            "name": "EWA 16mm 82°",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 270,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Agena_EWA_20mm_82": {
            "brand": "Agena",
            "name": "EWA 20mm 82°",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 300,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Astro_Tech_Paradigm_3_5mm": {
            "brand": "Astro-Tech",
            "name": "Paradigm 3.5mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 170,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Astro_Tech_Paradigm_5mm": {
            "brand": "Astro-Tech",
            "name": "Paradigm 5mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 180,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Astro_Tech_Paradigm_7mm": {
            "brand": "Astro-Tech",
            "name": "Paradigm 7mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 190,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Astro_Tech_Paradigm_9mm": {
            "brand": "Astro-Tech",
            "name": "Paradigm 9mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 200,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Astro_Tech_Paradigm_12mm": {
            "brand": "Astro-Tech",
            "name": "Paradigm 12mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 220,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Astro_Tech_Paradigm_15mm": {
            "brand": "Astro-Tech",
            "name": "Paradigm 15mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 240,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Astro_Tech_Paradigm_18mm": {
            "brand": "Astro-Tech",
            "name": "Paradigm 18mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 260,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Astro_Tech_Paradigm_22mm": {
            "brand": "Astro-Tech",
            "name": "Paradigm 22mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 290,
            "tside_thread": '2"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Astro_Tech_Paradigm_27mm": {
            "brand": "Astro-Tech",
            "name": "Paradigm 27mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 350,
            "tside_thread": '2"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Astro_Tech_Titan_5mm_68": {
            "brand": "Astro-Tech",
            "name": "Titan 5mm 68°",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 130,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Astro_Tech_Titan_8mm_68": {
            "brand": "Astro-Tech",
            "name": "Titan 8mm 68°",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 140,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Astro_Tech_Titan_12mm_68": {
            "brand": "Astro-Tech",
            "name": "Titan 12mm 68°",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 155,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Astro_Tech_Titan_18mm_68": {
            "brand": "Astro-Tech",
            "name": "Titan 18mm 68°",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 180,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Astro_Tech_Titan_25mm_68": {
            "brand": "Astro-Tech",
            "name": "Titan 25mm 68°",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 210,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Lunt_Solar_EWA_6mm_82": {
            "brand": "Lunt Solar",
            "name": "EWA 6mm 82°",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 140,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Lunt_Solar_EWA_8mm_82": {
            "brand": "Lunt Solar",
            "name": "EWA 8mm 82°",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 150,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Lunt_Solar_EWA_10mm_82": {
            "brand": "Lunt Solar",
            "name": "EWA 10mm 82°",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 160,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Lunt_Solar_EWA_13mm_82": {
            "brand": "Lunt Solar",
            "name": "EWA 13mm 82°",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 175,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Lunt_Solar_EWA_16mm_82": {
            "brand": "Lunt Solar",
            "name": "EWA 16mm 82°",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 190,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Lunt_Solar_EWA_19mm_82": {
            "brand": "Lunt Solar",
            "name": "EWA 19mm 82°",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 210,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Lunt_Solar_EWA_22mm_82": {
            "brand": "Lunt Solar",
            "name": "EWA 22mm 82°",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 235,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Lunt_Solar_EWA_26mm_82": {
            "brand": "Lunt Solar",
            "name": "EWA 26mm 82°",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 270,
            "tside_thread": '2"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Lunt_Solar_EWA_32mm_82": {
            "brand": "Lunt Solar",
            "name": "EWA 32mm 82°",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 400,
            "tside_thread": '2"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Kasai_HD_Ortho_4mm": {
            "brand": "Kasai",
            "name": "HD Ortho 4mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 160,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Kasai_HD_Ortho_5mm": {
            "brand": "Kasai",
            "name": "HD Ortho 5mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 168,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Kasai_HD_Ortho_6mm": {
            "brand": "Kasai",
            "name": "HD Ortho 6mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 175,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Kasai_HD_Ortho_8mm": {
            "brand": "Kasai",
            "name": "HD Ortho 8mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 190,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Kasai_HD_Ortho_10mm": {
            "brand": "Kasai",
            "name": "HD Ortho 10mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 200,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Kasai_HD_Ortho_12_5mm": {
            "brand": "Kasai",
            "name": "HD Ortho 12.5mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 215,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Kasai_HD_Ortho_18mm": {
            "brand": "Kasai",
            "name": "HD Ortho 18mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 250,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Kasai_HD_Ortho_25mm": {
            "brand": "Kasai",
            "name": "HD Ortho 25mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 300,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Antares_Plossl_4mm": {
            "brand": "Antares",
            "name": "Plossl 4mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 120,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Antares_Plossl_6mm": {
            "brand": "Antares",
            "name": "Plossl 6mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 125,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Antares_Plossl_8mm": {
            "brand": "Antares",
            "name": "Plossl 8mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 130,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Antares_Plossl_10mm": {
            "brand": "Antares",
            "name": "Plossl 10mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 140,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Antares_Plossl_12_5mm": {
            "brand": "Antares",
            "name": "Plossl 12.5mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 155,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Antares_Plossl_15mm": {
            "brand": "Antares",
            "name": "Plossl 15mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 170,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Antares_Plossl_20mm": {
            "brand": "Antares",
            "name": "Plossl 20mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 195,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Antares_Plossl_25mm": {
            "brand": "Antares",
            "name": "Plossl 25mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 220,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Tecnosky_SWA_5mm_70": {
            "brand": "Tecnosky",
            "name": "SWA 5mm 70°",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 140,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Tecnosky_SWA_7mm_70": {
            "brand": "Tecnosky",
            "name": "SWA 7mm 70°",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 150,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Tecnosky_SWA_10mm_70": {
            "brand": "Tecnosky",
            "name": "SWA 10mm 70°",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 165,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Tecnosky_SWA_14mm_70": {
            "brand": "Tecnosky",
            "name": "SWA 14mm 70°",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 185,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Tecnosky_SWA_20mm_70": {
            "brand": "Tecnosky",
            "name": "SWA 20mm 70°",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 210,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Tecnosky_SWA_25mm_70": {
            "brand": "Tecnosky",
            "name": "SWA 25mm 70°",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 240,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Tecnosky_SWA_30mm_70": {
            "brand": "Tecnosky",
            "name": "SWA 30mm 70°",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 400,
            "tside_thread": '2"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Tecnosky_Plossl_6mm": {
            "brand": "Tecnosky",
            "name": "Plossl 6mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 95,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Tecnosky_Plossl_10mm": {
            "brand": "Tecnosky",
            "name": "Plossl 10mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 105,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Tecnosky_Plossl_15mm": {
            "brand": "Tecnosky",
            "name": "Plossl 15mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 120,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Tecnosky_Plossl_20mm": {
            "brand": "Tecnosky",
            "name": "Plossl 20mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 135,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Tecnosky_Plossl_25mm": {
            "brand": "Tecnosky",
            "name": "Plossl 25mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 155,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Tecnosky_Plossl_32mm": {
            "brand": "Tecnosky",
            "name": "Plossl 32mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 180,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "TPO_SWA_5mm_68": {
            "brand": "TPO",
            "name": "SWA 5mm 68°",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 120,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "TPO_SWA_8mm_68": {
            "brand": "TPO",
            "name": "SWA 8mm 68°",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 130,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "TPO_SWA_12mm_68": {
            "brand": "TPO",
            "name": "SWA 12mm 68°",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 145,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "TPO_SWA_18mm_68": {
            "brand": "TPO",
            "name": "SWA 18mm 68°",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 170,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "TPO_SWA_25mm_68": {
            "brand": "TPO",
            "name": "SWA 25mm 68°",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 200,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "TPO_SWA_32mm_68": {
            "brand": "TPO",
            "name": "SWA 32mm 68°",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 250,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "TPO_Plossl_6mm": {
            "brand": "TPO",
            "name": "Plossl 6mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 80,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "TPO_Plossl_10mm": {
            "brand": "TPO",
            "name": "Plossl 10mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 88,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "TPO_Plossl_15mm": {
            "brand": "TPO",
            "name": "Plossl 15mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 100,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "TPO_Plossl_20mm": {
            "brand": "TPO",
            "name": "Plossl 20mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 112,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "TPO_Plossl_25mm": {
            "brand": "TPO",
            "name": "Plossl 25mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 125,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "TPO_Plossl_32mm": {
            "brand": "TPO",
            "name": "Plossl 32mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 150,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Istar_UWA_3_5mm_100": {
            "brand": "Istar",
            "name": "UWA 3.5mm 100°",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 250,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Istar_UWA_5mm_100": {
            "brand": "Istar",
            "name": "UWA 5mm 100°",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 260,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Istar_UWA_7mm_100": {
            "brand": "Istar",
            "name": "UWA 7mm 100°",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 270,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Istar_UWA_10mm_100": {
            "brand": "Istar",
            "name": "UWA 10mm 100°",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 290,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Istar_UWA_14mm_100": {
            "brand": "Istar",
            "name": "UWA 14mm 100°",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 320,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Istar_UWA_18mm_100": {
            "brand": "Istar",
            "name": "UWA 18mm 100°",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 350,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Istar_UWA_22mm_100": {
            "brand": "Istar",
            "name": "UWA 22mm 100°",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 400,
            "tside_thread": '2"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Istar_UWA_30mm_100": {
            "brand": "Istar",
            "name": "UWA 30mm 100°",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 600,
            "tside_thread": '2"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Maxvision_3_5mm_82": {
            "brand": "Maxvision",
            "name": "3.5mm 82°",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 280,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Maxvision_6mm_82": {
            "brand": "Maxvision",
            "name": "6mm 82°",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 300,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Maxvision_9mm_82": {
            "brand": "Maxvision",
            "name": "9mm 82°",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 320,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Maxvision_13mm_82": {
            "brand": "Maxvision",
            "name": "13mm 82°",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 350,
            "tside_thread": '2"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Maxvision_20mm_82": {
            "brand": "Maxvision",
            "name": "20mm 82°",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 500,
            "tside_thread": '2"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Maxvision_28mm_82": {
            "brand": "Maxvision",
            "name": "28mm 82°",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 700,
            "tside_thread": '2"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Explore_Scientific_5mm_92": {
            "brand": "Explore Scientific",
            "name": "5mm 92°",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 280,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Explore_Scientific_8mm_92": {
            "brand": "Explore Scientific",
            "name": "8mm 92°",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 300,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Explore_Scientific_12mm_92": {
            "brand": "Explore Scientific",
            "name": "12mm 92°",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 320,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Explore_Scientific_17mm_92": {
            "brand": "Explore Scientific",
            "name": "17mm 92°",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 500,
            "tside_thread": '2"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Vixen_NPL_Plossl_2_5mm": {
            "brand": "Vixen",
            "name": "NPL Plossl 2.5mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 130,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Vixen_NPL_Plossl_4mm": {
            "brand": "Vixen",
            "name": "NPL Plossl 4mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 135,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Vixen_NPL_Plossl_5mm": {
            "brand": "Vixen",
            "name": "NPL Plossl 5mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 140,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Vixen_NPL_Plossl_6mm": {
            "brand": "Vixen",
            "name": "NPL Plossl 6mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 145,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Vixen_NPL_Plossl_8mm": {
            "brand": "Vixen",
            "name": "NPL Plossl 8mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 155,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Vixen_NPL_Plossl_10mm": {
            "brand": "Vixen",
            "name": "NPL Plossl 10mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 165,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Vixen_NPL_Plossl_12mm": {
            "brand": "Vixen",
            "name": "NPL Plossl 12mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 175,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Vixen_NPL_Plossl_15mm": {
            "brand": "Vixen",
            "name": "NPL Plossl 15mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 190,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Vixen_NPL_Plossl_18mm": {
            "brand": "Vixen",
            "name": "NPL Plossl 18mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 210,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Vixen_NPL_Plossl_25mm": {
            "brand": "Vixen",
            "name": "NPL Plossl 25mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 250,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Sky_Watcher_Long_Eye_Relief_4_5mm": {
            "brand": "Sky-Watcher",
            "name": "Long Eye Relief 4.5mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 130,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Sky_Watcher_Long_Eye_Relief_6mm": {
            "brand": "Sky-Watcher",
            "name": "Long Eye Relief 6mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 135,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Sky_Watcher_Long_Eye_Relief_8mm": {
            "brand": "Sky-Watcher",
            "name": "Long Eye Relief 8mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 145,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Sky_Watcher_Long_Eye_Relief_10mm": {
            "brand": "Sky-Watcher",
            "name": "Long Eye Relief 10mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 155,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Sky_Watcher_Long_Eye_Relief_12_5mm": {
            "brand": "Sky-Watcher",
            "name": "Long Eye Relief 12.5mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 165,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Sky_Watcher_Long_Eye_Relief_15mm": {
            "brand": "Sky-Watcher",
            "name": "Long Eye Relief 15mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 175,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Sky_Watcher_Long_Eye_Relief_18mm": {
            "brand": "Sky-Watcher",
            "name": "Long Eye Relief 18mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 190,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Sky_Watcher_Long_Eye_Relief_21mm": {
            "brand": "Sky-Watcher",
            "name": "Long Eye Relief 21mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 210,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Sky_Watcher_Long_Eye_Relief_25mm": {
            "brand": "Sky-Watcher",
            "name": "Long Eye Relief 25mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 240,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Generic_Plossl_32mm": {
            "brand": "Generic",
            "name": "Plossl 32mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 140,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Generic_SWA_6mm_70": {
            "brand": "Generic",
            "name": "SWA 6mm 70°",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 90,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Generic_SWA_10mm_70": {
            "brand": "Generic",
            "name": "SWA 10mm 70°",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 100,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Generic_SWA_15mm_70": {
            "brand": "Generic",
            "name": "SWA 15mm 70°",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 115,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Generic_SWA_20mm_70": {
            "brand": "Generic",
            "name": "SWA 20mm 70°",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 135,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Generic_SWA_25mm_70": {
            "brand": "Generic",
            "name": "SWA 25mm 70°",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 155,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Generic_SWA_32mm_70": {
            "brand": "Generic",
            "name": "SWA 32mm 70°",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 190,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Generic_WA_6mm_68": {
            "brand": "Generic",
            "name": "WA 6mm 68°",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 120,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Generic_WA_9mm_68": {
            "brand": "Generic",
            "name": "WA 9mm 68°",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 130,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Generic_WA_12mm_68": {
            "brand": "Generic",
            "name": "WA 12mm 68°",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 145,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Generic_WA_15mm_68": {
            "brand": "Generic",
            "name": "WA 15mm 68°",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 165,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Generic_WA_20mm_68": {
            "brand": "Generic",
            "name": "WA 20mm 68°",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 190,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Celestron_StarSense_10mm": {
            "brand": "Celestron",
            "name": "StarSense 10mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 115,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Celestron_StarSense_15mm": {
            "brand": "Celestron",
            "name": "StarSense 15mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 125,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Celestron_StarSense_20mm": {
            "brand": "Celestron",
            "name": "StarSense 20mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 135,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Celestron_StarSense_25mm": {
            "brand": "Celestron",
            "name": "StarSense 25mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 150,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Baader_Classic_Ortho_3_5mm_v2": {
            "brand": "Baader",
            "name": "Classic Ortho 3.5mm (v2)",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 75,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Baader_Classic_Ortho_5mm_v2": {
            "brand": "Baader",
            "name": "Classic Ortho 5mm (v2)",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 78,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Baader_Classic_Ortho_7mm_v2": {
            "brand": "Baader",
            "name": "Classic Ortho 7mm (v2)",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 82,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Baader_Classic_Ortho_12_5mm_v2": {
            "brand": "Baader",
            "name": "Classic Ortho 12.5mm (v2)",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 88,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Baader_Classic_Ortho_18mm_v2": {
            "brand": "Baader",
            "name": "Classic Ortho 18mm (v2)",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 92,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Baader_Classic_Ortho_25mm_v2": {
            "brand": "Baader",
            "name": "Classic Ortho 25mm (v2)",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 100,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Baader_Genuine_Ortho_4mm": {
            "brand": "Baader",
            "name": "Genuine Ortho 4mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 85,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Baader_Genuine_Ortho_5mm": {
            "brand": "Baader",
            "name": "Genuine Ortho 5mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 88,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Baader_Genuine_Ortho_6mm": {
            "brand": "Baader",
            "name": "Genuine Ortho 6mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 92,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Baader_Genuine_Ortho_7mm": {
            "brand": "Baader",
            "name": "Genuine Ortho 7mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 95,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Baader_Genuine_Ortho_9mm": {
            "brand": "Baader",
            "name": "Genuine Ortho 9mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 100,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Baader_Genuine_Ortho_10mm": {
            "brand": "Baader",
            "name": "Genuine Ortho 10mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 105,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Baader_Genuine_Ortho_12_5mm": {
            "brand": "Baader",
            "name": "Genuine Ortho 12.5mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 112,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Baader_Genuine_Ortho_18mm": {
            "brand": "Baader",
            "name": "Genuine Ortho 18mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 128,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Baader_Genuine_Ortho_25mm": {
            "brand": "Baader",
            "name": "Genuine Ortho 25mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 145,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Pentax_XL_2_5mm": {
            "brand": "Pentax",
            "name": "XL 2.5mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 200,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Pentax_XL_5_2mm": {
            "brand": "Pentax",
            "name": "XL 5.2mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 210,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Pentax_XL_7mm": {
            "brand": "Pentax",
            "name": "XL 7mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 220,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Pentax_XL_10_5mm": {
            "brand": "Pentax",
            "name": "XL 10.5mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 240,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Pentax_XL_14mm": {
            "brand": "Pentax",
            "name": "XL 14mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 260,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Pentax_XL_21mm": {
            "brand": "Pentax",
            "name": "XL 21mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 300,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Pentax_XL_28mm": {
            "brand": "Pentax",
            "name": "XL 28mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 420,
            "tside_thread": '2"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Pentax_XL_40mm": {
            "brand": "Pentax",
            "name": "XL 40mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 550,
            "tside_thread": '2"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Pentax_XO_2_5mm": {
            "brand": "Pentax",
            "name": "XO 2.5mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 250,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Pentax_XO_5mm": {
            "brand": "Pentax",
            "name": "XO 5mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 260,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Pentax_XO_10mm": {
            "brand": "Pentax",
            "name": "XO 10mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 280,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Nikon_NAV_HW_7mm": {
            "brand": "Nikon",
            "name": "NAV-HW 7mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 550,
            "tside_thread": '2"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Nikon_NAV_HW_14mm": {
            "brand": "Nikon",
            "name": "NAV-HW 14mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 630,
            "tside_thread": '2"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Takahashi_TOE_2_5mm": {
            "brand": "Takahashi",
            "name": "TOE 2.5mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 200,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Takahashi_TOE_4mm": {
            "brand": "Takahashi",
            "name": "TOE 4mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 210,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Takahashi_TOE_6mm": {
            "brand": "Takahashi",
            "name": "TOE 6mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 220,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Takahashi_TOE_8mm": {
            "brand": "Takahashi",
            "name": "TOE 8mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 235,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Takahashi_TOE_10mm": {
            "brand": "Takahashi",
            "name": "TOE 10mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 250,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Takahashi_TOE_18mm": {
            "brand": "Takahashi",
            "name": "TOE 18mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 310,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Leica_ASPH_6_5mm_v2": {
            "brand": "Leica",
            "name": "ASPH 6.5mm (v2)",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 320,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Leica_ASPH_12_5mm_v2": {
            "brand": "Leica",
            "name": "ASPH 12.5mm (v2)",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 370,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Leica_ASPH_20mm_v2": {
            "brand": "Leica",
            "name": "ASPH 20mm (v2)",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 400,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Siebert_Stellar_4mm": {
            "brand": "Siebert",
            "name": "Stellar 4mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 180,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Siebert_Stellar_6mm": {
            "brand": "Siebert",
            "name": "Stellar 6mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 190,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Siebert_Stellar_8mm": {
            "brand": "Siebert",
            "name": "Stellar 8mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 200,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Siebert_Stellar_10mm": {
            "brand": "Siebert",
            "name": "Stellar 10mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 215,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Siebert_Stellar_13mm": {
            "brand": "Siebert",
            "name": "Stellar 13mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 240,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Siebert_Stellar_18mm": {
            "brand": "Siebert",
            "name": "Stellar 18mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 270,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Siebert_Stellar_24mm": {
            "brand": "Siebert",
            "name": "Stellar 24mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 320,
            "tside_thread": '2"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Siebert_Stellar_36mm": {
            "brand": "Siebert",
            "name": "Stellar 36mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 500,
            "tside_thread": '2"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "TMB_Super_Mono_2_5mm": {
            "brand": "TMB",
            "name": "Super Mono 2.5mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 150,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "TMB_Super_Mono_3_2mm": {
            "brand": "TMB",
            "name": "Super Mono 3.2mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 155,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "TMB_Super_Mono_4mm": {
            "brand": "TMB",
            "name": "Super Mono 4mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 160,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "TMB_Super_Mono_5mm": {
            "brand": "TMB",
            "name": "Super Mono 5mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 168,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "TMB_Super_Mono_6mm": {
            "brand": "TMB",
            "name": "Super Mono 6mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 175,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "TMB_Super_Mono_7mm": {
            "brand": "TMB",
            "name": "Super Mono 7mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 180,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "TMB_Super_Mono_8mm": {
            "brand": "TMB",
            "name": "Super Mono 8mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 190,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "TMB_Super_Mono_9mm": {
            "brand": "TMB",
            "name": "Super Mono 9mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 195,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "TMB_Super_Mono_10mm": {
            "brand": "TMB",
            "name": "Super Mono 10mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 200,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "TMB_Super_Mono_12_5mm": {
            "brand": "TMB",
            "name": "Super Mono 12.5mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 220,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "TMB_Super_Mono_16mm": {
            "brand": "TMB",
            "name": "Super Mono 16mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 240,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "TMB_Super_Mono_20mm": {
            "brand": "TMB",
            "name": "Super Mono 20mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 260,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "TMB_Super_Mono_25mm": {
            "brand": "TMB",
            "name": "Super Mono 25mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 290,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Antares_W70_5mm": {
            "brand": "Antares",
            "name": "W70 5mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 140,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Antares_W70_8mm": {
            "brand": "Antares",
            "name": "W70 8mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 150,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Antares_W70_12mm": {
            "brand": "Antares",
            "name": "W70 12mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 170,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Antares_W70_18mm": {
            "brand": "Antares",
            "name": "W70 18mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 200,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Antares_W70_25mm": {
            "brand": "Antares",
            "name": "W70 25mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 235,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Antares_W70_32mm": {
            "brand": "Antares",
            "name": "W70 32mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 300,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Astro_Tech_EF_4_5mm_70": {
            "brand": "Astro-Tech",
            "name": "EF 4.5mm 70°",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 160,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Astro_Tech_EF_6_5mm_70": {
            "brand": "Astro-Tech",
            "name": "EF 6.5mm 70°",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 170,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Astro_Tech_EF_8_5mm_70": {
            "brand": "Astro-Tech",
            "name": "EF 8.5mm 70°",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 180,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Astro_Tech_EF_11mm_70": {
            "brand": "Astro-Tech",
            "name": "EF 11mm 70°",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 200,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Astro_Tech_EF_14mm_70": {
            "brand": "Astro-Tech",
            "name": "EF 14mm 70°",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 220,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Astro_Tech_EF_18mm_70": {
            "brand": "Astro-Tech",
            "name": "EF 18mm 70°",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 250,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Astro_Tech_EF_24mm_70": {
            "brand": "Astro-Tech",
            "name": "EF 24mm 70°",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 320,
            "tside_thread": '2"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Astro_Tech_EF_30mm_70": {
            "brand": "Astro-Tech",
            "name": "EF 30mm 70°",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 450,
            "tside_thread": '2"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Lunt_Solar_Solar_7_5mm": {
            "brand": "Lunt Solar",
            "name": "Solar 7.5mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 170,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Lunt_Solar_Solar_10mm": {
            "brand": "Lunt Solar",
            "name": "Solar 10mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 180,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Lunt_Solar_Solar_12mm": {
            "brand": "Lunt Solar",
            "name": "Solar 12mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 190,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Lunt_Solar_Solar_16mm": {
            "brand": "Lunt Solar",
            "name": "Solar 16mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 210,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Lunt_Solar_Solar_19mm": {
            "brand": "Lunt Solar",
            "name": "Solar 19mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 230,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Lunt_Solar_Solar_25mm": {
            "brand": "Lunt Solar",
            "name": "Solar 25mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 260,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Lunt_Solar_Solar_32mm": {
            "brand": "Lunt Solar",
            "name": "Solar 32mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 350,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Agena_Starguider_Plossl_6mm": {
            "brand": "Agena",
            "name": "Starguider Plossl 6mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 100,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Agena_Starguider_Plossl_8mm": {
            "brand": "Agena",
            "name": "Starguider Plossl 8mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 108,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Agena_Starguider_Plossl_10mm": {
            "brand": "Agena",
            "name": "Starguider Plossl 10mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 115,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Agena_Starguider_Plossl_12_5mm": {
            "brand": "Agena",
            "name": "Starguider Plossl 12.5mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 125,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Agena_Starguider_Plossl_15mm": {
            "brand": "Agena",
            "name": "Starguider Plossl 15mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 135,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Agena_Starguider_Plossl_20mm": {
            "brand": "Agena",
            "name": "Starguider Plossl 20mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 155,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Agena_Starguider_Plossl_25mm": {
            "brand": "Agena",
            "name": "Starguider Plossl 25mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 175,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Agena_Starguider_Plossl_32mm": {
            "brand": "Agena",
            "name": "Starguider Plossl 32mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 210,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Agena_Starguider_Plossl_40mm": {
            "brand": "Agena",
            "name": "Starguider Plossl 40mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 260,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Stellarvue_Optimus_Wide_5mm": {
            "brand": "Stellarvue",
            "name": "Optimus Wide 5mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 220,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Stellarvue_Optimus_Wide_8mm": {
            "brand": "Stellarvue",
            "name": "Optimus Wide 8mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 240,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Stellarvue_Optimus_Wide_12mm": {
            "brand": "Stellarvue",
            "name": "Optimus Wide 12mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 260,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Stellarvue_Optimus_Wide_16mm": {
            "brand": "Stellarvue",
            "name": "Optimus Wide 16mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 290,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Stellarvue_Optimus_Wide_22mm": {
            "brand": "Stellarvue",
            "name": "Optimus Wide 22mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 350,
            "tside_thread": '2"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Stellarvue_Optimus_Wide_32mm": {
            "brand": "Stellarvue",
            "name": "Optimus Wide 32mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 500,
            "tside_thread": '2"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "William_Optics_XWA_3_5mm_110": {
            "brand": "William Optics",
            "name": "XWA 3.5mm 110°",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 280,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "William_Optics_XWA_7mm_110": {
            "brand": "William Optics",
            "name": "XWA 7mm 110°",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 300,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "William_Optics_XWA_13mm_110": {
            "brand": "William Optics",
            "name": "XWA 13mm 110°",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 350,
            "tside_thread": '2"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "William_Optics_XWA_20mm_110": {
            "brand": "William Optics",
            "name": "XWA 20mm 110°",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 500,
            "tside_thread": '2"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Orion_Epic_ED_2_5mm": {
            "brand": "Orion",
            "name": "Epic ED-2 5mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 180,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Orion_Epic_ED_2_7mm": {
            "brand": "Orion",
            "name": "Epic ED-2 7mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 190,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Orion_Epic_ED_2_10mm": {
            "brand": "Orion",
            "name": "Epic ED-2 10mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 200,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Orion_Epic_ED_2_15mm": {
            "brand": "Orion",
            "name": "Epic ED-2 15mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 230,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Orion_Epic_ED_2_20mm": {
            "brand": "Orion",
            "name": "Epic ED-2 20mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 260,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Orion_Epic_ED_2_25mm": {
            "brand": "Orion",
            "name": "Epic ED-2 25mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 290,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Orion_UltraView_5mm": {
            "brand": "Orion",
            "name": "UltraView 5mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 100,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Orion_UltraView_10mm": {
            "brand": "Orion",
            "name": "UltraView 10mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 108,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Orion_UltraView_15mm": {
            "brand": "Orion",
            "name": "UltraView 15mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 118,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Orion_UltraView_20mm": {
            "brand": "Orion",
            "name": "UltraView 20mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 130,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Orion_UltraView_25mm": {
            "brand": "Orion",
            "name": "UltraView 25mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 145,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Orion_UltraView_35mm": {
            "brand": "Orion",
            "name": "UltraView 35mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 200,
            "tside_thread": '2"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Meade_HD_60_8_5mm_60": {
            "brand": "Meade",
            "name": "HD-60 8.5mm 60°",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 205,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Meade_HD_60_12mm_60": {
            "brand": "Meade",
            "name": "HD-60 12mm 60°",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 225,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Meade_HD_60_16mm_60": {
            "brand": "Meade",
            "name": "HD-60 16mm 60°",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 245,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Meade_HD_60_20mm_60": {
            "brand": "Meade",
            "name": "HD-60 20mm 60°",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 265,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Meade_HD_60_28mm_60": {
            "brand": "Meade",
            "name": "HD-60 28mm 60°",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 450,
            "tside_thread": '2"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Omegon_Flatfield_4mm_65": {
            "brand": "Omegon",
            "name": "Flatfield 4mm 65°",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 140,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Omegon_Flatfield_6mm_65": {
            "brand": "Omegon",
            "name": "Flatfield 6mm 65°",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 150,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Omegon_Flatfield_8mm_65": {
            "brand": "Omegon",
            "name": "Flatfield 8mm 65°",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 160,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Omegon_Flatfield_10mm_65": {
            "brand": "Omegon",
            "name": "Flatfield 10mm 65°",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 172,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Omegon_Flatfield_13mm_65": {
            "brand": "Omegon",
            "name": "Flatfield 13mm 65°",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 190,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Omegon_Flatfield_16mm_65": {
            "brand": "Omegon",
            "name": "Flatfield 16mm 65°",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 210,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Omegon_Flatfield_19mm_65": {
            "brand": "Omegon",
            "name": "Flatfield 19mm 65°",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 235,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Omegon_Flatfield_24mm_65": {
            "brand": "Omegon",
            "name": "Flatfield 24mm 65°",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 280,
            "tside_thread": '2"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Omegon_Flatfield_32mm_65": {
            "brand": "Omegon",
            "name": "Flatfield 32mm 65°",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 400,
            "tside_thread": '2"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Bresser_Wide_Field_4mm": {
            "brand": "Bresser",
            "name": "Wide Field 4mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 100,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Bresser_Wide_Field_6mm": {
            "brand": "Bresser",
            "name": "Wide Field 6mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 108,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Bresser_Wide_Field_8mm": {
            "brand": "Bresser",
            "name": "Wide Field 8mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 115,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Bresser_Wide_Field_11mm": {
            "brand": "Bresser",
            "name": "Wide Field 11mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 128,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Bresser_Wide_Field_14mm": {
            "brand": "Bresser",
            "name": "Wide Field 14mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 140,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Bresser_Wide_Field_18mm": {
            "brand": "Bresser",
            "name": "Wide Field 18mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 160,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Bresser_Wide_Field_23mm": {
            "brand": "Bresser",
            "name": "Wide Field 23mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 200,
            "tside_thread": '2"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Bresser_Wide_Field_28mm": {
            "brand": "Bresser",
            "name": "Wide Field 28mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 280,
            "tside_thread": '2"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Celestron_Ultima_Duo_6mm_v2": {
            "brand": "Celestron",
            "name": "Ultima Duo 6mm (v2)",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 140,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Celestron_Ultima_Duo_8mm_v2": {
            "brand": "Celestron",
            "name": "Ultima Duo 8mm (v2)",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 150,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Celestron_Ultima_Duo_10mm_v2": {
            "brand": "Celestron",
            "name": "Ultima Duo 10mm (v2)",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 160,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Celestron_Ultima_Duo_12mm_v2": {
            "brand": "Celestron",
            "name": "Ultima Duo 12mm (v2)",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 175,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Celestron_Ultima_Duo_15mm_v2": {
            "brand": "Celestron",
            "name": "Ultima Duo 15mm (v2)",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 195,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Celestron_Ultima_Duo_20mm_v2": {
            "brand": "Celestron",
            "name": "Ultima Duo 20mm (v2)",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 225,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Celestron_Ultima_Duo_25mm_v2": {
            "brand": "Celestron",
            "name": "Ultima Duo 25mm (v2)",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 260,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "TS_Optics_SuperFlat_4mm": {
            "brand": "TS-Optics",
            "name": "SuperFlat 4mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 160,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "TS_Optics_SuperFlat_6mm": {
            "brand": "TS-Optics",
            "name": "SuperFlat 6mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 170,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "TS_Optics_SuperFlat_8mm": {
            "brand": "TS-Optics",
            "name": "SuperFlat 8mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 180,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "TS_Optics_SuperFlat_10mm": {
            "brand": "TS-Optics",
            "name": "SuperFlat 10mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 190,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "TS_Optics_SuperFlat_13mm": {
            "brand": "TS-Optics",
            "name": "SuperFlat 13mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 210,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "TS_Optics_SuperFlat_16mm": {
            "brand": "TS-Optics",
            "name": "SuperFlat 16mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 230,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "TS_Optics_SuperFlat_22mm": {
            "brand": "TS-Optics",
            "name": "SuperFlat 22mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 290,
            "tside_thread": '2"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "TS_Optics_SuperFlat_30mm": {
            "brand": "TS-Optics",
            "name": "SuperFlat 30mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 450,
            "tside_thread": '2"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "SVBony_SV215_UWA_4mm": {
            "brand": "SVBony",
            "name": "SV215 UWA 4mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 170,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "SVBony_SV215_UWA_6mm": {
            "brand": "SVBony",
            "name": "SV215 UWA 6mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 180,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "SVBony_SV215_UWA_8mm": {
            "brand": "SVBony",
            "name": "SV215 UWA 8mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 190,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "SVBony_SV215_UWA_10mm": {
            "brand": "SVBony",
            "name": "SV215 UWA 10mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 200,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "SVBony_SV215_UWA_13mm": {
            "brand": "SVBony",
            "name": "SV215 UWA 13mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 220,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "SVBony_SV215_UWA_16mm": {
            "brand": "SVBony",
            "name": "SV215 UWA 16mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 240,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "SVBony_SV215_UWA_20mm": {
            "brand": "SVBony",
            "name": "SV215 UWA 20mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 270,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "GSO_SuperPlossl_4mm": {
            "brand": "GSO",
            "name": "SuperPlossl 4mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 82,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "GSO_SuperPlossl_5mm": {
            "brand": "GSO",
            "name": "SuperPlossl 5mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 85,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "GSO_SuperPlossl_7_5mm": {
            "brand": "GSO",
            "name": "SuperPlossl 7.5mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 92,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "GSO_SuperPlossl_9_7mm": {
            "brand": "GSO",
            "name": "SuperPlossl 9.7mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 98,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "GSO_SuperPlossl_12_5mm": {
            "brand": "GSO",
            "name": "SuperPlossl 12.5mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 108,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "GSO_SuperPlossl_15mm": {
            "brand": "GSO",
            "name": "SuperPlossl 15mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 118,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "GSO_SuperPlossl_17mm": {
            "brand": "GSO",
            "name": "SuperPlossl 17mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 128,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "GSO_SuperPlossl_20mm": {
            "brand": "GSO",
            "name": "SuperPlossl 20mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 138,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "GSO_SuperPlossl_25mm": {
            "brand": "GSO",
            "name": "SuperPlossl 25mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 155,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "GSO_SuperPlossl_30mm": {
            "brand": "GSO",
            "name": "SuperPlossl 30mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 180,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "GSO_SuperPlossl_40mm": {
            "brand": "GSO",
            "name": "SuperPlossl 40mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 215,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Vixen_HR_1_6mm": {
            "brand": "Vixen",
            "name": "HR 1.6mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 200,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Vixen_HR_2mm": {
            "brand": "Vixen",
            "name": "HR 2mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 205,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Vixen_HR_2_4mm": {
            "brand": "Vixen",
            "name": "HR 2.4mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 210,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Vixen_HR_3_4mm": {
            "brand": "Vixen",
            "name": "HR 3.4mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 215,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Celestron_12mm_Reticle_Eyepiece_1_25": {
            "brand": "Celestron",
            "name": '12mm Reticle Eyepiece (1.25")',
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 150,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Meade_12mm_Reticle_Eyepiece_1_25": {
            "brand": "Meade",
            "name": '12mm Reticle Eyepiece (1.25")',
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 140,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Orion_12mm_Reticle_Eyepiece_1_25": {
            "brand": "Orion",
            "name": '12mm Reticle Eyepiece (1.25")',
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 135,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Sky_Watcher_12mm_Reticle_Eyepiece_1_25": {
            "brand": "Sky-Watcher",
            "name": '12mm Reticle Eyepiece (1.25")',
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 130,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "Baader_Micro_Guide_Eyepiece_12_5mm": {
            "brand": "Baader",
            "name": "Micro Guide Eyepiece 12.5mm",
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 200,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
        "TeleVue_Starbeam_1_25": {
            "brand": "TeleVue",
            "name": 'Starbeam (1.25")',
            "type": "type_eyepiece",
            "optical_length": 0,
            "mass": 120,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "",
        },
    }

    @classmethod
    def TeleVue_Ethos_3_7mm(cls):
        return cls.from_database(cls._DATABASE["TeleVue_Ethos_3_7mm"])

    @classmethod
    def TeleVue_Ethos_6mm(cls):
        return cls.from_database(cls._DATABASE["TeleVue_Ethos_6mm"])

    @classmethod
    def TeleVue_Ethos_8mm(cls):
        return cls.from_database(cls._DATABASE["TeleVue_Ethos_8mm"])

    @classmethod
    def TeleVue_Ethos_10mm(cls):
        return cls.from_database(cls._DATABASE["TeleVue_Ethos_10mm"])

    @classmethod
    def TeleVue_Ethos_13mm(cls):
        return cls.from_database(cls._DATABASE["TeleVue_Ethos_13mm"])

    @classmethod
    def TeleVue_Ethos_17mm(cls):
        return cls.from_database(cls._DATABASE["TeleVue_Ethos_17mm"])

    @classmethod
    def TeleVue_Ethos_21mm(cls):
        return cls.from_database(cls._DATABASE["TeleVue_Ethos_21mm"])

    @classmethod
    def TeleVue_Nagler_3_5mm(cls):
        return cls.from_database(cls._DATABASE["TeleVue_Nagler_3_5mm"])

    @classmethod
    def TeleVue_Nagler_5mm(cls):
        return cls.from_database(cls._DATABASE["TeleVue_Nagler_5mm"])

    @classmethod
    def TeleVue_Nagler_7mm(cls):
        return cls.from_database(cls._DATABASE["TeleVue_Nagler_7mm"])

    @classmethod
    def TeleVue_Nagler_9mm(cls):
        return cls.from_database(cls._DATABASE["TeleVue_Nagler_9mm"])

    @classmethod
    def TeleVue_Nagler_11mm(cls):
        return cls.from_database(cls._DATABASE["TeleVue_Nagler_11mm"])

    @classmethod
    def TeleVue_Nagler_13mm(cls):
        return cls.from_database(cls._DATABASE["TeleVue_Nagler_13mm"])

    @classmethod
    def TeleVue_Nagler_16mm(cls):
        return cls.from_database(cls._DATABASE["TeleVue_Nagler_16mm"])

    @classmethod
    def TeleVue_Nagler_22mm(cls):
        return cls.from_database(cls._DATABASE["TeleVue_Nagler_22mm"])

    @classmethod
    def TeleVue_Nagler_31mm(cls):
        return cls.from_database(cls._DATABASE["TeleVue_Nagler_31mm"])

    @classmethod
    def TeleVue_Delos_3_5mm(cls):
        return cls.from_database(cls._DATABASE["TeleVue_Delos_3_5mm"])

    @classmethod
    def TeleVue_Delos_6mm(cls):
        return cls.from_database(cls._DATABASE["TeleVue_Delos_6mm"])

    @classmethod
    def TeleVue_Delos_8mm(cls):
        return cls.from_database(cls._DATABASE["TeleVue_Delos_8mm"])

    @classmethod
    def TeleVue_Delos_10mm(cls):
        return cls.from_database(cls._DATABASE["TeleVue_Delos_10mm"])

    @classmethod
    def TeleVue_Delos_12mm(cls):
        return cls.from_database(cls._DATABASE["TeleVue_Delos_12mm"])

    @classmethod
    def TeleVue_Delos_14mm(cls):
        return cls.from_database(cls._DATABASE["TeleVue_Delos_14mm"])

    @classmethod
    def TeleVue_Delos_17_3mm(cls):
        return cls.from_database(cls._DATABASE["TeleVue_Delos_17_3mm"])

    @classmethod
    def TeleVue_Panoptic_15mm(cls):
        return cls.from_database(cls._DATABASE["TeleVue_Panoptic_15mm"])

    @classmethod
    def TeleVue_Panoptic_19mm(cls):
        return cls.from_database(cls._DATABASE["TeleVue_Panoptic_19mm"])

    @classmethod
    def TeleVue_Panoptic_22mm(cls):
        return cls.from_database(cls._DATABASE["TeleVue_Panoptic_22mm"])

    @classmethod
    def TeleVue_Panoptic_24mm(cls):
        return cls.from_database(cls._DATABASE["TeleVue_Panoptic_24mm"])

    @classmethod
    def TeleVue_Panoptic_27mm(cls):
        return cls.from_database(cls._DATABASE["TeleVue_Panoptic_27mm"])

    @classmethod
    def TeleVue_Panoptic_35mm(cls):
        return cls.from_database(cls._DATABASE["TeleVue_Panoptic_35mm"])

    @classmethod
    def TeleVue_Panoptic_41mm(cls):
        return cls.from_database(cls._DATABASE["TeleVue_Panoptic_41mm"])

    @classmethod
    def TeleVue_Plossl_8mm(cls):
        return cls.from_database(cls._DATABASE["TeleVue_Plossl_8mm"])

    @classmethod
    def TeleVue_Plossl_11mm(cls):
        return cls.from_database(cls._DATABASE["TeleVue_Plossl_11mm"])

    @classmethod
    def TeleVue_Plossl_15mm(cls):
        return cls.from_database(cls._DATABASE["TeleVue_Plossl_15mm"])

    @classmethod
    def TeleVue_Plossl_20mm(cls):
        return cls.from_database(cls._DATABASE["TeleVue_Plossl_20mm"])

    @classmethod
    def TeleVue_Plossl_25mm(cls):
        return cls.from_database(cls._DATABASE["TeleVue_Plossl_25mm"])

    @classmethod
    def TeleVue_Plossl_32mm(cls):
        return cls.from_database(cls._DATABASE["TeleVue_Plossl_32mm"])

    @classmethod
    def TeleVue_Plossl_40mm(cls):
        return cls.from_database(cls._DATABASE["TeleVue_Plossl_40mm"])

    @classmethod
    def TeleVue_Radian_3mm(cls):
        return cls.from_database(cls._DATABASE["TeleVue_Radian_3mm"])

    @classmethod
    def TeleVue_Radian_4mm(cls):
        return cls.from_database(cls._DATABASE["TeleVue_Radian_4mm"])

    @classmethod
    def TeleVue_Radian_5mm(cls):
        return cls.from_database(cls._DATABASE["TeleVue_Radian_5mm"])

    @classmethod
    def TeleVue_Radian_6mm(cls):
        return cls.from_database(cls._DATABASE["TeleVue_Radian_6mm"])

    @classmethod
    def TeleVue_Radian_8mm(cls):
        return cls.from_database(cls._DATABASE["TeleVue_Radian_8mm"])

    @classmethod
    def TeleVue_Radian_10mm(cls):
        return cls.from_database(cls._DATABASE["TeleVue_Radian_10mm"])

    @classmethod
    def TeleVue_Radian_12mm(cls):
        return cls.from_database(cls._DATABASE["TeleVue_Radian_12mm"])

    @classmethod
    def TeleVue_Radian_14mm(cls):
        return cls.from_database(cls._DATABASE["TeleVue_Radian_14mm"])

    @classmethod
    def TeleVue_Radian_18mm(cls):
        return cls.from_database(cls._DATABASE["TeleVue_Radian_18mm"])

    @classmethod
    def Baader_Hyperion_5mm(cls):
        return cls.from_database(cls._DATABASE["Baader_Hyperion_5mm"])

    @classmethod
    def Baader_Hyperion_8mm(cls):
        return cls.from_database(cls._DATABASE["Baader_Hyperion_8mm"])

    @classmethod
    def Baader_Hyperion_10mm(cls):
        return cls.from_database(cls._DATABASE["Baader_Hyperion_10mm"])

    @classmethod
    def Baader_Hyperion_13mm(cls):
        return cls.from_database(cls._DATABASE["Baader_Hyperion_13mm"])

    @classmethod
    def Baader_Hyperion_17mm(cls):
        return cls.from_database(cls._DATABASE["Baader_Hyperion_17mm"])

    @classmethod
    def Baader_Hyperion_21mm(cls):
        return cls.from_database(cls._DATABASE["Baader_Hyperion_21mm"])

    @classmethod
    def Baader_Hyperion_24mm(cls):
        return cls.from_database(cls._DATABASE["Baader_Hyperion_24mm"])

    @classmethod
    def Baader_Hyperion_36mm(cls):
        return cls.from_database(cls._DATABASE["Baader_Hyperion_36mm"])

    @classmethod
    def Baader_Morpheus_4_5mm(cls):
        return cls.from_database(cls._DATABASE["Baader_Morpheus_4_5mm"])

    @classmethod
    def Baader_Morpheus_6_5mm(cls):
        return cls.from_database(cls._DATABASE["Baader_Morpheus_6_5mm"])

    @classmethod
    def Baader_Morpheus_9mm(cls):
        return cls.from_database(cls._DATABASE["Baader_Morpheus_9mm"])

    @classmethod
    def Baader_Morpheus_12_5mm(cls):
        return cls.from_database(cls._DATABASE["Baader_Morpheus_12_5mm"])

    @classmethod
    def Baader_Morpheus_14mm(cls):
        return cls.from_database(cls._DATABASE["Baader_Morpheus_14mm"])

    @classmethod
    def Baader_Morpheus_17_5mm(cls):
        return cls.from_database(cls._DATABASE["Baader_Morpheus_17_5mm"])

    @classmethod
    def Baader_Classic_Ortho_6mm(cls):
        return cls.from_database(cls._DATABASE["Baader_Classic_Ortho_6mm"])

    @classmethod
    def Baader_Classic_Ortho_10mm(cls):
        return cls.from_database(cls._DATABASE["Baader_Classic_Ortho_10mm"])

    @classmethod
    def Baader_Classic_Ortho_18mm(cls):
        return cls.from_database(cls._DATABASE["Baader_Classic_Ortho_18mm"])

    @classmethod
    def Explore_Scientific_4_5mm_82(cls):
        return cls.from_database(cls._DATABASE["Explore_Scientific_4_5mm_82"])

    @classmethod
    def Explore_Scientific_6_5mm_82(cls):
        return cls.from_database(cls._DATABASE["Explore_Scientific_6_5mm_82"])

    @classmethod
    def Explore_Scientific_8_8mm_82(cls):
        return cls.from_database(cls._DATABASE["Explore_Scientific_8_8mm_82"])

    @classmethod
    def Explore_Scientific_11mm_82(cls):
        return cls.from_database(cls._DATABASE["Explore_Scientific_11mm_82"])

    @classmethod
    def Explore_Scientific_14mm_82(cls):
        return cls.from_database(cls._DATABASE["Explore_Scientific_14mm_82"])

    @classmethod
    def Explore_Scientific_18mm_82(cls):
        return cls.from_database(cls._DATABASE["Explore_Scientific_18mm_82"])

    @classmethod
    def Explore_Scientific_24mm_82(cls):
        return cls.from_database(cls._DATABASE["Explore_Scientific_24mm_82"])

    @classmethod
    def Explore_Scientific_30mm_82(cls):
        return cls.from_database(cls._DATABASE["Explore_Scientific_30mm_82"])

    @classmethod
    def Explore_Scientific_5_5mm_62(cls):
        return cls.from_database(cls._DATABASE["Explore_Scientific_5_5mm_62"])

    @classmethod
    def Explore_Scientific_9mm_62(cls):
        return cls.from_database(cls._DATABASE["Explore_Scientific_9mm_62"])

    @classmethod
    def Explore_Scientific_14mm_62(cls):
        return cls.from_database(cls._DATABASE["Explore_Scientific_14mm_62"])

    @classmethod
    def Explore_Scientific_20mm_62(cls):
        return cls.from_database(cls._DATABASE["Explore_Scientific_20mm_62"])

    @classmethod
    def Explore_Scientific_26mm_62(cls):
        return cls.from_database(cls._DATABASE["Explore_Scientific_26mm_62"])

    @classmethod
    def Explore_Scientific_32mm_62(cls):
        return cls.from_database(cls._DATABASE["Explore_Scientific_32mm_62"])

    @classmethod
    def Explore_Scientific_40mm_62(cls):
        return cls.from_database(cls._DATABASE["Explore_Scientific_40mm_62"])

    @classmethod
    def Explore_Scientific_5_5mm_100(cls):
        return cls.from_database(cls._DATABASE["Explore_Scientific_5_5mm_100"])

    @classmethod
    def Explore_Scientific_9mm_100(cls):
        return cls.from_database(cls._DATABASE["Explore_Scientific_9mm_100"])

    @classmethod
    def Explore_Scientific_14mm_100(cls):
        return cls.from_database(cls._DATABASE["Explore_Scientific_14mm_100"])

    @classmethod
    def Explore_Scientific_20mm_100(cls):
        return cls.from_database(cls._DATABASE["Explore_Scientific_20mm_100"])

    @classmethod
    def Explore_Scientific_25mm_100(cls):
        return cls.from_database(cls._DATABASE["Explore_Scientific_25mm_100"])

    @classmethod
    def Explore_Scientific_16mm_68(cls):
        return cls.from_database(cls._DATABASE["Explore_Scientific_16mm_68"])

    @classmethod
    def Explore_Scientific_20mm_68(cls):
        return cls.from_database(cls._DATABASE["Explore_Scientific_20mm_68"])

    @classmethod
    def Explore_Scientific_24mm_68(cls):
        return cls.from_database(cls._DATABASE["Explore_Scientific_24mm_68"])

    @classmethod
    def Explore_Scientific_28mm_68(cls):
        return cls.from_database(cls._DATABASE["Explore_Scientific_28mm_68"])

    @classmethod
    def Explore_Scientific_34mm_68(cls):
        return cls.from_database(cls._DATABASE["Explore_Scientific_34mm_68"])

    @classmethod
    def Explore_Scientific_40mm_68(cls):
        return cls.from_database(cls._DATABASE["Explore_Scientific_40mm_68"])

    @classmethod
    def Celestron_Luminos_7mm(cls):
        return cls.from_database(cls._DATABASE["Celestron_Luminos_7mm"])

    @classmethod
    def Celestron_Luminos_10mm(cls):
        return cls.from_database(cls._DATABASE["Celestron_Luminos_10mm"])

    @classmethod
    def Celestron_Luminos_15mm(cls):
        return cls.from_database(cls._DATABASE["Celestron_Luminos_15mm"])

    @classmethod
    def Celestron_Luminos_19mm(cls):
        return cls.from_database(cls._DATABASE["Celestron_Luminos_19mm"])

    @classmethod
    def Celestron_Luminos_23mm(cls):
        return cls.from_database(cls._DATABASE["Celestron_Luminos_23mm"])

    @classmethod
    def Celestron_Luminos_31mm(cls):
        return cls.from_database(cls._DATABASE["Celestron_Luminos_31mm"])

    @classmethod
    def Celestron_X_Cel_LX_2_3mm(cls):
        return cls.from_database(cls._DATABASE["Celestron_X_Cel_LX_2_3mm"])

    @classmethod
    def Celestron_X_Cel_LX_5mm(cls):
        return cls.from_database(cls._DATABASE["Celestron_X_Cel_LX_5mm"])

    @classmethod
    def Celestron_X_Cel_LX_7mm(cls):
        return cls.from_database(cls._DATABASE["Celestron_X_Cel_LX_7mm"])

    @classmethod
    def Celestron_X_Cel_LX_9mm(cls):
        return cls.from_database(cls._DATABASE["Celestron_X_Cel_LX_9mm"])

    @classmethod
    def Celestron_X_Cel_LX_12mm(cls):
        return cls.from_database(cls._DATABASE["Celestron_X_Cel_LX_12mm"])

    @classmethod
    def Celestron_X_Cel_LX_18mm(cls):
        return cls.from_database(cls._DATABASE["Celestron_X_Cel_LX_18mm"])

    @classmethod
    def Celestron_X_Cel_LX_25mm(cls):
        return cls.from_database(cls._DATABASE["Celestron_X_Cel_LX_25mm"])

    @classmethod
    def Celestron_Plossl_6mm(cls):
        return cls.from_database(cls._DATABASE["Celestron_Plossl_6mm"])

    @classmethod
    def Celestron_Plossl_8mm(cls):
        return cls.from_database(cls._DATABASE["Celestron_Plossl_8mm"])

    @classmethod
    def Celestron_Plossl_10mm(cls):
        return cls.from_database(cls._DATABASE["Celestron_Plossl_10mm"])

    @classmethod
    def Celestron_Plossl_15mm(cls):
        return cls.from_database(cls._DATABASE["Celestron_Plossl_15mm"])

    @classmethod
    def Celestron_Plossl_17mm(cls):
        return cls.from_database(cls._DATABASE["Celestron_Plossl_17mm"])

    @classmethod
    def Celestron_Plossl_20mm(cls):
        return cls.from_database(cls._DATABASE["Celestron_Plossl_20mm"])

    @classmethod
    def Celestron_Plossl_25mm(cls):
        return cls.from_database(cls._DATABASE["Celestron_Plossl_25mm"])

    @classmethod
    def Celestron_Plossl_32mm(cls):
        return cls.from_database(cls._DATABASE["Celestron_Plossl_32mm"])

    @classmethod
    def Celestron_Plossl_40mm(cls):
        return cls.from_database(cls._DATABASE["Celestron_Plossl_40mm"])

    @classmethod
    def Pentax_XW_3_5mm(cls):
        return cls.from_database(cls._DATABASE["Pentax_XW_3_5mm"])

    @classmethod
    def Pentax_XW_5mm(cls):
        return cls.from_database(cls._DATABASE["Pentax_XW_5mm"])

    @classmethod
    def Pentax_XW_7mm(cls):
        return cls.from_database(cls._DATABASE["Pentax_XW_7mm"])

    @classmethod
    def Pentax_XW_10mm(cls):
        return cls.from_database(cls._DATABASE["Pentax_XW_10mm"])

    @classmethod
    def Pentax_XW_14mm(cls):
        return cls.from_database(cls._DATABASE["Pentax_XW_14mm"])

    @classmethod
    def Pentax_XW_20mm(cls):
        return cls.from_database(cls._DATABASE["Pentax_XW_20mm"])

    @classmethod
    def Pentax_XW_30mm(cls):
        return cls.from_database(cls._DATABASE["Pentax_XW_30mm"])

    @classmethod
    def Pentax_XW_40mm(cls):
        return cls.from_database(cls._DATABASE["Pentax_XW_40mm"])

    @classmethod
    def Nikon_NAV_SW_10mm(cls):
        return cls.from_database(cls._DATABASE["Nikon_NAV_SW_10mm"])

    @classmethod
    def Nikon_NAV_SW_12_5mm(cls):
        return cls.from_database(cls._DATABASE["Nikon_NAV_SW_12_5mm"])

    @classmethod
    def Nikon_NAV_SW_17mm(cls):
        return cls.from_database(cls._DATABASE["Nikon_NAV_SW_17mm"])

    @classmethod
    def Nikon_NAV_HW_12_5mm(cls):
        return cls.from_database(cls._DATABASE["Nikon_NAV_HW_12_5mm"])

    @classmethod
    def Vixen_SSW_3_5mm(cls):
        return cls.from_database(cls._DATABASE["Vixen_SSW_3_5mm"])

    @classmethod
    def Vixen_SSW_5mm(cls):
        return cls.from_database(cls._DATABASE["Vixen_SSW_5mm"])

    @classmethod
    def Vixen_SSW_7mm(cls):
        return cls.from_database(cls._DATABASE["Vixen_SSW_7mm"])

    @classmethod
    def Vixen_SSW_10mm(cls):
        return cls.from_database(cls._DATABASE["Vixen_SSW_10mm"])

    @classmethod
    def Vixen_SSW_14mm(cls):
        return cls.from_database(cls._DATABASE["Vixen_SSW_14mm"])

    @classmethod
    def Vixen_SLV_2_5mm(cls):
        return cls.from_database(cls._DATABASE["Vixen_SLV_2_5mm"])

    @classmethod
    def Vixen_SLV_4mm(cls):
        return cls.from_database(cls._DATABASE["Vixen_SLV_4mm"])

    @classmethod
    def Vixen_SLV_6mm(cls):
        return cls.from_database(cls._DATABASE["Vixen_SLV_6mm"])

    @classmethod
    def Vixen_SLV_9mm(cls):
        return cls.from_database(cls._DATABASE["Vixen_SLV_9mm"])

    @classmethod
    def Vixen_SLV_10mm(cls):
        return cls.from_database(cls._DATABASE["Vixen_SLV_10mm"])

    @classmethod
    def Vixen_SLV_12mm(cls):
        return cls.from_database(cls._DATABASE["Vixen_SLV_12mm"])

    @classmethod
    def Vixen_SLV_15mm(cls):
        return cls.from_database(cls._DATABASE["Vixen_SLV_15mm"])

    @classmethod
    def Vixen_SLV_20mm(cls):
        return cls.from_database(cls._DATABASE["Vixen_SLV_20mm"])

    @classmethod
    def Vixen_SLV_25mm(cls):
        return cls.from_database(cls._DATABASE["Vixen_SLV_25mm"])

    @classmethod
    def Vixen_NLV_4mm(cls):
        return cls.from_database(cls._DATABASE["Vixen_NLV_4mm"])

    @classmethod
    def Vixen_NLV_5mm(cls):
        return cls.from_database(cls._DATABASE["Vixen_NLV_5mm"])

    @classmethod
    def Vixen_NLV_6mm(cls):
        return cls.from_database(cls._DATABASE["Vixen_NLV_6mm"])

    @classmethod
    def Vixen_NLV_8mm(cls):
        return cls.from_database(cls._DATABASE["Vixen_NLV_8mm"])

    @classmethod
    def Vixen_NLV_10mm(cls):
        return cls.from_database(cls._DATABASE["Vixen_NLV_10mm"])

    @classmethod
    def Vixen_NLV_12mm(cls):
        return cls.from_database(cls._DATABASE["Vixen_NLV_12mm"])

    @classmethod
    def Vixen_NLV_15mm(cls):
        return cls.from_database(cls._DATABASE["Vixen_NLV_15mm"])

    @classmethod
    def Vixen_NLV_20mm(cls):
        return cls.from_database(cls._DATABASE["Vixen_NLV_20mm"])

    @classmethod
    def Vixen_NLV_25mm(cls):
        return cls.from_database(cls._DATABASE["Vixen_NLV_25mm"])

    @classmethod
    def Meade_Series_5000_HD_60_5_5mm(cls):
        return cls.from_database(cls._DATABASE["Meade_Series_5000_HD_60_5_5mm"])

    @classmethod
    def Meade_Series_5000_HD_60_8_8mm(cls):
        return cls.from_database(cls._DATABASE["Meade_Series_5000_HD_60_8_8mm"])

    @classmethod
    def Meade_Series_5000_HD_60_14mm(cls):
        return cls.from_database(cls._DATABASE["Meade_Series_5000_HD_60_14mm"])

    @classmethod
    def Meade_Series_5000_HD_60_18mm(cls):
        return cls.from_database(cls._DATABASE["Meade_Series_5000_HD_60_18mm"])

    @classmethod
    def Meade_Series_5000_HD_60_24mm(cls):
        return cls.from_database(cls._DATABASE["Meade_Series_5000_HD_60_24mm"])

    @classmethod
    def Meade_Series_5000_HD_60_32mm(cls):
        return cls.from_database(cls._DATABASE["Meade_Series_5000_HD_60_32mm"])

    @classmethod
    def Meade_Series_5000_HD_60_40mm(cls):
        return cls.from_database(cls._DATABASE["Meade_Series_5000_HD_60_40mm"])

    @classmethod
    def Meade_Series_5000_UWA_5_5mm(cls):
        return cls.from_database(cls._DATABASE["Meade_Series_5000_UWA_5_5mm"])

    @classmethod
    def Meade_Series_5000_UWA_8_8mm(cls):
        return cls.from_database(cls._DATABASE["Meade_Series_5000_UWA_8_8mm"])

    @classmethod
    def Meade_Series_5000_UWA_14mm(cls):
        return cls.from_database(cls._DATABASE["Meade_Series_5000_UWA_14mm"])

    @classmethod
    def Meade_Series_5000_UWA_18mm(cls):
        return cls.from_database(cls._DATABASE["Meade_Series_5000_UWA_18mm"])

    @classmethod
    def Meade_Series_5000_UWA_24mm(cls):
        return cls.from_database(cls._DATABASE["Meade_Series_5000_UWA_24mm"])

    @classmethod
    def Meade_Series_4000_Plossl_6_4mm(cls):
        return cls.from_database(cls._DATABASE["Meade_Series_4000_Plossl_6_4mm"])

    @classmethod
    def Meade_Series_4000_Plossl_9_7mm(cls):
        return cls.from_database(cls._DATABASE["Meade_Series_4000_Plossl_9_7mm"])

    @classmethod
    def Meade_Series_4000_Plossl_12_4mm(cls):
        return cls.from_database(cls._DATABASE["Meade_Series_4000_Plossl_12_4mm"])

    @classmethod
    def Meade_Series_4000_Plossl_15mm(cls):
        return cls.from_database(cls._DATABASE["Meade_Series_4000_Plossl_15mm"])

    @classmethod
    def Meade_Series_4000_Plossl_20mm(cls):
        return cls.from_database(cls._DATABASE["Meade_Series_4000_Plossl_20mm"])

    @classmethod
    def Meade_Series_4000_Plossl_26mm(cls):
        return cls.from_database(cls._DATABASE["Meade_Series_4000_Plossl_26mm"])

    @classmethod
    def Meade_Series_4000_Plossl_32mm(cls):
        return cls.from_database(cls._DATABASE["Meade_Series_4000_Plossl_32mm"])

    @classmethod
    def Meade_Series_4000_Plossl_40mm(cls):
        return cls.from_database(cls._DATABASE["Meade_Series_4000_Plossl_40mm"])

    @classmethod
    def William_Optics_SWAN_3_5mm(cls):
        return cls.from_database(cls._DATABASE["William_Optics_SWAN_3_5mm"])

    @classmethod
    def William_Optics_SWAN_7mm(cls):
        return cls.from_database(cls._DATABASE["William_Optics_SWAN_7mm"])

    @classmethod
    def William_Optics_SWAN_11mm(cls):
        return cls.from_database(cls._DATABASE["William_Optics_SWAN_11mm"])

    @classmethod
    def William_Optics_SWAN_16mm(cls):
        return cls.from_database(cls._DATABASE["William_Optics_SWAN_16mm"])

    @classmethod
    def William_Optics_SWAN_20mm(cls):
        return cls.from_database(cls._DATABASE["William_Optics_SWAN_20mm"])

    @classmethod
    def William_Optics_SWAN_33mm(cls):
        return cls.from_database(cls._DATABASE["William_Optics_SWAN_33mm"])

    @classmethod
    def William_Optics_UWAN_3mm(cls):
        return cls.from_database(cls._DATABASE["William_Optics_UWAN_3mm"])

    @classmethod
    def William_Optics_UWAN_6mm(cls):
        return cls.from_database(cls._DATABASE["William_Optics_UWAN_6mm"])

    @classmethod
    def William_Optics_UWAN_10mm(cls):
        return cls.from_database(cls._DATABASE["William_Optics_UWAN_10mm"])

    @classmethod
    def William_Optics_UWAN_15mm(cls):
        return cls.from_database(cls._DATABASE["William_Optics_UWAN_15mm"])

    @classmethod
    def William_Optics_UWAN_20mm(cls):
        return cls.from_database(cls._DATABASE["William_Optics_UWAN_20mm"])

    @classmethod
    def William_Optics_SPL_3mm(cls):
        return cls.from_database(cls._DATABASE["William_Optics_SPL_3mm"])

    @classmethod
    def William_Optics_SPL_6mm(cls):
        return cls.from_database(cls._DATABASE["William_Optics_SPL_6mm"])

    @classmethod
    def William_Optics_SPL_10mm(cls):
        return cls.from_database(cls._DATABASE["William_Optics_SPL_10mm"])

    @classmethod
    def William_Optics_SPL_15mm(cls):
        return cls.from_database(cls._DATABASE["William_Optics_SPL_15mm"])

    @classmethod
    def William_Optics_SPL_20mm(cls):
        return cls.from_database(cls._DATABASE["William_Optics_SPL_20mm"])

    @classmethod
    def APM_XWA_3_5mm_100(cls):
        return cls.from_database(cls._DATABASE["APM_XWA_3_5mm_100"])

    @classmethod
    def APM_XWA_7mm_100(cls):
        return cls.from_database(cls._DATABASE["APM_XWA_7mm_100"])

    @classmethod
    def APM_XWA_9mm_100(cls):
        return cls.from_database(cls._DATABASE["APM_XWA_9mm_100"])

    @classmethod
    def APM_XWA_13mm_100(cls):
        return cls.from_database(cls._DATABASE["APM_XWA_13mm_100"])

    @classmethod
    def APM_XWA_20mm_100(cls):
        return cls.from_database(cls._DATABASE["APM_XWA_20mm_100"])

    @classmethod
    def APM_HDC_4mm(cls):
        return cls.from_database(cls._DATABASE["APM_HDC_4mm"])

    @classmethod
    def APM_HDC_6mm(cls):
        return cls.from_database(cls._DATABASE["APM_HDC_6mm"])

    @classmethod
    def APM_HDC_9mm(cls):
        return cls.from_database(cls._DATABASE["APM_HDC_9mm"])

    @classmethod
    def APM_HDC_12mm(cls):
        return cls.from_database(cls._DATABASE["APM_HDC_12mm"])

    @classmethod
    def APM_HDC_18mm(cls):
        return cls.from_database(cls._DATABASE["APM_HDC_18mm"])

    @classmethod
    def APM_HDC_25mm(cls):
        return cls.from_database(cls._DATABASE["APM_HDC_25mm"])

    @classmethod
    def Sky_Watcher_Aero_ED_2mm(cls):
        return cls.from_database(cls._DATABASE["Sky_Watcher_Aero_ED_2mm"])

    @classmethod
    def Sky_Watcher_Aero_ED_3_5mm(cls):
        return cls.from_database(cls._DATABASE["Sky_Watcher_Aero_ED_3_5mm"])

    @classmethod
    def Sky_Watcher_Aero_ED_5mm(cls):
        return cls.from_database(cls._DATABASE["Sky_Watcher_Aero_ED_5mm"])

    @classmethod
    def Sky_Watcher_Aero_ED_7mm(cls):
        return cls.from_database(cls._DATABASE["Sky_Watcher_Aero_ED_7mm"])

    @classmethod
    def Sky_Watcher_Aero_ED_9mm(cls):
        return cls.from_database(cls._DATABASE["Sky_Watcher_Aero_ED_9mm"])

    @classmethod
    def Sky_Watcher_Aero_ED_11mm(cls):
        return cls.from_database(cls._DATABASE["Sky_Watcher_Aero_ED_11mm"])

    @classmethod
    def Sky_Watcher_Aero_ED_15mm(cls):
        return cls.from_database(cls._DATABASE["Sky_Watcher_Aero_ED_15mm"])

    @classmethod
    def Sky_Watcher_Aero_ED_20mm(cls):
        return cls.from_database(cls._DATABASE["Sky_Watcher_Aero_ED_20mm"])

    @classmethod
    def Sky_Watcher_Nirvana_UWA_15mm(cls):
        return cls.from_database(cls._DATABASE["Sky_Watcher_Nirvana_UWA_15mm"])

    @classmethod
    def Sky_Watcher_Nirvana_UWA_20mm(cls):
        return cls.from_database(cls._DATABASE["Sky_Watcher_Nirvana_UWA_20mm"])

    @classmethod
    def Sky_Watcher_Nirvana_UWA_23mm(cls):
        return cls.from_database(cls._DATABASE["Sky_Watcher_Nirvana_UWA_23mm"])

    @classmethod
    def Sky_Watcher_Nirvana_UWA_31mm(cls):
        return cls.from_database(cls._DATABASE["Sky_Watcher_Nirvana_UWA_31mm"])

    @classmethod
    def Sky_Watcher_Super_Plossl_6mm(cls):
        return cls.from_database(cls._DATABASE["Sky_Watcher_Super_Plossl_6mm"])

    @classmethod
    def Sky_Watcher_Super_Plossl_10mm(cls):
        return cls.from_database(cls._DATABASE["Sky_Watcher_Super_Plossl_10mm"])

    @classmethod
    def Sky_Watcher_Super_Plossl_15mm(cls):
        return cls.from_database(cls._DATABASE["Sky_Watcher_Super_Plossl_15mm"])

    @classmethod
    def Sky_Watcher_Super_Plossl_20mm(cls):
        return cls.from_database(cls._DATABASE["Sky_Watcher_Super_Plossl_20mm"])

    @classmethod
    def Sky_Watcher_Super_Plossl_25mm(cls):
        return cls.from_database(cls._DATABASE["Sky_Watcher_Super_Plossl_25mm"])

    @classmethod
    def Sky_Watcher_Super_Plossl_32mm(cls):
        return cls.from_database(cls._DATABASE["Sky_Watcher_Super_Plossl_32mm"])

    @classmethod
    def SVBony_SV131_4mm_68(cls):
        return cls.from_database(cls._DATABASE["SVBony_SV131_4mm_68"])

    @classmethod
    def SVBony_SV131_6mm_68(cls):
        return cls.from_database(cls._DATABASE["SVBony_SV131_6mm_68"])

    @classmethod
    def SVBony_SV131_9mm_68(cls):
        return cls.from_database(cls._DATABASE["SVBony_SV131_9mm_68"])

    @classmethod
    def SVBony_SV131_12mm_68(cls):
        return cls.from_database(cls._DATABASE["SVBony_SV131_12mm_68"])

    @classmethod
    def SVBony_SV131_15mm_68(cls):
        return cls.from_database(cls._DATABASE["SVBony_SV131_15mm_68"])

    @classmethod
    def SVBony_SV131_20mm_68(cls):
        return cls.from_database(cls._DATABASE["SVBony_SV131_20mm_68"])

    @classmethod
    def SVBony_SV131_25mm_68(cls):
        return cls.from_database(cls._DATABASE["SVBony_SV131_25mm_68"])

    @classmethod
    def SVBony_SV190_3_2mm_82(cls):
        return cls.from_database(cls._DATABASE["SVBony_SV190_3_2mm_82"])

    @classmethod
    def SVBony_SV190_5mm_82(cls):
        return cls.from_database(cls._DATABASE["SVBony_SV190_5mm_82"])

    @classmethod
    def SVBony_SV190_7mm_82(cls):
        return cls.from_database(cls._DATABASE["SVBony_SV190_7mm_82"])

    @classmethod
    def SVBony_SV190_9mm_82(cls):
        return cls.from_database(cls._DATABASE["SVBony_SV190_9mm_82"])

    @classmethod
    def SVBony_SV190_11mm_82(cls):
        return cls.from_database(cls._DATABASE["SVBony_SV190_11mm_82"])

    @classmethod
    def SVBony_SV190_15mm_82(cls):
        return cls.from_database(cls._DATABASE["SVBony_SV190_15mm_82"])

    @classmethod
    def SVBony_SV190_20mm_82(cls):
        return cls.from_database(cls._DATABASE["SVBony_SV190_20mm_82"])

    @classmethod
    def Orion_Stratus_5mm(cls):
        return cls.from_database(cls._DATABASE["Orion_Stratus_5mm"])

    @classmethod
    def Orion_Stratus_7mm(cls):
        return cls.from_database(cls._DATABASE["Orion_Stratus_7mm"])

    @classmethod
    def Orion_Stratus_10mm(cls):
        return cls.from_database(cls._DATABASE["Orion_Stratus_10mm"])

    @classmethod
    def Orion_Stratus_12_5mm(cls):
        return cls.from_database(cls._DATABASE["Orion_Stratus_12_5mm"])

    @classmethod
    def Orion_Stratus_15mm(cls):
        return cls.from_database(cls._DATABASE["Orion_Stratus_15mm"])

    @classmethod
    def Orion_Stratus_18mm(cls):
        return cls.from_database(cls._DATABASE["Orion_Stratus_18mm"])

    @classmethod
    def Orion_Stratus_20mm(cls):
        return cls.from_database(cls._DATABASE["Orion_Stratus_20mm"])

    @classmethod
    def Orion_Stratus_25mm(cls):
        return cls.from_database(cls._DATABASE["Orion_Stratus_25mm"])

    @classmethod
    def Orion_Edge_On_Planetary_6mm(cls):
        return cls.from_database(cls._DATABASE["Orion_Edge_On_Planetary_6mm"])

    @classmethod
    def Orion_Edge_On_Planetary_9mm(cls):
        return cls.from_database(cls._DATABASE["Orion_Edge_On_Planetary_9mm"])

    @classmethod
    def Orion_Edge_On_Planetary_12mm(cls):
        return cls.from_database(cls._DATABASE["Orion_Edge_On_Planetary_12mm"])

    @classmethod
    def Orion_Edge_On_Planetary_15mm(cls):
        return cls.from_database(cls._DATABASE["Orion_Edge_On_Planetary_15mm"])

    @classmethod
    def Orion_Edge_On_Planetary_20mm(cls):
        return cls.from_database(cls._DATABASE["Orion_Edge_On_Planetary_20mm"])

    @classmethod
    def Orion_Edge_On_Planetary_25mm(cls):
        return cls.from_database(cls._DATABASE["Orion_Edge_On_Planetary_25mm"])

    @classmethod
    def Omegon_Panorama_II_5mm(cls):
        return cls.from_database(cls._DATABASE["Omegon_Panorama_II_5mm"])

    @classmethod
    def Omegon_Panorama_II_7mm(cls):
        return cls.from_database(cls._DATABASE["Omegon_Panorama_II_7mm"])

    @classmethod
    def Omegon_Panorama_II_9mm(cls):
        return cls.from_database(cls._DATABASE["Omegon_Panorama_II_9mm"])

    @classmethod
    def Omegon_Panorama_II_12mm(cls):
        return cls.from_database(cls._DATABASE["Omegon_Panorama_II_12mm"])

    @classmethod
    def Omegon_Panorama_II_15mm(cls):
        return cls.from_database(cls._DATABASE["Omegon_Panorama_II_15mm"])

    @classmethod
    def Omegon_Panorama_II_20mm(cls):
        return cls.from_database(cls._DATABASE["Omegon_Panorama_II_20mm"])

    @classmethod
    def Omegon_Panorama_II_25mm(cls):
        return cls.from_database(cls._DATABASE["Omegon_Panorama_II_25mm"])

    @classmethod
    def Omegon_Panorama_II_30mm(cls):
        return cls.from_database(cls._DATABASE["Omegon_Panorama_II_30mm"])

    @classmethod
    def Omegon_Cronus_WA_4mm(cls):
        return cls.from_database(cls._DATABASE["Omegon_Cronus_WA_4mm"])

    @classmethod
    def Omegon_Cronus_WA_6mm(cls):
        return cls.from_database(cls._DATABASE["Omegon_Cronus_WA_6mm"])

    @classmethod
    def Omegon_Cronus_WA_9mm(cls):
        return cls.from_database(cls._DATABASE["Omegon_Cronus_WA_9mm"])

    @classmethod
    def Omegon_Cronus_WA_12_5mm(cls):
        return cls.from_database(cls._DATABASE["Omegon_Cronus_WA_12_5mm"])

    @classmethod
    def Omegon_Cronus_WA_17mm(cls):
        return cls.from_database(cls._DATABASE["Omegon_Cronus_WA_17mm"])

    @classmethod
    def Omegon_Cronus_WA_25mm(cls):
        return cls.from_database(cls._DATABASE["Omegon_Cronus_WA_25mm"])

    @classmethod
    def TS_Optics_Planetary_HR_2_5mm(cls):
        return cls.from_database(cls._DATABASE["TS_Optics_Planetary_HR_2_5mm"])

    @classmethod
    def TS_Optics_Planetary_HR_3_2mm(cls):
        return cls.from_database(cls._DATABASE["TS_Optics_Planetary_HR_3_2mm"])

    @classmethod
    def TS_Optics_Planetary_HR_4mm(cls):
        return cls.from_database(cls._DATABASE["TS_Optics_Planetary_HR_4mm"])

    @classmethod
    def TS_Optics_Planetary_HR_5mm(cls):
        return cls.from_database(cls._DATABASE["TS_Optics_Planetary_HR_5mm"])

    @classmethod
    def TS_Optics_Planetary_HR_7mm(cls):
        return cls.from_database(cls._DATABASE["TS_Optics_Planetary_HR_7mm"])

    @classmethod
    def TS_Optics_Planetary_HR_9mm(cls):
        return cls.from_database(cls._DATABASE["TS_Optics_Planetary_HR_9mm"])

    @classmethod
    def TS_Optics_UWA_82_5_5mm(cls):
        return cls.from_database(cls._DATABASE["TS_Optics_UWA_82_5_5mm"])

    @classmethod
    def TS_Optics_UWA_82_7mm(cls):
        return cls.from_database(cls._DATABASE["TS_Optics_UWA_82_7mm"])

    @classmethod
    def TS_Optics_UWA_82_10mm(cls):
        return cls.from_database(cls._DATABASE["TS_Optics_UWA_82_10mm"])

    @classmethod
    def TS_Optics_UWA_82_15mm(cls):
        return cls.from_database(cls._DATABASE["TS_Optics_UWA_82_15mm"])

    @classmethod
    def TS_Optics_UWA_82_20mm(cls):
        return cls.from_database(cls._DATABASE["TS_Optics_UWA_82_20mm"])

    @classmethod
    def TS_Optics_UWA_82_30mm(cls):
        return cls.from_database(cls._DATABASE["TS_Optics_UWA_82_30mm"])

    @classmethod
    def Bresser_LER_5mm_70(cls):
        return cls.from_database(cls._DATABASE["Bresser_LER_5mm_70"])

    @classmethod
    def Bresser_LER_9mm_70(cls):
        return cls.from_database(cls._DATABASE["Bresser_LER_9mm_70"])

    @classmethod
    def Bresser_LER_12mm_70(cls):
        return cls.from_database(cls._DATABASE["Bresser_LER_12mm_70"])

    @classmethod
    def Bresser_LER_15mm_70(cls):
        return cls.from_database(cls._DATABASE["Bresser_LER_15mm_70"])

    @classmethod
    def Bresser_LER_20mm_70(cls):
        return cls.from_database(cls._DATABASE["Bresser_LER_20mm_70"])

    @classmethod
    def Bresser_LER_25mm_70(cls):
        return cls.from_database(cls._DATABASE["Bresser_LER_25mm_70"])

    @classmethod
    def Bresser_LER_32mm_70(cls):
        return cls.from_database(cls._DATABASE["Bresser_LER_32mm_70"])

    @classmethod
    def Lacerta_LER_5mm_72(cls):
        return cls.from_database(cls._DATABASE["Lacerta_LER_5mm_72"])

    @classmethod
    def Lacerta_LER_7mm_72(cls):
        return cls.from_database(cls._DATABASE["Lacerta_LER_7mm_72"])

    @classmethod
    def Lacerta_LER_10mm_72(cls):
        return cls.from_database(cls._DATABASE["Lacerta_LER_10mm_72"])

    @classmethod
    def Lacerta_LER_15mm_72(cls):
        return cls.from_database(cls._DATABASE["Lacerta_LER_15mm_72"])

    @classmethod
    def Lacerta_LER_20mm_72(cls):
        return cls.from_database(cls._DATABASE["Lacerta_LER_20mm_72"])

    @classmethod
    def Lacerta_LER_25mm_72(cls):
        return cls.from_database(cls._DATABASE["Lacerta_LER_25mm_72"])

    @classmethod
    def GSO_Plossl_6mm(cls):
        return cls.from_database(cls._DATABASE["GSO_Plossl_6mm"])

    @classmethod
    def GSO_Plossl_8mm(cls):
        return cls.from_database(cls._DATABASE["GSO_Plossl_8mm"])

    @classmethod
    def GSO_Plossl_10mm(cls):
        return cls.from_database(cls._DATABASE["GSO_Plossl_10mm"])

    @classmethod
    def GSO_Plossl_12_5mm(cls):
        return cls.from_database(cls._DATABASE["GSO_Plossl_12_5mm"])

    @classmethod
    def GSO_Plossl_15mm(cls):
        return cls.from_database(cls._DATABASE["GSO_Plossl_15mm"])

    @classmethod
    def GSO_Plossl_20mm(cls):
        return cls.from_database(cls._DATABASE["GSO_Plossl_20mm"])

    @classmethod
    def GSO_Plossl_25mm(cls):
        return cls.from_database(cls._DATABASE["GSO_Plossl_25mm"])

    @classmethod
    def GSO_Plossl_32mm(cls):
        return cls.from_database(cls._DATABASE["GSO_Plossl_32mm"])

    @classmethod
    def GSO_Plossl_40mm(cls):
        return cls.from_database(cls._DATABASE["GSO_Plossl_40mm"])

    @classmethod
    def GSO_SuperView_7mm(cls):
        return cls.from_database(cls._DATABASE["GSO_SuperView_7mm"])

    @classmethod
    def GSO_SuperView_9mm(cls):
        return cls.from_database(cls._DATABASE["GSO_SuperView_9mm"])

    @classmethod
    def GSO_SuperView_12mm(cls):
        return cls.from_database(cls._DATABASE["GSO_SuperView_12mm"])

    @classmethod
    def GSO_SuperView_15mm(cls):
        return cls.from_database(cls._DATABASE["GSO_SuperView_15mm"])

    @classmethod
    def GSO_SuperView_20mm(cls):
        return cls.from_database(cls._DATABASE["GSO_SuperView_20mm"])

    @classmethod
    def GSO_SuperView_30mm(cls):
        return cls.from_database(cls._DATABASE["GSO_SuperView_30mm"])

    @classmethod
    def Masuyama_5mm_85(cls):
        return cls.from_database(cls._DATABASE["Masuyama_5mm_85"])

    @classmethod
    def Masuyama_8mm_85(cls):
        return cls.from_database(cls._DATABASE["Masuyama_8mm_85"])

    @classmethod
    def Masuyama_10mm_85(cls):
        return cls.from_database(cls._DATABASE["Masuyama_10mm_85"])

    @classmethod
    def Masuyama_15mm_85(cls):
        return cls.from_database(cls._DATABASE["Masuyama_15mm_85"])

    @classmethod
    def Masuyama_20mm_85(cls):
        return cls.from_database(cls._DATABASE["Masuyama_20mm_85"])

    @classmethod
    def Masuyama_25mm_85(cls):
        return cls.from_database(cls._DATABASE["Masuyama_25mm_85"])

    @classmethod
    def Masuyama_32mm_85(cls):
        return cls.from_database(cls._DATABASE["Masuyama_32mm_85"])

    @classmethod
    def Agena_Starguider_5mm_60(cls):
        return cls.from_database(cls._DATABASE["Agena_Starguider_5mm_60"])

    @classmethod
    def Agena_Starguider_7mm_60(cls):
        return cls.from_database(cls._DATABASE["Agena_Starguider_7mm_60"])

    @classmethod
    def Agena_Starguider_9mm_60(cls):
        return cls.from_database(cls._DATABASE["Agena_Starguider_9mm_60"])

    @classmethod
    def Agena_Starguider_12mm_60(cls):
        return cls.from_database(cls._DATABASE["Agena_Starguider_12mm_60"])

    @classmethod
    def Agena_Starguider_15mm_60(cls):
        return cls.from_database(cls._DATABASE["Agena_Starguider_15mm_60"])

    @classmethod
    def Agena_Starguider_20mm_60(cls):
        return cls.from_database(cls._DATABASE["Agena_Starguider_20mm_60"])

    @classmethod
    def Agena_Starguider_25mm_60(cls):
        return cls.from_database(cls._DATABASE["Agena_Starguider_25mm_60"])

    @classmethod
    def Stellarvue_Optimus_3_5mm_82(cls):
        return cls.from_database(cls._DATABASE["Stellarvue_Optimus_3_5mm_82"])

    @classmethod
    def Stellarvue_Optimus_5mm_82(cls):
        return cls.from_database(cls._DATABASE["Stellarvue_Optimus_5mm_82"])

    @classmethod
    def Stellarvue_Optimus_7mm_82(cls):
        return cls.from_database(cls._DATABASE["Stellarvue_Optimus_7mm_82"])

    @classmethod
    def Stellarvue_Optimus_9mm_82(cls):
        return cls.from_database(cls._DATABASE["Stellarvue_Optimus_9mm_82"])

    @classmethod
    def Stellarvue_Optimus_13mm_82(cls):
        return cls.from_database(cls._DATABASE["Stellarvue_Optimus_13mm_82"])

    @classmethod
    def Stellarvue_Optimus_20mm_82(cls):
        return cls.from_database(cls._DATABASE["Stellarvue_Optimus_20mm_82"])

    @classmethod
    def Celestron_Ultima_Duo_5mm(cls):
        return cls.from_database(cls._DATABASE["Celestron_Ultima_Duo_5mm"])

    @classmethod
    def Celestron_Ultima_Duo_8mm(cls):
        return cls.from_database(cls._DATABASE["Celestron_Ultima_Duo_8mm"])

    @classmethod
    def Celestron_Ultima_Duo_10mm(cls):
        return cls.from_database(cls._DATABASE["Celestron_Ultima_Duo_10mm"])

    @classmethod
    def Celestron_Ultima_Duo_13mm(cls):
        return cls.from_database(cls._DATABASE["Celestron_Ultima_Duo_13mm"])

    @classmethod
    def Celestron_Ultima_Duo_15mm(cls):
        return cls.from_database(cls._DATABASE["Celestron_Ultima_Duo_15mm"])

    @classmethod
    def Celestron_Ultima_Duo_17mm(cls):
        return cls.from_database(cls._DATABASE["Celestron_Ultima_Duo_17mm"])

    @classmethod
    def Celestron_Ultima_Duo_21mm(cls):
        return cls.from_database(cls._DATABASE["Celestron_Ultima_Duo_21mm"])

    @classmethod
    def Celestron_Ultima_Duo_25mm(cls):
        return cls.from_database(cls._DATABASE["Celestron_Ultima_Duo_25mm"])

    @classmethod
    def Meade_Series_6000_MWA_4_7mm(cls):
        return cls.from_database(cls._DATABASE["Meade_Series_6000_MWA_4_7mm"])

    @classmethod
    def Meade_Series_6000_MWA_6_7mm(cls):
        return cls.from_database(cls._DATABASE["Meade_Series_6000_MWA_6_7mm"])

    @classmethod
    def Meade_Series_6000_MWA_9_5mm(cls):
        return cls.from_database(cls._DATABASE["Meade_Series_6000_MWA_9_5mm"])

    @classmethod
    def Meade_Series_6000_MWA_14mm(cls):
        return cls.from_database(cls._DATABASE["Meade_Series_6000_MWA_14mm"])

    @classmethod
    def Meade_Series_6000_MWA_18mm(cls):
        return cls.from_database(cls._DATABASE["Meade_Series_6000_MWA_18mm"])

    @classmethod
    def Meade_Series_6000_MWA_24_5mm(cls):
        return cls.from_database(cls._DATABASE["Meade_Series_6000_MWA_24_5mm"])

    @classmethod
    def Takahashi_Abbe_Ortho_2_8mm(cls):
        return cls.from_database(cls._DATABASE["Takahashi_Abbe_Ortho_2_8mm"])

    @classmethod
    def Takahashi_Abbe_Ortho_5mm(cls):
        return cls.from_database(cls._DATABASE["Takahashi_Abbe_Ortho_5mm"])

    @classmethod
    def Takahashi_Abbe_Ortho_7_5mm(cls):
        return cls.from_database(cls._DATABASE["Takahashi_Abbe_Ortho_7_5mm"])

    @classmethod
    def Takahashi_Abbe_Ortho_10mm(cls):
        return cls.from_database(cls._DATABASE["Takahashi_Abbe_Ortho_10mm"])

    @classmethod
    def Takahashi_Abbe_Ortho_15mm(cls):
        return cls.from_database(cls._DATABASE["Takahashi_Abbe_Ortho_15mm"])

    @classmethod
    def Takahashi_Abbe_Ortho_20mm(cls):
        return cls.from_database(cls._DATABASE["Takahashi_Abbe_Ortho_20mm"])

    @classmethod
    def Takahashi_Abbe_Ortho_25mm(cls):
        return cls.from_database(cls._DATABASE["Takahashi_Abbe_Ortho_25mm"])

    @classmethod
    def Takahashi_TOE_12_5mm(cls):
        return cls.from_database(cls._DATABASE["Takahashi_TOE_12_5mm"])

    @classmethod
    def Takahashi_TOE_20mm(cls):
        return cls.from_database(cls._DATABASE["Takahashi_TOE_20mm"])

    @classmethod
    def Takahashi_TOE_25mm(cls):
        return cls.from_database(cls._DATABASE["Takahashi_TOE_25mm"])

    @classmethod
    def Astro_Physics_MaxView_10mm(cls):
        return cls.from_database(cls._DATABASE["Astro_Physics_MaxView_10mm"])

    @classmethod
    def Astro_Physics_MaxView_15mm(cls):
        return cls.from_database(cls._DATABASE["Astro_Physics_MaxView_15mm"])

    @classmethod
    def Astro_Physics_MaxView_20mm(cls):
        return cls.from_database(cls._DATABASE["Astro_Physics_MaxView_20mm"])

    @classmethod
    def Astro_Physics_MaxView_25mm(cls):
        return cls.from_database(cls._DATABASE["Astro_Physics_MaxView_25mm"])

    @classmethod
    def Lunt_H_alpha_7_5mm(cls):
        return cls.from_database(cls._DATABASE["Lunt_H_alpha_7_5mm"])

    @classmethod
    def Lunt_H_alpha_12mm(cls):
        return cls.from_database(cls._DATABASE["Lunt_H_alpha_12mm"])

    @classmethod
    def Lunt_H_alpha_16mm(cls):
        return cls.from_database(cls._DATABASE["Lunt_H_alpha_16mm"])

    @classmethod
    def Lunt_H_alpha_19mm(cls):
        return cls.from_database(cls._DATABASE["Lunt_H_alpha_19mm"])

    @classmethod
    def Lunt_H_alpha_27mm(cls):
        return cls.from_database(cls._DATABASE["Lunt_H_alpha_27mm"])

    @classmethod
    def Generic_Plossl_4mm(cls):
        return cls.from_database(cls._DATABASE["Generic_Plossl_4mm"])

    @classmethod
    def Generic_Plossl_6mm(cls):
        return cls.from_database(cls._DATABASE["Generic_Plossl_6mm"])

    @classmethod
    def Generic_Plossl_8mm(cls):
        return cls.from_database(cls._DATABASE["Generic_Plossl_8mm"])

    @classmethod
    def Generic_Plossl_10mm(cls):
        return cls.from_database(cls._DATABASE["Generic_Plossl_10mm"])

    @classmethod
    def Generic_Plossl_12_5mm(cls):
        return cls.from_database(cls._DATABASE["Generic_Plossl_12_5mm"])

    @classmethod
    def Generic_Plossl_15mm(cls):
        return cls.from_database(cls._DATABASE["Generic_Plossl_15mm"])

    @classmethod
    def Generic_Plossl_20mm(cls):
        return cls.from_database(cls._DATABASE["Generic_Plossl_20mm"])

    @classmethod
    def Generic_Plossl_25mm(cls):
        return cls.from_database(cls._DATABASE["Generic_Plossl_25mm"])

    @classmethod
    def Generic_Plossl_30mm(cls):
        return cls.from_database(cls._DATABASE["Generic_Plossl_30mm"])

    @classmethod
    def Generic_Plossl_40mm(cls):
        return cls.from_database(cls._DATABASE["Generic_Plossl_40mm"])

    @classmethod
    def Generic_Wide_Angle_66_6mm(cls):
        return cls.from_database(cls._DATABASE["Generic_Wide_Angle_66_6mm"])

    @classmethod
    def Generic_Wide_Angle_66_9mm(cls):
        return cls.from_database(cls._DATABASE["Generic_Wide_Angle_66_9mm"])

    @classmethod
    def Generic_Wide_Angle_66_12mm(cls):
        return cls.from_database(cls._DATABASE["Generic_Wide_Angle_66_12mm"])

    @classmethod
    def Generic_Wide_Angle_66_15mm(cls):
        return cls.from_database(cls._DATABASE["Generic_Wide_Angle_66_15mm"])

    @classmethod
    def Generic_Wide_Angle_66_20mm(cls):
        return cls.from_database(cls._DATABASE["Generic_Wide_Angle_66_20mm"])

    @classmethod
    def Generic_Wide_Angle_66_25mm(cls):
        return cls.from_database(cls._DATABASE["Generic_Wide_Angle_66_25mm"])

    @classmethod
    def Sky_Watcher_Plossl_6mm(cls):
        return cls.from_database(cls._DATABASE["Sky_Watcher_Plossl_6mm"])

    @classmethod
    def Sky_Watcher_Plossl_9mm(cls):
        return cls.from_database(cls._DATABASE["Sky_Watcher_Plossl_9mm"])

    @classmethod
    def Sky_Watcher_Plossl_12mm(cls):
        return cls.from_database(cls._DATABASE["Sky_Watcher_Plossl_12mm"])

    @classmethod
    def Sky_Watcher_Plossl_15mm(cls):
        return cls.from_database(cls._DATABASE["Sky_Watcher_Plossl_15mm"])

    @classmethod
    def Sky_Watcher_Plossl_20mm(cls):
        return cls.from_database(cls._DATABASE["Sky_Watcher_Plossl_20mm"])

    @classmethod
    def Sky_Watcher_Plossl_25mm(cls):
        return cls.from_database(cls._DATABASE["Sky_Watcher_Plossl_25mm"])

    @classmethod
    def Lacerta_ED_4mm_82(cls):
        return cls.from_database(cls._DATABASE["Lacerta_ED_4mm_82"])

    @classmethod
    def Lacerta_ED_6mm_82(cls):
        return cls.from_database(cls._DATABASE["Lacerta_ED_6mm_82"])

    @classmethod
    def Lacerta_ED_9mm_82(cls):
        return cls.from_database(cls._DATABASE["Lacerta_ED_9mm_82"])

    @classmethod
    def Lacerta_ED_12mm_82(cls):
        return cls.from_database(cls._DATABASE["Lacerta_ED_12mm_82"])

    @classmethod
    def Lacerta_ED_15mm_82(cls):
        return cls.from_database(cls._DATABASE["Lacerta_ED_15mm_82"])

    @classmethod
    def Lacerta_ED_20mm_82(cls):
        return cls.from_database(cls._DATABASE["Lacerta_ED_20mm_82"])

    @classmethod
    def TeleVue_DeLite_4mm(cls):
        return cls.from_database(cls._DATABASE["TeleVue_DeLite_4mm"])

    @classmethod
    def TeleVue_DeLite_5mm(cls):
        return cls.from_database(cls._DATABASE["TeleVue_DeLite_5mm"])

    @classmethod
    def TeleVue_DeLite_7mm(cls):
        return cls.from_database(cls._DATABASE["TeleVue_DeLite_7mm"])

    @classmethod
    def TeleVue_DeLite_9mm(cls):
        return cls.from_database(cls._DATABASE["TeleVue_DeLite_9mm"])

    @classmethod
    def TeleVue_DeLite_11mm(cls):
        return cls.from_database(cls._DATABASE["TeleVue_DeLite_11mm"])

    @classmethod
    def TeleVue_DeLite_13mm(cls):
        return cls.from_database(cls._DATABASE["TeleVue_DeLite_13mm"])

    @classmethod
    def TeleVue_DeLite_15mm(cls):
        return cls.from_database(cls._DATABASE["TeleVue_DeLite_15mm"])

    @classmethod
    def TeleVue_DeLite_18_2mm(cls):
        return cls.from_database(cls._DATABASE["TeleVue_DeLite_18_2mm"])

    @classmethod
    def Kasai_Wide_View_5mm_84(cls):
        return cls.from_database(cls._DATABASE["Kasai_Wide_View_5mm_84"])

    @classmethod
    def Kasai_Wide_View_7_5mm_84(cls):
        return cls.from_database(cls._DATABASE["Kasai_Wide_View_7_5mm_84"])

    @classmethod
    def Kasai_Wide_View_10mm_84(cls):
        return cls.from_database(cls._DATABASE["Kasai_Wide_View_10mm_84"])

    @classmethod
    def Kasai_Wide_View_14mm_84(cls):
        return cls.from_database(cls._DATABASE["Kasai_Wide_View_14mm_84"])

    @classmethod
    def Kasai_Wide_View_20mm_84(cls):
        return cls.from_database(cls._DATABASE["Kasai_Wide_View_20mm_84"])

    @classmethod
    def TMB_Planetary_II_2_5mm_58(cls):
        return cls.from_database(cls._DATABASE["TMB_Planetary_II_2_5mm_58"])

    @classmethod
    def TMB_Planetary_II_3_2mm_58(cls):
        return cls.from_database(cls._DATABASE["TMB_Planetary_II_3_2mm_58"])

    @classmethod
    def TMB_Planetary_II_4mm_58(cls):
        return cls.from_database(cls._DATABASE["TMB_Planetary_II_4mm_58"])

    @classmethod
    def TMB_Planetary_II_5mm_58(cls):
        return cls.from_database(cls._DATABASE["TMB_Planetary_II_5mm_58"])

    @classmethod
    def TMB_Planetary_II_6mm_58(cls):
        return cls.from_database(cls._DATABASE["TMB_Planetary_II_6mm_58"])

    @classmethod
    def TMB_Planetary_II_7mm_58(cls):
        return cls.from_database(cls._DATABASE["TMB_Planetary_II_7mm_58"])

    @classmethod
    def TMB_Planetary_II_8mm_58(cls):
        return cls.from_database(cls._DATABASE["TMB_Planetary_II_8mm_58"])

    @classmethod
    def TMB_Planetary_II_9mm_58(cls):
        return cls.from_database(cls._DATABASE["TMB_Planetary_II_9mm_58"])

    @classmethod
    def MaxVision_3_5mm_82(cls):
        return cls.from_database(cls._DATABASE["MaxVision_3_5mm_82"])

    @classmethod
    def MaxVision_5mm_82(cls):
        return cls.from_database(cls._DATABASE["MaxVision_5mm_82"])

    @classmethod
    def MaxVision_7mm_82(cls):
        return cls.from_database(cls._DATABASE["MaxVision_7mm_82"])

    @classmethod
    def MaxVision_10mm_82(cls):
        return cls.from_database(cls._DATABASE["MaxVision_10mm_82"])

    @classmethod
    def MaxVision_15mm_82(cls):
        return cls.from_database(cls._DATABASE["MaxVision_15mm_82"])

    @classmethod
    def MaxVision_20mm_82(cls):
        return cls.from_database(cls._DATABASE["MaxVision_20mm_82"])

    @classmethod
    def Celestron_Omni_Plossl_4mm(cls):
        return cls.from_database(cls._DATABASE["Celestron_Omni_Plossl_4mm"])

    @classmethod
    def Celestron_Omni_Plossl_6mm(cls):
        return cls.from_database(cls._DATABASE["Celestron_Omni_Plossl_6mm"])

    @classmethod
    def Celestron_Omni_Plossl_9mm(cls):
        return cls.from_database(cls._DATABASE["Celestron_Omni_Plossl_9mm"])

    @classmethod
    def Celestron_Omni_Plossl_12_5mm(cls):
        return cls.from_database(cls._DATABASE["Celestron_Omni_Plossl_12_5mm"])

    @classmethod
    def Celestron_Omni_Plossl_15mm(cls):
        return cls.from_database(cls._DATABASE["Celestron_Omni_Plossl_15mm"])

    @classmethod
    def Celestron_Omni_Plossl_20mm(cls):
        return cls.from_database(cls._DATABASE["Celestron_Omni_Plossl_20mm"])

    @classmethod
    def Celestron_Omni_Plossl_25mm(cls):
        return cls.from_database(cls._DATABASE["Celestron_Omni_Plossl_25mm"])

    @classmethod
    def Celestron_Omni_Plossl_32mm(cls):
        return cls.from_database(cls._DATABASE["Celestron_Omni_Plossl_32mm"])

    @classmethod
    def Celestron_Omni_Plossl_40mm(cls):
        return cls.from_database(cls._DATABASE["Celestron_Omni_Plossl_40mm"])

    @classmethod
    def Meade_Super_Plossl_6_4mm(cls):
        return cls.from_database(cls._DATABASE["Meade_Super_Plossl_6_4mm"])

    @classmethod
    def Meade_Super_Plossl_9_7mm(cls):
        return cls.from_database(cls._DATABASE["Meade_Super_Plossl_9_7mm"])

    @classmethod
    def Meade_Super_Plossl_12_4mm(cls):
        return cls.from_database(cls._DATABASE["Meade_Super_Plossl_12_4mm"])

    @classmethod
    def Meade_Super_Plossl_15mm(cls):
        return cls.from_database(cls._DATABASE["Meade_Super_Plossl_15mm"])

    @classmethod
    def Meade_Super_Plossl_20mm(cls):
        return cls.from_database(cls._DATABASE["Meade_Super_Plossl_20mm"])

    @classmethod
    def Meade_Super_Plossl_25mm(cls):
        return cls.from_database(cls._DATABASE["Meade_Super_Plossl_25mm"])

    @classmethod
    def Meade_Super_Plossl_32mm(cls):
        return cls.from_database(cls._DATABASE["Meade_Super_Plossl_32mm"])

    @classmethod
    def Meade_Super_Plossl_40mm(cls):
        return cls.from_database(cls._DATABASE["Meade_Super_Plossl_40mm"])

    @classmethod
    def Meade_Super_Plossl_56mm(cls):
        return cls.from_database(cls._DATABASE["Meade_Super_Plossl_56mm"])

    @classmethod
    def Orion_Sirius_Plossl_6_3mm(cls):
        return cls.from_database(cls._DATABASE["Orion_Sirius_Plossl_6_3mm"])

    @classmethod
    def Orion_Sirius_Plossl_7_5mm(cls):
        return cls.from_database(cls._DATABASE["Orion_Sirius_Plossl_7_5mm"])

    @classmethod
    def Orion_Sirius_Plossl_10mm(cls):
        return cls.from_database(cls._DATABASE["Orion_Sirius_Plossl_10mm"])

    @classmethod
    def Orion_Sirius_Plossl_12_5mm(cls):
        return cls.from_database(cls._DATABASE["Orion_Sirius_Plossl_12_5mm"])

    @classmethod
    def Orion_Sirius_Plossl_17mm(cls):
        return cls.from_database(cls._DATABASE["Orion_Sirius_Plossl_17mm"])

    @classmethod
    def Orion_Sirius_Plossl_20mm(cls):
        return cls.from_database(cls._DATABASE["Orion_Sirius_Plossl_20mm"])

    @classmethod
    def Orion_Sirius_Plossl_25mm(cls):
        return cls.from_database(cls._DATABASE["Orion_Sirius_Plossl_25mm"])

    @classmethod
    def Orion_Sirius_Plossl_32mm(cls):
        return cls.from_database(cls._DATABASE["Orion_Sirius_Plossl_32mm"])

    @classmethod
    def Orion_Sirius_Plossl_40mm(cls):
        return cls.from_database(cls._DATABASE["Orion_Sirius_Plossl_40mm"])

    @classmethod
    def Pentax_XF_6_5mm(cls):
        return cls.from_database(cls._DATABASE["Pentax_XF_6_5mm"])

    @classmethod
    def Pentax_XF_8_5mm(cls):
        return cls.from_database(cls._DATABASE["Pentax_XF_8_5mm"])

    @classmethod
    def Pentax_XF_12mm(cls):
        return cls.from_database(cls._DATABASE["Pentax_XF_12mm"])

    @classmethod
    def Brandon_8mm(cls):
        return cls.from_database(cls._DATABASE["Brandon_8mm"])

    @classmethod
    def Brandon_12mm(cls):
        return cls.from_database(cls._DATABASE["Brandon_12mm"])

    @classmethod
    def Brandon_16mm(cls):
        return cls.from_database(cls._DATABASE["Brandon_16mm"])

    @classmethod
    def Brandon_24mm(cls):
        return cls.from_database(cls._DATABASE["Brandon_24mm"])

    @classmethod
    def Brandon_32mm(cls):
        return cls.from_database(cls._DATABASE["Brandon_32mm"])

    @classmethod
    def Fujiyama_HD_Ortho_4mm(cls):
        return cls.from_database(cls._DATABASE["Fujiyama_HD_Ortho_4mm"])

    @classmethod
    def Fujiyama_HD_Ortho_5mm(cls):
        return cls.from_database(cls._DATABASE["Fujiyama_HD_Ortho_5mm"])

    @classmethod
    def Fujiyama_HD_Ortho_6mm(cls):
        return cls.from_database(cls._DATABASE["Fujiyama_HD_Ortho_6mm"])

    @classmethod
    def Fujiyama_HD_Ortho_7mm(cls):
        return cls.from_database(cls._DATABASE["Fujiyama_HD_Ortho_7mm"])

    @classmethod
    def Fujiyama_HD_Ortho_9mm(cls):
        return cls.from_database(cls._DATABASE["Fujiyama_HD_Ortho_9mm"])

    @classmethod
    def Fujiyama_HD_Ortho_12_5mm(cls):
        return cls.from_database(cls._DATABASE["Fujiyama_HD_Ortho_12_5mm"])

    @classmethod
    def Fujiyama_HD_Ortho_18mm(cls):
        return cls.from_database(cls._DATABASE["Fujiyama_HD_Ortho_18mm"])

    @classmethod
    def Fujiyama_HD_Ortho_25mm(cls):
        return cls.from_database(cls._DATABASE["Fujiyama_HD_Ortho_25mm"])

    @classmethod
    def William_Optics_Pleiades_3mm_55(cls):
        return cls.from_database(cls._DATABASE["William_Optics_Pleiades_3mm_55"])

    @classmethod
    def William_Optics_Pleiades_6mm_55(cls):
        return cls.from_database(cls._DATABASE["William_Optics_Pleiades_6mm_55"])

    @classmethod
    def William_Optics_Pleiades_10mm_55(cls):
        return cls.from_database(cls._DATABASE["William_Optics_Pleiades_10mm_55"])

    @classmethod
    def William_Optics_Pleiades_15mm_55(cls):
        return cls.from_database(cls._DATABASE["William_Optics_Pleiades_15mm_55"])

    @classmethod
    def William_Optics_Pleiades_20mm_55(cls):
        return cls.from_database(cls._DATABASE["William_Optics_Pleiades_20mm_55"])

    @classmethod
    def Saxon_Plossl_4mm(cls):
        return cls.from_database(cls._DATABASE["Saxon_Plossl_4mm"])

    @classmethod
    def Saxon_Plossl_6mm(cls):
        return cls.from_database(cls._DATABASE["Saxon_Plossl_6mm"])

    @classmethod
    def Saxon_Plossl_9mm(cls):
        return cls.from_database(cls._DATABASE["Saxon_Plossl_9mm"])

    @classmethod
    def Saxon_Plossl_12_5mm(cls):
        return cls.from_database(cls._DATABASE["Saxon_Plossl_12_5mm"])

    @classmethod
    def Saxon_Plossl_16mm(cls):
        return cls.from_database(cls._DATABASE["Saxon_Plossl_16mm"])

    @classmethod
    def Saxon_Plossl_20mm(cls):
        return cls.from_database(cls._DATABASE["Saxon_Plossl_20mm"])

    @classmethod
    def Saxon_Plossl_25mm(cls):
        return cls.from_database(cls._DATABASE["Saxon_Plossl_25mm"])

    @classmethod
    def National_Geographic_Plossl_4mm(cls):
        return cls.from_database(cls._DATABASE["National_Geographic_Plossl_4mm"])

    @classmethod
    def National_Geographic_Plossl_6mm(cls):
        return cls.from_database(cls._DATABASE["National_Geographic_Plossl_6mm"])

    @classmethod
    def National_Geographic_Plossl_9mm(cls):
        return cls.from_database(cls._DATABASE["National_Geographic_Plossl_9mm"])

    @classmethod
    def National_Geographic_Plossl_12_5mm(cls):
        return cls.from_database(cls._DATABASE["National_Geographic_Plossl_12_5mm"])

    @classmethod
    def National_Geographic_Plossl_20mm(cls):
        return cls.from_database(cls._DATABASE["National_Geographic_Plossl_20mm"])

    @classmethod
    def National_Geographic_Plossl_25mm(cls):
        return cls.from_database(cls._DATABASE["National_Geographic_Plossl_25mm"])

    @classmethod
    def National_Geographic_Plossl_32mm(cls):
        return cls.from_database(cls._DATABASE["National_Geographic_Plossl_32mm"])

    @classmethod
    def Omegon_Super_Plossl_4mm(cls):
        return cls.from_database(cls._DATABASE["Omegon_Super_Plossl_4mm"])

    @classmethod
    def Omegon_Super_Plossl_6mm(cls):
        return cls.from_database(cls._DATABASE["Omegon_Super_Plossl_6mm"])

    @classmethod
    def Omegon_Super_Plossl_9mm(cls):
        return cls.from_database(cls._DATABASE["Omegon_Super_Plossl_9mm"])

    @classmethod
    def Omegon_Super_Plossl_12mm(cls):
        return cls.from_database(cls._DATABASE["Omegon_Super_Plossl_12mm"])

    @classmethod
    def Omegon_Super_Plossl_16mm(cls):
        return cls.from_database(cls._DATABASE["Omegon_Super_Plossl_16mm"])

    @classmethod
    def Omegon_Super_Plossl_20mm(cls):
        return cls.from_database(cls._DATABASE["Omegon_Super_Plossl_20mm"])

    @classmethod
    def Omegon_Super_Plossl_25mm(cls):
        return cls.from_database(cls._DATABASE["Omegon_Super_Plossl_25mm"])

    @classmethod
    def Omegon_Super_Plossl_32mm(cls):
        return cls.from_database(cls._DATABASE["Omegon_Super_Plossl_32mm"])

    @classmethod
    def Vixen_LVW_3_5mm(cls):
        return cls.from_database(cls._DATABASE["Vixen_LVW_3_5mm"])

    @classmethod
    def Vixen_LVW_5mm(cls):
        return cls.from_database(cls._DATABASE["Vixen_LVW_5mm"])

    @classmethod
    def Vixen_LVW_8mm(cls):
        return cls.from_database(cls._DATABASE["Vixen_LVW_8mm"])

    @classmethod
    def Vixen_LVW_13mm(cls):
        return cls.from_database(cls._DATABASE["Vixen_LVW_13mm"])

    @classmethod
    def Vixen_LVW_17mm(cls):
        return cls.from_database(cls._DATABASE["Vixen_LVW_17mm"])

    @classmethod
    def Vixen_LVW_22mm(cls):
        return cls.from_database(cls._DATABASE["Vixen_LVW_22mm"])

    @classmethod
    def Vixen_LVW_30mm(cls):
        return cls.from_database(cls._DATABASE["Vixen_LVW_30mm"])

    @classmethod
    def Vixen_LVW_42mm(cls):
        return cls.from_database(cls._DATABASE["Vixen_LVW_42mm"])

    @classmethod
    def Bresser_Plossl_2_5mm(cls):
        return cls.from_database(cls._DATABASE["Bresser_Plossl_2_5mm"])

    @classmethod
    def Bresser_Plossl_4mm(cls):
        return cls.from_database(cls._DATABASE["Bresser_Plossl_4mm"])

    @classmethod
    def Bresser_Plossl_6mm(cls):
        return cls.from_database(cls._DATABASE["Bresser_Plossl_6mm"])

    @classmethod
    def Bresser_Plossl_8mm(cls):
        return cls.from_database(cls._DATABASE["Bresser_Plossl_8mm"])

    @classmethod
    def Bresser_Plossl_12_5mm(cls):
        return cls.from_database(cls._DATABASE["Bresser_Plossl_12_5mm"])

    @classmethod
    def Bresser_Plossl_20mm(cls):
        return cls.from_database(cls._DATABASE["Bresser_Plossl_20mm"])

    @classmethod
    def Bresser_Plossl_25mm(cls):
        return cls.from_database(cls._DATABASE["Bresser_Plossl_25mm"])

    @classmethod
    def Bresser_Plossl_32mm(cls):
        return cls.from_database(cls._DATABASE["Bresser_Plossl_32mm"])

    @classmethod
    def Lacerta_Plossl_6mm(cls):
        return cls.from_database(cls._DATABASE["Lacerta_Plossl_6mm"])

    @classmethod
    def Lacerta_Plossl_9mm(cls):
        return cls.from_database(cls._DATABASE["Lacerta_Plossl_9mm"])

    @classmethod
    def Lacerta_Plossl_12_5mm(cls):
        return cls.from_database(cls._DATABASE["Lacerta_Plossl_12_5mm"])

    @classmethod
    def Lacerta_Plossl_20mm(cls):
        return cls.from_database(cls._DATABASE["Lacerta_Plossl_20mm"])

    @classmethod
    def Lacerta_Plossl_25mm(cls):
        return cls.from_database(cls._DATABASE["Lacerta_Plossl_25mm"])

    @classmethod
    def Lacerta_Plossl_40mm(cls):
        return cls.from_database(cls._DATABASE["Lacerta_Plossl_40mm"])

    @classmethod
    def GSO_Wide_Field_4mm_70(cls):
        return cls.from_database(cls._DATABASE["GSO_Wide_Field_4mm_70"])

    @classmethod
    def GSO_Wide_Field_6mm_70(cls):
        return cls.from_database(cls._DATABASE["GSO_Wide_Field_6mm_70"])

    @classmethod
    def GSO_Wide_Field_10mm_70(cls):
        return cls.from_database(cls._DATABASE["GSO_Wide_Field_10mm_70"])

    @classmethod
    def GSO_Wide_Field_15mm_70(cls):
        return cls.from_database(cls._DATABASE["GSO_Wide_Field_15mm_70"])

    @classmethod
    def GSO_Wide_Field_20mm_70(cls):
        return cls.from_database(cls._DATABASE["GSO_Wide_Field_20mm_70"])

    @classmethod
    def GSO_Wide_Field_25mm_70(cls):
        return cls.from_database(cls._DATABASE["GSO_Wide_Field_25mm_70"])

    @classmethod
    def Celestron_Ultima_Edge_3_2mm(cls):
        return cls.from_database(cls._DATABASE["Celestron_Ultima_Edge_3_2mm"])

    @classmethod
    def Celestron_Ultima_Edge_5mm(cls):
        return cls.from_database(cls._DATABASE["Celestron_Ultima_Edge_5mm"])

    @classmethod
    def Celestron_Ultima_Edge_8mm(cls):
        return cls.from_database(cls._DATABASE["Celestron_Ultima_Edge_8mm"])

    @classmethod
    def Celestron_Ultima_Edge_12mm(cls):
        return cls.from_database(cls._DATABASE["Celestron_Ultima_Edge_12mm"])

    @classmethod
    def Celestron_Ultima_Edge_16mm(cls):
        return cls.from_database(cls._DATABASE["Celestron_Ultima_Edge_16mm"])

    @classmethod
    def Masuyama_12_5mm_85(cls):
        return cls.from_database(cls._DATABASE["Masuyama_12_5mm_85"])

    @classmethod
    def Docter_Noblex_UWF_10mm(cls):
        return cls.from_database(cls._DATABASE["Docter_Noblex_UWF_10mm"])

    @classmethod
    def Docter_Noblex_UWF_12_5mm(cls):
        return cls.from_database(cls._DATABASE["Docter_Noblex_UWF_12_5mm"])

    @classmethod
    def Docter_Noblex_UWF_17mm(cls):
        return cls.from_database(cls._DATABASE["Docter_Noblex_UWF_17mm"])

    @classmethod
    def Kokusai_Kohki_Ortho_5mm(cls):
        return cls.from_database(cls._DATABASE["Kokusai_Kohki_Ortho_5mm"])

    @classmethod
    def Kokusai_Kohki_Ortho_8mm(cls):
        return cls.from_database(cls._DATABASE["Kokusai_Kohki_Ortho_8mm"])

    @classmethod
    def Kokusai_Kohki_Ortho_12mm(cls):
        return cls.from_database(cls._DATABASE["Kokusai_Kohki_Ortho_12mm"])

    @classmethod
    def Kokusai_Kohki_Ortho_18mm(cls):
        return cls.from_database(cls._DATABASE["Kokusai_Kohki_Ortho_18mm"])

    @classmethod
    def Kokusai_Kohki_Ortho_25mm(cls):
        return cls.from_database(cls._DATABASE["Kokusai_Kohki_Ortho_25mm"])

    @classmethod
    def Takahashi_TPL_2_5mm(cls):
        return cls.from_database(cls._DATABASE["Takahashi_TPL_2_5mm"])

    @classmethod
    def Takahashi_TPL_3_6mm(cls):
        return cls.from_database(cls._DATABASE["Takahashi_TPL_3_6mm"])

    @classmethod
    def Takahashi_TPL_5mm(cls):
        return cls.from_database(cls._DATABASE["Takahashi_TPL_5mm"])

    @classmethod
    def Takahashi_TPL_6_4mm(cls):
        return cls.from_database(cls._DATABASE["Takahashi_TPL_6_4mm"])

    @classmethod
    def Takahashi_TPL_8mm(cls):
        return cls.from_database(cls._DATABASE["Takahashi_TPL_8mm"])

    @classmethod
    def Takahashi_TPL_12_5mm(cls):
        return cls.from_database(cls._DATABASE["Takahashi_TPL_12_5mm"])

    @classmethod
    def Takahashi_TPL_18mm(cls):
        return cls.from_database(cls._DATABASE["Takahashi_TPL_18mm"])

    @classmethod
    def Takahashi_TPL_25mm(cls):
        return cls.from_database(cls._DATABASE["Takahashi_TPL_25mm"])

    @classmethod
    def Takahashi_TPL_40mm(cls):
        return cls.from_database(cls._DATABASE["Takahashi_TPL_40mm"])

    @classmethod
    def Takahashi_Abbe_Ortho_4mm(cls):
        return cls.from_database(cls._DATABASE["Takahashi_Abbe_Ortho_4mm"])

    @classmethod
    def Takahashi_Abbe_Ortho_6mm(cls):
        return cls.from_database(cls._DATABASE["Takahashi_Abbe_Ortho_6mm"])

    @classmethod
    def Takahashi_Abbe_Ortho_9mm(cls):
        return cls.from_database(cls._DATABASE["Takahashi_Abbe_Ortho_9mm"])

    @classmethod
    def Takahashi_Abbe_Ortho_12_5mm(cls):
        return cls.from_database(cls._DATABASE["Takahashi_Abbe_Ortho_12_5mm"])

    @classmethod
    def Takahashi_Abbe_Ortho_18mm(cls):
        return cls.from_database(cls._DATABASE["Takahashi_Abbe_Ortho_18mm"])

    @classmethod
    def Takahashi_Abbe_Ortho_32mm(cls):
        return cls.from_database(cls._DATABASE["Takahashi_Abbe_Ortho_32mm"])

    @classmethod
    def Zeiss_Abbe_Ortho_4mm(cls):
        return cls.from_database(cls._DATABASE["Zeiss_Abbe_Ortho_4mm"])

    @classmethod
    def Zeiss_Abbe_Ortho_6mm(cls):
        return cls.from_database(cls._DATABASE["Zeiss_Abbe_Ortho_6mm"])

    @classmethod
    def Zeiss_Abbe_Ortho_10mm(cls):
        return cls.from_database(cls._DATABASE["Zeiss_Abbe_Ortho_10mm"])

    @classmethod
    def Zeiss_Abbe_Ortho_16mm(cls):
        return cls.from_database(cls._DATABASE["Zeiss_Abbe_Ortho_16mm"])

    @classmethod
    def Zeiss_Abbe_Ortho_25mm(cls):
        return cls.from_database(cls._DATABASE["Zeiss_Abbe_Ortho_25mm"])

    @classmethod
    def Leica_ASPH_10mm(cls):
        return cls.from_database(cls._DATABASE["Leica_ASPH_10mm"])

    @classmethod
    def Leica_ASPH_17_5mm(cls):
        return cls.from_database(cls._DATABASE["Leica_ASPH_17_5mm"])

    @classmethod
    def Leica_ASPH_25mm(cls):
        return cls.from_database(cls._DATABASE["Leica_ASPH_25mm"])

    @classmethod
    def Leica_ASPH_30mm(cls):
        return cls.from_database(cls._DATABASE["Leica_ASPH_30mm"])

    @classmethod
    def Antares_Speers_WALER_4_7mm(cls):
        return cls.from_database(cls._DATABASE["Antares_Speers_WALER_4_7mm"])

    @classmethod
    def Antares_Speers_WALER_7_5mm(cls):
        return cls.from_database(cls._DATABASE["Antares_Speers_WALER_7_5mm"])

    @classmethod
    def Antares_Speers_WALER_10mm(cls):
        return cls.from_database(cls._DATABASE["Antares_Speers_WALER_10mm"])

    @classmethod
    def Antares_Speers_WALER_15mm(cls):
        return cls.from_database(cls._DATABASE["Antares_Speers_WALER_15mm"])

    @classmethod
    def Antares_Speers_WALER_20mm(cls):
        return cls.from_database(cls._DATABASE["Antares_Speers_WALER_20mm"])

    @classmethod
    def Antares_Speers_WALER_25mm(cls):
        return cls.from_database(cls._DATABASE["Antares_Speers_WALER_25mm"])

    @classmethod
    def Antares_Speers_WALER_32mm(cls):
        return cls.from_database(cls._DATABASE["Antares_Speers_WALER_32mm"])

    @classmethod
    def GSO_Wide_Field_8mm_70(cls):
        return cls.from_database(cls._DATABASE["GSO_Wide_Field_8mm_70"])

    @classmethod
    def GSO_Wide_Field_30mm_70(cls):
        return cls.from_database(cls._DATABASE["GSO_Wide_Field_30mm_70"])

    @classmethod
    def GSO_Wide_Field_42mm_70(cls):
        return cls.from_database(cls._DATABASE["GSO_Wide_Field_42mm_70"])

    @classmethod
    def Celestron_Omni_4mm(cls):
        return cls.from_database(cls._DATABASE["Celestron_Omni_4mm"])

    @classmethod
    def Celestron_Omni_6mm(cls):
        return cls.from_database(cls._DATABASE["Celestron_Omni_6mm"])

    @classmethod
    def Celestron_Omni_9mm(cls):
        return cls.from_database(cls._DATABASE["Celestron_Omni_9mm"])

    @classmethod
    def Celestron_Omni_12mm(cls):
        return cls.from_database(cls._DATABASE["Celestron_Omni_12mm"])

    @classmethod
    def Celestron_Omni_15mm(cls):
        return cls.from_database(cls._DATABASE["Celestron_Omni_15mm"])

    @classmethod
    def Celestron_Omni_20mm(cls):
        return cls.from_database(cls._DATABASE["Celestron_Omni_20mm"])

    @classmethod
    def Celestron_Omni_25mm(cls):
        return cls.from_database(cls._DATABASE["Celestron_Omni_25mm"])

    @classmethod
    def Celestron_Omni_32mm(cls):
        return cls.from_database(cls._DATABASE["Celestron_Omni_32mm"])

    @classmethod
    def Celestron_Omni_40mm(cls):
        return cls.from_database(cls._DATABASE["Celestron_Omni_40mm"])

    @classmethod
    def Celestron_E_Lux_6_5mm(cls):
        return cls.from_database(cls._DATABASE["Celestron_E_Lux_6_5mm"])

    @classmethod
    def Celestron_E_Lux_10mm(cls):
        return cls.from_database(cls._DATABASE["Celestron_E_Lux_10mm"])

    @classmethod
    def Celestron_E_Lux_13mm(cls):
        return cls.from_database(cls._DATABASE["Celestron_E_Lux_13mm"])

    @classmethod
    def Celestron_E_Lux_20mm(cls):
        return cls.from_database(cls._DATABASE["Celestron_E_Lux_20mm"])

    @classmethod
    def Celestron_E_Lux_25mm(cls):
        return cls.from_database(cls._DATABASE["Celestron_E_Lux_25mm"])

    @classmethod
    def Celestron_E_Lux_32mm(cls):
        return cls.from_database(cls._DATABASE["Celestron_E_Lux_32mm"])

    @classmethod
    def Celestron_E_Lux_40mm(cls):
        return cls.from_database(cls._DATABASE["Celestron_E_Lux_40mm"])

    @classmethod
    def Orion_DeepView_20mm(cls):
        return cls.from_database(cls._DATABASE["Orion_DeepView_20mm"])

    @classmethod
    def Orion_DeepView_28mm(cls):
        return cls.from_database(cls._DATABASE["Orion_DeepView_28mm"])

    @classmethod
    def Orion_DeepView_35mm(cls):
        return cls.from_database(cls._DATABASE["Orion_DeepView_35mm"])

    @classmethod
    def Orion_DeepView_42mm(cls):
        return cls.from_database(cls._DATABASE["Orion_DeepView_42mm"])

    @classmethod
    def Orion_Q70_20mm(cls):
        return cls.from_database(cls._DATABASE["Orion_Q70_20mm"])

    @classmethod
    def Orion_Q70_26mm(cls):
        return cls.from_database(cls._DATABASE["Orion_Q70_26mm"])

    @classmethod
    def Orion_Q70_32mm(cls):
        return cls.from_database(cls._DATABASE["Orion_Q70_32mm"])

    @classmethod
    def Orion_Q70_38mm(cls):
        return cls.from_database(cls._DATABASE["Orion_Q70_38mm"])

    @classmethod
    def Orion_Expanse_6mm(cls):
        return cls.from_database(cls._DATABASE["Orion_Expanse_6mm"])

    @classmethod
    def Orion_Expanse_9mm(cls):
        return cls.from_database(cls._DATABASE["Orion_Expanse_9mm"])

    @classmethod
    def Orion_Expanse_15mm(cls):
        return cls.from_database(cls._DATABASE["Orion_Expanse_15mm"])

    @classmethod
    def Orion_Expanse_20mm(cls):
        return cls.from_database(cls._DATABASE["Orion_Expanse_20mm"])

    @classmethod
    def Orion_Sirius_Plossl_6mm(cls):
        return cls.from_database(cls._DATABASE["Orion_Sirius_Plossl_6mm"])

    @classmethod
    def Meade_Super_Plossl_4_7mm(cls):
        return cls.from_database(cls._DATABASE["Meade_Super_Plossl_4_7mm"])

    @classmethod
    def Meade_Super_Plossl_8_8mm(cls):
        return cls.from_database(cls._DATABASE["Meade_Super_Plossl_8_8mm"])

    @classmethod
    def Meade_Super_Plossl_17_8mm(cls):
        return cls.from_database(cls._DATABASE["Meade_Super_Plossl_17_8mm"])

    @classmethod
    def Meade_Super_Plossl_26mm(cls):
        return cls.from_database(cls._DATABASE["Meade_Super_Plossl_26mm"])

    @classmethod
    def Meade_Series_5000_MWA_5mm(cls):
        return cls.from_database(cls._DATABASE["Meade_Series_5000_MWA_5mm"])

    @classmethod
    def Meade_Series_5000_MWA_10mm(cls):
        return cls.from_database(cls._DATABASE["Meade_Series_5000_MWA_10mm"])

    @classmethod
    def Meade_Series_5000_MWA_15mm(cls):
        return cls.from_database(cls._DATABASE["Meade_Series_5000_MWA_15mm"])

    @classmethod
    def Meade_Series_5000_MWA_21mm(cls):
        return cls.from_database(cls._DATABASE["Meade_Series_5000_MWA_21mm"])

    @classmethod
    def Meade_Series_5000_MWA_28mm(cls):
        return cls.from_database(cls._DATABASE["Meade_Series_5000_MWA_28mm"])

    @classmethod
    def Omegon_SWA_4_5mm_70(cls):
        return cls.from_database(cls._DATABASE["Omegon_SWA_4_5mm_70"])

    @classmethod
    def Omegon_SWA_6_5mm_70(cls):
        return cls.from_database(cls._DATABASE["Omegon_SWA_6_5mm_70"])

    @classmethod
    def Omegon_SWA_9mm_70(cls):
        return cls.from_database(cls._DATABASE["Omegon_SWA_9mm_70"])

    @classmethod
    def Omegon_SWA_12mm_70(cls):
        return cls.from_database(cls._DATABASE["Omegon_SWA_12mm_70"])

    @classmethod
    def Omegon_SWA_15mm_70(cls):
        return cls.from_database(cls._DATABASE["Omegon_SWA_15mm_70"])

    @classmethod
    def Omegon_SWA_20mm_70(cls):
        return cls.from_database(cls._DATABASE["Omegon_SWA_20mm_70"])

    @classmethod
    def Omegon_LE_Planetary_3mm(cls):
        return cls.from_database(cls._DATABASE["Omegon_LE_Planetary_3mm"])

    @classmethod
    def Omegon_LE_Planetary_5mm(cls):
        return cls.from_database(cls._DATABASE["Omegon_LE_Planetary_5mm"])

    @classmethod
    def Omegon_LE_Planetary_7mm(cls):
        return cls.from_database(cls._DATABASE["Omegon_LE_Planetary_7mm"])

    @classmethod
    def Omegon_LE_Planetary_10mm(cls):
        return cls.from_database(cls._DATABASE["Omegon_LE_Planetary_10mm"])

    @classmethod
    def Omegon_LE_Planetary_14mm(cls):
        return cls.from_database(cls._DATABASE["Omegon_LE_Planetary_14mm"])

    @classmethod
    def Omegon_LE_Planetary_19mm(cls):
        return cls.from_database(cls._DATABASE["Omegon_LE_Planetary_19mm"])

    @classmethod
    def Omegon_LE_Planetary_25mm(cls):
        return cls.from_database(cls._DATABASE["Omegon_LE_Planetary_25mm"])

    @classmethod
    def Bresser_Plossl_6_5mm(cls):
        return cls.from_database(cls._DATABASE["Bresser_Plossl_6_5mm"])

    @classmethod
    def Bresser_Plossl_10mm(cls):
        return cls.from_database(cls._DATABASE["Bresser_Plossl_10mm"])

    @classmethod
    def Bresser_Plossl_15mm(cls):
        return cls.from_database(cls._DATABASE["Bresser_Plossl_15mm"])

    @classmethod
    def Bresser_Plossl_40mm(cls):
        return cls.from_database(cls._DATABASE["Bresser_Plossl_40mm"])

    @classmethod
    def Bresser_Wide_Angle_5mm_70(cls):
        return cls.from_database(cls._DATABASE["Bresser_Wide_Angle_5mm_70"])

    @classmethod
    def Bresser_Wide_Angle_8mm_70(cls):
        return cls.from_database(cls._DATABASE["Bresser_Wide_Angle_8mm_70"])

    @classmethod
    def Bresser_Wide_Angle_12mm_70(cls):
        return cls.from_database(cls._DATABASE["Bresser_Wide_Angle_12mm_70"])

    @classmethod
    def Bresser_Wide_Angle_15mm_70(cls):
        return cls.from_database(cls._DATABASE["Bresser_Wide_Angle_15mm_70"])

    @classmethod
    def Bresser_Wide_Angle_20mm_70(cls):
        return cls.from_database(cls._DATABASE["Bresser_Wide_Angle_20mm_70"])

    @classmethod
    def Bresser_Wide_Angle_25mm_70(cls):
        return cls.from_database(cls._DATABASE["Bresser_Wide_Angle_25mm_70"])

    @classmethod
    def SVBony_SV154_Plossl_4mm(cls):
        return cls.from_database(cls._DATABASE["SVBony_SV154_Plossl_4mm"])

    @classmethod
    def SVBony_SV154_Plossl_6_3mm(cls):
        return cls.from_database(cls._DATABASE["SVBony_SV154_Plossl_6_3mm"])

    @classmethod
    def SVBony_SV154_Plossl_10mm(cls):
        return cls.from_database(cls._DATABASE["SVBony_SV154_Plossl_10mm"])

    @classmethod
    def SVBony_SV154_Plossl_12_5mm(cls):
        return cls.from_database(cls._DATABASE["SVBony_SV154_Plossl_12_5mm"])

    @classmethod
    def SVBony_SV154_Plossl_17mm(cls):
        return cls.from_database(cls._DATABASE["SVBony_SV154_Plossl_17mm"])

    @classmethod
    def SVBony_SV154_Plossl_20mm(cls):
        return cls.from_database(cls._DATABASE["SVBony_SV154_Plossl_20mm"])

    @classmethod
    def SVBony_SV154_Plossl_25mm(cls):
        return cls.from_database(cls._DATABASE["SVBony_SV154_Plossl_25mm"])

    @classmethod
    def SVBony_SV154_Plossl_32mm(cls):
        return cls.from_database(cls._DATABASE["SVBony_SV154_Plossl_32mm"])

    @classmethod
    def SVBony_SV154_Plossl_40mm(cls):
        return cls.from_database(cls._DATABASE["SVBony_SV154_Plossl_40mm"])

    @classmethod
    def SVBony_SV213_TMB_3mm(cls):
        return cls.from_database(cls._DATABASE["SVBony_SV213_TMB_3mm"])

    @classmethod
    def SVBony_SV213_TMB_4mm(cls):
        return cls.from_database(cls._DATABASE["SVBony_SV213_TMB_4mm"])

    @classmethod
    def SVBony_SV213_TMB_5mm(cls):
        return cls.from_database(cls._DATABASE["SVBony_SV213_TMB_5mm"])

    @classmethod
    def SVBony_SV213_TMB_6mm(cls):
        return cls.from_database(cls._DATABASE["SVBony_SV213_TMB_6mm"])

    @classmethod
    def SVBony_SV213_TMB_7mm(cls):
        return cls.from_database(cls._DATABASE["SVBony_SV213_TMB_7mm"])

    @classmethod
    def SVBony_SV213_TMB_8mm(cls):
        return cls.from_database(cls._DATABASE["SVBony_SV213_TMB_8mm"])

    @classmethod
    def SVBony_SV213_TMB_9mm(cls):
        return cls.from_database(cls._DATABASE["SVBony_SV213_TMB_9mm"])

    @classmethod
    def SVBony_SV213_TMB_10mm(cls):
        return cls.from_database(cls._DATABASE["SVBony_SV213_TMB_10mm"])

    @classmethod
    def SVBony_SV213_TMB_12_5mm(cls):
        return cls.from_database(cls._DATABASE["SVBony_SV213_TMB_12_5mm"])

    @classmethod
    def Lacerta_SWMA_100_5mm(cls):
        return cls.from_database(cls._DATABASE["Lacerta_SWMA_100_5mm"])

    @classmethod
    def Lacerta_SWMA_100_7mm(cls):
        return cls.from_database(cls._DATABASE["Lacerta_SWMA_100_7mm"])

    @classmethod
    def Lacerta_SWMA_100_9mm(cls):
        return cls.from_database(cls._DATABASE["Lacerta_SWMA_100_9mm"])

    @classmethod
    def Lacerta_SWMA_100_14mm(cls):
        return cls.from_database(cls._DATABASE["Lacerta_SWMA_100_14mm"])

    @classmethod
    def Lacerta_SWMA_100_20mm(cls):
        return cls.from_database(cls._DATABASE["Lacerta_SWMA_100_20mm"])

    @classmethod
    def Lacerta_Plossl_10mm(cls):
        return cls.from_database(cls._DATABASE["Lacerta_Plossl_10mm"])

    @classmethod
    def Lacerta_Plossl_15mm(cls):
        return cls.from_database(cls._DATABASE["Lacerta_Plossl_15mm"])

    @classmethod
    def Lacerta_Plossl_32mm(cls):
        return cls.from_database(cls._DATABASE["Lacerta_Plossl_32mm"])

    @classmethod
    def TS_Optics_WA_72_5mm(cls):
        return cls.from_database(cls._DATABASE["TS_Optics_WA_72_5mm"])

    @classmethod
    def TS_Optics_WA_72_7mm(cls):
        return cls.from_database(cls._DATABASE["TS_Optics_WA_72_7mm"])

    @classmethod
    def TS_Optics_WA_72_10mm(cls):
        return cls.from_database(cls._DATABASE["TS_Optics_WA_72_10mm"])

    @classmethod
    def TS_Optics_WA_72_15mm(cls):
        return cls.from_database(cls._DATABASE["TS_Optics_WA_72_15mm"])

    @classmethod
    def TS_Optics_WA_72_20mm(cls):
        return cls.from_database(cls._DATABASE["TS_Optics_WA_72_20mm"])

    @classmethod
    def TS_Optics_WA_72_25mm(cls):
        return cls.from_database(cls._DATABASE["TS_Optics_WA_72_25mm"])

    @classmethod
    def TS_Optics_Expanse_4mm_70(cls):
        return cls.from_database(cls._DATABASE["TS_Optics_Expanse_4mm_70"])

    @classmethod
    def TS_Optics_Expanse_6mm_70(cls):
        return cls.from_database(cls._DATABASE["TS_Optics_Expanse_6mm_70"])

    @classmethod
    def TS_Optics_Expanse_8mm_70(cls):
        return cls.from_database(cls._DATABASE["TS_Optics_Expanse_8mm_70"])

    @classmethod
    def TS_Optics_Expanse_10mm_70(cls):
        return cls.from_database(cls._DATABASE["TS_Optics_Expanse_10mm_70"])

    @classmethod
    def TS_Optics_Expanse_13mm_70(cls):
        return cls.from_database(cls._DATABASE["TS_Optics_Expanse_13mm_70"])

    @classmethod
    def TS_Optics_Expanse_17mm_70(cls):
        return cls.from_database(cls._DATABASE["TS_Optics_Expanse_17mm_70"])

    @classmethod
    def TS_Optics_Expanse_22mm_70(cls):
        return cls.from_database(cls._DATABASE["TS_Optics_Expanse_22mm_70"])

    @classmethod
    def TS_Optics_Plossl_4mm(cls):
        return cls.from_database(cls._DATABASE["TS_Optics_Plossl_4mm"])

    @classmethod
    def TS_Optics_Plossl_6_3mm(cls):
        return cls.from_database(cls._DATABASE["TS_Optics_Plossl_6_3mm"])

    @classmethod
    def TS_Optics_Plossl_10mm(cls):
        return cls.from_database(cls._DATABASE["TS_Optics_Plossl_10mm"])

    @classmethod
    def TS_Optics_Plossl_15mm(cls):
        return cls.from_database(cls._DATABASE["TS_Optics_Plossl_15mm"])

    @classmethod
    def TS_Optics_Plossl_20mm(cls):
        return cls.from_database(cls._DATABASE["TS_Optics_Plossl_20mm"])

    @classmethod
    def TS_Optics_Plossl_25mm(cls):
        return cls.from_database(cls._DATABASE["TS_Optics_Plossl_25mm"])

    @classmethod
    def TS_Optics_Plossl_32mm(cls):
        return cls.from_database(cls._DATABASE["TS_Optics_Plossl_32mm"])

    @classmethod
    def TS_Optics_Plossl_40mm(cls):
        return cls.from_database(cls._DATABASE["TS_Optics_Plossl_40mm"])

    @classmethod
    def Explore_Scientific_9mm_120(cls):
        return cls.from_database(cls._DATABASE["Explore_Scientific_9mm_120"])

    @classmethod
    def Explore_Scientific_10mm_52(cls):
        return cls.from_database(cls._DATABASE["Explore_Scientific_10mm_52"])

    @classmethod
    def Explore_Scientific_15mm_52(cls):
        return cls.from_database(cls._DATABASE["Explore_Scientific_15mm_52"])

    @classmethod
    def Explore_Scientific_20mm_52(cls):
        return cls.from_database(cls._DATABASE["Explore_Scientific_20mm_52"])

    @classmethod
    def Explore_Scientific_25mm_52(cls):
        return cls.from_database(cls._DATABASE["Explore_Scientific_25mm_52"])

    @classmethod
    def Explore_Scientific_40mm_52(cls):
        return cls.from_database(cls._DATABASE["Explore_Scientific_40mm_52"])

    @classmethod
    def APM_UFF_10mm(cls):
        return cls.from_database(cls._DATABASE["APM_UFF_10mm"])

    @classmethod
    def APM_UFF_15mm(cls):
        return cls.from_database(cls._DATABASE["APM_UFF_15mm"])

    @classmethod
    def APM_UFF_18mm(cls):
        return cls.from_database(cls._DATABASE["APM_UFF_18mm"])

    @classmethod
    def APM_UFF_24mm(cls):
        return cls.from_database(cls._DATABASE["APM_UFF_24mm"])

    @classmethod
    def APM_UFF_30mm(cls):
        return cls.from_database(cls._DATABASE["APM_UFF_30mm"])

    @classmethod
    def APM_Plossl_6_5mm(cls):
        return cls.from_database(cls._DATABASE["APM_Plossl_6_5mm"])

    @classmethod
    def APM_Plossl_10mm(cls):
        return cls.from_database(cls._DATABASE["APM_Plossl_10mm"])

    @classmethod
    def APM_Plossl_15mm(cls):
        return cls.from_database(cls._DATABASE["APM_Plossl_15mm"])

    @classmethod
    def APM_Plossl_20mm(cls):
        return cls.from_database(cls._DATABASE["APM_Plossl_20mm"])

    @classmethod
    def APM_Plossl_25mm(cls):
        return cls.from_database(cls._DATABASE["APM_Plossl_25mm"])

    @classmethod
    def APM_Plossl_32mm(cls):
        return cls.from_database(cls._DATABASE["APM_Plossl_32mm"])

    @classmethod
    def APM_Plossl_40mm(cls):
        return cls.from_database(cls._DATABASE["APM_Plossl_40mm"])

    @classmethod
    def Stellarvue_Optimus_3_5mm(cls):
        return cls.from_database(cls._DATABASE["Stellarvue_Optimus_3_5mm"])

    @classmethod
    def Stellarvue_Optimus_5mm(cls):
        return cls.from_database(cls._DATABASE["Stellarvue_Optimus_5mm"])

    @classmethod
    def Stellarvue_Optimus_7mm(cls):
        return cls.from_database(cls._DATABASE["Stellarvue_Optimus_7mm"])

    @classmethod
    def Stellarvue_Optimus_10mm(cls):
        return cls.from_database(cls._DATABASE["Stellarvue_Optimus_10mm"])

    @classmethod
    def Stellarvue_Optimus_14mm(cls):
        return cls.from_database(cls._DATABASE["Stellarvue_Optimus_14mm"])

    @classmethod
    def Stellarvue_Optimus_19mm(cls):
        return cls.from_database(cls._DATABASE["Stellarvue_Optimus_19mm"])

    @classmethod
    def Stellarvue_Optimus_28mm(cls):
        return cls.from_database(cls._DATABASE["Stellarvue_Optimus_28mm"])

    @classmethod
    def Meade_Series_4000_8_24mm_Zoom(cls):
        return cls.from_database(cls._DATABASE["Meade_Series_4000_8_24mm_Zoom"])

    @classmethod
    def Baader_Hyperion_Mark_IV_8_24mm_Zoom(cls):
        return cls.from_database(cls._DATABASE["Baader_Hyperion_Mark_IV_8_24mm_Zoom"])

    @classmethod
    def Celestron_8_24mm_Zoom(cls):
        return cls.from_database(cls._DATABASE["Celestron_8_24mm_Zoom"])

    @classmethod
    def Sky_Watcher_7_2_21_5mm_Zoom(cls):
        return cls.from_database(cls._DATABASE["Sky_Watcher_7_2_21_5mm_Zoom"])

    @classmethod
    def Orion_8_24mm_Zoom(cls):
        return cls.from_database(cls._DATABASE["Orion_8_24mm_Zoom"])

    @classmethod
    def SVBony_SV135_7_21mm_Zoom(cls):
        return cls.from_database(cls._DATABASE["SVBony_SV135_7_21mm_Zoom"])

    @classmethod
    def Explore_Scientific_8_24mm_68_Zoom(cls):
        return cls.from_database(cls._DATABASE["Explore_Scientific_8_24mm_68_Zoom"])

    @classmethod
    def Pentax_XF_6_5_19_5mm_Zoom(cls):
        return cls.from_database(cls._DATABASE["Pentax_XF_6_5_19_5mm_Zoom"])

    @classmethod
    def Nikon_Fieldscope_Zoom_13_40mm(cls):
        return cls.from_database(cls._DATABASE["Nikon_Fieldscope_Zoom_13_40mm"])

    @classmethod
    def Vixen_NLV_Zoom_8_24mm(cls):
        return cls.from_database(cls._DATABASE["Vixen_NLV_Zoom_8_24mm"])

    @classmethod
    def Sky_Watcher_Starguider_Dual_ED_2_5mm(cls):
        return cls.from_database(cls._DATABASE["Sky_Watcher_Starguider_Dual_ED_2_5mm"])

    @classmethod
    def Sky_Watcher_Starguider_Dual_ED_3_2mm(cls):
        return cls.from_database(cls._DATABASE["Sky_Watcher_Starguider_Dual_ED_3_2mm"])

    @classmethod
    def Sky_Watcher_Starguider_Dual_ED_4mm(cls):
        return cls.from_database(cls._DATABASE["Sky_Watcher_Starguider_Dual_ED_4mm"])

    @classmethod
    def Sky_Watcher_Starguider_Dual_ED_5mm(cls):
        return cls.from_database(cls._DATABASE["Sky_Watcher_Starguider_Dual_ED_5mm"])

    @classmethod
    def Sky_Watcher_Starguider_Dual_ED_6mm(cls):
        return cls.from_database(cls._DATABASE["Sky_Watcher_Starguider_Dual_ED_6mm"])

    @classmethod
    def Sky_Watcher_Starguider_Dual_ED_8mm(cls):
        return cls.from_database(cls._DATABASE["Sky_Watcher_Starguider_Dual_ED_8mm"])

    @classmethod
    def Sky_Watcher_Starguider_Dual_ED_10mm(cls):
        return cls.from_database(cls._DATABASE["Sky_Watcher_Starguider_Dual_ED_10mm"])

    @classmethod
    def Sky_Watcher_Starguider_Dual_ED_15mm(cls):
        return cls.from_database(cls._DATABASE["Sky_Watcher_Starguider_Dual_ED_15mm"])

    @classmethod
    def Sky_Watcher_Starguider_Dual_ED_20mm(cls):
        return cls.from_database(cls._DATABASE["Sky_Watcher_Starguider_Dual_ED_20mm"])

    @classmethod
    def Sky_Watcher_Starguider_Dual_ED_25mm(cls):
        return cls.from_database(cls._DATABASE["Sky_Watcher_Starguider_Dual_ED_25mm"])

    @classmethod
    def Agena_SWA_4mm_70(cls):
        return cls.from_database(cls._DATABASE["Agena_SWA_4mm_70"])

    @classmethod
    def Agena_SWA_6mm_70(cls):
        return cls.from_database(cls._DATABASE["Agena_SWA_6mm_70"])

    @classmethod
    def Agena_SWA_9mm_70(cls):
        return cls.from_database(cls._DATABASE["Agena_SWA_9mm_70"])

    @classmethod
    def Agena_SWA_12mm_70(cls):
        return cls.from_database(cls._DATABASE["Agena_SWA_12mm_70"])

    @classmethod
    def Agena_SWA_15mm_70(cls):
        return cls.from_database(cls._DATABASE["Agena_SWA_15mm_70"])

    @classmethod
    def Agena_SWA_20mm_70(cls):
        return cls.from_database(cls._DATABASE["Agena_SWA_20mm_70"])

    @classmethod
    def Agena_SWA_25mm_70(cls):
        return cls.from_database(cls._DATABASE["Agena_SWA_25mm_70"])

    @classmethod
    def Agena_SWA_32mm_70(cls):
        return cls.from_database(cls._DATABASE["Agena_SWA_32mm_70"])

    @classmethod
    def Agena_EWA_3_5mm_82(cls):
        return cls.from_database(cls._DATABASE["Agena_EWA_3_5mm_82"])

    @classmethod
    def Agena_EWA_5mm_82(cls):
        return cls.from_database(cls._DATABASE["Agena_EWA_5mm_82"])

    @classmethod
    def Agena_EWA_7mm_82(cls):
        return cls.from_database(cls._DATABASE["Agena_EWA_7mm_82"])

    @classmethod
    def Agena_EWA_9mm_82(cls):
        return cls.from_database(cls._DATABASE["Agena_EWA_9mm_82"])

    @classmethod
    def Agena_EWA_13mm_82(cls):
        return cls.from_database(cls._DATABASE["Agena_EWA_13mm_82"])

    @classmethod
    def Agena_EWA_16mm_82(cls):
        return cls.from_database(cls._DATABASE["Agena_EWA_16mm_82"])

    @classmethod
    def Agena_EWA_20mm_82(cls):
        return cls.from_database(cls._DATABASE["Agena_EWA_20mm_82"])

    @classmethod
    def Astro_Tech_Paradigm_3_5mm(cls):
        return cls.from_database(cls._DATABASE["Astro_Tech_Paradigm_3_5mm"])

    @classmethod
    def Astro_Tech_Paradigm_5mm(cls):
        return cls.from_database(cls._DATABASE["Astro_Tech_Paradigm_5mm"])

    @classmethod
    def Astro_Tech_Paradigm_7mm(cls):
        return cls.from_database(cls._DATABASE["Astro_Tech_Paradigm_7mm"])

    @classmethod
    def Astro_Tech_Paradigm_9mm(cls):
        return cls.from_database(cls._DATABASE["Astro_Tech_Paradigm_9mm"])

    @classmethod
    def Astro_Tech_Paradigm_12mm(cls):
        return cls.from_database(cls._DATABASE["Astro_Tech_Paradigm_12mm"])

    @classmethod
    def Astro_Tech_Paradigm_15mm(cls):
        return cls.from_database(cls._DATABASE["Astro_Tech_Paradigm_15mm"])

    @classmethod
    def Astro_Tech_Paradigm_18mm(cls):
        return cls.from_database(cls._DATABASE["Astro_Tech_Paradigm_18mm"])

    @classmethod
    def Astro_Tech_Paradigm_22mm(cls):
        return cls.from_database(cls._DATABASE["Astro_Tech_Paradigm_22mm"])

    @classmethod
    def Astro_Tech_Paradigm_27mm(cls):
        return cls.from_database(cls._DATABASE["Astro_Tech_Paradigm_27mm"])

    @classmethod
    def Astro_Tech_Titan_5mm_68(cls):
        return cls.from_database(cls._DATABASE["Astro_Tech_Titan_5mm_68"])

    @classmethod
    def Astro_Tech_Titan_8mm_68(cls):
        return cls.from_database(cls._DATABASE["Astro_Tech_Titan_8mm_68"])

    @classmethod
    def Astro_Tech_Titan_12mm_68(cls):
        return cls.from_database(cls._DATABASE["Astro_Tech_Titan_12mm_68"])

    @classmethod
    def Astro_Tech_Titan_18mm_68(cls):
        return cls.from_database(cls._DATABASE["Astro_Tech_Titan_18mm_68"])

    @classmethod
    def Astro_Tech_Titan_25mm_68(cls):
        return cls.from_database(cls._DATABASE["Astro_Tech_Titan_25mm_68"])

    @classmethod
    def Lunt_Solar_EWA_6mm_82(cls):
        return cls.from_database(cls._DATABASE["Lunt_Solar_EWA_6mm_82"])

    @classmethod
    def Lunt_Solar_EWA_8mm_82(cls):
        return cls.from_database(cls._DATABASE["Lunt_Solar_EWA_8mm_82"])

    @classmethod
    def Lunt_Solar_EWA_10mm_82(cls):
        return cls.from_database(cls._DATABASE["Lunt_Solar_EWA_10mm_82"])

    @classmethod
    def Lunt_Solar_EWA_13mm_82(cls):
        return cls.from_database(cls._DATABASE["Lunt_Solar_EWA_13mm_82"])

    @classmethod
    def Lunt_Solar_EWA_16mm_82(cls):
        return cls.from_database(cls._DATABASE["Lunt_Solar_EWA_16mm_82"])

    @classmethod
    def Lunt_Solar_EWA_19mm_82(cls):
        return cls.from_database(cls._DATABASE["Lunt_Solar_EWA_19mm_82"])

    @classmethod
    def Lunt_Solar_EWA_22mm_82(cls):
        return cls.from_database(cls._DATABASE["Lunt_Solar_EWA_22mm_82"])

    @classmethod
    def Lunt_Solar_EWA_26mm_82(cls):
        return cls.from_database(cls._DATABASE["Lunt_Solar_EWA_26mm_82"])

    @classmethod
    def Lunt_Solar_EWA_32mm_82(cls):
        return cls.from_database(cls._DATABASE["Lunt_Solar_EWA_32mm_82"])

    @classmethod
    def Kasai_HD_Ortho_4mm(cls):
        return cls.from_database(cls._DATABASE["Kasai_HD_Ortho_4mm"])

    @classmethod
    def Kasai_HD_Ortho_5mm(cls):
        return cls.from_database(cls._DATABASE["Kasai_HD_Ortho_5mm"])

    @classmethod
    def Kasai_HD_Ortho_6mm(cls):
        return cls.from_database(cls._DATABASE["Kasai_HD_Ortho_6mm"])

    @classmethod
    def Kasai_HD_Ortho_8mm(cls):
        return cls.from_database(cls._DATABASE["Kasai_HD_Ortho_8mm"])

    @classmethod
    def Kasai_HD_Ortho_10mm(cls):
        return cls.from_database(cls._DATABASE["Kasai_HD_Ortho_10mm"])

    @classmethod
    def Kasai_HD_Ortho_12_5mm(cls):
        return cls.from_database(cls._DATABASE["Kasai_HD_Ortho_12_5mm"])

    @classmethod
    def Kasai_HD_Ortho_18mm(cls):
        return cls.from_database(cls._DATABASE["Kasai_HD_Ortho_18mm"])

    @classmethod
    def Kasai_HD_Ortho_25mm(cls):
        return cls.from_database(cls._DATABASE["Kasai_HD_Ortho_25mm"])

    @classmethod
    def Antares_Plossl_4mm(cls):
        return cls.from_database(cls._DATABASE["Antares_Plossl_4mm"])

    @classmethod
    def Antares_Plossl_6mm(cls):
        return cls.from_database(cls._DATABASE["Antares_Plossl_6mm"])

    @classmethod
    def Antares_Plossl_8mm(cls):
        return cls.from_database(cls._DATABASE["Antares_Plossl_8mm"])

    @classmethod
    def Antares_Plossl_10mm(cls):
        return cls.from_database(cls._DATABASE["Antares_Plossl_10mm"])

    @classmethod
    def Antares_Plossl_12_5mm(cls):
        return cls.from_database(cls._DATABASE["Antares_Plossl_12_5mm"])

    @classmethod
    def Antares_Plossl_15mm(cls):
        return cls.from_database(cls._DATABASE["Antares_Plossl_15mm"])

    @classmethod
    def Antares_Plossl_20mm(cls):
        return cls.from_database(cls._DATABASE["Antares_Plossl_20mm"])

    @classmethod
    def Antares_Plossl_25mm(cls):
        return cls.from_database(cls._DATABASE["Antares_Plossl_25mm"])

    @classmethod
    def Tecnosky_SWA_5mm_70(cls):
        return cls.from_database(cls._DATABASE["Tecnosky_SWA_5mm_70"])

    @classmethod
    def Tecnosky_SWA_7mm_70(cls):
        return cls.from_database(cls._DATABASE["Tecnosky_SWA_7mm_70"])

    @classmethod
    def Tecnosky_SWA_10mm_70(cls):
        return cls.from_database(cls._DATABASE["Tecnosky_SWA_10mm_70"])

    @classmethod
    def Tecnosky_SWA_14mm_70(cls):
        return cls.from_database(cls._DATABASE["Tecnosky_SWA_14mm_70"])

    @classmethod
    def Tecnosky_SWA_20mm_70(cls):
        return cls.from_database(cls._DATABASE["Tecnosky_SWA_20mm_70"])

    @classmethod
    def Tecnosky_SWA_25mm_70(cls):
        return cls.from_database(cls._DATABASE["Tecnosky_SWA_25mm_70"])

    @classmethod
    def Tecnosky_SWA_30mm_70(cls):
        return cls.from_database(cls._DATABASE["Tecnosky_SWA_30mm_70"])

    @classmethod
    def Tecnosky_Plossl_6mm(cls):
        return cls.from_database(cls._DATABASE["Tecnosky_Plossl_6mm"])

    @classmethod
    def Tecnosky_Plossl_10mm(cls):
        return cls.from_database(cls._DATABASE["Tecnosky_Plossl_10mm"])

    @classmethod
    def Tecnosky_Plossl_15mm(cls):
        return cls.from_database(cls._DATABASE["Tecnosky_Plossl_15mm"])

    @classmethod
    def Tecnosky_Plossl_20mm(cls):
        return cls.from_database(cls._DATABASE["Tecnosky_Plossl_20mm"])

    @classmethod
    def Tecnosky_Plossl_25mm(cls):
        return cls.from_database(cls._DATABASE["Tecnosky_Plossl_25mm"])

    @classmethod
    def Tecnosky_Plossl_32mm(cls):
        return cls.from_database(cls._DATABASE["Tecnosky_Plossl_32mm"])

    @classmethod
    def TPO_SWA_5mm_68(cls):
        return cls.from_database(cls._DATABASE["TPO_SWA_5mm_68"])

    @classmethod
    def TPO_SWA_8mm_68(cls):
        return cls.from_database(cls._DATABASE["TPO_SWA_8mm_68"])

    @classmethod
    def TPO_SWA_12mm_68(cls):
        return cls.from_database(cls._DATABASE["TPO_SWA_12mm_68"])

    @classmethod
    def TPO_SWA_18mm_68(cls):
        return cls.from_database(cls._DATABASE["TPO_SWA_18mm_68"])

    @classmethod
    def TPO_SWA_25mm_68(cls):
        return cls.from_database(cls._DATABASE["TPO_SWA_25mm_68"])

    @classmethod
    def TPO_SWA_32mm_68(cls):
        return cls.from_database(cls._DATABASE["TPO_SWA_32mm_68"])

    @classmethod
    def TPO_Plossl_6mm(cls):
        return cls.from_database(cls._DATABASE["TPO_Plossl_6mm"])

    @classmethod
    def TPO_Plossl_10mm(cls):
        return cls.from_database(cls._DATABASE["TPO_Plossl_10mm"])

    @classmethod
    def TPO_Plossl_15mm(cls):
        return cls.from_database(cls._DATABASE["TPO_Plossl_15mm"])

    @classmethod
    def TPO_Plossl_20mm(cls):
        return cls.from_database(cls._DATABASE["TPO_Plossl_20mm"])

    @classmethod
    def TPO_Plossl_25mm(cls):
        return cls.from_database(cls._DATABASE["TPO_Plossl_25mm"])

    @classmethod
    def TPO_Plossl_32mm(cls):
        return cls.from_database(cls._DATABASE["TPO_Plossl_32mm"])

    @classmethod
    def Istar_UWA_3_5mm_100(cls):
        return cls.from_database(cls._DATABASE["Istar_UWA_3_5mm_100"])

    @classmethod
    def Istar_UWA_5mm_100(cls):
        return cls.from_database(cls._DATABASE["Istar_UWA_5mm_100"])

    @classmethod
    def Istar_UWA_7mm_100(cls):
        return cls.from_database(cls._DATABASE["Istar_UWA_7mm_100"])

    @classmethod
    def Istar_UWA_10mm_100(cls):
        return cls.from_database(cls._DATABASE["Istar_UWA_10mm_100"])

    @classmethod
    def Istar_UWA_14mm_100(cls):
        return cls.from_database(cls._DATABASE["Istar_UWA_14mm_100"])

    @classmethod
    def Istar_UWA_18mm_100(cls):
        return cls.from_database(cls._DATABASE["Istar_UWA_18mm_100"])

    @classmethod
    def Istar_UWA_22mm_100(cls):
        return cls.from_database(cls._DATABASE["Istar_UWA_22mm_100"])

    @classmethod
    def Istar_UWA_30mm_100(cls):
        return cls.from_database(cls._DATABASE["Istar_UWA_30mm_100"])

    @classmethod
    def Maxvision_3_5mm_82(cls):
        return cls.from_database(cls._DATABASE["Maxvision_3_5mm_82"])

    @classmethod
    def Maxvision_6mm_82(cls):
        return cls.from_database(cls._DATABASE["Maxvision_6mm_82"])

    @classmethod
    def Maxvision_9mm_82(cls):
        return cls.from_database(cls._DATABASE["Maxvision_9mm_82"])

    @classmethod
    def Maxvision_13mm_82(cls):
        return cls.from_database(cls._DATABASE["Maxvision_13mm_82"])

    @classmethod
    def Maxvision_20mm_82(cls):
        return cls.from_database(cls._DATABASE["Maxvision_20mm_82"])

    @classmethod
    def Maxvision_28mm_82(cls):
        return cls.from_database(cls._DATABASE["Maxvision_28mm_82"])

    @classmethod
    def Explore_Scientific_5mm_92(cls):
        return cls.from_database(cls._DATABASE["Explore_Scientific_5mm_92"])

    @classmethod
    def Explore_Scientific_8mm_92(cls):
        return cls.from_database(cls._DATABASE["Explore_Scientific_8mm_92"])

    @classmethod
    def Explore_Scientific_12mm_92(cls):
        return cls.from_database(cls._DATABASE["Explore_Scientific_12mm_92"])

    @classmethod
    def Explore_Scientific_17mm_92(cls):
        return cls.from_database(cls._DATABASE["Explore_Scientific_17mm_92"])

    @classmethod
    def Vixen_NPL_Plossl_2_5mm(cls):
        return cls.from_database(cls._DATABASE["Vixen_NPL_Plossl_2_5mm"])

    @classmethod
    def Vixen_NPL_Plossl_4mm(cls):
        return cls.from_database(cls._DATABASE["Vixen_NPL_Plossl_4mm"])

    @classmethod
    def Vixen_NPL_Plossl_5mm(cls):
        return cls.from_database(cls._DATABASE["Vixen_NPL_Plossl_5mm"])

    @classmethod
    def Vixen_NPL_Plossl_6mm(cls):
        return cls.from_database(cls._DATABASE["Vixen_NPL_Plossl_6mm"])

    @classmethod
    def Vixen_NPL_Plossl_8mm(cls):
        return cls.from_database(cls._DATABASE["Vixen_NPL_Plossl_8mm"])

    @classmethod
    def Vixen_NPL_Plossl_10mm(cls):
        return cls.from_database(cls._DATABASE["Vixen_NPL_Plossl_10mm"])

    @classmethod
    def Vixen_NPL_Plossl_12mm(cls):
        return cls.from_database(cls._DATABASE["Vixen_NPL_Plossl_12mm"])

    @classmethod
    def Vixen_NPL_Plossl_15mm(cls):
        return cls.from_database(cls._DATABASE["Vixen_NPL_Plossl_15mm"])

    @classmethod
    def Vixen_NPL_Plossl_18mm(cls):
        return cls.from_database(cls._DATABASE["Vixen_NPL_Plossl_18mm"])

    @classmethod
    def Vixen_NPL_Plossl_25mm(cls):
        return cls.from_database(cls._DATABASE["Vixen_NPL_Plossl_25mm"])

    @classmethod
    def Sky_Watcher_Long_Eye_Relief_4_5mm(cls):
        return cls.from_database(cls._DATABASE["Sky_Watcher_Long_Eye_Relief_4_5mm"])

    @classmethod
    def Sky_Watcher_Long_Eye_Relief_6mm(cls):
        return cls.from_database(cls._DATABASE["Sky_Watcher_Long_Eye_Relief_6mm"])

    @classmethod
    def Sky_Watcher_Long_Eye_Relief_8mm(cls):
        return cls.from_database(cls._DATABASE["Sky_Watcher_Long_Eye_Relief_8mm"])

    @classmethod
    def Sky_Watcher_Long_Eye_Relief_10mm(cls):
        return cls.from_database(cls._DATABASE["Sky_Watcher_Long_Eye_Relief_10mm"])

    @classmethod
    def Sky_Watcher_Long_Eye_Relief_12_5mm(cls):
        return cls.from_database(cls._DATABASE["Sky_Watcher_Long_Eye_Relief_12_5mm"])

    @classmethod
    def Sky_Watcher_Long_Eye_Relief_15mm(cls):
        return cls.from_database(cls._DATABASE["Sky_Watcher_Long_Eye_Relief_15mm"])

    @classmethod
    def Sky_Watcher_Long_Eye_Relief_18mm(cls):
        return cls.from_database(cls._DATABASE["Sky_Watcher_Long_Eye_Relief_18mm"])

    @classmethod
    def Sky_Watcher_Long_Eye_Relief_21mm(cls):
        return cls.from_database(cls._DATABASE["Sky_Watcher_Long_Eye_Relief_21mm"])

    @classmethod
    def Sky_Watcher_Long_Eye_Relief_25mm(cls):
        return cls.from_database(cls._DATABASE["Sky_Watcher_Long_Eye_Relief_25mm"])

    @classmethod
    def Generic_Plossl_32mm(cls):
        return cls.from_database(cls._DATABASE["Generic_Plossl_32mm"])

    @classmethod
    def Generic_SWA_6mm_70(cls):
        return cls.from_database(cls._DATABASE["Generic_SWA_6mm_70"])

    @classmethod
    def Generic_SWA_10mm_70(cls):
        return cls.from_database(cls._DATABASE["Generic_SWA_10mm_70"])

    @classmethod
    def Generic_SWA_15mm_70(cls):
        return cls.from_database(cls._DATABASE["Generic_SWA_15mm_70"])

    @classmethod
    def Generic_SWA_20mm_70(cls):
        return cls.from_database(cls._DATABASE["Generic_SWA_20mm_70"])

    @classmethod
    def Generic_SWA_25mm_70(cls):
        return cls.from_database(cls._DATABASE["Generic_SWA_25mm_70"])

    @classmethod
    def Generic_SWA_32mm_70(cls):
        return cls.from_database(cls._DATABASE["Generic_SWA_32mm_70"])

    @classmethod
    def Generic_WA_6mm_68(cls):
        return cls.from_database(cls._DATABASE["Generic_WA_6mm_68"])

    @classmethod
    def Generic_WA_9mm_68(cls):
        return cls.from_database(cls._DATABASE["Generic_WA_9mm_68"])

    @classmethod
    def Generic_WA_12mm_68(cls):
        return cls.from_database(cls._DATABASE["Generic_WA_12mm_68"])

    @classmethod
    def Generic_WA_15mm_68(cls):
        return cls.from_database(cls._DATABASE["Generic_WA_15mm_68"])

    @classmethod
    def Generic_WA_20mm_68(cls):
        return cls.from_database(cls._DATABASE["Generic_WA_20mm_68"])

    @classmethod
    def Celestron_StarSense_10mm(cls):
        return cls.from_database(cls._DATABASE["Celestron_StarSense_10mm"])

    @classmethod
    def Celestron_StarSense_15mm(cls):
        return cls.from_database(cls._DATABASE["Celestron_StarSense_15mm"])

    @classmethod
    def Celestron_StarSense_20mm(cls):
        return cls.from_database(cls._DATABASE["Celestron_StarSense_20mm"])

    @classmethod
    def Celestron_StarSense_25mm(cls):
        return cls.from_database(cls._DATABASE["Celestron_StarSense_25mm"])

    @classmethod
    def Baader_Classic_Ortho_3_5mm_v2(cls):
        return cls.from_database(cls._DATABASE["Baader_Classic_Ortho_3_5mm_v2"])

    @classmethod
    def Baader_Classic_Ortho_5mm_v2(cls):
        return cls.from_database(cls._DATABASE["Baader_Classic_Ortho_5mm_v2"])

    @classmethod
    def Baader_Classic_Ortho_7mm_v2(cls):
        return cls.from_database(cls._DATABASE["Baader_Classic_Ortho_7mm_v2"])

    @classmethod
    def Baader_Classic_Ortho_12_5mm_v2(cls):
        return cls.from_database(cls._DATABASE["Baader_Classic_Ortho_12_5mm_v2"])

    @classmethod
    def Baader_Classic_Ortho_18mm_v2(cls):
        return cls.from_database(cls._DATABASE["Baader_Classic_Ortho_18mm_v2"])

    @classmethod
    def Baader_Classic_Ortho_25mm_v2(cls):
        return cls.from_database(cls._DATABASE["Baader_Classic_Ortho_25mm_v2"])

    @classmethod
    def Baader_Genuine_Ortho_4mm(cls):
        return cls.from_database(cls._DATABASE["Baader_Genuine_Ortho_4mm"])

    @classmethod
    def Baader_Genuine_Ortho_5mm(cls):
        return cls.from_database(cls._DATABASE["Baader_Genuine_Ortho_5mm"])

    @classmethod
    def Baader_Genuine_Ortho_6mm(cls):
        return cls.from_database(cls._DATABASE["Baader_Genuine_Ortho_6mm"])

    @classmethod
    def Baader_Genuine_Ortho_7mm(cls):
        return cls.from_database(cls._DATABASE["Baader_Genuine_Ortho_7mm"])

    @classmethod
    def Baader_Genuine_Ortho_9mm(cls):
        return cls.from_database(cls._DATABASE["Baader_Genuine_Ortho_9mm"])

    @classmethod
    def Baader_Genuine_Ortho_10mm(cls):
        return cls.from_database(cls._DATABASE["Baader_Genuine_Ortho_10mm"])

    @classmethod
    def Baader_Genuine_Ortho_12_5mm(cls):
        return cls.from_database(cls._DATABASE["Baader_Genuine_Ortho_12_5mm"])

    @classmethod
    def Baader_Genuine_Ortho_18mm(cls):
        return cls.from_database(cls._DATABASE["Baader_Genuine_Ortho_18mm"])

    @classmethod
    def Baader_Genuine_Ortho_25mm(cls):
        return cls.from_database(cls._DATABASE["Baader_Genuine_Ortho_25mm"])

    @classmethod
    def Pentax_XL_2_5mm(cls):
        return cls.from_database(cls._DATABASE["Pentax_XL_2_5mm"])

    @classmethod
    def Pentax_XL_5_2mm(cls):
        return cls.from_database(cls._DATABASE["Pentax_XL_5_2mm"])

    @classmethod
    def Pentax_XL_7mm(cls):
        return cls.from_database(cls._DATABASE["Pentax_XL_7mm"])

    @classmethod
    def Pentax_XL_10_5mm(cls):
        return cls.from_database(cls._DATABASE["Pentax_XL_10_5mm"])

    @classmethod
    def Pentax_XL_14mm(cls):
        return cls.from_database(cls._DATABASE["Pentax_XL_14mm"])

    @classmethod
    def Pentax_XL_21mm(cls):
        return cls.from_database(cls._DATABASE["Pentax_XL_21mm"])

    @classmethod
    def Pentax_XL_28mm(cls):
        return cls.from_database(cls._DATABASE["Pentax_XL_28mm"])

    @classmethod
    def Pentax_XL_40mm(cls):
        return cls.from_database(cls._DATABASE["Pentax_XL_40mm"])

    @classmethod
    def Pentax_XO_2_5mm(cls):
        return cls.from_database(cls._DATABASE["Pentax_XO_2_5mm"])

    @classmethod
    def Pentax_XO_5mm(cls):
        return cls.from_database(cls._DATABASE["Pentax_XO_5mm"])

    @classmethod
    def Pentax_XO_10mm(cls):
        return cls.from_database(cls._DATABASE["Pentax_XO_10mm"])

    @classmethod
    def Nikon_NAV_HW_7mm(cls):
        return cls.from_database(cls._DATABASE["Nikon_NAV_HW_7mm"])

    @classmethod
    def Nikon_NAV_HW_14mm(cls):
        return cls.from_database(cls._DATABASE["Nikon_NAV_HW_14mm"])

    @classmethod
    def Takahashi_TOE_2_5mm(cls):
        return cls.from_database(cls._DATABASE["Takahashi_TOE_2_5mm"])

    @classmethod
    def Takahashi_TOE_4mm(cls):
        return cls.from_database(cls._DATABASE["Takahashi_TOE_4mm"])

    @classmethod
    def Takahashi_TOE_6mm(cls):
        return cls.from_database(cls._DATABASE["Takahashi_TOE_6mm"])

    @classmethod
    def Takahashi_TOE_8mm(cls):
        return cls.from_database(cls._DATABASE["Takahashi_TOE_8mm"])

    @classmethod
    def Takahashi_TOE_10mm(cls):
        return cls.from_database(cls._DATABASE["Takahashi_TOE_10mm"])

    @classmethod
    def Takahashi_TOE_18mm(cls):
        return cls.from_database(cls._DATABASE["Takahashi_TOE_18mm"])

    @classmethod
    def Leica_ASPH_6_5mm_v2(cls):
        return cls.from_database(cls._DATABASE["Leica_ASPH_6_5mm_v2"])

    @classmethod
    def Leica_ASPH_12_5mm_v2(cls):
        return cls.from_database(cls._DATABASE["Leica_ASPH_12_5mm_v2"])

    @classmethod
    def Leica_ASPH_20mm_v2(cls):
        return cls.from_database(cls._DATABASE["Leica_ASPH_20mm_v2"])

    @classmethod
    def Siebert_Stellar_4mm(cls):
        return cls.from_database(cls._DATABASE["Siebert_Stellar_4mm"])

    @classmethod
    def Siebert_Stellar_6mm(cls):
        return cls.from_database(cls._DATABASE["Siebert_Stellar_6mm"])

    @classmethod
    def Siebert_Stellar_8mm(cls):
        return cls.from_database(cls._DATABASE["Siebert_Stellar_8mm"])

    @classmethod
    def Siebert_Stellar_10mm(cls):
        return cls.from_database(cls._DATABASE["Siebert_Stellar_10mm"])

    @classmethod
    def Siebert_Stellar_13mm(cls):
        return cls.from_database(cls._DATABASE["Siebert_Stellar_13mm"])

    @classmethod
    def Siebert_Stellar_18mm(cls):
        return cls.from_database(cls._DATABASE["Siebert_Stellar_18mm"])

    @classmethod
    def Siebert_Stellar_24mm(cls):
        return cls.from_database(cls._DATABASE["Siebert_Stellar_24mm"])

    @classmethod
    def Siebert_Stellar_36mm(cls):
        return cls.from_database(cls._DATABASE["Siebert_Stellar_36mm"])

    @classmethod
    def TMB_Super_Mono_2_5mm(cls):
        return cls.from_database(cls._DATABASE["TMB_Super_Mono_2_5mm"])

    @classmethod
    def TMB_Super_Mono_3_2mm(cls):
        return cls.from_database(cls._DATABASE["TMB_Super_Mono_3_2mm"])

    @classmethod
    def TMB_Super_Mono_4mm(cls):
        return cls.from_database(cls._DATABASE["TMB_Super_Mono_4mm"])

    @classmethod
    def TMB_Super_Mono_5mm(cls):
        return cls.from_database(cls._DATABASE["TMB_Super_Mono_5mm"])

    @classmethod
    def TMB_Super_Mono_6mm(cls):
        return cls.from_database(cls._DATABASE["TMB_Super_Mono_6mm"])

    @classmethod
    def TMB_Super_Mono_7mm(cls):
        return cls.from_database(cls._DATABASE["TMB_Super_Mono_7mm"])

    @classmethod
    def TMB_Super_Mono_8mm(cls):
        return cls.from_database(cls._DATABASE["TMB_Super_Mono_8mm"])

    @classmethod
    def TMB_Super_Mono_9mm(cls):
        return cls.from_database(cls._DATABASE["TMB_Super_Mono_9mm"])

    @classmethod
    def TMB_Super_Mono_10mm(cls):
        return cls.from_database(cls._DATABASE["TMB_Super_Mono_10mm"])

    @classmethod
    def TMB_Super_Mono_12_5mm(cls):
        return cls.from_database(cls._DATABASE["TMB_Super_Mono_12_5mm"])

    @classmethod
    def TMB_Super_Mono_16mm(cls):
        return cls.from_database(cls._DATABASE["TMB_Super_Mono_16mm"])

    @classmethod
    def TMB_Super_Mono_20mm(cls):
        return cls.from_database(cls._DATABASE["TMB_Super_Mono_20mm"])

    @classmethod
    def TMB_Super_Mono_25mm(cls):
        return cls.from_database(cls._DATABASE["TMB_Super_Mono_25mm"])

    @classmethod
    def Antares_W70_5mm(cls):
        return cls.from_database(cls._DATABASE["Antares_W70_5mm"])

    @classmethod
    def Antares_W70_8mm(cls):
        return cls.from_database(cls._DATABASE["Antares_W70_8mm"])

    @classmethod
    def Antares_W70_12mm(cls):
        return cls.from_database(cls._DATABASE["Antares_W70_12mm"])

    @classmethod
    def Antares_W70_18mm(cls):
        return cls.from_database(cls._DATABASE["Antares_W70_18mm"])

    @classmethod
    def Antares_W70_25mm(cls):
        return cls.from_database(cls._DATABASE["Antares_W70_25mm"])

    @classmethod
    def Antares_W70_32mm(cls):
        return cls.from_database(cls._DATABASE["Antares_W70_32mm"])

    @classmethod
    def Astro_Tech_EF_4_5mm_70(cls):
        return cls.from_database(cls._DATABASE["Astro_Tech_EF_4_5mm_70"])

    @classmethod
    def Astro_Tech_EF_6_5mm_70(cls):
        return cls.from_database(cls._DATABASE["Astro_Tech_EF_6_5mm_70"])

    @classmethod
    def Astro_Tech_EF_8_5mm_70(cls):
        return cls.from_database(cls._DATABASE["Astro_Tech_EF_8_5mm_70"])

    @classmethod
    def Astro_Tech_EF_11mm_70(cls):
        return cls.from_database(cls._DATABASE["Astro_Tech_EF_11mm_70"])

    @classmethod
    def Astro_Tech_EF_14mm_70(cls):
        return cls.from_database(cls._DATABASE["Astro_Tech_EF_14mm_70"])

    @classmethod
    def Astro_Tech_EF_18mm_70(cls):
        return cls.from_database(cls._DATABASE["Astro_Tech_EF_18mm_70"])

    @classmethod
    def Astro_Tech_EF_24mm_70(cls):
        return cls.from_database(cls._DATABASE["Astro_Tech_EF_24mm_70"])

    @classmethod
    def Astro_Tech_EF_30mm_70(cls):
        return cls.from_database(cls._DATABASE["Astro_Tech_EF_30mm_70"])

    @classmethod
    def Lunt_Solar_Solar_7_5mm(cls):
        return cls.from_database(cls._DATABASE["Lunt_Solar_Solar_7_5mm"])

    @classmethod
    def Lunt_Solar_Solar_10mm(cls):
        return cls.from_database(cls._DATABASE["Lunt_Solar_Solar_10mm"])

    @classmethod
    def Lunt_Solar_Solar_12mm(cls):
        return cls.from_database(cls._DATABASE["Lunt_Solar_Solar_12mm"])

    @classmethod
    def Lunt_Solar_Solar_16mm(cls):
        return cls.from_database(cls._DATABASE["Lunt_Solar_Solar_16mm"])

    @classmethod
    def Lunt_Solar_Solar_19mm(cls):
        return cls.from_database(cls._DATABASE["Lunt_Solar_Solar_19mm"])

    @classmethod
    def Lunt_Solar_Solar_25mm(cls):
        return cls.from_database(cls._DATABASE["Lunt_Solar_Solar_25mm"])

    @classmethod
    def Lunt_Solar_Solar_32mm(cls):
        return cls.from_database(cls._DATABASE["Lunt_Solar_Solar_32mm"])

    @classmethod
    def Agena_Starguider_Plossl_6mm(cls):
        return cls.from_database(cls._DATABASE["Agena_Starguider_Plossl_6mm"])

    @classmethod
    def Agena_Starguider_Plossl_8mm(cls):
        return cls.from_database(cls._DATABASE["Agena_Starguider_Plossl_8mm"])

    @classmethod
    def Agena_Starguider_Plossl_10mm(cls):
        return cls.from_database(cls._DATABASE["Agena_Starguider_Plossl_10mm"])

    @classmethod
    def Agena_Starguider_Plossl_12_5mm(cls):
        return cls.from_database(cls._DATABASE["Agena_Starguider_Plossl_12_5mm"])

    @classmethod
    def Agena_Starguider_Plossl_15mm(cls):
        return cls.from_database(cls._DATABASE["Agena_Starguider_Plossl_15mm"])

    @classmethod
    def Agena_Starguider_Plossl_20mm(cls):
        return cls.from_database(cls._DATABASE["Agena_Starguider_Plossl_20mm"])

    @classmethod
    def Agena_Starguider_Plossl_25mm(cls):
        return cls.from_database(cls._DATABASE["Agena_Starguider_Plossl_25mm"])

    @classmethod
    def Agena_Starguider_Plossl_32mm(cls):
        return cls.from_database(cls._DATABASE["Agena_Starguider_Plossl_32mm"])

    @classmethod
    def Agena_Starguider_Plossl_40mm(cls):
        return cls.from_database(cls._DATABASE["Agena_Starguider_Plossl_40mm"])

    @classmethod
    def Stellarvue_Optimus_Wide_5mm(cls):
        return cls.from_database(cls._DATABASE["Stellarvue_Optimus_Wide_5mm"])

    @classmethod
    def Stellarvue_Optimus_Wide_8mm(cls):
        return cls.from_database(cls._DATABASE["Stellarvue_Optimus_Wide_8mm"])

    @classmethod
    def Stellarvue_Optimus_Wide_12mm(cls):
        return cls.from_database(cls._DATABASE["Stellarvue_Optimus_Wide_12mm"])

    @classmethod
    def Stellarvue_Optimus_Wide_16mm(cls):
        return cls.from_database(cls._DATABASE["Stellarvue_Optimus_Wide_16mm"])

    @classmethod
    def Stellarvue_Optimus_Wide_22mm(cls):
        return cls.from_database(cls._DATABASE["Stellarvue_Optimus_Wide_22mm"])

    @classmethod
    def Stellarvue_Optimus_Wide_32mm(cls):
        return cls.from_database(cls._DATABASE["Stellarvue_Optimus_Wide_32mm"])

    @classmethod
    def William_Optics_XWA_3_5mm_110(cls):
        return cls.from_database(cls._DATABASE["William_Optics_XWA_3_5mm_110"])

    @classmethod
    def William_Optics_XWA_7mm_110(cls):
        return cls.from_database(cls._DATABASE["William_Optics_XWA_7mm_110"])

    @classmethod
    def William_Optics_XWA_13mm_110(cls):
        return cls.from_database(cls._DATABASE["William_Optics_XWA_13mm_110"])

    @classmethod
    def William_Optics_XWA_20mm_110(cls):
        return cls.from_database(cls._DATABASE["William_Optics_XWA_20mm_110"])

    @classmethod
    def Orion_Epic_ED_2_5mm(cls):
        return cls.from_database(cls._DATABASE["Orion_Epic_ED_2_5mm"])

    @classmethod
    def Orion_Epic_ED_2_7mm(cls):
        return cls.from_database(cls._DATABASE["Orion_Epic_ED_2_7mm"])

    @classmethod
    def Orion_Epic_ED_2_10mm(cls):
        return cls.from_database(cls._DATABASE["Orion_Epic_ED_2_10mm"])

    @classmethod
    def Orion_Epic_ED_2_15mm(cls):
        return cls.from_database(cls._DATABASE["Orion_Epic_ED_2_15mm"])

    @classmethod
    def Orion_Epic_ED_2_20mm(cls):
        return cls.from_database(cls._DATABASE["Orion_Epic_ED_2_20mm"])

    @classmethod
    def Orion_Epic_ED_2_25mm(cls):
        return cls.from_database(cls._DATABASE["Orion_Epic_ED_2_25mm"])

    @classmethod
    def Orion_UltraView_5mm(cls):
        return cls.from_database(cls._DATABASE["Orion_UltraView_5mm"])

    @classmethod
    def Orion_UltraView_10mm(cls):
        return cls.from_database(cls._DATABASE["Orion_UltraView_10mm"])

    @classmethod
    def Orion_UltraView_15mm(cls):
        return cls.from_database(cls._DATABASE["Orion_UltraView_15mm"])

    @classmethod
    def Orion_UltraView_20mm(cls):
        return cls.from_database(cls._DATABASE["Orion_UltraView_20mm"])

    @classmethod
    def Orion_UltraView_25mm(cls):
        return cls.from_database(cls._DATABASE["Orion_UltraView_25mm"])

    @classmethod
    def Orion_UltraView_35mm(cls):
        return cls.from_database(cls._DATABASE["Orion_UltraView_35mm"])

    @classmethod
    def Meade_HD_60_8_5mm_60(cls):
        return cls.from_database(cls._DATABASE["Meade_HD_60_8_5mm_60"])

    @classmethod
    def Meade_HD_60_12mm_60(cls):
        return cls.from_database(cls._DATABASE["Meade_HD_60_12mm_60"])

    @classmethod
    def Meade_HD_60_16mm_60(cls):
        return cls.from_database(cls._DATABASE["Meade_HD_60_16mm_60"])

    @classmethod
    def Meade_HD_60_20mm_60(cls):
        return cls.from_database(cls._DATABASE["Meade_HD_60_20mm_60"])

    @classmethod
    def Meade_HD_60_28mm_60(cls):
        return cls.from_database(cls._DATABASE["Meade_HD_60_28mm_60"])

    @classmethod
    def Omegon_Flatfield_4mm_65(cls):
        return cls.from_database(cls._DATABASE["Omegon_Flatfield_4mm_65"])

    @classmethod
    def Omegon_Flatfield_6mm_65(cls):
        return cls.from_database(cls._DATABASE["Omegon_Flatfield_6mm_65"])

    @classmethod
    def Omegon_Flatfield_8mm_65(cls):
        return cls.from_database(cls._DATABASE["Omegon_Flatfield_8mm_65"])

    @classmethod
    def Omegon_Flatfield_10mm_65(cls):
        return cls.from_database(cls._DATABASE["Omegon_Flatfield_10mm_65"])

    @classmethod
    def Omegon_Flatfield_13mm_65(cls):
        return cls.from_database(cls._DATABASE["Omegon_Flatfield_13mm_65"])

    @classmethod
    def Omegon_Flatfield_16mm_65(cls):
        return cls.from_database(cls._DATABASE["Omegon_Flatfield_16mm_65"])

    @classmethod
    def Omegon_Flatfield_19mm_65(cls):
        return cls.from_database(cls._DATABASE["Omegon_Flatfield_19mm_65"])

    @classmethod
    def Omegon_Flatfield_24mm_65(cls):
        return cls.from_database(cls._DATABASE["Omegon_Flatfield_24mm_65"])

    @classmethod
    def Omegon_Flatfield_32mm_65(cls):
        return cls.from_database(cls._DATABASE["Omegon_Flatfield_32mm_65"])

    @classmethod
    def Bresser_Wide_Field_4mm(cls):
        return cls.from_database(cls._DATABASE["Bresser_Wide_Field_4mm"])

    @classmethod
    def Bresser_Wide_Field_6mm(cls):
        return cls.from_database(cls._DATABASE["Bresser_Wide_Field_6mm"])

    @classmethod
    def Bresser_Wide_Field_8mm(cls):
        return cls.from_database(cls._DATABASE["Bresser_Wide_Field_8mm"])

    @classmethod
    def Bresser_Wide_Field_11mm(cls):
        return cls.from_database(cls._DATABASE["Bresser_Wide_Field_11mm"])

    @classmethod
    def Bresser_Wide_Field_14mm(cls):
        return cls.from_database(cls._DATABASE["Bresser_Wide_Field_14mm"])

    @classmethod
    def Bresser_Wide_Field_18mm(cls):
        return cls.from_database(cls._DATABASE["Bresser_Wide_Field_18mm"])

    @classmethod
    def Bresser_Wide_Field_23mm(cls):
        return cls.from_database(cls._DATABASE["Bresser_Wide_Field_23mm"])

    @classmethod
    def Bresser_Wide_Field_28mm(cls):
        return cls.from_database(cls._DATABASE["Bresser_Wide_Field_28mm"])

    @classmethod
    def Celestron_Ultima_Duo_6mm_v2(cls):
        return cls.from_database(cls._DATABASE["Celestron_Ultima_Duo_6mm_v2"])

    @classmethod
    def Celestron_Ultima_Duo_8mm_v2(cls):
        return cls.from_database(cls._DATABASE["Celestron_Ultima_Duo_8mm_v2"])

    @classmethod
    def Celestron_Ultima_Duo_10mm_v2(cls):
        return cls.from_database(cls._DATABASE["Celestron_Ultima_Duo_10mm_v2"])

    @classmethod
    def Celestron_Ultima_Duo_12mm_v2(cls):
        return cls.from_database(cls._DATABASE["Celestron_Ultima_Duo_12mm_v2"])

    @classmethod
    def Celestron_Ultima_Duo_15mm_v2(cls):
        return cls.from_database(cls._DATABASE["Celestron_Ultima_Duo_15mm_v2"])

    @classmethod
    def Celestron_Ultima_Duo_20mm_v2(cls):
        return cls.from_database(cls._DATABASE["Celestron_Ultima_Duo_20mm_v2"])

    @classmethod
    def Celestron_Ultima_Duo_25mm_v2(cls):
        return cls.from_database(cls._DATABASE["Celestron_Ultima_Duo_25mm_v2"])

    @classmethod
    def TS_Optics_SuperFlat_4mm(cls):
        return cls.from_database(cls._DATABASE["TS_Optics_SuperFlat_4mm"])

    @classmethod
    def TS_Optics_SuperFlat_6mm(cls):
        return cls.from_database(cls._DATABASE["TS_Optics_SuperFlat_6mm"])

    @classmethod
    def TS_Optics_SuperFlat_8mm(cls):
        return cls.from_database(cls._DATABASE["TS_Optics_SuperFlat_8mm"])

    @classmethod
    def TS_Optics_SuperFlat_10mm(cls):
        return cls.from_database(cls._DATABASE["TS_Optics_SuperFlat_10mm"])

    @classmethod
    def TS_Optics_SuperFlat_13mm(cls):
        return cls.from_database(cls._DATABASE["TS_Optics_SuperFlat_13mm"])

    @classmethod
    def TS_Optics_SuperFlat_16mm(cls):
        return cls.from_database(cls._DATABASE["TS_Optics_SuperFlat_16mm"])

    @classmethod
    def TS_Optics_SuperFlat_22mm(cls):
        return cls.from_database(cls._DATABASE["TS_Optics_SuperFlat_22mm"])

    @classmethod
    def TS_Optics_SuperFlat_30mm(cls):
        return cls.from_database(cls._DATABASE["TS_Optics_SuperFlat_30mm"])

    @classmethod
    def SVBony_SV215_UWA_4mm(cls):
        return cls.from_database(cls._DATABASE["SVBony_SV215_UWA_4mm"])

    @classmethod
    def SVBony_SV215_UWA_6mm(cls):
        return cls.from_database(cls._DATABASE["SVBony_SV215_UWA_6mm"])

    @classmethod
    def SVBony_SV215_UWA_8mm(cls):
        return cls.from_database(cls._DATABASE["SVBony_SV215_UWA_8mm"])

    @classmethod
    def SVBony_SV215_UWA_10mm(cls):
        return cls.from_database(cls._DATABASE["SVBony_SV215_UWA_10mm"])

    @classmethod
    def SVBony_SV215_UWA_13mm(cls):
        return cls.from_database(cls._DATABASE["SVBony_SV215_UWA_13mm"])

    @classmethod
    def SVBony_SV215_UWA_16mm(cls):
        return cls.from_database(cls._DATABASE["SVBony_SV215_UWA_16mm"])

    @classmethod
    def SVBony_SV215_UWA_20mm(cls):
        return cls.from_database(cls._DATABASE["SVBony_SV215_UWA_20mm"])

    @classmethod
    def GSO_SuperPlossl_4mm(cls):
        return cls.from_database(cls._DATABASE["GSO_SuperPlossl_4mm"])

    @classmethod
    def GSO_SuperPlossl_5mm(cls):
        return cls.from_database(cls._DATABASE["GSO_SuperPlossl_5mm"])

    @classmethod
    def GSO_SuperPlossl_7_5mm(cls):
        return cls.from_database(cls._DATABASE["GSO_SuperPlossl_7_5mm"])

    @classmethod
    def GSO_SuperPlossl_9_7mm(cls):
        return cls.from_database(cls._DATABASE["GSO_SuperPlossl_9_7mm"])

    @classmethod
    def GSO_SuperPlossl_12_5mm(cls):
        return cls.from_database(cls._DATABASE["GSO_SuperPlossl_12_5mm"])

    @classmethod
    def GSO_SuperPlossl_15mm(cls):
        return cls.from_database(cls._DATABASE["GSO_SuperPlossl_15mm"])

    @classmethod
    def GSO_SuperPlossl_17mm(cls):
        return cls.from_database(cls._DATABASE["GSO_SuperPlossl_17mm"])

    @classmethod
    def GSO_SuperPlossl_20mm(cls):
        return cls.from_database(cls._DATABASE["GSO_SuperPlossl_20mm"])

    @classmethod
    def GSO_SuperPlossl_25mm(cls):
        return cls.from_database(cls._DATABASE["GSO_SuperPlossl_25mm"])

    @classmethod
    def GSO_SuperPlossl_30mm(cls):
        return cls.from_database(cls._DATABASE["GSO_SuperPlossl_30mm"])

    @classmethod
    def GSO_SuperPlossl_40mm(cls):
        return cls.from_database(cls._DATABASE["GSO_SuperPlossl_40mm"])

    @classmethod
    def Vixen_HR_1_6mm(cls):
        return cls.from_database(cls._DATABASE["Vixen_HR_1_6mm"])

    @classmethod
    def Vixen_HR_2mm(cls):
        return cls.from_database(cls._DATABASE["Vixen_HR_2mm"])

    @classmethod
    def Vixen_HR_2_4mm(cls):
        return cls.from_database(cls._DATABASE["Vixen_HR_2_4mm"])

    @classmethod
    def Vixen_HR_3_4mm(cls):
        return cls.from_database(cls._DATABASE["Vixen_HR_3_4mm"])

    @classmethod
    def Celestron_12mm_Reticle_Eyepiece_1_25(cls):
        return cls.from_database(cls._DATABASE["Celestron_12mm_Reticle_Eyepiece_1_25"])

    @classmethod
    def Meade_12mm_Reticle_Eyepiece_1_25(cls):
        return cls.from_database(cls._DATABASE["Meade_12mm_Reticle_Eyepiece_1_25"])

    @classmethod
    def Orion_12mm_Reticle_Eyepiece_1_25(cls):
        return cls.from_database(cls._DATABASE["Orion_12mm_Reticle_Eyepiece_1_25"])

    @classmethod
    def Sky_Watcher_12mm_Reticle_Eyepiece_1_25(cls):
        return cls.from_database(
            cls._DATABASE["Sky_Watcher_12mm_Reticle_Eyepiece_1_25"]
        )

    @classmethod
    def Baader_Micro_Guide_Eyepiece_12_5mm(cls):
        return cls.from_database(cls._DATABASE["Baader_Micro_Guide_Eyepiece_12_5mm"])

    @classmethod
    def TeleVue_Starbeam_1_25(cls):
        return cls.from_database(cls._DATABASE["TeleVue_Starbeam_1_25"])
