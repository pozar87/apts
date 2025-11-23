import unittest
from unittest.mock import patch, mock_open, MagicMock
from apts.config import (
    load_config,
    get_cache_settings,
    set_redis_location,
    add_config_path,
    remove_config_path,
)


class ConfigTest(unittest.TestCase):
    def test_redis_location_from_ini(self):
        config_content = """
        [cache]
        backend = redis
        redis_location = redis://test-server:6379
        """
        fake_config_path = "/fake/path/for/this/test/apts.ini"
        try:
            with patch("builtins.open", mock_open(read_data=config_content)):
                with patch("os.path.exists", return_value=True):
                    add_config_path(fake_config_path, priority=True)
                    load_config()
                    settings = get_cache_settings()

            self.assertEqual(settings["backend"], "redis")
            self.assertEqual(settings["redis_location"], "redis://test-server:6379")
        finally:
            # Clean up
            remove_config_path(fake_config_path)
            load_config()  # Reload original config

    def test_set_redis_location_override(self):
        config_content = """
        [cache]
        backend = redis
        """
        fake_config_path = "/fake/path/for/this/test/apts.ini"
        try:
            with patch("builtins.open", mock_open(read_data=config_content)):
                with patch("os.path.exists", return_value=True):
                    add_config_path(fake_config_path, priority=True)
                    load_config()
                    set_redis_location("redis://new-server:6379")
                    settings = get_cache_settings()

            self.assertEqual(settings["redis_location"], "redis://new-server:6379")
        finally:
            # Clean up
            remove_config_path(fake_config_path)
            load_config()  # Reload original config


    @patch('apts.weather_providers.requests_cache.CachedSession')
    def test_redis_connection_fallback(self, mock_cached_session):
        # Import redis and its exception class for mocking
        try:
            from redis.exceptions import ConnectionError as RedisConnectionError
        except ImportError:
            self.skipTest("redis library not installed")

        # Mock the side effect of CachedSession to raise a ConnectionError
        # when called with a 'url' kwarg, but succeed otherwise.
        def session_side_effect(name, **kwargs):
            if 'url' in kwargs:
                # Simulate the real behavior: the connection is lazy, so the error
                # happens on the first cache access, not on creation.
                mock_session_instance = MagicMock()
                mock_session_instance.cache.get_response.side_effect = RedisConnectionError
                return mock_session_instance
            else:
                # Return a non-raising mock for the in-memory fallback
                return MagicMock()

        mock_cached_session.side_effect = session_side_effect

        # Manually reset the global session to ensure get_session runs its logic
        import apts.weather_providers
        apts.weather_providers.session = None

        # Configure apts to use redis
        set_redis_location("redis://nonexistent-server:6379")
        config_content = """
        [cache]
        backend = redis
        redis_location = redis://nonexistent-server:6379
        """
        fake_config_path = "/fake/path/for/this/test/apts.ini"
        try:
            with patch("builtins.open", mock_open(read_data=config_content)):
                 with patch("os.path.exists", return_value=True):
                    add_config_path(fake_config_path, priority=True)
                    load_config()

                    # This call should now trigger the fallback logic
                    with self.assertLogs('apts.weather_providers', level='WARNING') as cm:
                        session = apts.weather_providers.get_session()
                        self.assertIn("Redis connection failed", cm.output[0])
                        self.assertIn("Falling back to in-memory cache", cm.output[0])

            # Verify that CachedSession was first called for Redis, then for in-memory
            self.assertEqual(mock_cached_session.call_count, 2)

            # First call is for Redis
            first_call_args, first_call_kwargs = mock_cached_session.call_args_list[0]
            self.assertEqual(first_call_kwargs['backend'], 'redis')
            self.assertIn('url', first_call_kwargs)

            # Second call is the fallback to in-memory
            second_call_args, second_call_kwargs = mock_cached_session.call_args_list[1]
            self.assertEqual(second_call_kwargs['backend'], 'memory')
            self.assertNotIn('url', second_call_kwargs)

        finally:
            remove_config_path(fake_config_path)
            load_config()  # Reload original config
            apts.weather_providers.session = None # Clean up global state


if __name__ == "__main__":
    unittest.main()
