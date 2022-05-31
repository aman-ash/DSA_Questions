import time
from math import factorial


def ncr(array):
    for i in range(1, len(array)):
        n, r = array[i - 1], array[i]
        n, r = n - 1, r - 1
        r = min(n - r, r)
        ans = 1
        for i in range(1, r+1):
            ans = (ans * (n - r + i)) // i
    return ans % 1000000007


def new(n, r):

    D = factorial(n - 1) // (factorial(r - 1)
                             * factorial(n - r))
    return (D % 1000000007)


def best(n, r, s):
    D = s[n - 1] // (s[r - 1]
                     * s[n - r])
    return (D % 1000000007)


if __name__ == '__main__':
    # st = time.time()
    # s = []
    # t = [81, 66, 96, 88]
    # s = [s[-1] for x in range(0, 20001) if not s.append(x*s[-1] if s else 1)]
    # ans = []
    # for i in range(1, len(t), 2):
    #     ans.append(best(t[i - 1], t[i], s))
    # et = time.time()
    # print(et - st)
    # print(ans[:10])
    t = int(input())
    s = [int(input()) for i in range(t)]
    print(s)
