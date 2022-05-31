def calculateSum(N, A, B):
    sums = 0
    if A == 1 or B == 1:
        for i in range(1, N+1):
            sums += i
        return sums

    if A % B == 0 or B % A == 0:
        i = min(A, B)
        for i in range(i, N+1, i):
            sums += i
        return sums

    T = A + B
    i = A
    j = B
    while A < N:
        sums += A
        A += i

    while B < N:
        if B % T == 0:
            B += B
            continue
        sums += B
        B += j

    if N % A == 0 or N % B == 0:
        sums += N

    return sums


if __name__ == "__main__":
    N = 10
    A = 3
    B = 2
    print(calculateSum(N, A, B))
