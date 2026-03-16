import pytest
import math
from apts.opticalequipment.camera.vendors.zwo import ZwoCamera
from apts.opticalequipment.smart_telescope import SmartTelescope
from apts.optics import OpticalPath
from apts.opticalequipment.telescope.vendors.sky_watcher import Sky_watcherTelescope

def test_camera_dynamic_range():
    # ASI2600MC Pro: 50,000e- full well, 1.0e- read noise
    # Checking existing factory method name
    cam = ZwoCamera.ZWO_ASI_2600MC_Pro()
    dr = cam.dynamic_range()
    assert dr is not None
    assert pytest.approx(dr, 0.1) == math.log2(50000 / 1.0)
    assert dr > 15.0

def test_camera_dynamic_range_missing_data():
    # Model with missing data (using heuristics or partial data)
    cam = ZwoCamera(23.5, 15.7, 6000, 4000)
    assert cam.dynamic_range() is None

def test_smart_telescope_dynamic_range():
    # Assuming a smart telescope with some values
    st = SmartTelescope(50, 250, 5.6, 3.2, 1920, 1080, full_well=12000, read_noise=0.5)
    dr = st.dynamic_range()
    assert dr is not None
    assert pytest.approx(dr, 0.1) == math.log2(12000 / 0.5)

def test_optical_path_dynamic_range_delegation():
    telescope = Sky_watcherTelescope.Sky_Watcher_Explorer_150P()
    camera = ZwoCamera.ZWO_ASI_2600MC_Pro()
    path = OpticalPath.from_path([telescope, camera])

    assert path.dynamic_range() == camera.dynamic_range()

def test_zwo_cooled_backfocus_consistency():
    # Pro models should be 17.5mm
    models_to_check = [
        ZwoCamera.ZWO_ASI_2600MC_Pro(),
        ZwoCamera.ZWO_ASI_533MC_Pro(),
        ZwoCamera.ZWO_ASI_183MM_Pro(),
        ZwoCamera.ZWO_ASI_6200MM_Pro()
    ]

    for cam in models_to_check:
        # backfocus and optical_length should be 17.5
        assert cam.backfocus.to("mm").magnitude == 17.5
        assert cam.optical_length.to("mm").magnitude == 17.5

def test_zwo_uncooled_backfocus_remains_short():
    # Standard planetary (uncooled) are usually 12.5mm (CS mount) or 6.5mm
    cam = ZwoCamera.ZWO_ASI_224MC()
    # ASI224MC in _DATABASE has 12.5mm optical_length
    assert cam.optical_length.to("mm").magnitude == 12.5
