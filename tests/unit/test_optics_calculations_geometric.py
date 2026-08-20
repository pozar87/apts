import pytest
from unittest.mock import MagicMock

from apts.optics.calculations.geometric import (
    barlows_multiplications,
    calculate_zoom,
    calculate_field_of_view,
    calculate_fov_ratio,
    calculate_is_magnification_useful,
    calculate_brightness,
    calculate_exit_pupil,
)
from apts.units import get_unit_registry

ureg = get_unit_registry()


def test_barlows_multiplications():
    # Empty list should return 1.0
    assert barlows_multiplications([]) == 1.0

    # Mock barlow lenses
    barlow1 = MagicMock()
    barlow1.magnification = 2.0
    barlow2 = MagicMock()
    barlow2.magnification = 1.5

    assert barlows_multiplications([barlow1]) == 2.0
    assert barlows_multiplications([barlow1, barlow2]) == 3.0


def test_calculate_zoom_binoculars_etc():
    # Binoculars, NakedEye, or SmartTelescope have a magnification property
    mock_binoculars = MagicMock()
    mock_binoculars.magnification = 8.0

    # Using isinstance check with a dynamically subclassed mock or registering classes
    from apts.opticalequipment.binoculars import Binoculars

    # Create mock of Binoculars class
    class MyBinoculars(Binoculars):
        def __init__(self):
            pass

    binocs = MyBinoculars()
    binocs.magnification = 10.0

    zoom = calculate_zoom(binocs, [], None)
    assert zoom.magnitude == 10.0
    assert zoom.units == ureg.dimensionless


def test_calculate_zoom_telescope():
    mock_telescope = MagicMock()
    mock_telescope.focal_length = 1000 * ureg.mm

    mock_barlow = MagicMock()
    mock_barlow.magnification = 2.0

    mock_output = MagicMock()
    mock_output._zoom_divider.return_value = 10 * ureg.mm

    zoom = calculate_zoom(mock_telescope, [mock_barlow], mock_output)
    # 1000 * 2 / 10 = 200
    assert zoom.magnitude == 200.0


def test_calculate_field_of_view_binoculars_etc():
    from apts.opticalequipment.naked_eye import NakedEye

    class MyNakedEye(NakedEye):
        def __init__(self):
            pass

    eye = MyNakedEye()
    eye.fov = MagicMock(return_value=120 * ureg.deg)

    fov = calculate_field_of_view(eye, [], None)
    assert fov.magnitude == 120.0
    assert fov.units == ureg.deg


def test_calculate_field_of_view_telescope():
    mock_telescope = MagicMock()
    mock_telescope.focal_length = 1000 * ureg.mm

    mock_barlow = MagicMock()
    mock_barlow.magnification = 2.0

    mock_output = MagicMock()
    mock_output._zoom_divider.return_value = 10 * ureg.mm
    mock_output.field_of_view.return_value = 0.5 * ureg.deg

    fov = calculate_field_of_view(mock_telescope, [mock_barlow], mock_output)
    assert fov.magnitude == 0.5
    assert fov.units == ureg.deg


def test_calculate_fov_ratio_scalar():
    ratio = calculate_fov_ratio((60, 30), (22.2, 14.8), 750)
    assert ratio == pytest.approx(58.96, rel=1e-3)


def test_calculate_is_magnification_useful():
    from apts.opticalequipment.telescope import Telescope

    class MyTelescope(Telescope):
        def __init__(self):
            pass
        def lowest_useful_magnification(self):
            return 30.0
        def highest_useful_magnification(self):
            return 300.0

    telescope = MyTelescope()
    output_visual = MagicMock()
    output_visual.is_visual_output.return_value = True

    output_camera = MagicMock()
    output_camera.is_visual_output.return_value = False

    # Standard camera output (non-visual) -> True
    assert calculate_is_magnification_useful(telescope, output_camera, 10 * ureg.dimensionless) is True

    # Visual output in range -> True
    assert calculate_is_magnification_useful(telescope, output_visual, 100 * ureg.dimensionless) is True

    # Visual output below lowest -> False
    assert calculate_is_magnification_useful(telescope, output_visual, 20 * ureg.dimensionless) is False

    # Visual output above highest -> False
    assert calculate_is_magnification_useful(telescope, output_visual, 350 * ureg.dimensionless) is False

    # Non-telescope -> True
    assert calculate_is_magnification_useful(MagicMock(), output_visual, 100 * ureg.dimensionless) is True


def test_calculate_brightness():
    from apts.opticalequipment.naked_eye import NakedEye

    class MyNakedEye(NakedEye):
        def __init__(self):
            pass
        def brightness(self):
            return 75.0

    eye = MyNakedEye()
    f1 = MagicMock()
    f1.transmission = 0.8
    f2 = MagicMock()
    f2.transmission = 0.9

    # NakedEye with filters
    res = calculate_brightness(eye, None, None, [f1, f2])
    assert res.magnitude == pytest.approx(75.0 * 0.8 * 0.9)
    assert res.units == ureg.dimensionless

    # Standard telescope
    telescope = MagicMock()
    output = MagicMock()
    output.brightness.return_value = 50.0 * ureg.dimensionless

    res_tel = calculate_brightness(telescope, output, 100 * ureg.dimensionless, [f1])
    assert res_tel.magnitude == pytest.approx(50.0 * 0.8)


def test_calculate_exit_pupil():
    from apts.opticalequipment.naked_eye import NakedEye

    class MyNakedEye(NakedEye):
        def __init__(self):
            pass
        def exit_pupil(self):
            return 7.0 * ureg.mm

    eye = MyNakedEye()
    assert calculate_exit_pupil(eye, None) == 7.0 * ureg.mm

    # Telescope exit pupil zoom != 0
    telescope = MagicMock()
    telescope.aperture = 200 * ureg.mm
    assert calculate_exit_pupil(telescope, 50 * ureg.dimensionless) == 4.0 * ureg.mm

    # Telescope exit pupil zoom == 0
    assert calculate_exit_pupil(telescope, 0 * ureg.dimensionless) == 0 * ureg.mm
