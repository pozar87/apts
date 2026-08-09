from .barlow import Barlow
from .telescope import Telescope
from .camera import Camera
from .eyepiece import Eyepiece
from .base import (
    OpticalEquipment,
    IntermediateOpticalEquipment,
    OutputOpticalEquipment,
)
from .binoculars import Binoculars
from .naked_eye import NakedEye
from .diagonal import Diagonal
from .smart_telescope import SmartTelescope
from .filter import Filter
from .reducer import Reducer, Flattener, Corrector
from .filter_wheel import FilterWheel, FilterHolder
from .oag import OAG
from .rotator import Rotator
from .focuser import Focuser
from .adapter import Adapter, Spacer
from .anti_tilt import AntiTilt
from .flip_mirror import FlipMirror
from .guide_scope import GuideScope

EQUIPMENT_CLASSES = [
    Telescope,
    Camera,
    Eyepiece,
    Barlow,
    Diagonal,
    Filter,
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
    "type_filter": Filter,
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

__all__ = [
    "Barlow",
    "Telescope",
    "Camera",
    "Eyepiece",
    "OpticalEquipment",
    "IntermediateOpticalEquipment",
    "OutputOpticalEquipment",
    "Binoculars",
    "NakedEye",
    "Diagonal",
    "SmartTelescope",
    "Filter",
    "Reducer",
    "Flattener",
    "Corrector",
    "FilterWheel",
    "FilterHolder",
    "OAG",
    "Rotator",
    "Focuser",
    "Adapter",
    "Spacer",
    "AntiTilt",
    "FlipMirror",
    "GuideScope",
    "EQUIPMENT_CLASSES",
    "TYPE_TO_CLASS_MAP",
]

__version__ = "0.2.0"
