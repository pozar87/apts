from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from pint import Quantity

from ...units import get_unit_registry
from ..utils import OpticsUtils


class GeometricMixIn:
    if TYPE_CHECKING:
        telescope: Any
        barlows: list[Any]
        output: Any
        filters: list[Any]
        _cache: dict[str, Any]

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
        from ...opticalequipment.telescope import Telescope

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

    def brightness(self) -> "Quantity":
        if "brightness" in self._cache:
            return self._cache["brightness"]

        from ...opticalequipment.binoculars import Binoculars
        from ...opticalequipment.naked_eye import NakedEye
        from ...opticalequipment.smart_telescope import SmartTelescope

        if isinstance(self.telescope, (Binoculars, NakedEye, SmartTelescope)):
            # self.telescope.brightness() returns a float like 75.0 (for 75%)
            # To be consistent so that .magnitude can be called later:
            brightness = self.telescope.brightness() * get_unit_registry().dimensionless
        else:
            # This already returns a pint Quantity from OutputOpticalEquipment's method
            brightness = self.output.brightness(self.telescope, self.zoom())

        # Account for filters transmission
        for f in self.filters:
            brightness *= f.transmission

        self._cache["brightness"] = brightness
        return brightness

    def exit_pupil(self) -> "Quantity":
        from ...opticalequipment.binoculars import Binoculars
        from ...opticalequipment.naked_eye import NakedEye
        from ...opticalequipment.smart_telescope import SmartTelescope

        if isinstance(self.telescope, (Binoculars, NakedEye, SmartTelescope)):
            return self.telescope.exit_pupil()  # This returns a Quantity

        # Original logic for telescopes:
        if hasattr(self.telescope, "aperture"):
            zoom_value = self.zoom()
            if zoom_value.magnitude == 0:
                return 0 * get_unit_registry().mm
            return self.telescope.aperture / zoom_value

        return 0 * get_unit_registry().mm
