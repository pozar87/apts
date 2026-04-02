import pytest
from apts.opticalequipment.telescope.vendors.ioptron import IoptronTelescope

@pytest.mark.parametrize("factory_method, expected_aperture, expected_focal, expected_mass, expected_co, expected_type", [
    (IoptronTelescope.iOptron_Photron_RC_6, 150, 1370, 5443, 67, "catadioptric"),
    (IoptronTelescope.iOptron_iOptron_RC_6, 150, 1370, 5443, 67, "catadioptric"), # Legacy
    (IoptronTelescope.iOptron_Photron_RC_8, 200, 1624, 8165, 95, "catadioptric"),
    (IoptronTelescope.iOptron_iOptron_RC_8, 200, 1624, 8165, 95, "catadioptric"), # Legacy
    (IoptronTelescope.iOptron_Photron_RC_10_Steel, 250, 2000, 15876, 110, "catadioptric"),
    (IoptronTelescope.iOptron_Photron_RC_10_Truss, 254, 2032, 15422, 110, "catadioptric"),
    (IoptronTelescope.iOptron_Photron_RC_12_Truss, 304, 2432, 24040, 150, "catadioptric"),
    (IoptronTelescope.iOptron_Photron_RC_16_Truss, 406, 3250, 42184, 171, "catadioptric"),
    (IoptronTelescope.iOptron_80mm_APO, 80, 480, 3100, 0, "refractor"),
    (IoptronTelescope.iOptron_iOptron_80mm_APO, 80, 480, 3100, 0, "refractor"), # Legacy
    (IoptronTelescope.iOptron_102mm_APO, 102, 714, 4500, 0, "refractor"),
    (IoptronTelescope.iOptron_iOptron_102mm_APO, 102, 714, 4500, 0, "refractor"), # Legacy
    (IoptronTelescope.iOptron_R80, 80, 400, 998, 0, "refractor"),
])
def test_ioptron_telescope_specs(factory_method, expected_aperture, expected_focal, expected_mass, expected_co, expected_type):
    """Verify iOptron telescope hardware specifications against manufacturer data."""
    telescope = factory_method()

    assert telescope.aperture.magnitude == expected_aperture
    assert telescope.focal_length.magnitude == expected_focal
    assert telescope.mass.magnitude == expected_mass
    assert telescope.central_obstruction.magnitude == expected_co
    assert telescope.get_vendor().startswith("iOptron")
    assert telescope.telescope_type.value == expected_type
