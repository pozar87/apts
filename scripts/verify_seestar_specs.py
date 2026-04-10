import sys
import os

# Add the project root to sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from apts.opticalequipment.telescope.vendors.zwo import ZwoTelescope
from apts.opticalequipment.camera.vendors.zwo import ZwoCamera

def verify_seestar():
    print("--- Verifying ZWO Seestar Series Data Integrity ---")

    # Verify S50
    print("\n[Seestar S50]")
    s50 = ZwoTelescope.ZWO_Seestar_S50()
    print(f"Model: {s50.get_vendor()}")
    print(f"Aperture: {s50.aperture}")
    print(f"Focal Length: {s50.focal_length}")
    print(f"Focal Ratio: f/{s50.focal_ratio()}")
    print(f"Sensor: {s50.sensor_width} x {s50.sensor_height}")
    print(f"Pixel Size: {s50.pixel_size()}")
    print(f"Full Well: {s50.full_well}e-")

    # S50 should be 50/250 = f/5
    assert s50.aperture.magnitude == 50
    assert s50.focal_length.magnitude == 250
    assert s50.focal_ratio() == 5.0
    assert s50.full_well == 11200

    # Verify S30 Pro
    print("\n[Seestar S30 Pro]")
    s30pro = ZwoTelescope.ZWO_Seestar_S30_Pro()
    print(f"Model: {s30pro.get_vendor()}")
    print(f"Aperture: {s30pro.aperture}")
    print(f"Focal Length: {s30pro.focal_length}")
    print(f"Focal Ratio: f/{s30pro.focal_ratio():.2f}")
    print(f"Sensor: {s30pro.sensor_width} x {s30pro.sensor_height}")
    print(f"Pixel Size: {s30pro.pixel_size()}")
    print(f"Full Well: {s30pro.full_well}e-")
    print(f"Dynamic Range: {s30pro.dynamic_range():.2f} stops")

    # S30 Pro should be 30/160 = f/5.33
    assert s30pro.aperture.magnitude == 30
    assert s30pro.focal_length.magnitude == 160
    assert round(s30pro.focal_ratio(), 2) == 5.33
    assert s30pro.full_well == 40000
    assert s30pro.sensor_width.magnitude == 11.13
    assert s30pro.pixel_size().magnitude == 2.9

    # Verify Sensors in Camera Database
    print("\n[Seestar Sensors - Camera Database]")
    s30pro_sensor = ZwoCamera.ZWO_Seestar_S30_Pro_Sensor()
    print(f"S30 Pro Sensor Full Well: {s30pro_sensor.full_well}e-")
    assert s30pro_sensor.full_well == 40000
    assert s30pro_sensor.sensor_width.magnitude == 11.13

    s50_sensor = ZwoCamera.ZWO_Seestar_S50_Sensor()
    print(f"S50 Sensor Full Well: {s50_sensor.full_well}e-")
    assert s50_sensor.full_well == 11200

    print("\n✅ All Seestar data integrity checks passed!")

if __name__ == "__main__":
    try:
        verify_seestar()
    except AssertionError as e:
        print(f"\n❌ Data Integrity Check FAILED: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"\n❌ An error occurred: {e}")
        sys.exit(1)
