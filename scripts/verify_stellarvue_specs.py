import sys
import os

# Add the repository root to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from apts.opticalequipment.telescope.vendors.stellarvue import StellarvueTelescope

def verify_stellarvue():
    database = StellarvueTelescope._DATABASE
    success = True

    for key, expected in database.items():
        print(f"Verifying {key}...")
        try:
            # Instantiate the telescope
            scope = StellarvueTelescope.from_database(expected)

            # Check aperture
            if scope.aperture.magnitude != expected['aperture_mm']:
                print(f"  [FAIL] Aperture mismatch: expected {expected['aperture_mm']}, got {scope.aperture.magnitude}")
                success = False

            # Check focal length
            if scope.focal_length.magnitude != expected['focal_length_mm']:
                print(f"  [FAIL] Focal length mismatch: expected {expected['focal_length_mm']}, got {scope.focal_length.magnitude}")
                success = False

            # Check mass
            if scope.mass.magnitude != expected['mass']:
                print(f"  [FAIL] Mass mismatch: expected {expected['mass']}, got {scope.mass.magnitude}")
                success = False

            # Check central obstruction
            if scope.central_obstruction.magnitude != expected['central_obstruction_mm']:
                print(f"  [FAIL] Central obstruction mismatch: expected {expected['central_obstruction_mm']}, got {scope.central_obstruction.magnitude}")
                success = False

            if success:
                print(f"  [OK] {key} verified.")

        except Exception as e:
            print(f"  [ERROR] Failed to verify {key}: {e}")
            success = False

    if success:
        print("\nAll Stellarvue models verified successfully!")
    else:
        print("\nVerification failed for one or more Stellarvue models.")
        sys.exit(1)

if __name__ == "__main__":
    verify_stellarvue()
