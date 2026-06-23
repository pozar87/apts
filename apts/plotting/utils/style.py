import logging
import numpy
import pandas as pd
from typing import Union

logger = logging.getLogger(__name__)


def get_brightness_color(
    magnitude: Union[float, numpy.ndarray, pd.Series]
) -> Union[str, numpy.ndarray]:
    """
    Calculates a grayscale color based on the magnitude of a celestial object.
    Dimmer objects get a color closer to the background.

    Optimization: replaces slow matplotlib colormap lookups with vectorized math.
    """
    if hasattr(magnitude, "magnitude"):
        magnitude = getattr(magnitude, "magnitude")  # type: ignore

    if magnitude is None or (
        isinstance(magnitude, (float, int)) and numpy.isnan(magnitude)
    ):
        return "none"

    # Normalize magnitude to a 0-1 range for color mapping (2.0 to 12.0)
    # Optimization: pre-calculate constants.
    norm_mag = (numpy.asarray(magnitude) - 2.0) / 10.0
    norm_mag = numpy.clip(norm_mag, 0, 1)

    # Invert the value, so brighter objects (lower mag) are lighter
    brightness = 1.0 - norm_mag

    # Blend the color with the background color (0,0,0) to avoid pure white/black.
    # The original logic resulted in final_color = brightness * brightness.
    final_color_val = brightness * brightness

    if numpy.isscalar(final_color_val):
        return str(final_color_val)

    return final_color_val.astype(str)


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
