
import time
import pandas as pd
from apts.place import Place
from apts.catalogs import Catalogs
from apts.discovery import DiscoveryService
from apts.equipment_database import EquipmentDatabase
from apts.equipment import Equipment
from apts.units import get_unit_registry
import cProfile
import pstats

def main():
    ureg = get_unit_registry()
    place = Place(lat=52.216, lon=21.0, elevation=100)
    catalogs = Catalogs()

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

    print("Profiling DiscoveryService.get_top_picks...")
    profiler = cProfile.Profile()
    profiler.enable()
    top_picks = DiscoveryService.get_top_picks(place, equipment, catalogs)
    profiler.disable()

    stats = pstats.Stats(profiler).sort_stats('cumulative')
    stats.print_stats(20)

    # Check specifically for get_imaging_window
    print("\nStats for get_imaging_window:")
    stats.print_stats('get_imaging_window')

if __name__ == "__main__":
    main()
