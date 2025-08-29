import json
import logging
from abc import ABC, abstractmethod

import pandas as pd
import requests

logger = logging.getLogger(__name__)


class WeatherProvider(ABC):
    def __init__(self, api_key, lat, lon, local_timezone):
        self.api_key = api_key
        self.lat = lat
        self.lon = lon
        self.local_timezone = local_timezone

    @abstractmethod
    def download_data(self):
        pass


class PirateWeather(WeatherProvider):
    API_URL = "https://api.pirateweather.net/forecast/{apikey}/{lat},{lon}?units=si"

    def download_data(self):
        url = self.API_URL.format(apikey=self.api_key, lat=self.lat, lon=self.lon)
        logger.debug("Download weather from: {}".format(url))
        with requests.get(url) as data:
            logger.debug(f"Data {data}")
            columns = [
                "time",
                "summary",
                "precipType",
                "precipProbability",
                "precipIntensity",
                "temperature",
                "apparentTemperature",
                "dewPoint",
                "humidity",
                "windSpeed",
                "cloudCover",
                "visibility",
                "pressure",
                "ozone",
            ]
            json_data = json.loads(data.text)
            if "hourly" in json_data and "data" in json_data["hourly"]:
                raw_data = [
                    [
                        (item[column] if column in item.keys() else "none")
                        for column in columns
                    ]
                    for item in json_data["hourly"]["data"]
                ]
            else:
                logger.error(f"KeyError in weather data. Full response: {json_data}")
                return pd.DataFrame(columns=columns)
            result = pd.DataFrame(raw_data, columns=columns)
            # Convert units
            result["precipProbability"] *= 100
            result["cloudCover"] *= 100
            result.time = (
                result.time.astype("datetime64[s]")
                .dt.tz_localize("UTC")
                .dt.tz_convert(self.local_timezone)
            )
            return result


class VisualCrossing(WeatherProvider):
    API_URL = "https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/{lat},{lon}?unitGroup=metric&key={apikey}&include=hours"

    def download_data(self):
        url = self.API_URL.format(apikey=self.api_key, lat=self.lat, lon=self.lon)
        logger.debug("Download weather from: {}".format(url))
        with requests.get(url) as data:
            logger.debug(f"Data {data}")
            json_data = json.loads(data.text)

            if "days" not in json_data:
                logger.error(f"KeyError 'days' in weather data. Full response: {json_data}")
                return pd.DataFrame()

            all_hours_data = []
            for day in json_data['days']:
                all_hours_data.extend(day['hours'])

            df = pd.DataFrame(all_hours_data)

            # Rename columns to match the standard format
            rename_map = {
                'datetimeEpoch': 'time',
                'conditions': 'summary',
                'preciptype': 'precipType',
                'precipprob': 'precipProbability',
                'precip': 'precipIntensity',
                'temp': 'temperature',
                'feelslike': 'apparentTemperature',
                'dew': 'dewPoint',
                'humidity': 'humidity',
                'windspeed': 'windSpeed',
                'cloudcover': 'cloudCover',
                'visibility': 'visibility',
                'pressure': 'pressure',
                'ozone': 'ozone'
            }
            df.rename(columns=rename_map, inplace=True)

            # Convert units and types
            df['time'] = pd.to_datetime(df['time'], unit='s').dt.tz_localize('UTC').dt.tz_convert(self.local_timezone)
            if 'precipProbability' in df.columns:
                 df['precipProbability'] *= 100

            # Ensure all required columns are present
            required_columns = [
                "time", "summary", "precipType", "precipProbability", "precipIntensity",
                "temperature", "apparentTemperature", "dewPoint", "humidity",
                "windSpeed", "cloudCover", "visibility", "pressure", "ozone"
            ]
            for col in required_columns:
                if col not in df.columns:
                    df[col] = 'none' # or pd.NA

            return df[required_columns]


