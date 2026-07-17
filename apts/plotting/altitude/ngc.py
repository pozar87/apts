from typing import TYPE_CHECKING, Optional
from matplotlib import pyplot
from apts.config import get_dark_mode
from apts.i18n import gettext_
from .base_catalog import generate_catalog_altitude_plot

if TYPE_CHECKING:
    from apts.observations import Observation


def generate_plot_ngc(
    observation: "Observation", dark_mode_override: Optional[bool] = None, **args
):
    return generate_catalog_altitude_plot(
        observation=observation,
        get_df_func=observation.get_visible_ngc,
        label_column="Name",
        title=gettext_("NGC/IC Objects Altitude"),
        legend_title=gettext_("Object Types"),
        logger_msg=gettext_("Successfully generated NGC plot."),
        error_title=gettext_("NGC Plot Error"),
        error_text=gettext_("Error generating NGC plot.\nSee logs for details."),
        logger_error_msg="Error generating NGC plot",
        clip_lower=10.0,
        dark_mode_override=dark_mode_override,
        scatter_kwargs={"alpha": 0.7},
        annotate_kwargs={"fontsize": 8, "alpha": 0.8},
        pyplot_module=pyplot,
        get_dark_mode_func=get_dark_mode,
        **args,
    )
