import urllib.request, json
import pandas as pd


class Weather:

  API_URL = "https://api.darksky.net/forecast/<api>/{},{}?units=si"

  def __init__(self, lat, lon):
    self.lat = lat
    self.lon = lon
    self.data = self.get_data()
     
  def get_data(self):  
    with urllib.request.urlopen(Weather.API_URL.format(self.lat,self.lon)) as url:
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
