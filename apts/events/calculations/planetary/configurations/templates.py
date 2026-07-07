
# Define specific configurations to look for
CELESTIAL_CONFIGURATIONS = [
    # 1. Mars and Uranus between Pleiades (4 July 2026)
    {
        "type": "group",
        "bodies": [
            {"type": "planet", "name": "Mars", "skyfield_name": "mars barycenter"},
            {"type": "planet", "name": "Uranus", "skyfield_name": "uranus barycenter"},
            {"type": "messier", "name": "M45"}
        ],
        "threshold": 10.0,
        "label": "Mars and Uranus between Pleiades"
    },
    # 2. Venus near Regulus (9 July 2026)
    {
        "type": "group",
        "bodies": [
            {"type": "planet", "name": "Venus"},
            {"type": "star", "name": "Regulus"}
        ],
        "threshold": 2.0,
        "label": "Venus near Regulus"
    },
    # 3. Moon near Mars and Pleiades (11 July 2026)
    {
        "type": "group",
        "bodies": [
            {"type": "planet", "name": "Moon"},
            {"type": "planet", "name": "Mars", "skyfield_name": "mars barycenter"},
            {"type": "messier", "name": "M45"}
        ],
        "threshold": 10.0,
        "label": "Moon near Mars and Pleiades"
    },
    # 4. Mars forms a line with Aldebaran and Denebola (22 July 2026)
    {
        "type": "line",
        "bodies": [
            {"type": "star", "name": "Aldebaran"},
            {"type": "planet", "name": "Mars", "skyfield_name": "mars barycenter"},
            {"type": "star", "name": "Denebola"}
        ],
        "tolerance": 10.0,
        "max_span": 120.0,
        "label": "Mars in line with Aldebaran and Denebola"
    },
    # 5. Venus, Regulus, and Elnath triangle (22 July 2026)
    {
        "type": "group",
        "bodies": [
            {"type": "planet", "name": "Venus"},
            {"type": "star", "name": "Regulus"},
            {"type": "star", "name": "El Nath"} # Note: handled as El Nath or Beta Tauri in old code
        ],
        "threshold": 50.0,
        "label": "Venus with Regulus and Elnath triangle"
    }
]
