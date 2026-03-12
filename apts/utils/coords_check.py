
from apts.cache import get_ephemeris, get_timescale
from apts.place import Place

def coords_check():
    ts = get_timescale()
    eph = get_ephemeris()
    earth = eph["earth"]

    # Observer in Warsaw
    place = Place(52.2297, 21.0122, elevation=110)
    observer = earth + place.location

    # Reference time: 2025-01-01 00:00:00 UTC
    t = ts.utc(2025, 1, 1, 0, 0, 0)

    # Check Moon position
    moon = eph["moon"]
    astrometric = observer.at(t).observe(moon)
    apparent = astrometric.apparent()

    ra, dec, distance = apparent.radec()
    alt, az, _ = apparent.altaz()

    print(f"Time: {t.utc_iso()}")
    print(f"Moon RA (apparent): {ra}")
    print(f"Moon Dec (apparent): {dec}")
    print(f"Moon Alt: {alt.degrees:.4f}°")
    print(f"Moon Az: {az.degrees:.4f}°")

    # Warsaw (52N, 21E) at 00:00 UTC on Jan 1st 2025:
    expected_alt = -63.7558
    expected_az = 10.5343

    print(f"Expected Alt: ~{expected_alt}°, Az: ~{expected_az}°")

    # Use 1 degree tolerance for rough check
    assert abs(alt.degrees - expected_alt) < 1.0
    assert abs(az.degrees - expected_az) < 1.0

    # Check Jupiter position
    jupiter = eph["jupiter barycenter"]
    astrometric_j = observer.at(t).observe(jupiter)
    apparent_j = astrometric_j.apparent()

    alt_j, az_j, _ = apparent_j.altaz()
    print(f"Jupiter Alt: {alt_j.degrees:.4f}°")
    print(f"Jupiter Az: {az_j.degrees:.4f}°")

    # Warsaw (52N, 21E) at 00:00 UTC (01:00 local) Jan 1st 2025.
    expected_alt_j = 41.2042
    expected_az_j = 251.0614

    print(f"Expected Jupiter Alt: ~{expected_alt_j}°, Az: ~{expected_az_j}°")

    assert abs(alt_j.degrees - expected_alt_j) < 1.0
    assert abs(az_j.degrees - expected_az_j) < 1.0

    print("Coordinate checks passed!")

if __name__ == "__main__":
    coords_check()
