import io
import logging
import math
from datetime import timezone
from typing import TYPE_CHECKING, Union

import matplotlib.pyplot as plt
import numpy as np
from matplotlib import patches

if TYPE_CHECKING:
    from matplotlib.figure import Figure

    from apts.events.event import Event

logger = logging.getLogger(__name__)
utc = timezone.utc

THEMES = {
    "stargazer_dark": {
        "sky_bg": "#0B0F19",
        "sky_top": "#0B0F19",
        "sky_bottom": "#1E293B",
        "ground_top": "#142319",
        "ground_bottom": "#070E09",
        "horizon_line": "#34D399",
        "text_main": "#F8FAFC",
        "text_sub": "#94A3B8",
        "star": "#FFFFFF",
        "star_glow": "#38BDF8",
        "target_primary": "#38BDF8",
        "target_secondary": "#FACC15",
        "moon_bright": "#F1F5F9",
        "moon_dark": "#1E293B",
        "separation_line": "#38BDF8",
        "separation_bg": "#0F172A",
    },
    "stargazer_light": {
        "sky_bg": "#F8FAFC",
        "sky_top": "#BAE6FD",
        "sky_bottom": "#F8FAFC",
        "ground_top": "#A7F3D0",
        "ground_bottom": "#D1FAE5",
        "horizon_line": "#059669",
        "text_main": "#0F172A",
        "text_sub": "#475569",
        "star": "#1E293B",
        "star_glow": "#0284C7",
        "target_primary": "#0284C7",
        "target_secondary": "#D97706",
        "moon_bright": "#475569",
        "moon_dark": "#CBD5E1",
        "separation_line": "#0284C7",
        "separation_bg": "#E2E8F0",
    },
}

SKY_GRADIENT_COLORS = {
    "DAY": ("#38BDF8", "#7DD3FC"),
    "CIVIL_TWILIGHT": ("#1E1B4B", "#F43F5E"),
    "NAUTICAL_TWILIGHT": ("0F172A", "#4338CA"),
    "ASTRONOMICAL_TWILIGHT": ("#0B0F19", "#1E293B"),
    "NIGHT_MOONLIT": ("#0F172A", "#1E293B"),
    "NIGHT_DARK": ("#0B0F19", "#111827"),
}

COMPASS_POINTS = [
    (0.0, "N"),
    (22.5, "NNE"),
    (45.0, "NE"),
    (67.5, "ENE"),
    (90.0, "E"),
    (112.5, "ESE"),
    (135.0, "SE"),
    (157.5, "SSE"),
    (180.0, "S"),
    (202.5, "SSW"),
    (225.0, "SW"),
    (247.5, "WSW"),
    (270.0, "W"),
    (292.5, "WNW"),
    (315.0, "NW"),
    (337.5, "NNW"),
    (360.0, "N"),
]


def _get_compass_labels(az_min: float, az_max: float) -> list[tuple[float, str]]:
    """Returns compass direction labels that fall within the given azimuth window."""
    labels = []
    for deg, code in COMPASS_POINTS:
        d = deg
        if d < az_min and d + 360.0 <= az_max:
            d += 360.0
        elif d > az_max and d - 360.0 >= az_min:
            d -= 360.0

        if az_min <= d <= az_max:
            labels.append((d, code))

    return labels


def _draw_moon_phase(
    ax: plt.Axes,
    x: float,
    y: float,
    radius_deg: float,
    phase_frac: float,
    theme: dict,
):
    """Renders a Moon disc with illuminated phase shading, maintaining circular aspect ratio."""
    bright_color = theme["moon_bright"]
    dark_color = theme["moon_dark"]

    # Account for data aspect ratio so Moon disc is a true circle in data coordinates
    xlim = ax.get_xlim()
    ylim = ax.get_ylim()
    bbox = ax.get_window_extent()
    ax_width = bbox.width if bbox else 1.0
    ax_height = bbox.height if bbox else 1.0
    data_width = xlim[1] - xlim[0]
    data_height = ylim[1] - ylim[0]

    rx = radius_deg
    ry = radius_deg * (data_height / data_width) * (ax_width / ax_height) if data_width > 0 and ax_height > 0 else radius_deg

    dark_disk = patches.Ellipse((x, y), width=2 * rx, height=2 * ry, facecolor=dark_color, edgecolor=theme["text_sub"], linewidth=0.8, zorder=10)
    ax.add_patch(dark_disk)

    if phase_frac <= 0.02 or phase_frac >= 0.98:
        return

    if 0.48 <= phase_frac <= 0.52:
        bright_disk = patches.Ellipse((x, y), width=2 * rx, height=2 * ry, facecolor=bright_color, edgecolor=None, zorder=11)
        ax.add_patch(bright_disk)
        return

    n_pts = 50
    theta = np.linspace(-np.pi / 2, np.pi / 2, n_pts)

    x_outer = rx * np.cos(theta)
    y_outer = ry * np.sin(theta)

    is_waxing = phase_frac < 0.5
    phase_angle = phase_frac * 2 * np.pi
    k = np.cos(phase_angle)

    x_term = rx * k * np.cos(theta)

    if is_waxing:
        poly_x = np.concatenate([x + x_outer, x + x_term[::-1]])
        poly_y = np.concatenate([y + y_outer, y + y_outer[::-1]])
    else:
        poly_x = np.concatenate([x - x_outer, x - x_term[::-1]])
        poly_y = np.concatenate([y + y_outer, y + y_outer[::-1]])

    poly_pts = np.column_stack([poly_x, poly_y])
    polygon = patches.Polygon(poly_pts, closed=True, facecolor=bright_color, edgecolor=None, zorder=11)
    ax.add_patch(polygon)


