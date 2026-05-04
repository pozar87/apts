import logging
import math
import io
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from ..constants import ObjectTableLabels
from .fits_analyzer import FitsAnalyzer

logger = logging.getLogger(__name__)

def suggest_polar_alignment_stars(observation, magnitude_limit=4.0, min_alt=20, max_alt=70):
    """
    Suggests bright stars for polar alignment based on current visibility and horizon.
    Optimal stars are between 20 and 70 degrees in altitude.
    """
    if observation.effective_date is None:
        logger.warning("Observation effective_date is None, cannot suggest stars.")
        return pd.DataFrame()

    # We want stars visible AT THE MOMENT of alignment
    start_time = observation.observation_local_time
    if start_time is None:
        # Fallback to place date
        if hasattr(observation.place.date, 'utc_datetime'):
            start_time = observation.place.date.utc_datetime()
        else:
            start_time = observation.place.date

    # Use a very short window for 'now'
    if isinstance(start_time, pd.Timestamp):
        stop_time = start_time + pd.Timedelta(seconds=1)
    elif isinstance(start_time, (int, float)):
        # Probably shouldn't happen but let's be safe
        stop_time = start_time + 1/86400.0
    else:
        from datetime import timedelta
        try:
            stop_time = start_time + timedelta(seconds=1)
        except:
            # Last resort
            stop_time = start_time

    visible_stars = observation.local_stars.get_visible(
        observation.conditions,
        start_time,
        stop_time,
        star_magnitude_limit=magnitude_limit
    )

    if visible_stars.empty:
        return visible_stars

    # Filter by altitude range
    # Note: get_visible ensures ALTITUDE is computed for visible objects
    mask = (visible_stars[ObjectTableLabels.ALTITUDE] >= min_alt) & \
           (visible_stars[ObjectTableLabels.ALTITUDE] <= max_alt)

    candidates = visible_stars[mask].copy()

    # Sort by brightness
    if "Magnitude_float" in candidates.columns:
        candidates = candidates.sort_values(by="Magnitude_float")

    return candidates

