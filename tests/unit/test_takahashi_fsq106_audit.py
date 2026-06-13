import pytest
from apts.opticalequipment.telescope.vendors.takahashi import TakahashiTelescope

def test_takahashi_fsq106_specs():
    """
    Test the audited specifications for the Takahashi FSQ-106ED (EDX4).
    """
    telescope = TakahashiTelescope.Takahashi_FSQ_106ED()

    # Assert mass (7000g = 7.0kg)
    # Mass is stored as a Pint Quantity in grams
    assert telescope.mass.magnitude == 7000
    assert str(telescope.mass.units) == 'gram'

    # Assert aperture and focal length
    assert telescope.aperture.magnitude == 106
    assert telescope.focal_length.magnitude == 530

    # Assert focal ratio (f/5)
    assert telescope.focal_ratio() == 5.0

    # Assert backfocus (metal back distance)
    # In the database it is stored as optical_length (178)
    # and bf_role="start" means it is assigned to self.backfocus
    assert telescope.backfocus.magnitude == 178
    assert telescope.optical_length.magnitude == 178

    # Assert connection type
    from apts.utils import ConnectionType
    assert telescope.connection_type == ConnectionType.M92

if __name__ == "__main__":
    pytest.main([__file__])
