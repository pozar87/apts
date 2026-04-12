from .base import Rotator
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


def _merge_vendors(base_cls):
    if not hasattr(base_cls, '_DATABASE') or base_cls._DATABASE is None:
        base_cls._DATABASE = {}
    for module in _VENDOR_MODULES:
        for name, obj in vars(module).items():
            if isinstance(obj, type) and issubclass(obj, base_cls) and obj is not base_cls:
                if hasattr(obj, '_DATABASE'):
                    base_cls._DATABASE.update(obj._DATABASE)
                for attr_name in vars(obj):
                    if attr_name.startswith('__') or attr_name == '_DATABASE':
                        continue
                    attr_val = getattr(obj, attr_name)
                    if callable(attr_val):
                        setattr(base_cls, attr_name, attr_val)


_merge_vendors(Rotator)

__all__ = ["Rotator"]