class PolarAlignment:
    def __init__(self, observation, target_star_name=None):
        self.observation = observation
        self.target_star_name = target_star_name
        self.rotation_frames = []
        self.adjustment_frames = []
        self.mount_axis_image = None  # (x, y) in pixels
        self.pixel_scale = None  # arcsec/pixel
        self.orientation = None  # degrees (angle of RA axis in image)

    def add_frame(self, filepath, ra_rotation_deg=0, phase='rotation'):
        """
        Analyzes a frame and tracks the target star.
        """
        analyzer = FitsAnalyzer(filepath)
        summary = analyzer.analyze()
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
                target = max(stars, key=lambda s: s.get("flux", 0)) if any("flux" in s for s in stars) else stars[0]
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
            # if we have enough stars in the previous frame.
            target = self._robust_star_tracking(prev_target, prev_stars, stars)

            if target is None:
                # Fallback to proximity
                distances = [
                    ((s["x"] - prev_target["x"]) ** 2 + (s["y"] - prev_target["y"]) ** 2, s)
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
            "timestamp": self.observation.place.ts.utc(self.observation.observation_local_time)
        }

        if phase == 'rotation':
            self.rotation_frames.append(frame_data)
        else:
            self.adjustment_frames.append(frame_data)

        return True

    def _robust_star_tracking(self, prev_target, prev_stars, current_stars):
        """
        Attempts to find the target star in the current frame by comparing
        the local configuration of stars (asterism).
        """
        if len(prev_stars) < 3 or len(current_stars) < 3:
            return None

        # 1. Select a few bright neighbors of the target in the previous frame
        def dist(s1, s2):
            return math.sqrt((s1["x"] - s2["x"]) ** 2 + (s1["y"] - s2["y"]) ** 2)

        # Use only high-confidence stars (high flux) for neighbors to be robust against noise
        min_flux = prev_target.get("flux", 0) * 0.1
        neighbors = sorted(
            [s for s in prev_stars if dist(s, prev_target) > 1.0 and s.get("flux", 0) > min_flux],
            key=lambda s: dist(s, prev_target)
        )[:5] # Take up to 5 closest neighbors

        if not neighbors:
            return None

        # Precompute relative distances from target to neighbors in previous frame
        target_to_neighbors_dists = [dist(prev_target, n) for n in neighbors]

        # 2. For each star in the current frame, check if it has neighbors at similar distances
        best_star = None
        best_match_count = 0

        for s_curr in current_stars:
            curr_neighbors_dists = sorted([dist(s_curr, other) for other in current_stars if dist(s_curr, other) > 1.0])

            match_count = 0
            # Also consider flux similarity
            flux_ratio = s_curr.get("flux", 0) / prev_target.get("flux", 1)
            if flux_ratio < 0.5 or flux_ratio > 2.0:
                # Too much flux difference, likely not the same star
                continue

            for d_target in target_to_neighbors_dists:
                # Find if any current neighbor distance matches d_target within tolerance (e.g. 5%)
                for d_curr in curr_neighbors_dists:
                    if d_curr > d_target * 1.1: # Too far
                        break
                    if abs(d_curr - d_target) < max(2.0, d_target * 0.10): # Relaxed to 10%
                        match_count += 1
                        break

            if match_count > best_match_count:
                best_match_count = match_count
                best_star = s_curr

        # We need a significant match (e.g. at least 2 neighbors matching distances)
        if best_match_count >= min(2, len(neighbors)):
            return best_star

        return None

    def _fit_circle(self):
        """
        Fits a circle to the tracked target star positions to find the center of rotation.
        Supports 2 points (using RA rotation) or 3+ points (general circle fit).
        """
        if len(self.rotation_frames) < 2:
            return None

        points = np.array([(f["target"]["x"], f["target"]["y"]) for f in self.rotation_frames])
        rotations = np.array([f["ra_rotation"] for f in self.rotation_frames])

        if len(points) == 2:
            # Solve for center using 2 points and known rotation angle
            p1, p2 = points[0], points[1]
            theta = np.radians(rotations[1] - rotations[0])

            # Midpoint
            m = (p1 + p2) / 2
            # Distance between points
            d = np.linalg.norm(p2 - p1)

            if abs(theta) < 1e-6:
                return None

            # Distance from midpoint to center
            # h = (d/2) / tan(theta/2)
            h = (d / 2) / np.tan(theta / 2)

            # Unit vector p1 -> p2
            v = (p2 - p1) / d
            # Perpendicular vector
            n = np.array([-v[1], v[0]])

            # Center is m + h*n or m - h*n depending on rotation direction
            self.mount_axis_image = m + h * n
        else:
            # 3+ points: General circle fit
            A = np.column_stack([2 * points[:, 0], 2 * points[:, 1], np.ones(len(points))])
            b = points[:, 0] ** 2 + points[:, 1] ** 2
            res, _, _, _ = np.linalg.lstsq(A, b, rcond=None)
            self.mount_axis_image = res[:2]

        # Estimate orientation and pixel scale
        self._estimate_sensor_params()

        return self.mount_axis_image

    def _estimate_sensor_params(self):
        """
        Estimates camera orientation and pixel scale.
        """
        if len(self.rotation_frames) < 2 or self.mount_axis_image is None:
            return

        p1 = np.array([self.rotation_frames[0]["target"]["x"], self.rotation_frames[0]["target"]["y"]])
        c = self.mount_axis_image

        # Radius in pixels
        r_px = np.linalg.norm(p1 - c)

        target_star = None
        if self.target_star_name:
            target_star = self.observation.local_stars.find_by_name(self.target_star_name)

        if target_star:
            dec = target_star.dec.degrees
            # Distance from pole in degrees
            dist_deg = 90.0 - abs(dec)
            # radius in arcsec
            r_arcsec = dist_deg * 3600.0
            self.pixel_scale = r_arcsec / r_px if r_px > 0 else None

        # Orientation: Angle of the vector from center to p1 at ra_rotation[0]
        v = p1 - c
        self.orientation = np.degrees(np.arctan2(v[1], v[0]))

    def calculate_correction(self):
        """
        Calculates the required corrections for Altitude and Azimuth knobs.
        Uses parallactic angle and sensor orientation to map image-space errors
        to topocentric mount adjustments.
        """
        if self.mount_axis_image is None:
            self._fit_circle()

        if self.mount_axis_image is None or self.pixel_scale is None:
            logger.warning("Mount axis or pixel scale not determined. Add more frames.")
            return None

        # 1. Get true coordinates of the Celestial Pole and the Star
        lat = self.observation.place.lat_decimal
        pole_alt = abs(lat)
        pole_az = 0.0 if lat >= 0 else 180.0

        if self.target_star_name is None:
            logger.warning("Target star name not specified.")
            return None

        target_star = self.observation.local_stars.find_by_name(self.target_star_name)
        if target_star is None:
            logger.warning(f"Target star {self.target_star_name} not found in catalog.")
            return None

        # Use latest frame for correction feedback
        latest_frame = self.adjustment_frames[-1] if self.adjustment_frames else self.rotation_frames[-1]
        t = latest_frame["timestamp"]

        obs_pos = self.observation.place.observer.at(t).observe(target_star).apparent()
        alt, az, _ = obs_pos.altaz()
        star_alt, star_az = alt.degrees, az.degrees
        star_dec = target_star.dec.degrees

        # 2. Calculate Parallactic Angle (q)
        lat_rad = np.radians(lat)
        alt_rad = np.radians(star_alt)
        dec_rad = np.radians(star_dec)

        # Find Hour Angle (H)
        lst = t.gmst + self.observation.place.lon_decimal / 15.0
        h_rad = np.radians((lst - target_star.ra.hours) * 15.0)

        # Standard formula for q
        sin_q = np.sin(h_rad) * np.cos(lat_rad) / np.cos(dec_rad)
        cos_q = (np.sin(lat_rad) - np.sin(alt_rad) * np.sin(dec_rad)) / (np.cos(alt_rad) * np.cos(dec_rad))
        q = np.arctan2(sin_q, cos_q)

        # 3. Determine Image Orientation in Alt/Az space
        p_current = np.array([latest_frame["target"]["x"], latest_frame["target"]["y"]])
        c = self.mount_axis_image
        v_pole_img = c - p_current
        angle_pole_img = np.arctan2(v_pole_img[1], v_pole_img[0])

        # Direction of "Up" (Alt+) in image is towards Pole rotated by -q
        # q is Zenith -> Pole angle. So Zenith is at -q from Pole.
        angle_alt_img = angle_pole_img - q
        u_alt = np.array([np.cos(angle_alt_img), np.sin(angle_alt_img)])
        # Az+ (Eastward increase) is 90 degrees clockwise from Alt+ in the sky.
        # In a Y-down image, clockwise rotation is +pi/2.
        u_az = np.array([np.cos(angle_alt_img + np.pi/2), np.sin(angle_alt_img + np.pi/2)])

        # 4. Project Star-to-NCP vector into Image Space
        d_alt_sky = pole_alt - star_alt
        d_az_raw = pole_az - star_az
        if d_az_raw > 180: d_az_raw -= 360
        if d_az_raw < -180: d_az_raw += 360
        d_az_sky = d_az_raw * np.cos(np.radians((star_alt + pole_alt) / 2))

        # Expected position of NCP in image if mount was aligned
        ncp_image = p_current + (d_alt_sky * 3600 / self.pixel_scale) * u_alt + \
                         (d_az_sky * 3600 / self.pixel_scale) * u_az

        # 5. Calculate Misalignment Error Vector
        error_img = c - ncp_image

        # Decompose error into Alt and Az components
        err_alt = np.dot(error_img, u_alt) * self.pixel_scale / 3600.0
        err_az = np.dot(error_img, u_az) * self.pixel_scale / 3600.0 / np.cos(np.radians(pole_alt))

        total_error_arcmin = np.linalg.norm(error_img) * self.pixel_scale / 60.0

        # 6. Generate Instructions
        inst = []
        if abs(err_alt) > 1/60.0:
            inst.append(f"Move Altitude {'Down' if err_alt > 0 else 'Up'} {abs(err_alt*60):.1f}'")
        if abs(err_az) > 1/60.0:
            inst.append(f"Move Azimuth {'West' if err_az > 0 else 'East'} {abs(err_az*60):.1f}'")

        if not inst:
            inst.append("Alignment is excellent!")

        return {
            "error_arcmin": total_error_arcmin,
            "alt_error_deg": err_alt,
            "az_error_deg": err_az,
            "mount_axis_image": c,
            "ncp_image": ncp_image,
            "instructions": ". ".join(inst),
            "star_image": p_current,
            "u_alt": u_alt,
            "u_az": u_az
        }

    def generate_alignment_map(self, dark_mode=True):
        """
        Generates a visual guide showing the star, RA axis, and the required correction.
        """
        correction = self.calculate_correction()
        if correction is None:
            return None

        # Create plot
        fig, ax = plt.subplots(figsize=(8, 8))

        bg_color = "#1e1e1e" if dark_mode else "#ffffff"
        text_color = "#ffffff" if dark_mode else "#000000"
        fig.patch.set_facecolor(bg_color)
        ax.set_facecolor(bg_color)

        # Plot star position
        star = correction["star_image"]
        ax.scatter(star[0], star[1], c="yellow", s=100, label="Target Star", edgecolors="white", zorder=5)

        # Plot mount RA axis
        axis = correction["mount_axis_image"]
        ax.scatter(axis[0], axis[1], c="red", marker="x", s=100, label="Mount RA Axis", zorder=5)

        # Plot target NCP position
        ncp = correction["ncp_image"]
        ax.scatter(ncp[0], ncp[1], c="cyan", marker="+", s=100, label="Target NCP Position", zorder=5)

        # Draw correction vector
        ax.arrow(axis[0], axis[1], ncp[0] - axis[0], ncp[1] - axis[1],
                 color="green", width=2, head_width=10, length_includes_head=True,
                 label="Correction Vector", zorder=4)

        # Axis labels and title
        ax.set_title(f"Polar Alignment Guide - Error: {correction['error_arcmin']:.1f}'", color=text_color)
        ax.set_xlabel("Pixel X", color=text_color)
        ax.set_ylabel("Pixel Y", color=text_color)
        ax.tick_params(colors=text_color)

        # Legend
        ax.legend(facecolor=bg_color, labelcolor=text_color)

        # Reverse Y axis because image coordinates usually start from top
        ax.invert_yaxis()

        # Grid
        ax.grid(True, linestyle="--", alpha=0.3)

        # Output to bytes
        buf = io.BytesIO()
        plt.savefig(buf, format="png", bbox_inches="tight", facecolor=bg_color)
        plt.close(fig)
        buf.seek(0)
        return buf

