import datetime

# timedelta is part of datetime
import pytz  # For timezone awareness

from apts import catalogs
from apts.constants import ObjectTableLabels
from apts.objects import Messier, SolarObjects

from . import setup_observation, setup_place, setup_southern_observation

# Helper to get initial datetime from setup_place
INITIAL_DATE_STR = "2025/02/18 12:00:00"
INITIAL_DT = datetime.datetime.strptime(INITIAL_DATE_STR, "%Y/%m/%d %H:%M:%S").replace(
    tzinfo=pytz.UTC
)


def test_visiable_messier():
    o = setup_observation()
    m = o.get_visible_messier()
    assert len(m) == 37

    # Check that string columns have string dtype
    assert m["Messier"].dtype == "string"
    assert m["NGC"].dtype == "string"
    assert m["Name"].dtype == "string"
    assert m["Type"].dtype == "string"
    assert m["Constellation"].dtype == "string"

    # Check that unit fields have proper units
    assert hasattr(m["RA"].iloc[0], "magnitude")
    assert hasattr(m["RA"].iloc[0], "units")
    assert m["RA"].iloc[0].units == "hour"

    assert hasattr(m["Dec"].iloc[0], "magnitude")
    assert hasattr(m["Dec"].iloc[0], "units")
    assert m["Dec"].iloc[0].units == "degree"

    assert hasattr(m["Distance"].iloc[0], "magnitude")
    assert hasattr(m["Distance"].iloc[0], "units")
    assert str(m["Distance"].iloc[0].units) == "light_year"

    assert hasattr(m["Width"].iloc[0], "magnitude")
    assert hasattr(m["Width"].iloc[0], "units")
    assert m["Width"].iloc[0].units == "arcminute"

    assert hasattr(m["Magnitude"].iloc[0], "magnitude")
    assert hasattr(m["Magnitude"].iloc[0], "units")
    assert m["Magnitude"].iloc[0].units == "mag"


def test_visible_planets():
    o = setup_observation()
    p = o.get_visible_planets()
    assert len(p) == 5  # Allow for small variations, but expect around 5

    # Check that Name is string type
    assert p["Name"].dtype == "string"

    # Check that unit fields have proper units
    assert not hasattr(p["RA"].iloc[0], "magnitude")
    assert not hasattr(p["RA"].iloc[0], "units")

    assert not hasattr(p["Dec"].iloc[0], "magnitude")
    assert not hasattr(p["Dec"].iloc[0], "units")

    assert not hasattr(p["Distance"].iloc[0], "magnitude")
    assert not hasattr(p["Distance"].iloc[0], "units")

    assert not hasattr(p["Size"].iloc[0], "magnitude")
    assert not hasattr(p["Size"].iloc[0], "units")

    assert not hasattr(p["Magnitude"].iloc[0], "magnitude")
    assert not hasattr(p["Magnitude"].iloc[0], "units")

    assert not hasattr(p["Elongation"].iloc[0], "magnitude")
    assert not hasattr(p["Elongation"].iloc[0], "units")

    assert not hasattr(p["Phase"].iloc[0], "magnitude")
    assert not hasattr(p["Phase"].iloc[0], "units")


def test_plot_messier():
    o = setup_observation()
    result = o.plot_messier()
    assert result is not None


def test_plot_planets():
    o = setup_observation()
    result = o.plot_planets()
    assert result is not None


def test_planets_recomputation_with_date():
    place = setup_place()  # Uses fixed date '2025/02/18 12:00:00'
    planets = SolarObjects(place)

    # Store the original transit time for Mars
    mars_transit = planets.objects.loc[
        planets.objects[ObjectTableLabels.NAME] == "Mars", ObjectTableLabels.TRANSIT
    ]
    if not mars_transit.empty:
        original_transit_time_mars = mars_transit.iloc[0]

        # Define a new calculation_date
        new_calculation_date = INITIAL_DT + datetime.timedelta(days=1)

        # Call compute with the new date
        planets.compute(calculation_date=new_calculation_date)

        # Get the new transit time for Mars
        new_transit_time_mars = planets.objects.loc[
            planets.objects[ObjectTableLabels.NAME] == "Mars", ObjectTableLabels.TRANSIT
        ].iloc[0]

        # Assert that the new transit time is different from the original
        assert new_transit_time_mars != original_transit_time_mars

        # Assert that the new transit time is approximately 24 hours after the original
        # Mars' transit shifts by about 24 hours and ~39 minutes per solar day.
        # We'll check if it's within a reasonable window (e.g., 23 to 25 hours to be safe, or more precisely for Mars)
        # For simplicity, we'll check if it's roughly one day later.
        # Allow for some variation due to planetary motion, not exactly 24h.
        # Mars' solar day is approx 24h 39m. So transit will be later.
        time_difference = new_transit_time_mars - original_transit_time_mars
        assert (
            datetime.timedelta(hours=23, minutes=50)
            < time_difference
            < datetime.timedelta(hours=24, minutes=50)
        )


