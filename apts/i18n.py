import gettext
import os

localedir = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'locale')
translate = gettext.translation('messages', localedir, languages=['pl'], fallback=True)
gettext_ = translate.gettext
