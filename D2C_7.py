def solution(n, X, Y):
    count = 0
    if X == Y:
        return count

    for i in range(0, n - 1):
        if X[i] != Y[i]:
            X[i], Y[i] = Y[i], X[i]
            X[i] = X[i] + 1
            X[i + 1] = X[i + 1] - 1
            count += 1

        if X == Y:
            return count

    return -1


if __name__ == "__main__":
    n = int(input())
    X = list(map(int, input().strip().split()))
    Y = list(map(int, input().strip().split()))
    print(solution(n, X, Y))
