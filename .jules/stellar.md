# Stellar's Journal

## 2024-05-23 - Adding popular missing equipment

### Observe
- The ZWO ASI432MM is a popular camera for solar and lunar imaging due to its large 9µm pixels and global shutter, but it's missing from `apts/opticalequipment/camera/vendors/zwo.py`.
- The Sky-Watcher Evolux series (62ED, 82ED) are popular modern refractors missing from `apts/opticalequipment/telescope/vendors/sky_watcher.py`.

### Target
- Priority 2: Add missing popular camera and telescopes to the internal database.
- Choosing to add ASI432MM and the Evolux series.

### Calibrate
- ASI432MM specs: 1608x1104, 9.0µm pixels, 14.5x9.9mm sensor, 97ke- full well, 79% QE, 126g mass.
- Evolux 62ED specs: 62mm aperture, 400mm focal length, 2.5kg mass.
- Evolux 82ED specs: 82mm aperture, 530mm focal length, 2.92kg (OTA) mass.

### Develop
- I will add these entries to the respective `_DATABASE` dictionaries and add factory methods.
- I will verify with a small script that they can be instantiated and their properties are correct.
