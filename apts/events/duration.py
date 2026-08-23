from .calculations.evaluations import (
    _get_time_diff_seconds,
    calculate_event_duration,
)


def get_duration(event_type: str, data: dict) -> int:
    """
    Delegates duration calculation to the pure calculation engine in evaluations.py.
    Maintained for full backward compatibility.
    """
    return calculate_event_duration(event_type, data)


__all__ = [
    "get_duration",
    "calculate_event_duration",
    "_get_time_diff_seconds",
]
