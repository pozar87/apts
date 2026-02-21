import inspect
from typing import Dict, List, Any, Type
from .opticalequipment import (
    Telescope, Camera, Eyepiece, Barlow, Diagonal, Filter,
    Reducer, Flattener, Corrector, FilterWheel, FilterHolder,
    OAG, Rotator, Focuser, Adapter, Spacer, AntiTilt, FlipMirror,
    GuideScope, Binoculars, SmartTelescope
)

class EquipmentRegistry:
    """
    Utility to discover and list all built-in equipment models (factory methods).
    """

    EQUIPMENT_CLASSES = [
        Telescope, Camera, Eyepiece, Barlow, Diagonal, Filter,
        Reducer, Flattener, Corrector, FilterWheel, FilterHolder,
        OAG, Rotator, Focuser, Adapter, Spacer, AntiTilt, FlipMirror,
        GuideScope, Binoculars, SmartTelescope
    ]

    @staticmethod
    def list_all_by_type() -> Dict[str, List[Dict[str, Any]]]:
        """
        Returns a dictionary where keys are class names and values are lists of
        available factory methods (model names) and their instantiation functions.
        """
        registry = {}
        for cls in EquipmentRegistry.EQUIPMENT_CLASSES:
            class_name = cls.__name__
            models = []

            # Inspect class for class methods that return an instance of the class
            for name, method in inspect.getmembers(cls, predicate=inspect.ismethod):
                # We look for methods that are not private and not standard class methods
                if not name.startswith('_') and name not in ['register', 'from_path', 'get_parent_id', 'type', 'Dawes_Limit', 'ZWO_ASI2600MC_PRO', 'ZWO_ASI1600MM_PRO', 'Nikon_D850']:
                    # In Python 3, ismethod on a class usually means it's a classmethod
                    models.append({
                        "model_name": name.replace('_', ' '),
                        "factory_name": name,
                        "class": cls
                    })

            # Special handling for Camera since I already had some there
            if cls == Camera:
                for name in ['ZWO_ASI2600MC_PRO', 'ZWO_ASI1600MM_PRO', 'Nikon_D850']:
                    models.append({
                        "model_name": name.replace('_', ' '),
                        "factory_name": name,
                        "class": cls
                    })

            if models:
                registry[class_name] = models

        return registry

    @staticmethod
    def create(class_name: str, factory_name: str) -> Any:
        """
        Instantiate an equipment model by its class and factory method names.
        """
        for cls in EquipmentRegistry.EQUIPMENT_CLASSES:
            if cls.__name__ == class_name:
                method = getattr(cls, factory_name, None)
                if method:
                    return method()
        return None
