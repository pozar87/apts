import pytest
from datetime import datetime
import pytz
from apts.place import Place
from apts.equipment import Equipment
from apts.conditions import Conditions
from apts.observations import Observation
from apts.plotting.utils import get_object_angular_size_deg
from apts.i18n import language_context


@pytest.fixture
def mock_observation():
    place = Place(lat=52.0, lon=21.0, elevation=100, name="Warsaw")
    equipment = Equipment()
    target_date = datetime(2023, 11, 1, 22, 0, tzinfo=pytz.UTC)
    conditions = Conditions()
    observation = Observation(
        place=place, equipment=equipment, conditions=conditions, target_date=target_date
    )
    return observation


def test_get_object_angular_size_deg_i18n(mock_observation):
    # Test English context
    with language_context("en"):
        size_en = get_object_angular_size_deg(mock_observation, "Jupiter")
        assert size_en > 0
        assert abs(size_en * 3600 - 49.4) < 1.0  # Jupiter is around 49 arcsec

    # Test Polish context
    with language_context("pl"):
        # Even if we pass "Jupiter" (English name), it should work because of technical name matching
        size_pl = get_object_angular_size_deg(mock_observation, "Jupiter")
        assert size_pl == size_en

        # Test with Polish name
        size_pl_translated = get_object_angular_size_deg(mock_observation, "Jowisz")
        assert size_pl_translated == size_en
