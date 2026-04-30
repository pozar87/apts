from datetime import datetime, timezone
from apts.events import AstronomicalEvents
from apts.place import Place
from apts.constants.event_types import EventType

def test_moon_libration_maxima_detection():
    # Look for libration maxima in Jan 2026
    start_date = datetime(2026, 1, 1, tzinfo=timezone.utc)
    end_date = datetime(2026, 2, 1, tzinfo=timezone.utc)

    # Use global observer (elevation=-9999) to skip topocentric visibility checks
    place_test = Place(name="Global", lat=0, lon=0, elevation=-9999)

    events = AstronomicalEvents(
        place_test,
        start_date,
        end_date,
        events_to_calculate=[EventType.MOON_LIBRATION_MAXIMA]
    )

    df = events.get_events()
    lib_maxima = df[df["type"] == "Moon Libration Maximum"]

    # In a typical month, there should be 4 libration maxima (Lon Max/Min, Lat Max/Min)
    assert not lib_maxima.empty
    assert len(lib_maxima) >= 4

    # Check for all four sides
    sides = lib_maxima["side"].tolist()
    assert "North" in sides
    assert "South" in sides
    assert "East" in sides
    assert "West" in sides

    # Check for typical libration values (approx +/- 6 to 8 degrees)
    for val in lib_maxima["libration_value"]:
        assert abs(val) > 4.0
        assert abs(val) < 10.0

    # Ensure rarity is calculated
    assert all(lib_maxima["rarity"].notna())
    assert all(lib_maxima["rarity"] == 1) # Libration maxima are relatively common (monthly)
