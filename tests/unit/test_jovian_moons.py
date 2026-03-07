import pytest
from datetime import datetime, timezone
from apts.events import AstronomicalEvents
from apts.place import Place
from apts.constants.event_types import EventType

def test_jovian_moon_events_found():
    place = Place(52.2297, 21.0122, name="Warsaw")
    # A known period with events
    start_date = datetime(2024, 1, 1, 0, 0, tzinfo=timezone.utc)
    end_date = datetime(2024, 1, 5, 0, 0, tzinfo=timezone.utc)

    ae = AstronomicalEvents(place, start_date, end_date, events_to_calculate=[EventType.JOVIAN_MOON_EVENTS])
    df = ae.get_events()

    assert not df.empty
    assert all(df['type'] == 'Jovian Moon Event')
    assert 'Io' in df['object'].values
    ae.shutdown()

def test_jovian_event_rarity():
    place = Place(52.2297, 21.0122, name="Warsaw")
    ae = AstronomicalEvents(place, datetime(2024,1,1, tzinfo=timezone.utc), datetime(2024,1,2, tzinfo=timezone.utc))
    rarity = ae._get_rarity("Jovian Moon Event", {})
    assert rarity == 4
    ae.shutdown()