def test_messier_recomputation_with_date():
    place = setup_place()  # Uses fixed date '2025/02/18 12:00:00'
    messier = Messier(place, catalogs, calculation_date=place.date)
    messier.compute(
        calculation_date=place.date
    )  # Explicitly compute for the initial date

    # Store the original transit time for M1 (Crab Nebula)
    # Assuming M1 is in the catalog and its name is 'M1' in the 'Messier' column
    m1_transit = messier.objects.loc[
        messier.objects[ObjectTableLabels.MESSIER] == "M1", ObjectTableLabels.TRANSIT
    ]
    if not m1_transit.empty:
        original_transit_time_m1 = m1_transit.iloc[0]

        # Define a new calculation_date
        new_calculation_date = INITIAL_DT + datetime.timedelta(days=1)

        # Call compute with the new date
        messier.compute(calculation_date=new_calculation_date)

        # Get the new transit time for M1
        new_transit_time_m1 = messier.objects.loc[
            messier.objects[ObjectTableLabels.MESSIER] == "M1",
            ObjectTableLabels.TRANSIT,
        ].iloc[0]

        # Assert that the new transit time is different from the original
        assert new_transit_time_m1 != original_transit_time_m1

        # Assert that the new transit time is approximately 1 solar day minus ~3m 56s (sidereal correction) after the original.
        # This means the actual interval between the two transits will be ~23h 56m 4s.
        time_difference = new_transit_time_m1 - original_transit_time_m1

        # Lower bound: 1 day - 4 minutes = 23 hours 56 minutes 0 seconds
        expected_interval_lower = datetime.timedelta(days=1) - datetime.timedelta(
            minutes=4, seconds=4
        )
        # Upper bound: 1 day - 3 minutes 50 seconds = 23 hours 56 minutes 10 seconds
        expected_interval_upper = datetime.timedelta(days=1) - datetime.timedelta(
            minutes=3, seconds=50
        )

        assert expected_interval_lower < time_difference < expected_interval_upper


def test_planets_backward_compatibility():
    place = setup_place()
    planets = SolarObjects(place)
    mars_transit = planets.objects.loc[
        planets.objects[ObjectTableLabels.NAME] == "Mars", ObjectTableLabels.TRANSIT
    ]
    if not mars_transit.empty:
        original_transit_time_mars = mars_transit.iloc[0]

        # Call compute without arguments
        planets.compute()
        new_transit_time_mars = planets.objects.loc[
            planets.objects[ObjectTableLabels.NAME] == "Mars", ObjectTableLabels.TRANSIT
        ].iloc[0]

        # Assert that the transit time has not changed
        assert new_transit_time_mars == original_transit_time_mars


def test_messier_backward_compatibility():
    place = setup_place()
    messier = Messier(place, catalogs, calculation_date=place.date)
    messier.compute(
        calculation_date=place.date
    )  # Explicitly compute for the initial date
    original_transit_time_m1 = messier.objects.loc[
        messier.objects[ObjectTableLabels.MESSIER] == "M1", ObjectTableLabels.TRANSIT
    ].iloc[0]

    # Call compute without arguments
    messier.compute()
    new_transit_time_m1 = messier.objects.loc[
        messier.objects[ObjectTableLabels.MESSIER] == "M1", ObjectTableLabels.TRANSIT
    ].iloc[0]

    # Assert that the transit time has not changed
    assert new_transit_time_m1 == original_transit_time_m1


def test_visible_messier_southern_hemisphere():
    o = setup_southern_observation()
    m = o.get_visible_messier()
    assert len(m) > 0
