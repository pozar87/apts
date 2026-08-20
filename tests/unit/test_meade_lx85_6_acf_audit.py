import pytest
from apts.opticalequipment.telescope.vendors.meade import MeadeTelescope
from apts.opticalequipment.telescope.base import TelescopeType
from apts.utils import ConnectionType

def test_meade_lx85_6_acf_specs():
    """
    Audit test for Meade LX85 ACF 6" telescope based on official Meade / manufacturer documentation.
    Source: https://eu.levenhuk.com/catalogue/telescopes/meade-lx85-6-acf-ota/
    """
    scope = MeadeTelescope.Meade_LX85_ACF_6()

    # Vendor / Model Name
    assert scope.get_vendor() == "Meade LX85 ACF 6\""

    # Telescope Type
    assert scope.telescope_type == TelescopeType.CATADIOPTRIC

    # Mass: stored as a Pint Quantity in grams (5030g / 5.03kg OTA weight)
    assert scope.mass.to('gram').magnitude == 5030
    assert scope.mass.to('kg').magnitude == pytest.approx(5.03, abs=1e-3)

    # Aperture: 152.4mm
    assert scope.aperture.to('mm').magnitude == pytest.approx(152.4, abs=1e-3)

    # Focal length: 1524mm
    assert scope.focal_length.to('mm').magnitude == 1524

    # Focal ratio: f/10
    assert float(scope.focal_ratio().magnitude) == pytest.approx(10.0, abs=1e-3)

    # Central obstruction: 56mm
    assert scope.central_obstruction.to('mm').magnitude == 56

    # Connection type: SC (Schmidt-Cassegrain)
    assert scope.connection_type == ConnectionType.SC

if __name__ == "__main__":
    pytest.main([__file__])
