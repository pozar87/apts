import numpy as np

def fit_circle(rotation_frames):
    """
    Fits a circle to the tracked target star positions to find the center of rotation.
    Supports 2 points (using RA rotation) or 3+ points (general circle fit).
    """
    if len(rotation_frames) < 2:
        return None

    points = np.array(
        [(f["target"]["x"], f["target"]["y"]) for f in rotation_frames]
    )
    rotations = np.array([f["ra_rotation"] for f in rotation_frames])

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
        return m + h * n
    else:
        # 3+ points: General circle fit
        A = np.column_stack([2 * points[:, 0], 2 * points[:, 1], np.ones(len(points))])
        b = points[:, 0] ** 2 + points[:, 1] ** 2
        res, _, _, _ = np.linalg.lstsq(A, b, rcond=None)
        return res[:2]

def estimate_sensor_params(rotation_frames, mount_axis_image, observation, target_star_name):
    """
    Estimates camera orientation and pixel scale.
    """
    if len(rotation_frames) < 2 or mount_axis_image is None:
        return None, None

    p1 = np.array(
        [rotation_frames[0]["target"]["x"], rotation_frames[0]["target"]["y"]]
    )
    c = mount_axis_image

    # Radius in pixels
    r_px = np.linalg.norm(p1 - c)

    pixel_scale = None
    if target_star_name:
        target_star = observation.local_stars.find_by_name(target_star_name)
        if target_star:
            dec = target_star.dec.degrees
            # Distance from pole in degrees
            dist_deg = 90.0 - abs(dec)
            # radius in arcsec
            r_arcsec = dist_deg * 3600.0
            pixel_scale = r_arcsec / r_px if r_px > 0 else None

    # Orientation: Angle of the vector from center to p1 at ra_rotation[0]
    v = p1 - c
    orientation = np.degrees(np.arctan2(v[1], v[0]))

    return pixel_scale, orientation
