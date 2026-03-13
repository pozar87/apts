
from datetime import datetime, timezone
from apts.events import AstronomicalEvents
from apts.place import Place
from apts.constants.event_types import EventType

def test_jupiter_grs_transits_integration():
    # Known transit: 2025-01-01 01:52 UTC
    start_date = datetime(2025, 1, 1, 0, 0, tzinfo=timezone.utc)
    end_date = datetime(2025, 1, 1, 6, 0, tzinfo=timezone.utc)

    place = Place(51.48, 0.0, "Greenwich", 0.0)
    events = AstronomicalEvents(place, start_date, end_date, events_to_calculate=[EventType.JUPITER_GRS_TRANSITS])
    df = events.get_events()

    assert not df.empty, "Should find at least one GRS transit"
    assert any("Great Red Spot" in ev for ev in df["event"]), "Event name should contain 'Great Red Spot'"
    assert all(df["type"] == "Jupiter GRS Transit"), "Event type should be correct"
    assert all(df["rarity"] == 4), "GRS transit rarity should be 4"

    # Check approximate time
    transit_time = df.iloc[0]["date"]
    assert transit_time.hour == 1
    assert 50 <= transit_time.minute <= 55
