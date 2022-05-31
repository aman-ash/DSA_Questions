def printPascal(n: int):
    ans = [[1]]
    if n < 2:
        return ans

    for _ in range(n-1):
        prev = ans[-1]
        next = [prev[0]]

        for i in range(1, len(prev)):
            next.append(prev[i] + prev[i - 1])
        next.append(prev[-1])
        ans.append(next)

    return ans


if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        print(printPascal(int(input())))
