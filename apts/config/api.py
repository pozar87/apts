from .base import config

def get_api_key(service: str) -> str:
    """
    Reads the API key for a given service from the [api_keys] section.

    Args:
        service (str): The name of the service (e.g., 'nasa').

    Returns:
        str: The API key, or an empty string if not found.
    """
    return config.get("api_keys", f"{service}_api_key", fallback="")
