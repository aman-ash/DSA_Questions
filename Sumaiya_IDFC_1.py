def maxProfit(N, M, D, A):
    if D == len(A) - 1:
        return sum(A) + M

    potential = []
    val = A[0]
    i = j = 0
    while abs(i - j) < d:
        val += A[j]
        j += 1
    potential.append(val)

    count = (D * 2) + 1

    for j in range(M):
        Idx = 0
        minimum = float("inf")
        for i in range(len(A)):
            if potential[i] < minimum:
                minimum = potential[i]
                Idx = i

        potential[Idx] += 1

    return min(potential)


if __name__ == '__main__':
    N = 3
    M = 2
    D = 0
    A = [3, 4, 3]
    print(maxProfit(N, M, D, A))
    n, m, d = 4, 1, 1
    a = [2, 1, 3, 2]
    print(maxProfit(n, m, d, a))
