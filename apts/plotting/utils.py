import functools
import logging
from datetime import datetime, timedelta
from typing import TYPE_CHECKING, Any, Optional, cast

import numpy
import pandas as pd
from matplotlib import dates as mdates, pyplot
from skyfield import almanac
from skyfield.units import Angle

from apts.constants.plot import CoordinateSystem
from apts.i18n import get_language
from apts.utils import planetary
from ..constants import ObjectTableLabels

if TYPE_CHECKING:
    from apts.observations import Observation

logger = logging.getLogger(__name__)


def calculate_parallactic_angle(
    latitude_deg: float, declination: Any, azimuth: Any
) -> float:
    """Calculates the parallactic angle in degrees."""
    dec_deg = (
        declination.degrees if hasattr(declination, "degrees") else float(declination)
    )
    if abs(dec_deg) > 89.99:
        return 0.0

    lat_rad = numpy.deg2rad(latitude_deg)
    dec_rad = (
        declination.radians if hasattr(declination, "radians") else numpy.deg2rad(dec_deg)
    )
    az_rad = (
        azimuth.radians
        if hasattr(azimuth, "radians")
        else numpy.deg2rad(azimuth)
    )

    sin_q = numpy.sin(az_rad) * numpy.cos(lat_rad) / numpy.cos(dec_rad)
    sin_q = numpy.clip(sin_q, -1.0, 1.0)
    q_rad = numpy.arcsin(sin_q)
    return numpy.rad2deg(q_rad)


def calculate_ellipse_angle(
    pos_angle: float,
    parallactic_angle: float | Angle,
    coordinate_system: CoordinateSystem,
    flipped_horizontally: bool,
    flipped_vertically: bool,
) -> float:
    """Calculates the final rotation angle for a celestial object's ellipse."""
    if coordinate_system == CoordinateSystem.HORIZONTAL:
        if hasattr(parallactic_angle, "degrees"):
            angle = pos_angle - cast(Any, parallactic_angle).degrees
        else:
            angle = pos_angle - cast(float, parallactic_angle)
        angle = -angle
    else:  # EQUATORIAL
        angle = -pos_angle

    if flipped_horizontally:
        angle = -angle
    if flipped_vertically:
        angle = 180 - angle

    return angle % 360


def get_object_angular_size_deg(observation: "Observation", object_name: str) -> float:
    """Gets the angular size of a solar system object in degrees."""
    # Handle translated names by reverse-translating if necessary
    current_lang = get_language()
    if current_lang != "en":
        reverse_map = planetary.get_reverse_translated_planet_names(current_lang)
        object_name = reverse_map.get(object_name, object_name)

    # Use the technical name for consistent matching regardless of language
    technical_name = planetary.get_technical_name(object_name)

    # Search in all computed planets (language-independent)
    planets_df = observation.local_planets.objects
    object_data = planets_df[
        (planets_df[ObjectTableLabels.NAME] == technical_name)
        | (planets_df[ObjectTableLabels.NAME] == object_name)
    ]

    if not object_data.empty:
        size_arcsec = object_data.iloc[0].get(ObjectTableLabels.SIZE)
        if pd.notna(size_arcsec):
            if hasattr(size_arcsec, "magnitude"):
                size_arcsec = size_arcsec.magnitude
            return float(size_arcsec) / 3600.0

    # Fallback to English-named visible planets
    visible_planets = observation.get_visible_planets(language="en")
    object_data = visible_planets[
        (visible_planets["TechnicalName"] == object_name)
        | (visible_planets["Name"] == object_name)
    ]
    if not object_data.empty:
        size_arcsec = object_data.iloc[0].get(ObjectTableLabels.SIZE)
        if pd.notna(size_arcsec):
            if hasattr(size_arcsec, "magnitude"):
                size_arcsec = size_arcsec.magnitude
            return float(size_arcsec) / 3600.0

    # Final fallback for Sun/Moon if not found above
    if technical_name in ["sun", "moon"]:
        return 0.5
    return 0.0


def get_brightness_color(magnitude: Optional[float]) -> str:
    """
    Calculates a grayscale color based on the magnitude of a celestial object.
    Dimmer objects get a color closer to the background.
    """
    if hasattr(magnitude, "magnitude"):
        magnitude = getattr(magnitude, "magnitude")  # type: ignore
    if magnitude is None or pd.isna(magnitude):
        return "none"

    # Normalize magnitude to a 0-1 range for color mapping
    # Typical naked-eye limit is 6. Faintest in catalogs can be ~15-20.
    # Let's cap the range for better visual differentiation.
    min_mag = 2.0  # Brightest objects
    max_mag = 12.0  # Faintest objects for fill variation

    norm_mag = (magnitude - min_mag) / (max_mag - min_mag)
    norm_mag = numpy.clip(norm_mag, 0, 1)

    # Invert the value, so brighter objects (lower mag) are lighter
    brightness = 1 - norm_mag

    # Blend the color with the background color to avoid pure white/black
    bg_color = pyplot.colormaps.get_cmap("gray")(0)
    fg_color = pyplot.colormaps.get_cmap("gray")(brightness)

    # Simple alpha blending: final_color = fg * alpha + bg * (1 - alpha)
    # We use brightness as a proxy for alpha here.
    final_color_val = fg_color[0] * brightness + bg_color[0] * (1 - brightness)
    final_color_val = numpy.clip(final_color_val, 0, 1)

    return str(final_color_val)


