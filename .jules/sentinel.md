## 2025-01-30 - Generalized Secret Masking in Configuration
**Vulnerability:** Configuration secrets (like SMTP passwords and API keys) were only masked in one specific section ("weather") when logging. Other sections containing credentials could accidentally leak secrets if logged.
**Learning:** Hardcoded section checks for masking are fragile and easily missed when adding new features or sections.
**Prevention:** Implement generalized masking in the configuration loading logic that iterates through all sections and applies keyword-based redaction (e.g., "api_key", "password") to protect secrets across the entire application.

## 2025-01-30 - Sensitive Data Exposure in API Exceptions
**Vulnerability:** Exceptions raised by libraries like `requests` often include the full URL in the error message. If the API key is passed as a query parameter (as in NASA API), it can be leaked in logs when a request fails.
**Learning:** `response.raise_for_status()` can expose sensitive parameters in logs if the resulting exception is not handled with security in mind.
**Prevention:** Wrap API calls in try-except blocks and use masking utilities to scrub secrets from exception messages before logging. Re-raise the exception after scrubbing to preserve application logic.
