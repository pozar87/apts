import functools
import operator
from typing import TYPE_CHECKING, Any, Sequence, Union, cast

import numpy as np

if TYPE_CHECKING:
    from pint import Quantity
    from ..opticalequipment.abstract import OpticalEquipment, OutputOpticalEquipment
    from ..opticalequipment.smart_telescope import SmartTelescope

from ..units import get_unit_registry
from ..utils import optics as optics_utils
from ..opticalequipment.binoculars import Binoculars
from ..opticalequipment.naked_eye import NakedEye


class OpticsUtils:
    @staticmethod
    def expand(
        path: Sequence["OpticalEquipment"],
    ) -> tuple[
        Union["OpticalEquipment", Binoculars, NakedEye, "SmartTelescope"],
        Sequence[Any],
        Sequence[Any],
        Sequence[Any],
        Sequence[Any],
        Union["OutputOpticalEquipment", Binoculars, NakedEye, "SmartTelescope"],
    ]:
        from ..opticalequipment.barlow import Barlow
        from ..opticalequipment.diagonal import Diagonal
        from ..opticalequipment.filter import Filter
        from ..opticalequipment.reducer.base import Corrector, Flattener, Reducer
        from ..opticalequipment.smart_telescope import SmartTelescope

        # First item in the path should be the telescope or binoculars
        main_optic = path[0]
        if isinstance(main_optic, (Binoculars, NakedEye, SmartTelescope)):
            # Treat binoculars as the 'output' as well for path structure consistency
            return (main_optic, [], [], [], [], main_optic)

        # Original logic for telescopes
        telescope = main_optic
        # Last item in the path is output
        output = cast("OutputOpticalEquipment", path[-1])
        # Intermediate elements - categorized in a single pass
        barlows = []
        diagonals = []
        filters = []
        others = []

        for item in path[1:-1]:
            if isinstance(item, (Barlow, Reducer, Flattener, Corrector)):
                barlows.append(item)
            elif isinstance(item, Diagonal):
                diagonals.append(item)
            elif isinstance(item, Filter):
                filters.append(item)
            else:
                others.append(item)

        return (telescope, barlows, diagonals, filters, others, output)

    @staticmethod
    def barlows_multiplications(barlows_list: Sequence[Any]) -> float:
        barlows = [barlow.magnification for barlow in barlows_list]
        # Multiply all barlows
        return float(functools.reduce(operator.mul, barlows, 1))

    @staticmethod
    def compute_zoom(
        telescope: Union["OpticalEquipment", Binoculars, NakedEye, "SmartTelescope"],
        barlows: Sequence[Any],
        output: Union["OutputOpticalEquipment", Binoculars, NakedEye, "SmartTelescope"],
    ) -> "Quantity":
        from ..opticalequipment.smart_telescope import SmartTelescope

        if isinstance(telescope, (Binoculars, NakedEye, SmartTelescope)):
            return telescope.magnification * get_unit_registry().dimensionless

        # Original logic
        magnification = OpticsUtils.barlows_multiplications(barlows)
        return telescope.focal_length * magnification / output._zoom_divider()

    @staticmethod
    def calculate_airmass(altitude_degrees: float) -> float:
        """
        Calculates the relative airmass using the Kasten-Young (1989) formula.
        Formula: X = 1 / (sin(h) + 0.50572 * (h + 6.07995)^-1.6364)
        Where h is the apparent altitude in degrees.
        Source: https://en.wikipedia.org/wiki/Air_mass_(astronomy)
        """
        return float(optics_utils.calculate_airmass(altitude_degrees))

    @staticmethod
    def compute_field_of_view(
        telescope: Union["OpticalEquipment", Binoculars, NakedEye, "SmartTelescope"],
        barlows: Sequence[Any],
        output: Union["OutputOpticalEquipment", Binoculars, NakedEye, "SmartTelescope"],
    ) -> "Quantity":
        from ..opticalequipment.smart_telescope import SmartTelescope

        if isinstance(telescope, (Binoculars, NakedEye, SmartTelescope)):
            return telescope.fov()

        # Original logic
        magnification = OpticsUtils.barlows_multiplications(barlows)
        zoom = OpticsUtils.compute_zoom(telescope, barlows, output)
        # TODO: this is not best way to do it
        return output.field_of_view(telescope, zoom, magnification)

    @staticmethod
    def calculate_fov_ratio(object_size, sensor_size, focal_length):
        """
        Determine the percentage of the frame the object occupies.
        object_size: tuple (major, minor) in arcminutes
        sensor_size: tuple (width, height) in mm
        focal_length: focal length in mm
        """
        # Handle potential pint.Quantity objects in object_size
        obj_major_arcmin = (
            object_size[0].magnitude
            if hasattr(object_size[0], "magnitude")
            else object_size[0]
        )
        obj_minor_arcmin = (
            object_size[1].magnitude
            if hasattr(object_size[1], "magnitude")
            else object_size[1]
        )

        # Convert to float and handle None/NaN
        if hasattr(obj_major_arcmin, "__iter__") and not isinstance(obj_major_arcmin, (str, bytes)):
            obj_major_arcmin = np.array(obj_major_arcmin, dtype=float)
            obj_minor_arcmin = np.array(obj_minor_arcmin, dtype=float)
        else:
            obj_major_arcmin = float(obj_major_arcmin or 0)
            obj_minor_arcmin = float(obj_minor_arcmin or 0)

        obj_major_deg = obj_major_arcmin / 60.0
        obj_minor_deg = obj_minor_arcmin / 60.0

        # FOV in degrees = 2 * arctan(sensor_size / (2 * focal_length))
        fov_w_deg = np.degrees(2 * np.arctan(sensor_size[0] / (2 * focal_length)))
        fov_h_deg = np.degrees(2 * np.arctan(sensor_size[1] / (2 * focal_length)))

        ratio_w = obj_major_deg / fov_w_deg
        ratio_h = obj_minor_deg / fov_h_deg

        # Use the maximum ratio to ensure it's not "clipped"
        return np.maximum(ratio_w, ratio_h) * 100.0
