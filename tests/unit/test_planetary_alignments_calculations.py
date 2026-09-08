from datetime import datetime, timezone
import numpy as np
from apts.skyfield_searches.planets.calculations import (
    aggregate_alignment_daily_results,
    calculate_alignment_step_results,
    format_alignment_events,
    get_best_alignment_at_time,
)


class MockTime:
    def __init__(self, dt):
        self._dt = dt

    def utc_datetime(self):
        return self._dt


def test_get_best_alignment_at_time_tight_cluster():
    # Longitudes for 7 planets: 3 aligned closely at 10, 15, 20 degrees
    lons = np.array([10.0, 15.0, 20.0, 100.0, 180.0, 250.0, 310.0])
    k, arc, indices = get_best_alignment_at_time(lons)

    assert k == 3
    assert np.isclose(arc, 10.0)
    assert set(indices) == {0, 1, 2}


def test_get_best_alignment_at_time_no_alignment():
    # Longitudes evenly spaced around 360 degrees (approx 51 deg apart)
    lons = np.array([0.0, 52.0, 104.0, 156.0, 208.0, 260.0, 312.0])
    k, arc, indices = get_best_alignment_at_time(lons)

    assert k == 0
    assert arc == 360.0
    assert indices == []


def test_get_best_alignment_at_time_wrap_around():
    # Longitudes wrapping around 0/360 boundary (355, 359, 5) -> arc of 10 degrees
    lons = np.array([355.0, 359.0, 5.0, 90.0, 150.0, 220.0, 280.0])
    k, arc, indices = get_best_alignment_at_time(lons)

    assert k == 3
    assert np.isclose(arc, 10.0)
    assert set(indices) == {0, 1, 2}


def test_calculate_alignment_step_results():
    times = [MockTime(datetime(2025, 3, 1, 1, 0, tzinfo=timezone.utc))]
    longitudes = np.array([[10.0], [15.0], [20.0], [100.0], [180.0], [250.0], [310.0]])
    altitudes = np.array([[15.0], [20.0], [25.0], [-10.0], [-5.0], [-20.0], [-15.0]])
    is_dark = np.array([True])

    results = calculate_alignment_step_results(
        times, longitudes, altitudes, is_dark
    )

    assert len(results) == 1
    step = results[0]
    assert step["k"] == 3
    assert step["num_visible"] == 3
    assert step["visible_indices"] == [0, 1, 2]


def test_aggregate_alignment_daily_results():
    dt1 = datetime(2025, 3, 1, 1, 0, tzinfo=timezone.utc)
    dt2 = datetime(2025, 3, 1, 2, 0, tzinfo=timezone.utc)
    times = [MockTime(dt1), MockTime(dt2)]

    step_results = [
        {"k": 3, "arc": 12.0, "num_visible": 2, "indices": [0, 1, 2]},
        {"k": 3, "arc": 10.0, "num_visible": 3, "indices": [0, 1, 2]},
    ]

    daily = aggregate_alignment_daily_results(times, step_results)
    assert len(daily) == 1
    best_time, best_res = daily[0]
    assert best_time.utc_datetime() == dt2
    assert best_res["num_visible"] == 3
    assert best_res["arc"] == 10.0


def test_format_alignment_events():
    dt = datetime(2025, 3, 1, 2, 0, tzinfo=timezone.utc)
    daily_results = [
        (
            MockTime(dt),
            {
                "k": 3,
                "arc": 10.0,
                "indices": [0, 1, 2],
                "num_visible": 3,
                "visible_indices": [0, 1, 2],
            },
        )
    ]
    planets = [
        "mercury",
        "venus",
        "mars barycenter",
        "jupiter barycenter",
        "saturn barycenter",
        "uranus barycenter",
        "neptune barycenter",
    ]

    events = format_alignment_events(daily_results, planets)
    assert len(events) == 1
    ev = events[0]
    assert ev["date"] == dt
    assert ev["num_visible"] == 3
    assert ev["planets"] == ["Mercury", "Venus", "Mars"]
    assert "Alignment of 3 planets" in ev["event"]
