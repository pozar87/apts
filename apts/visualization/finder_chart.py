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
        # Check direct or wrapped azimuth
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
    phase_frac: float,  # 0.0 = New, 0.25 = First Qtr, 0.5 = Full, 0.75 = Last Qtr
    theme: dict,
):
    """Renders a Moon disc with illuminated phase shading."""
    bright_color = theme["moon_bright"]
    dark_color = theme["moon_dark"]

    # Base dark disk
    dark_disk = patches.Circle((x, y), radius, facecolor=dark_color, edgecolor=theme["text_sub"], linewidth=0.8, zorder=10)
    ax.add_patch(dark_disk)

    if phase_frac <= 0.02 or phase_frac >= 0.98:
        # New Moon - fully dark
        return

    if 0.48 <= phase_frac <= 0.52:
        # Full Moon - fully illuminated
        bright_disk = patches.Circle((x, y), radius, facecolor=bright_color, edgecolor=None, zorder=11)
        ax.add_patch(bright_disk)
        return

    # Draw illuminated crescent / gibbous polygon approximation
    n_pts = 50
    theta = np.linspace(-np.pi / 2, np.pi / 2, n_pts)

    # Outer arc
    x_outer = radius * np.cos(theta)
    y_outer = radius * np.sin(theta)

    # Terminator arc
    # Phase 0.0..0.5: Waxing (right side illuminated)
    # Phase 0.5..1.0: Waning (left side illuminated)
    is_waxing = phase_frac < 0.5
    phase_angle = phase_frac * 2 * np.pi
    k = np.cos(phase_angle)  # Ranges from 1 (full) to -1 (new)

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

    if not isinstance(event, Event):
        event_obj = Event.from_dict(dict(event))
    else:
        event_obj = event

    t_theme = THEMES.get(theme, THEMES["stargazer_dark"])

    # Center coordinates
    center_az = float(event_obj.azimuth_deg) if event_obj.azimuth_deg is not None else 90.0
    center_alt = float(event_obj.altitude_deg) if event_obj.altitude_deg is not None else 25.0

    # Ensure center altitude is above horizon for view framing
    center_alt = max(10.0, min(80.0, center_alt))

    # Field of view
    h_fov = float(fov_deg) if fov_deg is not None else 36.0
    v_fov = h_fov * (figsize[1] / figsize[0] if len(figsize) >= 2 and figsize[0] > 0 else 0.8)

    az_min = center_az - h_fov / 2.0
    az_max = center_az + h_fov / 2.0
    alt_min = -5.0  # Show horizon profile
    alt_max = max(center_alt + v_fov / 1.5, 30.0)

    fig, ax = plt.subplots(figsize=figsize, dpi=dpi)
    fig.patch.set_facecolor(t_theme["sky_bg"])
    ax.set_facecolor(t_theme["sky_bg"])

    # Remove all borders/axes frames
    ax.axis("off")
    ax.set_xlim(az_min, az_max)
    ax.set_ylim(alt_min, alt_max)

    # 1. Subtle Horizon Profile
    # Fill ground polygon below Alt = 0 deg
    ground_poly = patches.Rectangle(
        (az_min - 10.0, alt_min - 10.0),
        (az_max - az_min) + 20.0,
        10.0,
        facecolor=t_theme["ground_bg"],
        edgecolor=None,
        zorder=2,
    )
    ax.add_patch(ground_poly)

    # Horizon line
    ax.axhline(0.0, color=t_theme["horizon_line"], linestyle="-", linewidth=1.2, zorder=3)

    # Compass direction labels along horizon
    compass_labels = _get_compass_labels(az_min, az_max)
    for c_az, c_code in compass_labels:
        ax.plot([c_az, c_az], [0.0, -1.2], color=t_theme["horizon_line"], linewidth=1.0, zorder=4)
        ax.text(
            c_az,
            -3.2,
            c_code,
            color=t_theme["text_sub"],
            fontsize=10,
            fontweight="bold",
            ha="center",
            va="center",
            zorder=4,
        )

    # 2. Celestial Objects Setup
    main_objs = event_obj.objects or ["Moon", "Target"]

    # Generate or compute positions for primary objects
    p1_az = center_az
    p1_alt = center_alt

    # Calculate offset for secondary object if separation exists
    sep_str = event_obj.angular_separation
    sep_deg = 1.2  # Default offset degrees
    if sep_str:
        try:
            clean_sep = sep_str.replace("°", "").replace("'", "").strip()
            val = float(clean_sep)
            if "'" in sep_str:
                val = val / 60.0
            sep_deg = max(0.2, min(5.0, val))
        except ValueError:
            sep_deg = 1.2

    p2_az = center_az + sep_deg * 0.8
    p2_alt = center_alt + sep_deg * 0.6

    # 3. Background Stars Context Field
    # Deterministic background stars array around target
    np.random.seed(int(center_az * 100 + center_alt) % 10000)
    num_bg_stars = 45
    bg_az = np.random.uniform(az_min, az_max, num_bg_stars)
    bg_alt = np.random.uniform(1.0, alt_max, num_bg_stars)
    bg_mag = np.random.uniform(2.0, 5.5, num_bg_stars)

    for st_az, st_alt, st_mag in zip(bg_az, bg_alt, bg_mag):
        # Skip if too close to main objects
        if math.hypot(st_az - p1_az, st_alt - p1_alt) < 1.5 or math.hypot(st_az - p2_az, st_alt - p2_alt) < 1.5:
            continue
        size = max(4.0, 40.0 * (2.5 ** ((4.5 - st_mag) / 3.0)))
        alpha = max(0.3, min(1.0, (6.0 - st_mag) / 4.0))
        ax.scatter(st_az, st_alt, s=size, color=t_theme["star"], alpha=alpha, edgecolors="none", zorder=5)

    # 4. Primary Celestial Objects Plotting
    obj1_name = main_objs[0] if len(main_objs) > 0 else "Moon"
    obj2_name = main_objs[1] if len(main_objs) > 1 else None

    # Check if Moon is primary or secondary object
    moon_in_event = any("moon" in str(o).lower() or "księżyc" in str(o).lower() for o in main_objs) or event_obj.category in ("OCCULTATION", "LUNAR_ECLIPSE")

    # Plot Object 1
    if "moon" in obj1_name.lower() or "księżyc" in obj1_name.lower() or (moon_in_event and obj1_name == "Moon"):
        phase = float(event_obj.extra_data.get("phase", 0.25)) if isinstance(event_obj.extra_data.get("phase"), (int, float)) else 0.25
        _draw_moon_phase(ax, p1_az, p1_alt, radius=0.9, phase_frac=phase, theme=t_theme)
        ax.text(
            p1_az,
            p1_alt + 1.6,
            obj1_name.title(),
            color=t_theme["text_main"],
            fontsize=12,
            fontweight="bold",
            ha="center",
            va="bottom",
            zorder=15,
        )
    else:
        ax.scatter(
            p1_az,
            p1_alt,
            s=120,
            color=t_theme["target_primary"],
            edgecolors=t_theme["star"],
            linewidth=1.2,
            zorder=12,
        )
        # Glow halo
        ax.scatter(p1_az, p1_alt, s=350, color=t_theme["target_primary"], alpha=0.25, edgecolors="none", zorder=11)
        ax.text(
            p1_az,
            p1_alt + 1.4,
            obj1_name.title(),
            color=t_theme["text_main"],
            fontsize=12,
            fontweight="bold",
            ha="center",
            va="bottom",
            zorder=15,
        )

    # Plot Object 2 if present
    if obj2_name:
        if "moon" in obj2_name.lower() or "księżyc" in obj2_name.lower():
            phase = float(event_obj.extra_data.get("phase", 0.25)) if isinstance(event_obj.extra_data.get("phase"), (int, float)) else 0.25
            _draw_moon_phase(ax, p2_az, p2_alt, radius=0.9, phase_frac=phase, theme=t_theme)
            ax.text(
                p2_az,
                p2_alt + 1.6,
                obj2_name.title(),
                color=t_theme["text_main"],
                fontsize=12,
                fontweight="bold",
                ha="center",
                va="bottom",
                zorder=15,
            )
        else:
            ax.scatter(
                p2_az,
                p2_alt,
                s=90,
                color=t_theme["target_secondary"],
                edgecolors=t_theme["star"],
                linewidth=1.0,
                zorder=12,
            )
            # Glow halo
            ax.scatter(p2_az, p2_alt, s=260, color=t_theme["target_secondary"], alpha=0.3, edgecolors="none", zorder=11)
            ax.text(
                p2_az,
                p2_alt + 1.4,
                obj2_name.title(),
                color=t_theme["text_main"],
                fontsize=11,
                fontweight="bold",
                ha="center",
                va="bottom",
                zorder=15,
            )

        # 5. Angular Separation Arc / Indicator Line
        if sep_str or sep_deg:
            ax.plot(
                [p1_az, p2_az],
                [p1_alt, p2_alt],
                color=t_theme["separation_line"],
                linestyle="--",
                linewidth=1.2,
                alpha=0.85,
                zorder=13,
            )

            # Separation text badge
            mid_az = (p1_az + p2_az) / 2.0
            mid_alt = (p1_alt + p2_alt) / 2.0
            sep_label = sep_str if sep_str else f"{round(sep_deg, 1)}°"

            ax.text(
                mid_az,
                mid_alt - 0.9,
                sep_label,
                color=t_theme["target_primary"],
                fontsize=10,
                fontweight="bold",
                ha="center",
                va="top",
                bbox={
                    "boxstyle": "round,pad=0.25",
                    "facecolor": t_theme["separation_bg"],
                    "edgecolor": t_theme["separation_line"],
                    "linewidth": 0.8,
                    "alpha": 0.9,
                },
                zorder=16,
            )

    plt.subplots_adjust(left=0, right=1, bottom=0, top=1)

    # Handle output format
    if format is None or str(format).lower() in ("figure", "fig"):
        return fig

    fmt_clean = str(format).lower()
    buf = io.BytesIO()

    if fmt_clean == "svg":
        fig.savefig(buf, format="svg", facecolor=fig.get_facecolor(), bbox_inches="tight", pad_inches=0)
        plt.close(fig)
        return buf.getvalue().decode("utf-8")
    else:
        # Default PNG output
        fig.savefig(buf, format="png", dpi=dpi, facecolor=fig.get_facecolor(), bbox_inches="tight", pad_inches=0)
        plt.close(fig)
        return buf.getvalue()


# Alias for APTS plotting API consistency
plot_finder_chart = generate_finder_chart
