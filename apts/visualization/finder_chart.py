import io
import logging
import math
from datetime import timezone
from typing import TYPE_CHECKING, Any, Union

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


def _get_event_moon_phase_frac(event_obj: "Event") -> float:
    """Helper to determine float phase fraction (0.0-1.0) for Moon rendering."""
    p_val = getattr(event_obj, "extra_data", {}).get("phase")
    if isinstance(p_val, (int, float)):
        if float(p_val) > 1.0:
            return (float(p_val) % 360.0) / 360.0
        return float(p_val)

    title_lower = f"{event_obj.title} {event_obj.category} {p_val}".lower()
    if "first quarter" in title_lower or "pierwsza kwadra" in title_lower or "cuarto creciente" in title_lower or "erstes viertel" in title_lower or "primeiro quarto" in title_lower:
        return 0.25
    if "third quarter" in title_lower or "last quarter" in title_lower or "trzecia kwadra" in title_lower or "ostatnia kwadra" in title_lower or "cuarto menguante" in title_lower or "drittes viertel" in title_lower or "quarto minguante" in title_lower:
        return 0.75
    if "full moon" in title_lower or "pełnia" in title_lower or "luna llena" in title_lower or "vollmond" in title_lower or "lua cheia" in title_lower:
        return 0.5
    if "new moon" in title_lower or "nów" in title_lower or "luna nueva" in title_lower or "neumond" in title_lower or "lua nova" in title_lower:
        return 0.0

    return 0.25


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


def _get_satellite_name(event_obj: "Event") -> str:
    """Helper to derive clean satellite name (ISS, Tiangong, etc.) without generic fallback."""
    if event_obj.objects:
        obj_name = str(event_obj.objects[0])
        if obj_name and obj_name.lower() != "target":
            return obj_name

    title_lower = str(event_obj.title).lower()
    cat_lower = str(event_obj.category).lower()

    if "tiangong" in title_lower or "tiangong" in cat_lower or "css" in title_lower:
        return "Tiangong"
    if "iss" in title_lower or "iss" in cat_lower or "station" in title_lower:
        return "ISS"

    return "Satellite"


def _draw_satellite_flyby_trail(
    ax: plt.Axes,
    center_az: float,
    center_alt: float,
    event_obj: "Event",
    theme: dict,
):
    """Renders a satellite flyby trajectory trail across the sky with arrows and peak marker."""
    from datetime import timedelta

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


LONG_EVENT_CATEGORIES = {
    "CONJUNCTION",
    "PLANET_ALIGNMENT",
    "OPPOSITION",
    "CELESTIAL_CONFIGURATION",
    "MOON_PHASE",
    "SUPERMOON",
    "MOON_LIBRATION",
    "GREATEST_ELONGATION",
    "VENUS_GREAT_BRILLIANCY",
    "EQUINOX_SOLSTICE",
    "METEOR_SHOWER",
    "CELESTIAL_EVENT",
}


def is_long_event(category: str, title: str = "") -> bool:
    """Checks if an event category or title represents a multi-hour / long-duration event."""
    cat = str(category).upper()
    title_lower = str(title).lower()
    if cat in LONG_EVENT_CATEGORIES:
        return True
    long_keywords = [
        "conjunction",
        "alignment",
        "opposition",
        "elongation",
        "phase",
        "shower",
        "solstice",
        "equinox",
    ]
    return any(kw in title_lower for kw in long_keywords)


