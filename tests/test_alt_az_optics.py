import numpy
from typing import Any, cast
import pytest
from apts.opticalequipment.camera import Camera
from apts.opticalequipment.telescope import Telescope
from apts.optics import OpticalPath

def test_field_rotation_rate_equator():
    t = Telescope(aperture=150, focal_length=750)
    c = Camera(36, 24, 6000, 4000, pixel_size=3.76)
    path = OpticalPath(t, [], [], [], [], c)

    # At the equator (phi=0), looking North (Az=0) at the horizon (Alt=0)
    # R = 15.041 * cos(0) * cos(0) / cos(0) = 15.041 deg/hr
    rate = path.field_rotation_rate(altitude_degrees=0, azimuth_degrees=0, latitude_degrees=0)
    assert numpy.isclose(cast(Any, rate).to("degree/hour").magnitude, 15.041, atol=0.001)

    # At the equator (phi=0), looking East (Az=90) at the horizon (Alt=0)
    # R = 15.041 * cos(0) * cos(90) / cos(0) = 0 deg/hr
    rate = path.field_rotation_rate(altitude_degrees=0, azimuth_degrees=90, latitude_degrees=0)
    assert numpy.isclose(cast(Any, rate).to("degree/hour").magnitude, 0, atol=0.001)

def test_field_rotation_rate_pole():
    t = Telescope(aperture=150, focal_length=750)
    c = Camera(36, 24, 6000, 4000, pixel_size=3.76)
    path = OpticalPath(t, [], [], [], [], c)

    # At the North Pole (phi=90), R should be 0 regardless of Az/Alt (except zenith)
    rate = path.field_rotation_rate(altitude_degrees=0, azimuth_degrees=45, latitude_degrees=90)
    assert numpy.isclose(cast(Any, rate).to("degree/hour").magnitude, 0, atol=0.001)

def test_max_alt_az_exposure():
    # ASI2600MC: 6248 x 4176 pixels
    # Diagonal = sqrt(6248^2 + 4176^2) = 7515.5 pixels
    # d_px = 3757.75 pixels
    t = Telescope(aperture=50, focal_length=250)
    c = Camera(23.5, 15.7, 6248, 4176, pixel_size=3.76)
    path = OpticalPath(t, [], [], [], [], c)

    # Latitude 45, Azimuth 0, Altitude 45
    # R = 15.041 * cos(45) * cos(0) / cos(45) = 15.041 deg/hr
    # R_rad_s = (15.041 / 3600) * (pi / 180) = 7.292e-5 rad/s
    # T = 1.0 / (3757.75 * 7.292e-5) = 1.0 / 0.274 = 3.65 seconds
    exposure = path.max_alt_az_exposure(altitude_degrees=45, azimuth_degrees=0, latitude_degrees=45, tolerance_px=1.0)
    assert exposure is not None
    assert numpy.isclose(cast(Any, exposure).to("second").magnitude, 3.65, atol=0.1)

def test_max_alt_az_exposure_zero_rate():
    t = Telescope(aperture=50, focal_length=250)
    c = Camera(23.5, 15.7, 6248, 4176, pixel_size=3.76)
    path = OpticalPath(t, [], [], [], [], c)

    # East/West at equator has zero rotation rate
    exposure = path.max_alt_az_exposure(altitude_degrees=0, azimuth_degrees=90, latitude_degrees=0)
    assert exposure is not None
    assert cast(Any, exposure).to("second").magnitude == 3600
