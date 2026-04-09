import pytest
from apts.optics import OpticalPath
from apts.opticalequipment.telescope.vendors.askar import AskarTelescope
from apts.opticalequipment.camera.vendors.zwo import ZwoCamera
from apts.opticalequipment.camera.vendors.qhy import QhyCamera

def test_atmospheric_dispersion_in_pixels():
    telescope = AskarTelescope.Askar_FRA300_Pro() # 300mm FL
    camera = ZwoCamera.ZWO_ASI_664MC() # 2.9um pixel size
    # Pixel scale: (2.9 / 300) * 206265 = 1.993895 arcsec/px

    path = OpticalPath.from_path([telescope, camera])

    # Benchmarks from Stellar's Journal: ~1.437" at 45° (400nm to 700nm)
    # Expected pixels = 1.437 / 1.993895 = 0.7207 pixels

    dispersion_px = path.atmospheric_dispersion_in_pixels(45, 400, 700)
    assert dispersion_px is not None
    assert pytest.approx(dispersion_px, abs=1e-3) == 0.7207

def test_askar_71f_specs():
    telescope = AskarTelescope.Askar_71F()
    assert telescope.aperture.magnitude == 71
    assert telescope.focal_length.magnitude == 490
    assert telescope.mass.magnitude == 2500
    assert telescope.get_vendor() == "Askar 71F"

def test_zwo_asi664mc_optical_length():
    camera = ZwoCamera.ZWO_ASI_664MC()
    # Corrected value should be 6.5
    assert camera.optical_length.magnitude == 6.5

def test_qhy_factory_refactor():
    # Verify they still return the correct models with expected properties
    m600m = QhyCamera.QHY_QHY_600M()
    assert m600m.get_vendor() == "QHY QHY 600M"
    assert m600m.sensor_width.magnitude == 36.0
    assert m600m.pixel_size().magnitude == 3.76

    c600c = QhyCamera.QHY_QHY_600C()
    assert c600c.get_vendor() == "QHY QHY 600C"
    assert c600c.quantum_efficiency == 91

    m268m = QhyCamera.QHY_QHY_268M()
    assert m268m.get_vendor() == "QHY QHY 268M"
    assert m268m.sensor_width.magnitude == 23.5

    c268c = QhyCamera.QHY_QHY_268C()
    assert c268c.get_vendor() == "QHY QHY 268C"
    assert c268c.sensor_height.magnitude == 15.7
