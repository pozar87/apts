from datetime import datetime, timezone
from skyfield.api import Star
from apts.place import Place
from apts.skyfield_searches import find_object_culminations

def test_find_object_culminations_vectorized():
    # Given: A specific observer (e.g., Warsaw) and a DSO (e.g., M31)
    observer = Place(52.2297, 21.0122, "Warsaw", 100)

    # M31: RA 00h 42m 44s, Dec +41° 16' 09"
    m31 = Star(ra_hours=(0, 42, 44), dec_degrees=(41, 16, 9))
    objects_data = [("M31", m31)]

    start_date = datetime(2025, 9, 1, tzinfo=timezone.utc)
    end_date = datetime(2025, 9, 3, tzinfo=timezone.utc)

    # When: Finding culminations
    events = find_object_culminations(observer.observer, objects_data, start_date, end_date)

    # Then: We expect one culmination per day
    assert len(events) >= 2
    for event in events:
        assert event["object"] == "M31"
        assert event["type"] == "Messier Culmination"
        assert "altitude" in event
        assert event["altitude"] > 0
        # Check that date is within range
        assert start_date <= event["date"] <= end_date

def test_find_object_culminations_multiple_objects():
    observer = Place(52.2297, 21.0122, "Warsaw", 100)

    # M31 and M13
    m31 = Star(ra_hours=(0, 42, 44), dec_degrees=(41, 16, 9))
    m13 = Star(ra_hours=(16, 41, 41), dec_degrees=(36, 27, 37))
    objects_data = [("M31", m31), ("M13", m13)]

    start_date = datetime(2025, 12, 1, tzinfo=timezone.utc)
    end_date = datetime(2025, 12, 3, tzinfo=timezone.utc)

    # Disable sun threshold for testing
    events = find_object_culminations(observer.observer, objects_data, start_date, end_date, sun_alt_threshold=90)

    objects_found = {event["object"] for event in events}
    assert "M31" in objects_found
    assert "M13" in objects_found
