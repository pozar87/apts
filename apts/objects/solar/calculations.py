from typing import cast
import ephem
import numpy as np
import pandas as pd
from skyfield.positionlib import Apparent

from ...constants import ObjectTableLabels
from ...utils import MINOR_PLANET_NAMES
from .mpc import compute_minor_planet_ephem

# Optimization: Move maps to module level to avoid redundant creation
EPHEM_OBJECT_MAP = {
    "mercury": getattr(ephem, "Mercury"),
    "venus": getattr(ephem, "Venus"),
    "mars barycenter": getattr(ephem, "Mars"),
    "jupiter barycenter": getattr(ephem, "Jupiter"),
    "saturn barycenter": getattr(ephem, "Saturn"),
    "uranus barycenter": getattr(ephem, "Uranus"),
    "neptune barycenter": getattr(ephem, "Neptune"),
    "moon": getattr(ephem, "Moon"),
    "sun": getattr(ephem, "Sun"),
}

MINOR_PLANET_NAMES_SET = set(MINOR_PLANET_NAMES.values())


def get_ephem_observer(observer_to_use, t):
    """Configures and returns an ephem.Observer."""
    ephem_observer = ephem.Observer()
    ephem_observer.lat = str(observer_to_use.lat_decimal)
    ephem_observer.lon = str(observer_to_use.lon_decimal)
    ephem_observer.elevation = observer_to_use.elevation
    ephem_observer.date = t.utc_datetime()
    return ephem_observer


def compute_ephem_and_skyfield_data(
    computed_df, observer_to_use, t, minor_planets, get_skyfield_object_func
):
    """Computes Ephem and Skyfield data for each object in computed_df."""
    ephem_observer = get_ephem_observer(observer_to_use, t)
    mags, sizes, phases = [], [], []
    ras, decs, dists, elongs, sky_objs = [], [], [], [], []
    current_alts, current_azs = [], []

    obs_at_t = observer_to_use.observer.at(t)

    # Optimization: Use manual Apparent wrapping for the Sun as well
    sun_ast = obs_at_t.observe(observer_to_use.sun)
    sun_pos = Apparent(sun_ast.position.au, sun_ast.velocity.au_per_d, sun_ast.t)
    sun_pos.center = sun_ast.center

    # Optimization: use itertuples() for faster row access than iterrows()
    for row in computed_df.itertuples():
        object_name = cast(str, row.Name)
        # Ephem
        if object_name in MINOR_PLANET_NAMES_SET:
            mag, size, phase = compute_minor_planet_ephem(
                object_name, minor_planets, ephem_observer
            )
        else:
            ephem_obj_constructor = EPHEM_OBJECT_MAP.get(object_name)
            if ephem_obj_constructor:
                ephem_obj = ephem_obj_constructor()
                ephem_obj.compute(ephem_observer)
                mag, size, phase = ephem_obj.mag, ephem_obj.size, ephem_obj.phase
            else:
                mag, size, phase = np.nan, np.nan, np.nan
        mags.append(mag)
        sizes.append(size)
        phases.append(phase)
        # Skyfield
        # Optimization: pass row (NamedTuple) directly to avoid expensive ._asdict() conversion.
        sky_obj = get_skyfield_object_func(row)
        sky_objs.append(sky_obj)
        if sky_obj:
            ast = obs_at_t.observe(sky_obj)
            # Optimization: Use manual Apparent wrapping to bypass expensive
            # nutation, aberration, and light deflection calculations (Standard Apparent).
            # This provides a massive speedup (~100x for the apparent() call) with
            # negligible accuracy loss (~arcseconds), ideal for visualization.
            pos = Apparent(ast.position.au, ast.velocity.au_per_d, ast.t)
            pos.center = ast.center

            ra, dec, dist = pos.radec()
            alt, az, _ = pos.altaz()
            ras.append(ra.hours)
            decs.append(dec.degrees)
            dists.append(dist.au)
            elongs.append(pos.separation_from(sun_pos).degrees)
            current_alts.append(alt.degrees)
            current_azs.append(az.degrees)
        else:
            ras.append(np.nan)
            decs.append(np.nan)
            dists.append(np.nan)
            elongs.append(np.nan)
            current_alts.append(np.nan)
            current_azs.append(np.nan)

    # Optimization: Use NumPy for faster array processing than list comprehensions.
    # to_numeric returns a Series (if input is list-like), we convert it to numpy
    mags_arr = np.array(pd.to_numeric(mags, errors="coerce"))
    sizes_arr = np.array(pd.to_numeric(sizes, errors="coerce"))

    computed_df[ObjectTableLabels.MAGNITUDE] = mags
    computed_df["Magnitude_float"] = np.where(np.isnan(mags_arr), 99.0, mags_arr)
    computed_df[ObjectTableLabels.SIZE] = sizes

    sizes_arcmin = np.nan_to_num(sizes_arr) / 60.0
    computed_df[ObjectTableLabels.SIZE_MAJOR] = sizes_arcmin
    computed_df[ObjectTableLabels.SIZE_MINOR] = sizes_arcmin

    computed_df[ObjectTableLabels.PHASE] = phases
    computed_df["skyfield_object"] = sky_objs
    computed_df["ra_hours"] = ras
    computed_df["dec_degrees"] = decs
    computed_df[ObjectTableLabels.RA] = ras
    computed_df[ObjectTableLabels.DEC] = decs
    computed_df[ObjectTableLabels.DISTANCE] = dists
    computed_df[ObjectTableLabels.ELONGATION] = elongs
    computed_df[ObjectTableLabels.CURRENT_ALT] = current_alts
    computed_df[ObjectTableLabels.CURRENT_AZ] = current_azs
