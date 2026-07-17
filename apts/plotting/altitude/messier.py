from typing import TYPE_CHECKING, Optional
from matplotlib import pyplot
from apts.config import get_dark_mode
from apts.utils.plot import PlotUtils  # noqa: F401
from apts.i18n import gettext_
from .base_catalog import generate_catalog_altitude_plot
from ...constants import ObjectTableLabels

if TYPE_CHECKING:
    from apts.observations import Observation


def generate_plot_messier(
    observation: "Observation", dark_mode_override: Optional[bool] = None, **args
):
    return generate_catalog_altitude_plot(
        observation=observation,
        get_df_func=observation.get_visible_messier,
        label_column=ObjectTableLabels.MESSIER,
        title=gettext_("Messier Objects Altitude"),
        legend_title=gettext_("Object Types"),
        logger_msg=gettext_("Successfully generated Messier plot."),
        error_title=gettext_("Messier Plot Error"),
        error_text=gettext_("Error generating Messier plot.\nSee logs for details."),
        logger_error_msg="Error generating Messier plot",
        clip_lower=None,
        dark_mode_override=dark_mode_override,
        scatter_kwargs=None,
        annotate_kwargs=None,
        pyplot_module=pyplot,
        get_dark_mode_func=get_dark_mode,
        **args,
    )
