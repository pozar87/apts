from typing import Any, cast
from ..abstract import OutputOpticalEquipment
from ...constants import GraphConstants, OpticalType
from ...units import get_unit_registry
from ...utils import ConnectionType, Gender

class Eyepiece(OutputOpticalEquipment):
    @classmethod
    def normalize_database_entry(cls, entry: dict) -> dict:
        from ...utils import map_conn, map_gender, guess_optical_properties, extract_number
        import re
        entry = entry.copy()
        name = entry.get("name", "")
        if "focal_length_mm" not in entry and "focal_length" not in entry:
            focal_length = extract_number(name)
            if focal_length:
                entry["focal_length_mm"] = focal_length
        if "field_of_view_deg" not in entry and "field_of_view" not in entry:
            match = re.search(r"(\d+)°", name) or re.search(r"(\d+)\s*deg", name)
            if match:
                entry["field_of_view_deg"] = float(match.group(1))
        return super(Eyepiece, cls).normalize_database_entry(entry)

    _DATABASE = {}

    @classmethod
    def from_database(cls, entry):
        from ...utils import map_conn, map_gender, guess_optical_properties, extract_number
        entry = cls.normalize_database_entry(entry)
        brand = entry.get('brand', 'Unknown')
        name = entry.get('name', 'Unknown')
        vendor = f'{brand} {name}'
        tt = map_conn(entry.get('tside_thread'))
        tg = map_gender(entry.get('tside_gender'))
        fl = entry.get('focal_length_mm', 20)
        fov = entry.get('field_of_view_deg', 70)
        fs = entry.get('field_stop_mm')
        mass = entry.get('mass', 0)
        ol = entry.get('optical_length', 0)
        return cls(fl, vendor=vendor, field_of_view=fov, field_stop=fs, connection_type=tt, connection_gender=tg or Gender.MALE, mass=mass, optical_length=ol)

    '\n  Class representing ocular\n  '

    def __init__(self, focal_length, vendor='unknown ocular', field_of_view=70, field_stop=None, connection_type=ConnectionType.F_1_25, connection_gender=Gender.MALE, mass=0.0, optical_length=0.0):
        super().__init__(focal_length, vendor, mass=mass, optical_length=optical_length)
        self._connection_type = connection_type
        self._connection_gender = connection_gender
        self._field_of_view = cast(Any, field_of_view * get_unit_registry().deg)
        self.field_stop = cast(Any, field_stop * get_unit_registry().mm) if field_stop is not None else None

    def _zoom_divider(self):
        return self.focal_length

    def field_of_view(self, telescope, zoom, barlow_magnification):
        """
        Calculates true field of view (TFoV).
        If field stop diameter is available, it uses the accurate formula:
        TFoV = 2 * atan(field_stop / (2 * focal_length_eff))
        Otherwise, it falls back to the Apparent Field of View (AFoV) formula:
        TFoV = AFoV / magnification
        """
        if self.field_stop is not None:
            import numpy
            f_eff = (telescope.focal_length * barlow_magnification).to('mm').magnitude
            fs = self.field_stop.to('mm').magnitude
            if f_eff > 0:
                return 2 * numpy.degrees(numpy.arctan(fs / (2 * f_eff))) * get_unit_registry().deg

        return self._field_of_view / zoom

    def output_type(self):
        return OpticalType.VISUAL

    def register(self, equipment):
        """
        Register ocular in optical equipment graph. Ocular node is build out of two vertices:
        ocular node and its input. Ocular node is automatically connected with output IMAGE node.
        """
        super()._register(equipment)
        self._register_input(equipment, self._connection_type, self._connection_gender)
        equipment.add_edge(self.id(), GraphConstants.EYE_ID)

    def __str__(self):
        return '{} f={}'.format(self.get_vendor(), self.focal_length.magnitude)