import numpy as np
from typing import Any, cast

from apts.constants import GraphConstants, OpticalType
from apts.equipment import Equipment
from apts.opticalequipment.camera import Camera
from apts.opticalequipment.telescope import Telescope
from apts.utils import ConnectionType


def test_camera_init():
    c = Camera(
        sensor_width=36, sensor_height=24, width=6000, height=4000, vendor="Canon"
    )
    assert c.sensor_width.magnitude == 36
    assert c.sensor_height.magnitude == 24
    assert c.width == 6000
    assert c.height == 4000
    assert c.vendor == "Canon"
    assert c.connection_type == ConnectionType.T2


def test_camera_pixel_size():
    c = Camera(sensor_width=36, sensor_height=24, width=6000, height=4000)
    expected = np.sqrt(36**2 + 24**2) / np.sqrt(6000**2 + 4000**2)
    assert np.isclose(cast(Any, c.pixel_size()).magnitude, expected)


def test_camera_fov():
    c = Camera(sensor_width=36, sensor_height=24, width=6000, height=4000)
    t = Telescope(aperture=150, focal_length=750)
    fov = c.field_of_view(t, 1, 1)
    # Accurate formula: 2 * atan(24 / (2 * 750)) = 1.8333...
    assert np.isclose(cast(Any, fov).magnitude, 1.8333085)


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
    c = Camera(
        sensor_width=36, sensor_height=24, width=6000, height=4000, vendor="Canon"
    )
    # Using format in the actual code results in 'Canon 36x24' or 'Canon 36.0x24.0' depending on value
    assert str(c) == "Canon 36x24" or str(c) == "Canon 36.0x24.0"


def test_factory_zwo_2600():
    cam = Camera.ZWO_ASI2600MC_PRO()
    assert cam.vendor == "ZWO ASI2600MC Pro"
    assert cam.pixel_size().to("micrometer").magnitude == 3.76
    assert cam.quantum_efficiency == 80
    assert cam.sensor_width.to("mm").magnitude == 23.5
    assert cam.sensor_height.to("mm").magnitude == 15.7


def test_factory_zwo_1600():
    cam = Camera.ZWO_ASI1600MM_PRO()
    assert cam.vendor == "ZWO ASI1600MM Pro"
    assert cam.pixel_size().to("micrometer").magnitude == 3.8
    assert cam.quantum_efficiency == 60


def test_factory_nikon_d850():
    cam = Camera.Nikon_D850()
    assert cam.vendor == "Nikon D850"
    assert cam.pixel_size().to("micrometer").magnitude == 4.35
    assert cam.quantum_efficiency == 54
    assert cam.sensor_width.to("mm").magnitude == 35.9
    assert cam.sensor_height.to("mm").magnitude == 23.9
