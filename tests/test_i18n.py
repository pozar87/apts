import apts
from apts import Place, Observation, Equipment
from apts.conditions import Conditions
from apts.events import AstronomicalEvents
from datetime import datetime, timedelta, timezone
from apts.constants.event_types import EventType
from apts.cache import clear_cache
import pytest

def test_language_switching_for_events():
    """
    Tests that the language of events can be switched dynamically.
    """
    clear_cache()
    my_place = Place(lat=52.2297, lon=21.0122, name="Warsaw")
    start_date = datetime(2025, 1, 1, tzinfo=timezone.utc)
    end_date = start_date + timedelta(days=365)

    apts.set_language('en')
    events_en = AstronomicalEvents(place=my_place, start_date=start_date, end_date=end_date, events_to_calculate=[EventType.SOLAR_ECLIPSES])
    events_df_en = events_en.get_events()
    assert "Solar Eclipse" in events_df_en['type'].values

    apts.set_language('pl')
    events_pl = AstronomicalEvents(place=my_place, start_date=start_date, end_date=end_date, events_to_calculate=[EventType.SOLAR_ECLIPSES])
    events_df_pl = events_pl.get_events()
    assert "Zaćmienie Słońca" in events_df_pl['type'].values

def test_language_switching_for_plots():
    """
    Tests that the language of plots can be switched dynamically.
    """
    clear_cache()
    my_place = Place(lat=52.2297, lon=21.0122, name="Warsaw", date=datetime(2025, 1, 1, tzinfo=timezone.utc))
    equipment = Equipment()

    apts.set_language('en')
    observation_en = Observation(place=my_place, equipment=equipment)
    fig_en = observation_en.plot_messier()
    assert fig_en.axes[0].get_title() == "Messier Objects Altitude"

    apts.set_language('pl')
    observation_pl = Observation(place=my_place, equipment=equipment)
    fig_pl = observation_pl.plot_messier()
    assert fig_pl.axes[0].get_title() == "Wysokość obiektów Messiera"

def test_language_switching_for_messier_types():
    """
    Tests that the language of Messier object types can be switched dynamically.
    """
    clear_cache()
    target_date = datetime(2025, 1, 1, tzinfo=timezone.utc)
    my_place = Place(lat=52.2297, lon=21.0122, name="Warsaw")
    equipment = Equipment()

    conditions = Conditions(max_return="04:00:00")

    apts.set_language('en')
    observation_en = Observation(
        place=my_place,
        equipment=equipment,
        limiting_magnitude=15.0,
        conditions=conditions,
        target_date=target_date,
    )
    visible_messier_en = observation_en.get_visible_messier()
    assert "Globular Cluster" in visible_messier_en["Type"].values

    apts.set_language("pl")
    observation_pl = Observation(
        place=my_place,
        equipment=equipment,
        limiting_magnitude=15.0,
        conditions=conditions,
        target_date=target_date,
    )
    visible_messier_pl = observation_pl.get_visible_messier()
    assert "Gromada kulista" in visible_messier_pl["Type"].values
