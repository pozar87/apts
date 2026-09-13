import io
import logging
from typing import TYPE_CHECKING, Union

import matplotlib.pyplot as plt

from .calculations import (
    _parse_separation_deg,
    _resolve_target_coordinates,
)
from .constants import THEMES
from .drawing import (
    _draw_chart_time_note_banner,
    _draw_jovian_system,
    _draw_meteor_shower_radiant,
    _draw_planet_alignment,
    _draw_rocket_launch_trajectory,
    _draw_satellite_flyby_trail,
    _plot_background_stars,
    _plot_primary_event_objects,
    _setup_chart_axes_and_horizon,
)

if TYPE_CHECKING:
    from matplotlib.figure import Figure

    from apts.events.event import Event

logger = logging.getLogger(__name__)


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
    v_fov = h_fov * (
        figsize[1] / figsize[0] if len(figsize) >= 2 and figsize[0] > 0 else 0.8
    )

    az_min, az_max = center_az - h_fov / 2.0, center_az + h_fov / 2.0
    alt_min, alt_max = -5.0, max(center_alt + v_fov / 1.5, 30.0)

    fig, ax = plt.subplots(figsize=figsize, dpi=dpi)
    fig.patch.set_facecolor(t_theme["sky_bg"])
    ax.set_facecolor(t_theme["sky_bg"])

    _setup_chart_axes_and_horizon(
        ax, az_min, az_max, alt_min, alt_max, sky_brightness, t_theme
    )
    _draw_chart_time_note_banner(
        ax, getattr(event_obj, "chart_time_note", None), t_theme
    )

    if (
        cat_upper in ("FLYBY", "ISS_FLYBY", "TIANGONG_FLYBY")
        or "flyby" in title_lower
        or "iss" in title_lower
        or "tiangong" in title_lower
    ):
        _draw_satellite_flyby_trail(ax, center_az, center_alt, event_obj, t_theme)
    elif (
        cat_upper == "METEOR_SHOWER"
        or "shower" in title_lower
        or "meteor" in title_lower
    ):
        _draw_meteor_shower_radiant(ax, center_az, center_alt, event_obj, t_theme)
    elif (
        cat_upper in ("ROCKET_LAUNCH", "SPACE_LAUNCH")
        or "launch" in title_lower
        or "rocket" in title_lower
    ):
        _draw_rocket_launch_trajectory(ax, center_az, center_alt, event_obj, t_theme)
    elif (
        cat_upper in ("PLANET_ALIGNMENT", "CELESTIAL_CONFIGURATION")
        or "alignment" in title_lower
    ) and len(all_target_positions) >= 2:
        _draw_planet_alignment(ax, all_target_positions, event_obj, t_theme)
    elif (
        "jovian" in cat_upper.lower()
        or "jovian" in title_lower
        or "grs" in title_lower
        or ("jupiter" in title_lower and ("moon" in title_lower or "transit" in title_lower))
    ):
        _draw_jovian_system(ax, center_az, center_alt, event_obj, t_theme)
    else:
        _plot_primary_event_objects(ax, event_obj, p1_pos, p2_pos, sep_deg, t_theme)

    _plot_background_stars(
        ax, az_min, az_max, alt_max, center_az, center_alt, p1_pos, p2_pos, event_obj, t_theme
    )

    plt.subplots_adjust(left=0, right=1, bottom=0, top=1)

    if format is None or str(format).lower() in ("figure", "fig"):
        return fig

    fmt_clean = str(format).lower()
    buf = io.BytesIO()

    if fmt_clean == "svg":
        fig.savefig(
            buf,
            format="svg",
            facecolor=fig.get_facecolor(),
            bbox_inches="tight",
            pad_inches=0,
        )
        plt.close(fig)
        return buf.getvalue().decode("utf-8")
    else:
        fig.savefig(
            buf,
            format="png",
            dpi=dpi,
            facecolor=fig.get_facecolor(),
            bbox_inches="tight",
            pad_inches=0,
        )
        plt.close(fig)
        return buf.getvalue()


# Alias for APTS plotting API consistency
plot_finder_chart = generate_finder_chart