class PolarAlignmentWizard:
    PHASE_SELECT_STAR = "SELECT_STAR"
    PHASE_ROTATION = "ROTATION"
    PHASE_ADJUSTMENT = "ADJUSTMENT"

    def __init__(self, observation):
        self.observation = observation
        self.pa = None
        self.phase = self.PHASE_SELECT_STAR
        self.error = None
        self.instructions = "Please select a target star for polar alignment."

    def select_star(self, star_name):
        self.pa = PolarAlignment(self.observation, target_star_name=star_name)
        self.phase = self.PHASE_ROTATION
        self.instructions = "Take the first frame at the home position (RA=0)."

    def add_rotation_frame(self, filepath, ra_rotation_deg):
        if self.phase != self.PHASE_ROTATION:
            raise ValueError(f"Not in rotation phase. Current phase: {self.phase}")
        success = self.pa.add_frame(filepath, ra_rotation_deg=ra_rotation_deg, phase='rotation')
        if success:
            if len(self.pa.rotation_frames) == 1:
                self.instructions = "Rotate RA (e.g. 60-90 degrees) and take another frame."
            elif len(self.pa.rotation_frames) >= 2:
                self.instructions = "Rotation data collected. You can add more frames or calculate the alignment."
        return success

    def calculate(self):
        if self.pa is None or len(self.pa.rotation_frames) < 2:
            raise ValueError("Need at least 2 rotation frames to calculate alignment.")
        correction = self.pa.calculate_correction()
        if correction:
            self.error = correction["error_arcmin"]
            self.instructions = f"Alignment calculated. Error: {self.error:.1f}'. {correction['instructions']}. Start adjustment phase for live feedback."
            return correction
        return None

    def start_adjustment(self):
        if self.pa is None or self.pa.mount_axis_image is None:
            # Try to calculate if not done yet
            self.calculate()
        self.phase = self.PHASE_ADJUSTMENT
        self.instructions = "Take adjustment frames for live feedback. Adjust Altitude and Azimuth knobs as instructed."

    def add_adjustment_frame(self, filepath):
        if self.phase != self.PHASE_ADJUSTMENT:
            raise ValueError(f"Not in adjustment phase. Current phase: {self.phase}")
        success = self.pa.add_frame(filepath, phase='adjustment')
        if success:
            correction = self.pa.calculate_correction()
            if correction:
                self.error = correction["error_arcmin"]
                self.instructions = f"Error: {self.error:.1f}'. {correction['instructions']}"
                return correction
        return None

    def get_status(self):
        return {
            "phase": self.phase,
            "error_arcmin": self.error,
            "instructions": self.instructions,
            "target_star": self.pa.target_star_name if self.pa else None,
            "rotation_frames_count": len(self.pa.rotation_frames) if self.pa else 0,
            "adjustment_frames_count": len(self.pa.adjustment_frames) if self.pa else 0
        }
