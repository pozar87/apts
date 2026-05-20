from typing import Any

from .planetary import MINOR_PLANET_NAMES
from .coordinates import decdeg2dms, dms2decdeg
from .date import format_date, date_format
from .graph import find_all_paths
from .text import sanitize_header, extract_number, mask_secret
from .equipment import ConnectionType, Gender, map_conn, map_gender, guess_optical_properties
from .plot import PlotUtils

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
]


def __getattr__(name: str) -> Any:
    if name == "ureg":
        from ..units import ureg
        return ureg
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
    extract_number = staticmethod(extract_number)
    guess_optical_properties = staticmethod(guess_optical_properties)
