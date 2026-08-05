def calculate_backfocus_gap(
    required_bf_mm: float,
    intermediate_optical_lengths_mm: list[float],
    output_backfocus_mm: float,
) -> float:
    """
    Calculates the backfocus gap in millimeters.
    Formula: Gap = RequiredBackfocus - (Sum(IntermediateOpticalLengths) + OutputBackfocus)
    """
    actual_distance = sum(intermediate_optical_lengths_mm) + output_backfocus_mm
    return required_bf_mm - actual_distance


def calculate_image_orientation(
    has_telescope: bool, diagonal_is_erecting_list: list[bool]
) -> tuple[bool, bool]:
    """
    Calculates image orientation flips (horizontal, vertical).
    """
    if not has_telescope:
        return (False, False)

    flipped_horizontally = True
    flipped_vertically = True

    for is_erecting in diagonal_is_erecting_list:
        if is_erecting:
            flipped_horizontally = not flipped_horizontally
            flipped_vertically = not flipped_vertically
        else:
            flipped_vertically = not flipped_vertically

    return (flipped_horizontally, flipped_vertically)


def calculate_thermal_drift(
    focal_length_mm: float, alpha: float, delta_t: float
) -> float:
    """
    Calculates thermal drift in millimeters.
    Formula: Drift = Length * Alpha * DeltaT
    """
    return focal_length_mm * alpha * delta_t
