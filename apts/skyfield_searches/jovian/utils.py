import logging
from typing import cast

import numpy as np
from skyfield.positionlib import Apparent

from ..utils import fast_altaz

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
            try:
                moon_objs[moon_id] = eph[jup300_ids[moon_id]]
                logger.warning(
                    f"ID {moon_id} not found in Jovian ephemeris. Falling back to non-standard ID {jup300_ids[moon_id]}."
                )
            except KeyError:
                logger.error(
                    f"Neither ID {moon_id} nor fallback {jup300_ids[moon_id]} found in ephemeris. Jovian moon plotting will be skipped for this moon."
                )
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

    def _get_entry(self, t):
        """Internal helper to get or create a cache entry."""
        key = self._get_time_key(t)
        if key not in self._cache:
            self._cache[key] = {"moons": {}, "moons_sun": {}}
        return self._cache[key]

    def get_obs_at_t(self, t):
        """Gets or caches topocentric observer state at time t."""
        data = self._get_entry(t)
        if "obs_at_t" not in data:
            data["obs_at_t"] = self.observer.at(t)
        return data["obs_at_t"]

    def get_basic_data(self, t):
        data = self._get_entry(t)
        if "z_pole" not in data:
            # Performance Optimization: Hoist observer.at(t) to evaluate topocentric state once per time step
            obs_at_t = self.get_obs_at_t(t)
            # Ensure positions are available
            if "j_obs" not in data:
                data["j_obs"] = obs_at_t.observe(self.jupiter)
            if "s_obs" not in data:
                data["s_obs"] = obs_at_t.observe(self.sun)

            j_obs = data["j_obs"]
            t_emitted = self.ts.tt_jd(t.tt - j_obs.light_time)
            sun_from_j = self.jupiter.at(t_emitted).observe(self.sun)

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

            data["t_emitted"] = t_emitted
            data["sun_from_j"] = sun_from_j
            data["z_pole"] = z_pole

        return data

    def get_visibility(self, t):
        """
        Calculates and caches Jupiter visibility (altitude, sun altitude, elongation).
        Uses a coarse decimated check first to avoid expensive calls.
        """
        data = self._get_entry(t)
        if "visible" not in data:
            is_array = hasattr(t, "shape") and t.shape != ()
            # Special elevation -9999 bypasses topocentric checks for global indexing
            if self.elevation == -9999:
                data["visible"] = np.ones(len(t) if is_array else 1, dtype=bool)
            elif is_array and len(t) > 25:
                # Coarse check: sample every 25 points to see if Jupiter is anywhere near visible.
                # 25 points at 0.005 step is ~3 hours.
                t_coarse = t[::25]
                j_ast = self.observer.at(t_coarse).observe(self.jupiter)
                j_app = Apparent(j_ast.position.au, j_ast.velocity.au_per_d, j_ast.t)
                j_app.center = j_ast.center
                alt_coarse, _, _ = j_app.altaz()
                # If Jupiter is more than 5 degrees below horizon in all samples,
                # we assume it's not visible for the whole block.
                # 5 degrees is a safe margin for 3-hour decimation.
                if np.all(alt_coarse.degrees < -5.0):  # type: ignore[operator]
                    data["visible"] = np.zeros(len(t), dtype=bool)
                else:
                    # Fallback to high-precision for the whole block
                    self._compute_full_visibility(t, data)
            else:
                self._compute_full_visibility(t, data)
        return data["visible"]

    def _compute_full_visibility(self, t, data):
        """High-precision visibility calculation."""
        # Performance Optimization: Hoist observer.at(t) to evaluate topocentric state once per time step
        obs_at_t = self.get_obs_at_t(t)
        # Optimization: Use fast_altaz to bypass expensive Standard Apparent frame transformations
        # for Jupiter and Sun altitude calculations (~4x speedup on this path).
        j_alt, _, _ = fast_altaz(obs_at_t, self.jupiter)
        s_alt, _, _ = fast_altaz(obs_at_t, self.sun)

        if "j_obs" not in data:
            data["j_obs"] = obs_at_t.observe(self.jupiter)
        if "s_obs" not in data:
            data["s_obs"] = obs_at_t.observe(self.sun)

        elongation = data["j_obs"].separation_from(data["s_obs"]).degrees
        data["visible"] = (
            (cast(float, j_alt.degrees) > 0)
            & (cast(float, s_alt.degrees) <= -6)
            & (elongation > 10)
        )

    def get_moon_obs(self, t, moon_id):
        data = self.get_basic_data(t)
        if moon_id not in data["moons"]:
            # Performance Optimization: Hoist observer.at(t) to evaluate topocentric state once per time step
            obs_at_t = self.get_obs_at_t(t)
            data["moons"][moon_id] = obs_at_t.observe(self.moon_objs[moon_id])
        return data["moons"][moon_id]

    def get_moon_sun_obs(self, t, moon_id):
        data = self.get_basic_data(t)
        if moon_id not in data["moons_sun"]:
            data["moons_sun"][moon_id] = self.sun.at(data["t_emitted"]).observe(
                self.moon_objs[moon_id]
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
        # Optimization: For 3D vectors (3, N), direct component dot products
        # (A[0]*B[0] + A[1]*B[1] + A[2]*B[2]) are ~25-30% faster than np.einsum("ij,ij->j", A, B)
        # by bypassing string parsing and C-engine dispatch overhead in NumPy.
        p_z = p_vec[0] * z_pole[0] + p_vec[1] * z_pole[1] + p_vec[2] * z_pole[2]
        u_z = u_vec[0] * z_pole[0] + u_vec[1] * z_pole[1] + u_vec[2] * z_pole[2]
        p_u = p_vec[0] * u_vec[0] + p_vec[1] * u_vec[1] + p_vec[2] * u_vec[2]
        p_sq = p_vec[0] * p_vec[0] + p_vec[1] * p_vec[1] + p_vec[2] * p_vec[2]
    else:
        p_z = np.dot(p_vec, z_pole)
        u_z = np.dot(u_vec, z_pole)
        p_u = np.dot(p_vec, u_vec)
        p_sq = np.dot(p_vec, p_vec)

    return is_inside_ellipsoid_projection_fast(p_z, p_u, p_sq, u_z, re, rp)


def is_inside_ellipsoid_projection_fast(p_z, p_u, p_sq, u_z, re, rp, u_prime_sq=None):
    """
    Checks if point p is within the projection of an ellipsoid along direction u.
    Uses pre-calculated dot products to avoid redundant computations.

    p_z: dot(p, z_pole)
    p_u: dot(p, u)
    p_sq: dot(p, p)
    u_z: dot(u, z_pole)
    u_prime_sq: pre-calculated (1.0 - u_z**2) / re**2 + u_z**2 / rp**2 (optional)
    """
    if u_prime_sq is None:
        u_prime_sq = (1.0 - u_z**2) / re**2 + u_z**2 / rp**2

    # Scaled space parameters
    p_prime_sq = (p_sq - p_z**2) / re**2 + p_z**2 / rp**2
    p_prime_u_prime = (p_u - p_z * u_z) / re**2 + (p_z * u_z) / rp**2

    # Projected distance squared: |P'|^2 - (P' . U')^2 / |U'|^2
    return p_prime_sq - (p_prime_u_prime**2 / u_prime_sq) <= 1.000001
