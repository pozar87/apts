import pytest
from apts.opticalequipment.telescope.vendors.sky_watcher import Sky_watcherTelescope

def test_sky_watcher_starquest_90mc_specs():
    """
    Test that the Sky-Watcher Starquest-90MC specifications are correct.
    Verified via First Light Optics: https://www.firstlightoptics.com/telescopes-in-stock/sky-watcher-starquest-90mc-90mm-maksutov-cassegrain.html
    """
    telescope = Sky_watcherTelescope.Sky_Watcher_Starquest_90MC()

    assert telescope.get_vendor() == "Sky-Watcher Starquest-90MC"
    assert telescope.telescope_type.name == "MAKSUTOV_CASSEGRAIN"

    # Check physical specs
    assert telescope.aperture.to("mm").magnitude == pytest.approx(90.0)
    assert telescope.focal_length.to("mm").magnitude == pytest.approx(1250.0)
    assert telescope.central_obstruction.to("mm").magnitude == pytest.approx(29.0)
    assert telescope.mass.to("gram").magnitude == pytest.approx(1370.0)

    # Check connections
    from apts.utils import ConnectionType, Gender
    assert telescope.connection_type == ConnectionType.F_1_25
    assert telescope.connection_gender == Gender.FEMALE

def test_old_starquest_80mc_is_removed():
    """
    Ensure the hallucinated Sky_Watcher_Starquest_80MC is no longer in the database.
    """
    with pytest.raises(AttributeError):
        getattr(Sky_watcherTelescope, "Sky_Watcher_Starquest_80MC")

    assert "Sky_Watcher_Starquest_80MC" not in Sky_watcherTelescope._DATABASE
