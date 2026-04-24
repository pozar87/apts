DEFAULT_WEATHER_VALUES = {
    "fog": 0,
    "aurora": 0,
    "precipIntensity": 0,
    "precipProbability": 0,
    "cloudCover": 0,
    "windSpeed": 0,
    "temperature": 20,
    "visibility": 20,
    "moonIllumination": 0,
    "seeing": 1.5,
    "sqm": 21.0,
}

RENAME_MAP = {
    "cloudCover": "clouds",
    "precipProbability": "precipitation",
    "precipIntensity": "precipitation_intensity",
    "windSpeed": "wind_speed",
    "moonIllumination": "moon_illumination",
}

FINAL_COLS = [
    "time",
    "is_good_hour",
    "reasons",
    "reason_keys",
    "temperature",
    "cloudCover",
    "precipProbability",
    "precipIntensity",
    "windSpeed",
    "visibility",
    "moonIllumination",
    "fog",
    "aurora",
    "seeing",
    "sqm",
]
