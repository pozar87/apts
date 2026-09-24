import importlib
import os
import pkgutil

from .base import Filter
from .calculations import normalize_filter_database_entry

_VENDOR_MODULES = []
vendors_path = os.path.join(os.path.dirname(__file__), "vendors")
for loader, module_name, is_pkg in pkgutil.iter_modules([vendors_path]):
    full_module_name = f".vendors.{module_name}"
    try:
        module = importlib.import_module(full_module_name, __package__)
        _VENDOR_MODULES.append(module)
    except ImportError:
        continue

if not hasattr(Filter, "_DATABASE") or Filter._DATABASE is None:
    Filter._DATABASE = {}
for module in _VENDOR_MODULES:
    for obj in vars(module).values():
        if isinstance(obj, type) and issubclass(obj, Filter) and obj is not Filter:
            if hasattr(obj, "_DATABASE"):
                Filter._DATABASE.update(obj._DATABASE)
            for attr_name in vars(obj):
                if attr_name.startswith("__") or attr_name == "_DATABASE":
                    continue
                attr_val = getattr(obj, attr_name)
                if callable(attr_val):
                    setattr(Filter, attr_name, attr_val)

__all__ = ["Filter", "normalize_filter_database_entry"]
