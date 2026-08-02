import pytest
from apts.opticalequipment.telescope.vendors.canon import CanonTelescope

def test_canon_ef_200_specs():
    """
    Audit test for Canon EF 200mm f/2.8L II and Canon EF 200mm f/2.8L II USM based on official Canon Europe specs.
    Source: https://www.canon-europe.com/lenses/ef-200mm-f-2-8l-ii-usm-lens/specification.html
    """
    lenses = [
        CanonTelescope.Canon_EF_200mm_f_2_8L_II(),
        CanonTelescope.Canon_EF_200mm_f_2_8L_II_USM()
    ]

    for lens in lenses:
        # Mass: stored as a Pint Quantity in grams (765g)
        assert lens.mass.to('gram').magnitude == 765
        assert str(lens.mass.units) == 'gram'

        # Aperture: 71.42857mm
        assert lens.aperture.to('mm').magnitude == pytest.approx(71.42857, abs=1e-5)

        # Focal length: 200mm
        assert lens.focal_length.to('mm').magnitude == 200

        # Focal ratio (f/2.8)
        assert float(lens.focal_ratio().magnitude) == pytest.approx(2.8, abs=1e-5)

        # Central obstruction is 0 (refractor/lens)
        assert lens.central_obstruction.magnitude == 0

        # Connection type is EOS
        from apts.utils.equipment import ConnectionType
        assert lens.connection_type == ConnectionType.EOS

if __name__ == "__main__":
    pytest.main([__file__])
