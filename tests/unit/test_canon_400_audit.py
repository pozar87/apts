import pytest
from apts.opticalequipment.telescope.vendors.canon import CanonTelescope

def test_canon_ef_400_specs():
    """
    Audit test for Canon EF 400mm f/5.6L and Canon EF 400mm f/5.6L USM based on official Canon USA specs.
    Source: https://www.usa.canon.com/support/p/ef-400mm-f-5-6l-usm
    """
    lenses = [
        CanonTelescope.Canon_EF_400mm_f_5_6L(),
        CanonTelescope.Canon_EF_400mm_f_5_6L_USM()
    ]

    for lens in lenses:
        # Mass: stored as a Pint Quantity in grams (1250g)
        assert lens.mass.to('gram').magnitude == 1250
        assert str(lens.mass.units) == 'gram'

        # Aperture: 71.42857mm
        assert lens.aperture.to('mm').magnitude == pytest.approx(71.42857, abs=1e-5)

        # Focal length: 400mm
        assert lens.focal_length.to('mm').magnitude == 400

        # Focal ratio (f/5.6)
        assert float(lens.focal_ratio().magnitude) == pytest.approx(5.6, abs=1e-5)

        # Central obstruction is 0 (refractor/lens)
        assert lens.central_obstruction.magnitude == 0

        # Connection type is EOS
        from apts.utils.equipment import ConnectionType
        assert lens.connection_type == ConnectionType.EOS

if __name__ == "__main__":
    pytest.main([__file__])
