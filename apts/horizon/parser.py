import os
import configparser
from typing import Tuple, List

def parse_horizon_content(content: str) -> Tuple[List[float], List[float]]:
    """
    Parses a string content for azimuth and altitude data points.
    Expects lines starting with space-separated float numbers (azimuth, altitude).
    Comments starting with '#' or ';' are ignored.
    """
    az = []
    alt = []
    for line in content.splitlines():
        line = line.strip()
        if not line or line.startswith(("#", ";")):
            continue
        parts = line.split()
        if len(parts) >= 2:
            try:
                az.append(float(parts[0]))
                alt.append(float(parts[1]))
            except ValueError:
                continue
    return az, alt


def parse_horizon_file(file_path: str) -> Tuple[List[float], List[float]]:
    """
    Parses a file containing azimuth and altitude data points.
    Supports Stellarium-style landscape ini files which refer to .hrz files,
    as well as raw .hrz data files directly.
    """
    if file_path.lower().endswith(".ini"):
        config = configparser.ConfigParser()
        try:
            config.read(file_path)
            if config.has_section("landscape") and config.has_option(
                "landscape", "polygonal_horizon_list"
            ):
                hrz_filename = config.get("landscape", "polygonal_horizon_list")
                # Assume .hrz is in the same directory as .ini
                hrz_path = os.path.join(os.path.dirname(file_path), hrz_filename)
                if os.path.exists(hrz_path):
                    file_path = hrz_path
                else:
                    return [], []
            else:
                return [], []
        except Exception:
            return [], []

    with open(file_path, "r") as f:
        content = f.read()
    return parse_horizon_content(content)


def process_horizon_data(az: List[float], alt: List[float]) -> Tuple[List[float], List[float]]:
    """
    Processes the raw azimuth and altitude lists by:
    1. Ensuring data is sorted by azimuth.
    2. Ensuring both azimuth 0.0 and 360.0 boundaries are covered for continuous interpolation.
    """
    if not az:
        return [], []

    # Ensure sorted
    data = sorted(zip(az, alt))
    az, alt = map(list, zip(*data))

    # Ensure 0 and 360 are covered for interpolation
    if az[0] > 0:
        if az[-1] == 360.0:
            az.insert(0, 0.0)
            alt.insert(0, alt[-1])
        else:
            az.insert(0, 0.0)
            alt.insert(0, alt[0])

    if az[-1] < 360.0:
        az.append(360.0)
        alt.append(alt[0])

    return az, alt
