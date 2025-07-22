import pandas as pd
from datetime import datetime, timedelta, timezone
from itertools import combinations

utc = timezone.utc
from . import skyfield_searches
from .catalogs import Catalogs
from skyfield.api import load, Topos
from skyfield import almanac

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
        self.calculate_moon_phases_skyfield()
        self.calculate_conjunctions_skyfield()
        self.calculate_oppositions_skyfield()
        self.calculate_meteor_showers()
        self.calculate_highest_altitudes_skyfield()
        self.calculate_lunar_occultations_skyfield()
        self.calculate_aphelion_perihelion_skyfield()
        self.calculate_moon_apogee_perigee_skyfield()
        self.calculate_mercury_inferior_conjunctions_skyfield()
        return pd.DataFrame(self.events)

    def calculate_moon_phases_skyfield(self):
        t0 = self.ts.utc(self.start_date)
        t1 = self.ts.utc(self.end_date)
        which_phase = almanac.moon_phases(self.eph)
        t, y = almanac.find_discrete(t0, t1, which_phase)
        for ti, yi in zip(t, y):
            self.events.append({'date': ti.utc_datetime(), 'event': almanac.MOON_PHASES[yi]})

    def calculate_conjunctions_skyfield(self):
        planets = ['mercury', 'venus', 'mars', 'jupiter barycenter', 'saturn barycenter', 'uranus barycenter', 'neptune barycenter']
        moon = 'moon'

        # Planet-Planet conjunctions
        for p1, p2 in combinations(planets, 2):
            self.events.extend(skyfield_searches.find_conjunctions(self.eph, p1, p2, self.start_date, self.end_date))

        # Planet-Moon conjunctions
        for p in planets:
            self.events.extend(skyfield_searches.find_conjunctions(self.eph, p, moon, self.start_date, self.end_date))

    def calculate_oppositions_skyfield(self):
        planets = ['mars', 'jupiter barycenter', 'saturn barycenter', 'uranus barycenter', 'neptune barycenter']
        for p in planets:
            self.events.extend(skyfield_searches.find_oppositions(self.eph, p, self.start_date, self.end_date))

    def calculate_meteor_showers(self):
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
                peak_date = datetime(year, dates['peak'][0], dates['peak'][1], tzinfo=utc)
                if self.start_date <= peak_date <= self.end_date:
                    self.events.append({'date': peak_date, 'event': f'{shower} Meteor Shower (Peak)'})

    def calculate_highest_altitudes_skyfield(self):
        for planet_name in ['mercury', 'venus']:
            time, alt = skyfield_searches.find_highest_altitude(self.observer, self.eph[planet_name], self.start_date, self.end_date)
            if time:
                self.events.append({'date': time, 'event': f'Highest altitude of {planet_name.capitalize()}'})

    def calculate_lunar_occultations_skyfield(self):
        self.events.extend(skyfield_searches.find_lunar_occultations(self.observer, self.eph, Catalogs.BRIGHT_STARS, self.start_date, self.end_date))

    def calculate_aphelion_perihelion_skyfield(self):
        planets = ['mercury', 'venus', 'mars', 'jupiter barycenter', 'saturn barycenter', 'uranus barycenter', 'neptune barycenter', 'moon']
        for planet_name in planets:
            self.events.extend(skyfield_searches.find_aphelion_perihelion(self.eph, planet_name, self.start_date, self.end_date))

    def calculate_moon_apogee_perigee_skyfield(self):
        self.events.extend(skyfield_searches.find_moon_apogee_perigee(self.eph, self.start_date, self.end_date))

    def calculate_mercury_inferior_conjunctions_skyfield(self):
        self.events.extend(skyfield_searches.find_mercury_inferior_conjunctions(self.eph, self.start_date, self.end_date))
