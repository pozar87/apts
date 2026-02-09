import pytest
import datetime
import pytz
from unittest.mock import MagicMock
from apts.observations import Observation
from apts.plotting.utils import mark_observation
from . import setup_place

def test_mark_observation_sun_and_moon_spans():
    place = setup_place()
    # Mock observation
    obs = MagicMock(spec=Observation)
    obs.place = place
    # Range covering a full day to ensure transitions are caught
    obs.start = datetime.datetime(2023, 6, 1, 12, 0, tzinfo=pytz.utc)
    obs.time_limit = datetime.datetime(2023, 6, 2, 12, 0, tzinfo=pytz.utc)

    mock_ax = MagicMock()
    # Mock xlim to match our observation range
    import matplotlib.dates as mdates
    x_min = mdates.date2num(obs.start)
    x_max = mdates.date2num(obs.time_limit)
    mock_ax.get_xlim.return_value = (x_min, x_max)

    style = {
        "GRID_COLOR": "gray",
        "AXIS_COLOR": "black",
        "SPAN_BACKGROUND_COLOR": "blue", # Night
        "DAY_SPAN_COLOR": "yellow",      # Day
        "MOON_SPAN_COLOR": "purple"      # Moon
    }

    mark_observation(obs, mock_ax, False, style)

    vspan_calls = mock_ax.axvspan.call_args_list

    # We expect several spans covering the whole range for Sun (Day/Night)
    sun_spans = [c for c in vspan_calls if c[1].get('color') in ['blue', 'yellow']]
    moon_spans = [c for c in vspan_calls if c[1].get('color') == 'purple']

    assert len(sun_spans) >= 2, "Should have at least two Sun spans (e.g. Day then Night)"
    assert len(moon_spans) >= 1, "Should have at least one Moon span"

    # Verify Sun spans are contiguous
    sun_spans.sort(key=lambda x: x[0][0])
    for i in range(len(sun_spans) - 1):
        # End of span i should be close to start of span i+1
        diff = abs((sun_spans[i+1][0][0] - sun_spans[i][0][1]).total_seconds())
        assert diff < 1.0

    # Verify first and last Sun spans match plot limits
    start_date = mdates.num2date(x_min).astimezone(place.local_timezone)
    end_date = mdates.num2date(x_max).astimezone(place.local_timezone)
    assert abs((sun_spans[0][0][0] - start_date).total_seconds()) < 1.0
    assert abs((sun_spans[-1][0][1] - end_date).total_seconds()) < 1.0

    # Check for observation start/stop lines
    vline_calls = mock_ax.axvline.call_args_list
    assert any(c[1].get('linestyle') == '--' for c in vline_calls)