class Meteoblue(WeatherProvider):
    API_URL = "https://my.meteoblue.com/packages/basic-1h_agro-1h_clouds-1h_airquality-1h?lat={lat}&lon={lon}&apikey={apikey}&format=json"

    def download_data(self):
        url = self.API_URL.format(apikey=self.api_key, lat=self.lat, lon=self.lon)
        logger.debug("Download weather from: {}".format(url))
        with requests.get(url) as data:
            logger.debug(f"Data {data}")
            json_data = json.loads(data.text)

            if "data_1h" not in json_data:
                logger.error(f"KeyError 'data_1h' in weather data. Full response: {json_data}")
                return pd.DataFrame()

            df = pd.DataFrame(json_data['data_1h'])

            # Rename columns to match the standard format
            rename_map = {
                'time': 'time',
                'pictocode': 'summary',
                'snowfraction': 'precipType',
                'precipitation_probability': 'precipProbability',
                'precipitation': 'precipIntensity',
                'temperature': 'temperature',
                'felttemperature': 'apparentTemperature',
                'dewpointtemperature': 'dewPoint',
                'relativehumidity': 'humidity',
                'windspeed': 'windSpeed',
                'totalcloudcover': 'cloudCover',
                'visibility': 'visibility',
                'sealevelpressure': 'pressure',
                'ozone_concentration': 'ozone'
            }
            df.rename(columns=rename_map, inplace=True)

            # Convert units and types
            df['time'] = pd.to_datetime(df['time']).dt.tz_localize('UTC').dt.tz_convert(self.local_timezone)
            if 'precipType' in df.columns:
                df['precipType'] = df['precipType'].apply(lambda x: 'snow' if x > 0 else 'rain')

            if 'visibility' in df.columns:
                df['visibility'] /= 1000

            # Ensure all required columns are present
            required_columns = [
                "time", "summary", "precipType", "precipProbability", "precipIntensity",
                "temperature", "apparentTemperature", "dewPoint", "humidity",
                "windSpeed", "cloudCover", "visibility", "pressure", "ozone"
            ]
            for col in required_columns:
                if col not in df.columns:
                    df[col] = 'none'

            return df[required_columns]


class OpenWeatherMap(WeatherProvider):
    API_URL = "https://api.openweathermap.org/data/3.0/onecall?lat={lat}&lon={lon}&appid={apikey}&units=metric&exclude=minutely,daily,alerts"

    def download_data(self):
        url = self.API_URL.format(apikey=self.api_key, lat=self.lat, lon=self.lon)
        logger.debug("Download weather from: {}".format(url))
        with requests.get(url) as data:
            logger.debug(f"Data {data}")
            json_data = json.loads(data.text)

            if "hourly" not in json_data:
                logger.error(f"KeyError 'hourly' in weather data. Full response: {json_data}")
                return pd.DataFrame()

            df = pd.DataFrame(json_data['hourly'])

            # The 'weather' column contains a list with a dictionary, extract the description
            df['summary'] = df['weather'].apply(lambda x: x[0]['description'] if x else 'none')
            df['precipType'] = df['weather'].apply(lambda x: x[0]['main'] if x else 'none')

            # Rename columns to match the standard format
            rename_map = {
                'dt': 'time',
                'pop': 'precipProbability',
                'temp': 'temperature',
                'feels_like': 'apparentTemperature',
                'dew_point': 'dewPoint',
                'humidity': 'humidity',
                'wind_speed': 'windSpeed',
                'clouds': 'cloudCover',
                'visibility': 'visibility',
                'pressure': 'pressure',
            }
            df.rename(columns=rename_map, inplace=True)

            # precipIntensity
            if 'rain' in df.columns and isinstance(df['rain'].iloc[0], dict):
                df['precipIntensity'] = df['rain'].apply(lambda x: x.get('1h', 0) if isinstance(x, dict) else 0)
            elif 'snow' in df.columns and isinstance(df['snow'].iloc[0], dict):
                df['precipIntensity'] = df['snow'].apply(lambda x: x.get('1h', 0) if isinstance(x, dict) else 0)
            else:
                df['precipIntensity'] = 0

            # Convert units and types
            df['time'] = pd.to_datetime(df['time'], unit='s').dt.tz_localize('UTC').dt.tz_convert(self.local_timezone)
            if 'precipProbability' in df.columns:
                df['precipProbability'] *= 100

            if 'humidity' in df.columns:
                df['humidity'] /= 100

            # Convert wind speed from m/s to km/h
            if 'windSpeed' in df.columns:
                df['windSpeed'] *= 3.6

            # Convert visibility from meters to km
            if 'visibility' in df.columns:
                df['visibility'] /= 1000

            # Ensure all required columns are present
            required_columns = [
                "time", "summary", "precipType", "precipProbability", "precipIntensity",
                "temperature", "apparentTemperature", "dewPoint", "humidity",
                "windSpeed", "cloudCover", "visibility", "pressure", "ozone"
            ]
            for col in required_columns:
                if col not in df.columns:
                    df[col] = 'none'

            return df[required_columns]
