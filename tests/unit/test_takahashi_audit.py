import pytest
from apts.opticalequipment.telescope.vendors.takahashi import TakahashiTelescope

def test_takahashi_fsq_85edp_audit():
    """
    Test the audited specifications for the Takahashi FSQ-85EDP.
    """
    telescope = TakahashiTelescope.Takahashi_FSQ_85EDP()
    assert telescope.aperture.magnitude == 85
    assert telescope.focal_length.magnitude == 450
    assert telescope.mass.magnitude == 3600
    assert telescope.backfocus.magnitude == 197.5
    assert telescope.optical_length.magnitude == 197.5

def test_takahashi_fsq_130ed_audit():
    """
    Test the audited specifications for the Takahashi FSQ-130ED.
    """
    telescope = TakahashiTelescope.Takahashi_FSQ_130ED()
    assert telescope.aperture.magnitude == 130
    assert telescope.focal_length.magnitude == 650
    assert telescope.mass.magnitude == 12700
    assert telescope.backfocus.magnitude == 172.9
    assert telescope.optical_length.magnitude == 172.9

def test_takahashi_tsa_120_audit():
    """
    Test the audited specifications for the Takahashi TSA-120.
    """
    telescope = TakahashiTelescope.Takahashi_TSA_120()
    assert telescope.aperture.magnitude == 120
    assert telescope.focal_length.magnitude == 900
    assert telescope.mass.magnitude == 6700
    assert telescope.backfocus.magnitude == 227.5
    assert telescope.optical_length.magnitude == 227.5

def test_takahashi_toa_130nfb_audit():
    """
    Test the audited specifications for the Takahashi TOA-130NFB.
    """
    telescope = TakahashiTelescope.Takahashi_TOA_130NFB()
    assert telescope.aperture.magnitude == 130
    assert telescope.focal_length.magnitude == 1000
    assert telescope.mass.magnitude == 12300
    assert telescope.backfocus.magnitude == 274.5
    assert telescope.optical_length.magnitude == 274.5
