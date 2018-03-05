import urllib.request
import json
import pandas as pd

from datetime import datetime, timedelta


class Weather:

  API_KEY = ""
  API_URL = ""

  def __init__(self, lat, lon, local_timezone):
    self.lat = lat
    self.lon = lon
    self.local_timezone = local_timezone
    self.data = self.download_data()

  def _filter_data(self, rows, hours):
    # Always add time column
    columns = ["time"] + rows
    # Calculate time horizon base on number of hours (max is 48h as longer predictions are inacurate)
    time_horizon = datetime.now() + timedelta(hours=min(hours, 48))
    return self.data[columns][self.data.time < time_horizon]

  def plot_clouds(self, hours=24, **args):
    data = self._filter_data(["cloudCover"], hours)
    plt = data.plot(x="time", ylim=(0, 1.05), title="Clouds", **args)
    return plt

  def plot_precipitation(self, hours=24, **args):
    data = self._filter_data(
        ["precipIntensity", "precipProbability"], hours)
    plt = data.plot(
        x="time", title="precipitation intensity and probability", **args)
    return plt

  def plot_precipitation_type_summary(self, hours=24, **args):
    data = self._filter_data(["precipType"], hours)
    plt = data.groupby('precipType').size().plot(
        kind='pie', label="precipitation type summary", **args)
    return plt

  def plot_clouds_summary(self, hours=24, **args):
    data = self._filter_data(["summary"], hours)
    plt = data.groupby('summary').size().plot(
        kind='pie', label="Cloud summary", **args)
    return plt

  def plot_temperature(self, hours=24, **args):
    data = self._filter_data(
        ["temperature", "apparentTemperature", "dewPoint"], hours)
    plt = data.plot(x="time", title="Temperatures", **args)
    return plt

  def plot_wind(self, hours=24, **args):
    max_wind_speed = self.data[["windSpeed"]].max().max()
    data = self._filter_data(["windSpeed"], hours)
    plt = data.plot(x="time", y="windSpeed", ylim=(
        0, max_wind_speed + 1), title="Wind speed", **args)
    return plt

  def plot_pressure_and_ozone(self,  hours=24, **args):
    data = self._filter_data(["pressure", "ozone"], hours)
    plt = data.plot(x="time", title="Pressure and Ozone",
                    secondary_y=['ozone'],  **args)
    return plt

  def get_critical_data(self, start, stop):
    data = self._filter_data(
        ["cloudCover", "precipProbability", "windSpeed", "temperature"], hours=24)
    return data[(data.time > start) & (data.time < stop)]

  def plot_visibility(self, hours=24, **args):
    data = self._filter_data(["visibility"], hours)
    plt = data[data.visibility != 'none'].plot(
        x="time", title="Visibility", **args)
    return plt

  def download_data(self):
    #print(Weather.API_URL.format(Weather.API_KEY, self.lat, self.lon))
    with urllib.request.urlopen(Weather.API_URL.format(Weather.API_KEY, self.lat, self.lon)) as url:
      columns = ["time",
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
                 "ozone"]
      json_data = json.loads(url.read().decode())
      raw_data = [[(item[column] if column in item.keys() else 'none')
                   for column in columns] for item in json_data["hourly"]["data"]]
      result = pd.DataFrame(raw_data, columns=columns)
      result.time = result.time.astype('datetime64[s]').dt.tz_localize(
          'UTC').dt.tz_convert(self.local_timezone)
      #result.time = result.time.astype('datetime64[s]')
      return result
