import re
from typing import Optional, Any

def sanitize_header(value: str) -> str:
    """Removes newlines to prevent header injection and crashes."""
    if not value:
        return ""
    return str(value).replace("\n", "").replace("\r", "")


def mask_secret(secret: Any) -> str:
    from ..secrets import mask_secret as internal_mask_secret

    return internal_mask_secret(secret)


def extract_number(s: str, prefix: str = "", suffix: str = "") -> Optional[float]:
    pattern = f"{prefix}(\\d+\\.?\\d*){suffix}"
    match = re.search(pattern, s)
    if match:
        return float(match.group(1))
    return None
