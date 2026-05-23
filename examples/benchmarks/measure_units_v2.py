import time
import sys
import os

# Add current directory to sys.path
sys.path.insert(0, os.getcwd())

start = time.time()
from apts.units import ureg  # noqa: E402
end = time.time()
print(f"Importing apts.units took: {end - start:.4f}s")

start = time.time()
_ = ureg.mm
end = time.time()
print(f"Accessing ureg.mm took: {end - start:.4f}s")
