from typing import Any, Iterable, Union
import urllib.parse


def mask_secret(secret: Any) -> str:
    if secret is None:
        return "None"
    s = str(secret)
    if not s or s == "None" or len(s) < 3:
        return s
    if len(s) <= 8:
        return "***"
    return f"{s[:4]}...{s[-4:]}"


def mask_text(text: Any, secret: Union[str, Iterable[str]]) -> str:
    if not text or not secret:
        return str(text)

    s_text = str(text)
    secrets = [secret] if isinstance(secret, str) else secret

    for s in secrets:
        if not s or s == "None" or len(str(s)) < 3:
            continue

        str_s = str(s)
        masked_s = mask_secret(str_s)

        # Replace literal secret
        s_text = s_text.replace(str_s, masked_s)

        # Replace URL-encoded variations
        # Use quote and quote_plus to cover common ways secrets might be encoded in URLs
        quoted = urllib.parse.quote(str_s)
        if quoted != str_s:
            s_text = s_text.replace(quoted, masked_s)

        quoted_plus = urllib.parse.quote_plus(str_s)
        if quoted_plus != str_s and quoted_plus != quoted:
            s_text = s_text.replace(quoted_plus, masked_s)

    return s_text
