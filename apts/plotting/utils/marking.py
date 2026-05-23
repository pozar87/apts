import functools
import logging
import numpy
from datetime import datetime, timedelta
from typing import TYPE_CHECKING, Optional, Tuple, Dict, Any
from matplotlib import dates as mdates
from skyfield import almanac

if TYPE_CHECKING:
    from apts.observations import Observation

logger = logging.getLogger(__name__)

def normalize_dates(start, stop):
    if start is None or stop is None:
        return (None, None)
    if stop < start:
        stop += timedelta(days=1)
    return (start, stop)


def create_ra_zoom_mask(ra_hours, xlim):
    """
    Create a mask for RA values that fall within the zoom window,
    handling both the case where the window crosses the RA = 0/24 boundary
    and the case where the RA axis is inverted.

    Args:
        ra_hours: array of RA values in hours
        xlim: tuple of (x_left, x_right) RA values in hours

    Returns:
        boolean array mask indicating which RA values are in the zoom window
    """
    ra_1, ra_2 = xlim
    # Normalize to [0, 24]
    ra_1 %= 24
    ra_2 %= 24

    # We assume the window is the shorter arc between ra_1 and ra_2
    dist = abs(ra_1 - ra_2)
    if dist > 12:
        # Shorter arc is the one that wraps around 24
        ra_min = max(ra_1, ra_2)
        ra_max = min(ra_1, ra_2)
        return (ra_hours >= ra_min) | (ra_hours <= ra_max)
    else:
        # Shorter arc doesn't wrap
        ra_min = min(ra_1, ra_2)
        ra_max = max(ra_1, ra_2)
        return (ra_hours >= ra_min) & (ra_hours <= ra_max)


@functools.lru_cache(maxsize=128)
def _get_astrometric_shading_data(
    lat_rad: float,
    lon_rad: float,
    elevation: float,
    start_date: datetime,
    end_date: datetime,
):
    """
    Internal cached helper to calculate Sun and Moon rising/setting events.
    """
    from skyfield.api import Topos

    from apts.cache import get_ephemeris, get_timescale

    ts = get_timescale()
    eph = get_ephemeris()
    location = Topos(
        latitude_degrees=numpy.rad2deg(lat_rad),
        longitude_degrees=numpy.rad2deg(lon_rad),
        elevation_m=float(elevation),
    )

    t0 = ts.from_datetime(start_date)
    t1 = ts.from_datetime(end_date)

    # 1. Sun
    f_sun = almanac.risings_and_settings(eph, eph["sun"], location)
    t_sun, y_sun = almanac.find_discrete(t0, t1, f_sun)
    sun_events = [
        (t.astimezone(start_date.tzinfo), bool(y)) for t, y in zip(t_sun, y_sun)
    ]
    sun_init_up = bool(f_sun(t0))

    # 2. Moon
    f_moon = almanac.risings_and_settings(eph, eph["moon"], location)
    t_moon, y_moon = almanac.find_discrete(t0, t1, f_moon)
    moon_events = [
        (t.astimezone(start_date.tzinfo), bool(y)) for t, y in zip(t_moon, y_moon)
    ]
    moon_init_up = bool(f_moon(t0))

    return {
        "sun": {"init_up": sun_init_up, "events": sun_events},
        "moon": {"init_up": moon_init_up, "events": moon_events},
    }


def _get_plot_time_range(
    observation: "Observation", plot
) -> Tuple[datetime, datetime]:
    """Determines the datetime range of the plot for shading."""
    x_min, x_max = plot.get_xlim()

    if isinstance(x_min, (float, int, numpy.number)):
        if x_min < 1.0:
            raise ValueError("Plot limits appear uninitialized (too early)")
        start_date = mdates.num2date(x_min, tz=observation.place.local_timezone)
        end_date = mdates.num2date(x_max, tz=observation.place.local_timezone)
    else:
        start_date = x_min
        end_date = x_max

    if not isinstance(start_date, datetime) or not isinstance(end_date, datetime):
        raise ValueError("Plot limits are not valid datetime objects")

    if (end_date - start_date).days > 31:
        logger.debug(
            f"Plot range too large ({(end_date - start_date).days} days), limiting to 31."
        )
        end_date = start_date + timedelta(days=31)

    return start_date, end_date


