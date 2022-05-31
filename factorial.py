import time
import math

if __name__ == '__main__':
    B = 1
    n = time.time()
    for i in range(1, 56988):
        B *= i
    m = time.time()
    print(m - n)
    start = time.time()
    A = math.factorial(56987)
    end = time.time()
    print(end - start)