def _parse_separation_deg(sep_str: str | None) -> float:
    """Parses angular separation degrees from string representation."""
    if not sep_str:
        return 1.2
    try:
        clean_sep = sep_str.replace("°", "").replace("'", "").strip()
        val = float(clean_sep)
        if "'" in sep_str:
            val = val / 60.0
        return max(0.2, min(5.0, val))
    except ValueError:
        return 1.2


def _hex_to_rgb(hex_str: str) -> np.ndarray:
    clean = hex_str.lstrip("#")
    return np.array([int(clean[i : i + 2], 16) / 255.0 for i in (0, 2, 4)])


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
    p2_pos: tuple[float, float],
    event_obj: "Event",
    theme: dict,
):
    """Plots background stars using real catalog positions when place/time is available or realistic grid."""
    from apts.catalogs.stars import get_bright_stars_raw

    p1_az, p1_alt = p1_pos
    p2_az, p2_alt = p2_pos

    place = getattr(event_obj, "place", None)
    plotted_real = False

    if place is not None and hasattr(place, "observer") and hasattr(place, "ts"):
        try:
            dt_utc = event_obj.dt_utc
            ts_time = place.ts.utc(dt_utc.year, dt_utc.month, dt_utc.day, dt_utc.hour, dt_utc.minute, dt_utc.second)
            obs_at_t = place.observer.at(ts_time)
            stars_df = get_bright_stars_raw()

            for _, row in stars_df.iterrows():
                st_obj = row.get("skyfield_object")
                if st_obj is None:
                    continue
                app = obs_at_t.observe(st_obj).apparent()
                alt_obj, az_obj, _ = app.altaz()
                st_alt = alt_obj.degrees
                st_az = az_obj.degrees
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
                    ax.text(
                        st_az,
                        st_alt + 0.6,
                        str(row.get("Name", "")),
                        color=theme["text_sub"],
                        fontsize=7,
                        alpha=0.7,
                        ha="center",
                        va="bottom",
                        zorder=6,
                    )
            plotted_real = True
        except Exception as e:
            logger.debug(f"Failed to plot real background stars: {e}")

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
):
    """Renders an individual primary or secondary target object on the finder chart."""
    if is_moon:
        phase = float(event_obj.extra_data.get("phase", 0.25)) if isinstance(event_obj.extra_data.get("phase"), (int, float)) else 0.25
        _draw_moon_phase(ax, az, alt, radius_deg=0.9, phase_frac=phase, theme=theme)
    else:
        ax.scatter(az, alt, s=dot_size, color=theme[color_key], edgecolors=theme["star"], linewidth=1.0, zorder=12)
        ax.scatter(az, alt, s=glow_size, color=theme[color_key], alpha=0.25, edgecolors="none", zorder=11)

    ax.text(
        az,
        alt + 1.4,
        name.title(),
        color=theme["text_main"],
        fontsize=12 if color_key == "target_primary" else 11,
        fontweight="bold",
        ha="center",
        va="bottom",
        zorder=15,
    )