def _compute_sky_brightness_at_time(
    event_obj: "Event", observer: Any, ts_chart: Any
) -> str:
    """Computes topocentric sky brightness classification at a specific chart observation time."""
    from apts.cache import get_ephemeris
    from apts.events.event import get_sky_brightness

    try:
        eph = get_ephemeris()
        obs_at_c = observer.at(ts_chart)
        sun_alt = float(obs_at_c.observe(eph["sun"]).apparent().altaz()[0].degrees)
        moon_alt = float(obs_at_c.observe(eph["moon"]).apparent().altaz()[0].degrees)
        phase = (
            float(event_obj.extra_data.get("phase", 0.0))
            if isinstance(event_obj.extra_data.get("phase"), (int, float))
            else 0.0
        )
        return get_sky_brightness(sun_alt, moon_alt, phase)
    except (ValueError, KeyError, AttributeError, TypeError, RuntimeError):
        return getattr(event_obj, "sky_brightness", "NIGHT_DARK")


def _find_optimal_chart_time(
    event_obj: "Event",
    observer: Any,
    ts_time: Any,
    sf_obj1: Any | None,
) -> tuple[Any, float, str | None, str | None]:
    """
    Evaluates target altitude at peak time and searches for an optimal observation time
    when the target is at good altitude for long-lasting events.
    Returns (ts_chart, target_alt_chart, chart_datetime_utc, chart_time_note).
    """
    from datetime import timedelta

    from apts.i18n import gettext_

    dt_utc = event_obj.dt_utc

    alt_peak = 25.0
    if sf_obj1 is not None:
        try:
            app_peak = observer.at(ts_time).observe(sf_obj1).apparent()
            alt_o, _, _ = app_peak.altaz()
            alt_peak = float(alt_o.degrees)
        except (ValueError, KeyError, AttributeError, TypeError, RuntimeError):
            alt_peak = (
                float(event_obj.altitude_deg)
                if event_obj.altitude_deg is not None
                else 25.0
            )
    elif event_obj.altitude_deg is not None:
        alt_peak = float(event_obj.altitude_deg)

    if alt_peak < 0.0:
        event_obj.is_below_horizon = True

    if alt_peak >= 5.0:
        event_obj.target_altitude_deg = float(alt_peak)
        return ts_time, alt_peak, None, None

    # Target is below or near horizon (< 5.0 deg).
    if is_long_event(event_obj.category, event_obj.title) and sf_obj1 is not None:
        try:
            from apts.cache import get_ephemeris

            eph = get_ephemeris()
            sun = eph["sun"]

            best_ts = ts_time
            best_dt = dt_utc
            best_score = -999999.0
            best_alt = alt_peak

            ts_factory = getattr(ts_time, "ts", None) or getattr(
                getattr(event_obj, "place", None), "ts", None
            )

            offsets_hours = np.linspace(-12.0, 12.0, 97)
            for dh in offsets_hours:
                dt_cand = dt_utc + timedelta(hours=float(dh))
                if ts_factory is not None:
                    ts_c = ts_factory.utc(
                        dt_cand.year,
                        dt_cand.month,
                        dt_cand.day,
                        dt_cand.hour,
                        dt_cand.minute,
                        dt_cand.second,
                    )
                else:
                    ts_c = ts_time

                obs_c = observer.at(ts_c)
                alt_c = float(obs_c.observe(sf_obj1).apparent().altaz()[0].degrees)
                sun_alt_c = float(obs_c.observe(sun).apparent().altaz()[0].degrees)

                if alt_c < 0.0:
                    score = -1000.0 + alt_c
                else:
                    score = alt_c
                    if sun_alt_c < -0.833:
                        score += 100.0
                    score -= abs(dh) * 0.5

                if score > best_score:
                    best_score = score
                    best_ts = ts_c
                    best_dt = dt_cand
                    best_alt = alt_c

            if best_alt >= 5.0 or (alt_peak < 0.0 and best_alt > 0.0):
                chart_datetime_str = best_dt.strftime("%Y-%m-%dT%H:%M:%SZ")
                time_peak_str = dt_utc.strftime("%H:%M")
                time_chart_str = best_dt.strftime("%H:%M")
                alt_peak_fmt = f"{round(alt_peak, 1)}°"
                alt_chart_fmt = f"{round(best_alt, 1)}°"

                note = gettext_(
                    "Peak at {time_peak} UTC ({alt_peak}) is below horizon. Chart shown for {time_chart} UTC (Alt: {alt_chart})."
                ).format(
                    time_peak=time_peak_str,
                    alt_peak=alt_peak_fmt,
                    time_chart=time_chart_str,
                    alt_chart=alt_chart_fmt,
                )
                return best_ts, best_alt, chart_datetime_str, note
        except (ValueError, KeyError, AttributeError, TypeError, RuntimeError) as e:
            logger.debug(f"Failed to find optimal chart time: {e}")

    alt_peak_fmt = f"{round(alt_peak, 1)}°"
    warn_note = None
    if alt_peak < 0.0:
        warn_note = gettext_(
            "Warning: Target is below horizon ({alt_peak}) at event peak time."
        ).format(alt_peak=alt_peak_fmt)

    return ts_time, alt_peak, None, warn_note


