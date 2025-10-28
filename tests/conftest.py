import pytest
import os
import tempfile
import requests
from unittest.mock import patch
from apts.cache import get_mpcorb_data, get_timescale, get_ephemeris, get_hipparcos_data

# Global variable to store the temporary config file path
_temp_config_file = None


@pytest.fixture(scope="session", autouse=True)
def setup_test_config():
    """Set up test configuration at the start of the test session."""
    global _temp_config_file

    # Create a temporary config file with test settings
    temp_fd, _temp_config_file = tempfile.mkstemp(suffix=".ini", prefix="apts_test_")

    with os.fdopen(temp_fd, "w") as f:
        f.write("""[weather]
# Minimal test settings for weather API
provider = pirateweather

[notification]
# Minimal test settings for notifications
sender_email = test@example.com
smtp_host = localhost
smtp_port = 587
smtp_user = test@example.com
smtp_password = test
smtp_use_tls = False

[style]
# Test seaborn style
seaborn = whitegrid

[logging]
# Test logging level
level = WARNING

[data]
# Use light data mode for tests
mode = light

[Display]
# Test display settings
dark_mode = false

[minor_planets]
# Load only essential dwarf planets for testing to speed up tests
# Packed designations: Ceres, Pallas, Haumea, Makemake, Eris
load_only = 00001, 00002, K08S73P, K05X53E, K03E75A

[events]
# Enable minimal events for testing
moon_phases = true
conjunctions = true
oppositions = true
meteor_showers = false
highest_altitudes = true
lunar_occultations = false
aphelion_perihelion = false
moon_apogee_perigee = false
mercury_inferior_conjunctions = false
moon_messier_conjunctions = false
space_launches = false
space_events = false
iss_flybys = false
tiangong_flybys = false
solar_eclipses = false
lunar_eclipses = false
""")

    # Set environment variable to point to our test config
    os.environ["APTS_TEST_CONFIG"] = _temp_config_file

    # Patch the config module's config_paths to include our test file
    try:
        import apts.config as config_module

        if hasattr(config_module, "config_paths"):
            config_module.config_paths.insert(0, _temp_config_file)
            config_module.load_config()
    except (AttributeError, ImportError):
        # If we can't patch the config paths, the test will use defaults
        pass

    yield

    # Cleanup: remove temp config file
    if _temp_config_file and os.path.exists(_temp_config_file):
        os.unlink(_temp_config_file)

    # Remove environment variable
    if "APTS_TEST_CONFIG" in os.environ:
        del os.environ["APTS_TEST_CONFIG"]


@pytest.fixture(scope="session")
def preload_expensive_data():
    """Pre-load expensive data once per test session to avoid repeated loading."""
    # Load expensive cached data at session start with test config
    # This will use the limited dwarf planet set from test config
    get_timescale()
    get_ephemeris()
    get_mpcorb_data()  # Now loads only limited set from test config
    get_hipparcos_data()
    return True


@pytest.fixture(autouse=True)
def ensure_data_loaded(preload_expensive_data):
    """Ensure expensive data is loaded before each test without reloading."""
    # This fixture depends on preload_expensive_data which loads once per session
    # Individual tests will reuse the cached data instead of reloading
    pass


# Selective cache clearing fixtures - only used when explicitly requested by tests
@pytest.fixture
def clear_mpcorb_cache():
    """Fixture to clear MPCORB cache when specifically needed by a test."""

    def _clear():
        get_mpcorb_data.cache_clear()

    return _clear


@pytest.fixture
def clear_ephemeris_cache():
    """Fixture to clear ephemeris cache when specifically needed by a test."""

    def _clear():
        get_ephemeris.cache_clear()

    return _clear


@pytest.fixture
def clear_timescale_cache():
    """Fixture to clear timescale cache when specifically needed by a test."""

    def _clear():
        get_timescale.cache_clear()

    return _clear


@pytest.fixture
def clear_hipparcos_cache():
    """Fixture to clear Hipparcos cache when specifically needed by a test."""

    def _clear():
        get_hipparcos_data.cache_clear()

    return _clear


@pytest.fixture
def clear_all_caches():
    """Fixture to clear all caches when specifically needed by a test."""

    def _clear():
        get_mpcorb_data.cache_clear()
        get_timescale.cache_clear()
        get_ephemeris.cache_clear()
        get_hipparcos_data.cache_clear()

    return _clear


# Pytest markers for cache clearing - tests can use these to request cache clearing
def pytest_configure(config):
    """Register custom pytest markers."""
    config.addinivalue_line(
        "markers", "clear_caches: mark test to clear all caches before running"
    )
    config.addinivalue_line(
        "markers", "clear_mpcorb: mark test to clear MPCORB cache before running"
    )


@pytest.fixture(autouse=True)
def conditional_cache_clearing(request):
    """Clear caches only when test is marked to require it."""
    # Check for cache clearing markers
    if request.node.get_closest_marker("clear_caches"):
        get_mpcorb_data.cache_clear()
        get_timescale.cache_clear()
        get_ephemeris.cache_clear()
        get_hipparcos_data.cache_clear()
    elif request.node.get_closest_marker("clear_mpcorb"):
        get_mpcorb_data.cache_clear()


@pytest.fixture(autouse=True)
def mock_weather_session(request):
    """Mock get_session to return a regular requests.Session for tests.

    This ensures that requests_mock can properly intercept HTTP calls
    made by weather providers, bypassing the caching mechanism.
    """
    # Create a fresh session for each test
    test_session = requests.Session()

    # Patch get_session to return our test session
    with patch("apts.weather_providers.get_session", return_value=test_session):
        yield test_session
