import logging
import numpy
import pandas as pd
from matplotlib import pyplot
from typing import Optional

logger = logging.getLogger(__name__)

def get_brightness_color(magnitude: Optional[float]) -> str:
    """
    Calculates a grayscale color based on the magnitude of a celestial object.
    Dimmer objects get a color closer to the background.
    """
    if hasattr(magnitude, "magnitude"):
        magnitude = getattr(magnitude, "magnitude")  # type: ignore
    if magnitude is None or pd.isna(magnitude):
        return "none"

    # Normalize magnitude to a 0-1 range for color mapping
    # Typical naked-eye limit is 6. Faintest in catalogs can be ~15-20.
    # Let's cap the range for better visual differentiation.
    min_mag = 2.0  # Brightest objects
    max_mag = 12.0  # Faintest objects for fill variation

    norm_mag = (magnitude - min_mag) / (max_mag - min_mag)
    norm_mag = numpy.clip(norm_mag, 0, 1)

    # Invert the value, so brighter objects (lower mag) are lighter
    brightness = 1 - norm_mag

    # Blend the color with the background color to avoid pure white/black
    bg_color = pyplot.colormaps.get_cmap("gray")(0)
    fg_color = pyplot.colormaps.get_cmap("gray")(brightness)

    # Simple alpha blending: final_color = fg * alpha + bg * (1 - alpha)
    # We use brightness as a proxy for alpha here.
    final_color_val = fg_color[0] * brightness + bg_color[0] * (1 - brightness)
    final_color_val = numpy.clip(final_color_val, 0, 1)

    return str(final_color_val)


_style_initialized = False


def setup_plotting_style():
    """
    Initializes the Seaborn plotting style based on the configuration.
    """
    global _style_initialized
    if _style_initialized:
        return

    import seaborn as sns

    from apts.config import config

    allowed_styles = ["white", "dark", "whitegrid", "darkgrid", "ticks"]
    seaborn_style = config.get("style", "seaborn", fallback="whitegrid")
    if seaborn_style not in allowed_styles:
        logger.warning(
            f"Invalid seaborn style '{seaborn_style}' in config. Using default 'whitegrid'."
        )
        seaborn_style = "whitegrid"

    try:
        sns.set_style(seaborn_style)  # pyright: ignore
        logger.info(f"Seaborn style set to '{seaborn_style}'")
    except ValueError:
        # This is a fallback, in case of unexpected issues with seaborn
        logger.warning(
            f"Could not set seaborn style to '{seaborn_style}'. Using default 'whitegrid'."
        )
        sns.set_style("whitegrid")

    _style_initialized = True
