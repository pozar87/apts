from pint import UnitRegistry

_ureg = None


def get_unit_registry() -> UnitRegistry:
    global _ureg
    if _ureg is None:
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


ureg = get_unit_registry()
