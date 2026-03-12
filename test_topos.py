from skyfield.api import Topos, load

eph = load('de421.bsp')
observer = eph['earth'] + Topos(latitude_degrees=52.2297, longitude_degrees=21.0122, elevation_m=100)
print(f"Observer: {observer}")
print(f"Topos: {observer.topos}")
print(f"Lat: {observer.topos.latitude.degrees}")
print(f"Lon: {observer.topos.longitude.degrees}")
