import functools
import operator
from typing import Sequence, Any, Union
import numpy as np


def barlows_multiplications(barlows_list: Sequence[Any]) -> float:
    """
    Calculates total Barlow lens multiplication factor.
    """
    barlows = [barlow.magnification for barlow in barlows_list]
    # Multiply all barlows
    return float(functools.reduce(operator.mul, barlows, 1))


def calculate_zoom(
    telescope: Any,
    barlows: Sequence[Any],
    output: Any,
) -> Any:
    """
    Calculates zoom (magnification) of an optical configuration.
    """
    from ...units import get_unit_registry
    from ...opticalequipment.binoculars import Binoculars
    from ...opticalequipment.naked_eye import NakedEye
    from ...opticalequipment.smart_telescope import SmartTelescope

    if isinstance(telescope, (Binoculars, NakedEye, SmartTelescope)):
        return telescope.magnification * get_unit_registry().dimensionless

    # Original logic
    magnification = barlows_multiplications(barlows)
    return telescope.focal_length * magnification / output._zoom_divider()


def calculate_field_of_view(
    telescope: Any,
    barlows: Sequence[Any],
    output: Any,
) -> Any:
    """
    Calculates field of view of an optical configuration.
    """
    from ...opticalequipment.binoculars import Binoculars
    from ...opticalequipment.naked_eye import NakedEye
    from ...opticalequipment.smart_telescope import SmartTelescope

    if isinstance(telescope, (Binoculars, NakedEye, SmartTelescope)):
        return telescope.fov()

    # Original logic
    magnification = barlows_multiplications(barlows)
    zoom = calculate_zoom(telescope, barlows, output)
    return output.field_of_view(telescope, zoom, magnification)


def calculate_fov_ratio(object_size: Any, sensor_size: Any, focal_length: Any) -> Any:
    """
    Determine the percentage of the frame the object occupies.
    object_size: tuple (major, minor) in arcminutes
    sensor_size: tuple (width, height) in mm
    focal_length: focal length in mm
    """

    def _get_magnitude(data):
        if hasattr(data, "to"):
            # It's a Quantity (scalar or array-wrapped)
            return data.to("arcminute").magnitude
        if isinstance(data, (np.ndarray, list, tuple)):
            # If we have a list of Quantities, np.array() might try to be too smart
            # and fail if they are heterogeneous or have different units.
            # Let's handle it by checking if it's a list/tuple and converting elements
            if isinstance(data, (list, tuple)):
                # Check if any element is a Quantity
                if any(hasattr(v, "to") for v in data):
                    return np.array(
                        [
                            (
                                v.to("arcminute").magnitude
                                if hasattr(v, "to")
                                else float(v or 0)
                            )
                            for v in data
                        ],
                        dtype=float,
                    )

            data_array = np.array(data)
            # Check if it contains Quantities (object dtype)
            if data_array.dtype == object and len(data_array) > 0:
                # Check first element to see if it's a Quantity
                if hasattr(data_array[0], "to"):
                    return np.array(
                        [
                            (
                                v.to("arcminute").magnitude
                                if hasattr(v, "to")
                                else float(v or 0)
                            )
                            for v in data_array
                        ],
                        dtype=float,
                    )
            return data_array.astype(float)
        return float(data or 0)

    # Handle potential pint.Quantity objects in object_size
    obj_major_arcmin = _get_magnitude(object_size[0])
    obj_minor_arcmin = _get_magnitude(object_size[1])

    obj_major_deg = obj_major_arcmin / 60.0
    obj_minor_deg = obj_minor_arcmin / 60.0

    # FOV in degrees = 2 * arctan(sensor_size / (2 * focal_length))
    fov_w_deg = np.degrees(2 * np.arctan(sensor_size[0] / (2 * focal_length)))
    fov_h_deg = np.degrees(2 * np.arctan(sensor_size[1] / (2 * focal_length)))

    ratio_w = obj_major_deg / fov_w_deg
    ratio_h = obj_minor_deg / fov_h_deg

    # Use the maximum ratio to ensure it's not "clipped"
    return np.maximum(ratio_w, ratio_h) * 100.0
