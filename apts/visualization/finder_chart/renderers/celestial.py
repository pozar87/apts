import logging
from typing import TYPE_CHECKING

import matplotlib.pyplot as plt
import numpy as np
from matplotlib import patches

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
    ry = (
        radius_deg * (data_height / data_width) * (ax_width / ax_height)
        if data_width > 0 and ax_height > 0
        else radius_deg
    )

    dark_disk = patches.Ellipse(
        (x, y),
        width=2 * rx,
        height=2 * ry,
        facecolor=dark_color,
        edgecolor=theme["text_sub"],
        linewidth=0.8,
        zorder=10,
    )
    ax.add_patch(dark_disk)

    if phase_frac <= 0.02 or phase_frac >= 0.98:
        return

    if 0.48 <= phase_frac <= 0.52:
        bright_disk = patches.Ellipse(
            (x, y),
            width=2 * rx,
            height=2 * ry,
            facecolor=bright_color,
            edgecolor=None,
            zorder=11,
        )
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
    polygon = patches.Polygon(
        poly_pts, closed=True, facecolor=bright_color, edgecolor=None, zorder=11
    )
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
    ry = (
        radius_deg * (data_height / data_width) * (ax_width / ax_height)
        if data_width > 0 and ax_height > 0
        else radius_deg
    )

    glow_outer = patches.Ellipse(
        (x, y),
        width=3.2 * rx,
        height=3.2 * ry,
        facecolor="#FDE047",
        alpha=0.25,
        edgecolor=None,
        zorder=10,
    )
    ax.add_patch(glow_outer)

    glow_inner = patches.Ellipse(
        (x, y),
        width=2.2 * rx,
        height=2.2 * ry,
        facecolor="#FACC15",
        alpha=0.4,
        edgecolor=None,
        zorder=10,
    )
    ax.add_patch(glow_inner)

    sun_disk = patches.Ellipse(
        (x, y),
        width=2 * rx,
        height=2 * ry,
        facecolor="#F59E0B",
        edgecolor="#FEF08A",
        linewidth=1.2,
        zorder=11,
    )
    ax.add_patch(sun_disk)


def _draw_jovian_system(
    ax: plt.Axes,
    center_az: float,
    center_alt: float,
    event_obj: "Event",
    theme: dict,
):
    """Renders Jupiter with equatorial cloud bands, Galilean Moons, and optional GRS marker."""
    jup_disk = patches.Circle(
        (center_az, center_alt),
        radius=1.0,
        facecolor="#EAB308",
        edgecolor="#FACC15",
        linewidth=1.2,
        zorder=12,
    )
    ax.add_patch(jup_disk)

    band1 = patches.Rectangle(
        (center_az - 0.95, center_alt + 0.25),
        1.9,
        0.25,
        facecolor="#9A3412",
        alpha=0.7,
        zorder=13,
    )
    band2 = patches.Rectangle(
        (center_az - 0.95, center_alt - 0.50),
        1.9,
        0.25,
        facecolor="#9A3412",
        alpha=0.7,
        zorder=13,
    )
    ax.add_patch(band1)
    ax.add_patch(band2)

    title_lower = str(event_obj.title).lower()
    if "grs" in title_lower or "red spot" in title_lower:
        grs = patches.Ellipse(
            (center_az + 0.35, center_alt - 0.38),
            width=0.45,
            height=0.3,
            facecolor="#DC2626",
            edgecolor="#991B1B",
            zorder=14,
        )
        ax.add_patch(grs)

    moons_offsets = [
        (-3.2, "Io"),
        (-1.8, "Europa"),
        (2.2, "Ganymede"),
        (4.0, "Callisto"),
    ]
    for dx, m_name in moons_offsets:
        mx, my = center_az + dx, center_alt + (dx * 0.08)
        ax.scatter(
            mx,
            my,
            s=35,
            color="#F8FAFC",
            edgecolors="#38BDF8",
            linewidth=0.8,
            zorder=14,
        )
        ax.text(
            mx,
            my - 1.2,
            m_name,
            color=theme["text_sub"],
            fontsize=8,
            ha="center",
            zorder=15,
        )

    ax.text(
        center_az,
        center_alt + 1.8,
        "Jupiter",
        color=theme["text_main"],
        fontsize=12,
        fontweight="bold",
        ha="center",
        zorder=15,
    )
