import io
import logging
import math
from typing import TYPE_CHECKING, Union

import matplotlib.pyplot as plt
import numpy as np

from .calculations import (
    _get_compass_labels,
    _hex_to_rgb,
    _parse_separation_deg,
    _resolve_target_coordinates,
)
from .constants import SKY_GRADIENT_COLORS, THEMES
from .drawing import (
    _draw_chart_time_note_banner,
    _draw_jovian_system,
    _draw_meteor_shower_radiant,
    _draw_planet_alignment,
    _draw_rocket_launch_trajectory,
    _draw_satellite_flyby_trail,
    _draw_single_object,
)

if TYPE_CHECKING:
    from matplotlib.figure import Figure

    from apts.events.event import Event

logger = logging.getLogger(__name__)


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
    sky_c_top_hex, sky_c_bot_hex = SKY_GRADIENT_COLORS.get(sky_brightness, (theme["sky_top"], theme["sky_bottom"]))
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
        ax.plot([c_az, c_az], [0.0, -1.2], color=theme["horizon_line"], linewidth=1.0, zorder=4)
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
    from apts.catalogs.messier import get_messier_raw
    from apts.catalogs.stars import get_bright_stars_raw
    from apts.constants.graphconstants import get_messier_color

    p1_az, p1_alt = p1_pos
    p2_az, p2_alt = p2_pos if p2_pos is not None else (None, None)

    place = getattr(event_obj, "place", None)
    plotted_real = False

    if place is not None and hasattr(place, "observer") and hasattr(place, "ts"):
        try:
            dt_utc = event_obj.dt_utc
            ts_time = place.ts.utc(dt_utc.year, dt_utc.month, dt_utc.day, dt_utc.hour, dt_utc.minute, dt_utc.second)
            obs_at_t = place.observer.at(ts_time)

            # 1. Plot Bright Stars with names
            stars_df = get_bright_stars_raw()
            for _, row in stars_df.iterrows():
                st_obj = row.get("skyfield_object")
                if st_obj is None:
                    continue
                app = obs_at_t.observe(st_obj).apparent()
                alt_obj, az_obj, _ = app.altaz()
                st_alt = float(alt_obj.degrees)
                st_az = float(az_obj.degrees)
                st_mag = float(row.get("Magnitude_float", 3.0))

                # Normalize azimuth range to chart window
                if st_az < az_min and st_az + 360.0 <= az_max:
                    st_az += 360.0
                elif st_az > az_max and st_az - 360.0 >= az_min:
                    st_az -= 360.0

                if az_min <= st_az <= az_max and 0.5 <= st_alt <= alt_max:
                    if math.hypot(st_az - p1_az, st_alt - p1_alt) < 1.2 or (p2_pos and math.hypot(st_az - p2_az, st_alt - p2_alt) < 1.2):
                        continue
                    size = max(4.0, 45.0 * (2.512 ** ((4.5 - st_mag) / 2.5)))
                    alpha = max(0.3, min(1.0, (6.5 - st_mag) / 4.5))
                    ax.scatter(st_az, st_alt, s=size, color=theme["star"], alpha=alpha, edgecolors="none", zorder=5)

                    st_name = str(row.get("Name", "")).strip()
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

            # 2. Plot Visible Messier Objects with labels (M1, M31, M42, etc.)
            messier_df = get_messier_raw()
            for _, m_row in messier_df.iterrows():
                m_obj = m_row.get("skyfield_object")
                if m_obj is None:
                    continue
                app_m = obs_at_t.observe(m_obj).apparent()
                m_alt_o, m_az_o, _ = app_m.altaz()
                m_alt = float(m_alt_o.degrees)
                m_az = float(m_az_o.degrees)

                if m_az < az_min and m_az + 360.0 <= az_max:
                    m_az += 360.0
                elif m_az > az_max and m_az - 360.0 >= az_min:
                    m_az -= 360.0

                if az_min <= m_az <= az_max and 1.0 <= m_alt <= alt_max:
                    if math.hypot(m_az - p1_az, m_alt - p1_alt) < 1.5 or (p2_pos and math.hypot(m_az - p2_az, m_alt - p2_alt) < 1.5):
                        continue

                    m_type = str(m_row.get("Type", "Other"))
                    m_color = get_messier_color(m_type, effective_dark_mode=True)
                    m_name = str(m_row.get("Messier", ""))

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
            logger.debug(f"Failed to plot real background stars and Messier objects: {e}")

    if not plotted_real:
        np.random.seed(int(center_az * 100 + center_alt) % 10000)
        num_bg_stars = 40
        bg_az = np.random.uniform(az_min, az_max, num_bg_stars)
        bg_alt = np.random.uniform(1.0, alt_max, num_bg_stars)
        bg_mag = np.random.uniform(2.0, 5.5, num_bg_stars)

        for st_az, st_alt, st_mag in zip(bg_az, bg_alt, bg_mag):
            if math.hypot(st_az - p1_az, st_alt - p1_alt) < 1.5 or (p2_pos and math.hypot(st_az - p2_az, st_alt - p2_alt) < 1.5):
                continue
            size = max(4.0, 40.0 * (2.5 ** ((4.5 - st_mag) / 3.0)))
            alpha = max(0.3, min(1.0, (6.0 - st_mag) / 4.0))
            ax.scatter(st_az, st_alt, s=size, color=theme["star"], alpha=alpha, edgecolors="none", zorder=5)


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

    moon_in_event = (
        any(any(k in str(o).lower() for k in moon_kws) for o in main_objs)
        or event_obj.category in ("OCCULTATION", "LUNAR_ECLIPSE", "MOON_PHASE", "SUPERMOON", "MOON_LIBRATION", "LUNAR_FEATURE")
    )
    obj1_is_moon = (
        any(k in obj1_name.lower() for k in moon_kws)
        or (moon_in_event and obj1_name in ("Moon", "Księżyc", "Mond", "Luna", "Target"))
    )

    sun_in_event = (
        any(any(k in str(o).lower() for k in sun_kws) for o in main_objs)
        or event_obj.category in ("EQUINOX_SOLSTICE", "SOLAR_ECLIPSE")
    )
    obj1_is_sun = (
        any(k in obj1_name.lower() for k in sun_kws)
        or (sun_in_event and obj1_name in ("Sun", "Słońce", "Sonne", "Sol", "Target"))
    )

    _draw_single_object(ax, obj1_name, p1_az, p1_alt, obj1_is_moon, "target_primary", 350, 120, event_obj, theme, is_sun=obj1_is_sun)

    if p2_pos is not None:
        p2_az, p2_alt = p2_pos
        obj2_name = main_objs[1] if len(main_objs) > 1 else "Companion"
        obj2_is_moon = any(k in obj2_name.lower() for k in moon_kws)
        obj2_is_sun = any(k in obj2_name.lower() for k in sun_kws)
        _draw_single_object(ax, obj2_name, p2_az, p2_alt, obj2_is_moon, "target_secondary", 260, 90, event_obj, theme, is_sun=obj2_is_sun)

        # Separation indicator
        ax.plot([p1_az, p2_az], [p1_alt, p2_alt], color=theme["separation_line"], linestyle="--", linewidth=1.2, alpha=0.85, zorder=13)
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


