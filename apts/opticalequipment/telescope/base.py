import numpy
from ..abstract import OpticalEquipment
from ...units import get_unit_registry
from ...utils import ConnectionType, Gender
from ...constants import GraphConstants, astronomy
from enum import Enum
from typing import Optional, Any, cast

class TelescopeType(Enum):
    REFRACTOR = 'refractor'
    NEWTONIAN_REFLECTOR = 'newtonian_reflector'
    SCHMIDT_CASSEGRAIN = 'schmidt_cassegrain'
    MAKSUTOV_CASSEGRAIN = 'maksutov_cassegrain'
    CATADIOPTRIC = 'catadioptric'

class TubeMaterial(Enum):
    ALUMINUM = 2.31e-05
    CARBON_FIBER = 5e-07
    STEEL = 1.2e-05
    BRASS = 1.9e-05
    GLASS_FIBER = 8e-06

class Telescope(OpticalEquipment):
    path_layer = 1

    @classmethod
    def normalize_database_entry(cls, entry: dict) -> dict:
        from ...utils import guess_optical_properties
        entry = entry.copy()
        name = entry.get("name", "")
        if "aperture_mm" not in entry and "aperture" not in entry:
            aperture, focal_length = guess_optical_properties(name)
            if aperture:
                entry["aperture_mm"] = aperture
            if focal_length:
                entry["focal_length_mm"] = focal_length
        elif "focal_length_mm" not in entry and "focal_length" not in entry:
            _, focal_length = guess_optical_properties(name)
            if focal_length:
                entry["focal_length_mm"] = focal_length
        return super(Telescope, cls).normalize_database_entry(entry)

    _DATABASE = {}

    @classmethod
    def from_database(cls, entry):
        from ...utils import map_conn, map_gender, guess_optical_properties, Gender
        brand = entry['brand']
        name = entry['name']
        vendor = f'{brand} {name}'
        ol = entry.get('optical_length', 0)
        mass = entry.get('mass', 0)
        ct = map_conn(entry.get('cside_thread'))
        cg = map_gender(entry.get('cside_gender'))

        # Use explicit aperture and focal length if available, otherwise guess
        aperture = entry.get('aperture_mm')
        focal_length = entry.get('focal_length_mm')
        if aperture is None or focal_length is None:
            g_aperture, g_focal_length = guess_optical_properties(name)
            aperture = aperture or g_aperture
            focal_length = focal_length or g_focal_length

        central_obstruction = entry.get('central_obstruction_mm', 0)

        # Map type string to TelescopeType enum
        type_str = entry.get('type', '')
        telescope_type = TelescopeType.REFRACTOR  # Default
        if 'refractor' in type_str:
            telescope_type = TelescopeType.REFRACTOR
        elif 'newtonian' in type_str:
            telescope_type = TelescopeType.NEWTONIAN_REFLECTOR
        elif 'schmidt_cassegrain' in type_str or 'sct' in type_str:
            telescope_type = TelescopeType.SCHMIDT_CASSEGRAIN
        elif 'maksutov' in type_str:
            telescope_type = TelescopeType.MAKSUTOV_CASSEGRAIN
        elif 'catadioptric' in type_str or 'astrograph' in type_str:
            telescope_type = TelescopeType.CATADIOPTRIC

        bf_val = entry.get('bf_role') == 'start'
        return cls(aperture or 80, focal_length or 500, vendor=vendor, connection_type=ct, connection_gender=cg or Gender.FEMALE, backfocus=ol if bf_val else None, mass=mass, optical_length=ol, telescope_type=telescope_type, central_obstruction=central_obstruction)
    '\n    Class representing telescope\n    '

    def __init__(self, aperture, focal_length, vendor='unknown telescope', connection_type=ConnectionType.F_1_25, t2_output=False, telescope_type: Optional[TelescopeType]=TelescopeType.REFRACTOR, focuser_step_size=None, tube_material: Optional[TubeMaterial]=TubeMaterial.ALUMINUM, backfocus=None, mass=0.0, optical_length=0.0, connection_gender=Gender.FEMALE, central_obstruction=0.0):
        super(Telescope, self).__init__(focal_length, vendor, mass=mass, optical_length=optical_length)
        self.aperture = cast(Any, aperture * get_unit_registry().mm)
        self.central_obstruction = cast(Any, central_obstruction * get_unit_registry().mm)
        self.connection_type = connection_type
        self.connection_gender = connection_gender
        self.t2_output = t2_output
        self.telescope_type = telescope_type
        self.focuser_step_size = focuser_step_size
        self.tube_material = tube_material
        self.backfocus = cast(Any, backfocus * get_unit_registry().mm) if backfocus is not None else None

        self.add_output(self.connection_type, self.connection_gender)
        if self.t2_output:
            self.add_output(ConnectionType.T2, Gender.MALE)

    def focal_ratio(self):
        return self.focal_length / self.aperture

    def aperture_area(self):
        """
        Calculate the light gathering area of the telescope, accounting for central obstruction.
        :return: area in mm^2
        """
        return numpy.pi * (self.aperture ** 2 - self.central_obstruction ** 2) / 4.0

    def effective_aperture(self):
        """
        Return the diameter of a clear aperture that would have the same light-gathering area.
        :return: effective aperture in mm
        """
        return numpy.sqrt(self.aperture ** 2 - self.central_obstruction ** 2)

    def dawes_limit(self):
        """
        Calculate the maximum resolving power of your telescope using the Dawes' Limit formula.
        https://en.wikipedia.org/wiki/Dawes%27_limit
        :return: limit in arcsecond
        """
        return round((11.6 / self.aperture.to('cm')).magnitude, 3) * get_unit_registry().arcsecond

    def rayleigh_limit(self, wavelength_nm: float | int = 550):
        """
        Calculate the maximum resolving power of your telescope using the Rayleigh Limit formula.
        θ = 1.22 * λ / D
        Where λ is the wavelength and D is the aperture.
        https://en.wikipedia.org/wiki/Angular_resolution
        :param wavelength_nm: wavelength in nanometers (default 550nm for green light)
        :return: limit in arcsecond
        """
        wavelength_m = wavelength_nm * 1e-9
        aperture_m = self.aperture.to("m").magnitude
        limit_rad = 1.22 * wavelength_m / aperture_m
        limit_arcsec = limit_rad * astronomy.RAD_TO_ARCSEC
        return round(limit_arcsec, 3) * get_unit_registry().arcsecond

    def limiting_magnitude(self):
        """
        Calculate a telescopes approximate limiting magnitude.
        Uses effective aperture diameter for better accuracy when central obstruction is present.
        :return: range in magnitude
        """
        return 7.7 + 5 * numpy.log10(self.effective_aperture().to('cm').magnitude)

    def light_grasp_ratio(self, other_aperture):
        """
        Calculate the light grasp ratio between two telescopes.
        Uses effective aperture area for better accuracy when central obstruction is present.
        :param other_aperture: aperture in mm
        :return: ratio between telescope and other aperture
        """
        other_aperture *= get_unit_registry().mm
        return self.effective_aperture() ** 2 / other_aperture ** 2

    def highest_useful_magnification(self) -> float:
        """
        Calculate the theoretical highest useful magnification for the telescope.
        Rule of thumb: 2.0x aperture in mm (or 50x per inch of aperture).
        Above this limit, the image usually becomes blurry and loses contrast due to diffraction.
        Source: Sidgwick, J. B. (1971), "Amateur Astronomer's Handbook".
        """
        return float(self.aperture.magnitude * 2.0)

    def lowest_useful_magnification(self, pupil_diameter_mm: float = 7.0) -> float:
        """
        Calculate the theoretical lowest useful magnification for the telescope.
        Formula: aperture / pupil_diameter.
        Assuming a 7.0mm dark-adapted human eye pupil. Lower magnifications result
        in an exit pupil larger than the eye, wasting gathered light.
        Source: Sidgwick, J. B. (1971), "Amateur Astronomer's Handbook".
        """
        return float(self.aperture.magnitude / pupil_diameter_mm)

    def min_useful_zoom(self):
        """
        Returns the minimum useful magnification.
        """
        return self.lowest_useful_magnification()

    def max_useful_zoom(self):
        """
        Returns the maximum useful magnification.
        """
        return self.highest_useful_magnification()

    def register(self, equipment):
        """
        Register telescope in optical equipment graph. Telescope node is build out of two vertices:
        telescope node and its output. Telescope node is automatically connected with SPACE node.
        """
        super(Telescope, self).register(equipment)
        equipment.add_edge(GraphConstants.SPACE_ID, self.id())

    def __str__(self):
        return '{} {}/{}'.format(self.get_vendor(), cast(Any, self.aperture).magnitude, cast(Any, self.focal_length).magnitude)
