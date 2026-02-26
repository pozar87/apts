import unittest
from unittest.mock import MagicMock, patch
from apts.notify import Notify

class TestSentinelSecurity(unittest.TestCase):
    def test_notify_str_masking(self):
        # Setup Notify with sensitive smtp_user
        recipient = "recipient@example.com"
        with patch('apts.notify.config') as mock_config:
            mock_config.get.side_effect = lambda section, option, fallback=None, **kwargs: \
                       "secret_user" if option == "smtp_user" else fallback
            mock_config.getint.return_value = 587
            mock_config.getboolean.return_value = True

            notify = Notify(recipient)
            notify_str = str(notify)
            self.assertIn("smtp_user='secr...user'", notify_str)
            self.assertNotIn("secret_user", notify_str)

    def test_notify_init_warning_masking(self):
        recipient = "recipient@example.com"
        with patch('apts.notify.config') as mock_config:
            mock_config.get.side_effect = lambda section, option, fallback=None, **kwargs: \
                       "secret_user" if option == "smtp_user" else (None if option == "smtp_host" else fallback)
            mock_config.getint.return_value = 587
            mock_config.getboolean.return_value = True

            with patch('apts.notify.logger.warning') as mock_warning:
                Notify(recipient)
                mock_warning.assert_called_once()
                warning_msg = mock_warning.call_args[0][0]
                self.assertIn("user ('secr...user')", warning_msg)
                self.assertNotIn("secret_user", warning_msg)

    @patch('apts.notify.smtplib.SMTP')
    @patch('apts.notify.logger.error')
    def test_notify_send_email_exception_masking(self, mock_logger_error, mock_smtp):
        recipient = "recipient@example.com"
        # Mock SMTP login to fail with an exception containing secrets
        mock_smtp_instance = mock_smtp.return_value
        mock_smtp_instance.login.side_effect = Exception("Error for user secret_user with password secret_pass")

        with patch('apts.notify.config') as mock_config:
            mock_config.get.side_effect = lambda section, option, fallback=None, **kwargs: \
                       "secret_user" if option == "smtp_user" else ("secret_pass" if option == "smtp_password" else ("smtp.host.com" if option == "smtp_host" else fallback))
            mock_config.getint.return_value = 587
            mock_config.getboolean.return_value = True

            notify = Notify(recipient)
            notify._send_email(MagicMock())

            # Check if logger.error was called with masked message
            # The exception masking should redact both user and password
            # It might be called multiple times, we want the one from the exception
            found = False
            for call_args in mock_logger_error.call_args_list:
                msg = call_args[0][0]
                if "Failed to send email" in msg:
                    self.assertIn("secr...user", msg)
                    self.assertIn("secr...pass", msg)
                    self.assertNotIn("secret_user", msg)
                    self.assertNotIn("secret_pass", msg)
                    found = True
            self.assertTrue(found, "Log message 'Failed to send email' not found")

if __name__ == "__main__":
    unittest.main()
