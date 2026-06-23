from typing import TYPE_CHECKING, Optional

from matplotlib.ticker import FuncFormatter

from ...config import get_dark_mode
from ...constants import EquipmentTableLabels
from ...constants.graphconstants import get_plot_style
from ...i18n import gettext_, language_context
from ...utils import decdeg2dms, dms2decdeg
from .base import BaseEquipmentPlottingMixIn

if TYPE_CHECKING:
    import pandas as pd


class SimpleEquipmentPlottingMixIn(BaseEquipmentPlottingMixIn):
    def plot_zoom(
        self,
        dark_mode_override: Optional[bool] = None,
        include_naked_eye: bool = False,
        language: Optional[str] = None,
        **args,
    ):
        """
        Plot available magnification
        """
        with language_context(language):
            if dark_mode_override is not None:
                effective_dark_mode = dark_mode_override
            else:
                effective_dark_mode = get_dark_mode()
            plot = self._plot(
                EquipmentTableLabels.ZOOM,
                gettext_("Available zoom"),
                gettext_("Used equipment"),
                gettext_("Magnification"),
                dark_mode_enabled=effective_dark_mode,
                include_naked_eye=include_naked_eye,
                **args,
            )
            # Add marker for maximal useful zoom
            style = get_plot_style(effective_dark_mode)  # Get style for the annotations
            max_zoom = self.max_zoom()
            plot.axhline(max_zoom, color=style["TEXT_COLOR"], linestyle="--", alpha=0.7)
            plot.annotate(
                gettext_("Max useful zoom due to atmosphere"),
                (-0.4, max_zoom + 2),
                alpha=0.7,
                color=style["TEXT_COLOR"],
            )

    def plot_fov(
        self,
        dark_mode_override: Optional[bool] = None,
        include_naked_eye: bool = False,
        language: Optional[str] = None,
        **args,
    ):
        """
        Plot available fields of view
        """
        with language_context(language):
            if dark_mode_override is not None:
                effective_dark_mode = dark_mode_override
            else:
                effective_dark_mode = get_dark_mode()

            style = get_plot_style(effective_dark_mode)

            def formatter(tick, pos):
                return decdeg2dms(tick, pretty=True)

            def add_line(description, position):
                position = dms2decdeg(position)
                plot.axhline(
                    position, color=style["TEXT_COLOR"], linestyle="--", alpha=0.7
                )
                plot.annotate(
                    description,
                    (-0.4, position + 0.03),
                    alpha=0.7,
                    color=style["TEXT_COLOR"],
                )

            plot = self._plot(
                EquipmentTableLabels.FOV,
                gettext_("Available fields of view"),
                gettext_("Used equipment"),
                gettext_("Field of view [°]"),
                dark_mode_enabled=effective_dark_mode,
                include_naked_eye=include_naked_eye,
                **args,
            )
            plot.yaxis.set_major_formatter(FuncFormatter(formatter))
            # Pleiades width is 1°50'
            add_line(gettext_("Pleiades size"), (1, 50, 0))
            # Average moon size is 0°31'42"
            add_line(gettext_("Moon size"), (0, 31, 42))
            # M51 width is 0°11'
            add_line(gettext_("M51 size"), (0, 11, 0))
