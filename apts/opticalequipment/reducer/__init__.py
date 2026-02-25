from .base import Reducer, Flattener, Corrector
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

if not hasattr(Reducer, '_DATABASE') or Reducer._DATABASE is None:
    Reducer._DATABASE = {}
for module in _VENDOR_MODULES:
    for name, obj in vars(module).items():
        if isinstance(obj, type) and issubclass(obj, Reducer) and obj is not Reducer:
            if hasattr(obj, '_DATABASE'):
                Reducer._DATABASE.update(obj._DATABASE)
            for attr_name in vars(obj):
                if attr_name.startswith('__') or attr_name == '_DATABASE':
                    continue
                attr_val = getattr(obj, attr_name)
                if callable(attr_val):
                    setattr(Reducer, attr_name, attr_val)

if not hasattr(Flattener, '_DATABASE') or Flattener._DATABASE is None:
    Flattener._DATABASE = {}
for module in _VENDOR_MODULES:
    for name, obj in vars(module).items():
        if isinstance(obj, type) and issubclass(obj, Flattener) and obj is not Flattener:
            if hasattr(obj, '_DATABASE'):
                Flattener._DATABASE.update(obj._DATABASE)
            for attr_name in vars(obj):
                if attr_name.startswith('__') or attr_name == '_DATABASE':
                    continue
                attr_val = getattr(obj, attr_name)
                if callable(attr_val):
                    setattr(Flattener, attr_name, attr_val)

if not hasattr(Corrector, '_DATABASE') or Corrector._DATABASE is None:
    Corrector._DATABASE = {}
for module in _VENDOR_MODULES:
    for name, obj in vars(module).items():
        if isinstance(obj, type) and issubclass(obj, Corrector) and obj is not Corrector:
            if hasattr(obj, '_DATABASE'):
                Corrector._DATABASE.update(obj._DATABASE)
            for attr_name in vars(obj):
                if attr_name.startswith('__') or attr_name == '_DATABASE':
                    continue
                attr_val = getattr(obj, attr_name)
                if callable(attr_val):
                    setattr(Corrector, attr_name, attr_val)
