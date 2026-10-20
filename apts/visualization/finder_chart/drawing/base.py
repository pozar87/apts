import matplotlib.pyplot as plt
import numpy as np

from ..calculations import (
    _get_compass_labels,
    _hex_to_rgb,
)
from ..constants import SKY_GRADIENT_COLORS


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
