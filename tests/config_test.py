import unittest
from unittest.mock import patch, mock_open
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


if __name__ == "__main__":
    unittest.main()
