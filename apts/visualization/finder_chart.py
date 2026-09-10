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
        "ground_bg": "#070A12",
        "horizon_line": "#1E293B",
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
        "ground_bg": "#E2E8F0",
        "horizon_line": "#CBD5E1",
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
    radius: float,
    phase_frac: float,
    theme: dict,
):
    """Renders a Moon disc with illuminated phase shading."""
    bright_color = theme["moon_bright"]
    dark_color = theme["moon_dark"]

    dark_disk = patches.Circle((x, y), radius, facecolor=dark_color, edgecolor=theme["text_sub"], linewidth=0.8, zorder=10)
    ax.add_patch(dark_disk)

    if phase_frac <= 0.02 or phase_frac >= 0.98:
        return

    if 0.48 <= phase_frac <= 0.52:
        bright_disk = patches.Circle((x, y), radius, facecolor=bright_color, edgecolor=None, zorder=11)
        ax.add_patch(bright_disk)
        return

    n_pts = 50
    theta = np.linspace(-np.pi / 2, np.pi / 2, n_pts)

    x_outer = radius * np.cos(theta)
    y_outer = radius * np.sin(theta)

    is_waxing = phase_frac < 0.5
    phase_angle = phase_frac * 2 * np.pi
    k = np.cos(phase_angle)

    x_term = radius * k * np.cos(theta)

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


def _setup_chart_axes_and_horizon(
    ax: plt.Axes,
    az_min: float,
    az_max: float,
    alt_min: float,
    alt_max: float,
    theme: dict,
):
    """Sets up canvas limits, hides frame, and draws ground/horizon elements."""
    ax.axis("off")
    ax.set_xlim(az_min, az_max)
    ax.set_ylim(alt_min, alt_max)

    ground_poly = patches.Rectangle(
        (az_min - 10.0, alt_min - 10.0),
        (az_max - az_min) + 20.0,
        10.0,
        facecolor=theme["ground_bg"],
        edgecolor=None,
        zorder=2,
    )
    ax.add_patch(ground_poly)
    ax.axhline(0.0, color=theme["horizon_line"], linestyle="-", linewidth=1.2, zorder=3)

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
    theme: dict,
):
    """Generates and plots contextual field stars."""
    np.random.seed(int(center_az * 100 + center_alt) % 10000)
    num_bg_stars = 45
    bg_az = np.random.uniform(az_min, az_max, num_bg_stars)
    bg_alt = np.random.uniform(1.0, alt_max, num_bg_stars)
    bg_mag = np.random.uniform(2.0, 5.5, num_bg_stars)

    p1_az, p1_alt = p1_pos
    p2_az, p2_alt = p2_pos

    for st_az, st_alt, st_mag in zip(bg_az, bg_alt, bg_mag):
        if math.hypot(st_az - p1_az, st_alt - p1_alt) < 1.5 or math.hypot(st_az - p2_az, st_alt - p2_alt) < 1.5:
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
        _draw_moon_phase(ax, az, alt, radius=0.9, phase_frac=phase, theme=theme)
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


def _plot_primary_event_objects(
    ax: plt.Axes,
    event_obj: "Event",
    center_az: float,
    center_alt: float,
    sep_deg: float,
    theme: dict,
) -> tuple[tuple[float, float], tuple[float, float]]:
    """Plots primary and secondary targets and separation indicator line."""
    main_objs = event_obj.objects or ["Moon", "Target"]
    p1_az, p1_alt = center_az, center_alt
    p2_az, p2_alt = center_az + sep_deg * 0.8, center_alt + sep_deg * 0.6

    obj1_name = main_objs[0] if len(main_objs) > 0 else "Moon"
    obj2_name = main_objs[1] if len(main_objs) > 1 else None

    moon_in_event = any("moon" in str(o).lower() or "księżyc" in str(o).lower() for o in main_objs) or event_obj.category in ("OCCULTATION", "LUNAR_ECLIPSE")
    obj1_is_moon = "moon" in obj1_name.lower() or "księżyc" in obj1_name.lower() or (moon_in_event and obj1_name == "Moon")

    _draw_single_object(ax, obj1_name, p1_az, p1_alt, obj1_is_moon, "target_primary", 350, 120, event_obj, theme)

    if obj2_name:
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

    return (p1_az, p1_alt), (p2_az, p2_alt)


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

    _setup_chart_axes_and_horizon(ax, az_min, az_max, alt_min, alt_max, t_theme)

    sep_deg = _parse_separation_deg(event_obj.angular_separation)
    p1_pos, p2_pos = _plot_primary_event_objects(ax, event_obj, center_az, center_alt, sep_deg, t_theme)
    _plot_background_stars(ax, az_min, az_max, alt_max, center_az, center_alt, p1_pos, p2_pos, t_theme)

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
