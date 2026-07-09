from typing import Any, Optional, cast

import numpy

from .enums import TelescopeType, TubeMaterial
from ...constants import GraphConstants
from ...optics.calculations import telescope as telescope_calc
from ...units import get_unit_registry
from ...utils import ConnectionType
from ..base import OpticalEquipment


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
        from ...utils import guess_optical_properties, map_conn, map_gender

        brand = entry["brand"]
        name = entry["name"]
        vendor = f"{brand} {name}"
        ol = entry.get("optical_length", 0)
        mass = entry.get("mass", 0)
        ct = map_conn(entry.get("cside_thread"))
        cg = map_gender(entry.get("cside_gender"))

        # Use explicit aperture and focal length if available, otherwise guess
        aperture = entry.get("aperture_mm")
        focal_length = entry.get("focal_length_mm")
        if aperture is None or focal_length is None:
            g_aperture, g_focal_length = guess_optical_properties(name)
            aperture = aperture or g_aperture
            focal_length = focal_length or g_focal_length

        central_obstruction = entry.get("central_obstruction_mm", 0)

        # Map type string to TelescopeType enum
        type_str = entry.get("type", "")
        telescope_type = TelescopeType.REFRACTOR  # Default
        if "refractor" in type_str:
            telescope_type = TelescopeType.REFRACTOR
        elif "newtonian" in type_str:
            telescope_type = TelescopeType.NEWTONIAN_REFLECTOR
        elif "schmidt_cassegrain" in type_str or "sct" in type_str:
            telescope_type = TelescopeType.SCHMIDT_CASSEGRAIN
        elif "maksutov" in type_str:
            telescope_type = TelescopeType.MAKSUTOV_CASSEGRAIN
        elif "catadioptric" in type_str or "astrograph" in type_str:
            telescope_type = TelescopeType.CATADIOPTRIC

        bf_val = entry.get("bf_role") == "start"

        outputs = entry.get("outputs")
        if outputs is None:
            outputs = [(ct, cg)] if ct else []
            if entry.get("t2_output", False):
                from ...utils import Gender

                outputs.append((ConnectionType.T2, Gender.MALE))
        else:
            from ...utils import map_conn, map_gender

            outputs = [
                (map_conn(c), map_gender(g)) if isinstance(c, str) else (c, g)
                for c, g in outputs
            ]

        # Optimization: remove t2_output check in a future version after all databases are updated.
        # For now, it's safer to keep it for items that might not have migrated to 'outputs' list.

        return cls(
            aperture or 80,
            focal_length or 500,
            vendor=vendor,
            outputs=outputs,
            backfocus=ol if bf_val else None,
            mass=mass,
            optical_length=ol,
            telescope_type=telescope_type,
            central_obstruction=central_obstruction,
        )

    "\n    Class representing telescope\n    "

    def __init__(
        self,
        aperture,
        focal_length,
        vendor="unknown telescope",
        outputs=None,
        telescope_type: Optional[TelescopeType] = TelescopeType.REFRACTOR,
        focuser_step_size=None,
        tube_material: Optional[TubeMaterial] = TubeMaterial.ALUMINUM,
        backfocus=None,
        mass=0.0,
        optical_length=0.0,
        central_obstruction=0.0,
        connection_type=None,
        connection_gender=None,
    ):
        if outputs is None:
            if connection_type:
                outputs = [(connection_type, connection_gender)]
            else:
                outputs = [ConnectionType.F_1_25]

        super(Telescope, self).__init__(
            focal_length,
            vendor,
            mass=mass,
            optical_length=optical_length,
            outputs=outputs,
        )
        self.aperture = cast(Any, aperture * get_unit_registry().mm)
        self.central_obstruction = cast(
            Any, central_obstruction * get_unit_registry().mm
        )
        self.telescope_type = telescope_type
        self.focuser_step_size = focuser_step_size
        self.tube_material = tube_material
        self.backfocus = (
            cast(Any, backfocus * get_unit_registry().mm)
            if backfocus is not None
            else None
        )

    @property
    def connection_type(self):
        return self._outputs[0][0] if self._outputs else None

    @property
    def connection_gender(self):
        return self._outputs[0][1] if self._outputs else None

    def focal_ratio(self):
        return self.focal_length / self.aperture

    def aperture_area(self):
        """
        Calculate the light gathering area of the telescope, accounting for central obstruction.
        :return: area in mm^2
        """
        return numpy.pi * (self.aperture**2 - self.central_obstruction**2) / 4.0

    def effective_aperture(self):
        """
        Return the diameter of a clear aperture that would have the same light-gathering area.
        :return: effective aperture in mm
        """
        return numpy.sqrt(self.aperture**2 - self.central_obstruction**2)

    def dawes_limit(self):
        """
        Calculate the maximum resolving power of your telescope using the Dawes' Limit formula.
        https://en.wikipedia.org/wiki/Dawes%27_limit
        :return: limit in arcsecond
        """
        aperture_mm = self.aperture.to("mm").magnitude
        return telescope_calc.calculate_dawes_limit(aperture_mm) * get_unit_registry().arcsecond

    def rayleigh_limit(self, wavelength_nm: float | int = 550):
        """
        Calculate the maximum resolving power of your telescope using the Rayleigh Limit formula.
        θ = 1.22 * λ / D
        Where λ is the wavelength and D is the aperture.
        https://en.wikipedia.org/wiki/Angular_resolution
        :param wavelength_nm: wavelength in nanometers (default 550nm for green light)
        :return: limit in arcsecond
        """
        aperture_mm = self.aperture.to("mm").magnitude
        return telescope_calc.calculate_rayleigh_limit(aperture_mm, wavelength_nm) * get_unit_registry().arcsecond

    def limiting_magnitude(self):
        """
        Calculate a telescopes approximate limiting magnitude.
        Uses effective aperture diameter for better accuracy when central obstruction is present.
        :return: range in magnitude
        """
        aperture_mm = self.aperture.to("mm").magnitude
        central_obstruction_mm = self.central_obstruction.to("mm").magnitude
        return telescope_calc.calculate_limiting_magnitude(aperture_mm, central_obstruction_mm)

    def light_grasp_ratio(self, other_aperture):
        """
        Calculate the light grasp ratio between two telescopes.
        Uses effective aperture area for better accuracy when central obstruction is present.
        :param other_aperture: aperture in mm
        :return: ratio between telescope and other aperture
        """
        other_aperture *= get_unit_registry().mm
        return self.effective_aperture() ** 2 / other_aperture**2

    def highest_useful_magnification(self) -> float:
        """
        Calculate the theoretical highest useful magnification for the telescope.
        Rule of thumb: 2.0x aperture in mm (or 50x per inch of aperture).
        Above this limit, the image usually becomes blurry and loses contrast due to diffraction.
        Source: Sidgwick, J. B. (1971), "Amateur Astronomer's Handbook".
        """
        aperture_mm = self.aperture.to("mm").magnitude
        return telescope_calc.calculate_highest_useful_magnification(aperture_mm)

    def lowest_useful_magnification(self, pupil_diameter_mm: float = 7.0) -> float:
        """
        Calculate the theoretical lowest useful magnification for the telescope.
        Formula: aperture / pupil_diameter.
        Assuming a 7.0mm dark-adapted human eye pupil. Lower magnifications result
        in an exit pupil larger than the eye, wasting gathered light.
        Source: Sidgwick, J. B. (1971), "Amateur Astronomer's Handbook".
        """
        aperture_mm = self.aperture.to("mm").magnitude
        return telescope_calc.calculate_lowest_useful_magnification(aperture_mm, pupil_diameter_mm)

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
        return "{} {}/{}".format(
            self.get_vendor(),
            cast(Any, self.aperture).magnitude,
            cast(Any, self.focal_length).magnitude,
        )
