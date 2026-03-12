from datetime import datetime, timezone
from apts.place import Place
from apts.events import AstronomicalEvents
from apts.constants.event_types import EventType

def test_jupiter_grs_transits():
    # London coordinates
    lat = 51.5074
    lon = 0.1278
    place = Place(lat, lon, "London", elevation=35)

    # Search window for Jan 1, 2025
    start_date = datetime(2025, 1, 1, 0, 0, tzinfo=timezone.utc)
    end_date = datetime(2025, 1, 2, 0, 0, tzinfo=timezone.utc)

    # Initialize events with only GRS transits enabled
    events_calculator = AstronomicalEvents(
        place,
        start_date,
        end_date,
        events_to_calculate=[EventType.JUPITER_GRS_TRANSITS]
    )

    events_df = events_calculator.get_events()

    # We expect at least one transit in this window (calculated at ~01:52 UTC)
    grs_events = events_df[events_df["type"] == "Jupiter GRS Transit"]

    assert len(grs_events) >= 1

    # Check the transit time for the evening event
    transit_time = grs_events.iloc[0]["date"]
    expected_time = datetime(2025, 1, 1, 1, 52, tzinfo=timezone.utc)

    diff_minutes = abs((transit_time - expected_time).total_seconds()) / 60.0
    assert diff_minutes < 10  # Should be within 10 minutes

    assert grs_events.iloc[0]["object"] == "Jupiter"
    assert grs_events.iloc[0]["rarity"] == 4

def test_jupiter_grs_transits_custom_longitude():
    # London coordinates
    lat = 51.5074
    lon = 0.1278
    place = Place(lat, lon, "London", elevation=35)

    # Search window for Jan 1, 2025
    start_date = datetime(2025, 1, 1, 0, 0, tzinfo=timezone.utc)
    end_date = datetime(2025, 1, 2, 0, 0, tzinfo=timezone.utc)

    events_calculator = AstronomicalEvents(place, start_date, end_date)

    # Test with custom longitude (e.g., 15.0 instead of default)
    # A transit at 15.0 should happen approx (66-15)/360 * 9.9 hours earlier than at 66.0
    # 51/360 * 9.9 = 1.4025 hours = 84 minutes
    # 01:52 - 84 mins = 00:28
    events = events_calculator.calculate_jupiter_grs_transits(grs_longitude=15.0)

    assert len(events) >= 1
    transit_time = events[0]["date"]

    expected_time = datetime(2025, 1, 1, 0, 28, tzinfo=timezone.utc)
    diff_minutes = abs((transit_time - expected_time).total_seconds()) / 60.0
    assert diff_minutes < 10
