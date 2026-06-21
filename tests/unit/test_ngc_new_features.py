
import pytest
from datetime import datetime, timezone
from apts.place import Place
from apts.equipment.base import Equipment
from apts.observations.base import Observation
from apts.conditions import Conditions
from apts.opticalequipment.telescope.vendors.sky_watcher import Sky_watcherTelescope
from apts.opticalequipment.camera.vendors.zwo import ZwoCamera

@pytest.fixture
def observation():
    place = Place(50.0647, 19.9450, "Krakow", 200)
    telescope = Sky_watcherTelescope.Sky_Watcher_Explorer_150P()
    camera = ZwoCamera.ZWO_ASI_178MM()
    equipment = Equipment()
    equipment.add_vertex("Telescope", telescope)
    equipment.add_vertex("Camera", camera)
    equipment.add_edge("Space", "Telescope")
    equipment.add_edge("Telescope", "Camera")
    conditions = Conditions()
    target_date = datetime(2025, 5, 20, 22, 0, 0, tzinfo=timezone.utc)
    return Observation(place, equipment, conditions, target_date=target_date)

def test_ngc_support(observation):
    # Test table support
    ngc_df = observation.get_visible_ngc()
    assert ngc_df is not None

    # Test that M column exists and objects with it can be excluded
    # NGC 224 is M31. Let's check if it's in the full list but not in the excluded list.
    full_ngc = observation.get_visible_ngc(exclude_messier=False)
    # We need to find NGC 224 index. In our catalog it's 'NGC0224'
    m31_ngc = full_ngc[full_ngc['NGC'] == '0224']
    if not m31_ngc.empty:
        # It should NOT be in the default list
        default_ngc = observation.get_visible_ngc(exclude_messier=True)
        assert '0224' not in default_ngc['NGC'].values

def test_ngc_plotting(observation):
    import matplotlib.pyplot as plt
    # Test that plot_ngc doesn't crash
    fig = observation.plot_ngc()
    assert fig is not None
    plt.close(fig)

def test_html_export(observation):
    html = observation.to_html()
    assert "NGC/IC" in html
    assert "ngc_table" not in html # Should be substituted
    assert "Number of visiable objects" in html
    assert "NGC:" in html
