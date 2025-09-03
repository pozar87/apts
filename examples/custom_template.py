#!/usr/bin/python
# -*- coding: utf-8 -*-

# Example showing how to use custom template and CSS with notifications
from apts import Place, Equipment, Observation, Notify

# Create a place for observation
place = Place("Example Location", 52.229, 21.012)
place.get_weather()

# Create equipment
equipment = Equipment()
telescope = equipment.add_telescope("Celestron", "C8", 200, 2032)
eyepiece = equipment.add_eyepiece("Example", "EP", 25)
equipment.add_barlow("Example", "Barlow", 2.0)

# Create observation
observation = Observation(place, equipment)

# Custom CSS style to use
custom_css = """
body {
  font-family: 'Arial', sans-serif;
  color: #333;
  background: #f8f8f8;
}
h1, h2 {
  color: #0066cc;
  text-align: center;
}
table {
  border-radius: 5px;
  border: 1px solid #ddd;
  box-shadow: 0 2px 3px rgba(0,0,0,0.1);
}
th {
  background-color: #0066cc;
  color: white;
}
tr:nth-child(even) {
  background-color: #f2f2f2;
}
"""

# Check if weather is good for observation and send notification with custom style
if observation.is_weather_good():
    notify = Notify("user@example.com")
    # Using default template but with custom CSS
    notify.send(observation, css=custom_css)
    
    # Alternatively, you could use a completely custom template:
    # custom_template_path = "/path/to/custom_template.html"
    # notify.send(observation, custom_template=custom_template_path, css=custom_css)

    # You can also specify a custom plain text fallback message:
    # notify.send(observation, plain_text_fallback="Your custom fallback message here.")
    
    print("Notification sent with custom styling!")
else:
    print("Weather is not suitable for observation.")