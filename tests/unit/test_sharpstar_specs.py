import pytest
from apts.opticalequipment.telescope.vendors.sharpstar import SharpstarTelescope

def test_sharpstar_61edph_ii():
    t = SharpstarTelescope.Sharpstar_61EDPH_II()
    assert t.aperture.magnitude == 61
    assert t.focal_length.magnitude == 335
    assert t.mass.magnitude == 1500
    assert t.central_obstruction.magnitude == 0

def test_sharpstar_76edph_ii():
    t = SharpstarTelescope.Sharpstar_76EDPH_II()
    assert t.aperture.magnitude == 76
    assert t.focal_length.magnitude == 418
    assert t.mass.magnitude == 2300
    assert t.central_obstruction.magnitude == 0

def test_sharpstar_94edph_ii():
    t = SharpstarTelescope.Sharpstar_94EDPH_II()
    assert t.aperture.magnitude == 94
    assert t.focal_length.magnitude == 517
    assert t.mass.magnitude == 3300
    assert t.central_obstruction.magnitude == 0

def test_sharpstar_140ph():
    t = SharpstarTelescope.Sharpstar_140PH()
    assert t.aperture.magnitude == 140
    assert t.focal_length.magnitude == 910
    assert t.mass.magnitude == 10100
    assert t.central_obstruction.magnitude == 0

def test_sharpstar_15028hnt():
    t = SharpstarTelescope.Sharpstar_15028HNT()
    assert t.aperture.magnitude == 150
    assert t.focal_length.magnitude == 420
    assert t.mass.magnitude == 4450
    assert t.central_obstruction.magnitude == 70

def test_sharpstar_20032hnt():
    t = SharpstarTelescope.Sharpstar_20032HNT()
    assert t.aperture.magnitude == 200
    assert t.focal_length.magnitude == 640
    assert t.mass.magnitude == 8000
    assert t.central_obstruction.magnitude == 90

def test_sharpstar_61edph_iii():
    t = SharpstarTelescope.Sharpstar_61EDPH_III()
    assert t.aperture.magnitude == 61
    assert t.focal_length.magnitude == 360
    assert t.mass.magnitude == 1480
    assert t.central_obstruction.magnitude == 0

def test_sharpstar_13028hnt():
    t = SharpstarTelescope.Sharpstar_13028HNT()
    assert t.aperture.magnitude == 130
    assert t.focal_length.magnitude == 364
    assert t.mass.magnitude == 3200
    assert t.central_obstruction.magnitude == 65
