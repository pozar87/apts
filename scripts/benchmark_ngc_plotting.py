import time
import pandas as pd
import numpy as np
from apts import Equipment, Place, Observation
from apts.plotting.skymap_objects import _plot_ngc_on_skymap
from apts.constants.plot import CoordinateSystem
import matplotlib.pyplot as plt

def benchmark():
    # Setup
    my_equipment = Equipment()
    my_place = Place(lat=50.0, lon=20.0, name="Test")
    my_observation = Observation(my_place, my_equipment)

    # We need a target object to trigger the zoomed-in logic
    target_name = "M31"
    target_object = my_observation.local_messier.find_by_name(target_name)

    # Mocking ax to avoid actual drawing overhead
    fig, ax = plt.subplots()

    observer = my_place.observer.at(my_place.ts.now())

    print("Starting benchmark for _plot_ngc_on_skymap (zoomed)...")
    start_time = time.time()

    # Run multiple times for better measurement
    iterations = 5
    for i in range(iterations):
        _plot_ngc_on_skymap(
            observation=my_observation,
            ax=ax,
            observer=observer,
            is_polar=False,
            target_name=target_name,
            zoom_deg=20.0, # Large zoom to include many objects
            target_object=target_object,
            coordinate_system=CoordinateSystem.HORIZONTAL
        )

    end_time = time.time()
    avg_time = (end_time - start_time) / iterations
    print(f"Average time per call: {avg_time:.4f} seconds")

    plt.close(fig)

if __name__ == "__main__":
    benchmark()
