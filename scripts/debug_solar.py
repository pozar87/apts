
from datetime import datetime, timezone
from skyfield.api import load, Topos
from apts.cache import get_ephemeris, get_timescale
from apts.utils import planetary
from apts.constants import astronomy
import numpy as np

ts = get_timescale()
eph = get_ephemeris()
observer = eph["earth"] + Topos(latitude_degrees=52.2, longitude_degrees=21.0)
sun = eph["sun"]
moon = eph["moon"]

# Check New Moon on 2023-01-21
t = ts.utc(2023, 1, 21, 20, 53) # Geocentric New Moon
s_pos = observer.at(t).observe(sun).apparent()
m_pos = observer.at(t).observe(moon).apparent()
d = s_pos.separation_from(m_pos).degrees
rs = np.degrees(np.arcsin(astronomy.SUN_RADIUS_KM / s_pos.distance().km))
rm = np.degrees(np.arcsin(astronomy.MOON_RADIUS_KM / m_pos.distance().km))

print(f"Time: {t.utc_iso()}")
print(f"Separation: {d:.4f} degrees")
print(f"rs + rm: {rs + rm:.4f} degrees")
print(f"Is eclipse: {d < rs + rm}")
