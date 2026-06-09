from typing import TYPE_CHECKING, Any, Optional, Tuple

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
    result_df = observation.local_messier.objects[
        observation.local_messier.objects["Messier"].isin([target_name])
    ]
    if not result_df.empty:
        target_object_data = result_df.iloc[0]
        target_object = observation.local_messier.get_skyfield_object(
            target_object_data
        )
    else:
        # NGC / IC
        target_object = observation.local_ngc.find_by_name(target_name)
        if target_object is not None:
            # We need to find the data too.
            # Since find_by_name only returns the skyfield object,
            # we re-run the mask to get the row.
            # Alternatively, we could refactor find_by_name to return both.
            # For now, to keep it simple and correct:
            from ...objects.ngc import NGC

            norm_name = NGC.normalize_name(target_name)
            ngc_objs = observation.local_ngc.objects
            mask = (ngc_objs[ObjectTableLabels.NGC].apply(NGC.normalize_name) == norm_name) | (
                ngc_objs[ObjectTableLabels.NAME].apply(NGC.normalize_name) == norm_name
            )
            if ObjectTableLabels.IC in ngc_objs.columns:
                mask |= ngc_objs[ObjectTableLabels.IC].apply(NGC.normalize_name) == norm_name

            result_df = ngc_objs[mask]
            if not result_df.empty:
                target_object_data = result_df.iloc[0]
        else:
            # Stars
            result_df = observation.local_stars.objects[
                observation.local_stars.objects["Name"].isin([target_name])
            ]
            if not result_df.empty:
                target_object_data = result_df.iloc[0]
                target_object = observation.local_stars.get_skyfield_object(
                    target_object_data
                )
            else:
                # Planets
                target_object = observation.local_planets.find_by_name(target_name)

    return target_object, target_object_data
