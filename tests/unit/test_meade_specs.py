import pytest
from apts.opticalequipment.telescope.vendors.meade import MeadeTelescope

@pytest.mark.parametrize("factory_method, expected_aperture, expected_focal, expected_mass, expected_co", [
    (MeadeTelescope.Meade_LX85_ACF_6, 152.4, 1524, 4490, 56),
    (MeadeTelescope.Meade_LX85_ACF_8, 203.2, 2032, 5760, 76),
    (MeadeTelescope.Meade_LX200_ACF_8, 203.2, 2032, 6350, 76),
    (MeadeTelescope.Meade_LX200_ACF_10, 254.0, 2540, 11790, 94),
    (MeadeTelescope.Meade_LX200_ACF_12, 304.8, 3048, 16330, 102),
    (MeadeTelescope.Meade_LX200_ACF_14, 355.6, 3556, 22680, 117),
    (MeadeTelescope.Meade_LX200_ACF_16, 406.4, 4064, 30390, 127),
    (MeadeTelescope.Meade_LX600_ACF_10, 254.0, 2032, 12250, 121),
    (MeadeTelescope.Meade_LX600_ACF_12, 304.8, 2438, 16780, 146),
    (MeadeTelescope.Meade_LX600_ACF_14, 355.6, 2845, 23130, 171),
])
def test_meade_telescope_specs(factory_method, expected_aperture, expected_focal, expected_mass, expected_co):
    """Verify Meade telescope hardware specifications against manufacturer data."""
    telescope = factory_method()

    assert telescope.aperture.magnitude == expected_aperture
    assert telescope.focal_length.magnitude == expected_focal
    assert telescope.mass.magnitude == expected_mass
    assert telescope.central_obstruction.magnitude == expected_co
    assert telescope.get_vendor().startswith("Meade")
    assert telescope.telescope_type.value == "catadioptric"
