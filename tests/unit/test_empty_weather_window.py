"""Regression tests for the empty weather-analysis window.

``is_weather_good(force=True)`` used to divide by ``len(analysis)`` without
checking that any hours had been analysed. An empty window raised
``ZeroDivisionError``, which aborted the caller's whole notification for that
observation (observed in stargazer.earth production as
``Error processing observation 593: division by zero``).
"""

from unittest.mock import MagicMock

import pytest

from apts.observations.weather.base import WeatherAnalysisMixIn


def _make_weather(analysis):
    weather = WeatherAnalysisMixIn.__new__(WeatherAnalysisMixIn)
    weather._weather_analysis = None
    weather.start = None
    weather.stop = None
    weather.conditions = MagicMock(min_weather_goodness=50.0)
    weather.place = MagicMock()
    weather.place.weather = None
    weather.get_weather_analysis = MagicMock(return_value=analysis)
    return weather


def test_empty_analysis_returns_false_instead_of_raising():
    weather = _make_weather([])
    assert weather.is_weather_good(force=True) is False


def test_empty_analysis_does_not_raise_zero_division():
    weather = _make_weather([])
    try:
        weather.is_weather_good(force=True)
    except ZeroDivisionError:  # pragma: no cover - the regression itself
        pytest.fail("is_weather_good(force=True) raised ZeroDivisionError on an empty window")


def test_all_good_hours_passes_the_threshold():
    analysis = [{"is_good_hour": True}, {"is_good_hour": True}]
    weather = _make_weather(analysis)
    assert weather.is_weather_good(force=True) is True


def test_half_good_hours_meets_a_fifty_percent_threshold():
    analysis = [{"is_good_hour": True}, {"is_good_hour": False}]
    weather = _make_weather(analysis)
    assert weather.is_weather_good(force=True) is True


def test_no_good_hours_fails_the_threshold():
    analysis = [{"is_good_hour": False}, {"is_good_hour": False}]
    weather = _make_weather(analysis)
    assert weather.is_weather_good(force=True) is False
