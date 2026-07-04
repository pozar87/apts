
import numpy as np
from skyfield.api import Star
from skyfield.searchlib import find_minima
from datetime import timedelta

from ..cache import get_timescale
from ..utils import planetary

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
        # Get positions of all bodies
        # If t is a Time object with multiple times, observer.at(t) returns multiple positions
        obs = observer.at(t)
        positions = [obs.observe(b[1]).apparent() for b in bodies]

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

    # Step size: Moon moves ~13 deg/day. 5 degrees threshold -> 0.1 days step is safe.
    setattr(max_separation, 'step_days', 0.1)

    times, values = find_minima(t0, t1, max_separation)

    events = []
    for t, val in zip(times, values):
        if val < threshold_degrees * 2: # heuristic for group diameter
            # Refine if needed, but let's keep it simple for now
            events.append({
                "date": t.utc_datetime(),
                "objects": [b[0] for b in bodies],
                "max_separation_degrees": float(val),
                "type": "Celestial Grouping"
            })
    return events

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