def _plot_sun_shading(
    plot,
    start_date: datetime,
    end_date: datetime,
    shading_data: Dict[str, Any],
    style: Dict[str, Any],
    alpha: float,
):
    """Plots Sun-based (day/night) shading."""
    sun_is_up = shading_data["sun"]["init_up"]
    current_t = start_date

    for transition_time, next_up in shading_data["sun"]["events"]:
        color_key = "DAY_SPAN_COLOR" if sun_is_up else "SPAN_BACKGROUND_COLOR"
        plot.axvspan(
            current_t,
            transition_time,
            color=style.get(color_key),
            alpha=alpha,
            label="_nolegend_",
        )
        current_t = transition_time
        sun_is_up = next_up

    color_key = "DAY_SPAN_COLOR" if sun_is_up else "SPAN_BACKGROUND_COLOR"
    plot.axvspan(
        current_t,
        end_date,
        color=style.get(color_key),
        alpha=alpha,
        label="_nolegend_",
    )


def _plot_moon_shading(
    plot,
    start_date: datetime,
    end_date: datetime,
    shading_data: Dict[str, Any],
    style: Dict[str, Any],
    alpha: float,
):
    """Plots Moon presence shading."""
    moon_is_up = shading_data["moon"]["init_up"]
    current_t = start_date

    for transition_time, next_up in shading_data["moon"]["events"]:
        if moon_is_up:
            plot.axvspan(
                current_t,
                transition_time,
                color=style.get("MOON_SPAN_COLOR"),
                alpha=alpha,
                label="_nolegend_",
            )
        current_t = transition_time
        moon_is_up = next_up

    if moon_is_up:
        plot.axvspan(
            current_t,
            end_date,
            color=style.get("MOON_SPAN_COLOR"),
            alpha=alpha,
            label="_nolegend_",
        )


def _plot_observation_markers(observation: "Observation", plot, style: Dict[str, Any]):
    """Draws vertical lines for the primary observation window."""
    if observation.start:
        plot.axvline(observation.start, color=style["GRID_COLOR"], linestyle="--")
    if observation.time_limit:
        plot.axvline(observation.time_limit, color=style["GRID_COLOR"], linestyle="--")


def mark_observation(
    observation: "Observation", plot, dark_mode_enabled: bool, style: dict
):
    if plot is None:
        return

    original_xlim = plot.get_xlim()

    try:
        start_date, end_date = _get_plot_time_range(observation, plot)
    except Exception as e:
        logger.debug(f"Could not determine plot range for multi-day marking: {e}")
        _plot_observation_markers(observation, plot, style)
        return

    try:
        shading_data = _get_astrometric_shading_data(
            observation.place.lat,
            observation.place.lon,
            observation.place.elevation,
            start_date,
            end_date,
        )

        alpha = 0.15 if dark_mode_enabled else 0.25
        _plot_sun_shading(plot, start_date, end_date, shading_data, style, alpha)
        _plot_moon_shading(plot, start_date, end_date, shading_data, style, alpha)

    except Exception as e:
        logger.debug(f"Astrometric shading failed (likely due to mocks): {e}")

    _plot_observation_markers(observation, plot, style)
    plot.set_xlim(original_xlim)


def mark_good_conditions(
    observation: "Observation",
    plot,
    minimal,
    maximal,
    dark_mode_enabled: bool,
    style: dict,
):
    if plot is None:
        return
    plot.axhspan(
        minimal,
        maximal,
        color=style.get(
            "GOOD_CONDITION_HL_COLOR",
            "#90EE90" if not dark_mode_enabled else "#00FF7F",
        ),
        alpha=0.25,
    )
