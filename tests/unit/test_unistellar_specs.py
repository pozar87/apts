from apts.opticalequipment.telescope.vendors.unistellar import UnistellarTelescope
from apts.opticalequipment.smart_telescope import SmartTelescope

def test_unistellar_evscope_specs():
    """
    Verify physical specifications for Unistellar eVscope (Legacy)
    """
    telescope = UnistellarTelescope.Unistellar_eVscope()
    assert isinstance(telescope, SmartTelescope)
    assert telescope.get_vendor() == "Unistellar eVscope"
    assert telescope.aperture.magnitude == 114
    assert telescope.focal_length.magnitude == 450
    assert telescope.pixel_size().magnitude == 3.75
    assert telescope.width == 1280
    assert telescope.height == 960
    # Sensor dimensions: 1280 * 0.00375 = 4.8mm, 960 * 0.00375 = 3.6mm
    assert telescope.sensor_width.magnitude == 4.8
    assert telescope.sensor_height.magnitude == 3.6

def test_unistellar_evscope_2_specs():
    """
    Verify physical specifications for Unistellar eVscope 2
    """
    telescope = UnistellarTelescope.Unistellar_eVscope_2()
    assert isinstance(telescope, SmartTelescope)
    assert telescope.get_vendor() == "Unistellar eVscope 2"
    assert telescope.aperture.magnitude == 114
    assert telescope.focal_length.magnitude == 450
    assert telescope.pixel_size().magnitude == 2.9
    assert telescope.width == 3200
    assert telescope.height == 2400
    assert telescope.sensor_width.magnitude == 9.28
    assert telescope.sensor_height.magnitude == 6.96

def test_unistellar_equinox_2_specs():
    """
    Verify physical specifications for Unistellar eQuinox 2
    """
    telescope = UnistellarTelescope.Unistellar_eQuinox_2()
    assert isinstance(telescope, SmartTelescope)
    assert telescope.get_vendor() == "Unistellar eQuinox 2"
    assert telescope.aperture.magnitude == 114
    assert telescope.focal_length.magnitude == 450
    assert telescope.pixel_size().magnitude == 2.9
    assert telescope.width == 3072
    assert telescope.height == 2048
    assert telescope.sensor_width.magnitude == 8.91
    assert telescope.sensor_height.magnitude == 5.94

def test_unistellar_odyssey_specs():
    """
    Verify physical specifications for Unistellar Odyssey series
    """
    telescope = UnistellarTelescope.Unistellar_Odyssey()
    assert isinstance(telescope, SmartTelescope)
    assert telescope.get_vendor() == "Unistellar Odyssey"
    assert telescope.aperture.magnitude == 85
    assert telescope.focal_length.magnitude == 320
    assert telescope.pixel_size().magnitude == 1.45
    assert telescope.width == 3088
    assert telescope.height == 2072
    assert telescope.sensor_width.magnitude == 4.48
    assert telescope.sensor_height.magnitude == 3.0
    assert telescope.mass.magnitude == 4000
