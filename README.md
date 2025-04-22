[![Join the chat at https://gitter.im/apts-core/Lobby](https://badges.gitter.im/apts-core/Lobby.svg)](https://gitter.im/apts-core/Lobby?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge)

# APTS - AstroPhotography Tool Set

A comprehensive suite of tools for amateur astronomers and astrophotographers. APTS helps with equipment management, image acquisition planning, processing, and provides notifications about optimal weather conditions for stargazing. This project was formerly known as **Astro-Pożar Tool Set** and is now an open source library supporting the [stargazer.earth](https://stargazer.earth) service.

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
  - Customize notification templates with your own HTML and CSS

## Installation

```bash
pip install apts
```

## Configuration

Create a *~/.config/apts/apts.ini* file with the following content:

```ini
[weather]
# Settings for weather API (e.g., pirateweather.net)
api_key = <api_key>

[notification]
# Recipient email address for notifications
recipient_email = <your_email@example.com>

# SMTP Server Configuration for sending emails
smtp_host = smtp.example.com
smtp_port = 587
smtp_user = <your_smtp_username_or_email>
# Use app password if using Gmail/2FA
smtp_password = <your_smtp_password_or_app_password>
# Use TLS (True/False) - Recommended: True
smtp_use_tls = True

[style]
# Seaborn style for plots (e.g., whitegrid, darkgrid, white, dark)
seaborn = whitegrid

[logging]
# Logging level (DEBUG, INFO, WARNING, ERROR, CRITICAL)
level = INFO
```

**Note:** The notification settings (SMTP host, port, user, password, TLS usage, and recipient email) are read from the configuration file when you instantiate the `apts.Notify` class in your script.

## Quick Start

```python
import configparser
import os
from apts import Equipment, Place, Observation, Notify
from apts.opticalequipment import Telescope, Eyepiece # Import specific equipment types

# --- Configuration Loading ---
config = configparser.ConfigParser()
# Define potential config file locations
config_files = [
    'examples/apts.ini', # Example config in project dir
    os.path.expanduser('~/.config/apts/apts.ini') # User-specific config
]
found_configs = config.read(config_files)
if not found_configs:
    print("Warning: No configuration file found. Notifications may fail.")
    # Handle missing config appropriately (e.g., exit or use defaults)

# --- Equipment Setup ---
# Note: Equipment details could also come from config or another source
my_telescope = Telescope(vendor="MyScope", aperture=200, focal_length=1000)
my_eyepiece = Eyepiece(vendor="MyEP", focal_length=25)

my_equipment = Equipment()
my_equipment.register(my_telescope)
my_equipment.register(my_eyepiece)

# --- Location Setup ---
# Note: Location details could also come from config
backyard = Place(name="Backyard", lat='40.7128', lon='-74.0060') # Use strings for lat/lon

# --- Observation Planning ---
my_observation = Observation(backyard, my_equipment)

# Example: Get visible Messier objects (assuming conditions are suitable)
# visible_messier = my_observation.get_visible_messier()
# print(visible_messier)

# Example: Generate plots (these methods return matplotlib figures)
# weather_plot = my_observation.plot_weather()
# messier_plot = my_observation.plot_visible_messier()
# planets_plot = my_observation.plot_visible_planets()
# weather_plot.show() # Display the plot

# --- Sending Notification (Example) ---
# Check if the recipient email is configured
if config.has_section('notification') and config.has_option('notification', 'recipient_email'):
    recipient = config.get("notification", "recipient_email")
    if recipient and recipient != '<email>': # Check if it's set and not the placeholder
        try:
            # Instantiate Notify with only the recipient email.
            # SMTP details are read from config within the Notify class.
            notifier = Notify(recipient_email=recipient)

            print("Sending notification...")
            # The send method expects an Observation object which contains
        # the data and methods to generate plots and HTML content.
        notifier.send(my_observation)
        print("Notification sent.")
    except Exception as e:
        print(f"Error sending notification: {e}")
else:
    print("Notification settings not found in configuration. Skipping email.")

```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.
