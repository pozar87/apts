#!/usr/bin/python
# -*- coding: utf-8 -*-

import os

from apts import Equipment, opticalequipment, observations, place
from apts.config import get_plot_format
from matplotlib import pyplot

# Create an output directory if it doesn't exist
if not os.path.exists("test_plots"):
    os.makedirs("test_plots")

# --- Equipment and Location Setup ---
my_equipment = Equipment()
sky_watcher = "SW"
my_equipment.register(opticalequipment.Telescope(150, 750, sky_watcher, t2_output=True))
my_place = place.Place(lat=50.1637973, lon=19.7855169, name="Zelków")
my_observation = observations.Observation(my_place, my_equipment)

# --- Target Object ---
target = "M13"

# --- Generate and Save Skymap Plots ---

# 1. Full sky skymap
print("Generating full sky skymap...")
fig_full = my_observation.plot_skymap(target_name=target)
if fig_full:
    plot_format = get_plot_format()
    fig_full.savefig(f"test_plots/skymap_full.{plot_format}")
    pyplot.close(fig_full)
    print(f"Saved full sky skymap to test_plots/skymap_full.{plot_format}")

# 2. Zoomed-in skymap (15 degrees)
print("\nGenerating zoomed-in skymap (15 degrees)...")
fig_zoom = my_observation.plot_skymap(target_name=target, zoom_deg=15)
if fig_zoom:
    plot_format = get_plot_format()
    fig_zoom.savefig(f"test_plots/skymap_zoom_15deg.{plot_format}")
    pyplot.close(fig_zoom)
    print(f"Saved zoomed-in skymap to test_plots/skymap_zoom_15deg.{plot_format}")

# 3. Zoomed-in skymap with custom magnitude limit
print("\nGenerating zoomed-in skymap with custom magnitude limit...")
fig_zoom_mag = my_observation.plot_skymap(target_name=target, zoom_deg=15, star_magnitude_limit=9)
if fig_zoom_mag:
    plot_format = get_plot_format()
    fig_zoom_mag.savefig(f"test_plots/skymap_zoom_mag9.{plot_format}")
    pyplot.close(fig_zoom_mag)
    print(f"Saved zoomed-in skymap with custom magnitude to test_plots/skymap_zoom_mag9.{plot_format}")

print("\nAll test plots generated.")