def generate_finder_chart(
    event: Union["Event", dict],
    format: str | None = "png",
    theme: str = "stargazer_dark",
    figsize: tuple[float, float] = (10, 8),
    dpi: int = 150,
    fov_deg: float | None = None,
    **kwargs,
) -> Union[bytes, str, "Figure"]:
    """
    Creates and returns a clean sky finder chart at the moment of an event.

    Parameters:
        event: Event instance or dictionary with event metadata.
        format: Export format - 'png' (returns bytes), 'svg' (returns str),
                or None/'figure' (returns matplotlib.figure.Figure).
        theme: 'stargazer_dark' or 'stargazer_light'.
        figsize: Output figure dimensions tuple (width, height).
        dpi: Output resolution.
        fov_deg: Horizontal field of view in degrees (default ~30-40 deg).

    Returns:
        PNG bytes, SVG string/bytes, or matplotlib Figure object.
    """
    from apts.events.event import Event

    event_obj = event if isinstance(event, Event) else Event.from_dict(dict(event))

    cat_upper = str(event_obj.category).upper()
    title_lower = str(event_obj.title).lower()

    t_theme = THEMES.get(theme, THEMES["stargazer_dark"])

    sep_deg = _parse_separation_deg(event_obj.angular_separation)
    p1_pos, p2_pos, all_target_positions, sky_brightness = _resolve_target_coordinates(
        event_obj, sep_deg
    )

    if p2_pos is not None:
        center_az = (p1_pos[0] + p2_pos[0]) / 2.0
        center_alt = (p1_pos[1] + p2_pos[1]) / 2.0
    else:
        center_az = p1_pos[0]
        center_alt = p1_pos[1]

    center_alt = max(10.0, min(80.0, center_alt))

    h_fov = float(fov_deg) if fov_deg is not None else 36.0
    v_fov = h_fov * (figsize[1] / figsize[0] if len(figsize) >= 2 and figsize[0] > 0 else 0.8)

    az_min, az_max = center_az - h_fov / 2.0, center_az + h_fov / 2.0
    alt_min, alt_max = -5.0, max(center_alt + v_fov / 1.5, 30.0)

    fig, ax = plt.subplots(figsize=figsize, dpi=dpi)
    fig.patch.set_facecolor(t_theme["sky_bg"])
    ax.set_facecolor(t_theme["sky_bg"])

    _setup_chart_axes_and_horizon(ax, az_min, az_max, alt_min, alt_max, sky_brightness, t_theme)
    _draw_chart_time_note_banner(ax, getattr(event_obj, "chart_time_note", None), t_theme)

    if cat_upper in ("FLYBY", "ISS_FLYBY", "TIANGONG_FLYBY") or "flyby" in title_lower or "iss" in title_lower or "tiangong" in title_lower:
        _draw_satellite_flyby_trail(ax, center_az, center_alt, event_obj, t_theme)
    elif cat_upper == "METEOR_SHOWER" or "shower" in title_lower or "meteor" in title_lower:
        _draw_meteor_shower_radiant(ax, center_az, center_alt, event_obj, t_theme)
    elif cat_upper in ("ROCKET_LAUNCH", "SPACE_LAUNCH") or "launch" in title_lower or "rocket" in title_lower:
        _draw_rocket_launch_trajectory(ax, center_az, center_alt, event_obj, t_theme)
    elif (cat_upper in ("PLANET_ALIGNMENT", "CELESTIAL_CONFIGURATION") or "alignment" in title_lower) and len(all_target_positions) >= 2:
        _draw_planet_alignment(ax, all_target_positions, event_obj, t_theme)
    elif "jovian" in cat_upper.lower() or "jovian" in title_lower or "grs" in title_lower or ("jupiter" in title_lower and ("moon" in title_lower or "transit" in title_lower)):
        _draw_jovian_system(ax, center_az, center_alt, event_obj, t_theme)
    else:
        _plot_primary_event_objects(ax, event_obj, p1_pos, p2_pos, sep_deg, t_theme)

    _plot_background_stars(ax, az_min, az_max, alt_max, center_az, center_alt, p1_pos, p2_pos, event_obj, t_theme)

    plt.subplots_adjust(left=0, right=1, bottom=0, top=1)

    if format is None or str(format).lower() in ("figure", "fig"):
        return fig

    fmt_clean = str(format).lower()
    buf = io.BytesIO()

    if fmt_clean == "svg":
        fig.savefig(buf, format="svg", facecolor=fig.get_facecolor(), bbox_inches="tight", pad_inches=0)
        plt.close(fig)
        return buf.getvalue().decode("utf-8")
    else:
        fig.savefig(buf, format="png", dpi=dpi, facecolor=fig.get_facecolor(), bbox_inches="tight", pad_inches=0)
        plt.close(fig)
        return buf.getvalue()


# Alias for APTS plotting API consistency
plot_finder_chart = generate_finder_chart
