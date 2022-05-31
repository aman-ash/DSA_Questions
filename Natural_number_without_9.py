def findNth(N):
    ans = N
    if ans - 9 < 0:
        return ans

    if N % 9 == 0:
        plus = N // 9
        ans = ans + plus
    else:
        cur = str(N)
        plus = cur[0]
        ans = ans + int(plus)
    return ans


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        N = int(input())
        print(findNth(N))
