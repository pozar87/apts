import time

from apts.config import get_plot_format
from apts.observations import Observation
from apts.place import Place
from apts.equipment import Equipment

# Setup
place = Place(lat=42.3601, lon=-71.0589, name="Boston")
equipment = Equipment()
observation = Observation(place=place, equipment=equipment)

# Arguments that caused performance issues
plot_kwargs = {
    "target_name": "M31",
    "plot_ngc": True,
    "star_magnitude_limit": 8,
    "zoom_deg": 5,
}

# Time the execution
start_time = time.time()
fig = observation.plot_skymap(**plot_kwargs)
end_time = time.time()

execution_time = end_time - start_time
print(f"Sky map generation took: {execution_time:.2f} seconds")

# Optionally, save the figure to visually inspect it
if fig:
    plot_format = get_plot_format()
    fig.savefig(f"performance_test_skymap.{plot_format}")
    print(f"Saved skymap to performance_test_skymap.{plot_format}")