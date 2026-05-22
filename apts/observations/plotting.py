import logging
from datetime import datetime
from typing import TYPE_CHECKING, Optional, cast

if TYPE_CHECKING:
    import matplotlib.figure

    from ..plotting import NullPlotter, Plotter

from ..conditions import Conditions
from ..constants.plot import CoordinateSystem
from ..i18n import language_context

if TYPE_CHECKING:
    from ..observations.base import Observation

logger = logging.getLogger(__name__)


class PlottingMixIn:
    if TYPE_CHECKING:
        _plot: Optional["Plotter | NullPlotter"]

    @property
    def plot(self) -> "Plotter | NullPlotter":
        if self._plot is None:
            try:
                from .. import plotting as apts_plot

                self._plot = apts_plot.Plotter(cast("Observation", self))
            except ImportError:
                # Fallback if dependencies are missing or plotting is disabled
                self._plot = apts_plot.NullPlotter()
            except Exception as e:
                # Fallback for any other initialization error
                logger.warning(f"Failed to initialize plotter: {e}")
                self._plot = apts_plot.NullPlotter()
        return self._plot

    @plot.setter
    def plot(self, value):
        self._plot = value

    def plot_visible_planets_svg(
        self,
        dark_mode_override: Optional[bool] = None,
        language: Optional[str] = None,
        **args,
    ):
        with language_context(language):
            return self.plot.visible_planets_svg(
                dark_mode_override=dark_mode_override, **args
            )

    def plot_visible_planets(
        self,
        dark_mode_override: Optional[bool] = None,
        language: Optional[str] = None,
        **args,
    ):
        with language_context(language):
            return self.plot.visible_planets(
                dark_mode_override=dark_mode_override, **args
            )

    def plot_messier(
        self,
        dark_mode_override: Optional[bool] = None,
        language: Optional[str] = None,
        **args,
    ):
        with language_context(language):
            return self.plot.messier(dark_mode_override=dark_mode_override, **args)

    def plot_planets(
        self,
        dark_mode_override: Optional[bool] = None,
        language: Optional[str] = None,
        **args,
    ):
        with language_context(language):
            return self.plot.planets(dark_mode_override=dark_mode_override, **args)

    def plot_weather(
        self,
        dark_mode_override: Optional[bool] = None,
        language: Optional[str] = None,
        conditions: Optional[Conditions] = None,
        **args,
    ):
        with language_context(language):
            return self.plot.weather(
                dark_mode_override=dark_mode_override, conditions=conditions, **args
            )

    def plot_clouds(
        self,
        dark_mode_override: Optional[bool] = None,
        language: Optional[str] = None,
        conditions: Optional[Conditions] = None,
        **args,
    ):
        with language_context(language):
            return self.plot.clouds(
                dark_mode_override=dark_mode_override, conditions=conditions, **args
            )

    def plot_clouds_summary(
        self,
        dark_mode_override: Optional[bool] = None,
        language: Optional[str] = None,
        **args,
    ):
        with language_context(language):
            return self.plot.clouds_summary(
                dark_mode_override=dark_mode_override, **args
            )

    def plot_precipitation(
        self,
        dark_mode_override: Optional[bool] = None,
        language: Optional[str] = None,
        conditions: Optional[Conditions] = None,
        **args,
    ):
        with language_context(language):
            return self.plot.precipitation(
                dark_mode_override=dark_mode_override, conditions=conditions, **args
            )

    def plot_precipitation_type_summary(
        self,
        dark_mode_override: Optional[bool] = None,
        language: Optional[str] = None,
        **args,
    ):
        with language_context(language):
            return self.plot.precipitation_type_summary(
                dark_mode_override=dark_mode_override, **args
            )

    def plot_temperature(
        self,
        dark_mode_override: Optional[bool] = None,
        language: Optional[str] = None,
        conditions: Optional[Conditions] = None,
        **args,
    ):
        with language_context(language):
            return self.plot.temperature(
                dark_mode_override=dark_mode_override, conditions=conditions, **args
            )

    def plot_wind(
        self,
        dark_mode_override: Optional[bool] = None,
        language: Optional[str] = None,
        conditions: Optional[Conditions] = None,
        **args,
    ):
        with language_context(language):
            return self.plot.wind(
                dark_mode_override=dark_mode_override, conditions=conditions, **args
            )

    def plot_pressure_and_ozone(
        self,
        dark_mode_override: Optional[bool] = None,
        language: Optional[str] = None,
        **args,
    ):
        with language_context(language):
            return self.plot.pressure_and_ozone(
                dark_mode_override=dark_mode_override, **args
            )

    def plot_visibility(
        self,
        dark_mode_override: Optional[bool] = None,
        language: Optional[str] = None,
        conditions: Optional[Conditions] = None,
        **args,
    ):
        with language_context(language):
            return self.plot.visibility(
                dark_mode_override=dark_mode_override, conditions=conditions, **args
            )

    def plot_moon_illumination(
        self,
        dark_mode_override: Optional[bool] = None,
        language: Optional[str] = None,
        conditions: Optional[Conditions] = None,
        **args,
    ):
        with language_context(language):
            return self.plot.moon_illumination(
                dark_mode_override=dark_mode_override, conditions=conditions, **args
            )

    def plot_fog(
        self,
        dark_mode_override: Optional[bool] = None,
        language: Optional[str] = None,
        conditions: Optional[Conditions] = None,
        **args,
    ):
        with language_context(language):
            return self.plot.fog(
                dark_mode_override=dark_mode_override, conditions=conditions, **args
            )

    def plot_aurora(
        self,
        dark_mode_override: Optional[bool] = None,
        language: Optional[str] = None,
        conditions: Optional[Conditions] = None,
        **args,
    ):
        with language_context(language):
            return self.plot.aurora(
                dark_mode_override=dark_mode_override, conditions=conditions, **args
            )

    def plot_seeing(
        self,
        dark_mode_override: Optional[bool] = None,
        language: Optional[str] = None,
        conditions: Optional[Conditions] = None,
        **args,
    ):
        with language_context(language):
            return self.plot.seeing(
                dark_mode_override=dark_mode_override, conditions=conditions, **args
            )

    def plot_sqm(
        self,
        dark_mode_override: Optional[bool] = None,
        language: Optional[str] = None,
        conditions: Optional[Conditions] = None,
        **args,
    ):
        with language_context(language):
            return self.plot.sqm(
                dark_mode_override=dark_mode_override, conditions=conditions, **args
            )

    def plot_weather_summary(
        self,
        dark_mode_override: Optional[bool] = None,
        language: Optional[str] = None,
        conditions: Optional[Conditions] = None,
        **args,
    ):
        with language_context(language):
            return self.plot.weather_summary(
                dark_mode_override=dark_mode_override, conditions=conditions, **args
            )

    def plot_sun_and_moon_path(
        self,
        dark_mode_override: Optional[bool] = None,
        language: Optional[str] = None,
        **args,
    ):
        with language_context(language):
            return self.plot.sun_and_moon_path(
                dark_mode_override=dark_mode_override, **args
            )

    def plot_skymap(
        self,
        target_name: Optional[str] = None,
        dark_mode_override: Optional[bool] = None,
        zoom_deg: Optional[float] = None,
        star_magnitude_limit: Optional[float] = None,
        plot_stars: bool = True,
        plot_messier: bool = False,
        plot_ngc: bool = False,
        plot_planets: bool = False,
        plot_sun: bool = False,
        plot_moon: bool = False,
        plot_date: Optional[datetime] = None,
        flip_horizontally: Optional[bool] = None,
        flip_vertically: Optional[bool] = None,
        coordinate_system: Optional[CoordinateSystem] = None,
        language: Optional[str] = None,
        texture_mode: bool = False,
        plot_labels: Optional[bool] = None,
        **kwargs,
    ) -> "matplotlib.figure.Figure":
        """
        Generates and displays a skymap for a specified celestial object.

        This method provides a high-level interface to the plotting capabilities in `apts.plot`.
        It can generate either a full-sky polar plot or a zoomed-in Cartesian plot for a
        given target. The orientation of the view can be flipped to match the output of
        certain telescopes.

        Args:
            target_name (Optional[str]): The name of the target object to center the skymap on.
            dark_mode_override (Optional[bool]): If set, overrides the system's dark mode setting.
            zoom_deg (Optional[float]): The diameter of the zoomed-in view in degrees. If None, a full skymap is generated.
            star_magnitude_limit (Optional[float]): The faintest magnitude of stars to plot.
            plot_stars (bool): Whether to plot stars on the skymap. Defaults to True.
            plot_messier (bool): Whether to plot Messier objects. Defaults to False.
            plot_ngc (bool): Whether to plot NGC objects. Defaults to False.
            plot_planets (bool): Whether to plot planets. Defaults to False.
            plot_sun (bool): Whether to plot Sun. Defaults to False.
            plot_moon (bool): Whether to plot Moon. Defaults to False.
            plot_date (Optional[datetime]): The specific date and time for which to generate the skymap.
                                            If None, the middle of the observation window is used.
            flip_horizontally (Optional[bool]): If True, the skymap's horizontal axis is inverted.
            flip_vertically (Optional[bool]): If True, the skymap's vertical axis is inverted.
            coordinate_system (Optional[CoordinateSystem]): The coordinate system to use for the skymap (e.g., 'altaz', 'radec').
            texture_mode (bool): If True, generates a 2D texture of the whole sky.
            plot_labels (Optional[bool]): Whether to plot labels. Defaults to True (False in texture mode).
            **kwargs: Additional keyword arguments to pass to the plotting function, including `equipment_id` and `figsize`.

        Returns:
            A matplotlib Figure object representing the skymap.
        """
        with language_context(language):
            return cast(
                "matplotlib.figure.Figure",
                self.plot.skymap(
                    target_name=target_name,
                    dark_mode_override=dark_mode_override,
                    zoom_deg=zoom_deg,
                    star_magnitude_limit=star_magnitude_limit,
                    plot_stars=plot_stars,
                    plot_messier=plot_messier,
                    plot_ngc=plot_ngc,
                    plot_planets=plot_planets,
                    plot_date=plot_date,
                    flip_horizontally=flip_horizontally,
                    flip_vertically=flip_vertically,
                    coordinate_system=coordinate_system,
                    texture_mode=texture_mode,
                    plot_labels=plot_labels,
                    **kwargs,
                ),
            )

    def plot_skymap_texture(
        self,
        dark_mode_override: Optional[bool] = None,
        star_magnitude_limit: Optional[float] = None,
        plot_stars: bool = True,
        plot_messier: bool = False,
        plot_ngc: bool = False,
        plot_planets: bool = False,
        plot_sun: bool = False,
        plot_moon: bool = False,
        plot_date: Optional[datetime] = None,
        coordinate_system: Optional[CoordinateSystem] = None,
        language: Optional[str] = None,
        plot_labels: bool = False,
        figsize: tuple = (40, 20),
        **kwargs,
    ) -> "matplotlib.figure.Figure":
        """
        Generates and displays a high-resolution skymap texture.

        Args:
            dark_mode_override (Optional[bool]): If set, overrides the system's dark mode setting.
            star_magnitude_limit (Optional[float]): The faintest magnitude of stars to plot.
            plot_stars (bool): Whether to plot stars. Defaults to True.
            plot_messier (bool): Whether to plot Messier objects. Defaults to False.
            plot_ngc (bool): Whether to plot NGC objects. Defaults to False.
            plot_planets (bool): Whether to plot planets. Defaults to False.
            plot_sun (bool): Whether to plot Sun. Defaults to False.
            plot_moon (bool): Whether to plot Moon. Defaults to False.
            plot_date (Optional[datetime]): The specific date and time for which to generate the skymap.
            coordinate_system (Optional[CoordinateSystem]): The coordinate system to use.
            language (Optional[str]): Language for translation.
            plot_labels (bool): Whether to plot labels. Defaults to False.
            figsize (tuple): Figure size for hi-res output. Defaults to (40, 20).
            **kwargs: Additional keyword arguments.

        Returns:
            A matplotlib Figure object representing the skymap texture.
        """
        with language_context(language):
            return cast(
                "matplotlib.figure.Figure",
                self.plot.skymap_texture(
                    dark_mode_override=dark_mode_override,
                    star_magnitude_limit=star_magnitude_limit,
                    plot_stars=plot_stars,
                    plot_messier=plot_messier,
                    plot_ngc=plot_ngc,
                    plot_planets=plot_planets,
                    plot_sun=plot_sun,
                    plot_moon=plot_moon,
                    plot_date=plot_date,
                    coordinate_system=coordinate_system,
                    plot_labels=plot_labels,
                    figsize=figsize,
                    **kwargs,
                ),
            )
