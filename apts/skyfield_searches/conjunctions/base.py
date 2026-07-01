from skyfield.searchlib import find_minima

from ...cache import get_timescale
from ...utils import planetary
from ..utils import _refine_conjunction


def find_conjunctions(
    observer,
    p1_name,
    p2_name,
    start_date,
    end_date,
    threshold_degrees=None,
):
    ts = get_timescale()
    t0 = ts.utc(start_date)
    t1 = ts.utc(end_date)

    p1 = planetary.get_skyfield_obj(p1_name)
    p2 = planetary.get_skyfield_obj(p2_name)

    def separation(t):
        # Use topocentric apparent positions to account for aberration and light deflection
        p1_obs = observer.at(t).observe(p1).apparent()
        p2_obs = observer.at(t).observe(p2).apparent()
        return p1_obs.separation_from(p2_obs).degrees

    # Dynamically adjust step size based on moving bodies
    # Moon moves ~13 deg/day, Mercury ~1.3 deg/day
    if "moon" in [p1_name.lower(), p2_name.lower()]:
        step = 0.05  # ~1.2 hours
    elif any(p in [p1_name.lower(), p2_name.lower()] for p in ["mercury", "venus"]):
        step = 0.2  # ~4.8 hours
    else:
        step = 0.5  # ~12 hours

    setattr(separation, "step_days", step)

    times, separations = find_minima(t0, t1, separation)

    events = []
    for t, s in zip(times, separations):
        if threshold_degrees is None or s < threshold_degrees:
            # Refine conjunction time and separation
            refined_t, refined_s = _refine_conjunction(observer, p1, p2, t)
            events.append(
                {
                    "date": refined_t.utc_datetime(),
                    "separation_degrees": float(refined_s),
                }
            )

    return events
