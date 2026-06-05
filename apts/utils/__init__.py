from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from ..units import ureg

from .coordinates import decdeg2dms, dms2decdeg
from .date import date_format, format_date
from .equipment import (
    ConnectionType,
    Gender,
    get_default_gender,
    guess_optical_properties,
    map_conn,
    map_gender,
)
from .graph import find_all_paths
from .planetary import MINOR_PLANET_NAMES
from .plot import PlotUtils
from .text import extract_number, mask_secret, sanitize_header

__all__ = [
    "ureg",
    "MINOR_PLANET_NAMES",
    "decdeg2dms",
    "dms2decdeg",
    "format_date",
    "date_format",
    "find_all_paths",
    "sanitize_header",
    "extract_number",
    "mask_secret",
    "ConnectionType",
    "Gender",
    "map_conn",
    "map_gender",
    "guess_optical_properties",
    "get_default_gender",
    "optics",  # pyright: ignore[reportUnsupportedDunderAll]
]


def __getattr__(name: str) -> Any:
    if name == "ureg":
        from ..units import ureg

        return ureg
    if name == "optics":
        from ..optics import calculations as optics

        return optics
    raise AttributeError(f"module {__name__} has no attribute {name}")


class Utils:
    find_all_paths = staticmethod(find_all_paths)
    decdeg2dms = staticmethod(decdeg2dms)
    dms2decdeg = staticmethod(dms2decdeg)
    format_date = staticmethod(format_date)
    sanitize_header = staticmethod(sanitize_header)
    plot_to_bytes = staticmethod(PlotUtils.plot_to_bytes)
    date_format = staticmethod(date_format)
    mask_secret = staticmethod(mask_secret)
    annotate_plot = staticmethod(PlotUtils.annotate_plot_simple)
    map_conn = staticmethod(map_conn)
    map_gender = staticmethod(map_gender)
    get_default_gender = staticmethod(get_default_gender)
    extract_number = staticmethod(extract_number)
    guess_optical_properties = staticmethod(guess_optical_properties)
