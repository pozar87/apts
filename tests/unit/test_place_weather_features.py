import datetime
import unittest
from unittest.mock import MagicMock, patch
import pandas as pd
from apts.place import Place
from apts.weather import Weather

class TestPlaceWeatherFeatures(unittest.TestCase):
    def setUp(self):
        # Setup Place at a specific location
        self.lat, self.lon = 52.2297, 21.0122  # Warsaw
        self.date = datetime.datetime(2024, 1, 1, 20, 0, 0, tzinfo=datetime.timezone.utc)
        self.place = Place(self.lat, self.lon, date=self.date)

        # Mock weather data
        weather_df = pd.DataFrame({
            "time": [self.date - datetime.timedelta(hours=1), self.date, self.date + datetime.timedelta(hours=1)],
            "cloudCover": [0.0, 50.0, 100.0],
            "windSpeed": [10.0, 20.0, 30.0],
            "humidity": [60.0, 85.0, 95.0]
        })
        self.place.weather = MagicMock(spec=Weather)
        self.place.weather.data = weather_df

    @patch("apts.place.LightPollution.get_light_pollution")
    @patch("apts.place.get_planet_magnitude")
    def test_get_sqm_urban_cloudy(self, mock_mag, mock_lp):
        # Scenario: Urban (Bortle 7), Cloudy (50%), Night (Sun below -18), No Moon
        mock_lp.return_value = 7
        mock_mag.return_value = -12.7  # Not used if moon is down

        # Mock sun and moon altitudes
        with patch.object(self.place.observer, "at") as mock_at:
            mock_sun = MagicMock()
            mock_sun.apparent.return_value.altaz.return_value = [MagicMock(degrees=-20), MagicMock(degrees=180), MagicMock(km=0)]

            mock_moon = MagicMock()
            mock_moon.apparent.return_value.altaz.return_value = [MagicMock(degrees=-10), MagicMock(degrees=180), MagicMock(km=0)]

            mock_at.return_value.observe.side_effect = [mock_sun, mock_moon]

            sqm = self.place.get_sqm()

            # Base Bortle 7 SQM is approx 18.25.
            # Clouds at Bortle 7 should make it brighter (lower SQM).
            base_sqm = 18.25 # LightPollution.bortle_to_sqm(7)
            self.assertLess(sqm, base_sqm)

    @patch("apts.place.LightPollution.get_light_pollution")
    @patch("apts.place.get_planet_magnitude")
    def test_get_sqm_dark_site_cloudy(self, mock_mag, mock_lp):
        # Scenario: Dark Site (Bortle 2), Cloudy (50%), Night, No Moon
        mock_lp.return_value = 2

        with patch.object(self.place.observer, "at") as mock_at:
            mock_sun = MagicMock()
            mock_sun.apparent.return_value.altaz.return_value = [MagicMock(degrees=-20), MagicMock(degrees=180), MagicMock(km=0)]

            mock_moon = MagicMock()
            mock_moon.apparent.return_value.altaz.return_value = [MagicMock(degrees=-10), MagicMock(degrees=180), MagicMock(km=0)]

            mock_at.return_value.observe.side_effect = [mock_sun, mock_moon]

            sqm = self.place.get_sqm()

            # Base Bortle 2 SQM is approx 21.67.
            # Clouds at Bortle 2 should make it darker (higher SQM).
            base_sqm = 21.67
            self.assertGreater(sqm, base_sqm)

    @patch("apts.place.LightPollution.get_light_pollution")
    @patch("apts.place.get_planet_magnitude")
    def test_get_sqm_full_moon(self, mock_mag, mock_lp):
        # Scenario: Dark Site, Clear, Full Moon at Zenith
        mock_lp.return_value = 1
        mock_mag.return_value = -12.7

        # Clear weather
        self.place.weather.data.loc[1, "cloudCover"] = 0.0

        with patch.object(self.place.observer, "at") as mock_at:
            mock_sun = MagicMock()
            mock_sun.apparent.return_value.altaz.return_value = [MagicMock(degrees=-30), MagicMock(degrees=180), MagicMock(km=0)]

            mock_moon = MagicMock()
            mock_moon.apparent.return_value.altaz.return_value = [MagicMock(degrees=90), MagicMock(degrees=180), MagicMock(km=0)]

            mock_at.return_value.observe.side_effect = [mock_sun, mock_moon]

            sqm = self.place.get_sqm()

            # Full moon should significantly lower SQM (brighter sky)
            base_sqm = 21.88
            self.assertLess(sqm, base_sqm)
            self.assertLess(sqm, 19.0) # Full moon is bright

    def test_get_seeing_ideal(self):
        # Scenario: Calm, Dry, Clear
        self.place.weather.data.loc[1, "cloudCover"] = 0.0
        self.place.weather.data.loc[1, "windSpeed"] = 5.0
        self.place.weather.data.loc[1, "humidity"] = 40.0

        seeing = self.place.get_seeing()
        self.assertEqual(seeing, 1.5)

    def test_get_seeing_bad(self):
        # Scenario: Windy, Humid, Cloudy
        self.place.weather.data.loc[1, "cloudCover"] = 80.0
        self.place.weather.data.loc[1, "windSpeed"] = 40.0
        self.place.weather.data.loc[1, "humidity"] = 90.0

        seeing = self.place.get_seeing()
        # Base 1.5 + wind(40-15)/50=0.5 + humidity(90-80)/40=0.25 + cloud 0.3 = 2.55
        self.assertAlmostEqual(seeing, 2.55)

if __name__ == "__main__":
    unittest.main()
