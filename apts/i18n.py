import gettext
import logging
import os
import threading
from contextlib import contextmanager
from typing import Optional

logger = logging.getLogger(__name__)

# Use thread-local data to store the translation object for the current thread
_thread_local = threading.local()

localedir = os.path.join(os.path.abspath(os.path.dirname(__file__)), "locale")


def set_language(language: Optional[str] = "en"):
    """
    Sets the language for the current user/thread.
    Supported languages can be passed (e.g., 'pl').
    Defaults to English if the language is not supported or not found.
    """
    logger.debug(f"Setting language to: {language}")
    # Use NullTranslations as a fallback for English (or if no language is provided)
    if language == "en" or not language:
        translation = gettext.NullTranslations()
        lang_code = "en"
    else:
        try:
            translation = gettext.translation(
                "messages", localedir, languages=[language]
            )
            lang_code = language
        except FileNotFoundError:
            # Fallback to English if a translation file for the given language is not found
            logger.warning(
                f"Translation file for language '{language}' not found. Falling back to English."
            )
            translation = gettext.NullTranslations()
            lang_code = "en"

    _thread_local.translation = translation
    _thread_local.language = lang_code


def get_language() -> str:
    """
    Returns the current language set for the thread.
    """
    if not hasattr(_thread_local, "language"):
        return "en"
    return _thread_local.language


def gettext_(message):
    """
    Translates the given message using the language set for the current thread.
    """
    if not hasattr(_thread_local, "translation"):
        # Default to English if no language has been set for the thread
        logger.debug("No language set for the current thread. Defaulting to English.")
        set_language("en")

    return _thread_local.translation.gettext(message)


# Initialize with a default language for the main thread
set_language("en")


@contextmanager
def language_context(language: Optional[str]):
    """
    A context manager to temporarily set the language for the current thread.
    """
    if language is None:
        yield
        return

    original_language = getattr(_thread_local, "language", "en")
    set_language(language)
    try:
        yield
    finally:
        set_language(original_language)
