#!/usr/bin/python
# -*- coding: utf-8 -*-

# Basic example
from apts import Equipment, opticalequipment, observations, place, notify

my_equipment = Equipment()

sky_watcher = "SW"

my_equipment.register(opticalequipment.Camera(23.5, 15.6, 6000, 4000, "Nikon"))
my_equipment.register(opticalequipment.Telescope(150, 750, sky_watcher, t2_output = True))
my_equipment.register(opticalequipment.Barlow(2, sky_watcher, t2_output = True))
my_equipment.register(opticalequipment.Eyepiece(25, sky_watcher))
my_equipment.register(opticalequipment.Eyepiece(10, sky_watcher))

my_place = place.Place(lat=50.1637973, lon=19.7855169, name="Zelków")
my_observation = observations.Observation(my_place, my_equipment)

if my_observation.is_weather_good():
  notify = notify.Notify('example@gmail.com')
  notify.send(my_observation)