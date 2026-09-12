import logging
from datetime import timedelta
from typing import TYPE_CHECKING

import matplotlib.pyplot as plt
import numpy as np
from matplotlib import patches

from .calculations import (
    _get_event_moon_phase_frac,
    _get_satellite_name,
)

if TYPE_CHECKING:
    from apts.events.event import Event

logger = logging.getLogger(__name__)


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


def _draw_sun_disk(
    ax: plt.Axes,
    x: float,
    y: float,
    radius_deg: float,
    theme: dict,
):
    """Renders a Sun disc with solar corona/glow, maintaining circular aspect ratio matching the Moon."""
    xlim = ax.get_xlim()
    ylim = ax.get_ylim()
    bbox = ax.get_window_extent()
    ax_width = bbox.width if bbox else 1.0
    ax_height = bbox.height if bbox else 1.0
    data_width = xlim[1] - xlim[0]
    data_height = ylim[1] - ylim[0]

    rx = radius_deg
    ry = radius_deg * (data_height / data_width) * (ax_width / ax_height) if data_width > 0 and ax_height > 0 else radius_deg

    glow_outer = patches.Ellipse((x, y), width=3.2 * rx, height=3.2 * ry, facecolor="#FDE047", alpha=0.25, edgecolor=None, zorder=10)
    ax.add_patch(glow_outer)

    glow_inner = patches.Ellipse((x, y), width=2.2 * rx, height=2.2 * ry, facecolor="#FACC15", alpha=0.4, edgecolor=None, zorder=10)
    ax.add_patch(glow_inner)

    sun_disk = patches.Ellipse((x, y), width=2 * rx, height=2 * ry, facecolor="#F59E0B", edgecolor="#FEF08A", linewidth=1.2, zorder=11)
    ax.add_patch(sun_disk)


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
        _draw_moon_phase(ax, az, alt, radius_deg=0.9, phase_frac=phase_frac, theme=theme)
    elif is_sun:
        _draw_sun_disk(ax, az, alt, radius_deg=0.9, theme=theme)
    else:
        ax.scatter(az, alt, s=dot_size, color=theme[color_key], edgecolors=theme["star"], linewidth=1.0, zorder=12)
        ax.scatter(az, alt, s=glow_size, color=theme[color_key], alpha=0.25, edgecolors="none", zorder=11)

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


def _draw_satellite_flyby_trail(
    ax: plt.Axes,
    center_az: float,
    center_alt: float,
    event_obj: "Event",
    theme: dict,
):
    """Renders a satellite flyby trajectory trail across the sky with arrows and peak marker."""
    from apts.skyfield_searches.satellites.flybys import _load_satellite

    sat_name = _get_satellite_name(event_obj)

    # Try exact topocentric trajectory evaluation if place and satellite TLE are available
    place = getattr(event_obj, "place", None)
    calculated_trajectory = False

    if place is not None and hasattr(place, "observer") and hasattr(place, "ts"):
        tle_sat_name = "ISS (ZARYA)" if "iss" in sat_name.lower() else "CSS (TIANHE)" if "tiangong" in sat_name.lower() or "china" in sat_name.lower() else None
        if tle_sat_name:
            try:
                sat = _load_satellite(tle_sat_name)
                if sat is not None:
                    dt_peak = event_obj.dt_utc
                    ts_times = [place.ts.utc((dt_peak + timedelta(seconds=sec)).year, (dt_peak + timedelta(seconds=sec)).month, (dt_peak + timedelta(seconds=sec)).day, (dt_peak + timedelta(seconds=sec)).hour, (dt_peak + timedelta(seconds=sec)).minute, (dt_peak + timedelta(seconds=sec)).second) for sec in range(-240, 241, 10)]
                    topos = sat - place.observer

                    az_curve, alt_curve = [], []
                    for t_sf in ts_times:
                        alt_o, az_o, _ = topos.at(t_sf).apparent().altaz()
                        a_deg, z_deg = float(alt_o.degrees), float(az_o.degrees)
                        if a_deg >= 1.0:
                            alt_curve.append(a_deg)
                            az_curve.append(z_deg)

                    if len(alt_curve) >= 5:
                        az_curve = np.array(az_curve)
                        alt_curve = np.array(alt_curve)
                        calculated_trajectory = True

                        az_start, alt_start = az_curve[0], alt_curve[0]
                        az_end, alt_end = az_curve[-1], alt_curve[-1]
                        peak_idx = int(np.argmax(alt_curve))
                        az_peak, alt_peak = az_curve[peak_idx], alt_curve[peak_idx]
            except (ValueError, KeyError, AttributeError, TypeError, RuntimeError) as e:
                logger.debug(f"Could not compute topocentric satellite trajectory: {e}")

    if not calculated_trajectory:
        az_start = center_az - 18.0
        alt_start = max(2.0, center_alt - 15.0)
        az_peak, alt_peak = center_az, center_alt
        az_end = center_az + 18.0
        alt_end = max(2.0, center_alt - 12.0)

        t_vals = np.linspace(0, 1, 100)
        az_curve = (1 - t_vals) ** 2 * az_start + 2 * (1 - t_vals) * t_vals * az_peak + t_vals ** 2 * az_end
        alt_curve = (1 - t_vals) ** 2 * alt_start + 2 * (1 - t_vals) * t_vals * alt_peak + t_vals ** 2 * alt_end

    ax.plot(az_curve, alt_curve, color=theme["target_primary"], linewidth=4.5, alpha=0.3, zorder=10)
    ax.plot(az_curve, alt_curve, color="#38BDF8", linestyle="-", linewidth=2.2, zorder=11)

    n_pts = len(az_curve)
    for frac in (0.3, 0.7):
        idx = int(frac * (n_pts - 1))
        if idx + 1 < n_pts:
            ax.annotate(
                "",
                xy=(az_curve[idx + 1], alt_curve[idx + 1]),
                xytext=(az_curve[idx], alt_curve[idx]),
                arrowprops={"arrowstyle": "->", "color": "#FACC15", "lw": 2},
                zorder=12,
            )

    ax.scatter([az_start, az_end], [alt_start, alt_end], s=40, color=theme["text_sub"], zorder=12)
    ax.text(az_start, alt_start - 1.5, "Rise", color=theme["text_sub"], fontsize=9, ha="center", zorder=12)
    ax.text(az_end, alt_end - 1.5, "Set", color=theme["text_sub"], fontsize=9, ha="center", zorder=12)

    ax.scatter(az_peak, alt_peak, s=160, color="#FACC15", edgecolors="#FFFFFF", linewidth=1.5, zorder=14)
    ax.scatter(az_peak, alt_peak, s=400, color="#FACC15", alpha=0.25, zorder=13)
    ax.text(az_peak, alt_peak + 1.8, f"{sat_name} Peak", color=theme["text_main"], fontsize=12, fontweight="bold", ha="center", zorder=15)