def _resolve_skyfield_object(name_str: str) -> Any | None:
    """Attempts to resolve any string object name to a Skyfield object."""
    from skyfield.api import Star

    from apts.catalogs.messier import get_messier_raw
    from apts.catalogs.stars import get_bright_stars_raw
    from apts.utils import planetary

    if not name_str or not isinstance(name_str, str):
        return None

    clean = name_str.strip()
    clean_lower = clean.lower()

    # Common synonym mapping across languages
    synonyms = {
        "księżyc": "moon",
        "mond": "moon",
        "luna": "moon",
        "słońce": "sun",
        "sonne": "sun",
        "sol": "sun",
        "jowisz": "jupiter",
        "wenus": "venus",
        "mars": "mars",
        "saturn": "saturn",
        "merkury": "mercury",
        "merkur": "mercurio",
        "uran": "uranus",
        "neptun": "neptune",
    }
    lookup_name = synonyms.get(clean_lower, clean)

    # 1. Ephemeris (major / minor planets, Sun, Moon)
    try:
        return planetary.get_skyfield_obj(lookup_name)
    except (ValueError, KeyError, RuntimeError, AttributeError):
        pass

    # 2. Messier catalog
    try:
        messier_df = get_messier_raw()
        m_match = messier_df[
            messier_df["Messier"].str.lower() == clean_lower
        ]
        if m_match.empty:
            m_match = messier_df[
                messier_df["Messier"].str.lower() == f"m{clean_lower.replace('messier', '').strip()}"
            ]
        if not m_match.empty:
            row = m_match.iloc[0]
            return Star(ra_hours=float(row["ra_hours"]), dec_degrees=float(row["dec_degrees"]))
    except (ValueError, KeyError, RuntimeError, AttributeError):
        pass

    # 3. Bright stars catalog
    try:
        stars_df = get_bright_stars_raw()
        s_match = stars_df[stars_df["Name"].str.lower() == clean_lower]
        if not s_match.empty:
            row = s_match.iloc[0]
            st_obj = row.get("skyfield_object")
            if st_obj is not None:
                return st_obj
            return Star(ra_hours=float(row["ra_hours"]), dec_degrees=float(row["dec_degrees"]))
    except (ValueError, KeyError, RuntimeError, AttributeError):
        pass

    return None


def _get_observer_for_event(event_obj: "Event") -> tuple[Any, Any]:
    """Returns Skyfield observer object and Skyfield time for the event moment."""
    place = getattr(event_obj, "place", None)
    if place is not None and hasattr(place, "observer") and hasattr(place, "ts"):
        dt_utc = event_obj.dt_utc
        ts_time = place.ts.utc(dt_utc.year, dt_utc.month, dt_utc.day, dt_utc.hour, dt_utc.minute, dt_utc.second)
        return place.observer, ts_time

    # Default Topos observer if place is missing
    from skyfield.api import Topos

    from apts.cache import get_ephemeris, get_timescale

    ts = get_timescale()
    eph = get_ephemeris()
    dt_utc = event_obj.dt_utc
    ts_time = ts.utc(dt_utc.year, dt_utc.month, dt_utc.day, dt_utc.hour, dt_utc.minute, dt_utc.second)
    lat = float(getattr(event_obj, "extra_data", {}).get("lat", 52.2))
    lon = float(getattr(event_obj, "extra_data", {}).get("lon", 21.0))
    observer = eph["earth"] + Topos(latitude_degrees=lat, longitude_degrees=lon)
    return observer, ts_time


