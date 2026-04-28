import logging
import numpy as np

logger = logging.getLogger(__name__)


def _get_jovian_moon_objects(eph):
    """
    Helper to get Galilean moon objects from ephemeris, handling different kernel IDs.
    """
    moon_map = {501: "Io", 502: "Europa", 503: "Ganymede", 504: "Callisto"}
    moon_objs = {}
    for moon_id in moon_map:
        try:
            moon_objs[moon_id] = eph[moon_id]
        except KeyError:
            # Fallback for jup300.bsp IDs (non-standard mapping)
            jup300_ids = {501: 55061, 502: 55062, 503: 55063, 504: 55064}
            logger.warning(
                f"ID {moon_id} not found in Jovian ephemeris. Falling back to non-standard ID {jup300_ids[moon_id]}."
            )
            moon_objs[moon_id] = eph[jup300_ids[moon_id]]
    return moon_map, moon_objs

def is_inside_ellipsoid_projection(p_vec, u_vec, z_pole, re, rp):
    """
    Checks if point p is within the projection of an ellipsoid along direction u.
    p and u are (3, N), z_pole is (3, N) or (3,).
    re: equatorial radius, rp: polar radius.
    """
    # Dots along z_pole
    if p_vec.ndim > 1:
        p_z = np.sum(p_vec * z_pole, axis=0)
        u_z = np.sum(u_vec * z_pole, axis=0)
        p_u = np.sum(p_vec * u_vec, axis=0)
        p_sq = np.sum(p_vec * p_vec, axis=0)
    else:
        p_z = np.dot(p_vec, z_pole)
        u_z = np.dot(u_vec, z_pole)
        p_u = np.dot(p_vec, u_vec)
        p_sq = np.dot(p_vec, p_vec)

    # Scaled space parameters
    p_prime_sq = (p_sq - p_z**2) / re**2 + p_z**2 / rp**2
    p_prime_u_prime = (p_u - p_z * u_z) / re**2 + (p_z * u_z) / rp**2
    u_prime_sq = (1.0 - u_z**2) / re**2 + u_z**2 / rp**2

    # Projected distance squared: |P'|^2 - (P' . U')^2 / |U'|^2
    return p_prime_sq - (p_prime_u_prime**2 / u_prime_sq) <= 1.000001
