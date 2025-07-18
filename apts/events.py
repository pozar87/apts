import pandas as pd
from datetime import datetime, timedelta
from itertools import combinations
from . import searches
from .catalogs import Catalogs
from skyfield.api import load, Topos

class AstronomicalEvents:
    def __init__(self, place, start_date, end_date):
        self.place = place
        self.start_date = start_date
        self.end_date = end_date
        self.ts = load.timescale()
        self.eph = load('de421.bsp')
        self.observer = self.eph['earth'] + Topos(latitude_degrees=self.place.lat_decimal,
                                                 longitude_degrees=self.place.lon_decimal,
                                                 elevation_m=self.place.elevation)
        self.events = []

    def get_events(self):
        self.calculate_moon_phases()
        self.calculate_conjunctions()
        self.calculate_meteor_showers()
        self.calculate_highest_altitudes()
        self.calculate_lunar_occultations()
        self.calculate_aphelion_perihelion()
        self.calculate_moon_apogee_perigee()
        self.calculate_mercury_inferior_conjunctions()
        return pd.DataFrame(self.events)

    def calculate_moon_phases(self):
        t0 = self.ts.utc(self.start_date)
        t1 = self.ts.utc(self.end_date)

        # Skyfield's almanac for moon phases is reliable
        from skyfield import almanac
        t, y = almanac.find_discrete(t0, t1, almanac.moon_phases(self.eph))

        phase_names = ['New Moon', 'First Quarter', 'Full Moon', 'Last Quarter']
        for ti, yi in zip(t, y):
            self.events.append({'date': ti.utc_datetime(), 'event': phase_names[yi]})

    def calculate_conjunctions(self):
        planets = ['mercury', 'venus', 'mars', 'jupiter barycenter', 'saturn barycenter', 'uranus barycenter', 'neptune barycenter']
        for p1_name, p2_name in combinations(planets, 2):
            self.events.extend(searches.find_conjunctions(self.eph, p1_name, p2_name, self.start_date, self.end_date))

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

    def calculate_highest_altitudes(self):
        for planet_name in ['mercury', 'venus']:
            time, alt = searches.find_highest_altitude(self.observer, self.eph[planet_name], self.start_date, self.end_date)
            if time:
                self.events.append({'date': time, 'event': f'Highest altitude of {planet_name.capitalize()}'})

    def calculate_lunar_occultations(self):
        self.events.extend(searches.find_lunar_occultations(self.observer, self.eph, Catalogs.BRIGHT_STARS, self.start_date, self.end_date))

    def calculate_aphelion_perihelion(self):
        planets = ['mercury', 'venus', 'mars', 'jupiter barycenter', 'saturn barycenter', 'uranus barycenter', 'neptune barycenter', 'moon']
        for planet_name in planets:
            self.events.extend(searches.find_aphelion_perihelion(self.eph, planet_name, self.start_date, self.end_date))

    def calculate_moon_apogee_perigee(self):
        self.events.extend(searches.find_moon_apogee_perigee(self.eph, self.start_date, self.end_date))

    def calculate_mercury_inferior_conjunctions(self):
        self.events.extend(searches.find_mercury_inferior_conjunctions(self.eph, self.start_date, self.end_date))
