import os
from apts.place import Place
from apts.observations import Observation
from apts.equipment import Equipment
from apts.constants.plot import CoordinateSystem

def test_skymap_texture_generation():
    place = Place(52.2297, 21.0122, "Warsaw")
    equipment = Equipment()
    observation = Observation(place, equipment)

    # Test horizontal texture
    filename_hor = "test_texture_hor.png"
    fig = observation.plot_skymap_texture(
        coordinate_system=CoordinateSystem.HORIZONTAL,
        figsize=(10, 5)
    )
    fig.savefig(filename_hor)
    assert os.path.exists(filename_hor)
    assert os.path.getsize(filename_hor) > 0
    os.remove(filename_hor)

    # Test equatorial texture
    filename_eq = "test_texture_eq.png"
    fig = observation.plot_skymap_texture(
        coordinate_system=CoordinateSystem.EQUATORIAL,
        figsize=(10, 5)
    )
    fig.savefig(filename_eq)
    assert os.path.exists(filename_eq)
    assert os.path.getsize(filename_eq) > 0
    os.remove(filename_eq)

def test_skymap_texture_no_labels():
    # This just ensures it runs without error with labels=False (default)
    place = Place(52.2297, 21.0122, "Warsaw")
    equipment = Equipment()
    observation = Observation(place, equipment)
    filename = "test_texture_no_labels.png"
    fig = observation.plot_skymap_texture(
        plot_labels=False
    )
    fig.savefig(filename)
    assert os.path.exists(filename)
    os.remove(filename)
