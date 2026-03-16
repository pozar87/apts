import time
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
from apts.weather_providers import Meteoblue
from apts.conditions import Conditions

def run_benchmark():
    # Setup
    lat, lon = 52.2297, 21.0122
    tz = "Europe/Warsaw"
    provider = Meteoblue("dummy_key", lat, lon, tz)

    # Create 1000 rows of weather data
    start_date = datetime(2025, 1, 1, tzinfo=datetime.now().astimezone().tzinfo)
    times = [start_date + timedelta(hours=i) for i in range(1000)]

    data = {
        "time": times,
        "cloudCover": np.random.uniform(0, 100, 1000),
        "visibility": np.random.uniform(0, 20, 1000),
        "fog": np.random.uniform(0, 100, 1000),
        "precipProbability": np.random.uniform(0, 100, 1000),
        "precipIntensity": np.random.uniform(0, 5, 1000),
        "windSpeed": np.random.uniform(0, 50, 1000),
        "temperature": np.random.uniform(-10, 30, 1000)
    }

    # Occasionally insert "none" and NaN
    df = pd.DataFrame(data)
    for col in df.columns:
        if col != "time":
            # Convert to object type to allow "none" string
            df[col] = df[col].astype(object)
            mask = np.random.choice([True, False], size=1000, p=[0.1, 0.9])
            df.loc[mask, col] = "none"
            mask = np.random.choice([True, False], size=1000, p=[0.05, 0.95])
            df.loc[mask, col] = np.nan

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

    observation_window = (times[0], times[-1])

    print(f"Running benchmark on {len(df)} rows...")
    start_time = time.perf_counter()
    result = provider._is_weather_good(df, conditions, observation_window)
    end_time = time.perf_counter()

    duration = end_time - start_time
    print(f"Benchmark result: {result}")
    print(f"Execution time: {duration:.4f} seconds")

if __name__ == "__main__":
    run_benchmark()
