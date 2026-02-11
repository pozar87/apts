import pytest
import numpy as np
from apts.opticalequipment.camera import Camera
from apts.opticalequipment.telescope import Telescope
from apts.constants import OpticalType, GraphConstants
from apts.equipment import Equipment
from apts.utils import ConnectionType

def test_camera_init():
    c = Camera(sensor_width=36, sensor_height=24, width=6000, height=4000, vendor="Canon")
    assert c.sensor_width.magnitude == 36
    assert c.sensor_height.magnitude == 24
    assert c.width == 6000
    assert c.height == 4000
    assert c.vendor == "Canon"
    assert c.connection_type == ConnectionType.T2

def test_camera_pixel_size():
    c = Camera(sensor_width=36, sensor_height=24, width=6000, height=4000)
    expected = np.sqrt(36**2 + 24**2) / np.sqrt(6000**2 + 4000**2)
    assert np.isclose(c.pixel_size().magnitude, expected)

def test_camera_fov():
    c = Camera(sensor_width=36, sensor_height=24, width=6000, height=4000)
    t = Telescope(aperture=150, focal_length=750)
    fov = c.field_of_view(t, 1, 1)
    assert np.isclose(fov.magnitude, 1.8336)

def test_camera_output_type():
    c = Camera(sensor_width=36, sensor_height=24, width=6000, height=4000)
    assert c.output_type() == OpticalType.IMAGE

def test_camera_register():
    eq = Equipment()
    c = Camera(sensor_width=36, sensor_height=24, width=6000, height=4000)
    c.register(eq)
    assert c.id() in eq.connection_garph.nodes()
    assert eq.connection_garph.has_edge(c.id(), GraphConstants.IMAGE_ID)

def test_camera_is_visual_output():
    c = Camera(sensor_width=36, sensor_height=24, width=6000, height=4000)
    assert not c.is_visual_output()

def test_camera_str():
    c = Camera(sensor_width=36, sensor_height=24, width=6000, height=4000, vendor="Canon")
    # Using format in the actual code results in 'Canon 36x24' or 'Canon 36.0x24.0' depending on value
    assert str(c) == "Canon 36x24" or str(c) == "Canon 36.0x24.0"
