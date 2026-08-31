from ..cache import get_ephemeris


def _get_observer(eph):
    """
    Returns a geocentric observer (Earth) from the ephemeris.
    Standard astronomical conjunctions and extrema are often defined geocentrically.
    """
    if eph is None:
        eph = get_ephemeris()
    # Check if eph is already an observer-like object (e.g. Earth + Topos)
    # or if it's the ephemeris dictionary.
    try:
        return eph["earth"]
    except (TypeError, KeyError):
        return eph
