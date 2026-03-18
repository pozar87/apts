
from datetime import datetime, timezone
from apts.events import AstronomicalEvents
from apts.place import Place
from apts.constants.event_types import EventType

def test_jupiter_grs_transits_integration():
    # Projected transit: 2026-03-18 22:16 UTC (night transit)
    start_date = datetime(2026, 3, 18, 20, 0, tzinfo=timezone.utc)
    end_date = datetime(2026, 3, 19, 0, 0, tzinfo=timezone.utc)

    place = Place(51.48, 0.0, "Greenwich", 0.0)
    events = AstronomicalEvents(place, start_date, end_date, events_to_calculate=[EventType.JUPITER_GRS_TRANSITS])
    df = events.get_events()

    assert not df.empty, "Should find at least one GRS transit"
    assert any("Great Red Spot" in ev for ev in df["event"]), "Event name should contain 'Great Red Spot'"
    assert all(df["type"] == "Jupiter GRS Transit"), "Event type should be correct"
    assert all(df["rarity"] == 1), "GRS transit rarity should be 1"

    # Check approximate time
    transit_time = df.iloc[0]["date"]
    assert transit_time.hour == 22
    assert 10 <= transit_time.minute <= 20