def _resolve_target_coordinates(
    event_obj: "Event",
    center_az: float,
    center_alt: float,
    sep_deg: float,
) -> tuple[tuple[float, float], tuple[float, float] | None]:
    """Calculates topocentric Az/Alt for primary and secondary targets."""
    place = getattr(event_obj, "place", None)
    main_objs = event_obj.objects or []

    # If place and skyfield objects available, compute exact coordinates
    if place is not None and len(main_objs) >= 2 and hasattr(place, "get_altitude") and hasattr(place, "get_azimuth"):
        try:
            dt_utc = event_obj.dt_utc
            ts_time = place.ts.utc(dt_utc.year, dt_utc.month, dt_utc.day, dt_utc.hour, dt_utc.minute, dt_utc.second)

            obj1 = main_objs[0]
            obj2 = main_objs[1]

            alt1 = place.get_altitude(obj1, ts_time)
            az1 = place.get_azimuth(obj1, ts_time)
            alt2 = place.get_altitude(obj2, ts_time)
            az2 = place.get_azimuth(obj2, ts_time)

            if not math.isnan(alt1) and not math.isnan(az1) and not math.isnan(alt2) and not math.isnan(az2):
                return (az1, alt1), (az2, alt2)
        except Exception as e:
            logger.debug(f"Could not compute exact target topocentric coordinates: {e}")

    # Fallback to event coordinates and angular separation offset
    p1_az, p1_alt = center_az, center_alt
    if len(main_objs) >= 2 or event_obj.angular_separation:
        p2_az = center_az + sep_deg * 0.8
        p2_alt = center_alt + sep_deg * 0.6
        return (p1_az, p1_alt), (p2_az, p2_alt)

    return (p1_az, p1_alt), None


def _plot_primary_event_objects(
    ax: plt.Axes,
    event_obj: "Event",
    center_az: float,
    center_alt: float,
    sep_deg: float,
    theme: dict,
) -> tuple[tuple[float, float], tuple[float, float] | None]:
    """Plots primary and secondary targets and separation indicator line."""
    main_objs = event_obj.objects or ["Target"]
    p1_pos, p2_pos = _resolve_target_coordinates(event_obj, center_az, center_alt, sep_deg)

    p1_az, p1_alt = p1_pos
    obj1_name = main_objs[0] if len(main_objs) > 0 else "Target"

    moon_in_event = any("moon" in str(o).lower() or "księżyc" in str(o).lower() for o in main_objs) or event_obj.category in ("OCCULTATION", "LUNAR_ECLIPSE")
    obj1_is_moon = "moon" in obj1_name.lower() or "księżyc" in obj1_name.lower() or (moon_in_event and obj1_name == "Moon")

    _draw_single_object(ax, obj1_name, p1_az, p1_alt, obj1_is_moon, "target_primary", 350, 120, event_obj, theme)

    if p2_pos is not None:
        p2_az, p2_alt = p2_pos
        obj2_name = main_objs[1] if len(main_objs) > 1 else "Companion"
        obj2_is_moon = "moon" in obj2_name.lower() or "księżyc" in obj2_name.lower()
        _draw_single_object(ax, obj2_name, p2_az, p2_alt, obj2_is_moon, "target_secondary", 260, 90, event_obj, theme)

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

    # Finder charts are not applicable for rocket/space launches
    cat_upper = str(event_obj.category).upper()
    title_lower = str(event_obj.title).lower()
    if cat_upper in ("ROCKET_LAUNCH", "SPACE_LAUNCH") or "launch" in title_lower or "rocket" in title_lower:
        return None

    t_theme = THEMES.get(theme, THEMES["stargazer_dark"])

    center_az = float(event_obj.azimuth_deg) if event_obj.azimuth_deg is not None else 90.0
    center_alt = max(10.0, min(80.0, float(event_obj.altitude_deg) if event_obj.altitude_deg is not None else 25.0))

    h_fov = float(fov_deg) if fov_deg is not None else 36.0
    v_fov = h_fov * (figsize[1] / figsize[0] if len(figsize) >= 2 and figsize[0] > 0 else 0.8)

    az_min, az_max = center_az - h_fov / 2.0, center_az + h_fov / 2.0
    alt_min, alt_max = -5.0, max(center_alt + v_fov / 1.5, 30.0)

    fig, ax = plt.subplots(figsize=figsize, dpi=dpi)
    fig.patch.set_facecolor(t_theme["sky_bg"])
    ax.set_facecolor(t_theme["sky_bg"])

    sky_brightness = getattr(event_obj, "sky_brightness", "NIGHT_DARK")
    _setup_chart_axes_and_horizon(ax, az_min, az_max, alt_min, alt_max, sky_brightness, t_theme)

    sep_deg = _parse_separation_deg(event_obj.angular_separation)
    p1_pos, p2_pos = _plot_primary_event_objects(ax, event_obj, center_az, center_alt, sep_deg, t_theme)
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
