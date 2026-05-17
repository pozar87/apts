import logging
import requests_cache
from ..config import get_cache_settings
from ..secrets import mask_text

logger = logging.getLogger(__name__)

session = None
_last_cache_settings = None


def reset_session():
    """
    Resets the global session, closing it if it exists.
    """
    global session, _last_cache_settings
    if session is not None:
        try:
            session.close()
        except Exception as e:
            logger.debug(f"Error closing session: {e}")
    session = None
    _last_cache_settings = None


def get_session():
    global session, _last_cache_settings
    cache_settings = get_cache_settings()

    # If session exists, check if settings have changed
    if session is not None and cache_settings != _last_cache_settings:
        logger.info("Cache settings changed, resetting session.")
        reset_session()

    if session is None:
        _last_cache_settings = cache_settings
        kwargs = {
            "backend": cache_settings["backend"],
            "expire_after": cache_settings["expire_after"],
        }

        if cache_settings["backend"] == "redis" and cache_settings["redis_location"]:
            try:
                # These imports are here to avoid a hard dependency on redis
                # if the user doesn't use the redis backend.
                import redis  # type: ignore

                kwargs["connection"] = redis.from_url(cache_settings["redis_location"])
                # The connection is lazy, so we need to trigger it to test it.
                # A full 'ping' is too slow, so we just initialize the session
                # and let it fail on first use if it's going to. A try/except
                # here on the constructor would be better, but the connection
                # is lazy. Let's try to connect and fall back if it fails.
                temp_session = requests_cache.CachedSession(
                    "apts_cache_test_connection", **kwargs
                )
                temp_session.cache.get_response(
                    "test"
                )  # dummy call to force connection
                session = temp_session

            except (ImportError, Exception) as e:
                error_msg = mask_text(str(e), cache_settings["redis_location"])
                logger.warning(
                    f"Redis connection failed with error: {error_msg}. "
                    "Falling back to in-memory cache for this session."
                )
                kwargs.pop("connection", None)
                kwargs["backend"] = "memory"
                session = requests_cache.CachedSession("apts_cache", **kwargs)
        else:
            session = requests_cache.CachedSession("apts_cache", **kwargs)

    return session
