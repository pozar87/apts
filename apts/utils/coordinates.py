from typing import overload, Literal, Tuple, Union, Any

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
