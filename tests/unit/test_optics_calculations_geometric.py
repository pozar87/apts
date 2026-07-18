import pytest
import numpy as np
from unittest.mock import MagicMock

from apts.optics.calculations.geometric import (
    barlows_multiplications,
    calculate_zoom,
    calculate_field_of_view,
    calculate_fov_ratio,
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
    from apts.opticalequipment.naked_eye import NakedEye
    from apts.opticalequipment.smart_telescope import SmartTelescope

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
