from skyfield.api import load
import numpy as np
from scipy.optimize import brentq


def find_extrema(f, t0, t1, num_points=1000):
    """
    Finds the extrema of a function f over the interval [t0, t1]
    by finding the roots of its derivative.
    Returns a list of tuples (time, value, is_max).
    """
    ts = load.timescale()
    times = ts.linspace(t0, t1, num_points)

    # Approximate derivative
    dt = (t1 - t0) / num_points
    values = f(times)
    deriv = np.gradient(values, dt)

    # Find roots of the derivative
    root_indices = np.where(np.diff(np.sign(deriv)))[0]

    extrema = []
    for i in root_indices:
        try:
            # Refine root location
            def deriv_at(t):
                # Ensure t is float
                t_val = float(t)
                return np.gradient(
                    f(ts.tt(jd=[t_val - 0.01, t_val, t_val + 0.01])), 0.01
                )[1]

            t_root = brentq(deriv_at, float(times[i].tt), float(times[i + 1].tt))
            t_extremum = ts.tt(jd=t_root)
            v_extremum = f(t_extremum)

            # Check second derivative to determine if max or min
            def second_deriv_at(t):
                t_val = float(t)
                return np.gradient(
                    np.gradient(f(ts.tt(jd=[t_val - 0.01, t_val, t_val + 0.01])), 0.01),
                    0.01,
                )[1]

            is_max = second_deriv_at(t_root) < 0

            extrema.append((t_extremum, v_extremum, is_max))
        except (RuntimeError, ValueError):
            # brentq can fail if the root is not bracketed
            continue

    return extrema
