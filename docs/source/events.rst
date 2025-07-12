Astronomical Events
===================

The `apts` library can be used to predict various astronomical events for a given location.

API
---

The `AstronomicalEvents` class is used to calculate a list of events for a given time period.

.. autoclass:: apts.events.AstronomicalEvents
   :members:
   :exclude-members: calculate_conjunctions

The `Observation` class provides a convenient way to access the event prediction functionality.

.. automethod:: apts.observations.Observation.get_astronomical_events

Usage
-----

The following script demonstrates how to use the `get_astronomical_events` method to get a list of events for a given location.

.. automethod:: apts.events.AstronomicalEvents.calculate_conjunctions

.. automethod:: apts.events.AstronomicalEvents.calculate_oppositions

.. code-block:: python

    from apts.observations import Observation
    from apts.place import Place
    from apts.equipment import Equipment

    def get_events(lat: float, lon: float, elevation: int = 300, days: int = 365):
        place = Place(lat=lat, lon=lon, elevation=elevation)
        equipment = Equipment() # Dummy equipment
        observation = Observation(place, equipment)
        events = observation.get_astronomical_events(days=days)
        return events

    if __name__ == '__main__':
        events_df = get_events(lat=52.2, lon=21.0)
        print(events_df)