def _draw_meteor_shower_radiant(
    ax: plt.Axes,
    center_az: float,
    center_alt: float,
    event_obj: "Event",
    theme: dict,
):
    """Renders a meteor shower radiant point with radiating shooting star streaks."""
    shower_name = event_obj.objects[0] if event_obj.objects else "Meteor Shower"

    ax.scatter(center_az, center_alt, s=500, facecolors="none", edgecolors="#FACC15", linewidth=1.5, alpha=0.8, zorder=11)
    ax.scatter(center_az, center_alt, s=200, facecolors="none", edgecolors="#F87171", linewidth=1.2, alpha=0.9, zorder=12)
    ax.scatter(center_az, center_alt, s=50, color="#FACC15", zorder=13)

    angles = np.array([20, 65, 110, 155, 205, 245, 290, 335])
    np.random.seed(int(center_az * 10) % 1000)

    for angle_deg in angles:
        rad = np.radians(angle_deg)
        dist_start = np.random.uniform(2.5, 4.0)
        dist_len = np.random.uniform(5.0, 9.0)

        x0 = center_az + dist_start * np.cos(rad)
        y0 = center_alt + dist_start * np.sin(rad)
        x1 = center_az + (dist_start + dist_len) * np.cos(rad)
        y1 = center_alt + (dist_start + dist_len) * np.sin(rad)

        if y1 > 0.5:
            ax.plot([x0, x1], [y0, y1], color="#FDE047", linewidth=1.8, alpha=0.85, zorder=10)
            ax.plot([x0, x1], [y0, y1], color="#FFFFFF", linewidth=0.8, alpha=0.95, zorder=11)
            ax.scatter(x1, y1, s=15, color="#F87171", alpha=0.9, zorder=12)

    ax.text(center_az, center_alt + 2.2, f"{shower_name} Radiant", color=theme["text_main"], fontsize=12, fontweight="bold", ha="center", zorder=15)


