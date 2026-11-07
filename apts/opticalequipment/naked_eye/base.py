from typing import ClassVar

from ...constants import GraphConstants, OpticalType
from ...i18n import gettext_ as _
from ...units import get_unit_registry
from ..base import OutputOpticalEquipment
from .calculations import (
    calculate_naked_eye_brightness,
    calculate_naked_eye_dawes_limit,
    calculate_naked_eye_exit_pupil,
    calculate_naked_eye_fov,
    calculate_naked_eye_limiting_magnitude,
    calculate_naked_eye_rayleigh_limit,
    normalize_naked_eye_database_entry,
)


class NakedEye(OutputOpticalEquipment):
    """
    Class representing the naked eye
    """

    path_layer = 1
    _DATABASE: ClassVar[dict] = {}

    @classmethod
    def normalize_database_entry(cls, entry: dict) -> dict:
        norm_entry = normalize_naked_eye_database_entry(entry)
        return super().normalize_database_entry(norm_entry)

    @classmethod
    def from_database(cls, entry: dict):
        norm_entry = cls.normalize_database_entry(entry)
        return cls(
            magnification=norm_entry["magnification"],
            objective_diameter=norm_entry["objective_diameter"],
            vendor=norm_entry["vendor"],
            apparent_fov_deg=norm_entry["apparent_fov_deg"],
            focal_length=norm_entry["focal_length"],
        )

    def __init__(
        self,
        magnification=1,
        objective_diameter=7,
        vendor=None,
        apparent_fov_deg=180,
        focal_length=1,
    ):
        if vendor is None:
            vendor = "Naked Eye"
        super().__init__(focal_length=focal_length, vendor=vendor)

        self.magnification = magnification
        self.objective_diameter = objective_diameter * get_unit_registry().mm
        self.apparent_fov_deg = apparent_fov_deg * get_unit_registry().deg
        self._type = OpticalType.VISUAL

    def get_name(self):
        return _("Naked Eye")

    def __str__(self):
        return f"{self.get_vendor()} {self.magnification}x{self.objective_diameter.to('mm').magnitude:.0f}"  # pyright: ignore

    def field_of_view(self, telescope, zoom, barlow_magnification):
        return self.fov()

    def _zoom_divider(self):
        return self.focal_length

    def fov(self):
        afov_deg = self.apparent_fov_deg.to("deg").magnitude
        fov_deg = calculate_naked_eye_fov(afov_deg, self.magnification)
        return fov_deg * get_unit_registry().deg

    def exit_pupil(self, telescope=None, zoom=None):
        obj_mm = self.objective_diameter.to("mm").magnitude
        exit_pupil_mm = calculate_naked_eye_exit_pupil(obj_mm, self.magnification)
        return exit_pupil_mm * get_unit_registry().mm

    def dawes_limit(self):
        obj_cm = self.objective_diameter.to("cm").magnitude
        limit_arcsec = calculate_naked_eye_dawes_limit(obj_cm)
        return limit_arcsec * get_unit_registry().arcsecond

    def rayleigh_limit(self, wavelength_nm: float = 550):
        obj_cm = self.objective_diameter.to("cm").magnitude
        limit_arcsec = calculate_naked_eye_rayleigh_limit(
            obj_cm, wavelength_nm=wavelength_nm
        )
        return limit_arcsec * get_unit_registry().arcsecond

    def limiting_magnitude(self):
        obj_cm = self.objective_diameter.to("cm").magnitude
        return calculate_naked_eye_limiting_magnitude(obj_cm)

    def brightness(self, telescope=None, zoom=None):
        exit_pupil_mm = self.exit_pupil().to("mm").magnitude
        return calculate_naked_eye_brightness(exit_pupil_mm)

    def register(self, equipment):
        super()._register(equipment)
        equipment.add_edge(GraphConstants.SPACE_ID, self.id())
        equipment.add_edge(self.id(), GraphConstants.EYE_ID)

    def output_type(self):
        return OpticalType.VISUAL

    def max_useful_zoom(self):
        return self.magnification
