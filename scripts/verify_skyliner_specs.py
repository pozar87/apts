import sys
from unittest.mock import MagicMock

class MockPackage(MagicMock):
    @property
    def __spec__(self):
        return None
    @property
    def __path__(self):
        return []

def mock_package(name):
    mock = MockPackage()
    sys.modules[name] = mock
    return mock

mock_package('pycairo')
mock_package('cairo')
mock_package('seaborn')
mock_package('matplotlib')
mock_package('matplotlib.ticker')
mock_package('matplotlib.pyplot')
mock_package('matplotlib.axes')
mock_package('matplotlib.figure')
mock_package('matplotlib.patches')
mock_package('matplotlib.collections')
mock_package('matplotlib.colors')
mock_package('matplotlib.cm')
mock_package('matplotlib.dates')
mock_package('matplotlib.font_manager')

from apts.opticalequipment.telescope.vendors.sky_watcher import Sky_watcherTelescope

def verify():
    skyliners = [
        ("Sky_Watcher_Skyliner_150P", 153, 1200, 34.5, 5900),
        ("Sky_Watcher_Skyliner_200P", 203, 1200, 47, 11000),
        ("Sky_Watcher_Skyliner_200P_FlexTube", 203, 1200, 47, 11000),
        ("Sky_Watcher_Skyliner_250P", 254, 1200, 58, 12500),
        ("Sky_Watcher_Skyliner_250P_FlexTube", 254, 1200, 58, 15000),
        ("Sky_Watcher_Skyliner_300P", 305, 1500, 70, 19500),
        ("Sky_Watcher_Skyliner_300P_FlexTube", 305, 1500, 70, 21000),
        ("Sky_Watcher_Skyliner_350P_FlexTube", 355, 1650, 83, 23500),
        ("Sky_Watcher_Skyliner_400P", 406, 1800, 102, 38000),
    ]

    for model_name, aperture, focal, co, mass in skyliners:
        print(f"Verifying {model_name}...")
        # Get via factory method
        factory_method = getattr(Sky_watcherTelescope, model_name)
        telescope = factory_method()

        # Access numerical value via .magnitude
        assert telescope.aperture.magnitude == aperture, f"{model_name} aperture mismatch: {telescope.aperture.magnitude} != {aperture}"
        assert telescope.focal_length.magnitude == focal, f"{model_name} focal length mismatch: {telescope.focal_length.magnitude} != {focal}"
        assert telescope.central_obstruction.magnitude == co, f"{model_name} CO mismatch: {telescope.central_obstruction.magnitude} != {co}"
        assert telescope.mass.magnitude == mass, f"{model_name} mass mismatch: {telescope.mass.magnitude} != {mass}"

        from apts.opticalequipment.telescope.base import TelescopeType
        assert telescope.telescope_type == TelescopeType.NEWTONIAN_REFLECTOR, f"{model_name} type mismatch: {telescope.telescope_type}"

        # Verify calculated focal ratio
        fr = telescope.focal_ratio().magnitude
        expected_fr = focal / aperture
        assert abs(fr - expected_fr) < 0.01, f"{model_name} focal ratio mismatch: {fr} != {expected_fr}"

        print(f"✅ {model_name} verified.")

if __name__ == "__main__":
    try:
        verify()
        print("\nAll Skyliner specifications verified successfully!")
    except Exception as e:
        print(f"\n❌ Verification failed: {e}")
        import traceback
        traceback.print_exc()
        exit(1)
