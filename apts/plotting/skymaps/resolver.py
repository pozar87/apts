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
    target_object, target_object_data = _resolve_messier(observation, target_name)
    if target_object is not None:
        return target_object, target_object_data

    target_object, target_object_data = _resolve_ngc(observation, target_name)
    if target_object is not None:
        return target_object, target_object_data

    target_object, target_object_data = _resolve_stars(observation, target_name)
    if target_object is not None:
        return target_object, target_object_data

    return _resolve_planets(observation, target_name)


def _resolve_messier(
    observation: "Observation", target_name: str
) -> Tuple[Optional[Any], Optional[Any]]:
    """Search for target in Messier catalog."""
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


def _resolve_ngc(
    observation: "Observation", target_name: str
) -> Tuple[Optional[Any], Optional[Any]]:
    """Search for target in NGC/IC catalog."""
    from ...objects.ngc import NGC

    norm_name = NGC.normalize_name(target_name)
    ngc_objs = observation.local_ngc.objects

    # Safety check for empty or improperly mocked DataFrames
    if not ngc_objs.empty:
        mask = pd.Series(False, index=ngc_objs.index)
        # Optimization: use pre-calculated normalized columns if available
        if "NGC_norm" in ngc_objs.columns:
            mask |= ngc_objs["NGC_norm"] == norm_name
        elif ObjectTableLabels.NGC in ngc_objs.columns:
            mask |= (
                NGC.normalize_name(ngc_objs[ObjectTableLabels.NGC]) == norm_name
            )

        if "Name_norm" in ngc_objs.columns:
            mask |= ngc_objs["Name_norm"] == norm_name
        elif ObjectTableLabels.NAME in ngc_objs.columns:
            mask |= (
                NGC.normalize_name(ngc_objs[ObjectTableLabels.NAME]) == norm_name
            )

        if "IC_norm" in ngc_objs.columns:
            mask |= ngc_objs["IC_norm"] == norm_name
        elif ObjectTableLabels.IC in ngc_objs.columns:
            mask |= (
                NGC.normalize_name(ngc_objs[ObjectTableLabels.IC]) == norm_name
            )

        result_df = ngc_objs[mask]
        if not result_df.empty:
            target_object_data = result_df.iloc[0]
            target_object = observation.local_ngc.get_skyfield_object(target_object_data)
            return target_object, target_object_data
    return None, None


def _resolve_stars(
    observation: "Observation", target_name: str
) -> Tuple[Optional[Any], Optional[Any]]:
    """Search for target in Stars catalog."""
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


def _resolve_planets(
    observation: "Observation", target_name: str
) -> Tuple[Optional[Any], Optional[Any]]:
    """Search for target in Planets catalog."""
    target_object = observation.local_planets.find_by_name(target_name)
    return target_object, None
