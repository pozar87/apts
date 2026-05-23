import time
import sys
import os

# Add current directory to sys.path
sys.path.insert(0, os.getcwd())

start = time.time()
end = time.time()
print(f"Importing apts.units and accessing ureg took: {end - start:.4f}s")
