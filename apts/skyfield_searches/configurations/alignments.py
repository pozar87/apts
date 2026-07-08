
import numpy as np
from skyfield.searchlib import find_minima

from ...cache import get_timescale

def _calculate_collinearity_error(t, observer, bodies, max_span_degrees):
    """
    Helper to calculate the collinearity error (angular distance from the great circle)
    between three bodies at time t. Supports vectorized Time objects.
    """
    # Get unit vectors for all 3 bodies
    # We use astrometric positions for speed in search
    pos = [observer.at(t).observe(b[1]).position.au for b in bodies]

    def to_unit_vector(p):
        if p.ndim > 1:
            return p / np.linalg.norm(p, axis=0)
        return p / np.linalg.norm(p)

    vec = [to_unit_vector(p) for p in pos]

    # Great circle through bodies 1 and 3
    # Normal vector to the plane of 1 and 3
    if vec[0].ndim > 1:
        normal = np.cross(vec[0], vec[2], axis=0)
        norm_val = np.linalg.norm(normal, axis=0)
        # Avoid division by zero
        normal = np.divide(normal, norm_val, out=np.zeros_like(normal), where=norm_val > 1e-6)

        # Distance of body 2 from this plane
        # sin(dist) = vec[1] . normal
        # Sum over axis 0 for dot product
        sin_dist = np.abs(np.sum(vec[1] * normal, axis=0))
        error_deg = np.degrees(np.arcsin(np.clip(sin_dist, -1.0, 1.0)))

        # Total span between 1 and 3
        span = np.degrees(np.arccos(np.clip(np.sum(vec[0] * vec[2], axis=0), -1.0, 1.0)))
        error_deg = np.where(span > max_span_degrees, 90.0, error_deg)
        error_deg = np.where(norm_val < 1e-6, 90.0, error_deg)
        return error_deg
    else:
        normal = np.cross(vec[0], vec[2])
        norm_val = np.linalg.norm(normal)
        if norm_val < 1e-6: # Bodies 1 and 3 are coincident or opposite
                return 90.0

        normal /= norm_val

        # Distance of body 2 from this plane
        # sin(dist) = vec[1] . normal
        sin_dist = np.abs(np.dot(vec[1], normal))
        error_deg = np.degrees(np.arcsin(np.clip(sin_dist, -1.0, 1.0)))

        # Total span between 1 and 3
        span = np.degrees(np.arccos(np.clip(np.dot(vec[0], vec[2]), -1.0, 1.0)))
        if span > max_span_degrees:
            return 90.0

        return error_deg

def find_linear_alignments(observer, bodies, start_date, end_date, tolerance_degrees=1.0, max_span_degrees=60.0):
    """
    Finds times when 3 celestial bodies form a nearly straight line on the celestial sphere.

    bodies: list of exactly 3 (name, skyfield_obj)
    tolerance_degrees: how far the middle body can be from the great circle through the other two.
    max_span_degrees: maximum angular distance between the two outer bodies.
    """
    if len(bodies) != 3:
        raise ValueError("Linear alignment search requires exactly 3 bodies.")

    ts = get_timescale()
    t0 = ts.utc(start_date)
    t1 = ts.utc(end_date)

    def collinearity_error(t):
        return _calculate_collinearity_error(t, observer, bodies, max_span_degrees)

    setattr(collinearity_error, 'step_days', 0.5)

    times, values = find_minima(t0, t1, collinearity_error)

    events = []
    for t, val in zip(times, values):
        if val < tolerance_degrees:
            # Re-calculate with apparent positions for final result
            pos_app = [observer.at(t).observe(b[1]).apparent() for b in bodies]
            # Verify span
            span = pos_app[0].separation_from(pos_app[2]).degrees
            if span <= max_span_degrees:
                events.append({
                    "date": t.utc_datetime(),
                    "objects": [b[0] for b in bodies],
                    "alignment_error_degrees": float(val),
                    "span_degrees": float(span),
                    "type": "Linear Alignment"
                })
    return events
