import numpy as np
import logging
from ...i18n import gettext_

logger = logging.getLogger(__name__)

def calculate_correction(
    observation,
    target_star_name,
    mount_axis_image,
    pixel_scale,
    rotation_frames,
    adjustment_frames
):
    """
    Calculates the required corrections for Altitude and Azimuth knobs.
    """
    if mount_axis_image is None or pixel_scale is None:
        logger.warning("Mount axis or pixel scale not determined. Add more frames.")
        return None

    # 1. Get true coordinates of the Celestial Pole and the Star
    lat = observation.place.lat_decimal
    pole_alt = abs(lat)
    pole_az = 0.0 if lat >= 0 else 180.0

    if target_star_name is None:
        logger.warning("Target star name not specified.")
        return None

    target_star = observation.local_stars.find_by_name(target_star_name)
    if target_star is None:
        logger.warning(f"Target star {target_star_name} not found in catalog.")
        return None

    # Use latest frame for correction feedback
    latest_frame = (
        adjustment_frames[-1]
        if adjustment_frames
        else rotation_frames[-1]
    )
    t = latest_frame["timestamp"]

    obs_pos = observation.place.observer.at(t).observe(target_star).apparent()
    alt, az, _ = obs_pos.altaz()
    star_alt, star_az = alt.degrees, az.degrees
    star_dec = target_star.dec.degrees

    # 2. Calculate Parallactic Angle (q)
    lat_rad = np.radians(lat)
    alt_rad = np.radians(star_alt)
    dec_rad = np.radians(star_dec)

    # Find Hour Angle (H)
    lst = t.gmst + observation.place.lon_decimal / 15.0
    h_rad = np.radians((lst - target_star.ra.hours) * 15.0)

    # Standard formula for q
    sin_q = np.sin(h_rad) * np.cos(lat_rad) / np.cos(dec_rad)
    cos_q = (np.sin(lat_rad) - np.sin(alt_rad) * np.sin(dec_rad)) / (
        np.cos(alt_rad) * np.cos(dec_rad)
    )
    q = np.arctan2(sin_q, cos_q)

    # 3. Determine Image Orientation in Alt/Az space
    p_current = np.array([latest_frame["target"]["x"], latest_frame["target"]["y"]])
    c = mount_axis_image
    v_pole_img = c - p_current
    angle_pole_img = np.arctan2(v_pole_img[1], v_pole_img[0])

    # Direction of "Up" (Alt+) in image is towards Pole rotated by -q
    # q is Zenith -> Pole angle. So Zenith is at -q from Pole.
    angle_alt_img = angle_pole_img - q
    u_alt = np.array([np.cos(angle_alt_img), np.sin(angle_alt_img)])
    # Az+ (Eastward increase) is 90 degrees clockwise from Alt+ in the sky.
    # In a Y-down image, clockwise rotation is +pi/2.
    u_az = np.array(
        [np.cos(angle_alt_img + np.pi / 2), np.sin(angle_alt_img + np.pi / 2)]
    )

    # 4. Project Star-to-NCP vector into Image Space
    d_alt_sky = pole_alt - star_alt
    d_az_raw = pole_az - star_az
    if d_az_raw > 180:
        d_az_raw -= 360
    if d_az_raw < -180:
        d_az_raw += 360
    d_az_sky = d_az_raw * np.cos(np.radians((star_alt + pole_alt) / 2))

    # Expected position of NCP in image if mount was aligned
    ncp_image = (
        p_current
        + (d_alt_sky * 3600 / pixel_scale) * u_alt
        + (d_az_sky * 3600 / pixel_scale) * u_az
    )

    # 5. Calculate Misalignment Error Vector
    error_img = c - ncp_image

    # Decompose error into Alt and Az components
    err_alt = np.dot(error_img, u_alt) * pixel_scale / 3600.0
    err_az = (
        np.dot(error_img, u_az)
        * pixel_scale
        / 3600.0
        / np.cos(np.radians(pole_alt))
    )

    total_error_arcmin = np.linalg.norm(error_img) * pixel_scale / 60.0

    # 6. Generate Instructions
    inst = []
    if abs(err_alt) > 1 / 60.0:
        inst.append(
            gettext_("Move Altitude {direction} {value:.1f}'").format(
                direction=gettext_("Down") if err_alt > 0 else gettext_("Up"),
                value=abs(err_alt*60)
            )
        )
    if abs(err_az) > 1 / 60.0:
        inst.append(
            gettext_("Move Azimuth {direction} {value:.1f}'").format(
                direction=gettext_("West") if err_az > 0 else gettext_("East"),
                value=abs(err_az*60)
            )
        )

    if not inst:
        inst.append(gettext_("Alignment is excellent!"))

    return {
        "error_arcmin": total_error_arcmin,
        "alt_error_deg": err_alt,
        "az_error_deg": err_az,
        "mount_axis_image": c,
        "ncp_image": ncp_image,
        "instructions": ". ".join(inst),
        "star_image": p_current,
        "u_alt": u_alt,
        "u_az": u_az,
    }
