import math
import logging

logger = logging.getLogger(__name__)

def dist(s1, s2):
    return math.sqrt((s1["x"] - s2["x"]) ** 2 + (s1["y"] - s2["y"]) ** 2)

def get_target_neighbors(prev_target, prev_stars):
    # Use only high-confidence stars (high flux) for neighbors to be robust against noise
    min_flux = prev_target.get("flux", 0) * 0.1
    candidates = []
    x_t, y_t = prev_target["x"], prev_target["y"]

    # PERFORMANCE OPTIMIZATION:
    # 1. Avoid calculating distance twice (previously done in the list comprehension filter and sort key).
    # 2. Avoid distance to self (s is prev_target).
    # 3. Use inline math instead of function call overhead where possible, and avoid sqrt on rejection.
    for s in prev_stars:
        if s.get("flux", 0) <= min_flux:
            continue
        dx = s["x"] - x_t
        dy = s["y"] - y_t
        dist_sq = dx * dx + dy * dy
        if dist_sq > 1.0:  # 1.0 squared is 1.0
            d = math.sqrt(dist_sq)
            candidates.append((d, s))

    # Sort candidates by precomputed distance to avoid sorting key lambda function overhead
    candidates.sort(key=lambda item: item[0])

    # Return the top 5 closest neighbors
    return [item[1] for item in candidates[:5]]

def match_asterism(s_curr, prev_target, target_to_neighbors_dists, current_stars):
    # Guard against empty target neighbor distances
    if not target_to_neighbors_dists:
        return 0

    # Also consider flux similarity
    flux_ratio = s_curr.get("flux", 0) / prev_target.get("flux", 1)
    if flux_ratio < 0.5 or flux_ratio > 2.0:
        # Too much flux difference, likely not the same star
        return 0

    # PERFORMANCE OPTIMIZATION:
    # Since target_to_neighbors_dists is sorted in ascending order, the last element is the maximum d_target.
    # In the loop below, as soon as d_curr > d_target * 1.1, the loop breaks.
    # So any d_curr > max_d_target * 1.1 can never be matched.
    # We can pre-calculate this maximum limit and its square (max_limit_sq).
    # By checking `dx * dx + dy * dy <= max_limit_sq` first, we can skip `math.sqrt` entirely
    # for all stars that are further away. This prunes almost all stars in the frame instantly!
    max_limit = target_to_neighbors_dists[-1] * 1.1
    max_limit_sq = max_limit * max_limit

    curr_neighbors_dists = []
    x_curr, y_curr = s_curr["x"], s_curr["y"]
    for other in current_stars:
        if other is s_curr:
            continue
        dx = x_curr - other["x"]
        dy = y_curr - other["y"]
        dist_sq = dx * dx + dy * dy
        if dist_sq <= max_limit_sq and dist_sq > 1.0:
            curr_neighbors_dists.append(math.sqrt(dist_sq))

    curr_neighbors_dists.sort()

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
