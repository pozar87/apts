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
    target_object = None
    target_object_data = None

    # Search logic that mirrors find_by_name methods
    # Messier
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

    if target_object is None:
        # NGC / IC
        from ...objects.ngc import NGC

        norm_name = NGC.normalize_name(target_name)
        ngc_objs = observation.local_ngc.objects

        # Safety check for empty or improperly mocked DataFrames
        if not ngc_objs.empty:
            mask = pd.Series(False, index=ngc_objs.index)
            if ObjectTableLabels.NGC in ngc_objs.columns:
                mask |= ngc_objs[ObjectTableLabels.NGC].apply(NGC.normalize_name) == norm_name
            if ObjectTableLabels.NAME in ngc_objs.columns:
                mask |= ngc_objs[ObjectTableLabels.NAME].apply(NGC.normalize_name) == norm_name
            if ObjectTableLabels.IC in ngc_objs.columns:
                mask |= ngc_objs[ObjectTableLabels.IC].apply(NGC.normalize_name) == norm_name

            result_df = ngc_objs[mask]
            if not result_df.empty:
                target_object_data = result_df.iloc[0]
                target_object = observation.local_ngc.get_skyfield_object(
                    target_object_data
                )

    if target_object is None:
        # Stars
        if (
            not observation.local_stars.objects.empty
            and ObjectTableLabels.NAME in observation.local_stars.objects.columns
        ):
            result_df = observation.local_stars.objects[
                observation.local_stars.objects[ObjectTableLabels.NAME].isin(
                    [target_name]
                )
            ]
            if not result_df.empty:
                target_object_data = result_df.iloc[0]
                target_object = observation.local_stars.get_skyfield_object(
                    target_object_data
                )

    if target_object is None:
        # Planets
        target_object = observation.local_planets.find_by_name(target_name)

    return target_object, target_object_data
