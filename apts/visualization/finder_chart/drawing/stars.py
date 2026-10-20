import logging
import math
from typing import TYPE_CHECKING, Any

import matplotlib.pyplot as plt
import numpy as np

if TYPE_CHECKING:
    from apts.events.event import Event

logger = logging.getLogger(__name__)


def _plot_bright_stars_catalog(
    ax: plt.Axes,
    obs_at_t: Any,
    az_min: float,
    az_max: float,
    alt_max: float,
    p1_pos: tuple[float, float],
    p2_pos: tuple[float, float] | None,
    theme: dict,
):
    """Plots bright stars from catalog with names and magnitude-based sizing."""
    from apts.catalogs.stars import (
        get_bright_stars_raw,
        get_bright_stars_skyfield_object,
    )
    from apts.skyfield_searches.utils import fast_altaz

    p1_az, p1_alt = p1_pos

    stars_df = get_bright_stars_raw()
    stars_sky_obj = get_bright_stars_skyfield_object()
    alt_v, az_v, _ = fast_altaz(obs_at_t, stars_sky_obj)
    st_alts = alt_v.degrees
    st_azs = az_v.degrees

    mags = stars_df["Magnitude_float"].to_numpy()
    names = stars_df["Name"].to_numpy()

    for i in range(len(stars_df)):
        st_alt = float(st_alts[i])
        st_az = float(st_azs[i])
        st_mag = float(mags[i])

        if st_az < az_min and st_az + 360.0 <= az_max:
            st_az += 360.0
        elif st_az > az_max and st_az - 360.0 >= az_min:
            st_az -= 360.0

        if az_min <= st_az <= az_max and 0.5 <= st_alt <= alt_max:
            if math.hypot(st_az - p1_az, st_alt - p1_alt) < 1.2 or (
                p2_pos and math.hypot(st_az - p2_pos[0], st_alt - p2_pos[1]) < 1.2
            ):
                continue
            size = max(4.0, 45.0 * (2.512 ** ((4.5 - st_mag) / 2.5)))
            alpha = max(0.3, min(1.0, (6.5 - st_mag) / 4.5))
            ax.scatter(
                st_az,
                st_alt,
                s=size,
                color=theme["star"],
                alpha=alpha,
                edgecolors="none",
                zorder=5,
            )

            st_name = str(names[i]).strip() if names[i] is not None else ""
            if st_name and st_mag <= 3.5:
                ax.text(
                    st_az,
                    st_alt + 0.6,
                    st_name,
                    color=theme["text_sub"],
                    fontsize=8,
                    fontweight="bold" if st_mag <= 2.0 else "normal",
                    alpha=0.85,
                    ha="center",
                    va="bottom",
                    zorder=6,
                )


def _plot_messier_catalog(
    ax: plt.Axes,
    obs_at_t: Any,
    az_min: float,
    az_max: float,
    alt_max: float,
    p1_pos: tuple[float, float],
    p2_pos: tuple[float, float] | None,
):
    """Plots Messier objects from catalog with type-colored markers and labels."""
    from apts.catalogs.messier import (
        get_messier_raw,
        get_messier_skyfield_object,
    )
    from apts.constants.graphconstants import get_messier_color
    from apts.skyfield_searches.utils import fast_altaz

    p1_az, p1_alt = p1_pos

    messier_df = get_messier_raw()
    messier_sky_obj = get_messier_skyfield_object()
    m_alt_v, m_az_v, _ = fast_altaz(obs_at_t, messier_sky_obj)
    m_alts = m_alt_v.degrees
    m_azs = m_az_v.degrees

    m_types = messier_df["Type"].to_numpy()
    m_names = messier_df["Messier"].to_numpy()

    for i in range(len(messier_df)):
        m_alt = float(m_alts[i])
        m_az = float(m_azs[i])

        if m_az < az_min and m_az + 360.0 <= az_max:
            m_az += 360.0
        elif m_az > az_max and m_az - 360.0 >= az_min:
            m_az -= 360.0

        if az_min <= m_az <= az_max and 1.0 <= m_alt <= alt_max:
            if math.hypot(m_az - p1_az, m_alt - p1_alt) < 1.5 or (
                p2_pos and math.hypot(m_az - p2_pos[0], m_alt - p2_pos[1]) < 1.5
            ):
                continue

            m_type = str(m_types[i]) if m_types[i] is not None else "Other"
            m_color = get_messier_color(m_type, effective_dark_mode=True)
            m_name = str(m_names[i])

            ax.scatter(
                m_az,
                m_alt,
                s=30,
                facecolors="none",
                edgecolors=m_color,
                linewidth=1.0,
                linestyle="--",
                zorder=7,
            )
            ax.scatter(m_az, m_alt, s=6, color=m_color, zorder=7)
            ax.text(
                m_az + 0.5,
                m_alt + 0.4,
                m_name,
                color=m_color,
                fontsize=8,
                fontweight="bold",
                ha="left",
                va="bottom",
                zorder=8,
            )


