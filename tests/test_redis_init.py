
import unittest
from unittest.mock import patch, MagicMock
from apts.config import set_redis_location, get_cache_settings, load_config, config
from apts.weather_providers import get_session, reset_session
import apts.weather_providers

class TestRedisInit(unittest.TestCase):
    def setUp(self):
        # Reset session and config before each test
        reset_session()
        config.clear()
        load_config()

    def test_set_redis_location_updates_backend(self):
        # Initially it should be memory (default)
        settings = get_cache_settings()
        self.assertEqual(settings["backend"], "memory")

        # Set redis location
        set_redis_location("redis://test-host:6379")

        settings = get_cache_settings()
        self.assertEqual(settings["redis_location"], "redis://test-host:6379")
        # Check if backend is also set to redis
        self.assertEqual(settings["backend"], "redis")

    @patch('requests_cache.CachedSession')
    def test_get_session_reinitializes_on_config_change(self, mock_session):
        # Ensure it returns a new mock each time
        mock_session.side_effect = lambda *args, **kwargs: MagicMock()

        # Initialize session once
        session1 = get_session()
        self.assertEqual(mock_session.call_count, 1)

        # Change config via set_redis_location
        set_redis_location("redis://new-host:6379")

        # Get session again - it should re-initialize because settings changed
        session2 = get_session()

        # Should have called CachedSession again
        self.assertGreater(mock_session.call_count, 1)
        self.assertIsNot(session1, session2)

    @patch('requests_cache.CachedSession')
    def test_get_session_caches_session_if_no_change(self, mock_session):
        # Initialize session
        session1 = get_session()
        call_count_after_first = mock_session.call_count

        # Get session again without change
        session2 = get_session()

        # Should be the same object and no new calls to CachedSession
        self.assertIs(session1, session2)
        self.assertEqual(mock_session.call_count, call_count_after_first)

if __name__ == "__main__":
    unittest.main()
