from typing import TYPE_CHECKING, Any, Optional

if TYPE_CHECKING:
    from pint import Quantity

from ...units import get_unit_registry


class MechanicalMixIn:
    if TYPE_CHECKING:
        telescope: Any
        barlows: list[Any]
        diagonals: list[Any]
        filters: list[Any]
        others: list[Any]
        output: Any
        _cache: dict[str, Any]
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

        from ...opticalequipment.abstract import OpticalEquipment

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
        Calculate the backfocus gap.
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
            if (
                hasattr(item, "required_backfocus")
                and item.required_backfocus is not None
            ):
                required_bf = item.required_backfocus
                start_index = i
            elif i == 0 and hasattr(item, "backfocus") and item.backfocus is not None:
                required_bf = item.backfocus
                start_index = i

        if required_bf is None:
            return None

        # 2. Calculate actual distance from that component's output to the sensor
        actual_distance = 0 * get_unit_registry().mm
        for item in path[start_index + 1 : -1]:
            item_ol = getattr(item, "optical_length", 0 * get_unit_registry().mm)
            if item_ol is not None:
                actual_distance += item_ol

        # 3. Add the output component's backfocus contribution
        if hasattr(self.output, "backfocus") and self.output.backfocus is not None:
            actual_distance += self.output.backfocus

        return required_bf - actual_distance

    def get_image_orientation(self):
        from ...opticalequipment.telescope import Telescope

        if not isinstance(self.telescope, Telescope):
            return (False, False)

        flipped_horizontally = True
        flipped_vertically = True

        for diagonal in self.diagonals:
            if diagonal.is_erecting:
                flipped_horizontally = not flipped_horizontally
                flipped_vertically = not flipped_vertically
            else:
                flipped_vertically = not flipped_vertically

        return (flipped_horizontally, flipped_vertically)

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
