import pytest
from apts.opticalequipment.telescope.vendors.canon import CanonTelescope

def test_canon_ef_135_specs():
    """
    Audit test for Canon EF 135mm f/2L and Canon EF 135mm f/2L USM based on official Canon Europe specs.
    Source: https://www.canon-europe.com/lenses/ef-135mm-f-2l-usm-lens/specification.html
    """
    lenses = [
        CanonTelescope.Canon_EF_135mm_f_2L(),
        CanonTelescope.Canon_EF_135mm_f_2L_USM()
    ]

    for lens in lenses:
        # Mass: stored as a Pint Quantity in grams (750g)
        assert lens.mass.to('gram').magnitude == 750
        assert str(lens.mass.units) == 'gram'

        # Aperture: 67.5mm
        assert lens.aperture.to('mm').magnitude == 67.5

        # Focal length: 135mm
        assert lens.focal_length.to('mm').magnitude == 135

        # Focal ratio (f/2)
        assert float(lens.focal_ratio().magnitude) == 2.0

        # Central obstruction is 0 (refractor/lens)
        assert lens.central_obstruction.magnitude == 0

        # Connection type is EOS
        from apts.utils.equipment import ConnectionType
        assert lens.connection_type == ConnectionType.EOS

if __name__ == "__main__":
    pytest.main([__file__])
