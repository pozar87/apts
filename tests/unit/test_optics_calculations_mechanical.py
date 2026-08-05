import pytest
from apts.optics.calculations.mechanical import (
    calculate_backfocus_gap,
    calculate_image_orientation,
    calculate_thermal_drift,
)


def test_calculate_backfocus_gap():
    # Test simple case
    # Required: 55mm, Intermediate length: [10mm, 15mm], Output backfocus: 17.5mm
    # Expected actual distance: 10 + 15 + 17.5 = 42.5mm
    # Expected gap: 55 - 42.5 = 12.5mm
    gap = calculate_backfocus_gap(55.0, [10.0, 15.0], 17.5)
    assert gap == 12.5

    # Test with no intermediate components
    # Expected actual: 0 + 17.5 = 17.5
    # Expected gap: 55 - 17.5 = 37.5
    gap2 = calculate_backfocus_gap(55.0, [], 17.5)
    assert gap2 == 37.5


def test_calculate_image_orientation():
    # Test case where telescope is False
    assert calculate_image_orientation(False, [True, False]) == (False, False)

    # Test telescope present, with erecting diagonal (toggles both horizontal and vertical)
    # Start state: (True, True)
    # [True] (erecting) -> flip both -> (False, False)
    assert calculate_image_orientation(True, [True]) == (False, False)

    # Test telescope present, with non-erecting diagonal (flips vertical only)
    # Start state: (True, True)
    # [False] (non-erecting) -> flip vertical only -> (True, False)
    assert calculate_image_orientation(True, [False]) == (True, False)

    # Test multiple diagonals: [True, False]
    # Start state: (True, True)
    # True (erecting) -> flip both -> (False, False)
    # False (non-erecting) -> flip vertical only -> (False, True)
    assert calculate_image_orientation(True, [True, False]) == (False, True)


def test_calculate_thermal_drift():
    # Length: 1000mm, alpha: 23e-6, delta_t: 10C
    # Drift = 1000 * 23e-6 * 10 = 0.23mm
    drift = calculate_thermal_drift(1000.0, 23e-6, 10.0)
    assert pytest.approx(drift) == 0.23
