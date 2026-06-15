import math
import logging

logger = logging.getLogger(__name__)

def dist(s1, s2):
    return math.sqrt((s1["x"] - s2["x"]) ** 2 + (s1["y"] - s2["y"]) ** 2)

def get_target_neighbors(prev_target, prev_stars):
    # Use only high-confidence stars (high flux) for neighbors to be robust against noise
    min_flux = prev_target.get("flux", 0) * 0.1
    neighbors = sorted(
        [
            s
            for s in prev_stars
            if dist(s, prev_target) > 1.0 and s.get("flux", 0) > min_flux
        ],
        key=lambda s: dist(s, prev_target),
    )[:5]  # Take up to 5 closest neighbors
    return neighbors

def match_asterism(s_curr, prev_target, target_to_neighbors_dists, current_stars):
    # Also consider flux similarity
    flux_ratio = s_curr.get("flux", 0) / prev_target.get("flux", 1)
    if flux_ratio < 0.5 or flux_ratio > 2.0:
        # Too much flux difference, likely not the same star
        return 0

    curr_neighbors_dists = sorted(
        [
            dist(s_curr, other)
            for other in current_stars
            if dist(s_curr, other) > 1.0
        ]
    )

    match_count = 0
    for d_target in target_to_neighbors_dists:
        # Find if any current neighbor distance matches d_target within tolerance (e.g. 10%)
        for d_curr in curr_neighbors_dists:
            if d_curr > d_target * 1.1:  # Too far
                break
            if abs(d_curr - d_target) < max(2.0, d_target * 0.10):
                match_count += 1
                break
    return match_count

def robust_star_tracking(prev_target, prev_stars, current_stars):
    """
    Attempts to find the target star in the current frame by comparing
    the local configuration of stars (asterism).
    """
    if len(prev_stars) < 3 or len(current_stars) < 3:
        return None

    neighbors = get_target_neighbors(prev_target, prev_stars)
    if not neighbors:
        return None

    # Precompute relative distances from target to neighbors in previous frame
    target_to_neighbors_dists = [dist(prev_target, n) for n in neighbors]

    # 2. For each star in the current frame, check if it has neighbors at similar distances
    best_star = None
    best_match_count = 0

    for s_curr in current_stars:
        m_count = match_asterism(
            s_curr, prev_target, target_to_neighbors_dists, current_stars
        )

        if m_count > best_match_count:
            best_match_count = m_count
            best_star = s_curr

    # We need a significant match (e.g. at least 2 neighbors matching distances)
    if best_match_count >= min(2, len(neighbors)):
        return best_star

    return None
