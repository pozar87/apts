import logging
from typing import TYPE_CHECKING, Optional, cast

if TYPE_CHECKING:
    from ...plotting import NullPlotter, Plotter
    from ..base import Observation

logger = logging.getLogger(__name__)


class BasePlottingMixIn:
    if TYPE_CHECKING:
        _plot: Optional["Plotter | NullPlotter"]

    @property
    def plot(self) -> "Plotter | NullPlotter":
        if self._plot is None:
            try:
                from ... import plotting as apts_plot

                self._plot = apts_plot.Plotter(cast("Observation", self))
            except ImportError:
                # Fallback if dependencies are missing or plotting is disabled
                from ...plotting.dispatcher import NullPlotter

                self._plot = NullPlotter()
            except Exception as e:
                # Fallback for any other initialization error
                logger.warning(f"Failed to initialize plotter: {e}")
                from ...plotting.dispatcher import NullPlotter

                self._plot = NullPlotter()
        return self._plot

    @plot.setter
    def plot(self, value):
        self._plot = value
