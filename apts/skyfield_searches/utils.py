from datetime import timedelta
from typing import Any, cast

from skyfield.positionlib import Apparent
from skyfield.searchlib import find_minima

from ..cache import get_ephemeris, get_timescale


def fast_altaz(observer_at_times, skyfield_obj, temperature_C=None, pressure_mbar=None):
    """
    Fast AltAz calculation that bypasses expensive nutation, aberration, and
    light deflection calculations (Standard Apparent) by manually wrapping
    an Astrometric position in an Apparent object.

    This provides a ~2.5x speedup with a negligible accuracy loss (~14 arcseconds)
    due to missing nutation/aberration, which is ideal for visibility gating
    and coarse searching.
    """
    pos = observer_at_times.observe(skyfield_obj)
    app = Apparent(pos.position.au, pos.velocity.au_per_d, pos.t)
    app.center = pos.center
    return app.altaz(temperature_C=temperature_C, pressure_mbar=pressure_mbar)  # type: ignore[arg-type]


def _refine_conjunction(observer, obj1, obj2, rough_t):
    """
    Refines the time of a conjunction using iterative minimization.
    """
    ts = get_timescale()
    # Search within +/- 30 minutes of the rough time
    t0 = ts.from_datetime(rough_t.utc_datetime() - timedelta(minutes=30))
    t1 = ts.from_datetime(rough_t.utc_datetime() + timedelta(minutes=30))

    def separation_func(t):
        # Optimization: We use .observe() (astrometric position) instead of .apparent()
        # during the iterative minimization loop to avoid redundant coordinate
        # transformations (aberration, deflection). This is ~2x faster and
        # provides near-identical results for the minimization step.
        p1 = observer.at(t).observe(obj1)
        p2 = observer.at(t).observe(obj2)
        return p1.separation_from(p2).degrees

    setattr(separation_func, "step_days", 0.005)  # 7.2 minutes step for minimization
    times, _ = find_minima(t0, t1, separation_func)

    if len(times) > 0:
        # We perform a single high-precision .apparent() observation at the final
        # refined time to return the exact separation.
        res_t = times[0]
        p1 = observer.at(res_t).observe(obj1).apparent()
        p2 = observer.at(res_t).observe(obj2).apparent()
        return res_t, p1.separation_from(p2).degrees

    p1 = observer.at(rough_t).observe(obj1).apparent()
    p2 = observer.at(rough_t).observe(obj2).apparent()
    return rough_t, p1.separation_from(p2).degrees


def find_solar_longitude_time(t0, t1, target_longitude, epoch=None):
    """
    Finds the exact time when the Sun reaches a specific ecliptic longitude.
    Default epoch is J2000.0 if not specified.
    """
    eph = cast(Any, get_ephemeris())
    sun = eph["sun"]
    earth = eph["earth"]
    ts = get_timescale()
    target_epoch = epoch if epoch is not None else ts.utc(2000)

    def solar_longitude_at(t):
        # Solar longitude (λ⊙) is the ecliptic longitude of the Sun as seen from Earth.
        # It must be calculated for a geocentric observer (earth.at(t)) observing the Sun.
        # We use apparent position to include aberration and nutation, which is
        # the standard for λ⊙ used in meteor shower prediction (apparent geocentric).
        _, lon, _ = earth.at(t).observe(sun).apparent().ecliptic_latlon(target_epoch)
        return lon.degrees

    # We want to find where solar_longitude_at(t) == target_longitude
    # Since longitude wraps at 360, we use a difference function
    def longitude_difference(t):
        diff = solar_longitude_at(t) - target_longitude
        return (diff + 180) % 360 - 180

    def abs_diff(t):
        return abs(longitude_difference(t))

    setattr(abs_diff, "step_days", 1.0)
    times, _ = find_minima(t0, t1, abs_diff)

    return times[0] if len(times) > 0 else None
