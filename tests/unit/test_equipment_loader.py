import unittest
from apts.equipment_database import EquipmentDatabase
from apts.opticalequipment import Telescope, Camera, SmartTelescope


class TestEquipmentLoader(unittest.TestCase):
    def test_search_and_create(self):
        db = EquipmentDatabase()

        # Search for Esprit 80ED
        results = db.find(brand="Sky-Watcher", name="Esprit 80ED")
        self.assertTrue(len(results) > 0)

        entry = results[0]
        obj = db.create_equipment(entry)

        self.assertIsInstance(obj, Telescope)
        self.assertEqual(obj.vendor, "Sky-Watcher Esprit 80ED")
        self.assertEqual(obj.aperture.magnitude, 80)

    def test_camera_loader(self):
        db = EquipmentDatabase()
        results = db.find(name="ASI2600MC Pro")
        self.assertTrue(len(results) > 0)

        obj = db.create_equipment(results[0])
        self.assertIsInstance(obj, Camera)
        self.assertEqual(obj.backfocus.magnitude, 6.5)

    def test_smart_telescope_loader(self):
        db = EquipmentDatabase()
        # Search for Dwarf II using equipment_type
        results = db.find(equipment_type="type_smart_telescope")
        self.assertTrue(len(results) > 0)

        # Filter specifically for Dwarf II to be sure
        dwarf_results = [r for r in results if "Dwarf II" in r["name"]]
        self.assertTrue(len(dwarf_results) > 0)

        obj = db.create_equipment(dwarf_results[0])
        self.assertIsInstance(obj, SmartTelescope)
        self.assertEqual(obj.vendor, "DwarfLab Dwarf II")
