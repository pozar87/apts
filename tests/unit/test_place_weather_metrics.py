import pytest
import pandas as pd
from datetime import datetime, timezone
from unittest.mock import MagicMock, patch
from apts.place import Place

@pytest.fixture
def place():
    return Place(lat=52.2297, lon=21.0122, name="Warsaw")

def test_get_sqm_no_weather(place):
    # Mock get_light_pollution to return a known Bortle class
    with patch.object(place, 'get_light_pollution', return_value=4):
        # Mock Sun and Moon altitude to be low (night, no moon)
        with patch.object(place.observer, 'at') as mock_at:
            # Sun altitude -20, Moon altitude -10
            # We need to handle multiple calls to observe()
            def side_effect(obj):
                mock_res = MagicMock()
                if obj == place.sun:
                    mock_res.apparent.return_value.altaz.return_value = [MagicMock(degrees=-20), 0, 0]
                elif obj == place.moon:
                    mock_res.apparent.return_value.altaz.return_value = [MagicMock(degrees=-10), 0, 0]
                return mock_res

            mock_at.return_value.observe.side_effect = side_effect

            sqm = place.get_sqm()
            # Bortle 4 base SQM is approx 21.2 - 21.5
            assert 21.0 <= sqm <= 22.0

def test_get_seeing_no_weather(place):
    seeing = place.get_seeing()
    assert seeing == 1.5 # Default base seeing

def test_add_extra_weather_info(place):
    # Setup mock weather data (using a date where Moon is down for Warsaw)
    # 2024-01-11 00:00 UTC
    dt = datetime(2024, 1, 11, 0, 0, tzinfo=timezone.utc)
    weather_data = pd.DataFrame({
        "time": [dt],
        "cloudCover": [0],
        "windSpeed": [10],
        "humidity": [50]
    })
    place.weather = MagicMock()
    place.weather.data = weather_data

    with patch.object(place, 'get_light_pollution', return_value=1):
        place._add_extra_weather_info()

    assert "sqm" in place.weather.data.columns
    assert "seeing" in place.weather.data.columns
    # SQM for Bortle 1 should be high (~21.9 - 22.0)
    assert place.weather.data.loc[0, "sqm"] > 21.5
    assert place.weather.data.loc[0, "seeing"] == 1.5

def test_get_sqm_with_weather(place):
    dt = datetime(2024, 1, 1, 0, 0, tzinfo=timezone.utc)
    weather_data = pd.DataFrame({
        "time": [dt],
        "cloudCover": [100],
        "windSpeed": [10],
        "humidity": [50]
    })
    place.weather = MagicMock()
    place.weather.data = weather_data

    # Mock Skyfield time to return our specific datetime
    ts = place.ts
    time_mock = ts.utc(dt)

    with patch.object(place, 'get_light_pollution', return_value=9): # Urban
        with patch.object(place, '_get_scalar_datetime', return_value=dt):
             sqm = place.get_sqm(time=time_mock)
             # In urban areas, clouds make sky brighter (SQM lower)
             # Bortle 9 base SQM is approx 18.0
             assert sqm < 18.0

def test_get_seeing_with_weather_penalty(place):
    dt = datetime(2024, 1, 1, 0, 0, tzinfo=timezone.utc)
    weather_data = pd.DataFrame({
        "time": [dt],
        "cloudCover": [60],
        "windSpeed": [30], # Penalty: (30-15)/50 = 0.3
        "humidity": [90]   # Penalty: (90-80)/40 = 0.25
    })
    # Total penalty = 0.3 (wind) + 0.25 (humidity) + 0.3 (clouds) = 0.85
    # Seeing = 1.5 + 0.85 = 2.35

    place.weather = MagicMock()
    place.weather.data = weather_data

    with patch.object(place, '_get_scalar_datetime', return_value=dt):
        seeing = place.get_seeing(time=place.ts.utc(dt))
        assert seeing == pytest.approx(2.35)
