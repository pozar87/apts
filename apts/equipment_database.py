import logging
import re
from typing import List, Dict, Any, Optional

from .data.equipment_database_raw import REFERENCE_DB
from .opticalequipment import (
    Telescope, Camera, Eyepiece, Barlow, Diagonal, Filter,
    Reducer, Flattener, Corrector, FilterWheel, FilterHolder,
    OAG, Rotator, Focuser, Adapter, Spacer, AntiTilt, FlipMirror,
    GuideScope
)
from .utils import ConnectionType, Gender

logger = logging.getLogger(__name__)

class EquipmentDatabase:
    """
    Utility class to interact with the equipment reference database.
    """

    def __init__(self):
        self.db = REFERENCE_DB

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
        brand = entry['brand']
        name = entry['name']
        vendor = f"{brand} {name}"
        ol = entry.get('optical_length', 0)
        mass = entry.get('mass', 0)

        # Connection mapping
        def map_conn(thread_str):
            if not thread_str:
                return ConnectionType.F_1_25 # Default
            # Try to match ConnectionType
            for ct in ConnectionType:
                if ct.value.lower() in thread_str.lower():
                    return ct
            return ConnectionType.F_1_25

        def map_gender(gender_str):
            if gender_str == "Male":
                return Gender.MALE
            if gender_str == "Female":
                return Gender.FEMALE
            return None

        tt = map_conn(entry.get('tside_thread'))
        tg = map_gender(entry.get('tside_gender'))
        ct = map_conn(entry.get('cside_thread'))
        cg = map_gender(entry.get('cside_gender'))

        if tp in ["type_telescope", "type_refractor", "type_camera_lens"]:
            aperture, focal_length = self._guess_optical_properties(name)
            bf_val = entry.get("bf_role") == "start"
            return Telescope(
                aperture or 80,
                focal_length or 500,
                vendor=vendor,
                connection_type=ct,
                connection_gender=cg or Gender.FEMALE,
                backfocus=ol if bf_val else None,
                mass=mass,
                optical_length=ol
            )

        if tp == "type_camera" or tp == "type_dslr":
            return Camera(
                23.5, 15.7, 6000, 4000, vendor=vendor,
                connection_type=tt, connection_gender=tg or Gender.FEMALE,
                backfocus=ol, mass=mass, optical_length=ol
            )

        if tp == "type_eyepiece":
            fl = self._extract_number(name) or 20
            return Eyepiece(fl, vendor=vendor, connection_type=tt, connection_gender=tg or Gender.MALE)

        if tp == "type_barlow":
            mag = self._extract_number(name, prefix="x") or 2.0
            return Barlow(
                mag, vendor=vendor, connection_type=tt,
                in_gender=tg or Gender.MALE, out_gender=cg or Gender.FEMALE,
                mass=mass, optical_length=ol
            )

        if tp == "type_reducer":
            mag = self._extract_number(name, suffix="x") or 0.8
            return Reducer(
                vendor,
                magnification=mag,
                optical_length=ol,
                mass=mass,
                required_backfocus=55, # Defaulting to 55mm
                in_connection_type=tt,
                out_connection_type=ct,
                in_gender=tg or Gender.MALE,
                out_gender=cg or Gender.FEMALE
            )

        if tp == "type_flattener":
            return Flattener(
                vendor, optical_length=ol, mass=mass, required_backfocus=55,
                in_connection_type=tt, out_connection_type=ct,
                in_gender=tg or Gender.MALE,
                out_gender=cg or Gender.FEMALE
            )

        if tp == "type_corrector":
            return Corrector(
                vendor, optical_length=ol, mass=mass, required_backfocus=55,
                in_connection_type=tt, out_connection_type=ct,
                in_gender=tg or Gender.MALE,
                out_gender=cg or Gender.FEMALE
            )

        if tp == 'type_diagonal':
            return Diagonal(vendor=vendor, connection_type=tt, optical_length=ol, mass=mass)

        if tp == 'type_filter_wheel':
            return FilterWheel(
                vendor, optical_length=ol, mass=mass,
                in_connection_type=tt, out_connection_type=ct,
                in_gender=tg or Gender.MALE,
                out_gender=cg or Gender.FEMALE
            )

        if tp == 'type_filter_holder':
            return FilterHolder(
                vendor, optical_length=ol, mass=mass,
                in_connection_type=tt, out_connection_type=ct,
                in_gender=tg or Gender.MALE,
                out_gender=cg or Gender.FEMALE
            )

        if tp == 'type_oag':
            return OAG(
                vendor, optical_length=ol, mass=mass,
                in_connection_type=tt, out_connection_type=ct,
                in_gender=tg or Gender.MALE,
                out_gender=cg or Gender.FEMALE
            )

        if tp == 'type_rotator':
            return Rotator(
                vendor, optical_length=ol, mass=mass,
                in_connection_type=tt, out_connection_type=ct,
                in_gender=tg or Gender.MALE,
                out_gender=cg or Gender.FEMALE
            )

        if tp == 'type_focuser':
            return Focuser(
                vendor, optical_length=ol, mass=mass,
                in_connection_type=tt, out_connection_type=ct,
                in_gender=tg or Gender.MALE,
                out_gender=cg or Gender.FEMALE
            )

        if tp == 'type_adapter':
            return Adapter(
                vendor, optical_length=ol, mass=mass,
                in_connection_type=tt, out_connection_type=ct,
                in_gender=tg or Gender.MALE,
                out_gender=cg or Gender.FEMALE
            )

        if tp == 'type_spacer':
            return Spacer(
                vendor, optical_length=ol, mass=mass,
                in_connection_type=tt, out_connection_type=ct,
                in_gender=tg or Gender.MALE,
                out_gender=cg or Gender.FEMALE
            )

        if tp == 'type_anti_tilt':
            return AntiTilt(
                vendor, optical_length=ol, mass=mass,
                in_connection_type=tt, out_connection_type=ct,
                in_gender=tg or Gender.MALE,
                out_gender=cg or Gender.FEMALE
            )

        if tp == 'type_flip_mirror':
            return FlipMirror(
                vendor, optical_length=ol, mass=mass,
                in_connection_type=tt, out_connection_type=ct,
                in_gender=tg or Gender.MALE,
                out_gender=cg or Gender.FEMALE
            )

        if tp == 'type_guide_scope':
            aperture, focal_length = self._guess_optical_properties(name)
            return GuideScope(
                aperture or 30, focal_length or 120, vendor=vendor,
                connection_type=ct, connection_gender=cg or Gender.FEMALE,
                mass=mass, optical_length=ol
            )

        return None

    def _extract_number(self, s: str, prefix: str = '', suffix: str = '') -> Optional[float]:
        pattern = f"{prefix}(\\d+\\.?\\d*){suffix}"
        match = re.search(pattern, s)
        if match:
            return float(match.group(1))
        return None

    def _guess_optical_properties(self, name: str):
        # Very simple heuristic
        aperture = None
        focal_length = None

        # Match 80ED, 100ED etc
        match = re.search(r'(\d+)ED', name)
        if match:
            aperture = float(match.group(1))

        # Match C8, C11
        match = re.search(r'C(\d+)', name)
        if match:
            inches = float(match.group(1))
            if inches < 20: # Heuristic for SCTs
                aperture = inches * 25.4

        # Match 135mm f/2
        match = re.search(r'(\d+)mm', name)
        if match:
            val = float(match.group(1))
            if val > 10:
                if 'f/' in name:
                    focal_length = val
                else:
                    aperture = val

        return aperture, focal_length
