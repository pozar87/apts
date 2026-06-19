from .base import config

def get_cache_settings() -> dict:
    """
    Reads the cache settings from the [cache] section.

    Returns:
        dict: A dictionary of cache-related settings.
    """
    cache_settings = {
        "backend": "memory",
        "expire_after": 300,
        "redis_location": None,
    }

    if config.has_section("cache"):
        if config.has_option("cache", "backend"):
            cache_settings["backend"] = config.get("cache", "backend")
        if config.has_option("cache", "expire_after"):
            cache_settings["expire_after"] = config.getint("cache", "expire_after")
        if config.has_option("cache", "redis_location"):
            cache_settings["redis_location"] = config.get("cache", "redis_location")

    return cache_settings


def set_redis_location(redis_location: str):
    """
    Overrides the redis location for the cache.
    """

    if not config.has_section("cache"):
        config.add_section("cache")
    config.set("cache", "redis_location", redis_location)
    config.set("cache", "backend", "redis")
