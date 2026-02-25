from .base import Camera
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

if not hasattr(Camera, '_DATABASE') or Camera._DATABASE is None:
    Camera._DATABASE = {}
for module in _VENDOR_MODULES:
    for name, obj in vars(module).items():
        if isinstance(obj, type) and issubclass(obj, Camera) and obj is not Camera:
            if hasattr(obj, '_DATABASE'):
                Camera._DATABASE.update(obj._DATABASE)
            for attr_name in vars(obj):
                if attr_name.startswith('__') or attr_name == '_DATABASE':
                    continue
                attr_val = getattr(obj, attr_name)
                if callable(attr_val):
                    setattr(Camera, attr_name, attr_val)
