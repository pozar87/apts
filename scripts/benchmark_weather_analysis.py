import time
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
from apts.observations import Observation
from apts.place import Place
from apts.equipment import Equipment
from apts.conditions import Conditions
from unittest.mock import MagicMock

def benchmark():
    # Mock Place and Weather
    place = Place(name="Test", lat=50.0, lon=20.0)

    # Create a large dummy weather dataset
    num_hours = 1000
    from pytz import UTC
    start_time = datetime.now(UTC)
    times = [start_time + timedelta(hours=i) for i in range(num_hours)]

    weather_data = pd.DataFrame({
        'time': times,
        'cloudCover': np.random.uniform(0, 100, num_hours),
        'precipProbability': np.random.uniform(0, 100, num_hours),
        'precipIntensity': np.random.uniform(0, 10, num_hours),
        'windSpeed': np.random.uniform(0, 30, num_hours),
        'temperature': np.random.uniform(-10, 30, num_hours),
        'visibility': np.random.uniform(0, 20, num_hours),
        'moonIllumination': np.random.uniform(0, 100, num_hours),
        'fog': np.random.uniform(0, 100, num_hours),
        'aurora': np.random.uniform(0, 100, num_hours),
    })

    mock_weather = MagicMock()
    mock_weather.get_critical_data.return_value = weather_data
    mock_weather.local_timezone = place.local_timezone
    place.weather = mock_weather

    obs = Observation(place, Equipment())
    obs.start = times[0]
    obs.stop = times[-1]
    obs.time_limit = times[-1]

    # Run get_weather_analysis
    start_bench = time.time()
    for _ in range(10):
        obs.get_weather_analysis(force=True)
    end_bench = time.time()

    print(f"Average execution time for get_weather_analysis (1000 rows): {(end_bench - start_bench) / 10:.4f}s")

if __name__ == "__main__":
    benchmark()
