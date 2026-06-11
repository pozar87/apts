from typing import TYPE_CHECKING, Any, Optional, Tuple

import pandas as pd

from ...constants.objecttablelabels import ObjectTableLabels

if TYPE_CHECKING:
    from ...observations import Observation


def resolve_target(
    observation: "Observation", target_name: str
) -> Tuple[Optional[Any], Optional[Any]]:
    """
    Resolves a target name into a Skyfield object and its associated data.
    Searches through Messier, NGC, Stars, and Planets catalogs.
    """
    # 1. Messier
    target_object, target_object_data = _resolve_messier(observation, target_name)
    if target_object:
        return target_object, target_object_data

    # 2. NGC / IC
    target_object, target_object_data = _resolve_ngc(observation, target_name)
    if target_object:
        return target_object, target_object_data

    # 3. Stars
    target_object, target_object_data = _resolve_stars(observation, target_name)
    if target_object:
        return target_object, target_object_data

    # 4. Planets
    target_object = observation.local_planets.find_by_name(target_name)
    return target_object, None


def _resolve_messier(observation: "Observation", target_name: str):
    if (
        not observation.local_messier.objects.empty
        and ObjectTableLabels.MESSIER in observation.local_messier.objects.columns
    ):
        result_df = observation.local_messier.objects[
            observation.local_messier.objects[ObjectTableLabels.MESSIER].isin(
                [target_name]
            )
        ]
        if not result_df.empty:
            target_object_data = result_df.iloc[0]
            target_object = observation.local_messier.get_skyfield_object(
                target_object_data
            )
            return target_object, target_object_data
    return None, None


def _resolve_ngc(observation: "Observation", target_name: str):
    from ...catalogs.ngc import normalize_name

    norm_name = normalize_name(target_name)
    ngc_objs = observation.local_ngc.objects

    if not ngc_objs.empty:
        mask = pd.Series(False, index=ngc_objs.index)
        # Optimization: use pre-calculated normalized columns
        if "NGC_norm" in ngc_objs.columns:
            mask |= ngc_objs["NGC_norm"] == norm_name
        if "Name_norm" in ngc_objs.columns:
            mask |= ngc_objs["Name_norm"] == norm_name
        if "IC_norm" in ngc_objs.columns:
            mask |= ngc_objs["IC_norm"] == norm_name

        result_df = ngc_objs[mask]
        if not result_df.empty:
            target_object_data = result_df.iloc[0]
            target_object = observation.local_ngc.get_skyfield_object(target_object_data)
            return target_object, target_object_data
    return None, None


def _resolve_stars(observation: "Observation", target_name: str):
    if (
        not observation.local_stars.objects.empty
        and ObjectTableLabels.NAME in observation.local_stars.objects.columns
    ):
        result_df = observation.local_stars.objects[
            observation.local_stars.objects[ObjectTableLabels.NAME].isin([target_name])
        ]
        if not result_df.empty:
            target_object_data = result_df.iloc[0]
            target_object = observation.local_stars.get_skyfield_object(
                target_object_data
            )
            return target_object, target_object_data
    return None, None
