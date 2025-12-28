import timeit
from datetime import datetime
import matplotlib.pyplot as plt

from apts.observations import Observation
from apts.place import Place
from apts.equipment import Equipment
from apts.conditions import Conditions
from apts.constants.plot import CoordinateSystem

def run_benchmark():
    """
    Sets up and runs the skymap generation benchmark.
    """
    # Set up the observation parameters
    place = Place(
        lat=34.0,
        lon=-118.0,
        elevation=100,
        name="Los Angeles"
    )
    equipment = Equipment()
    conditions = Conditions()

    obs = Observation(
        place=place,
        equipment=equipment,
        conditions=conditions,
        target_date=datetime(2024, 1, 1, 22, 0)
    )

    # Generate the skymap
    fig = obs.plot_skymap(
        target_name="NGC 224",  # Andromeda Galaxy
        zoom_deg=5.0,
        plot_stars=True,
        plot_ngc=True,
        coordinate_system=CoordinateSystem.EQUATORIAL,
    )
    # Close the plot to free up memory
    plt.close(fig)


if __name__ == "__main__":
    # Use timeit to run the benchmark
    number_of_runs = 5
    print(f"Running benchmark with {number_of_runs} iterations...")
    total_time = timeit.timeit(
        "run_benchmark()",
        setup="from __main__ import run_benchmark",
        number=number_of_runs,
    )

    avg_time = total_time / number_of_runs
    print(f"Benchmark finished.")
    print(f"Number of runs: {number_of_runs}")
    print(f"Total time: {total_time:.4f} seconds")
    print(f"Average time per run: {avg_time:.4f} seconds")
