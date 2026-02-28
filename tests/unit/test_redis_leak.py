
import logging
import unittest
from unittest.mock import patch, MagicMock
from apts.weather_providers import get_session, reset_session

class TestRedisLeak(unittest.TestCase):
    def setUp(self):
        reset_session()
        # Configure logging to capture warnings
        self.log_capture = []
        class CaptureHandler(logging.Handler):
            def __init__(self, capture_list):
                super().__init__()
                self.capture_list = capture_list
            def emit(self, record):
                self.capture_list.append(record.getMessage())

        self.handler = CaptureHandler(self.log_capture)
        # Ensure we capture from the correct logger
        self.logger = logging.getLogger("apts.weather_providers")
        self.logger.addHandler(self.handler)
        self.logger.setLevel(logging.WARNING)

    def tearDown(self):
        self.logger.removeHandler(self.handler)
        reset_session()

    @patch("apts.weather_providers.get_cache_settings")
    @patch("requests_cache.CachedSession")
    def test_redis_connection_leak_is_masked(self, mock_session, mock_get_cache_settings):
        # Sensitive Redis URL
        sensitive_url = "redis://:secret_password@localhost:9999/0"
        mock_get_cache_settings.return_value = {
            "backend": "redis",
            "expire_after": 300,
            "redis_location": sensitive_url
        }

        # Mock CachedSession to fail when get_response is called
        # simulate an exception that contains the full connection string
        mock_session_instance = mock_session.return_value
        mock_session_instance.cache.get_response.side_effect = Exception(f"Failed to connect to {sensitive_url}")

        # Mock redis module to avoid ImportError if not installed
        with patch.dict("sys.modules", {"redis": MagicMock()}):
            get_session()

        # Check that the secret_password is NOT in the logs
        leaked = any("secret_password" in msg for msg in self.log_capture)
        self.assertFalse(leaked, f"Sensitive Redis password leaked in logs: {self.log_capture}")

        # Check that the masked version IS in the logs
        masked_found = any("redi...99/0" in msg for msg in self.log_capture)
        self.assertTrue(masked_found, f"Masked Redis URL not found in logs: {self.log_capture}")

if __name__ == "__main__":
    unittest.main()
