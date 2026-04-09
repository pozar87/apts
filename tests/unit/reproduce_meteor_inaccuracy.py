import unittest
from datetime import datetime, timezone
from apts.place import Place
from apts.skyfield_searches.meteor_showers import find_meteor_showers
from skyfield.api import Star

class TestMeteorInaccuracy(unittest.TestCase):
    def test_perseids_radiant_drift(self):
        # Perseids 2024 peak is approx Aug 12.
        # Start is July 17.
        p = Place(52.0, 20.0)
        start_date = datetime(2024, 7, 18, tzinfo=timezone.utc)
        end_date = datetime(2024, 7, 20, tzinfo=timezone.utc)

        events = find_meteor_showers(p.observer, start_date, end_date)

        perseids_start = [e for e in events if e['shower_name'] == 'Perseids' and e['phase'] == 'Start']
        if not perseids_start:
            print("Perseids start not found in range")
            return

        # The current implementation doesn't return radiant info for Start/End, only for Peak.
        # But wait, find_meteor_showers in meteor_showers.py only calculates radiant altitude at peak.
        # It uses a FIXED radiant for each shower in the 'showers' dict.

        # Let's check the Peak of Perseids.
        start_date = datetime(2024, 8, 1, tzinfo=timezone.utc)
        end_date = datetime(2024, 8, 31, tzinfo=timezone.utc)
        events = find_meteor_showers(p.observer, start_date, end_date)
        perseids_peak = [e for e in events if e['shower_name'] == 'Perseids' and e['phase'] == 'Peak']

        if perseids_peak:
            peak = perseids_peak[0]
            print(f"Perseids Peak: {peak['date']}, Altitude: {peak['altitude']}")
            # Currently it uses (3.1, 58.0)

        # If I change the peak date to some other year, it still uses (3.1, 58.0).
        # Which is fine for the peak, but if the peak longitude was slightly different...
        # More importantly, if we wanted to know the radiant position at start/end of the shower.

if __name__ == "__main__":
    unittest.main()
