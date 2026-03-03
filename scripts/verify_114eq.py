from apts.opticalequipment.telescope.vendors.celestron import CelestronTelescope

def test_114eq():
    telescope = CelestronTelescope.Celestron_AstroMaster_114EQ()
    print(f"Vendor: {telescope.get_vendor()}")
    print(f"Type: {telescope.telescope_type}")
    print(f"Aperture: {telescope.aperture}")
    print(f"Focal Length: {telescope.focal_length}")
    print(f"Focal Ratio: {telescope.focal_ratio()}")
    print(f"Central Obstruction: {telescope.central_obstruction}")
    print(f"Mass: {telescope.mass}")
    print(f"Connection: {telescope.connection_type}")

if __name__ == "__main__":
    test_114eq()
