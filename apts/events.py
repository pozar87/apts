import ephem
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
        self.calculate_conjunctions_ephem()
        self.calculate_oppositions_ephem()
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

    def calculate_conjunctions_ephem(self):
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

                if ephem.separation(p1, p2) < ephem.separation(p1_next, p2_next):
                    if ephem.separation(p1, p2) < 1 * ephem.degree:
                        self.events.append({'date': ephem.Date(d).datetime(), 'event': f'{p1.name} conjunct {p2.name}'})
                d = d_next

    def calculate_oppositions_ephem(self):
        #This is a placeholder as the ephem library does not directly support opposition calculations.
        pass

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
