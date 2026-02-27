from apts.opticalequipment.telescope.vendors.celestron import CelestronTelescope
from apts.opticalequipment.telescope.base import TelescopeType
from apts.units import get_unit_registry

def verify_astrofi_130():
    ureg = get_unit_registry()
    telescope = CelestronTelescope.Celestron_AstroFi_130()

    print(f"Model: {telescope.vendor}")
    print(f"Aperture: {telescope.aperture}")
    print(f"Focal Length: {telescope.focal_length}")
    print(f"Central Obstruction: {telescope.central_obstruction}")
    print(f"Mass: {telescope.mass}")
    print(f"Type: {telescope.telescope_type}")

    assert telescope.aperture == 130 * ureg.mm
    assert telescope.focal_length == 650 * ureg.mm
    assert telescope.central_obstruction == 38 * ureg.mm
    assert telescope.mass == 3628 * ureg.gram
    assert telescope.telescope_type == TelescopeType.NEWTONIAN_REFLECTOR

    # Check calculated focal ratio
    expected_focal_ratio = 650 / 130
    assert telescope.focal_ratio().magnitude == expected_focal_ratio
    print(f"Focal Ratio: {telescope.focal_ratio()}")

    print("Verification successful!")

if __name__ == "__main__":
    verify_astrofi_130()
