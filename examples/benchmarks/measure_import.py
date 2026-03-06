import time
start = time.time()
import apts  # noqa: F401, E402
end = time.time()
print(f"Importing apts took: {end - start:.4f}s")
