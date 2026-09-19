import importlib
import os
import pkgutil
from typing import Any, cast

from .base import Telescope
from .calculations import (
    normalize_telescope_database_entry as normalize_telescope_database_entry,
)
from .enums import TelescopeType, TubeMaterial

_VENDOR_MODULES = []
vendors_path = os.path.join(os.path.dirname(__file__), 'vendors')
for loader, module_name, is_pkg in pkgutil.iter_modules([vendors_path]):
    full_module_name = f'.vendors.{module_name}'
    try:
        module = importlib.import_module(full_module_name, __package__)
        _VENDOR_MODULES.append(module)
    except ImportError:
        continue

if getattr(TelescopeType, '_DATABASE', None) is None:
    TelescopeType._DATABASE = {}
for module in _VENDOR_MODULES:
    for name, obj in vars(module).items():
        if isinstance(obj, type) and issubclass(obj, TelescopeType) and obj is not TelescopeType:
            if hasattr(obj, '_DATABASE'):
                db = TelescopeType._DATABASE
                if isinstance(db, dict):
                    db.update(cast(Any, obj)._DATABASE)
            for attr_name in vars(obj):
                if attr_name.startswith('__') or attr_name == '_DATABASE':
                    continue
                attr_val = getattr(obj, attr_name)
                if callable(attr_val):
                    setattr(TelescopeType, attr_name, attr_val)

if getattr(TubeMaterial, '_DATABASE', None) is None:
    TubeMaterial._DATABASE = {}
for module in _VENDOR_MODULES:
    for name, obj in vars(module).items():
        if isinstance(obj, type) and issubclass(obj, TubeMaterial) and obj is not TubeMaterial:
            if hasattr(obj, '_DATABASE'):
                db = TubeMaterial._DATABASE
                if isinstance(db, dict):
                    db.update(cast(Any, obj)._DATABASE)
            for attr_name in vars(obj):
                if attr_name.startswith('__') or attr_name == '_DATABASE':
                    continue
                attr_val = getattr(obj, attr_name)
                if callable(attr_val):
                    setattr(TubeMaterial, attr_name, attr_val)

if not hasattr(Telescope, '_DATABASE') or Telescope._DATABASE is None:
    Telescope._DATABASE = {}
for module in _VENDOR_MODULES:
    for name, obj in vars(module).items():
        if isinstance(obj, type) and issubclass(obj, Telescope) and obj is not Telescope:
            if hasattr(obj, '_DATABASE'):
                Telescope._DATABASE.update(obj._DATABASE)
            for attr_name in vars(obj):
                if attr_name.startswith('__') or attr_name == '_DATABASE':
                    continue
                attr_val = getattr(obj, attr_name)
                if callable(attr_val):
                    setattr(Telescope, attr_name, attr_val)
