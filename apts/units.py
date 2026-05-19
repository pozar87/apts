from typing import Any, TYPE_CHECKING

if TYPE_CHECKING:
    from pint import UnitRegistry

_ureg = None


def get_unit_registry() -> "UnitRegistry":
    global _ureg
    if _ureg is None:
        from pint import UnitRegistry
        _ureg = UnitRegistry()
        # Define astronomical units that might not be in Pint by default
        _ureg.define("mag = [] = magnitude")  # Astronomical magnitude
        _ureg.define("hour = 60 * minute = h = hr")  # Hour for Right Ascension
        _ureg.define("AU = 149597870700 * meter = au")  # Astronomical Unit
        _ureg.define("arcsecond = degree / 3600 = arcsec")  # Arc second
    return _ureg


def set_unit_registry(registry):
    global _ureg
    _ureg = registry


class LazyUnitRegistry:
    """
    A lazy proxy for the Pint UnitRegistry.
    Delays the expensive initialization until the registry is actually accessed.
    """

    def __getattr__(self, name: str) -> Any:
        return getattr(get_unit_registry(), name)

    def __getitem__(self, key: Any) -> Any:
        return get_unit_registry()[key]

    def __call__(self, *args: Any, **kwargs: Any) -> Any:
        return get_unit_registry()(*args, **kwargs)

    def __iter__(self):
        return iter(get_unit_registry())

    def __dir__(self):
        return dir(get_unit_registry())

    def __repr__(self):
        if _ureg is None:
            return "<LazyUnitRegistry (uninitialized)>"
        return repr(_ureg)


# Export a lazy instance of the registry
ureg: Any = LazyUnitRegistry()
