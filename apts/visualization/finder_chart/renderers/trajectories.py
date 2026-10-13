import logging
from datetime import timedelta
from typing import TYPE_CHECKING

import matplotlib.pyplot as plt
import numpy as np

from ..calculations import _get_satellite_name

if TYPE_CHECKING:
    from apts.events.event import Event

logger = logging.getLogger(__name__)


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
        tle_sat_name = (
            "ISS (ZARYA)"
            if "iss" in sat_name.lower()
            else "CSS (TIANHE)"
            if "tiangong" in sat_name.lower() or "china" in sat_name.lower()
            else None
        )
        if tle_sat_name:
            try:
                sat = _load_satellite(tle_sat_name)
                if sat is not None:
                    dt_peak = event_obj.dt_utc
                    ts_times = [
                        place.ts.utc(
                            (dt_peak + timedelta(seconds=sec)).year,
                            (dt_peak + timedelta(seconds=sec)).month,
                            (dt_peak + timedelta(seconds=sec)).day,
                            (dt_peak + timedelta(seconds=sec)).hour,
                            (dt_peak + timedelta(seconds=sec)).minute,
                            (dt_peak + timedelta(seconds=sec)).second,
                        )
                        for sec in range(-240, 241, 10)
                    ]
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
            except (
                ValueError,
                KeyError,
                AttributeError,
                TypeError,
                RuntimeError,
            ) as e:
                logger.debug(f"Could not compute topocentric satellite trajectory: {e}")

    if not calculated_trajectory:
        az_start = center_az - 18.0
        alt_start = max(2.0, center_alt - 15.0)
        az_peak, alt_peak = center_az, center_alt
        az_end = center_az + 18.0
        alt_end = max(2.0, center_alt - 12.0)

        t_vals = np.linspace(0, 1, 100)
        az_curve = (
            (1 - t_vals) ** 2 * az_start
            + 2 * (1 - t_vals) * t_vals * az_peak
            + t_vals**2 * az_end
        )
        alt_curve = (
            (1 - t_vals) ** 2 * alt_start
            + 2 * (1 - t_vals) * t_vals * alt_peak
            + t_vals**2 * alt_end
        )

    ax.plot(
        az_curve,
        alt_curve,
        color=theme["target_primary"],
        linewidth=4.5,
        alpha=0.3,
        zorder=10,
    )
    ax.plot(
        az_curve, alt_curve, color="#38BDF8", linestyle="-", linewidth=2.2, zorder=11
    )

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

    ax.scatter(
        [az_start, az_end],
        [alt_start, alt_end],
        s=40,
        color=theme["text_sub"],
        zorder=12,
    )
    ax.text(
        az_start,
        alt_start - 1.5,
        "Rise",
        color=theme["text_sub"],
        fontsize=9,
        ha="center",
        zorder=12,
    )
    ax.text(
        az_end,
        alt_end - 1.5,
        "Set",
        color=theme["text_sub"],
        fontsize=9,
        ha="center",
        zorder=12,
    )

    ax.scatter(
        az_peak,
        alt_peak,
        s=160,
        color="#FACC15",
        edgecolors="#FFFFFF",
        linewidth=1.5,
        zorder=14,
    )
    ax.scatter(az_peak, alt_peak, s=400, color="#FACC15", alpha=0.25, zorder=13)
    ax.text(
        az_peak,
        alt_peak + 1.8,
        f"{sat_name} Peak",
        color=theme["text_main"],
        fontsize=12,
        fontweight="bold",
        ha="center",
        zorder=15,
    )


def _draw_meteor_shower_radiant(
    ax: plt.Axes,
    center_az: float,
    center_alt: float,
    event_obj: "Event",
    theme: dict,
):
    """Renders a meteor shower radiant point with radiating shooting star streaks."""
    shower_name = event_obj.objects[0] if event_obj.objects else "Meteor Shower"

    ax.scatter(
        center_az,
        center_alt,
        s=500,
        facecolors="none",
        edgecolors="#FACC15",
        linewidth=1.5,
        alpha=0.8,
        zorder=11,
    )
    ax.scatter(
        center_az,
        center_alt,
        s=200,
        facecolors="none",
        edgecolors="#F87171",
        linewidth=1.2,
        alpha=0.9,
        zorder=12,
    )
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
            ax.plot(
                [x0, x1],
                [y0, y1],
                color="#FDE047",
                linewidth=1.8,
                alpha=0.85,
                zorder=10,
            )
            ax.plot(
                [x0, x1],
                [y0, y1],
                color="#FFFFFF",
                linewidth=0.8,
                alpha=0.95,
                zorder=11,
            )
            ax.scatter(x1, y1, s=15, color="#F87171", alpha=0.9, zorder=12)

    ax.text(
        center_az,
        center_alt + 2.2,
        f"{shower_name} Radiant",
        color=theme["text_main"],
        fontsize=12,
        fontweight="bold",
        ha="center",
        zorder=15,
    )


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

    ax.scatter(
        az_apex,
        alt_apex,
        s=180,
        color="#EF4444",
        edgecolors="#FFFFFF",
        linewidth=1.5,
        zorder=14,
    )
    ax.annotate(
        "",
        xy=(az_curve[-1], alt_curve[-1]),
        xytext=(az_curve[-5], alt_curve[-5]),
        arrowprops={
            "arrowstyle": "-|>",
            "color": "#FFFFFF",
            "lw": 2,
            "mutation_scale": 15,
        },
        zorder=15,
    )

    title_txt = event_obj.title or "Space Launch"
    ax.text(
        az_apex,
        alt_apex + 2.0,
        title_txt,
        color=theme["text_main"],
        fontsize=12,
        fontweight="bold",
        ha="center",
        zorder=15,
    )


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
        ax.plot(
            az_vals,
            alt_vals,
            color="#38BDF8",
            linestyle="--",
            linewidth=1.5,
            alpha=0.8,
            zorder=10,
        )

    for (az, alt), name in sorted_pairs:
        ax.scatter(
            az,
            alt,
            s=120,
            color="#FACC15",
            edgecolors="#FFFFFF",
            linewidth=1.0,
            zorder=12,
        )
        ax.text(
            az,
            alt + 1.4,
            str(name).title(),
            color=theme["text_main"],
            fontsize=10,
            fontweight="bold",
            ha="center",
            zorder=15,
        )

    mid_az = np.mean(az_vals) if az_vals else 90.0
    max_alt = max(alt_vals) if alt_vals else 25.0
    ax.text(
        mid_az,
        max_alt + 3.0,
        "Planet Alignment Arc",
        color=theme["target_primary"],
        fontsize=11,
        fontweight="bold",
        ha="center",
        zorder=16,
    )
