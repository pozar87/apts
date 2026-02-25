from .base import Eyepiece
import pkgutil
import importlib
import os

_VENDOR_MODULES = []
vendors_path = os.path.join(os.path.dirname(__file__), 'vendors')
for loader, module_name, is_pkg in pkgutil.iter_modules([vendors_path]):
    full_module_name = f'.vendors.{module_name}'
    try:
        module = importlib.import_module(full_module_name, __package__)
        _VENDOR_MODULES.append(module)
    except ImportError:
        continue

if not hasattr(Eyepiece, '_DATABASE') or Eyepiece._DATABASE is None:
    Eyepiece._DATABASE = {}
for module in _VENDOR_MODULES:
    for name, obj in vars(module).items():
        if isinstance(obj, type) and issubclass(obj, Eyepiece) and obj is not Eyepiece:
            if hasattr(obj, '_DATABASE'):
                Eyepiece._DATABASE.update(obj._DATABASE)
            for attr_name in vars(obj):
                if attr_name.startswith('__') or attr_name == '_DATABASE':
                    continue
                attr_val = getattr(obj, attr_name)
                if callable(attr_val):
                    setattr(Eyepiece, attr_name, attr_val)
