from typing import overload, Literal, Tuple, Union, Any
import pandas as pd

@overload
def decdeg2dms(dd: Any, pretty: Literal[True]) -> str: ...
@overload
def decdeg2dms(
    dd: Any, pretty: Literal[False] = False
) -> Tuple[float, float, float]: ...
def decdeg2dms(
    dd: Any, pretty: bool = False
) -> Union[str, Tuple[float, float, float]]:
    is_pandas_series = hasattr(dd, "iloc")
    dd_val = dd.iloc[0] if is_pandas_series else dd
    mnt, sec = divmod(dd_val * 3600, 60)
    deg, mnt = divmod(mnt, 60)

    if pretty:
        return f"{int(deg)}°{int(mnt)}'{int(sec)}\""
    else:
        return deg, mnt, sec


def dms2decdeg(dms):
    deg, mnt, sec = dms
    return deg + mnt / 60 + sec / 3600


def parse_ra_to_hours(ra: Union[str, pd.Series]) -> Union[float, pd.Series, None]:
    """
    Parse RA in 'HH:MM:SS' format to decimal hours.
    Supports both scalar strings and Pandas Series.
    """
    if isinstance(ra, pd.Series):
        ras_split = ra.str.split(":", expand=True)
        for col in range(3):
            if col not in ras_split.columns:
                ras_split[col] = 0
        h_ra = pd.to_numeric(ras_split[0], errors="coerce")
        m_ra = pd.to_numeric(ras_split[1], errors="coerce").fillna(0)
        s_ra = pd.to_numeric(ras_split[2], errors="coerce").fillna(0)
        return h_ra + m_ra / 60.0 + s_ra / 3600.0

    if isinstance(ra, str):
        parts = ra.split(":")
        if len(parts) > 0:
            try:
                h = float(parts[0])
                m = float(parts[1]) if len(parts) > 1 else 0
                s = float(parts[2]) if len(parts) > 2 else 0
                return h + m / 60 + s / 3600
            except ValueError:
                return None
    return None


def parse_dec_to_degrees(dec: Union[str, pd.Series]) -> Union[float, pd.Series, None]:
    """
    Parse Dec in '+/-DD:MM:SS' format to decimal degrees.
    Supports both scalar strings and Pandas Series.
    """
    if isinstance(dec, pd.Series):
        decs_signs = dec.str.startswith("-", na=False).map({True: -1, False: 1})
        decs_split = dec.str.lstrip("+-").str.split(":", expand=True)
        for col in range(3):
            if col not in decs_split.columns:
                decs_split[col] = 0
        h_dec = pd.to_numeric(decs_split[0], errors="coerce")
        m_dec = pd.to_numeric(decs_split[1], errors="coerce").fillna(0)
        s_dec = pd.to_numeric(decs_split[2], errors="coerce").fillna(0)
        return decs_signs * (h_dec + m_dec / 60.0 + s_dec / 3600.0)

    if isinstance(dec, str):
        sign = -1 if dec.startswith("-") else 1
        parts = dec.lstrip("+-").split(":")
        if len(parts) > 0:
            try:
                d = float(parts[0])
                m = float(parts[1]) if len(parts) > 1 else 0
                s = float(parts[2]) if len(parts) > 2 else 0
                return sign * (d + m / 60 + s / 3600)
            except ValueError:
                return None
    return None
