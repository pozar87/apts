[![Join the chat at https://gitter.im/apts-core/Lobby](https://badges.gitter.im/apts-core/Lobby.svg)](https://gitter.im/apts-core/Lobby?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge)

# APTS - AstroPhotography Tool Set

A comprehensive suite of tools for amateur astronomers and astrophotographers. APTS helps with equipment management, image acquisition planning, processing, and provides notifications about optimal weather conditions for stargazing. This project was formerly known as **Astro-Pożar Tool Set** and is now an open source library supporting the [stargazer.cloud](https://staging.stargazer.cloud) service.

## Features

- **Equipment Management**
  - Register telescopes, eyepieces, cameras, and accessories
  - Compute all possible magnifications (including DSLR configurations)
  - Plot available zoom levels and fields of view

- **Location and Weather**
  - Register observation locations
  - Check weather forecasts for your viewing spots
  - Calculate observing conditions based on configurable thresholds
  - Generate visual summaries of weather conditions

- **Astronomical Objects**
  - Track visible planets
  - Find observable Messier objects based on your location and time
  - Plan your viewing sessions for optimal results

- **Notifications**
  - Receive email alerts about favorable weather conditions
  - Get updates on interesting celestial objects visible at your location

## Installation

```bash
pip install apts
```

## Configuration 

Create a *~/.config/apts/apts.ini* file with the following content:

```ini
[weather]
# Settings for weather API 
api_url = <api_url>
api_key = <api_key>

[notification]
# Email configuration
email_address = <email>
# If using Gmail, use Google application passwords
email_password = <password>
```

## Quick Start

```python
from apts import equipment, place, weather, observations

# Set up your equipment
my_telescope = equipment.Telescope("My 8-inch", 200, 1000)
my_eyepiece = equipment.Eyepiece("25mm Plössl", 25)

# Create a viewing location
backyard = place.Place("Backyard", latitude=40.7128, longitude=-74.0060)

# Check conditions
conditions = weather.get_conditions(backyard)
print(f"Viewing conditions tonight: {conditions.quality}")

# Find observable objects
visible_objects = observations.get_visible_objects(backyard)
```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.