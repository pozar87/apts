from typing import TYPE_CHECKING, Any, Optional, Tuple

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
        # NGC
        result_df = observation.local_ngc.objects[
            (observation.local_ngc.objects["NGC"].isin([target_name]))
            | (observation.local_ngc.objects["Name"].isin([target_name]))
        ]
        if not result_df.empty:
            target_object_data = result_df.iloc[0]
            target_object = observation.local_ngc.get_skyfield_object(
                target_object_data
            )
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
