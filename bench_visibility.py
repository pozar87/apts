import numpy as np
import time

def calculate_refraction(alt_deg):
    alt_deg_arr = np.atleast_1d(alt_deg)
    refraction_deg = np.zeros_like(alt_deg_arr, dtype=float)
    mask = alt_deg_arr > -1.0
    if np.any(mask):
        r_arcmin = 1.0 / np.tan(
            np.deg2rad(alt_deg_arr[mask] + 7.31 / (alt_deg_arr[mask] + 4.4))
        )
        refraction_deg[mask] = r_arcmin / 60.0
    return refraction_deg

def test(N, M):
    lat = 52.0
    sin_lat = np.sin(np.deg2rad(lat))
    cos_lat = np.cos(np.deg2rad(lat))
    ras = np.random.rand(N) * 24.0
    decs = np.random.rand(N) * 180.0 - 90.0
    lsts = np.random.rand(M) * 24.0

    # 1. Original
    start = time.time()
    ra_rad = np.deg2rad(ras * 15.0)[:, np.newaxis]
    dec_rad = np.deg2rad(decs)[:, np.newaxis]
    sin_ra = np.sin(ra_rad)
    cos_ra = np.cos(ra_rad)
    sin_dec = np.sin(dec_rad)
    cos_dec = np.cos(dec_rad)
    tan_dec = np.tan(dec_rad)

    lst_rad = np.deg2rad(lsts * 15.0)[np.newaxis, :]
    sin_lst = np.sin(lst_rad)
    cos_lst = np.cos(lst_rad)

    cos_h = cos_lst * cos_ra + sin_lst * sin_ra
    sin_h = sin_lst * cos_ra - cos_lst * sin_ra

    sin_alt = sin_lat * sin_dec + cos_lat * cos_dec * cos_h
    true_alt_deg = np.rad2deg(np.arcsin(np.clip(sin_alt, -1.0, 1.0)))
    apparent_alt_deg = true_alt_deg + calculate_refraction(true_alt_deg)

    x = cos_h * sin_lat - tan_dec * cos_lat
    y = sin_h
    az_deg = (np.rad2deg(np.arctan2(y, x)) + 180.0) % 360.0

    res1 = np.any(apparent_alt_deg > 30, axis=1)
    dur1 = time.time() - start

    # 2. Pre-filter by dec
    start = time.time()
    max_alt = 90 - np.abs(lat - decs)
    potential_mask = max_alt + calculate_refraction(max_alt) > 30

    active_ras = ras[potential_mask]
    active_decs = decs[potential_mask]

    if np.any(potential_mask):
        ra_rad = np.deg2rad(active_ras * 15.0)[:, np.newaxis]
        dec_rad = np.deg2rad(active_decs)[:, np.newaxis]
        sin_ra = np.sin(ra_rad)
        cos_ra = np.cos(ra_rad)
        sin_dec = np.sin(dec_rad)
        cos_dec = np.cos(dec_rad)
        tan_dec = np.tan(dec_rad)

        lst_rad = np.deg2rad(lsts * 15.0)[np.newaxis, :]
        sin_lst = np.sin(lst_rad)
        cos_lst = np.cos(lst_rad)

        cos_h = cos_lst * cos_ra + sin_lst * sin_ra
        sin_h = sin_lst * cos_ra - cos_lst * sin_ra

        sin_alt = sin_lat * sin_dec + cos_lat * cos_dec * cos_h
        true_alt_deg = np.rad2deg(np.arcsin(np.clip(sin_alt, -1.0, 1.0)))
        apparent_alt_deg = true_alt_deg + calculate_refraction(true_alt_deg)

        x = cos_h * sin_lat - tan_dec * cos_lat
        y = sin_h
        az_deg = (np.rad2deg(np.arctan2(y, x)) + 180.0) % 360.0

        res_active = np.any(apparent_alt_deg > 30, axis=1)
        res2 = np.zeros(N, dtype=bool)
        res2[potential_mask] = res_active
    else:
        res2 = np.zeros(N, dtype=bool)

    dur2 = time.time() - start

    print(f"Original: {dur1:.4f}s")
    print(f"Filtered: {dur2:.4f}s")
    print(f"Match: {np.array_equal(res1, res2)}, Active: {np.sum(potential_mask)}/{N}")

test(14000, 100)
