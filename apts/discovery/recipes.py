from enum import Enum
from typing import cast

from ..constants.strategies import DSOType, FilterStrategy


class ImagingRecipe(str, Enum):
    """
    Recommended camera and filter equipment setup for astrophotography targets.
    """

    OSC_RGB = "OSC_RGB"  # One-Shot Color / Mono camera with RGB/L filters
    OSC_DUALBAND = "OSC_DUALBAND"  # One-Shot Color with dual-band filter (e.g. Ha/OIII, L-eNhance)
    MONO_HA_OIII = "MONO_HA_OIII"  # Mono camera with Ha and OIII narrowband filters
    MONO_SHO = "MONO_SHO"  # Mono camera with SII, Ha, and OIII narrowband filters (Hubble Palette)


def get_imaging_recipe(
    dso_type: DSOType,
    moon_illumination: float = 0.0,
    bortle: float | None = None,
) -> ImagingRecipe:
    """
    Determines the recommended imaging recipe based on target DSO type,
    Moon illumination (0.0 to 1.0), and sky light pollution (Bortle scale 1 to 9).

    Base mapping:
    - GX, GC, OC, RN, SC, AST, DS, OTHER -> OSC_RGB
    - EN, DN -> OSC_DUALBAND
    - SNR -> MONO_HA_OIII (or MONO_SHO if bright Moon or high light pollution)
    - PN -> MONO_HA_OIII

    Contextual adjustments:
    - High Bortle (>= 5) or bright Moon (>= 0.5) shifts EN/DN to MONO_HA_OIII and SNR to MONO_SHO.
    """
    high_light_pollution = bortle is not None and bortle >= 5.0
    bright_moon = moon_illumination >= 0.5
    challenging_conditions = high_light_pollution or bright_moon

    if dso_type in (
        DSOType.GX,
        DSOType.GC,
        DSOType.OC,
        DSOType.RN,
        DSOType.SC,
        DSOType.AST,
        DSOType.DS,
        DSOType.OTHER,
    ):
        return ImagingRecipe.OSC_RGB

    if dso_type in (DSOType.EN, DSOType.DN):
        if challenging_conditions:
            return ImagingRecipe.MONO_HA_OIII
        return ImagingRecipe.OSC_DUALBAND

    if dso_type == DSOType.SNR:
        if challenging_conditions:
            return ImagingRecipe.MONO_SHO
        return ImagingRecipe.MONO_HA_OIII

    if dso_type == DSOType.PN:
        return ImagingRecipe.MONO_HA_OIII

    return ImagingRecipe.OSC_RGB


def get_recommended_strategy(
    dso_type: DSOType,
    moon_illumination: float = 0.0,
    bortle: float | None = None,
) -> FilterStrategy:
    """
    Determines the recommended FilterStrategy (BROADBAND or NARROWBAND)
    corresponding to the recommended imaging recipe.
    """
    recipe = get_imaging_recipe(
        dso_type, moon_illumination=moon_illumination, bortle=bortle
    )
    if recipe == ImagingRecipe.OSC_RGB:
        return cast(FilterStrategy, FilterStrategy.BROADBAND)
    return cast(FilterStrategy, FilterStrategy.NARROWBAND)
