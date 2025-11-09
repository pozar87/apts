import gettext
import os
import threading

# Use thread-local data to store the translation object for the current thread
_thread_local = threading.local()

localedir = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'locale')

def set_language(language='en'):
    """
    Sets the language for the current user/thread.
    Supported languages can be passed (e.g., 'pl').
    Defaults to English if the language is not supported or not found.
    """
    # Use NullTranslations as a fallback for English (or if no language is provided)
    if language == 'en' or not language:
        translation = gettext.NullTranslations()
    else:
        try:
            translation = gettext.translation('messages', localedir, languages=[language])
        except FileNotFoundError:
            # Fallback to English if a translation file for the given language is not found
            translation = gettext.NullTranslations()

    _thread_local.translation = translation

def gettext_(message):
    """
    Translates the given message using the language set for the current thread.
    """
    if not hasattr(_thread_local, 'translation'):
        # Default to English if no language has been set for the thread
        set_language('en')

    return _thread_local.translation.gettext(message)

# Initialize with a default language for the main thread
set_language('en')
