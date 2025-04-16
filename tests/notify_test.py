import unittest
from unittest.mock import patch, Mock, MagicMock, call
from apts.notify import Notify
from tests import setup_observation

class TestNotify(unittest.TestCase):
    def setUp(self):
        self.observation = setup_observation()
        # Create a mock observation with needed attributes
        self.mock_observation = MagicMock()
        self.mock_observation.place.name = "Test Location"
        
        # Setup the notify object
        self.notify = Notify('test@example.com')
        
    @patch('apts.notify.smtplib.SMTP')
    def test_send_with_default_template(self, mock_smtp):
        """Test that send uses the default template and no CSS by default"""
        # Setup mocks
        mock_smtp_instance = Mock()
        mock_smtp.return_value = mock_smtp_instance
        
        # Mock the to_html method
        self.mock_observation.to_html.return_value = "<html><body>Test</body></html>"
        
        # Patch the attach_image method to prevent it from being called
        with patch.object(Notify, 'attach_image'):
            # Call send with default parameters
            self.notify.send(self.mock_observation)
            
            # Verify to_html was called without custom template or CSS
            self.mock_observation.to_html.assert_called_once_with(custom_template=None, css=None)
            
            # Verify SMTP was called
            self.assertTrue(mock_smtp_instance.sendmail.called)
    
    @patch('apts.notify.smtplib.SMTP')
    def test_send_with_custom_template(self, mock_smtp):
        """Test that send passes custom template to to_html"""
        # Setup mocks
        mock_smtp_instance = Mock()
        mock_smtp.return_value = mock_smtp_instance
        
        # Mock the to_html method
        self.mock_observation.to_html.return_value = "<html><body>Custom Template</body></html>"
        
        custom_template = "/path/to/custom/template.html"
        
        # Patch the attach_image method to prevent it from being called
        with patch.object(Notify, 'attach_image'):
            # Call send with custom template
            self.notify.send(self.mock_observation, custom_template=custom_template)
            
            # Verify to_html was called with custom template
            self.mock_observation.to_html.assert_called_once_with(custom_template=custom_template, css=None)
            
            # Verify SMTP was called
            self.assertTrue(mock_smtp_instance.sendmail.called)
    
    @patch('apts.notify.smtplib.SMTP')
    def test_send_with_custom_css(self, mock_smtp):
        """Test that send passes custom CSS to to_html"""
        # Setup mocks
        mock_smtp_instance = Mock()
        mock_smtp.return_value = mock_smtp_instance
        
        # Mock the to_html method
        self.mock_observation.to_html.return_value = "<html><head><style>body{} h1{color:blue}</style></head><body>Custom CSS</body></html>"
        
        custom_css = "h1 { color: blue; }"
        
        # Patch the attach_image method to prevent it from being called
        with patch.object(Notify, 'attach_image'):
            # Call send with custom CSS
            self.notify.send(self.mock_observation, css=custom_css)
            
            # Verify to_html was called with custom CSS
            self.mock_observation.to_html.assert_called_once_with(custom_template=None, css=custom_css)
            
            # Verify SMTP was called
            self.assertTrue(mock_smtp_instance.sendmail.called)
    
    @patch('apts.notify.smtplib.SMTP')
    def test_send_with_custom_template_and_css(self, mock_smtp):
        """Test that send passes both custom template and CSS to to_html"""
        # Setup mocks
        mock_smtp_instance = Mock()
        mock_smtp.return_value = mock_smtp_instance
        
        # Mock the to_html method
        self.mock_observation.to_html.return_value = "<html><head><style>body{} h1{color:blue}</style></head><body>Custom Template and CSS</body></html>"
        
        custom_template = "/path/to/custom/template.html"
        custom_css = "h1 { color: blue; }"
        
        # Patch the attach_image method to prevent it from being called
        with patch.object(Notify, 'attach_image'):
            # Call send with custom template and CSS
            self.notify.send(self.mock_observation, custom_template=custom_template, css=custom_css)
            
            # Verify to_html was called with custom template and CSS
            self.mock_observation.to_html.assert_called_once_with(custom_template=custom_template, css=custom_css)
            
            # Verify SMTP was called
            self.assertTrue(mock_smtp_instance.sendmail.called)

if __name__ == '__main__':
    unittest.main()