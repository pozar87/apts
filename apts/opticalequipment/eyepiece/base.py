from typing import Any, cast
from ..base import OutputOpticalEquipment
from ...constants import GraphConstants, OpticalType
from ...units import get_unit_registry
from ...utils import ConnectionType
from ...optics.calculations import calculate_eyepiece_field_of_view
from .calculations import normalize_eyepiece_database_entry

class Eyepiece(OutputOpticalEquipment):
    path_layer = 5

    @classmethod
    def normalize_database_entry(cls, entry: dict) -> dict:
        entry = normalize_eyepiece_database_entry(entry)
        return super(Eyepiece, cls).normalize_database_entry(entry)

    _DATABASE = {}

    @classmethod
    def from_database(cls, entry):
        entry = cls.normalize_database_entry(entry)
        brand = entry.get('brand', 'Unknown')
        name = entry.get('name', 'Unknown')
        vendor = f'{brand} {name}'
        fl = entry.get('focal_length_mm', 20)
        fov = entry.get('field_of_view_deg', 70)
        fs = entry.get('field_stop_mm')
        mass = entry.get('mass', 0)
        ol = entry.get('optical_length', 0)
        inputs = entry.get('inputs')

        return cls(fl, vendor=vendor, field_of_view=fov, field_stop=fs, inputs=inputs, mass=mass, optical_length=ol)

    '\n  Class representing ocular\n  '

    def __init__(self, focal_length, vendor='unknown ocular', field_of_view=70, field_stop=None, inputs=None, mass=0.0, optical_length=0.0, connection_type=None, connection_gender=None):
        if inputs is None:
            if connection_type:
                inputs = [(connection_type, connection_gender)]
            else:
                inputs = [ConnectionType.F_1_25]

        if not isinstance(inputs, list):
            inputs = [inputs]
        super().__init__(focal_length, vendor, mass=mass, optical_length=optical_length, inputs=inputs)
        self._field_of_view = cast(Any, field_of_view * get_unit_registry().deg)
        self.field_stop = cast(Any, field_stop * get_unit_registry().mm) if field_stop is not None else None

    @property
    def connection_type(self):
        return self._inputs[0][0] if self._inputs else None

    @property
    def connection_gender(self):
        return self._inputs[0][1] if self._inputs else None

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
        field_stop_mm = self.field_stop.to('mm').magnitude if self.field_stop is not None else None
        apparent_fov_deg = self._field_of_view.to('deg').magnitude
        f_eff_mm = (telescope.focal_length * barlow_magnification).to('mm').magnitude
        zoom_magnitude = getattr(zoom, "magnitude", float(zoom))

        fov_deg = calculate_eyepiece_field_of_view(
            field_stop_mm=field_stop_mm,
            apparent_fov_deg=apparent_fov_deg,
            focal_length_eff_mm=f_eff_mm,
            zoom_magnitude=zoom_magnitude,
        )
        return fov_deg * get_unit_registry().deg

    def output_type(self):
        return OpticalType.VISUAL

    def register(self, equipment):
        """
        Register ocular in optical equipment graph. Ocular node is build out of two vertices:
        ocular node and its input. Ocular node is automatically connected with output IMAGE node.
        """
        super().register(equipment)
        equipment.add_edge(self.id(), GraphConstants.EYE_ID)

    def __str__(self):
        return '{} f={}'.format(self.get_vendor(), self.focal_length.magnitude)
