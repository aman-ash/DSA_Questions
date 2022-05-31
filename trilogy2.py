from itertools import accumulate
import time

MOD_BASE = 1000000007
N_BOUND = 200000


def modmul(m):
    def mul(x, y):
        return x * y % m
    return mul


FACTORIALS = [1] + list(accumulate(range(1, N_BOUND+1), modmul(MOD_BASE)))


def nck(n, k, m):
    numerator = FACTORIALS[n]
    denominator = FACTORIALS[k] * FACTORIALS[n-k]
    return numerator * pow(denominator, -1, m) % m


def solve(n, k):
    return nck(n-1, k-1, MOD_BASE)


if __name__ == "__main__":
    t = [i for i in range(50000, 200001)]
    ans = []
    start = time.time()
    for i in range(1, len(t), 2):
        ans.append((solve(t[i], t[i - 1])))

    ans.append(solve(36, 6))
    ans.append(solve(81, 66))
    ans.append(solve(96, 88))
    end = time.time()

    print(end - start)
    print(ans[74990:])
    print(FACTORIALS[-1])