def _plot_fallback_background_stars(
    ax: plt.Axes,
    az_min: float,
    az_max: float,
    alt_max: float,
    center_az: float,
    center_alt: float,
    p1_pos: tuple[float, float],
    p2_pos: tuple[float, float] | None,
    theme: dict,
):
    """Plots random background stars when observer or timescale data is unavailable."""
    p1_az, p1_alt = p1_pos

    np.random.seed(int(center_az * 100 + center_alt) % 10000)
    num_bg_stars = 40
    bg_az = np.random.uniform(az_min, az_max, num_bg_stars)
    bg_alt = np.random.uniform(1.0, alt_max, num_bg_stars)
    bg_mag = np.random.uniform(2.0, 5.5, num_bg_stars)

    for st_az, st_alt, st_mag in zip(bg_az, bg_alt, bg_mag):
        if math.hypot(st_az - p1_az, st_alt - p1_alt) < 1.5 or (
            p2_pos and math.hypot(st_az - p2_pos[0], st_alt - p2_pos[1]) < 1.5
        ):
            continue
        size = max(4.0, 40.0 * (2.5 ** ((4.5 - st_mag) / 3.0)))
        alpha = max(0.3, min(1.0, (6.0 - st_mag) / 4.0))
        ax.scatter(
            st_az,
            st_alt,
            s=size,
            color=theme["star"],
            alpha=alpha,
            edgecolors="none",
            zorder=5,
        )


def _plot_background_stars(
    ax: plt.Axes,
    az_min: float,
    az_max: float,
    alt_max: float,
    center_az: float,
    center_alt: float,
    p1_pos: tuple[float, float],
    p2_pos: tuple[float, float] | None,
    event_obj: "Event",
    theme: dict,
):
    """Plots background stars and Messier objects using catalog positions with labels."""
    place = getattr(event_obj, "place", None)
    plotted_real = False

    if place is not None and hasattr(place, "observer") and hasattr(place, "ts"):
        try:
            dt_utc = event_obj.dt_utc
            ts_time = place.ts.utc(
                dt_utc.year,
                dt_utc.month,
                dt_utc.day,
                dt_utc.hour,
                dt_utc.minute,
                dt_utc.second,
            )
            obs_at_t = place.observer.at(ts_time)

            _plot_bright_stars_catalog(
                ax, obs_at_t, az_min, az_max, alt_max, p1_pos, p2_pos, theme
            )
            _plot_messier_catalog(
                ax, obs_at_t, az_min, az_max, alt_max, p1_pos, p2_pos
            )
            plotted_real = True
        except (ValueError, KeyError, AttributeError, TypeError, RuntimeError) as e:
            logger.debug(
                f"Failed to plot real background stars and Messier objects: {e}"
            )

    if not plotted_real:
        _plot_fallback_background_stars(
            ax,
            az_min,
            az_max,
            alt_max,
            center_az,
            center_alt,
            p1_pos,
            p2_pos,
            theme,
        )
