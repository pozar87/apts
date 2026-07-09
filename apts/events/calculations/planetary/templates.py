
from .utils import BodyResolver

def get_config_templates():
    """
    Returns the list of celestial configuration templates.
    """
    return [
        # 1. Mars and Uranus between Pleiades (4 July 2026)
        {
            "type": "group",
            "bodies": [("Mars", "planet"), ("Uranus", "planet"), ("M45", "messier")],
            "threshold": 10.0,
            "label": "Mars and Uranus between Pleiades"
        },
        # 2. Venus near Regulus (9 July 2026)
        {
            "type": "group",
            "bodies": [("Venus", "planet"), ("Regulus", "star")],
            "threshold": 2.0,
            "label": "Venus near Regulus"
        },
        # 3. Moon near Mars and Pleiades (11 July 2026)
        {
            "type": "group",
            "bodies": [("Moon", "planet"), ("Mars", "planet"), ("M45", "messier")],
            "threshold": 10.0,
            "label": "Moon near Mars and Pleiades"
        },
        # 4. Mars forms a line with Aldebaran and Denebola (22 July 2026)
        {
            "type": "line",
            "bodies": [("Aldebaran", "star"), ("Mars", "planet"), ("Denebola", "star")],
            "tolerance": 10.0,
            "max_span": 120.0,
            "label": "Mars in line with Aldebaran and Denebola"
        },
        # 5. Venus, Regulus, and Elnath triangle (22 July 2026)
        {
            "type": "group",
            "bodies": [("Venus", "planet"), ("Regulus", "star"), (["El Nath", "Beta Tauri"], "star")],
            "threshold": 50.0,
            "label": "Venus with Regulus and Elnath triangle"
        }
    ]

def get_resolved_configurations(resolver: BodyResolver):
    """
    Returns configuration templates with resolved celestial bodies.
    """
    templates = get_config_templates()
    resolved_configs = []

    for template in templates:
        bodies = resolver.resolve_multi(template["bodies"])
        if bodies:
            config = template.copy()
            config["bodies"] = bodies
            resolved_configs.append(config)

    return resolved_configs
