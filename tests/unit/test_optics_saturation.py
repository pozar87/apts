import sys
from unittest.mock import MagicMock

# Mock problematic dependencies before importing apts
sys.modules["cairo"] = MagicMock()
sys.modules["pycairo"] = MagicMock()
sys.modules["seaborn"] = MagicMock()

import pytest
import numpy as np
from apts.optics import OpticalPath
from apts.opticalequipment.telescope.vendors.zwo import ZwoTelescope
from apts.units import get_unit_registry

def test_psf_peak_fraction():
    # Setup a common configuration (e.g., Seestar S50)
    # Aperture 50mm, Focal length 250mm, Pixel size 2.9um
    # Pixel scale = (2.9 / 250) * 206265 = 2.392674 arcsec/pixel
    s50 = ZwoTelescope.ZWO_Seestar_S50()
    path = OpticalPath.from_path([s50])

    # Under-sampled case: seeing 1.0", pixel scale 2.39"
    # ratio = 2.39 / 1.0 = 2.39
    # arg = 2.39 * sqrt(ln2) / 1.0 = 2.39 * 0.83255 = 1.99
    # erf(1.99) is close to 1.0.
    f1 = path.psf_peak_fraction(1.0)
    assert f1 > 0.9

    # Over-sampled case: seeing 5.0", pixel scale 2.39"
    # ratio = 2.39 / 5.0 = 0.478
    # arg = 0.478 * 0.83255 = 0.398
    # erf(0.398)^2 is much smaller.
    f5 = path.psf_peak_fraction(5.0)
    assert f5 < f1
    assert f5 < 0.2

def test_saturation_calculations():
    s50 = ZwoTelescope.ZWO_Seestar_S50()
    print(f"Full well: {s50.full_well}")
    print(f"QE: {s50.quantum_efficiency}")
    # Seestar S50: Full well ~12000e-, QE ~80%
    path = OpticalPath.from_path([s50])

    magnitude = 0.0 # Very bright star (Vega-like)
    seeing = 2.0

    # Calculate saturation time
    t_sat = path.saturation_time(magnitude, seeing)
    assert t_sat is not None
    assert t_sat.magnitude > 0

    # At magnitude 0, it should saturate VERY quickly (milliseconds)
    assert t_sat.to("second").magnitude < 0.1

    # Calculate saturation magnitude for a 10s exposure
    m_sat = path.saturation_magnitude(10.0, seeing)
    assert m_sat is not None
    # For a 10s exposure, the star must be much fainter to just saturate
    assert m_sat > 5.0

def test_saturation_consistency():
    s50 = ZwoTelescope.ZWO_Seestar_S50()
    path = OpticalPath.from_path([s50])
    seeing = 2.5

    # If we take the saturation time for a given magnitude...
    mag = 10.0
    t_sat = path.saturation_time(mag, seeing).to("second").magnitude

    # ...then the saturation magnitude for that time should be the same mag.
    m_calc = path.saturation_magnitude(t_sat, seeing)

    assert pytest.approx(m_calc, abs=1e-5) == mag

if __name__ == "__main__":
    test_psf_peak_fraction()
    test_saturation_calculations()
    test_saturation_consistency()
    print("All saturation tests passed!")
