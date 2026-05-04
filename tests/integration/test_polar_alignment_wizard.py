import unittest
import os
import numpy as np
from astropy.io import fits
from unittest.mock import MagicMock
from datetime import datetime
from skyfield.api import utc

from apts.utils.polar_alignment import PolarAlignmentWizard

class TestPolarAlignmentWizardIntegration(unittest.TestCase):
    def setUp(self):
        self.temp_files = []
        self.mock_observation = MagicMock()
        self.mock_observation.effective_date = datetime(2025, 1, 1, 20, 0, 0, tzinfo=utc)
        self.mock_observation.observation_local_time = self.mock_observation.effective_date

        # Warsaw
        self.lat = 52.2
        self.lon = 21.0
        self.mock_observation.place.lat_decimal = self.lat
        self.mock_observation.place.lon_decimal = self.lon

        # Mock star: Polaris-like
        self.star_name = "Polaris"
        self.star_ra = 2.5 # hours
        self.star_dec = 89.2 # degrees

        self.mock_star = MagicMock()
        self.mock_star.ra.hours = self.star_ra
        self.mock_star.dec.degrees = self.star_dec
        self.mock_observation.local_stars.find_by_name.return_value = self.mock_star

        # Mock time and altaz
        self.mock_time = MagicMock()
        self.mock_time.gmst = 2.5 # LST will be 2.5 + 21/15 = 3.9h.
        # Actually let's make LST = RA for simplicity (H=0)
        # LST = GMST + LON/15 => GMST = LST - LON/15 = 2.5 - 21/15 = 2.5 - 1.4 = 1.1
        self.mock_time.gmst = 1.1
        self.mock_observation.place.ts.utc.return_value = self.mock_time

        # At H=0, Polaris is at its highest culmination (approx)
        # Alt = lat + (90 - dec) = 52.2 + 0.8 = 53.0
        # Az = 0 (North)
        self.star_alt = 53.0
        self.star_az = 0.0

        mock_altaz_obj = MagicMock()
        mock_altaz_obj.altaz.return_value = (MagicMock(degrees=self.star_alt), MagicMock(degrees=self.star_az), None)
        self.mock_observation.place.observer.at.return_value.observe.return_value.apparent.return_value = mock_altaz_obj

    def tearDown(self):
        for f in self.temp_files:
            if os.path.exists(f):
                os.remove(f)

    def create_synthetic_fits(self, filename, star_x, star_y, width=1000, height=1000):
        data = np.random.normal(100, 5, (height, width)).astype(np.float32)
        y, x = np.mgrid[0:height, 0:width]
        # Star blob
        star = 5000 * np.exp(-((x - star_x)**2 + (y - star_y)**2) / (2 * 2.0**2))
        data += star.astype(np.float32)

        hdu = fits.PrimaryHDU(data)
        # Add some minimal header
        hdu.header['EXPTIME'] = 1.0
        hdu.writeto(filename, overwrite=True)
        self.temp_files.append(filename)
        return filename

    def test_full_wizard_workflow(self):
        wizard = PolarAlignmentWizard(self.mock_observation)
        wizard.select_star(self.star_name)

        # Simulation parameters
        # Center of rotation (RA axis) at (500, 500)
        center_x, center_y = 500, 500
        # Radius: 0.8 degrees. Let's assume 30 arcsec/pixel => 96 pixels
        radius = 96

        # Rotation frames
        # RA 0 deg: star at (596, 500)
        f1 = self.create_synthetic_fits("rot_0.fits", center_x + radius, center_y)
        wizard.add_rotation_frame(f1, 0)

        # RA 90 deg: star at (500, 596)
        f2 = self.create_synthetic_fits("rot_90.fits", center_x, center_y + radius)
        wizard.add_rotation_frame(f2, 90)

        # RA 180 deg: star at (404, 500)
        f3 = self.create_synthetic_fits("rot_180.fits", center_x - radius, center_y)
        wizard.add_rotation_frame(f3, 180)

        # Calculate
        correction = wizard.calculate()

        self.assertIsNotNone(correction)
        # Check if RA axis found is close to (500, 500)
        np.testing.assert_allclose(correction["mount_axis_image"], [center_x, center_y], atol=1.0)

        # Check if pixel scale is close to 30 arcsec/pixel
        # Star is 0.8 deg from pole = 2880 arcsec. 2880 / 96 pixels = 30.0
        self.assertAlmostEqual(wizard.pa.pixel_scale, 30.0, delta=0.5)

        # Now test adjustment phase
        wizard.start_adjustment()

        # Simulate moving the star to a new position (e.g. adjustment made)
        # If the mount was misaligned, the NCP position in the image would be somewhere else.
        # Given our "perfect" rotation simulation, if the wizard thinks the NCP is at (500, 500)
        # then error should be near 0.

        f_adj = self.create_synthetic_fits("adj_1.fits", center_x + radius, center_y)
        adj_correction = wizard.add_adjustment_frame(f_adj)

        self.assertIsNotNone(adj_correction)
        # Error should be reasonably small in this "perfect" case
        # (Numerical errors and noise might give a small error)
        self.assertLess(wizard.error, 10.0) # Within 10 arcmin for a synthetic test with noise

    def test_iterative_adjustment(self):
        wizard = PolarAlignmentWizard(self.mock_observation)
        wizard.select_star(self.star_name)

        center_x, center_y = 500, 500
        radius = 96 # pixels

        # Calibration (rotation)
        wizard.add_rotation_frame(self.create_synthetic_fits("rot_0.fits", center_x + radius, center_y), 0)
        wizard.add_rotation_frame(self.create_synthetic_fits("rot_90.fits", center_x, center_y + radius), 90)

        wizard.calculate()
        wizard.start_adjustment()

        # Initial bad position: star at (620, 500) instead of (596, 500)
        # Offset is 24 pixels = 24 * 30 = 720 arcsec = 12 arcmin
        wizard.add_adjustment_frame(self.create_synthetic_fits("adj_iter_1.fits", 620, 500))
        error1 = wizard.error

        # Intermediate improvement: star at (608, 500)
        wizard.add_adjustment_frame(self.create_synthetic_fits("adj_iter_2.fits", 608, 500))
        error2 = wizard.error

        # Almost perfect: star at (596, 500)
        wizard.add_adjustment_frame(self.create_synthetic_fits("adj_iter_3.fits", 596, 500))
        error3 = wizard.error

        self.assertGreater(error1, error2)
        self.assertGreater(error2, error3)
        self.assertLess(error3, 5.0)

if __name__ == "__main__":
    unittest.main()
