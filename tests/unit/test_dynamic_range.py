import pytest
import numpy as np
from typing import Any, cast
from apts.opticalequipment.camera.base import Camera
from apts.opticalequipment.smart_telescope import SmartTelescope
from apts.opticalequipment.telescope.base import Telescope
from apts.optics import OpticalPath

def test_camera_dynamic_range():
    # Valid data: ZWO ASI2600MM Pro (Full well 50000, Read noise 1.0)
    camera = Camera(23.5, 15.7, 6248, 4176, full_well=50000, read_noise=1.0)
    dr = camera.dynamic_range()
    assert dr is not None
    assert dr == pytest.approx(np.log2(50000/1.0))

    # Missing full well
    camera_no_fw = Camera(23.5, 15.7, 6248, 4176, read_noise=1.0)
    assert camera_no_fw.dynamic_range() is None

    # Missing read noise
    camera_no_rn = Camera(23.5, 15.7, 6248, 4176, full_well=50000)
    assert camera_no_rn.dynamic_range() is None

    # Zero read noise
    camera_zero_rn = Camera(23.5, 15.7, 6248, 4176, full_well=50000, read_noise=0)
    assert camera_zero_rn.dynamic_range() is None

def test_smart_telescope_dynamic_range():
    # Valid data: Seestar S50 (Full well 12000, Read noise 1.0)
    st = SmartTelescope(50, 250, 5.6, 3.2, 1920, 1080, full_well=12000, read_noise=1.0)
    dr = st.dynamic_range()
    assert dr is not None
    assert dr == pytest.approx(np.log2(12000/1.0))

def test_optical_path_dynamic_range():
    telescope = Telescope(80, 480)
    camera = Camera(23.5, 15.7, 6248, 4176, full_well=50000, read_noise=1.0)
    path = OpticalPath(telescope, [], [], [], [], camera)

    assert path.dynamic_range() == camera.dynamic_range()

    # Non-camera output (e.g. Eyepiece)
    from apts.opticalequipment.eyepiece import Eyepiece
    eyepiece = Eyepiece(20, 50)
    path_visual = OpticalPath(telescope, [], [], [], [], eyepiece)
    assert path_visual.dynamic_range() is None