def _resolve_target_coordinates(
    event_obj: "Event",
    sep_deg: float,
) -> tuple[
    tuple[float, float],
    tuple[float, float] | None,
    list[tuple[float, float]],
    str,
]:
    """
    Calculates topocentric Az/Alt for target objects and evaluates optimal chart timing.
    Returns (p1_pos, p2_pos, all_object_positions, sky_brightness).
    """
    main_objs = event_obj.objects or []
    all_positions: list[tuple[float, float]] = []

    try:
        observer, ts_time = _get_observer_for_event(event_obj)
        sf_obj1 = _resolve_skyfield_object(str(main_objs[0])) if main_objs else None

        ts_chart, alt_chart, chart_dt_str, chart_note = _find_optimal_chart_time(
            event_obj, observer, ts_time, sf_obj1
        )

        event_obj.target_altitude_deg = float(alt_chart)
        if chart_dt_str:
            event_obj.chart_datetime_utc = chart_dt_str
        if chart_note:
            event_obj.chart_time_note = chart_note

        sky_brightness = _compute_sky_brightness_at_time(event_obj, observer, ts_chart)
        obs_at_chart = observer.at(ts_chart)

        for obj_name in main_objs:
            sf_obj = _resolve_skyfield_object(str(obj_name))
            if sf_obj is not None:
                app = obs_at_chart.observe(sf_obj).apparent()
                alt_o, az_o, _ = app.altaz()
                alt_v, az_v = float(alt_o.degrees), float(az_o.degrees)
                if not math.isnan(alt_v) and not math.isnan(az_v):
                    all_positions.append((az_v, alt_v))
    except (ValueError, KeyError, AttributeError, TypeError, RuntimeError) as e:
        logger.debug(f"Could not compute topocentric positions for target objects: {e}")
        sky_brightness = getattr(event_obj, "sky_brightness", "NIGHT_DARK")

    # Primary position priority:
    # 1. Computed topocentric position from primary object
    # 2. Event azimuth_deg / altitude_deg if explicitly provided
    # 3. Fallback default (90.0, 25.0)
    if all_positions:
        p1_pos = all_positions[0]
    elif event_obj.azimuth_deg is not None and event_obj.altitude_deg is not None:
        p1_pos = (float(event_obj.azimuth_deg), float(event_obj.altitude_deg))
    elif event_obj.azimuth_deg is not None:
        p1_pos = (float(event_obj.azimuth_deg), 25.0)
    else:
        p1_pos = (90.0, 25.0)

    # Clamp drawing altitude to >= 1.0 deg so no object is drawn below horizon
    p1_pos_draw = (p1_pos[0], max(1.0, p1_pos[1]))

    # Secondary position priority:
    if len(all_positions) >= 2:
        p2_pos = all_positions[1]
        p2_pos_draw = (p2_pos[0], max(1.0, p2_pos[1]))
    elif len(main_objs) >= 2 or event_obj.angular_separation:
        p2_pos = (p1_pos[0] + sep_deg * 0.8, p1_pos[1] + sep_deg * 0.6)
        p2_pos_draw = (p2_pos[0], max(1.0, p2_pos[1]))
    else:
        p2_pos_draw = None

    all_positions_draw = [(az, max(1.0, alt)) for az, alt in all_positions]

    return p1_pos_draw, p2_pos_draw, all_positions_draw, sky_brightness


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
