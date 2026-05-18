import time
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
from apts.observations.base import Observation
from apts.place.base import Place
from apts.equipment.base import Equipment
from apts.conditions import Conditions
import unittest.mock

def run_benchmark():
    # Setup
    lat, lon = 52.2297, 21.0122
    place = Place(lat, lon, "Warsaw")
    equipment = Equipment() # Dummy equipment
    conditions = Conditions()

    # Ensure some conditions are set
    conditions.max_clouds = 50
    conditions.min_visibility = 10
    conditions.max_fog = 20
    conditions.max_precipitation_probability = 30
    conditions.max_precipitation_intensity = 0.5
    conditions.max_wind = 20
    conditions.min_temperature = 0
    conditions.max_temperature = 25

    # Create an observation with a very long window to simulate many hours
    ts = place.ts
    from pytz import UTC
    start_time = datetime(2025, 1, 1, 12, 0, 0, tzinfo=UTC)
    end_time = start_time + timedelta(hours=10000)
    # Important: Observation class expects datetime objects for start/stop,
    # but uses Skyfield Time for effective_date.
    obs = Observation(place, equipment, conditions, sun_observation=True, start_time=start_time, end_time=end_time)
    # Fix effective_date to be a Skyfield Time object to avoid ValueError in moon illumination
    obs.effective_date = ts.utc(start_time)

    # Mock weather data - 10000 hours
    row_count = 10000
    # Start date matching observation start
    start_date = start_time
    times = [start_date + timedelta(hours=i) for i in range(row_count)]

    data = {
        "time": times,
        "cloudCover": np.random.uniform(0, 100, row_count),
        "visibility": np.random.uniform(0, 20, row_count),
        "fog": np.random.uniform(0, 100, row_count),
        "precipProbability": np.random.uniform(0, 100, row_count),
        "precipIntensity": np.random.uniform(0, 5, row_count),
        "windSpeed": np.random.uniform(0, 50, row_count),
        "temperature": np.random.uniform(-10, 30, row_count),
        "moonIllumination": np.random.uniform(0, 100, row_count),
        "seeing": np.random.uniform(0, 5, row_count),
        "sqm": np.random.uniform(16, 22, row_count),
        "aurora": np.random.uniform(0, 100, row_count),
        "Altitude": np.random.uniform(-90, 90, row_count)
    }

    df = pd.DataFrame(data)

    # Mock place.weather
    mock_weather = unittest.mock.MagicMock()
    # We need to ensure get_critical_data returns the right subset if called with start/stop

    def get_critical_data_side_effect(start, stop):
        return df[(df.time >= start) & (df.time <= stop)]

    mock_weather.get_critical_data.side_effect = get_critical_data_side_effect
    place.weather = mock_weather

    # Warm up
    # Clear cache to force recalculation
    obs._weather_analysis = None
    obs.get_weather_analysis()

    print(f"Running benchmark on {row_count} rows...")
    iterations = 50
    start_time = time.perf_counter()
    for _ in range(iterations):
        obs._weather_analysis = None
        result = obs.get_weather_analysis()
    end_time = time.perf_counter()

    duration = end_time - start_time
    avg_duration = duration / iterations
    print(f"Average execution time: {avg_duration:.6f} seconds")

if __name__ == "__main__":
    run_benchmark()
