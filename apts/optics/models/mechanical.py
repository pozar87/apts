from typing import TYPE_CHECKING, Any, Optional

if TYPE_CHECKING:
    from pint import Quantity

from ...units import get_unit_registry
from ..calculations import mechanical as optics_utils


class MechanicalMixIn:
    if TYPE_CHECKING:
        telescope: Any
        barlows: list[Any]
        diagonals: list[Any]
        filters: list[Any]
        others: list[Any]
        output: Any
        _cache: dict[str, Any]
        _path: Optional[list]

        def effective_barlow(self) -> float: ...

    def label(self) -> str:
        from ...opticalequipment.binoculars import Binoculars
        from ...opticalequipment.naked_eye import NakedEye
        from ...opticalequipment.smart_telescope import SmartTelescope

        if hasattr(self, "_path") and self._path is not None:
            return ", ".join([str(item) for item in self._path])

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
        from ...opticalequipment.binoculars import Binoculars
        from ...opticalequipment.naked_eye import NakedEye
        from ...opticalequipment.smart_telescope import SmartTelescope

        if isinstance(self.telescope, (Binoculars, NakedEye, SmartTelescope)):
            return 1  # Just the binoculars itself
        return (
            2
            + len(self.barlows)
            + len(self.diagonals)
            + len(self.filters)
            + len(self.others)
        )

    def total_mass(self) -> "Quantity":
        if "total_mass" in self._cache:
            return self._cache["total_mass"]

        from ...opticalequipment.base import OpticalEquipment

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

    def _get_flattened_path(self) -> list[Any]:
        """
        Builds and returns a flattened list of optical components in the path.
        """
        return (
            [self.telescope]
            + self.barlows
            + self.diagonals
            + self.filters
            + self.others
            + [self.output]
        )

    def _find_backfocus_reference(self, path: list[Any]) -> tuple[Optional[Any], int]:
        """
        Scans the path to find the component defining the required backfocus reference
        and its start index in the path.
        """
        required_bf = None
        start_index = -1
        for i, item in enumerate(path):
            if (
                hasattr(item, "required_backfocus")
                and item.required_backfocus is not None
            ):
                required_bf = item.required_backfocus
                start_index = i
            elif i == 0 and hasattr(item, "backfocus") and item.backfocus is not None:
                required_bf = item.backfocus
                start_index = i
        return required_bf, start_index

    def _gather_intermediate_lengths(self, path: list[Any], start_index: int) -> list[float]:
        """
        Collects optical lengths (in mm) for intermediate components following the reference.
        """
        intermediate_lengths = []
        for item in path[start_index + 1 : -1]:
            item_ol = getattr(item, "optical_length", 0 * get_unit_registry().mm)
            if item_ol is not None:
                if hasattr(item_ol, "to"):
                    intermediate_lengths.append(item_ol.to("mm").magnitude)
                else:
                    intermediate_lengths.append(float(item_ol))
            else:
                intermediate_lengths.append(0.0)
        return intermediate_lengths

    def _get_output_backfocus_value(self) -> float:
        """
        Converts and returns the output component's backfocus value in mm.
        """
        output_bf_val = 0.0
        if hasattr(self.output, "backfocus") and self.output.backfocus is not None:
            if hasattr(self.output.backfocus, "to"):
                output_bf_val = self.output.backfocus.to("mm").magnitude
            else:
                output_bf_val = float(self.output.backfocus)
        return output_bf_val

    def backfocus_gap(self) -> Optional["Quantity"]:
        """
        Calculate the backfocus gap.
        """
        path = self._get_flattened_path()
        required_bf, start_index = self._find_backfocus_reference(path)

        if required_bf is None:
            return None

        intermediate_lengths = self._gather_intermediate_lengths(path, start_index)
        output_bf_val = self._get_output_backfocus_value()

        if hasattr(required_bf, "to"):
            required_bf_mm = required_bf.to("mm").magnitude
        else:
            required_bf_mm = float(required_bf)

        gap_mm = optics_utils.calculate_backfocus_gap(
            required_bf_mm, intermediate_lengths, output_bf_val
        )
        return gap_mm * get_unit_registry().mm

    def get_image_orientation(self):
        from ...opticalequipment.telescope import Telescope

        has_telescope = isinstance(self.telescope, Telescope)
        diagonal_is_erecting_list = [
            bool(getattr(diagonal, "is_erecting", False)) for diagonal in self.diagonals
        ]
        return optics_utils.calculate_image_orientation(
            has_telescope, diagonal_is_erecting_list
        )

    def thermal_drift(self, delta_t: float) -> Optional["Quantity"]:
        if (
            not hasattr(self.telescope, "tube_material")
            or self.telescope.tube_material is None
        ):
            return None
        length_mm = self.telescope.focal_length.to("mm").magnitude
        alpha = self.telescope.tube_material.value  # m/(m*K)
        drift = optics_utils.calculate_thermal_drift(length_mm, alpha, delta_t)
        return drift * get_unit_registry().mm
