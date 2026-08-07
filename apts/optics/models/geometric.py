from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from pint import Quantity

from ..utils import OpticsUtils
from ..calculations import geometric as optics_utils


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
                optics_utils.barlows_multiplications(self.barlows)
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
        return optics_utils.calculate_is_magnification_useful(
            self.telescope, self.output, self.zoom()
        )

    def brightness(self) -> "Quantity":
        if "brightness" not in self._cache:
            self._cache["brightness"] = optics_utils.calculate_brightness(
                self.telescope, self.output, self.zoom(), self.filters
            )
        return self._cache["brightness"]

    def exit_pupil(self) -> "Quantity":
        return optics_utils.calculate_exit_pupil(
            self.telescope, self.zoom()
        )
