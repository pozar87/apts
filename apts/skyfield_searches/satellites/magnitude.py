import numpy as np

def calculate_satellite_magnitude(
    satellite_name, sat_pos_km, sun_pos_km, observer_pos_km, distance_km
):
    """Calculates the apparent magnitude of a satellite."""
    # Vector from satellite to sun
    vec_sat_sun = sun_pos_km - sat_pos_km

    # Vector from satellite to observer
    vec_sat_obs = observer_pos_km - sat_pos_km

    # Calculate phase angle beta
    norm_sun = np.linalg.norm(vec_sat_sun)
    norm_obs = np.linalg.norm(vec_sat_obs)

    if norm_sun > 0 and norm_obs > 0:
        cos_beta = np.dot(vec_sat_sun, vec_sat_obs) / (norm_sun * norm_obs)
        beta = np.arccos(np.clip(cos_beta, -1.0, 1.0))

        # Phase function for diffuse sphere
        phi = (np.sin(beta) + (np.pi - beta) * np.cos(beta)) / np.pi

        # Standard magnitude (at 1000km, 0 phase)
        # ISS is approx -1.8, Tiangong is approx 0.0
        m_std = -1.8 if "ISS" in satellite_name else 0.0

        # Apparent magnitude
        return float(
            m_std + 5 * np.log10(distance_km / 1000.0) - 2.5 * np.log10(max(phi, 1e-9))
        )
    return 5.0
