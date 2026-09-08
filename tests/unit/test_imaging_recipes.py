from apts.constants import DSOType, FilterStrategy
from apts.discovery.recipes import (
    ImagingRecipe,
    get_imaging_recipe,
    get_recommended_strategy,
)


def test_imaging_recipes_broadband_targets():
    broadband_types = [
        DSOType.GX,
        DSOType.GC,
        DSOType.OC,
        DSOType.RN,
        DSOType.SC,
        DSOType.AST,
        DSOType.DS,
        DSOType.OTHER,
    ]
    for dso_type in broadband_types:
        for moon in [0.0, 0.5, 1.0]:
            for bortle in [None, 3, 7]:
                assert get_imaging_recipe(dso_type, moon, bortle) == ImagingRecipe.OSC_RGB
                assert (
                    get_recommended_strategy(dso_type, moon, bortle)
                    == FilterStrategy.BROADBAND
                )


def test_imaging_recipes_emission_nebulas():
    # Under dark sky and low moon: OSC_DUALBAND
    assert get_imaging_recipe(DSOType.EN, 0.1, 3) == ImagingRecipe.OSC_DUALBAND
    assert (
        get_recommended_strategy(DSOType.EN, 0.1, 3) == FilterStrategy.NARROWBAND
    )

    # Under bright moon (>=0.5): MONO_HA_OIII
    assert get_imaging_recipe(DSOType.EN, 0.6, 3) == ImagingRecipe.MONO_HA_OIII
    assert (
        get_recommended_strategy(DSOType.EN, 0.6, 3) == FilterStrategy.NARROWBAND
    )

    # Under high Bortle (>=5): MONO_HA_OIII
    assert get_imaging_recipe(DSOType.EN, 0.1, 6) == ImagingRecipe.MONO_HA_OIII

    # Diffuse Nebula follows same rule
    assert get_imaging_recipe(DSOType.DN, 0.1, 3) == ImagingRecipe.OSC_DUALBAND
    assert get_imaging_recipe(DSOType.DN, 0.8, 2) == ImagingRecipe.MONO_HA_OIII


def test_imaging_recipes_snr():
    # Dark sky / low moon -> MONO_HA_OIII
    assert get_imaging_recipe(DSOType.SNR, 0.2, 3) == ImagingRecipe.MONO_HA_OIII
    assert (
        get_recommended_strategy(DSOType.SNR, 0.2, 3) == FilterStrategy.NARROWBAND
    )

    # Bright moon -> MONO_SHO
    assert get_imaging_recipe(DSOType.SNR, 0.7, 3) == ImagingRecipe.MONO_SHO

    # High Bortle -> MONO_SHO
    assert get_imaging_recipe(DSOType.SNR, 0.1, 5) == ImagingRecipe.MONO_SHO


def test_imaging_recipes_planetary_nebula():
    for moon in [0.0, 0.5, 1.0]:
        for bortle in [None, 1, 8]:
            assert get_imaging_recipe(DSOType.PN, moon, bortle) == ImagingRecipe.MONO_HA_OIII
            assert (
                get_recommended_strategy(DSOType.PN, moon, bortle)
                == FilterStrategy.NARROWBAND
            )
