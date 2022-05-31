import time
import numpy as np

st = time.time()
s = []
s = np.array([s[-1] for x in range(0, 10001)
              if not s.append(x*s[-1] if s else 1)], dtype=np.float)
#A = np.array([i**50 for i in range(1, 200001)], dtype=np.float64)


et = time.time()
print(et - st)
print(s[:10])
