import numpy as np
from dataclasses import dataclass
from typing import Dict, TYPE_CHECKING

from skyfield.api import Time

from apts.cache import get_jovian_ephemeris, get_timescale
from apts.constants import astronomy
from apts.skyfield_searches.jovian.moons import JovianMoonState
from apts.skyfield_searches.jovian.utils import JovianSearchContext

if TYPE_CHECKING:
    from ...observations import Observation

@dataclass
class JovianMoonPosition:
    name: str
    dx: float
    dy: float
    radius_arcsec: float
    is_behind: bool
    is_transit: bool

@dataclass
class JovianSystemState:
    jupiter_radius_arcsec: float
    jupiter_polar_radius_arcsec: float
    moons: Dict[int, JovianMoonPosition]
    time: Time

def calculate_jovian_state(
    observation: "Observation",
    t: Time
) -> JovianSystemState:
    """
    Calculates the positions and states of Jupiter and its Galilean moons.
    """
    eph = get_jovian_ephemeris()
    ts = get_timescale()
    ctx = JovianSearchContext(observation.place.observer, eph, ts)
    state_func = JovianMoonState(ctx)

    # Get Jupiter position and distance
    j_obs = observation.place.observer.at(t).observe(ctx.jupiter).apparent()
    j_ra, j_dec, j_dist = j_obs.radec()
    j_dist_km = j_dist.km

    # Calculate Jupiter angular radius in arcseconds
    j_radius_arcsec = (
        np.degrees(np.arctan2(astronomy.JUPITER_RADIUS_KM, j_dist_km)) * 3600
    )
    j_polar_radius_arcsec = (
        np.degrees(np.arctan2(astronomy.JUPITER_POLAR_RADIUS_KM, j_dist_km)) * 3600
    )

    # Moon data
    moons_radii = {
        501: astronomy.IO_RADIUS_KM,
        502: astronomy.EUROPA_RADIUS_KM,
        503: astronomy.GANYMEDE_RADIUS_KM,
        504: astronomy.CALLISTO_RADIUS_KM,
    }

    mask = state_func(t)
    cos_j_dec = np.cos(j_dec.radians)

    moon_positions = {}

    for i, (moon_id, moon_name) in enumerate(ctx.moon_map.items()):
        if moon_id not in ctx.moon_objs:
            continue
        m_obs = (
            observation.place.observer.at(t).observe(ctx.moon_objs[moon_id]).apparent()
        )
        m_ra, m_dec, m_dist = m_obs.radec()

        dx = (m_ra.hours - j_ra.hours) * 15 * 3600 * cos_j_dec
        dy = (m_dec.degrees - j_dec.degrees) * 3600

        moon_mask = (mask >> (4 * i)) & 0xF

        # Check if moon is behind Jupiter (Occultation or Eclipse)
        is_behind = bool(moon_mask & (2 | 8))
        # Check if moon is in front (Transit)
        is_transit = bool(moon_mask & 1)

        m_radius_arcsec = (
            np.degrees(np.arctan2(moons_radii[moon_id], m_dist.km)) * 3600
        )

        moon_positions[moon_id] = JovianMoonPosition(
            name=moon_name,
            dx=dx,
            dy=dy,
            radius_arcsec=m_radius_arcsec,
            is_behind=is_behind,
            is_transit=is_transit
        )

    return JovianSystemState(
        jupiter_radius_arcsec=j_radius_arcsec,
        jupiter_polar_radius_arcsec=j_polar_radius_arcsec,
        moons=moon_positions,
        time=t
    )
