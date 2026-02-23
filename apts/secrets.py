from typing import Any


def mask_secret(secret: Any) -> str:
    if secret is None:
        return "None"
    s = str(secret)
    if not s or s == "None" or len(s) < 3:
        return s
    if len(s) <= 8:
        return "***"
    return f"{s[:4]}...{s[-4:]}"


def mask_text(text: Any, secret: str) -> str:
    if not text or not secret or secret == "None" or len(secret) < 3:
        return str(text)
    s_text = str(text)
    return s_text.replace(secret, mask_secret(secret))
