import numpy as np
import time

N = 14000
arr = np.random.rand(N) * 360

start = time.time()
for _ in range(1000):
    rad = np.deg2rad(arr)
    s = np.sin(rad)
    c = np.cos(rad)
end = time.time()

print(f"Time for 1000 iterations of sin/cos on {N} elements: {end - start:.4f}s")
print(f"Average time per iteration: {(end - start) / 1000 * 1000:.4f}ms")
