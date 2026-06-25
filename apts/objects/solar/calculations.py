from typing import cast
import ephem
import numpy as np
import pandas as pd
from ...constants import ObjectTableLabels
from ...utils import MINOR_PLANET_NAMES
from .mpc import compute_minor_planet_ephem


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
    ephem_object_map = {
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
    ephem_observer = get_ephem_observer(observer_to_use, t)
    mags, sizes, phases = [], [], []
    ras, decs, dists, elongs, sky_objs = [], [], [], [], []
    current_alts, current_azs = [], []

    obs_at_t = observer_to_use.observer.at(t)
    sun_pos = obs_at_t.observe(observer_to_use.sun).apparent()

    # Optimization: use itertuples() for faster row access than iterrows()
    for row in computed_df.itertuples():
        object_name = cast(str, row.Name)
        # Ephem
        if object_name in MINOR_PLANET_NAMES.values():
            mag, size, phase = compute_minor_planet_ephem(
                object_name, minor_planets, ephem_observer
            )
        else:
            ephem_obj_constructor = ephem_object_map.get(object_name)
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
        # Convert row (NamedTuple) to dict for get_skyfield_object which expects Series/dict
        row_dict = row._asdict()
        sky_obj = get_skyfield_object_func(row_dict)
        sky_objs.append(sky_obj)
        if sky_obj:
            pos = obs_at_t.observe(sky_obj).apparent()
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

    computed_df[ObjectTableLabels.MAGNITUDE] = mags
    computed_df["Magnitude_float"] = [m if pd.notna(m) else 99 for m in mags]
    computed_df[ObjectTableLabels.SIZE] = sizes
    sizes_arcmin = [s / 60.0 if s is not None else 0 for s in sizes]
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