def _draw_jovian_system(
    ax: plt.Axes,
    center_az: float,
    center_alt: float,
    event_obj: "Event",
    theme: dict,
):
    """Renders Jupiter with equatorial cloud bands, Galilean Moons, and optional GRS marker."""
    jup_disk = patches.Circle((center_az, center_alt), radius=1.0, facecolor="#EAB308", edgecolor="#FACC15", linewidth=1.2, zorder=12)
    ax.add_patch(jup_disk)

    band1 = patches.Rectangle((center_az - 0.95, center_alt + 0.25), 1.9, 0.25, facecolor="#9A3412", alpha=0.7, zorder=13)
    band2 = patches.Rectangle((center_az - 0.95, center_alt - 0.50), 1.9, 0.25, facecolor="#9A3412", alpha=0.7, zorder=13)
    ax.add_patch(band1)
    ax.add_patch(band2)

    title_lower = str(event_obj.title).lower()
    if "grs" in title_lower or "red spot" in title_lower:
        grs = patches.Ellipse((center_az + 0.35, center_alt - 0.38), width=0.45, height=0.3, facecolor="#DC2626", edgecolor="#991B1B", zorder=14)
        ax.add_patch(grs)

    moons_offsets = [(-3.2, "Io"), (-1.8, "Europa"), (2.2, "Ganymede"), (4.0, "Callisto")]
    for dx, m_name in moons_offsets:
        mx, my = center_az + dx, center_alt + (dx * 0.08)
        ax.scatter(mx, my, s=35, color="#F8FAFC", edgecolors="#38BDF8", linewidth=0.8, zorder=14)
        ax.text(mx, my - 1.2, m_name, color=theme["text_sub"], fontsize=8, ha="center", zorder=15)

    ax.text(center_az, center_alt + 1.8, "Jupiter", color=theme["text_main"], fontsize=12, fontweight="bold", ha="center", zorder=15)


def _draw_rocket_launch_trajectory(
    ax: plt.Axes,
    center_az: float,
    center_alt: float,
    event_obj: "Event",
    theme: dict,
):
    """Renders a rising rocket launch trajectory vector curving upward from the horizon."""
    az_start = center_az - 4.0
    az_apex, alt_apex = center_az, center_alt

    t_vals = np.linspace(0, 1, 80)
    az_curve = (1 - t_vals) * az_start + t_vals * az_apex
    alt_curve = (1 - (1 - t_vals) ** 2) * alt_apex

    ax.plot(az_curve, alt_curve, color="#F97316", linewidth=5.0, alpha=0.3, zorder=10)
    ax.plot(az_curve, alt_curve, color="#FACC15", linewidth=2.5, zorder=11)
    ax.plot(az_curve, alt_curve, color="#FFFFFF", linewidth=1.0, zorder=12)

    ax.scatter(az_apex, alt_apex, s=180, color="#EF4444", edgecolors="#FFFFFF", linewidth=1.5, zorder=14)
    ax.annotate(
        "",
        xy=(az_curve[-1], alt_curve[-1]),
        xytext=(az_curve[-5], alt_curve[-5]),
        arrowprops={"arrowstyle": "-|>", "color": "#FFFFFF", "lw": 2, "mutation_scale": 15},
        zorder=15,
    )

    title_txt = event_obj.title or "Space Launch"
    ax.text(az_apex, alt_apex + 2.0, title_txt, color=theme["text_main"], fontsize=12, fontweight="bold", ha="center", zorder=15)


def _draw_planet_alignment(
    ax: plt.Axes,
    all_positions: list[tuple[float, float]],
    event_obj: "Event",
    theme: dict,
):
    """Renders an ecliptic arc line connecting aligned planets in the sky."""
    main_objs = event_obj.objects or ["Planet 1", "Planet 2"]

    sorted_pairs = sorted(zip(all_positions, main_objs), key=lambda p: p[0][0])
    az_vals = [p[0][0] for p in sorted_pairs]
    alt_vals = [p[0][1] for p in sorted_pairs]

    if len(az_vals) >= 2:
        ax.plot(az_vals, alt_vals, color="#38BDF8", linestyle="--", linewidth=1.5, alpha=0.8, zorder=10)

    for (az, alt), name in sorted_pairs:
        ax.scatter(az, alt, s=120, color="#FACC15", edgecolors="#FFFFFF", linewidth=1.0, zorder=12)
        ax.text(az, alt + 1.4, str(name).title(), color=theme["text_main"], fontsize=10, fontweight="bold", ha="center", zorder=15)

    mid_az = np.mean(az_vals) if az_vals else 90.0
    max_alt = max(alt_vals) if alt_vals else 25.0
    ax.text(mid_az, max_alt + 3.0, "Planet Alignment Arc", color=theme["target_primary"], fontsize=11, fontweight="bold", ha="center", zorder=16)


def _draw_chart_time_note_banner(ax: plt.Axes, note_text: str | None, theme: dict):
    """Renders a prominent informational banner on top of the chart figure for time shift or warning notes."""
    if not note_text:
        return
    note_lower = str(note_text).lower()
    is_warning = any(w in note_lower for w in ("warning", "ostrzeżenie", "advertencia", "warnung", "aviso", "below", "poniżej", "debajo", "unter", "abaixo"))
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
