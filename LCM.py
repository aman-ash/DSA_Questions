def LCM(n):
    if n <= 1:
        return [1]
    ans = []
    while n > 1:
        for i in range(2, n+1):
            if n % i == 0:
                ans.append(i)
                n = n // i
                break
    return ans


def solve(n):
    lcm = LCM(n)
    if len(lcm) == 1:
        return -1

    idx = len(lcm) // 2
    idx2 = len(lcm) // 2
    t = 1
    for i in range(idx+1):
        t *= lcm[i]
    t2 = 1
    for i in range(idx2, len(lcm)):
        t2 *= lcm[i]

    return int(str(t) + str(t2))


if __name__ == '__main__':
    print(solve(25))
    print(solve(67))
    print(solve(125))
    print(solve(64))
    print(solve(95))
