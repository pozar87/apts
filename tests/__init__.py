import datetime

from apts import equipment, observations, opticalequipment, place
from apts.utils import ConnectionType


def setup_equipment():
    # Setup basic equipment
    e = equipment.Equipment()
    # Register telescope with both 1.25" and T2 outputs
    e.register(
        opticalequipment.Telescope(
            150, 750, outputs=[ConnectionType.F_1_25, ConnectionType.T2]
        )
    )
    e.register(opticalequipment.Eyepiece(25))
    return e


def setup_place():
    p = place.Place(
        name="Zelków",
        lat=50.1637973,
        lon=19.7855169,
        date=datetime.datetime(2025, 2, 18, 12, 0, 0, tzinfo=datetime.timezone.utc),
    )
    return p


def setup_observation():
    # Setup basic observations
    p = setup_place()
    e = setup_equipment()
    o = observations.Observation(p, e)
    o.conditions.max_moon_illumination = 100
    return o


def setup_southern_place():
    p = place.Place(
        name="Sydney",
        lat=-33.8688,
        lon=151.2093,
        date=datetime.datetime(2025, 2, 18, 22, 0, 0, tzinfo=datetime.timezone.utc),
    )
    return p


def setup_southern_observation():
    # Setup basic observations
    p = setup_southern_place()
    e = setup_equipment()
    o = observations.Observation(p, e)
    o.conditions.max_moon_illumination = 100
    return o
