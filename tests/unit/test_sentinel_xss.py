import unittest
from apts.observations import Observation
from apts.place import Place
from apts.equipment import Equipment
from apts.opticalequipment import Telescope, Eyepiece

class TestXSS(unittest.TestCase):
    def test_equipment_table_xss_prevention(self):
        place = Place(52.2, 21.0, name="Warsaw")
        equipment = Equipment()
        # Malicious vendor name
        malicious_telescope = Telescope(vendor='<script>alert("XSS")</script>', aperture=100, focal_length=1000)
        eyepiece = Eyepiece(focal_length=25)
        equipment.register(malicious_telescope)
        equipment.register(eyepiece)

        obs = Observation(place, equipment)
        html_output = obs.to_html()

        # Check that the script tag is NOT present in its raw form
        self.assertNotIn('<script>alert("XSS")</script>', html_output, "VULNERABLE: Raw script tag found in HTML output!")
        # Check that it IS escaped
        self.assertIn('&lt;script&gt;alert("XSS")&lt;/script&gt;', html_output, "Script tag was not correctly escaped.")

if __name__ == "__main__":
    unittest.main()
