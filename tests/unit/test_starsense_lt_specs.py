import pytest
from apts.opticalequipment.telescope.vendors.celestron import CelestronTelescope
from apts.opticalequipment.telescope.base import TelescopeType

def test_starsense_explorer_lt_114_specs():
    telescope = CelestronTelescope.Celestron_StarSense_Explorer_LT_114()
    assert telescope.aperture.magnitude == 114
    assert telescope.focal_length.magnitude == 1000
    assert telescope.central_obstruction.magnitude == 44
    assert telescope.mass.magnitude == 2990
    assert telescope.telescope_type == TelescopeType.NEWTONIAN_REFLECTOR
    assert telescope.connection_type.value == '1.25'

def test_starsense_explorer_lt_127_specs():
    telescope = CelestronTelescope.Celestron_StarSense_Explorer_LT_127()
    assert telescope.aperture.magnitude == 127
    assert telescope.focal_length.magnitude == 1000
    assert telescope.central_obstruction.magnitude == 41
    assert telescope.mass.magnitude == 3440
    assert telescope.telescope_type == TelescopeType.NEWTONIAN_REFLECTOR
    assert telescope.connection_type.value == '1.25'

def test_starsense_explorer_lt_80az_specs():
    telescope = CelestronTelescope.Celestron_StarSense_Explorer_LT_80AZ()
    assert telescope.aperture.magnitude == 80
    assert telescope.focal_length.magnitude == 900
    assert telescope.central_obstruction.magnitude == 0
    assert telescope.mass.magnitude == 2450
    assert telescope.telescope_type == TelescopeType.REFRACTOR
    assert telescope.connection_type.value == '1.25'
