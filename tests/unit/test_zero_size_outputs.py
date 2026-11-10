"""Regression tests for zero-size optical outputs.

``calculate_zoom`` divides the telescope focal length by the output's
``_zoom_divider()`` (the sensor diagonal for cameras, the focal length for
eyepieces). Equipment rows with an unknown sensor size or a zero focal length
produced a divider of 0, which raised ``ZeroDivisionError`` deep inside
``apts.equipment.exporter`` and aborted the caller's whole observation.

Observed in stargazer.earth production as
``Error processing observation 593: division by zero`` coming from
``equipment/exporter.py`` -> ``optics/models/geometric.py`` -> ``compute_zoom``.
"""

import math

import pytest

from apts.opticalequipment.camera import Camera
from apts.opticalequipment.eyepiece import Eyepiece


class TestZeroSizeCamera:
    def _camera(self):
        return Camera(
            sensor_width=0,
            sensor_height=0,
            width=0,
            height=0,
            vendor="Test",
        )

    def test_zoom_divider_is_not_zero(self):
        assert self._camera()._zoom_divider().magnitude != 0

    def test_zoom_divider_is_infinite(self):
        assert math.isinf(self._camera()._zoom_divider().magnitude)


class TestZeroFocalLengthEyepiece:
    def _eyepiece(self):
        return Eyepiece(focal_length=0, vendor="Test")

    def test_zoom_divider_is_not_zero(self):
        assert self._eyepiece()._zoom_divider().magnitude != 0

    def test_zoom_divider_is_infinite(self):
        assert math.isinf(self._eyepiece()._zoom_divider().magnitude)


def test_camera_zoom_divider_matches_sensor_diagonal_for_valid_sensor():
    """A normal sensor still yields its real diagonal (no regression)."""
    camera = Camera(
        sensor_width=36,
        sensor_height=24,
        width=6000,
        height=4000,
        vendor="Test",
        pixel_size=5.9,
    )
    diagonal = camera._zoom_divider().to("mm").magnitude
    assert diagonal == pytest.approx(math.hypot(36, 24), rel=1e-6)
