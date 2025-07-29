import pandas as pd
from datetime import datetime, timedelta, timezone
from itertools import combinations
from concurrent.futures import ThreadPoolExecutor

utc = timezone.utc
from . import skyfield_searches
from .catalogs import Catalogs
from skyfield.api import load, Topos, Star
from skyfield import almanac


class AstronomicalEvents:
    def __init__(self, place, start_date, end_date):
        self.place = place
        self.start_date = start_date.astimezone(utc)  # Ensure start_date is UTC
        self.end_date = end_date.astimezone(utc)  # Ensure end_date is UTC
        self.ts = load.timescale()
        self.eph = load("de421.bsp")
        self.observer = self.eph["earth"] + Topos(
            latitude_degrees=self.place.lat_decimal,
            longitude_degrees=self.place.lon_decimal,
            elevation_m=self.place.elevation,
        )
        self.events = []

    def get_events(self):
        with ThreadPoolExecutor() as executor:
            futures = [
                executor.submit(self.calculate_moon_phases),
                executor.submit(self.calculate_conjunctions),
                executor.submit(self.calculate_oppositions),
                executor.submit(self.calculate_meteor_showers),
                executor.submit(self.calculate_highest_altitudes),
                executor.submit(self.calculate_lunar_occultations),
                executor.submit(self.calculate_aphelion_perihelion),
                executor.submit(self.calculate_moon_apogee_perigee),
                executor.submit(self.calculate_mercury_inferior_conjunctions),
                executor.submit(self.calculate_moon_messier_conjunctions),
            ]
            for future in futures:
                self.events.extend(future.result())
        return pd.DataFrame(self.events).sort_values(by="date")

    def calculate_moon_phases(self):
        events = []
        t0 = self.ts.utc(self.start_date)
        t1 = self.ts.utc(self.end_date)
        which_phase = almanac.moon_phases(self.eph)
        t, y = almanac.find_discrete(t0, t1, which_phase)
        for ti, yi in zip(t, y):
            events.append(
                {
                    "date": ti.utc_datetime().astimezone(utc),
                    "event": almanac.MOON_PHASES[yi],
                    "type": "Moon Phase",
                }
            )
        return events

    def calculate_conjunctions(self):
        events = []
        planets = [
            "mercury",
            "venus",
            "mars",
            "jupiter barycenter",
            "saturn barycenter",
            "uranus barycenter",
            "neptune barycenter",
        ]
        moon = "moon"

        # Planet-Planet conjunctions
        for p1, p2 in combinations(planets, 2):
            found_events = skyfield_searches.find_conjunctions(
                self.eph, p1, p2, self.start_date, self.end_date
            )
            for event in found_events:
                event["type"] = "Conjunction"
            events.extend(found_events)

        # Planet-Moon conjunctions
        for p in planets:
            found_events = skyfield_searches.find_conjunctions(
                self.eph, p, moon, self.start_date, self.end_date
            )
            for event in found_events:
                event["type"] = "Conjunction"
            events.extend(found_events)
        return events

    def calculate_oppositions(self):
        events = []
        planets = [
            "mars",
            "jupiter barycenter",
            "saturn barycenter",
            "uranus barycenter",
            "neptune barycenter",
        ]
        for p in planets:
            found_events = skyfield_searches.find_oppositions(
                self.eph, p, self.start_date, self.end_date
            )
            for event in found_events:
                event["type"] = "Opposition"
            events.extend(found_events)
        return events

    def calculate_meteor_showers(self):
        events = []
        showers = {
            "Quadrantids": {"start": (1, 1), "peak": (1, 4), "end": (1, 5)},
            "Lyrids": {"start": (4, 14), "peak": (4, 22), "end": (4, 30)},
            "Eta Aquarids": {"start": (4, 19), "peak": (5, 6), "end": (5, 28)},
            "Delta Aquarids": {"start": (7, 12), "peak": (7, 30), "end": (8, 23)},
            "Perseids": {"start": (7, 17), "peak": (8, 12), "end": (8, 24)},
            "Orionids": {"start": (10, 2), "peak": (10, 21), "end": (11, 7)},
            "Leonids": {"start": (11, 6), "peak": (11, 17), "end": (11, 30)},
            "Geminids": {"start": (12, 4), "peak": (12, 14), "end": (12, 17)},
            "Ursids": {"start": (12, 17), "peak": (12, 22), "end": (12, 26)},
        }
        for year in range(self.start_date.year, self.end_date.year + 1):
            for shower, dates in showers.items():
                peak_date = datetime(
                    year, dates["peak"][0], dates["peak"][1], tzinfo=utc
                )
                if self.start_date <= peak_date <= self.end_date:
                    events.append(
                        {
                            "date": peak_date.astimezone(utc),
                            "event": f"{shower} Meteor Shower (Peak)",
                            "type": "Meteor Shower",
                        }
                    )
        return events

    def calculate_highest_altitudes(self):
        events = []
        for planet_name in ["mercury", "venus"]:
            time, alt = skyfield_searches.find_highest_altitude(
                self.observer, self.eph[planet_name], self.start_date, self.end_date
            )
            if time:
                events.append(
                    {
                        "date": time.astimezone(utc),
                        "event": f"Highest altitude of {planet_name.capitalize()}",
                        "type": "Planet Altitude",
                    }
                )
        return events

    def calculate_lunar_occultations(self):
        events = skyfield_searches.find_lunar_occultations(
            self.observer,
            self.eph,
            Catalogs.BRIGHT_STARS,
            self.start_date,
            self.end_date,
        )
        for event in events:
            event["type"] = "Lunar Occultation"
        return events

    def calculate_aphelion_perihelion(self):
        events = []
        planets = [
            "mercury",
            "venus",
            "mars",
            "jupiter barycenter",
            "saturn barycenter",
            "uranus barycenter",
            "neptune barycenter",
            "moon",
        ]
        for planet_name in planets:
            events_from_search = skyfield_searches.find_aphelion_perihelion(
                self.eph, planet_name, self.start_date, self.end_date
            )
            for event_dict in events_from_search:
                event_dict["date"] = event_dict["date"].astimezone(utc)
                event_dict["type"] = "Aphelion/Perihelion"
                events.append(event_dict)
        return events

    def calculate_moon_apogee_perigee(self):
        events = skyfield_searches.find_moon_apogee_perigee(
            self.eph, self.start_date, self.end_date
        )
        for event in events:
            event["type"] = "Moon Apogee/Perigee"
        return events

    def calculate_mercury_inferior_conjunctions(self):
        events = skyfield_searches.find_mercury_inferior_conjunctions(
            self.eph, self.start_date, self.end_date
        )
        for event in events:
            event["type"] = "Inferior Conjunction"
        return events

    def calculate_moon_messier_conjunctions(self):
        events = []
        messier_objects_to_check = [
            "M1",
            "M2",
            "M3",
            "M4",
            "M5",
            "M8",
            "M9",
            "M10",
            "M11",
            "M12",
            "M14",
            "M15",
            "M16",
            "M17",
            "M18",
            "M19",
            "M20",
            "M21",
            "M22",
            "M23",
            "M24",
            "M25",
            "M26",
            "M27",
            "M28",
            "M30",
            "M35",
            "M41",
            "M42",
            "M43",
            "M44",
            "M45",
            "M46",
            "M47",
            "M48",
            "M49",
            "M50",
            "M53",
            "M54",
            "M55",
            "M58",
            "M59",
            "M60",
            "M61",
            "M62",
            "M64",
            "M65",
            "M66",
            "M67",
            "M68",
            "M71",
            "M72",
            "M73",
            "M74",
            "M75",
            "M77",
            "M78",
            "M79",
            "M80",
            "M83",
            "M84",
            "M85",
            "M86",
            "M87",
            "M88",
            "M89",
            "M90",
            "M91",
            "M93",
            "M95",
            "M96",
            "M98",
            "M99",
            "M100",
            "M104",
            "M105",
            "M107",
        ]

        messier_df = Catalogs.MESSIER[
            Catalogs.MESSIER["Messier"].isin(messier_objects_to_check)
        ]

        for index, messier_data in messier_df.iterrows():
            messier_star = Star.from_dataframe(
                pd.DataFrame(
                    {
                        "ra_hours": [messier_data["RA"].to("hour").magnitude],
                        "dec_degrees": [messier_data["Dec"].to("degree").magnitude],
                        "ra_mas_per_year": [0],
                        "dec_mas_per_year": [0],
                        "parallax_mas": [0],
                        "radial_km_per_s": [0],
                        "epoch_year": [2000.0],
                    },
                    index=[0],
                )
            )

            conjunctions = skyfield_searches.find_conjunctions_with_star(
                self.eph,
                "moon",
                messier_star,
                self.start_date,
                self.end_date,
                threshold_degrees=1.0,
            )
            for conj in conjunctions:
                events.append(
                    {
                        "date": conj["date"].astimezone(utc),
                        "event": f"Moon conjunct {messier_data['Messier']} (sep: {conj['separation_degrees']:.2f} deg)",
                        "type": "Moon-Messier Conjunction",
                    }
                )
        return events
