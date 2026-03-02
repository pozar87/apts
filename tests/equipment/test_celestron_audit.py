import pytest

from apts.opticalequipment import Telescope


def test_nexstar_130slt_data():
    t = Telescope.from_database("Celestron NexStar 130SLT")
    assert t.aperture.magnitude == 130
    assert t.focal_length.magnitude == 650
    assert t.central_obstruction.magnitude == 38
    assert t.mass.magnitude == 3990
    assert str(t.telescope_type) == "TelescopeType.NEWTONIAN_REFLECTOR"
    assert t.focal_ratio().magnitude == pytest.approx(5.0)


def test_nexstar_127slt_data():
    t = Telescope.from_database("Celestron NexStar 127SLT")
    assert t.aperture.magnitude == 127
    assert t.focal_length.magnitude == 1500
    assert t.central_obstruction.magnitude == 39
    assert t.mass.magnitude == 3950
    assert str(t.telescope_type) == "TelescopeType.MAKSUTOV_CASSEGRAIN"
    assert t.focal_ratio().magnitude == pytest.approx(11.811, abs=1e-3)
