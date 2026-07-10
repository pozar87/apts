
import numpy as np
from skyfield.searchlib import find_minima

from ...cache import get_timescale

def _get_max_separation_at_time(t, observer, bodies, use_apparent=False):
    """
    Helper to calculate the maximum angular separation between any pair of bodies at time t.
    Supports vectorized Time objects.
    """
    # Get positions of all bodies
    # If t is a Time object with multiple times, observer.at(t) returns multiple positions
    # Optimization: We use .observe() (astrometric position) by default instead of .apparent()
    # during the iterative minimization loop to avoid redundant coordinate
    # transformations (aberration, deflection). This is ~2x faster and
    # provides near-identical results for the minimization step.
    obs = observer.at(t)
    if use_apparent:
        positions = [obs.observe(b[1]).apparent() for b in bodies]
    else:
        positions = [obs.observe(b[1]) for b in bodies]

    # Calculate max pairwise separation
    if hasattr(t, 'shape') and t.shape:
        # Vectorized case: return an array of max separations for each time
        max_sep = np.zeros(t.shape)
        for i in range(len(positions)):
            for j in range(i + 1, len(positions)):
                sep = positions[i].separation_from(positions[j]).degrees
                max_sep = np.maximum(max_sep, sep)
        return max_sep
    else:
        # Scalar case
        max_sep = 0.0
        for i in range(len(positions)):
            for j in range(i + 1, len(positions)):
                sep = positions[i].separation_from(positions[j]).degrees
                if sep > max_sep:
                    max_sep = float(sep)
        return max_sep

def find_groupings(observer, bodies, start_date, end_date, threshold_degrees=5.0):
    """
    Finds times when multiple celestial bodies are grouped together.
    A grouping is defined as when all bodies are within 'threshold_degrees'
    of their angular centroid.

    bodies: list of (name, skyfield_obj)
    """
    if len(bodies) < 2:
        return []

    ts = get_timescale()
    t0 = ts.utc(start_date)
    t1 = ts.utc(end_date)

    def max_separation(t):
        return _get_max_separation_at_time(t, observer, bodies)

    # Step size: Moon moves ~13 deg/day. 5 degrees threshold -> 0.1 days step is safe.
    setattr(max_separation, 'step_days', 0.1)

    times, values = find_minima(t0, t1, max_separation)

    events = []
    for t, val in zip(times, values):
        if val < threshold_degrees * 2:  # heuristic for group diameter
            # Re-calculate with apparent positions for final result
            val_app = _get_max_separation_at_time(t, observer, bodies, use_apparent=True)
            events.append({
                "date": t.utc_datetime(),
                "objects": [b[0] for b in bodies],
                "max_separation_degrees": float(val_app),
                "type": "Celestial Grouping",
            })
    return events
