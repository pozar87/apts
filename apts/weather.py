import urllib.request, json
import pandas as pd

class Weather:

  API_KEY = ""
  API_URL = "https://api.darksky.net/forecast/{}/{},{}?units=si"

  def __init__(self, lat, lon):
    self.lat = lat
    self.lon = lon
    self.data = self.get_data()
    self.local_timezone = ""
     
  def plot_clouds(self, **args):
    plt = self.data.plot(x = "time", y = "cloudCover", ylim=(0, 1.05), title="Clouds", **args)
    return plt 
  
  def plot_temperature(self, **args):
    plt = self.data[["time","temperature","apparentTemperature","dewPoint"]].plot(x = "time", title="Temperatures", **args)
    return plt 
    
  def plot_wind(self, **args):
    max_wind_speed = self.data[["windSpeed"]].max().max()
    plt = self.data.plot(x = "time", y = "windSpeed", ylim=(0, max_wind_speed  + 1), title="Wind speed", **args)
    return plt    
  
  def plot_pressure_and_ozone(self, **args):
    plt = self.data[["time","pressure","ozone"]].plot(x = "time", title="Pressure and Ozon", secondary_y=['ozone'],  **args)
    return plt  
  
  def get_data(self):  
    #print(Weather.API_URL.format(Weather.API_KEY, self.lat, self.lon))
    with urllib.request.urlopen(Weather.API_URL.format(Weather.API_KEY, self.lat, self.lon)) as url:
      columns = ["time",
                 "summary",
                 "summary",
                 #"precipType",
                 "precipProbability",
                 "precipIntensity",
                 "temperature",
                 "apparentTemperature",
                 "dewPoint",
                 "humidity",
                 "windSpeed",
                 "cloudCover",
                 "pressure",
                 "ozone"]
      json_data = json.loads(url.read().decode())
      self.local_timezone = json_data["timezone"]
      raw_data = [[item[column] for column in columns] for item in json_data["hourly"]["data"]]
      result = pd.DataFrame(raw_data, columns=columns)
      result.time = result.time.astype('datetime64[s]').dt.tz_localize('UTC').dt.tz_convert(self.local_timezone)
      return result
