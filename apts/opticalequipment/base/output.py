from typing import Any

import numpy as np

from .equipment import OpticalEquipment


class OutputOpticalEquipment(OpticalEquipment):
    def __init__(
        self,
        focal_length,
        vendor,
        optical_length=0.0,
        mass=0.0,
        inputs=None,
        outputs=None,
        connection_type=None,
        connection_gender=None,
    ):
        if inputs is None:
            if connection_type is not None:
                inputs = [(connection_type, connection_gender)]
        super().__init__(
            focal_length,
            vendor,
            optical_length=optical_length,
            mass=mass,
            inputs=inputs,
            outputs=outputs,
        )

    def is_visual_output(self) -> bool:
        """Indicates if the output is primarily for visual observation."""
        return True  # Default for eyepieces etc.

    def field_of_view(self, telescope, zoom, barlow_magnification):
        """Calculates field of view."""
        raise NotImplementedError("Subclasses must implement field_of_view")

    def field_of_view_width(self, telescope, zoom, barlow_magnification):
        """Calculates horizontal field of view."""
        return self.field_of_view(telescope, zoom, barlow_magnification)

    def field_of_view_height(self, telescope, zoom, barlow_magnification):
        """Calculates vertical field of view."""
        return self.field_of_view(telescope, zoom, barlow_magnification)

    def field_of_view_diagonal(self, telescope, zoom, barlow_magnification):
        """Calculates diagonal field of view."""
        return self.field_of_view(telescope, zoom, barlow_magnification)

    def _zoom_divider(self) -> Any:
        """Returns the zoom divider for this equipment."""
        raise NotImplementedError("Subclasses must implement _zoom_divider")

    def exit_pupil(self, telescope, zoom):
        from ...optics.calculations import calculate_exit_pupil

        return calculate_exit_pupil(getattr(telescope, "aperture", None), zoom)

    def brightness(self, telescope, zoom):
        from ...optics.calculations import calculate_brightness
        from ...units import get_unit_registry

        if not self.is_visual_output():
            return np.nan * get_unit_registry().dimensionless

        ep_val = self.exit_pupil(telescope, zoom)
        return calculate_brightness(ep_val)
