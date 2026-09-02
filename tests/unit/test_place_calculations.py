from apts.place import Place
from apts.place.calculations import (
    calculate_moon_phase_letter,
    calculate_object_altitude,
    calculate_object_azimuth,
)


def test_calculate_object_altitude_and_azimuth():
    place = Place(lat=52.2297, lon=21.0122, name="Warsaw", elevation=100)
    t = place.date

    alt = calculate_object_altitude(place.observer, "Jupiter", t)
    az = calculate_object_azimuth(place.observer, "Jupiter", t)

    assert isinstance(alt, float)
    assert isinstance(az, float)
    assert 0 <= az <= 360
    assert -90 <= alt <= 90

    # Verify method delegation equivalence
    assert place.get_altitude("Jupiter", t) == alt
    assert place.get_azimuth("Jupiter", t) == az


def test_calculate_moon_phase_letter():
    place = Place(lat=52.2297, lon=21.0122, name="Warsaw")
    letter = calculate_moon_phase_letter(place.eph, place.date)

    assert isinstance(letter, str)
    assert len(letter) == 1
    assert "A" <= letter <= "Z"
    assert place._moon_phase_letter() == letter
