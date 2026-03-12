import pytest
from datetime import datetime, timezone
from apts.place import Place
from apts.events import AstronomicalEvents
from apts.constants.event_types import EventType

def test_jupiter_grs_transits():
    # London coordinates
    lat = 51.5074
    lon = 0.1278
    place = Place(lat, lon, "London", elevation=35)

    # Search window for Jan 1, 2024
    start_date = datetime(2024, 1, 1, 0, 0, tzinfo=timezone.utc)
    end_date = datetime(2024, 1, 2, 0, 0, tzinfo=timezone.utc)

    # Initialize events with only GRS transits enabled
    events_calculator = AstronomicalEvents(
        place,
        start_date,
        end_date,
        events_to_calculate=[EventType.JUPITER_GRS_TRANSITS]
    )

    events_df = events_calculator.get_events()

    # We expect at least one transit in this window (calculated at ~17:05 UTC)
    grs_events = events_df[events_df["type"] == "Jupiter GRS Transit"]

    assert len(grs_events) >= 1

    # Check the transit time for the evening event
    # Allowing some margin for calculation differences between ephem and skyfield/analytical search
    transit_time = grs_events.iloc[0]["date"]
    expected_time = datetime(2024, 1, 1, 17, 5, tzinfo=timezone.utc)

    diff_minutes = abs((transit_time - expected_time).total_seconds()) / 60.0
    assert diff_minutes < 10  # Should be within 10 minutes

    assert grs_events.iloc[0]["object"] == "Jupiter"
    assert grs_events.iloc[0]["rarity"] == 4
