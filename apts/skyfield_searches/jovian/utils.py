import logging
import numpy as np

logger = logging.getLogger(__name__)


def _get_observer_elevation(observer):
    """Extracts elevation from observer vector functions."""
    observer_elevation = 0
    for vf in observer.vector_functions:
        if hasattr(vf, "elevation"):
            observer_elevation = vf.elevation.m
            break
    return observer_elevation


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

class JovianSearchContext:
    """
    Caches Skyfield observations to be shared across Jovian event searches.
    Reduces redundant calculations of Jupiter, Sun, and Moon positions.
    """

    def __init__(self, observer, eph, ts):
        from ...utils import planetary

        self.observer = observer
        self.ts = ts
        self.planetary = planetary
        self.jupiter = eph["jupiter barycenter"]
        self.sun = eph["sun"]
        self.moon_map, self.moon_objs = _get_jovian_moon_objects(eph)
        self.elevation = _get_observer_elevation(observer)
        self._cache = {}

    def _get_time_key(self, t):
        if hasattr(t, "shape") and t.shape:
            # For arrays, use first, last and length as a proxy for identity
            return (t.tt[0], t.tt[-1], len(t.tt))
        return t.tt

    def get_basic_data(self, t):
        key = self._get_time_key(t)
        if key not in self._cache:
            j_obs = (
                self.observer.at(t).observe(self.jupiter).apparent(deflectors=(10, 599))
            )
            s_obs = self.observer.at(t).observe(self.sun).apparent(deflectors=(10, 599))
            t_emitted = self.ts.tt_jd(t.tt - j_obs.light_time)
            sun_from_j = (
                self.jupiter.at(t_emitted)
                .observe(self.sun)
                .apparent(deflectors=(10, 599))
            )

            # Jupiter's pole at emission time (IAU 2015 model)
            alpha0_deg, delta0_deg = self.planetary.get_planet_pole_coords(
                "jupiter", t_emitted
            )
            alpha0 = np.radians(alpha0_deg)
            delta0 = np.radians(delta0_deg)
            z_pole = np.array(
                [
                    np.cos(delta0) * np.cos(alpha0),
                    np.cos(delta0) * np.sin(alpha0),
                    np.sin(delta0),
                ]
            )

            self._cache[key] = {
                "j_obs": j_obs,
                "s_obs": s_obs,
                "t_emitted": t_emitted,
                "sun_from_j": sun_from_j,
                "z_pole": z_pole,
                "moons": {},
                "moons_sun": {},
            }
        return self._cache[key]

    def get_visibility(self, t):
        """
        Calculates and caches Jupiter visibility (altitude, sun altitude, elongation).
        """
        data = self.get_basic_data(t)
        if "visible" not in data:
            is_array = hasattr(t, "shape") and t.shape != ()
            # Special elevation -9999 bypasses topocentric checks for global indexing
            if self.elevation == -9999:
                data["visible"] = np.ones(len(t) if is_array else 1, dtype=bool)
            else:
                j_obs = data["j_obs"]
                s_obs = data["s_obs"]
                alt, _, _ = j_obs.altaz(temperature_C=10.0, pressure_mbar=1013.25)
                sun_alt = s_obs.altaz(temperature_C=10.0, pressure_mbar=1013.25)[
                    0
                ].degrees
                elongation = j_obs.separation_from(s_obs).degrees
                data["visible"] = (alt.degrees > 0) & (sun_alt <= -6) & (elongation > 10)
        return data["visible"]

    def get_moon_obs(self, t, moon_id):
        data = self.get_basic_data(t)
        if moon_id not in data["moons"]:
            data["moons"][moon_id] = (
                self.observer.at(t)
                .observe(self.moon_objs[moon_id])
                .apparent(deflectors=(10, 599))
            )
        return data["moons"][moon_id]

    def get_moon_sun_obs(self, t, moon_id):
        data = self.get_basic_data(t)
        if moon_id not in data["moons_sun"]:
            data["moons_sun"][moon_id] = (
                self.sun.at(data["t_emitted"])
                .observe(self.moon_objs[moon_id])
                .apparent(deflectors=(10, 599))
            )
        return data["moons_sun"][moon_id]


def is_inside_ellipsoid_projection(p_vec, u_vec, z_pole, re, rp):
    """
    Checks if point p is within the projection of an ellipsoid along direction u.
    p and u are (3, N), z_pole is (3, N) or (3,).
    re: equatorial radius, rp: polar radius.
    """
    # Dots along z_pole
    if p_vec.ndim > 1:
        # Optimization: einsum is ~2x faster than np.sum(A*B, axis=0) for large arrays
        p_z = np.einsum("ij,ij->j", p_vec, z_pole)
        u_z = np.einsum("ij,ij->j", u_vec, z_pole)
        p_u = np.einsum("ij,ij->j", p_vec, u_vec)
        p_sq = np.einsum("ij,ij->j", p_vec, p_vec)
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
