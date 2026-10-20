from typing import TYPE_CHECKING

import matplotlib.pyplot as plt

from ..calculations import _get_event_moon_phase_frac
from ..renderers import _draw_moon_phase, _draw_sun_disk

if TYPE_CHECKING:
    from apts.events.event import Event


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
        _draw_moon_phase(
            ax, az, alt, radius_deg=0.9, phase_frac=phase_frac, theme=theme
        )
    elif is_sun:
        _draw_sun_disk(ax, az, alt, radius_deg=0.9, theme=theme)
    else:
        ax.scatter(
            az,
            alt,
            s=dot_size,
            color=theme[color_key],
            edgecolors=theme["star"],
            linewidth=1.0,
            zorder=12,
        )
        ax.scatter(
            az,
            alt,
            s=glow_size,
            color=theme[color_key],
            alpha=0.25,
            edgecolors="none",
            zorder=11,
        )

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

    moon_in_event = any(
        any(k in str(o).lower() for k in moon_kws) for o in main_objs
    ) or event_obj.category in (
        "OCCULTATION",
        "LUNAR_ECLIPSE",
        "MOON_PHASE",
        "SUPERMOON",
        "MOON_LIBRATION",
        "LUNAR_FEATURE",
    )
    obj1_is_moon = any(k in obj1_name.lower() for k in moon_kws) or (
        moon_in_event and obj1_name in ("Moon", "Księżyc", "Mond", "Luna", "Target")
    )

    sun_in_event = any(
        any(k in str(o).lower() for k in sun_kws) for o in main_objs
    ) or event_obj.category in ("EQUINOX_SOLSTICE", "SOLAR_ECLIPSE")
    obj1_is_sun = any(k in obj1_name.lower() for k in sun_kws) or (
        sun_in_event and obj1_name in ("Sun", "Słońce", "Sonne", "Sol", "Target")
    )

    _draw_single_object(
        ax,
        obj1_name,
        p1_az,
        p1_alt,
        obj1_is_moon,
        "target_primary",
        350,
        120,
        event_obj,
        theme,
        is_sun=obj1_is_sun,
    )

    if p2_pos is not None:
        p2_az, p2_alt = p2_pos
        obj2_name = main_objs[1] if len(main_objs) > 1 else "Companion"
        obj2_is_moon = any(k in obj2_name.lower() for k in moon_kws)
        obj2_is_sun = any(k in obj2_name.lower() for k in sun_kws)
        _draw_single_object(
            ax,
            obj2_name,
            p2_az,
            p2_alt,
            obj2_is_moon,
            "target_secondary",
            260,
            90,
            event_obj,
            theme,
            is_sun=obj2_is_sun,
        )

        # Separation indicator
        ax.plot(
            [p1_az, p2_az],
            [p1_alt, p2_alt],
            color=theme["separation_line"],
            linestyle="--",
            linewidth=1.2,
            alpha=0.85,
            zorder=13,
        )
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
