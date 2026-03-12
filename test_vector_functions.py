from skyfield.api import Topos, load
from skyfield import vector_functions

eph = load('de421.bsp')
observer = eph['earth'] + Topos(latitude_degrees=52.2297, longitude_degrees=21.0122, elevation_m=100)
data = vector_functions.extract_observer_data(observer)
print(data)
