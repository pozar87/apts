import pytest
from datetime import datetime, timezone, timedelta
from apts.skyfield_searches import find_conjunctions_with_stars
from apts.place import Place
from apts.cache import get_timescale, get_ephemeris
from skyfield.api import Star

def test_conjunction_precision_is_local_minimum():
    place = Place(52.2297, 21.0122, name="Warsaw")
    ts = get_timescale()
    eph = get_ephemeris()
    # Regulus
    regulus = Star(ra_hours=(10, 8, 22.3), dec_degrees=(11, 58, 2))

    start_date = datetime(2024, 1, 1, 0, 0, tzinfo=timezone.utc)
    end_date = datetime(2024, 2, 1, 0, 0, tzinfo=timezone.utc)

    conjs = find_conjunctions_with_stars(
        place.observer,
        "moon",
        [("Regulus", regulus)],
        start_date,
        end_date,
        threshold_degrees=10.0
    )

    assert len(conjs) > 0

    for c in conjs:
        t_center = ts.from_datetime(c['date'])

        def get_sep(t):
            m = place.observer.at(t).observe(eph['moon']).apparent(deflectors=())
            s = place.observer.at(t).observe(regulus).apparent(deflectors=())
            return m.separation_from(s).degrees

        sep_center = get_sep(t_center)

        # Check +/- 1 second and +/- 1 minute
        for delta_sec in [1, 60]:
            t_minus = ts.utc(t_center.utc[0], t_center.utc[1], t_center.utc[2], t_center.utc[3], t_center.utc[4], t_center.utc[5] - delta_sec)
            t_plus = ts.utc(t_center.utc[0], t_center.utc[1], t_center.utc[2], t_center.utc[3], t_center.utc[4], t_center.utc[5] + delta_sec)

            sep_minus = get_sep(t_minus)
            sep_plus = get_sep(t_plus)

            # It should be a minimum, so center should be less than or equal to its neighbors
            # Allowing for very tiny floating point jitter
            assert sep_center <= sep_minus + 1e-9
            assert sep_center <= sep_plus + 1e-9

def test_conjunction_between_moving_bodies_precision():
    place = Place(52.2297, 21.0122, name="Warsaw")
    ts = get_timescale()
    eph = get_ephemeris()

    from apts.skyfield_searches import find_conjunctions_between_moving_bodies
    from apts.utils import planetary

    start_date = datetime(2024, 1, 1, 0, 0, tzinfo=timezone.utc)
    end_date = datetime(2024, 2, 1, 0, 0, tzinfo=timezone.utc)

    # Moon-Jupiter conjunction
    jupiter = planetary.get_skyfield_obj("jupiter barycenter")
    conjs = find_conjunctions_between_moving_bodies(
        place.observer,
        "moon",
        [("Jupiter", jupiter)],
        start_date,
        end_date,
        threshold_degrees=10.0
    )

    assert len(conjs) > 0

    for c in conjs:
        t_center = ts.from_datetime(c['date'])
        def get_sep(t):
            m = place.observer.at(t).observe(eph['moon']).apparent(deflectors=())
            j = place.observer.at(t).observe(jupiter).apparent(deflectors=())
            return m.separation_from(j).degrees

        sep_center = get_sep(t_center)
        t_minus = ts.utc(t_center.utc[0], t_center.utc[1], t_center.utc[2], t_center.utc[3], t_center.utc[4], t_center.utc[5] - 60)
        t_plus = ts.utc(t_center.utc[0], t_center.utc[1], t_center.utc[2], t_center.utc[3], t_center.utc[4], t_center.utc[5] + 60)

        assert sep_center <= get_sep(t_minus) + 1e-9
        assert sep_center <= get_sep(t_plus) + 1e-9
