#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
from apts import Equipment, opticalequipment, observations, place
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
    fig_full.savefig("test_plots/skymap_full.png")
    pyplot.close(fig_full)
    print("Saved full sky skymap to test_plots/skymap_full.png")

# 2. Zoomed-in skymap (15 degrees)
print("\nGenerating zoomed-in skymap (15 degrees)...")
fig_zoom = my_observation.plot_skymap(target_name=target, zoom_deg=15)
if fig_zoom:
    fig_zoom.savefig("test_plots/skymap_zoom_15deg.png")
    pyplot.close(fig_zoom)
    print("Saved zoomed-in skymap to test_plots/skymap_zoom_15deg.png")

# 3. Zoomed-in skymap with custom magnitude limit
print("\nGenerating zoomed-in skymap with custom magnitude limit...")
fig_zoom_mag = my_observation.plot_skymap(target_name=target, zoom_deg=15, star_magnitude_limit=9)
if fig_zoom_mag:
    fig_zoom_mag.savefig("test_plots/skymap_zoom_mag9.png")
    pyplot.close(fig_zoom_mag)
    print("Saved zoomed-in skymap with custom magnitude to test_plots/skymap_zoom_mag9.png")

print("\nAll test plots generated.")