_style_initialized = False


def setup_plotting_style():
    """
    Initializes the Seaborn plotting style based on the configuration.
    """
    global _style_initialized
    if _style_initialized:
        return

    import seaborn as sns

    from apts.config import config

    allowed_styles = ["white", "dark", "whitegrid", "darkgrid", "ticks"]
    seaborn_style = config.get("style", "seaborn", fallback="whitegrid")
    if seaborn_style not in allowed_styles:
        logger.warning(
            f"Invalid seaborn style '{seaborn_style}' in config. Using default 'whitegrid'."
        )
        seaborn_style = "whitegrid"

    try:
        sns.set_style(seaborn_style)  # pyright: ignore
        logger.info(f"Seaborn style set to '{seaborn_style}'")
    except ValueError:
        # This is a fallback, in case of unexpected issues with seaborn
        logger.warning(
            f"Could not set seaborn style to '{seaborn_style}'. Using default 'whitegrid'."
        )
        sns.set_style("whitegrid")

    _style_initialized = True


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


def mark_observation(
    observation: "Observation", plot, dark_mode_enabled: bool, style: dict
):
    if plot is None:
        return

    # Save current limits to restore them later, preventing unwanted expansion
    # from axvspan or axvline calls.
    original_xlim = plot.get_xlim()

    # Get plot limits to know which range to mark
    try:
        x_min, x_max = original_xlim
        # Handle both numeric and datetime plot limits
        if isinstance(x_min, (float, int, numpy.number)):
            # Matplotlib date numbers. We need to be careful here:
            # If the axis is not initialized, x_min/x_max might be defaults like 0.0, 1.0
            # which represent 1970-01-01. This can lead to huge searches.
            if x_min < 1.0:  # Roughly 1970
                raise ValueError("Plot limits appear uninitialized (too early)")

            start_date = mdates.num2date(x_min, tz=observation.place.local_timezone)
            end_date = mdates.num2date(x_max, tz=observation.place.local_timezone)
        else:
            start_date = x_min
            end_date = x_max

        # Ensure we have datetime objects before proceeding
        if not isinstance(start_date, datetime) or not isinstance(end_date, datetime):
            raise ValueError("Plot limits are not valid datetime objects")

        # Sanity check: don't search more than 31 days.
        # This prevents runaway calculations if axis limits are somehow extreme.
        if (end_date - start_date).days > 31:
            logger.debug(f"Plot range too large ({(end_date - start_date).days} days), limiting to 31.")
            end_date = start_date + timedelta(days=31)

    except Exception as e:
        logger.debug(f"Could not determine plot range for multi-day marking: {e}")
        # Fallback to marking primary observation window if possible
        if observation.start and observation.time_limit:
            plot.axvline(observation.start, color=style["GRID_COLOR"], linestyle="--")
            plot.axvline(
                observation.time_limit, color=style["GRID_COLOR"], linestyle="--"
            )
        return

    # Use skyfield almanac for accurate and comprehensive day/night and moon marking
    try:
        shading_data = _get_astrometric_shading_data(
            observation.place.lat,
            observation.place.lon,
            observation.place.elevation,
            start_date,
            end_date,
        )

        alpha = 0.15 if dark_mode_enabled else 0.25

        # 1. Sun (Day and Night periods)
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

        # Last Sun segment to end_date
        color_key = "DAY_SPAN_COLOR" if sun_is_up else "SPAN_BACKGROUND_COLOR"
        plot.axvspan(
            current_t,
            end_date,
            color=style.get(color_key),
            alpha=alpha,
            label="_nolegend_",
        )

        # 2. Moon (Moon Presence periods)
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

        # Last Moon segment to end_date
        if moon_is_up:
            plot.axvspan(
                current_t,
                end_date,
                color=style.get("MOON_SPAN_COLOR"),
                alpha=alpha,
                label="_nolegend_",
            )
    except Exception as e:
        logger.debug(f"Astrometric shading failed (likely due to mocks): {e}")

    # Still mark the primary observation start/stop with dashed lines
    if observation.start:
        plot.axvline(observation.start, color=style["GRID_COLOR"], linestyle="--")
    if observation.time_limit:
        plot.axvline(observation.time_limit, color=style["GRID_COLOR"], linestyle="--")

    # Restore original limits
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
