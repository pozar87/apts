import os
import unittest
import tempfile
from unittest.mock import patch, mock_open
from apts.observations import Observation
from tests import setup_observation

class TestObservationTemplate(unittest.TestCase):
    def setUp(self):
        self.observation = setup_observation()
        self.default_template_content = """<!doctype html>
<html>
  <head>
    <style>
      body { color: #555; }
    </style>
  </head>
  <body>
    <h1>$title</h1>
    <p>$place_name</p>
  </body>
</html>"""
    
    @patch('builtins.open', new_callable=mock_open, read_data="<!doctype html><html><head><style>body{color:#555;}</style></head><body><h1>$title</h1><p>$place_name</p></body></html>")
    def test_to_html_default_template(self, mock_file):
        """Test that to_html uses the default template when no custom template is provided"""
        html = self.observation.to_html()
        
        # Verify that open was called with the default template path
        mock_file.assert_called_once()
        self.assertEqual(mock_file.call_args[0][0], Observation.NOTIFICATION_TEMPLATE)
        
        # Verify that the template contains the substituted values
        self.assertIn(self.observation.place.name, html)
        self.assertIn("APTS", html)
        
    @patch('builtins.open', new_callable=mock_open, read_data="<!doctype html><html><head><style>body{color:#555;}</style></head><body><h1>$title</h1><p>$place_name</p></body></html>")
    def test_to_html_custom_template(self, mock_file):
        """Test that to_html uses a custom template when provided"""
        custom_template = "/path/to/custom/template.html"
        html = self.observation.to_html(custom_template=custom_template)
        
        # Verify that open was called with the custom template path
        mock_file.assert_called_once_with(custom_template)
        
        # Verify that the template contains the substituted values
        self.assertIn(self.observation.place.name, html)
        self.assertIn("APTS", html)
    
    @patch('builtins.open', new_callable=mock_open, read_data="<!doctype html><html><head><style>body{color:#555;}</style></head><body><h1>$title</h1><p>$place_name</p></body></html>")
    def test_to_html_custom_css(self, mock_file):
        """Test that to_html injects custom CSS when provided"""
        custom_css = "h1 { color: blue; }"
        html = self.observation.to_html(css=custom_css)
        
        # Verify that the CSS was properly injected
        self.assertIn(custom_css, html)
        self.assertIn("body{color:#555;}", html)
        
    def test_to_html_with_actual_template_file(self):
        """Test to_html with an actual temporary template file"""
        # Create a temporary template file
        with tempfile.NamedTemporaryFile(mode='w+', delete=False) as temp_file:
            temp_file.write(self.default_template_content)
            temp_path = temp_file.name
        
        try:
            # Test with the actual file
            custom_css = "h1 { color: blue; }"
            html = self.observation.to_html(custom_template=temp_path, css=custom_css)
            
            # Verify that the template worked and CSS was injected
            self.assertIn(self.observation.place.name, html)
            self.assertIn("APTS", html)
            self.assertIn(custom_css, html)
            
        finally:
            # Clean up
            os.unlink(temp_path)

if __name__ == '__main__':
    unittest.main()