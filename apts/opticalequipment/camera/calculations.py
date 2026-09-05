from ...utils import map_conn, map_gender


def normalize_camera_database_entry(entry: dict) -> dict:
    """
    Normalizes a camera database entry by filling in missing sensor dimensions
    using fallback heuristics and mapping input connection formats.
    """
    entry = entry.copy()
    name = entry.get("name", "")

    sw, sh = (entry.get("sensor_width_mm"), entry.get("sensor_height_mm"))
    w, h = (entry.get("width"), entry.get("height"))

    if sw is None or sh is None or w is None or h is None:
        name_lower = name.lower()
        sw_h, sh_h = (23.5, 15.7)
        w_h, h_h = (6000, 4000)
        if "full frame" in name_lower or "36x24" in name_lower:
            sw_h, sh_h = (35.9, 23.9)
            w_h, h_h = (8256, 5504)
        elif "4/3" in name_lower or "micro four thirds" in name_lower:
            sw_h, sh_h = (17.3, 13.0)
            w_h, h_h = (4656, 3520)

        entry["sensor_width_mm"] = sw if sw is not None else sw_h
        entry["sensor_height_mm"] = sh if sh is not None else sh_h
        entry["width"] = w if w is not None else w_h
        entry["height"] = h if h is not None else h_h

    inputs = entry.get("inputs")
    if inputs is None:
        tt = map_conn(entry.get("tside_thread"))
        tg = map_gender(entry.get("tside_gender"))
        entry["inputs"] = [(tt, tg)] if tt else []
    else:
        entry["inputs"] = [
            (map_conn(c), map_gender(g)) if isinstance(c, str) else (c, g)
            for c, g in inputs
        ]

    return entry
