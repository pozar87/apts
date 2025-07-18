import ephem
from datetime import timedelta

def find_highest_altitude(place, planet, start_date, end_date):
    """
    Finds the highest altitude of an inner planet (Mercury or Venus) in the morning or evening sky.
    """
    place.date = ephem.Date(start_date)
    end_date = ephem.Date(end_date)
    highest_alt = 0
    highest_alt_time = None

    while place.date < end_date:
        # Check evening sky
        place.date = ephem.Date(place.date + 1)
        sunset_time = place.next_setting(ephem.Sun())
        place.date = sunset_time
        planet.compute(place)
        if planet.alt > highest_alt:
            highest_alt = planet.alt
            highest_alt_time = place.date.datetime()

        # Check morning sky
        sunrise_time = place.next_rising(ephem.Sun())
        place.date = sunrise_time
        planet.compute(place)
        if planet.alt > highest_alt:
            highest_alt = planet.alt
            highest_alt_time = place.date.datetime()

    return highest_alt_time, highest_alt

def find_lunar_occultations(place, bright_stars, start_date, end_date):
    """
    Finds lunar occultations of bright stars.
    """
    events = []
    moon = ephem.Moon()
    start_date = ephem.Date(start_date)
    end_date = ephem.Date(end_date)

    for index, star_data in bright_stars.iterrows():
        star = ephem.FixedBody()
        star._ra = ephem.hours(str(star_data['RA'].magnitude))
        star._dec = ephem.degrees(str(star_data['Dec'].magnitude))
        star.name = star_data['Name']

        d = start_date
        while d < end_date:
            d_next = d + 1
            moon.compute(d, epoch='2000')
            star.compute(d, epoch='2000')

            moon_next = moon.copy()
            star_next = star.copy()

            moon_next.compute(d_next, epoch='2000')
            star_next.compute(d_next, epoch='2000')

            # A simplified check for occultation
            if ephem.separation(moon, star) < (moon.radius + star.radius):
                events.append({'date': d.datetime(), 'event': f'Moon occults {star.name}'})

            d = d_next
    return events
