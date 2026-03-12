from skyfield.api import Topos, load

eph = load('de421.bsp')
observer = eph['earth'] + Topos(latitude_degrees=52.2297, longitude_degrees=21.0122, elevation_m=100)
for segment in observer.vector_sum:
    print(f"Segment: {segment}")
    if hasattr(segment, 'latitude'):
        print(f"  Lat: {segment.latitude.degrees}")
    if hasattr(segment, 'longitude'):
        print(f"  Lon: {segment.longitude.degrees}")
