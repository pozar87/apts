import pytest
from apts.opticalequipment.telescope.vendors.explore_scientific import Explore_scientificTelescope
from apts.opticalequipment.telescope.base import TelescopeType

def test_es_fcd100_specs():
    # ED80 FCD100
    scope = Explore_scientificTelescope.Explore_Scientific_ED80_FCD100()
    assert scope.aperture.magnitude == 80
    assert scope.focal_length.magnitude == 480
    assert scope.central_obstruction.magnitude == 0
    assert scope.mass.magnitude == 3400
    assert scope.telescope_type == TelescopeType.REFRACTOR

    # ED102 FCD100
    scope = Explore_scientificTelescope.Explore_Scientific_ED102_FCD100()
    assert scope.aperture.magnitude == 102
    assert scope.focal_length.magnitude == 714
    assert scope.central_obstruction.magnitude == 0
    assert abs(scope.focal_ratio().magnitude - 7.0) < 0.01

def test_es_firstlight_newtonian_specs():
    # FirstLight 130mm
    scope = Explore_scientificTelescope.Explore_Scientific_FirstLight_130mm_Newtonian()
    assert scope.aperture.magnitude == 130
    assert scope.focal_length.magnitude == 600
    assert scope.central_obstruction.magnitude == 45
    assert scope.mass.magnitude == 3175
    assert scope.telescope_type == TelescopeType.NEWTONIAN_REFLECTOR

def test_es_firstlight_mak_specs():
    # FirstLight 152mm Mak
    scope = Explore_scientificTelescope.Explore_Scientific_FirstLight_152mm_Mak()
    assert scope.aperture.magnitude == 152
    assert scope.focal_length.magnitude == 1900
    assert scope.central_obstruction.magnitude == 47
    assert scope.mass.magnitude == 7710
    assert scope.telescope_type == TelescopeType.MAKSUTOV_CASSEGRAIN

def test_es_truss_dob_specs():
    # Truss Dob 10"
    scope = Explore_scientificTelescope.Explore_Scientific_Truss_Dob_10()
    assert scope.aperture.magnitude == 254
    assert scope.focal_length.magnitude == 1270
    assert scope.central_obstruction.magnitude == 61.5
    assert scope.mass.magnitude == 18800
    assert scope.telescope_type == TelescopeType.NEWTONIAN_REFLECTOR

def test_es_specialty_specs():
    # Comet Hunter 152 Mak-Newt
    scope = Explore_scientificTelescope.Explore_Scientific_Comet_Hunter_152_Mak_Newt()
    assert scope.aperture.magnitude == 152
    assert scope.focal_length.magnitude == 731
    assert scope.central_obstruction.magnitude == 49
    # In base.py: 'newtonian' in 'maksutov_newtonian' is True
    assert scope.telescope_type == TelescopeType.NEWTONIAN_REFLECTOR
