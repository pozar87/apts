import pytest
from apts.opticalequipment.telescope.vendors.celestron import CelestronTelescope

def test_celestron_c5_ota_xlt_audit():
    """
    Audit test for Celestron C5 OTA (XLT) to verify precision specs.
    Source: https://www.celestron.com/products/c5-spotting-scope
    """
    telescope = CelestronTelescope.Celestron_C5_OTA_XLT()

    # Official Aperture: 127mm (5")
    assert telescope.aperture.magnitude == 127

    # Official Focal Length: 1250mm
    assert telescope.focal_length.magnitude == 1250

    # Official weight: 96 oz = 2721.55g -> rounded to 2722g in official specs
    assert telescope.mass.magnitude == 2722

    # Official Secondary Mirror Obstruction: 51mm (2.0")
    assert telescope.central_obstruction.magnitude == 51

    # Verify vendor string construction
    assert telescope.get_vendor() == "Celestron C5 OTA (XLT)"

    # Verify focal ratio calculation (stated f/10)
    # 1250 / 127 = 9.84... but Celestron markets it as f/10.
    # Physical specs are more important than marketing numbers.
    assert round(telescope.focal_ratio().magnitude, 1) == 9.8
