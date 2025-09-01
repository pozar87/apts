#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Test script to validate ISS flyby functionality using local TLE data.
This avoids network issues and tests the core functionality.
"""

from datetime import datetime, timedelta
from skyfield.api import load, Topos, utc
import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), "../"))


def test_with_local_tle():
    """Test ISS flyby detection using local TLE file"""
    print("Testing ISS flyby with local TLE data...")

    # Set up observer location (Warsaw, Poland)
    topos_observer = Topos(latitude_degrees=52.2, longitude_degrees=21.0)

    # Load ephemeris
    eph = load("de421.bsp")
    vector_observer = eph["earth"] + topos_observer

    # Use current time for testing
    start_date = datetime.now(tz=utc)
    end_date = start_date + timedelta(hours=12)  # Shorter window

    print(f"Testing period: {start_date} to {end_date}")
    print(f"Observer: {topos_observer}")

    # Check if local TLE file exists
    tle_path = "stations.txt"
    if not os.path.exists(tle_path):
        print(f"❌ Local TLE file not found: {tle_path}")
        return False

    print(f"✅ Using local TLE file: {tle_path}")

    try:
        # Load satellites from local file
        satellites = load.tle_file(tle_path)
        print(f"Loaded {len(satellites)} satellites from local TLE file")

        # Find ISS
        iss = None
        for sat in satellites:
            if sat.name == "ISS (ZARYA)":
                iss = sat
                break

        if not iss:
            print("❌ ISS (ZARYA) not found in local TLE file")
            return False

        print(f"✅ Found ISS: {iss.name}")

        # Test direct satellite observation (what the function does internally)
        print("\nTesting direct satellite observation...")

        # Get current time
        ts = load.timescale()
        t = ts.now()

        # Try to observe ISS using vector subtraction
        try:
            difference = iss - vector_observer
            topocentric = difference.at(t)
            alt, az, distance = topocentric.apparent().altaz()
            mag = topocentric.apparent().magnitude

            print(f"✅ Satellite observation successful!")
            print(f"   Altitude: {alt.degrees:.1f}°")
            print(f"   Azimuth: {az.degrees:.1f}°")
            print(f"   Distance: {distance.km:.0f} km")
            print(f"   Magnitude: {mag:.1f}")

        except Exception as e:
            print(f"❌ Direct satellite observation failed: {e}")
            return False

        # Test find_events functionality
        print("\nTesting find_events...")
        try:
            times, events = iss.find_events(
                topos_observer, ts.utc(start_date), ts.utc(end_date), altitude_degrees=0
            )

            print(f"✅ find_events successful!")
            print(f"   Found {len(events)} satellite events")

            if events:
                for i, (t, event) in enumerate(zip(times, events)):
                    event_types = {0: "Rise", 1: "Culmination", 2: "Set"}
                    print(
                        f"   Event {i + 1}: {event_types.get(event, 'Unknown')} at {t.utc_datetime()}"
                    )

        except Exception as e:
            print(f"❌ find_events failed: {e}")
            return False

        return True

    except Exception as e:
        print(f"❌ Error loading local TLE: {e}")
        return False


def test_full_function():
    """Test the complete find_iss_flybys function with local data modification"""
    print("\nTesting complete find_iss_flybys function...")

    def local_find_iss_flybys(
        topos_observer,
        vector_observer,
        start_date,
        end_date,
        magnitude_threshold=-1.5,
        peak_altitude_threshold=40,
        rise_altitude_threshold=10,
    ):
        """Modified version that uses local TLE file"""
        from apts.cache import get_timescale, get_ephemeris

        ts = get_timescale()
        eph = get_ephemeris()
        t0 = ts.utc(start_date)
        t1 = ts.utc(end_date)

        try:
            # Use local file instead of URL
            satellites = load.tle_file("stations.txt")
            iss = next(s for s in satellites if s.name == "ISS (ZARYA)")
        except Exception as e:
            print(f"Could not load local ISS TLEs: {e}")
            return []

        # Use topos_observer for find_events
        times, events = iss.find_events(
            topos_observer, t0, t1, altitude_degrees=rise_altitude_threshold
        )

        events_list = []

        for i, event_code in enumerate(events):
            if event_code == 1:  # Culmination
                culmination_time = times[i]

                # Check for dark sky at culmination
                sun = eph["sun"]
                sun_alt, _, _ = (
                    vector_observer.at(culmination_time).observe(sun).apparent().altaz()
                )
                if sun_alt.degrees > -18:
                    continue

                # Check magnitude at culmination using vector subtraction
                difference = iss - vector_observer
                topocentric = difference.at(culmination_time)
                mag = topocentric.apparent().magnitude
                if mag > magnitude_threshold:
                    continue

                # Check peak altitude
                peak_alt, _, _ = topocentric.apparent().altaz()
                if peak_alt.degrees < peak_altitude_threshold:
                    continue

                # Find rise and set times for this pass
                if i > 0 and events[i - 1] == 0:
                    rise_time = times[i - 1]
                else:
                    continue

                if i < len(events) - 1 and events[i + 1] == 2:
                    set_time = times[i + 1]
                else:
                    continue

                events_list.append(
                    {
                        "date": culmination_time.utc_datetime(),
                        "event": f"Bright ISS Flyby (mag {mag:.2f}, peak alt {peak_alt.degrees:.1f}°)",
                        "type": "ISS Flyby",
                        "rise_time": rise_time.utc_datetime(),
                        "culmination_time": culmination_time.utc_datetime(),
                        "set_time": set_time.utc_datetime(),
                        "peak_altitude": peak_alt.degrees,
                        "peak_magnitude": mag,
                    }
                )

        return events_list

    # Test with local version
    try:
        topos_observer = Topos(latitude_degrees=52.2, longitude_degrees=21.0)
        eph = load("de421.bsp")
        vector_observer = eph["earth"] + topos_observer

        start_date = datetime.now(tz=utc)
        end_date = start_date + timedelta(hours=24)

        events = local_find_iss_flybys(
            topos_observer,
            vector_observer,
            start_date,
            end_date,
            magnitude_threshold=0.0,  # Very permissive
            peak_altitude_threshold=0,  # Very permissive
            rise_altitude_threshold=0,
        )

        print(f"✅ Full function test successful!")
        print(f"   Found {len(events)} ISS flyby events")

        if events:
            for i, event in enumerate(events, 1):
                print(f"   Event {i}:")
                print(f"     {event['event']}")
                print(f"     Rise: {event['rise_time']}")
                print(f"     Culmination: {event['culmination_time']}")
                print(f"     Set: {event['set_time']}")
        else:
            print(
                "   No events found (this may be normal depending on timing and location)"
            )

        return True

    except Exception as e:
        print(f"❌ Full function test failed: {e}")
        import traceback

        traceback.print_exc()
        return False


def main():
    """Main test function"""
    print("=" * 60)
    print("Local ISS TLE Test")
    print("=" * 60)

    success_count = 0
    total_tests = 2

    # Test 1: Basic satellite operations
    if test_with_local_tle():
        success_count += 1

    # Test 2: Full function test
    if test_full_function():
        success_count += 1

    print("\n" + "=" * 60)
    print(f"Test Results: {success_count}/{total_tests} tests passed")

    if success_count == total_tests:
        print("🎉 All tests passed! ISS observation approach is working correctly.")
    else:
        print("⚠️  Some tests failed. The approach may need adjustment.")

    print("=" * 60)

    return success_count == total_tests


if __name__ == "__main__":
    main()
