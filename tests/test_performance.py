import time
import pytest
from datetime import datetime, date
from apts.place import Place
from apts.equipment import Equipment
from apts.observations import Observation
from apts.conditions import Conditions

def test_observation_creation_performance():
    # Setup
    place = Place(52.2297, 21.0122, "Warsaw")
    equipment = Equipment()
    conditions = Conditions()
    target_date = date(2023, 10, 27)

    # First one might be slower due to initial loading/caching
    Observation(place, equipment, conditions, target_date=target_date)

    start_time = time.perf_counter()
    for _ in range(50):
        Observation(place, equipment, conditions, target_date=target_date)
    end_time = time.perf_counter()

    total_time = end_time - start_time
    avg_time = total_time / 50

    print(f"Total time for 50 observations: {total_time:.4f}s")
    print(f"Average time: {avg_time:.4f}s")

    # Assert that average time is less than 0.05s (it was ~0.12s before optimization)
    # Actually with caching it should be much faster.
    assert avg_time < 0.05

def test_observation_correctness_after_optimization():
    place = Place(52.2297, 21.0122, "Warsaw")
    equipment = Equipment()
    conditions = Conditions()
    target_date = date(2023, 10, 27)

    obs1 = Observation(place, equipment, conditions, target_date=target_date)

    # Re-create should give same results from cache
    obs2 = Observation(place, equipment, conditions, target_date=target_date)

    assert obs1.start == obs2.start
    assert obs1.stop == obs2.stop
    assert obs1.start is not None
    assert obs1.stop is not None

    # Different date should give different result
    target_date2 = date(2023, 10, 28)
    obs3 = Observation(place, equipment, conditions, target_date=target_date2)
    assert obs3.start != obs1.start
