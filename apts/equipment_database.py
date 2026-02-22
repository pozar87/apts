import logging
from typing import List, Dict, Any, Optional

from .opticalequipment import (
    Telescope, Camera, Eyepiece, Barlow, Diagonal,
    Reducer, Flattener, Corrector, FilterWheel, FilterHolder,
    OAG, Rotator, Focuser, Adapter, Spacer, AntiTilt, FlipMirror,
    GuideScope, Binoculars
)

logger = logging.getLogger(__name__)

EQUIPMENT_CLASSES = [
    Telescope, Camera, Eyepiece, Barlow, Diagonal,
    Reducer, Flattener, Corrector, FilterWheel, FilterHolder,
    OAG, Rotator, Focuser, Adapter, Spacer, AntiTilt, FlipMirror,
    GuideScope, Binoculars
]

class EquipmentDatabase:
    """
    Utility class to interact with the equipment reference database.
    Now loads data from individual equipment classes.
    """

    def __init__(self):
        self.db = []
        for cls in EQUIPMENT_CLASSES:
            if hasattr(cls, "_DATABASE"):
                if isinstance(cls._DATABASE, dict):
                    self.db.extend(cls._DATABASE.values())
                else:
                    self.db.extend(cls._DATABASE)

    def get_all(self) -> List[Dict[str, Any]]:
        return self.db

    def find(self, brand: Optional[str] = None, name: Optional[str] = None, equipment_type: Optional[str] = None) -> List[Dict[str, Any]]:
        results = self.db
        if brand:
            results = [e for e in results if brand.lower() in e['brand'].lower()]
        if name:
            results = [e for e in results if name.lower() in e['name'].lower()]
        if equipment_type:
            results = [e for e in results if equipment_type.lower() in e['type'].lower()]
        return results

    def create_equipment(self, entry: Dict[str, Any]) -> Any:
        """
        Creates an apts equipment object from a database entry.
        """
        tp = entry['type']
        name = entry.get('name', '')

        # Mapping to classes
        if "binocular" in name.lower():
            return Binoculars.from_database(entry)

        if tp in ["type_telescope", "type_refractor", "type_camera_lens"]:
            return Telescope.from_database(entry)
        if tp in ["type_camera", "type_dslr"]:
            return Camera.from_database(entry)
        if tp == "type_eyepiece":
            return Eyepiece.from_database(entry)
        if tp in ["type_barlow", "type_extender"]:
            return Barlow.from_database(entry)
        if tp == "type_reducer":
            return Reducer.from_database(entry)
        if tp == "type_flattener":
            return Flattener.from_database(entry)
        if tp == "type_corrector":
            return Corrector.from_database(entry)
        if tp == 'type_diagonal':
            return Diagonal.from_database(entry)
        if tp == 'type_filter_wheel':
            return FilterWheel.from_database(entry)
        if tp == 'type_filter_holder':
            return FilterHolder.from_database(entry)
        if tp == 'type_oag':
            return OAG.from_database(entry)
        if tp == 'type_rotator':
            return Rotator.from_database(entry)
        if tp == 'type_focuser':
            return Focuser.from_database(entry)
        if tp == 'type_adapter':
            return Adapter.from_database(entry)
        if tp == 'type_spacer':
            return Spacer.from_database(entry)
        if tp == 'type_anti_tilt':
            return AntiTilt.from_database(entry)
        if tp == 'type_flip_mirror':
            return FlipMirror.from_database(entry)
        if tp == 'type_guide_scope':
            return GuideScope.from_database(entry)

        return None
