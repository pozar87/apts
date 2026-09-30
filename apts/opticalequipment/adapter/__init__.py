import importlib
import os
import pkgutil

from .base import Adapter, Spacer
from .calculations import normalize_adapter_database_entry

_VENDOR_MODULES = []
vendors_path = os.path.join(os.path.dirname(__file__), "vendors")
for loader, module_name, is_pkg in pkgutil.iter_modules([vendors_path]):
    full_module_name = f".vendors.{module_name}"
    try:
        module = importlib.import_module(full_module_name, __package__)
        _VENDOR_MODULES.append(module)
    except ImportError:
        continue

if not hasattr(Adapter, "_DATABASE") or Adapter._DATABASE is None:
    Adapter._DATABASE = {}
for module in _VENDOR_MODULES:
    for obj in vars(module).values():
        if isinstance(obj, type) and issubclass(obj, Adapter) and obj is not Adapter:
            if hasattr(obj, "_DATABASE"):
                Adapter._DATABASE.update(obj._DATABASE)
            for attr_name in vars(obj):
                if attr_name.startswith("__") or attr_name == "_DATABASE":
                    continue
                attr_val = getattr(obj, attr_name)
                if callable(attr_val):
                    setattr(Adapter, attr_name, attr_val)

if not hasattr(Spacer, "_DATABASE") or Spacer._DATABASE is None:
    Spacer._DATABASE = {}
for module in _VENDOR_MODULES:
    for obj in vars(module).values():
        if isinstance(obj, type) and issubclass(obj, Spacer) and obj is not Spacer:
            if hasattr(obj, "_DATABASE"):
                Spacer._DATABASE.update(obj._DATABASE)
            for attr_name in vars(obj):
                if attr_name.startswith("__") or attr_name == "_DATABASE":
                    continue
                attr_val = getattr(obj, attr_name)
                if callable(attr_val):
                    setattr(Spacer, attr_name, attr_val)

__all__ = ["Adapter", "Spacer", "normalize_adapter_database_entry"]
