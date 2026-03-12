import sys
import os
from datetime import datetime, timezone

# Add repo root to sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from apts.place import Place

def test_timezone_offset():
    # Test Warsaw (CET/CEST)
    warsaw = Place(52.2297, 21.0122, name="Warsaw")

    # Winter time (UTC+1)
    winter_date = datetime(2025, 1, 1, tzinfo=timezone.utc)
    warsaw_tz = warsaw.local_timezone
    # local_timezone is a dateutil.tz object
    winter_offset_delta = winter_date.astimezone(warsaw_tz).utcoffset()
    assert winter_offset_delta is not None
    winter_offset = winter_offset_delta.total_seconds() / 3600
    print(f"Warsaw Winter Offset: {winter_offset} (Expected: 1.0)")
    assert winter_offset == 1.0

    # Summer time (UTC+2)
    summer_date = datetime(2025, 7, 1, tzinfo=timezone.utc)
    summer_offset_delta = summer_date.astimezone(warsaw_tz).utcoffset()
    assert summer_offset_delta is not None
    summer_offset = summer_offset_delta.total_seconds() / 3600
    print(f"Warsaw Summer Offset: {summer_offset} (Expected: 2.0)")
    assert summer_offset == 2.0

    # Test New York (EST/EDT)
    nyc = Place(40.7128, -74.0060, name="New York")
    nyc_tz = nyc.local_timezone

    # Winter time (UTC-5)
    winter_offset_nyc_delta = winter_date.astimezone(nyc_tz).utcoffset()
    assert winter_offset_nyc_delta is not None
    winter_offset_nyc = winter_offset_nyc_delta.total_seconds() / 3600
    print(f"NYC Winter Offset: {winter_offset_nyc} (Expected: -5.0)")
    assert winter_offset_nyc == -5.0

    print("Timezone offset tests passed!")

if __name__ == "__main__":
    test_timezone_offset()
