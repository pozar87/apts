def get_rarity(event_type: str, data: dict) -> int:
    if event_type == "Moon Phase":
        return 1
    if event_type in [
        "Conjunction",
        "Moon-Messier Conjunction",
        "Moon-Star Conjunction",
        "Planet-Messier Conjunction",
        "Planet-Star Conjunction",
    ]:
        sep = data.get("separation_degrees", 5.0)
        if sep < 0.15:
            return 5
        if sep < 0.4:
            return 4
        if sep < 1.2:
            return 3
        if sep < 2.5:
            return 2
        return 1
    if event_type == "Opposition":
        obj = data.get("object", "")
        if obj in ["Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]:
            return 4
        return 3
    if event_type == "Meteor Shower":
        if data.get("phase") == "Peak":
            return 4
        return 1
    if event_type == "Planet Altitude":
        return 3
    if event_type in ["Lunar Occultation", "Lunar Planetary Occultation"]:
        return 4
    if event_type == "Aphelion/Perihelion":
        return 1
    if event_type == "Moon Apogee/Perigee":
        return 1
    if event_type == "Inferior Conjunction":
        if data.get("is_transit"):
            return 5
        return 3
    if event_type == "Solar Eclipse":
        kind = str(data.get("eclipse_type", "")).lower()
        if "total" in kind:
            return 5
        if "annular" in kind:
            return 5
        return 4
    if event_type == "Lunar Eclipse":
        kind = str(data.get("eclipse_kind", "")).lower()
        if "total" in kind:
            return 5
        if "partial" in kind:
            return 4
        return 3
    if event_type in ["Space Launch", "Space Event"]:
        return 2
    if event_type in ["ISS Flyby", "Tiangong Flyby"]:
        mag = data.get("peak_magnitude", 0)
        if mag < -3:
            return 4
        if mag < -1:
            return 3
        return 1
    if event_type == "Comet":
        return 5
    if event_type == "Planet Alignment":
        planets_count = len(data.get("planets", []))
        if planets_count >= 6:
            return 5
        if planets_count == 5:
            return 4
        if planets_count == 4:
            return 3
        return 2
    if event_type == "Greatest Elongation":
        return 3
    if event_type == "Season":
        return 2
    if event_type == "Messier Culmination":
        return 2
    if event_type == "Jovian Moon Event":
        return 3
    if event_type == "Jupiter GRS Transit":
        return 1
    if event_type == "Planet Stationary Point":
        return 3
    if event_type == "Planet Solar Conjunction":
        return 3
    if event_type == "Lunar Feature":
        return 4
    if event_type == "Moon Libration Maximum":
        return 3
    if event_type == "Planet-Planet Occultation":
        return 5
    if event_type == "Venus Greatest Brilliancy":
        return 4
    if event_type == "Supermoon":
        return 3
    if event_type == "Planetary Dichotomy":
        return 3
    if event_type == "Mars Closest Approach":
        return 4
    return 1
