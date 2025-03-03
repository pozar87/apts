import pytest
import json
import requests_mock
from . import setup_place

def test_weather_successful_request():
  mock_response = {
    "hourly": {
      "data": [
        {
          "time": 1624000000,
          "summary": "Clear",
          "temperature": 20,
          "cloudCover": 0.1,
          "precipProbability": 0.2,
          "windSpeed": 5,
          "pressure": 1013,
          "visibility": 10,
          "ozone": 300
        }
      ]
    }
  }

  with requests_mock.Mocker() as m:
    m.get(requests_mock.ANY, json=mock_response)

    p = setup_place()
    p.get_weather()

    # Verify weather object was created
    assert p.weather is not None

    # Verify data was processed correctly
    weather_data = p.weather.data
    assert not weather_data.empty
    assert weather_data['temperature'].iloc[0] == 20
    assert weather_data['cloudCover'].iloc[0] == 10  # 0.1 * 100
    assert weather_data['precipProbability'].iloc[0] == 20  # 0.2 * 100

def test_weather_api_error():
  with requests_mock.Mocker() as m:
    m.get(requests_mock.ANY, status_code=500)

    p = setup_place()
    with pytest.raises(json.decoder.JSONDecodeError):
      p.get_weather()
