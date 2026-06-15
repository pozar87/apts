import logging
import math
import numpy as np
from ..fits_analyzer import FitsAnalyzer
from . import tracking, geometry, calculations, plotting

logger = logging.getLogger(__name__)


class PolarAlignment:
    def __init__(self, observation, target_star_name=None):
        self.observation = observation
        self.target_star_name = target_star_name
        self.rotation_frames = []
        self.adjustment_frames = []
        self.mount_axis_image = None  # (x, y) in pixels
        self.pixel_scale = None  # arcsec/pixel
        self.orientation = None  # degrees (angle of RA axis in image)

    def add_frame(self, filepath, ra_rotation_deg=0, phase="rotation"):
        """
        Analyzes a frame and tracks the target star.
        """
        analyzer = FitsAnalyzer(filepath)
        analyzer.analyze()
        stars = analyzer.fitted_stars

        if not stars:
            logger.warning(f"No stars detected in {filepath}")
            return False

        target = None
        # Logic to find the target star
        if not self.rotation_frames and not self.adjustment_frames:
            # First frame ever: pick the brightest or find by name
            if self.target_star_name is None:
                detected = analyzer.stars
                if detected:
                    brightest = max(detected, key=lambda s: s["flux"])
                    target = min(
                        stars,
                        key=lambda s: (s["x"] - brightest["x"]) ** 2
                        + (s["y"] - brightest["y"]) ** 2,
                    )
                else:
                    target = stars[0]
            else:
                # Ideally we'd plate solve, but for now we pick brightest
                target = (
                    max(stars, key=lambda s: s.get("flux", 0))
                    if any("flux" in s for s in stars)
                    else stars[0]
                )
        else:
            # Track from previous frame (either from rotation or adjustment)
            prev_frame = (
                self.adjustment_frames[-1]
                if self.adjustment_frames
                else self.rotation_frames[-1]
            )
            prev_target = prev_frame["target"]
            prev_stars = prev_frame["stars"]

            # Robust tracking using relative positions (triangles/asterisms)
            target = tracking.robust_star_tracking(prev_target, prev_stars, stars)

            if target is None:
                # Fallback to proximity
                distances = [
                    (
                        (s["x"] - prev_target["x"]) ** 2
                        + (s["y"] - prev_target["y"]) ** 2,
                        s,
                    )
                    for s in stars
                ]
                min_dist_sq, target = min(distances, key=lambda d: d[0])

                if min_dist_sq > 100**2:
                    logger.warning(
                        f"Large star tracking jump detected: {math.sqrt(min_dist_sq):.1f} pixels"
                    )

        frame_data = {
            "filepath": filepath,
            "ra_rotation": ra_rotation_deg,
            "target": target,
            "stars": stars,
            "width": analyzer.data.shape[1],
            "height": analyzer.data.shape[0],
            "timestamp": self.observation.place.ts.utc(
                self.observation.observation_local_time
            ),
        }

        if phase == "rotation":
            self.rotation_frames.append(frame_data)
        else:
            self.adjustment_frames.append(frame_data)

        return True

    def _fit_circle(self):
        """
        Fits a circle to the tracked target star positions to find the center of rotation.
        Supports 2 points (using RA rotation) or 3+ points (general circle fit).
        """
        self.mount_axis_image = geometry.fit_circle(self.rotation_frames)

        # Estimate orientation and pixel scale
        if self.mount_axis_image is not None:
            self.pixel_scale, self.orientation = geometry.estimate_sensor_params(
                self.rotation_frames,
                self.mount_axis_image,
                self.observation,
                self.target_star_name
            )

        return self.mount_axis_image

    def calculate_correction(self):
        """
        Calculates the required corrections for Altitude and Azimuth knobs.
        """
        if self.mount_axis_image is None:
            self._fit_circle()

        return calculations.calculate_correction(
            self.observation,
            self.target_star_name,
            self.mount_axis_image,
            self.pixel_scale,
            self.rotation_frames,
            self.adjustment_frames
        )

    def generate_alignment_map(self, dark_mode=True):
        """
        Generates a visual guide showing the star, RA axis, and the required correction.
        """
        correction = self.calculate_correction()
        return plotting.generate_alignment_map(correction, dark_mode=dark_mode)
