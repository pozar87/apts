## 2025-02-12 - Centralized Secret Masking
**Vulnerability:** API keys and other secrets leaked in application logs at DEBUG level and in error messages (including full response bodies).
**Learning:** Secrets were interpolated into URLs and logged. Error messages from requests often include the full URL. Response bodies from providers often echo the provided API key on authentication failure.
**Prevention:** Use a centralized masking utility (apts/secrets.py) and centralized logging methods in base classes (like WeatherProvider) to automatically redact secrets from URLs and response bodies before they reach the logs.
