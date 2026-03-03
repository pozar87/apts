import pickle
import datetime
import pytest
import pandas as pd
from apts.place import Place
from apts.equipment import Equipment
from apts.observations import Observation
from apts.conditions import Conditions
from apts.objects.messier import Messier
from apts.catalogs import Catalogs

def test_messier_pickle_get_visible():
    # Setup
    place = Place(52.2297, 21.0122, "Warsaw")
    equipment = Equipment()
    conditions = Conditions()
    target_date = datetime.date(2026, 3, 3)
    
    obs = Observation(place, equipment, conditions, target_date=target_date)
    
    # Get local_messier
    lm = obs.local_messier
    
    # Verify skyfield_object is there
    assert "skyfield_object" in lm.objects.columns
    
    # Pickle and unpickle
    pickled_lm = pickle.dumps(lm)
    
    # Ensure registry is initialized for unpickling
    from apts.units import get_unit_registry
    from pint import set_application_registry
    set_application_registry(get_unit_registry())
    
    unpickled_lm = pickle.loads(pickled_lm)
    
    # Verify skyfield_object is GONE (as expected by Objects.__getstate__)
    assert "skyfield_object" not in unpickled_lm.objects.columns
    
    # Now try to get visible objects. This should NOT fail with 
    # AttributeError: 'Series' object has no attribute 'skyfield_object'
    # It should recreate the objects on the fly.
    try:
        visible = unpickled_lm.get_visible(
            conditions,
            obs.start,
            obs.stop
        )
        assert len(visible) >= 0
    except AttributeError as e:
        if "'Series' object has no attribute 'skyfield_object'" in str(e):
            pytest.fail(f"Bug reproduced: {e}")
        raise e

def test_stars_pickle_get_visible():
    place = Place(52.2297, 21.0122, "Warsaw")
    equipment = Equipment()
    conditions = Conditions()
    target_date = datetime.date(2026, 3, 3)
    obs = Observation(place, equipment, conditions, target_date=target_date)
    
    ls = obs.local_stars
    assert "skyfield_object" in ls.objects.columns
    
    pickled_ls = pickle.dumps(ls)
    from apts.units import get_unit_registry
    from pint import set_application_registry
    set_application_registry(get_unit_registry())
    unpickled_ls = pickle.loads(pickled_ls)
    assert "skyfield_object" not in unpickled_ls.objects.columns
    
    # Should not fail
    visible = unpickled_ls.get_visible(conditions, obs.start, obs.stop)
    assert len(visible) >= 0

def test_ngc_pickle_get_visible():
    place = Place(52.2297, 21.0122, "Warsaw")
    equipment = Equipment()
    conditions = Conditions()
    target_date = datetime.date(2026, 3, 3)
    obs = Observation(place, equipment, conditions, target_date=target_date)
    
    ln = obs.local_ngc
    assert "skyfield_object" in ln.objects.columns
    
    pickled_ln = pickle.dumps(ln)
    from apts.units import get_unit_registry
    from pint import set_application_registry
    set_application_registry(get_unit_registry())
    unpickled_ln = pickle.loads(pickled_ln)
    assert "skyfield_object" not in unpickled_ln.objects.columns
    
    # Should not fail
    visible = unpickled_ln.get_visible(conditions, obs.start, obs.stop)
    assert len(visible) >= 0
