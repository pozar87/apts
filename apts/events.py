import ephem
import pandas as pd
from datetime import datetime, timedelta
from itertools import combinations

class AstronomicalEvents:
    def __init__(self, place, start_date, end_date):
        self.place = place
        self.start_date = start_date
        self.end_date = end_date
        self.events = []

    def get_events(self):
        self.calculate_moon_phases()
        self.calculate_eclipses()
        self.calculate_conjunctions()
        self.calculate_oppositions()
        self.calculate_meteor_showers()
        return pd.DataFrame(self.events)

    def calculate_moon_phases(self):
        d = ephem.Date(self.start_date)
        end_date = ephem.Date(self.end_date)
        while d < end_date:
            d = ephem.next_new_moon(d)
            if d > end_date: break
            self.events.append({'date': d.datetime(), 'event': 'New Moon'})
            d = ephem.next_first_quarter_moon(d)
            if d > end_date: break
            self.events.append({'date': d.datetime(), 'event': 'First Quarter Moon'})
            d = ephem.next_full_moon(d)
            if d > end_date: break
            self.events.append({'date': d.datetime(), 'event': 'Full Moon'})
            d = ephem.next_last_quarter_moon(d)
            if d > end_date: break
            self.events.append({'date': d.datetime(), 'event': 'Last Quarter Moon'})

    def calculate_eclipses(self):
        #This is a placeholder as the ephem library does not directly support eclipse calculations.
        pass

    def calculate_conjunctions(self):
        planets = [ephem.Mercury(), ephem.Venus(), ephem.Mars(), ephem.Jupiter(), ephem.Saturn(), ephem.Uranus(), ephem.Neptune()]
        moon = ephem.Moon()

        # Planet-Planet conjunctions
        for p1, p2 in combinations(planets, 2):
            d = ephem.Date(self.start_date)
            end_date = ephem.Date(self.end_date)
            while d < end_date:
                d_next = d + 1
                p1.compute(d)
                p2.compute(d)

                p1_next = p1.copy()
                p2_next = p2.copy()

                p1_next.compute(d_next)
                p2_next.compute(d_next)

                # Check for conjunction
                if ephem.separation(p1, p2) < ephem.separation(p1_next, p2_next):
                    # We are moving away from conjunction, so check if the closest approach was within this interval
                    # This is a simplified approach, a more robust solution would involve root-finding or optimization
                    if ephem.separation(p1, p2) < 1 * ephem.degree:
                        self.events.append({'date': ephem.Date(d).datetime(), 'event': f'{p1.name} conjunct {p2.name}'})
                d = d_next

    def calculate_oppositions(self):
        #This is a placeholder as the ephem library does not directly support opposition calculations.
        pass


    def calculate_meteor_showers(self):
        # Data from https://www.amsmeteors.org/meteor-showers/meteor-shower-calendar/
        showers = {
            'Quadrantids': {'start': (1, 1), 'peak': (1, 4), 'end': (1, 5)},
            'Lyrids': {'start': (4, 14), 'peak': (4, 22), 'end': (4, 30)},
            'Eta Aquarids': {'start': (4, 19), 'peak': (5, 6), 'end': (5, 28)},
            'Delta Aquarids': {'start': (7, 12), 'peak': (7, 30), 'end': (8, 23)},
            'Perseids': {'start': (7, 17), 'peak': (8, 12), 'end': (8, 24)},
            'Orionids': {'start': (10, 2), 'peak': (10, 21), 'end': (11, 7)},
            'Leonids': {'start': (11, 6), 'peak': (11, 17), 'end': (11, 30)},
            'Geminids': {'start': (12, 4), 'peak': (12, 14), 'end': (12, 17)},
            'Ursids': {'start': (12, 17), 'peak': (12, 22), 'end': (12, 26)},
        }
        for year in range(self.start_date.year, self.end_date.year + 1):
            for shower, dates in showers.items():
                peak_date = datetime(year, dates['peak'][0], dates['peak'][1])
                if self.start_date <= peak_date <= self.end_date:
                    self.events.append({'date': peak_date, 'event': f'{shower} Meteor Shower (Peak)'})
