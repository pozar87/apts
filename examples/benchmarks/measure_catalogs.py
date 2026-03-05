import time
import logging
import sys
import os

# Add current directory to sys.path to import apts
sys.path.insert(0, os.getcwd())

# Disable logging to avoid cluttering output
logging.basicConfig(level=logging.ERROR)

from apts.catalogs import Catalogs

def measure_catalogs():
    start = time.time()
    catalogs = Catalogs()
    end = time.time()
    print(f"First Catalogs() instantiation took: {end - start:.4f}s")

    start = time.time()
    _ = catalogs.MESSIER
    end = time.time()
    print(f"Accessing MESSIER took: {end - start:.4f}s")

    start = time.time()
    _ = catalogs.BRIGHT_STARS
    end = time.time()
    print(f"Accessing BRIGHT_STARS took: {end - start:.4f}s")

    start = time.time()
    _ = catalogs.NGC
    end = time.time()
    print(f"Accessing NGC took: {end - start:.4f}s")

if __name__ == "__main__":
    measure_catalogs()
