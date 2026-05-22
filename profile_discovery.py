
import time
import pandas as pd
from apts.place import Place
from apts.catalogs import Catalogs
from apts.discovery import DiscoveryService
from apts.equipment_database import EquipmentDatabase
from apts.equipment import Equipment
from apts.units import get_unit_registry

def main():
    ureg = get_unit_registry()
    # Fixed elevation to avoid network call
    place = Place(lat=52.216, lon=21.0, elevation=100)
    catalogs = Catalogs()
    db = EquipmentDatabase()

    # Create a proper mock with units to avoid previous error
    from types import SimpleNamespace
    class MockEquipment:
        def label(self): return "Test Equipment"
        def effective_barlow(self): return 1.0
        @property
        def output(self):
            return SimpleNamespace(
                sensor_width=23.5 * ureg.mm,
                sensor_height=15.7 * ureg.mm
            )
        @property
        def telescope(self):
            return SimpleNamespace(focal_length=550 * ureg.mm)
    equipment = MockEquipment()

    # No warm up to see the impact of hoisted calculations
    start = time.time()
    top_picks = DiscoveryService.get_top_picks(place, equipment, catalogs)
    end = time.time()

    print(f"get_top_picks took {end - start:.4f} seconds")
    print(f"Found {len(top_picks)} top picks")
    if top_picks:
        print(f"Top pick: {top_picks[0]['Name']} with score {top_picks[0]['Score']}")

if __name__ == "__main__":
    main()
