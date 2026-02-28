import numpy as np
from apts.opticalequipment.binoculars import Binoculars
from apts.constants import OpticalType, GraphConstants
from apts.equipment import Equipment


def test_binoculars_init():
    b = Binoculars(
        magnification=10, objective_diameter=50, vendor="Nikon", apparent_fov_deg=65
    )
    assert b.magnification == 10
    assert b.objective_diameter.magnitude == 50
    assert b.apparent_fov_deg.magnitude == 65
    assert b._type == OpticalType.BINOCULARS


def test_binoculars_str():
    b = Binoculars(
        magnification=10, objective_diameter=50, vendor="Nikon", apparent_fov_deg=65
    )
    assert str(b) == "Nikon 10x50"


def test_binoculars_fov():
    b = Binoculars(
        magnification=10, objective_diameter=50, vendor="Nikon", apparent_fov_deg=65
    )
    assert b.fov().magnitude == 6.5


def test_binoculars_exit_pupil():
    b = Binoculars(
        magnification=10, objective_diameter=50, vendor="Nikon", apparent_fov_deg=65
    )
    assert b.exit_pupil().magnitude == 5.0


def test_binoculars_limits():
    b = Binoculars(
        magnification=10, objective_diameter=50, vendor="Nikon", apparent_fov_deg=65
    )
    assert b.dawes_limit().magnitude == 2.32
    assert round(b.rayleigh_limit().magnitude, 2) == 2.77


def test_binoculars_limiting_magnitude():
    b = Binoculars(
        magnification=10, objective_diameter=50, vendor="Nikon", apparent_fov_deg=65
    )
    assert np.isclose(b.limiting_magnitude(), 11.19, atol=0.01)


def test_binoculars_brightness():
    b = Binoculars(
        magnification=10, objective_diameter=50, vendor="Nikon", apparent_fov_deg=65
    )
    assert np.isclose(b.brightness(), 51.02, atol=0.01)


def test_binoculars_register():
    eq = Equipment()
    b = Binoculars(
        magnification=10, objective_diameter=50, vendor="Nikon", apparent_fov_deg=65
    )
    b.register(eq)
    assert b.id() in eq.connection_garph.nodes()
    assert eq.connection_garph.has_edge(GraphConstants.SPACE_ID, b.id())
    assert eq.connection_garph.has_edge(b.id(), GraphConstants.EYE_ID)


def test_binoculars_output_type():
    b = Binoculars(
        magnification=10, objective_diameter=50, vendor="Nikon", apparent_fov_deg=65
    )
    assert b.output_type() == OpticalType.VISUAL


def test_binoculars_max_useful_zoom():
    b = Binoculars(
        magnification=10, objective_diameter=50, vendor="Nikon", apparent_fov_deg=65
    )
    assert b.max_useful_zoom() == 10
