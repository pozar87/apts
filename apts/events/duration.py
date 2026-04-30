from datetime import datetime
from typing import Optional


def _get_time_diff_seconds(t1: Optional[datetime], t2: Optional[datetime]) -> Optional[int]:
    if t1 and t2:
        return int(abs((t1 - t2).total_seconds()))
    return None


def get_duration(event_type: str, data: dict) -> int:
    """
    Returns the duration of an astronomical event in seconds.
    Prioritizes dynamic calculation if time bounds are available in the data.
    """

    # 1. Dynamic calculation if time bounds are present
    # Flybys
    if event_type in ["ISS Flyby", "Tiangong Flyby"]:
        duration = _get_time_diff_seconds(data.get("rise_time"), data.get("set_time"))
        if duration:
            return duration

    # Occultations
    if "Occultation" in event_type:
        duration = _get_time_diff_seconds(data.get("ingress_time"), data.get("egress_time"))
        if duration:
            return duration

    # 2. Defaults based on astronomical relevance
    # Fast events (seconds to hours)
    duration_map = {
        "ISS Flyby": 600,             # 10 minutes
        "Tiangong Flyby": 600,        # 10 minutes
        "Lunar Occultation": 3600,    # 1 hour
        "Lunar Planetary Occultation": 3600,
        "Planet-Planet Occultation": 3600,
        "Solar Eclipse": 7200,        # 2 hours
        "Lunar Eclipse": 14400,       # 4 hours
        "Jovian Moon Event": 7200,    # 2 hours (Transit, Shadow, etc.)
        "Jovian Mutual Occultation": 1800, # 30 minutes
        "Jovian Mutual Eclipse": 1800,
        "Jupiter GRS Transit": 7200,  # 2 hours
        "Golden Hour": 3600,          # 1 hour
        "Blue Hour": 3600,            # 1 hour
        "Culmination": 3600,          # 1 hour
        "Messier Culmination": 3600,
        "Space Launch": 600,          # 10 minutes
        "Space Event": 3600,          # 1 hour
    }

    if event_type in duration_map:
        return duration_map[event_type]

    # Slow events (days)
    # Default for conjunctions and other slow-moving events is 2 days (172800s)
    if "Conjunction" in event_type or event_type == "Planet Solar Conjunction":
        return 172800

    # Default for oppositions and closest approach is 3 days (259200s)
    if event_type in ["Opposition", "Mars Closest Approach"]:
        return 259200

    # Standard default for most other events (Moon phases, seasons, elongations, etc.) is 1 day
    return 86400
