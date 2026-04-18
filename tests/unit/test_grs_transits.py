from datetime import datetime, timezone
from apts.place import Place
from apts.events import AstronomicalEvents
from apts.constants.event_types import EventType

def test_jupiter_grs_transits():
    # London coordinates
    lat = 51.5074
    lon = 0.1278
    place = Place(lat, lon, "London", elevation=35)

    # Search window for March 18, 2026
    start_date = datetime(2026, 3, 18, 0, 0, tzinfo=timezone.utc)
    end_date = datetime(2026, 3, 19, 0, 0, tzinfo=timezone.utc)

    # Initialize events with only GRS transits enabled
    events_calculator = AstronomicalEvents(
        place,
        start_date,
        end_date,
        events_to_calculate=[EventType.JUPITER_GRS_TRANSITS]
    )

    events_df = events_calculator.get_events()

    # We expect at least one visible transit in this window (calculated at ~22:16 UTC)
    # The midday transit (~12:21 UTC) is not visible due to daylight (Sun altitude ~37 deg)
    grs_events = events_df[events_df["type"] == "Jupiter GRS Transit"]

    assert len(grs_events) >= 1

    # Check the transit time for the first event
    transit_time = grs_events.iloc[0]["date"]
    # With correctly identified intrinsic longitude (55.2),
    # the observed transit is at ~02:25 UTC
    expected_time = datetime(2026, 3, 18, 2, 25, tzinfo=timezone.utc)

    diff_minutes = abs((transit_time - expected_time).total_seconds()) / 60.0
    assert diff_minutes < 10  # Should be within 10 minutes

    assert grs_events.iloc[0]["object"] == "Jupiter"
    assert grs_events.iloc[0]["rarity"] == 1

def test_jupiter_grs_transits_custom_longitude():
    # London coordinates
    lat = 51.5074
    lon = 0.1278
    place = Place(lat, lon, "London", elevation=35)

    # Search window for March 18, 2026
    start_date = datetime(2026, 3, 18, 0, 0, tzinfo=timezone.utc)
    end_date = datetime(2026, 3, 19, 0, 0, tzinfo=timezone.utc)

    events_calculator = AstronomicalEvents(place, start_date, end_date)

    # Test with custom longitude (e.g., 15.0 instead of default)
    # A transit at 15.0 should happen approx (80-15)/360 * 9.9 hours earlier than at 80.0
    # 65/360 * 9.9 = 1.7875 hours = 107 minutes
    # Original (no LT): 02:26 - 107 mins = 00:39
    # With LT correction (~40 mins): 03:06 - 107 mins = 01:19
    events = events_calculator.calculate_jupiter_grs_transits(grs_longitude=15.0)

    assert len(events) >= 1
    # Depending on visibility, we might get the 01:19 one.
    # Let's find the one closest to 01:19.
    transit_time = min(events, key=lambda e: abs((e["date"] - datetime(2026, 3, 18, 1, 19, tzinfo=timezone.utc)).total_seconds()))["date"]

    expected_time = datetime(2026, 3, 18, 1, 19, tzinfo=timezone.utc)
    diff_minutes = abs((transit_time - expected_time).total_seconds()) / 60.0
    assert diff_minutes < 10
