import os
import struct
import xml.etree.ElementTree as ET
import zlib
import re
import numpy as np
from astropy.io import fits

def is_xisf(filepath):
    """
    Checks if a file is in XISF format.
    """
    try:
        with open(filepath, "rb") as f:
            return f.read(8) == b"XISF0100"
    except OSError:
        return False

def byte_unshuffle(data_bytes, item_size):
    """
    Unshuffles bytes for XISF decompression.
    """
    n_bytes = len(data_bytes)
    if item_size <= 1 or n_bytes < item_size:
        return data_bytes
    n_elements = n_bytes // item_size
    usable = n_elements * item_size
    arr = np.frombuffer(data_bytes[:usable], dtype=np.uint8)
    unshuffled = arr.reshape(item_size, n_elements).T.tobytes()
    if usable < n_bytes:
        unshuffled += data_bytes[usable:]
    return unshuffled

def load_xisf(filepath):
    """
    Loads image data and header from an XISF file.
    """
    with open(filepath, "rb") as f:
        magic = f.read(8)
        if magic != b"XISF0100":
            raise ValueError("Not a valid XISF file (bad magic)")
        header_len, _reserved = struct.unpack("<II", f.read(8))
        xml_bytes = f.read(header_len)
        xml_str = xml_bytes.decode("utf-8", errors="replace")
        xml_str = re.sub(r'\s+xmlns\s*=\s*["\'][^"\']*["\']', "", xml_str)
        root = ET.fromstring(xml_str)
        img_el = root.find(".//Image")
        if img_el is None:
            raise ValueError("No Image element found in XISF header")
        geom = img_el.get("geometry", "")
        parts = geom.split(":")
        width = int(parts[0])
        height = int(parts[1])
        channels = int(parts[2]) if len(parts) > 2 else 1
        sample_fmt = img_el.get("sampleFormat", "Float32")
        dtype_map = {
            "UInt8": np.uint8,
            "UInt16": np.uint16,
            "UInt32": np.uint32,
            "UInt64": np.uint64,
            "Int8": np.int8,
            "Int16": np.int16,
            "Int32": np.int32,
            "Int64": np.int64,
            "Float32": np.float32,
            "Float64": np.float64,
        }
        dtype = dtype_map.get(sample_fmt)
        pixel_storage = img_el.get("pixelStorage", "planar")
        location = img_el.get("location", "")
        compression = img_el.get("compression", "")
        if location.startswith("attachment:"):
            loc_parts = location.split(":")
            offset = int(loc_parts[1])
            size = int(loc_parts[2])
            f.seek(offset)
            raw = f.read(size)
        else:
            raise ValueError(f"Unsupported XISF location: {location}")

        if compression:
            comp_parts = compression.split(":")
            codec = comp_parts[0].lower()
            shuffle_item_size = (
                int(comp_parts[2])
                if len(comp_parts) > 2
                else np.dtype(dtype).itemsize
            )
            byte_shuffle = "+sh" in codec
            base_codec = codec.replace("+sh", "")
            if base_codec == "zlib":
                raw = zlib.decompress(raw)
            else:
                raise ValueError(f"Unsupported XISF compression: {codec}")
            if byte_shuffle:
                raw = byte_unshuffle(raw, shuffle_item_size)

        data = np.frombuffer(raw, dtype=dtype)
        if channels > 1:
            if pixel_storage == "planar":
                data = data.reshape(channels, height, width)[0]
            else:
                data = data.reshape(height, width, channels)[:, :, 0]
        else:
            data = data.reshape(height, width)

    header = {"XISF": True, "NAXIS1": width, "NAXIS2": height}
    return data, header

def load_data(filepath):
    """
    Generic loader for FITS and XISF files.
    """
    name_lower = os.path.basename(filepath).lower()
    if name_lower.endswith(".xisf") or is_xisf(filepath):
        return load_xisf(filepath)
    else:
        with fits.open(filepath) as hdul:
            data = None
            header = None
            for hdu in hdul:
                hdu_data = getattr(hdu, "data", None)
                if hdu_data is not None and hdu_data.ndim >= 2:
                    data = hdu_data
                    header = getattr(hdu, "header", None)
                    break
            if data is None:
                raise ValueError("No image data found in FITS file")
            return data, header
