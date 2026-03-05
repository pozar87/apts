from typing import Any, cast
from ..abstract import OutputOpticalEqipment
from ...constants import GraphConstants, OpticalType
from ...units import get_unit_registry
from ...utils import ConnectionType, Gender

class Eyepiece(OutputOpticalEqipment):
    @classmethod 
    def normalize_database_entry(cls, entry: dict) -> dict: 
        from ...utils import Utils 
        import re 
        entry = entry.copy() 
        name = entry.get("name", "") 
        if "focal_length_mm" not in entry and "focal_length" not in entry: 
            focal_length = Utils.extract_number(name) 
            if focal_length: entry["focal_length_mm"] = focal_length 
        if "field_of_view_deg" not in entry and "field_of_view" not in entry: 
            match = re.search(r"(\d+)°", name) or re.search(r"(\d+)\s*deg", name) 
            if match: entry["field_of_view_deg"] = float(match.group(1)) 
        return entry 

    _DATABASE = {}

    @classmethod
    def from_database(cls, entry):
        from ...utils import Utils
        brand = entry['brand']
        name = entry['name']
        vendor = f'{brand} {name}'
        tt = Utils.map_conn(entry.get('tside_thread'))
        tg = Utils.map_gender(entry.get('tside_gender'))
        fl = Utils.extract_number(name) or 20
        return cls(fl, vendor=vendor, connection_type=tt, connection_gender=tg or Gender.MALE)

    '\n  Class representing ocular\n  '

    def __init__(self, focal_length, vendor='unknown ocular', field_of_view=70, connection_type=ConnectionType.F_1_25, connection_gender=Gender.MALE, mass=0, optical_length=0):
        super(Eyepiece, self).__init__(focal_length, vendor, mass=mass, optical_length=optical_length)
        self._connection_type = connection_type
        self._connection_gender = connection_gender
        self._field_of_view = cast(Any, field_of_view * get_unit_registry().deg)

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
        super(Eyepiece, self)._register(equipment)
        self._register_input(equipment, self._connection_type, self._connection_gender)
        equipment.add_edge(self.id(), GraphConstants.EYE_ID)

    def __str__(self):
        return '{} f={}'.format(self.get_vendor(), self.focal_length.magnitude)