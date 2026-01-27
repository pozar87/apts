
import unittest
from apts.config import set_redis_location, get_cache_settings, load_config
from apts.weather_providers import get_session
import apts.weather_providers
from apts.config import config

class TestRedisConfig(unittest.TestCase):
    def setUp(self):
        # Reset session
        apts.weather_providers.session = None
        # Reset config
        config.clear()
        load_config()

    def test_set_redis_location_sets_backend(self):
        # Initially it should be memory (default)
        settings = get_cache_settings()
        self.assertEqual(settings["backend"], "memory")

        # Set redis location
        set_redis_location("redis://test-host:6379")

        settings = get_cache_settings()
        self.assertEqual(settings["redis_location"], "redis://test-host:6379")
        # Check if backend is also set to redis (this is what I suspect might be missing/needed)
        self.assertEqual(settings["backend"], "redis")

    def test_session_not_updated_after_initialization(self):
        # 1. Initialize session with default settings (memory)
        session1 = get_session()

        # 2. Update config to use redis
        # (Manually setting backend too for this test)
        if not config.has_section("cache"):
            config.add_section("cache")
        config.set("cache", "backend", "redis")
        set_redis_location("redis://localhost:6379")

        # 3. Get session again
        session2 = get_session()

        # It will be the same session object because it's cached in a global variable
        self.assertIs(session1, session2)

if __name__ == "__main__":
    unittest.main()
