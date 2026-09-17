import logging
import math
from typing import TYPE_CHECKING

import matplotlib.pyplot as plt
import numpy as np

from .calculations import (
    _get_compass_labels,
    _get_event_moon_phase_frac,
    _hex_to_rgb,
)
from .constants import SKY_GRADIENT_COLORS
from .renderers import (
    _draw_jovian_system,
    _draw_meteor_shower_radiant,
    _draw_moon_phase,
    _draw_planet_alignment,
    _draw_rocket_launch_trajectory,
    _draw_satellite_flyby_trail,
    _draw_sun_disk,
)

if TYPE_CHECKING:
    from apts.events.event import Event

logger = logging.getLogger(__name__)

__all__ = [
    "_draw_chart_time_note_banner",
    "_draw_jovian_system",
    "_draw_meteor_shower_radiant",
    "_draw_moon_phase",
    "_draw_planet_alignment",
    "_draw_rocket_launch_trajectory",
    "_draw_satellite_flyby_trail",
    "_draw_single_object",
    "_draw_sun_disk",
    "_plot_background_stars",
    "_plot_primary_event_objects",
    "_setup_chart_axes_and_horizon",
]


def _setup_chart_axes_and_horizon(
    ax: plt.Axes,
    az_min: float,
    az_max: float,
    alt_min: float,
    alt_max: float,
    sky_brightness: str,
    theme: dict,
):
    """Sets up canvas limits, hides frame, and draws smooth sky and ground gradients."""
    ax.axis("off")
    ax.set_xlim(az_min, az_max)
    ax.set_ylim(alt_min, alt_max)

    # 1. Sky Gradient
    sky_c_top_hex, sky_c_bot_hex = SKY_GRADIENT_COLORS.get(
        sky_brightness, (theme["sky_top"], theme["sky_bottom"])
    )
    c_sky_top = _hex_to_rgb(sky_c_top_hex)
    c_sky_bot = _hex_to_rgb(sky_c_bot_hex)

    n_grad = 256
    sky_rgb = np.zeros((n_grad, 1, 3))
    for i in range(3):
        sky_rgb[:, 0, i] = np.linspace(c_sky_bot[i], c_sky_top[i], n_grad)

    ax.imshow(
        sky_rgb,
        extent=[az_min - 5.0, az_max + 5.0, 0.0, alt_max + 5.0],
        aspect="auto",
        origin="lower",
        zorder=1,
    )

    # 2. Ground Gradient (Dark Earth / Green transition)
    c_grd_top = _hex_to_rgb(theme["ground_top"])
    c_grd_bot = _hex_to_rgb(theme["ground_bottom"])

    grd_rgb = np.zeros((n_grad, 1, 3))
    for i in range(3):
        grd_rgb[:, 0, i] = np.linspace(c_grd_bot[i], c_grd_top[i], n_grad)

    ax.imshow(
        grd_rgb,
        extent=[az_min - 5.0, az_max + 5.0, alt_min - 5.0, 0.0],
        aspect="auto",
        origin="lower",
        zorder=2,
    )

    # 3. Horizon Line and Compass Labels
    ax.axhline(0.0, color=theme["horizon_line"], linestyle="-", linewidth=1.5, zorder=3)

    for c_az, c_code in _get_compass_labels(az_min, az_max):
        ax.plot(
            [c_az, c_az], [0.0, -1.2], color=theme["horizon_line"], linewidth=1.0, zorder=4
        )
        ax.text(
            c_az,
            -3.2,
            c_code,
            color=theme["text_sub"],
            fontsize=10,
            fontweight="bold",
            ha="center",
            va="center",
            zorder=4,
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
    from apts.catalogs.messier import (
        get_messier_raw,
        get_messier_skyfield_object,
    )
    from apts.catalogs.stars import (
        get_bright_stars_raw,
        get_bright_stars_skyfield_object,
    )
    from apts.constants.graphconstants import get_messier_color
    from apts.skyfield_searches.utils import fast_altaz

    p1_az, p1_alt = p1_pos
    p2_az, p2_alt = p2_pos if p2_pos is not None else (None, None)

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

            # 1. Plot Bright Stars with names (vectorized fast_altaz observation)
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

                # Normalize azimuth range to chart window
                if st_az < az_min and st_az + 360.0 <= az_max:
                    st_az += 360.0
                elif st_az > az_max and st_az - 360.0 >= az_min:
                    st_az -= 360.0

                if az_min <= st_az <= az_max and 0.5 <= st_alt <= alt_max:
                    if math.hypot(st_az - p1_az, st_alt - p1_alt) < 1.2 or (
                        p2_pos and math.hypot(st_az - p2_az, st_alt - p2_alt) < 1.2
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

            # 2. Plot Visible Messier Objects with labels (vectorized fast_altaz observation)
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
                        p2_pos and math.hypot(m_az - p2_az, m_alt - p2_alt) < 1.5
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

            plotted_real = True
        except (ValueError, KeyError, AttributeError, TypeError, RuntimeError) as e:
            logger.debug(
                f"Failed to plot real background stars and Messier objects: {e}"
            )

    if not plotted_real:
        np.random.seed(int(center_az * 100 + center_alt) % 10000)
        num_bg_stars = 40
        bg_az = np.random.uniform(az_min, az_max, num_bg_stars)
        bg_alt = np.random.uniform(1.0, alt_max, num_bg_stars)
        bg_mag = np.random.uniform(2.0, 5.5, num_bg_stars)

        for st_az, st_alt, st_mag in zip(bg_az, bg_alt, bg_mag):
            if math.hypot(st_az - p1_az, st_alt - p1_alt) < 1.5 or (
                p2_pos and math.hypot(st_az - p2_az, st_alt - p2_alt) < 1.5
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


def _draw_single_object(
    ax: plt.Axes,
    name: str,
    az: float,
    alt: float,
    is_moon: bool,
    color_key: str,
    glow_size: float,
    dot_size: float,
    event_obj: "Event",
    theme: dict,
    is_sun: bool = False,
):
    """Renders an individual primary or secondary target object on the finder chart."""
    from apts.i18n import gettext_

    if is_moon:
        phase_frac = _get_event_moon_phase_frac(event_obj)
        _draw_moon_phase(
            ax, az, alt, radius_deg=0.9, phase_frac=phase_frac, theme=theme
        )
    elif is_sun:
        _draw_sun_disk(ax, az, alt, radius_deg=0.9, theme=theme)
    else:
        ax.scatter(
            az,
            alt,
            s=dot_size,
            color=theme[color_key],
            edgecolors=theme["star"],
            linewidth=1.0,
            zorder=12,
        )
        ax.scatter(
            az,
            alt,
            s=glow_size,
            color=theme[color_key],
            alpha=0.25,
            edgecolors="none",
            zorder=11,
        )

    display_name = gettext_(name).title()
    ax.text(
        az,
        alt + 1.4,
        display_name,
        color=theme["text_main"],
        fontsize=12 if color_key == "target_primary" else 11,
        fontweight="bold",
        ha="center",
        va="bottom",
        zorder=15,
    )


def _draw_chart_time_note_banner(ax: plt.Axes, note_text: str | None, theme: dict):
    """Renders a prominent informational banner on top of the chart figure for time shift or warning notes."""
    if not note_text:
        return
    note_lower = str(note_text).lower()
    is_warning = any(
        w in note_lower
        for w in (
            "warning",
            "ostrzeżenie",
            "advertencia",
            "warnung",
            "aviso",
            "below",
            "poniżej",
            "debajo",
            "unter",
            "abaixo",
        )
    )
    ax.text(
        0.5,
        0.96,
        note_text,
        transform=ax.transAxes,
        color="#FACC15" if is_warning else theme["text_main"],
        fontsize=9,
        fontweight="bold",
        ha="center",
        va="top",
        bbox={
            "boxstyle": "round,pad=0.35",
            "facecolor": theme["separation_bg"],
            "edgecolor": theme["separation_line"],
            "linewidth": 1.0,
            "alpha": 0.9,
        },
        zorder=20,
    )


def _plot_primary_event_objects(
    ax: plt.Axes,
    event_obj: "Event",
    p1_pos: tuple[float, float],
    p2_pos: tuple[float, float] | None,
    sep_deg: float,
    theme: dict,
) -> tuple[tuple[float, float], tuple[float, float] | None]:
    """Plots primary and secondary targets and separation indicator line."""
    main_objs = event_obj.objects or ["Target"]

    p1_az, p1_alt = p1_pos
    obj1_name = main_objs[0] if len(main_objs) > 0 else "Target"

    moon_kws = ("moon", "księżyc", "mond", "luna")
    sun_kws = ("sun", "słońce", "sonne", "sol")

    moon_in_event = any(
        any(k in str(o).lower() for k in moon_kws) for o in main_objs
    ) or event_obj.category in (
        "OCCULTATION",
        "LUNAR_ECLIPSE",
        "MOON_PHASE",
        "SUPERMOON",
        "MOON_LIBRATION",
        "LUNAR_FEATURE",
    )
    obj1_is_moon = any(k in obj1_name.lower() for k in moon_kws) or (
        moon_in_event and obj1_name in ("Moon", "Księżyc", "Mond", "Luna", "Target")
    )

    sun_in_event = any(
        any(k in str(o).lower() for k in sun_kws) for o in main_objs
    ) or event_obj.category in ("EQUINOX_SOLSTICE", "SOLAR_ECLIPSE")
    obj1_is_sun = any(k in obj1_name.lower() for k in sun_kws) or (
        sun_in_event and obj1_name in ("Sun", "Słońce", "Sonne", "Sol", "Target")
    )

    _draw_single_object(
        ax,
        obj1_name,
        p1_az,
        p1_alt,
        obj1_is_moon,
        "target_primary",
        350,
        120,
        event_obj,
        theme,
        is_sun=obj1_is_sun,
    )

    if p2_pos is not None:
        p2_az, p2_alt = p2_pos
        obj2_name = main_objs[1] if len(main_objs) > 1 else "Companion"
        obj2_is_moon = any(k in obj2_name.lower() for k in moon_kws)
        obj2_is_sun = any(k in obj2_name.lower() for k in sun_kws)
        _draw_single_object(
            ax,
            obj2_name,
            p2_az,
            p2_alt,
            obj2_is_moon,
            "target_secondary",
            260,
            90,
            event_obj,
            theme,
            is_sun=obj2_is_sun,
        )

        # Separation indicator
        ax.plot(
            [p1_az, p2_az],
            [p1_alt, p2_alt],
            color=theme["separation_line"],
            linestyle="--",
            linewidth=1.2,
            alpha=0.85,
            zorder=13,
        )
        mid_az, mid_alt = (p1_az + p2_az) / 2.0, (p1_alt + p2_alt) / 2.0
        sep_label = event_obj.angular_separation or f"{round(sep_deg, 1)}°"

        ax.text(
            mid_az,
            mid_alt - 0.9,
            sep_label,
            color=theme["target_primary"],
            fontsize=10,
            fontweight="bold",
            ha="center",
            va="top",
            bbox={
                "boxstyle": "round,pad=0.25",
                "facecolor": theme["separation_bg"],
                "edgecolor": theme["separation_line"],
                "linewidth": 0.8,
                "alpha": 0.9,
            },
            zorder=16,
        )

    return p1_pos, p2_pos
