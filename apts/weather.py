import urllib.request, json
import pandas as pd


class Weather:

  API_KEY = ""
  API_URL = "https://api.darksky.net/forecast/{}/{},{}?units=si"

  def __init__(self, lat, lon):
    self.lat = lat
    self.lon = lon
    self.data = self.get_data()
     
  def plot_clouds(self, **args):
    plt = self.data[["cloudCover"]].plot(ylim=(0, 1), **args)
    return plt 
  
  def plot_temperature(self, **args):
    plt = self.data[["temperature","dewPoint","apparentTemperature"]].plot(**args)
    return plt 
    
  def plot_wind(self, **args):
    plt = self.data[["windSpeed"]].plot(**args)
    return plt    
  
  def plot_pressure(self, **args):
    plt = self.data[["pressure"]].plot(**args)
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
      raw_data = [[item[column] for column in columns] for item in json_data["hourly"]["data"]]
      return pd.DataFrame(raw_data, columns=columns)
