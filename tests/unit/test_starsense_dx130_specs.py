from apts.opticalequipment.telescope.vendors.celestron import CelestronTelescope
from apts.opticalequipment.telescope.base import TelescopeType

def test_starsense_dx130_specs():
    """
    Verify physical specifications for Celestron StarSense Explorer DX 130
    against official manufacturer data.
    Source: https://www.celestron.com/products/starsense-explorer-dx-130az
    """
    telescope = CelestronTelescope.Celestron_StarSense_Explorer_DX_130()

    # Combined vendor string
    assert telescope.get_vendor() == "Celestron StarSense Explorer DX 130"

    # Telescope Type
    assert telescope.telescope_type == TelescopeType.NEWTONIAN_REFLECTOR

    # Physical specs (magnitudes of Pint Quantities)
    assert telescope.aperture.magnitude == 130
    assert telescope.focal_length.magnitude == 650
    assert telescope.central_obstruction.magnitude == 45
    assert telescope.mass.magnitude == 3990  # grams

    # Derived focal ratio check: 650 / 130 = 5.0
    # focal_ratio() returns a Pint Quantity (dimensionless)
    assert telescope.focal_ratio().magnitude == 5.0
