from datetime import datetime
from typing import TYPE_CHECKING, Optional, cast

import pandas as pd
from matplotlib import figure

from matplotlib import pyplot
from apts.cache import get_jovian_ephemeris, get_timescale
from apts.skyfield_searches.jovian.moons import JovianMoonState
from apts.skyfield_searches.jovian.utils import JovianSearchContext
from .plots import generate_plot_jovian_moons

if TYPE_CHECKING:
    from ...observations import Observation

def plot_jovian_moons(
    observation: "Observation",
    plot_date: Optional[datetime] = None,
    dark_mode_override: Optional[bool] = None,
    zoom_arcmin: float = 20.0,
    equipment_id: Optional[int] = None,
    flip_horizontally: Optional[bool] = None,
    flip_vertically: Optional[bool] = None,
    **kwargs,
) -> figure.Figure:
    """
    High-level function to plot Jovian moons with support for flipping and equipment lookup.
    """
    flipped_horizontally = False
    flipped_vertically = False

    if equipment_id is not None:
        # Check if equipment has data method, otherwise assume it's already a DataFrame
        equipment_data = cast(
            pd.DataFrame,
            observation.equipment.data()
            if hasattr(observation.equipment, "data")
            else observation.equipment,
        )
        if (
            equipment_data is not None
            and not equipment_data.empty
            and "ID" in equipment_data.columns
            and equipment_id in equipment_data["ID"].values
        ):
            row = equipment_data.loc[equipment_data["ID"] == equipment_id]
            if "Flipped Horizontally" in row.columns:
                flipped_horizontally = row["Flipped Horizontally"].iloc[0]
            if "Flipped Vertically" in row.columns:
                flipped_vertically = row["Flipped Vertically"].iloc[0]

    if flip_horizontally is not None:
        flipped_horizontally = flip_horizontally
    if flip_vertically is not None:
        flipped_vertically = flip_vertically

    return generate_plot_jovian_moons(
        observation,
        plot_date=plot_date,
        dark_mode_override=dark_mode_override,
        zoom_arcmin=zoom_arcmin,
        flipped_horizontally=flipped_horizontally,
        flipped_vertically=flipped_vertically,
        **kwargs,
    )

__all__ = [
    "plot_jovian_moons",
    "generate_plot_jovian_moons",
    "pyplot",
    "get_jovian_ephemeris",
    "get_timescale",
    "JovianMoonState",
    "JovianSearchContext",
]
