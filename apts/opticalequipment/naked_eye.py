from ..constants import OpticalType, GraphConstants
from ..units import get_unit_registry
from .abstract import OpticalEquipment

class NakedEye(OpticalEquipment):
    """
    Class representing the naked eye
    """

    def __init__(self, magnification=1, objective_diameter=7, vendor="Naked Eye", apparent_fov_deg=180, focal_length=1):
        super().__init__(focal_length=focal_length, vendor=vendor)

        self.magnification = magnification
        self.objective_diameter = objective_diameter * get_unit_registry().mm
        self.apparent_fov_deg = apparent_fov_deg * get_unit_registry().deg
        self._type = OpticalType.VISUAL

    def get_name(self):
        return "NakedEye"

    def __str__(self):
        return f"{self.vendor} {self.magnification}x{self.objective_diameter.to('mm').magnitude:.0f}"

    def fov(self):
        return self.apparent_fov_deg / self.magnification

    def exit_pupil(self):
        return self.objective_diameter / self.magnification

    def dawes_limit(self):
        return round((11.6 / self.objective_diameter.to('cm')).magnitude, 3) * get_unit_registry().arcsecond

    def rayleigh_limit(self):
        return round((13.8 / self.objective_diameter.to('cm')).magnitude, 3) * get_unit_registry().arcsecond

    def limiting_magnitude(self):
        import numpy
        return 7.7 + 5 * numpy.log10(self.objective_diameter.to('cm').magnitude)

    def brightness(self):
        return (self.exit_pupil().to('mm').magnitude / 7) ** 2 * 100

    def register(self, equipment):
        super()._register(equipment)
        equipment.add_edge(GraphConstants.SPACE_ID, self.id())
        equipment.add_edge(self.id(), GraphConstants.EYE_ID)

    def output_type(self):
        return OpticalType.VISUAL

    def max_useful_zoom(self):
        return self.magnification
