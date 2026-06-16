import time
import sys
import os

# Add current directory to sys.path to import apts
sys.path.insert(0, os.getcwd())

from apts.constants.graphconstants import get_messier_color
from apts.i18n import set_language, gettext_

# Mock translations if needed, but let's see what we have
set_language('pl')

# Ensure some types are translated to avoid "en" early return if any
types = [
    "Spiral Galaxy", "Elliptical Galaxy", "Irregular Galaxy",
    "Globular Cluster", "Open Cluster", "Diffuse Nebula",
    "Planetary Nebula", "Supernova Remnant", "Other"
]
translated_types = [gettext_(t) for t in types]

start = time.time()
iterations = 1000
for _ in range(iterations):
    for t in translated_types:
        get_messier_color(t, True)
end = time.time()
duration = end - start
print(f"Time for {iterations * len(translated_types)} calls: {duration:.4f}s")
print(f"Average time per call: {duration / (iterations * len(translated_types)):.6f}s")
