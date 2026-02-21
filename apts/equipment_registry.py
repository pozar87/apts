import inspect
from typing import Dict, List, Any, Type, Optional
from .opticalequipment import (
    Telescope, Camera, Eyepiece, Barlow, Diagonal, Filter,
    Reducer, Flattener, Corrector, FilterWheel, FilterHolder,
    OAG, Rotator, Focuser, Adapter, Spacer, AntiTilt, FlipMirror,
    GuideScope, Binoculars, SmartTelescope
)
from .equipment_database import EquipmentDatabase

class EquipmentRegistry:
    """
    Unified registry for astronomical equipment.
    Combines high-fidelity hardcoded presets with the full reference database.
    """

    EQUIPMENT_CLASSES = [
        Telescope, Camera, Eyepiece, Barlow, Diagonal, Filter,
        Reducer, Flattener, Corrector, FilterWheel, FilterHolder,
        OAG, Rotator, Focuser, Adapter, Spacer, AntiTilt, FlipMirror,
        GuideScope, Binoculars, SmartTelescope
    ]

    # Curated list of popular equipment names to feature in the UI
    FEATURED_NAMES = [
        # Telescopes
        "Evostar 80ED", "C8", "61EDPH", "ED80", "ED100", "ED120", "RedCat 51",
        # Cameras
        "ASI2600MC Pro", "ASI1600MM Pro", "D850", "ASI294MC", "ASI533MC",
        # Eyepieces
        "Nagler", "Ethos", "Delos", "Plossl", "Hyperion", "Morpheus",
        # Accessories
        "EAF", "OAG", "Falcon Rotator", "FocusCube", "L-Pro", "UHC-S"
    ]

    def __init__(self):
        self.db = EquipmentDatabase()

    def get_featured(self) -> Dict[str, List[Dict[str, Any]]]:
        """
        Returns a dictionary of featured equipment categorized by class name.
        """
        registry = {}

        # 1. Add hardcoded classmethods (like high-fidelity Camera presets)
        for cls in self.EQUIPMENT_CLASSES:
            class_name = cls.__name__
            models = []
            for name, method in inspect.getmembers(cls, predicate=inspect.ismethod):
                if not name.startswith('_') and name not in ['register', 'from_path', 'get_parent_id', 'type', 'Dawes_Limit']:
                    models.append({
                        "id": f"preset:{class_name}:{name}",
                        "name": name.replace('_', ' '),
                        "source": "preset",
                        "factory": method
                    })
            if models:
                registry[class_name] = models

        # 2. Search DB for featured items
        for name_query in self.FEATURED_NAMES:
            results = self.db.find(name=name_query)
            for entry in results:
                # Map DB type to Stargazer class
                obj = self.db.create_equipment(entry)
                if obj:
                    class_name = obj.__class__.__name__
                    if class_name not in registry:
                        registry[class_name] = []

                    # Avoid duplicates if already in registry
                    display_name = f"{entry['brand']} {entry['name']}"
                    if not any(m['name'] == display_name for m in registry[class_name]):
                        registry[class_name].append({
                            "id": f"db:{entry.get('id', entry['name'])}",
                            "name": display_name,
                            "source": "database",
                            "entry": entry
                        })

        return registry

    def get_all_by_type(self, class_name: Optional[str] = None) -> List[Dict[str, Any]]:
        """
        Returns all equipment from the database (optionally filtered by class).
        """
        results = []
        all_entries = self.db.get_all()
        for entry in all_entries:
            obj = self.db.create_equipment(entry)
            if obj:
                if class_name is None or obj.__class__.__name__ == class_name:
                    results.append({
                        "id": f"db:{entry.get('id', entry['name'])}",
                        "name": f"{entry['brand']} {entry['name']}",
                        "class": obj.__class__.__name__,
                        "entry": entry
                    })
        return results

    def create(self, item_id: str) -> Any:
        """
        Create an equipment instance from its registry ID.
        Format: 'preset:ClassName:MethodName' or 'db:Name'
        """
        if item_id.startswith("preset:"):
            _, class_name, method_name = item_id.split(":")
            for cls in self.EQUIPMENT_CLASSES:
                if cls.__name__ == class_name:
                    method = getattr(cls, method_name, None)
                    if method:
                        return method()
        elif item_id.startswith("db:"):
            name = item_id[3:]
            # Search by name in DB
            results = self.db.find(name=name)
            if results:
                return self.db.create_equipment(results[0])

        return None
