import logging
from typing import List, Dict, Any, Optional

from .opticalequipment import (
    Telescope,
    Camera,
    Eyepiece,
    Barlow,
    Diagonal,
    Reducer,
    Flattener,
    Corrector,
    FilterWheel,
    FilterHolder,
    OAG,
    Rotator,
    Focuser,
    Adapter,
    Spacer,
    AntiTilt,
    FlipMirror,
    GuideScope,
    Binoculars,
    SmartTelescope,
)

logger = logging.getLogger(__name__)

EQUIPMENT_CLASSES = [
    Telescope,
    Camera,
    Eyepiece,
    Barlow,
    Diagonal,
    Reducer,
    Flattener,
    Corrector,
    FilterWheel,
    FilterHolder,
    OAG,
    Rotator,
    Focuser,
    Adapter,
    Spacer,
    AntiTilt,
    FlipMirror,
    GuideScope,
    Binoculars,
    SmartTelescope,
]

# Mapping of equipment type strings to their corresponding classes for dynamic instantiation.
TYPE_TO_CLASS_MAP = {
    "type_telescope": Telescope,
    "type_refractor": Telescope,
    "refractor": Telescope,
    "newtonian_reflector": Telescope,
    "schmidt_cassegrain": Telescope,
    "maksutov_cassegrain": Telescope,
    "catadioptric": Telescope,
    "type_camera_lens": Telescope,
    "type_camera": Camera,
    "type_dslr": Camera,
    "type_eyepiece": Eyepiece,
    "type_barlow": Barlow,
    "type_extender": Barlow,
    "type_reducer": Reducer,
    "type_flattener": Flattener,
    "type_corrector": Corrector,
    "type_diagonal": Diagonal,
    "type_filter_wheel": FilterWheel,
    "type_filter_holder": FilterHolder,
    "type_oag": OAG,
    "type_rotator": Rotator,
    "type_focuser": Focuser,
    "type_adapter": Adapter,
    "type_spacer": Spacer,
    "type_anti_tilt": AntiTilt,
    "type_flip_mirror": FlipMirror,
    "type_guide_scope": GuideScope,
    "type_smart_telescope": SmartTelescope,
}


class EquipmentDatabase:
    """
    Utility class to interact with the equipment reference database.
    Now loads data from individual equipment classes.
    """

    def __init__(self):
        self.db_dict = {}
        for cls in EQUIPMENT_CLASSES:
            if hasattr(cls, "get_database_entries"):
                for e in cls.get_database_entries():
                    self.db_dict[(e["brand"], e["name"])] = e
        self.db = list(self.db_dict.values())

    def get_all(self) -> List[Dict[str, Any]]:
        return self.db

    def find(
        self,
        brand: Optional[str] = None,
        name: Optional[str] = None,
        equipment_type: Optional[str] = None,
    ) -> List[Dict[str, Any]]:
        results = self.db
        if brand:
            results = [e for e in results if brand.lower() in e["brand"].lower()]
        if name:
            results = [e for e in results if name.lower() in e["name"].lower()]
        if equipment_type:
            results = [
                e for e in results if equipment_type.lower() in e["type"].lower()
            ]
        return results

    def create_equipment(self, entry: Dict[str, Any]) -> Any:
        """
        Creates an apts equipment object from a database entry using a registry-based lookup.
        """
        tp = entry.get("type", "")
        name = entry.get("name", "")

        # Special case: Binoculars detection based on name
        if "binocular" in name.lower():
            return Binoculars.from_database(entry)

        # Lookup class in the registry
        cls = TYPE_TO_CLASS_MAP.get(tp)

        if cls and hasattr(cls, "from_database"):
            return cls.from_database(entry)

        logger.warning(f"Could not find a class to create equipment of type '{tp}' and name '{name}'.")
        return None
