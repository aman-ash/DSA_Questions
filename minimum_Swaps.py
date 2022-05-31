def minSwaps(N, A, B):
    countA = countB = 1
    Adic = {}
    Bdic = {}
    for i in range(N):
        if A[i] == A[0]:
            countA += 1
        if A[i] not in Adic:
            Adic[A[i]] = 1
        else:
            Adic[A[i]] += 1

        if B[i] == B[0]:
            countB += 1
        if B[i] not in Bdic:
            Bdic[B[i]] = 1
        else:
            Bdic[B[i]] += 1
    return Adic, Bdic


if __name__ == '__main__':
    N = 4
    A = [1, 1, 3, 1]
    B = [0, 1, 1, 1]
    print(minSwaps(N, A, B))
