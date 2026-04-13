import math
from typing import TYPE_CHECKING, Any, Optional, Union, cast

import numpy

if TYPE_CHECKING:
    from pint import Quantity

    from ..opticalequipment.abstract import OpticalEquipment, OutputOpticalEquipment
    from ..opticalequipment.smart_telescope import SmartTelescope

from ..constants import astronomy
from ..opticalequipment.binoculars import Binoculars
from ..opticalequipment.naked_eye import NakedEye
from ..units import get_unit_registry
from .utils import OpticsUtils
from .models.atmospheric import AtmosphericMixIn
from .models.photometry import PhotometryMixIn
from .models.exposure import ExposureMixIn
from .models.planetary import PlanetaryMixIn


class OpticalPath(
    AtmosphericMixIn, PhotometryMixIn, ExposureMixIn, PlanetaryMixIn
):
    """
    Class representing an optical path in a telescope setup.
    """

    def __init__(self, telescope, barlows, diagonals, filters, others, output=None):
        self.telescope = telescope
        self.barlows = barlows
        self.diagonals = diagonals
        self.filters = filters
        if output is None:
            # Handle 5-argument constructor calls for backward compatibility
            self.others = []
            self.output = others
        else:
            self.others = others
            self.output = output
        # Cache for expensive calculations
        self._cache = {}

    @classmethod
    def from_path(cls, path):
        telescope, barlows, diagonals, filters, others, output = OpticsUtils.expand(
            path
        )
        return cls(telescope, barlows, diagonals, filters, others, output)

    def zoom(self) -> "Quantity":
        if "zoom" not in self._cache:
            self._cache["zoom"] = OpticsUtils.compute_zoom(
                self.telescope, self.barlows, self.output
            )
        return self._cache["zoom"]

    def effective_barlow(self) -> float:
        if "effective_barlow" not in self._cache:
            self._cache["effective_barlow"] = float(
                OpticsUtils.barlows_multiplications(self.barlows)
            )
        return self._cache["effective_barlow"]

    def label(self) -> str:
        from ..opticalequipment.smart_telescope import SmartTelescope

        if isinstance(self.telescope, (Binoculars, NakedEye, SmartTelescope)):
            return str(self.telescope)
        return ", ".join(
            [str(self.telescope)]
            + [str(item) for item in self.barlows]
            + [str(item) for item in self.diagonals]
            + [str(item) for item in self.filters]
            + [str(item) for item in self.others]
            + [str(self.output)]
        )

    def length(self) -> int:
        from ..opticalequipment.smart_telescope import SmartTelescope

        # For binoculars, path is [Binoculars], expanded to (Binoculars, [], Binoculars)
        # So self.barlows is []. Length should be 1 for a direct binocular path.
        # Original: return 2 + len(self.barlows) (Telescope + Output + Barlows)
        if isinstance(self.telescope, (Binoculars, NakedEye, SmartTelescope)):
            return 1  # Just the binoculars itself
        return (
            2
            + len(self.barlows)
            + len(self.diagonals)
            + len(self.filters)
            + len(self.others)
        )

    def fov(self) -> "Quantity":
        return OpticsUtils.compute_field_of_view(
            self.telescope, self.barlows, self.output
        )

    def fov_width(self) -> "Quantity":
        return self.output.field_of_view_width(
            self.telescope, self.zoom(), self.effective_barlow()
        )

    def fov_height(self) -> "Quantity":
        return self.output.field_of_view_height(
            self.telescope, self.zoom(), self.effective_barlow()
        )

    def fov_diagonal(self) -> "Quantity":
        return self.output.field_of_view_diagonal(
            self.telescope, self.zoom(), self.effective_barlow()
        )

    def is_magnification_useful(self) -> bool:
        """
        Checks if the current magnification is within the theoretical useful range
        of the telescope. For non-visual outputs (cameras), it returns True.
        """
        from ..opticalequipment.telescope import Telescope

        if (
            not isinstance(self.telescope, Telescope)
            or not self.output.is_visual_output()
        ):
            return True

        zoom = self.zoom().magnitude
        return (
            self.telescope.lowest_useful_magnification()
            <= zoom
            <= self.telescope.highest_useful_magnification()
        )

    def elements(self) -> frozenset[Any]:
        """
        Return immutable set of elements - used for removing redundant optical paths
        """
        elements: set[Any] = set((self.telescope, self.output))
        elements |= set(self.barlows)
        elements |= set(self.diagonals)
        elements |= set(self.filters)
        elements |= set(self.others)
        return frozenset(elements)

    def component_list(self) -> list[Any]:
        """
        Return ordered list of all optical components in the path.
        """
        from ..opticalequipment.smart_telescope import SmartTelescope

        if isinstance(self.telescope, (Binoculars, NakedEye, SmartTelescope)):
            return [self.telescope]

        return (
            [self.telescope]
            + self.barlows
            + self.diagonals
            + self.filters
            + self.others
            + [self.output]
        )

    def total_mass(self) -> "Quantity":
        if "total_mass" in self._cache:
            return self._cache["total_mass"]

        from ..opticalequipment.abstract import OpticalEquipment

        all_equipment: set[OpticalEquipment] = set()
        for item in (
            [self.telescope]
            + self.barlows
            + self.diagonals
            + self.filters
            + self.others
            + [self.output]
        ):
            if hasattr(item, "collect_all_attached"):
                item.collect_all_attached(all_equipment)
            else:
                all_equipment.add(item)

        total = 0 * get_unit_registry().gram
        for eq in all_equipment:
            mass = getattr(eq, "mass", 0 * get_unit_registry().gram)
            if mass is not None:
                total += mass
        self._cache["total_mass"] = total
        return total

    def backfocus_gap(self) -> Optional["Quantity"]:
        """
        Calculates the remaining backfocus (gap) between the last component that
        requires a specific backfocus (like a Reducer or Flattener) and the current
        sensor position.

        Returns a Quantity (distance) or None if no backfocus requirement is defined.
        """
        # 1. Find the component that defines the required backfocus
        required_bf = None
        start_index = -1

        # Flatten path for searching
        path = (
            [self.telescope]
            + self.barlows
            + self.diagonals
            + self.filters
            + self.others
            + [self.output]
        )

        for i, item in enumerate(path):
            # Check if component has required_backfocus (Reducer, Flattener, etc.)
            if (
                hasattr(item, "required_backfocus")
                and item.required_backfocus is not None
            ):
                required_bf = item.required_backfocus
                start_index = i
            # For telescopes, 'backfocus' property can also mean required backfocus from flange
            elif i == 0 and hasattr(item, "backfocus") and item.backfocus is not None:
                required_bf = item.backfocus
                start_index = i

        if required_bf is None:
            return None

        # 2. Calculate actual distance from that component's output to the sensor
        actual_distance = 0 * get_unit_registry().mm
        # Sum optical lengths of everything between start and end
        for item in path[start_index + 1 : -1]:
            item_ol = getattr(item, "optical_length", 0 * get_unit_registry().mm)
            if item_ol is not None:
                actual_distance += item_ol

        # 3. Add the output component's backfocus contribution (e.g. sensor depth)
        if hasattr(self.output, "backfocus") and self.output.backfocus is not None:
            actual_distance += self.output.backfocus

        return required_bf - actual_distance

    def get_image_orientation(self):
        from ..opticalequipment.telescope import Telescope

        if not isinstance(self.telescope, Telescope):
            return (False, False)

        # Start with the telescope's inversion (1 horizontal + 1 vertical flip)
        flipped_horizontally = True
        flipped_vertically = True

        # Diagonals are typically used with Refractors and Catadioptrics,
        # and their effect depends on the telescope type.
        for diagonal in self.diagonals:
            if diagonal.is_erecting:
                # Erecting diagonal adds 1 horizontal and 1 vertical flip
                flipped_horizontally = not flipped_horizontally
                flipped_vertically = not flipped_vertically
            else:
                # Standard star diagonal adds 1 vertical flip
                flipped_vertically = not flipped_vertically

        return (flipped_horizontally, flipped_vertically)

    def pixel_scale(self) -> Optional["Quantity"]:
        if "pixel_scale" in self._cache:
            return self._cache["pixel_scale"]

        from ..opticalequipment.camera import Camera
        from ..opticalequipment.smart_telescope import SmartTelescope

        if not isinstance(self.output, (Camera, SmartTelescope)):
            self._cache["pixel_scale"] = None
            return None
        # Effective focal length
        eff_focal_length = self.telescope.focal_length * self.effective_barlow()
        # Pixel size
        p_size = self.output.pixel_size()
        # Formula: (p_size / eff_focal_length) * RAD_TO_ARCSEC
        scale = (
            p_size.to("mm").magnitude / eff_focal_length.to("mm").magnitude
        ) * astronomy.RAD_TO_ARCSEC
        res = scale * get_unit_registry().arcsecond
        self._cache["pixel_scale"] = res
        return res

    def sampling(self, seeing: float) -> Optional[str]:
        """
        Calculates the sampling status based on the resolution limit and the pixel scale.
        The resolution limit is the larger of the atmospheric seeing and the telescope's diffraction limit (Rayleigh limit).

        According to the Nyquist-Shannon sampling theorem, the ideal sampling (critical sampling)
        is at least 2 pixels per resolution element. In astrophotography, a ratio of 2.0 to 3.0
        is often considered ideal to capture all available detail without excessive oversampling.

        Thresholds:
        - Under-sampled: ratio < 1.0 (Information lost, stars look like squares)
        - Well-sampled: 1.0 <= ratio <= 3.0 (Good balance for most conditions)
        - Over-sampled: ratio > 3.0 (No extra detail gained, smaller field of view, lower SNR)

        Source: Nyquist-Shannon sampling theorem
        """
        scale = self.pixel_scale()
        if scale is None or scale.magnitude == 0:
            return None

        # Effective resolution limit is the larger of seeing and diffraction limit
        r_limit = seeing
        diffraction_limit = self.rayleigh_limit()
        if diffraction_limit is not None:
            r_limit = max(seeing, diffraction_limit.to("arcsecond").magnitude)

        ratio = r_limit / scale.magnitude
        if ratio < 1.0:
            return "Under-sampled"
        elif ratio <= 3.0:
            return "Well-sampled"
        else:
            return "Over-sampled"

    def sampling_status(self, seeing: float = 2.0) -> Optional[str]:
        """
        Returns the sampling status as a string for a given seeing in arcseconds.
        """
        return self.sampling(seeing)

    def critical_focus_zone(self, wavelength: float = 550) -> Optional["Quantity"]:
        if not hasattr(self.telescope, "focal_ratio"):
            return None
        # wavelength in nm
        fr = (self.telescope.focal_ratio() * self.effective_barlow()).magnitude
        # CFZ = 2.44 * (wavelength/1000) * fr^2
        cfz = 2.44 * (wavelength / 1000.0) * (fr**2)
        return cfz * get_unit_registry().micrometer

    def thermal_drift(self, delta_t: float) -> Optional["Quantity"]:
        if (
            not hasattr(self.telescope, "tube_material")
            or self.telescope.tube_material is None
        ):
            return None
        # delta_t in Celsius
        length = self.telescope.focal_length.to("mm").magnitude
        alpha = self.telescope.tube_material.value  # m/(m*K)
        drift = length * alpha * delta_t
        return drift * get_unit_registry().mm

    def dawes_limit(self) -> Optional["Quantity"]:
        """
        Calculates the Dawes' limit (resolving power) of the telescope in arcseconds.
        Based on the telescope aperture.
        """
        if "dawes_limit" not in self._cache:
            if hasattr(self.telescope, "dawes_limit"):
                self._cache["dawes_limit"] = self.telescope.dawes_limit()
            else:
                self._cache["dawes_limit"] = None
        return self._cache["dawes_limit"]

    def rayleigh_limit(self, wavelength_nm: float | int = 550) -> Optional["Quantity"]:
        """
        Calculates the Rayleigh limit (resolving power) of the telescope in arcseconds.
        Based on the telescope aperture and the provided wavelength (default 550nm).
        """
        cache_key = f"rayleigh_limit_{wavelength_nm}"
        if cache_key not in self._cache:
            if hasattr(self.telescope, "rayleigh_limit"):
                self._cache[cache_key] = self.telescope.rayleigh_limit(
                    wavelength_nm=wavelength_nm
                )
            else:
                self._cache[cache_key] = None
        return self._cache[cache_key]

    def airy_disk_diameter(self, wavelength_nm: float = 550) -> Optional["Quantity"]:
        """
        Calculates the physical diameter of the Airy disk (first dark ring) in micrometers.
        Formula: D = 2.44 * lambda * f/D
        Where lambda is the wavelength and f/D is the effective focal ratio.
        This represents the diffraction-limited spot size on the focal plane.
        """
        if not hasattr(self.telescope, "focal_ratio"):
            return None
        # Effective focal ratio
        fr = (self.telescope.focal_ratio() * self.effective_barlow()).magnitude
        from ..utils import optics as utils_optics
        diameter_um = utils_optics.calculate_airy_disk_diameter(fr, wavelength_nm)
        return float(diameter_um) * get_unit_registry().micrometer

    def ideal_planetary_focal_ratio(self, k: float = 5.0) -> Optional[float]:
        """
        Calculates the ideal focal ratio for planetary imaging based on the pixel size.
        Rule of thumb: Ideal focal ratio is between 3x and 5x the pixel size in microns.
        Formula: Ideal Focal Ratio = k * Pixel Size (µm)
        Where k is usually 5.0 for average to good seeing.
        """
        from ..opticalequipment.camera import Camera
        from ..opticalequipment.smart_telescope import SmartTelescope

        if not isinstance(self.output, (Camera, SmartTelescope)):
            return None

        # Pixel size in microns
        p_size_q = self.output.pixel_size()
        if p_size_q is None:
            return None
        p_size = p_size_q.to("micrometer").magnitude
        return k * p_size

    def nyquist_focal_ratio(
        self, wavelength_nm: float = 550, sampling_factor: float = 3.0
    ) -> Optional[float]:
        """
        Calculates the ideal focal ratio for a given wavelength and sampling factor based on the Nyquist criterion.
        Formula: f/D = (p * s) / (1.22 * lambda)
        Where p is pixel size (µm), s is sampling factor, and lambda is wavelength (µm).
        A sampling factor of 2.0-3.0 is typically used for planetary imaging.
        Source: Nyquist-Shannon sampling theorem applied to diffraction-limited optics.
        """
        from ..opticalequipment.camera import Camera
        from ..opticalequipment.smart_telescope import SmartTelescope

        if not isinstance(self.output, (Camera, SmartTelescope)):
            return None

        p_size_q = self.output.pixel_size()
        if p_size_q is None:
            return None

        p_um = p_size_q.to("micrometer").magnitude
        lambda_um = wavelength_nm / 1000.0

        return (p_um * sampling_factor) / (1.22 * lambda_um)
