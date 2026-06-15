import io
from matplotlib import pyplot as plt
from ...i18n import gettext_

def generate_alignment_map(correction, dark_mode=True):
    """
    Generates a visual guide showing the star, RA axis, and the required correction.
    """
    if correction is None:
        return None

    # Create plot
    fig, ax = plt.subplots(figsize=(8, 8))

    bg_color = "#1e1e1e" if dark_mode else "#ffffff"
    text_color = "#ffffff" if dark_mode else "#000000"
    fig.patch.set_facecolor(bg_color)
    ax.set_facecolor(bg_color)

    # Plot star position
    star = correction["star_image"]
    ax.scatter(
        star[0],
        star[1],
        c="yellow",
        s=100,
        label=gettext_("Target Star"),
        edgecolors="white",
        zorder=5,
    )

    # Plot mount RA axis
    axis = correction["mount_axis_image"]
    ax.scatter(
        axis[0], axis[1], c="red", marker="x", s=100, label=gettext_("Mount RA Axis"), zorder=5
    )

    # Plot target NCP position
    ncp = correction["ncp_image"]
    ax.scatter(
        ncp[0],
        ncp[1],
        c="cyan",
        marker="+",
        s=100,
        label=gettext_("Target NCP Position"),
        zorder=5,
    )

    # Draw correction vector
    ax.arrow(
        axis[0],
        axis[1],
        ncp[0] - axis[0],
        ncp[1] - axis[1],
        color="green",
        width=2,
        head_width=10,
        length_includes_head=True,
        label=gettext_("Correction Vector"),
        zorder=4,
    )

    # Axis labels and title
    ax.set_title(
        gettext_("Polar Alignment Guide - Error: {error:.1f}'").format(
            error=correction['error_arcmin']
        ),
        color=text_color,
    )
    ax.set_xlabel(gettext_("Pixel X"), color=text_color)
    ax.set_ylabel(gettext_("Pixel Y"), color=text_color)
    ax.tick_params(colors=text_color)

    # Legend
    ax.legend(facecolor=bg_color, labelcolor=text_color)

    # Reverse Y axis because image coordinates usually start from top
    ax.invert_yaxis()

    # Grid
    ax.grid(True, linestyle="--", alpha=0.3)

    # Output to bytes
    buf = io.BytesIO()
    plt.savefig(buf, format="png", bbox_inches="tight", facecolor=bg_color)
    plt.close(fig)
    buf.seek(0)
    return buf
