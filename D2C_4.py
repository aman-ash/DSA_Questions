def solution(n, a, b, c):
    A = list(a)
    B = list(b)
    C = list(c)
    if A == B:
        return "YES"
    for i in range(n):
        if A[i] != B[i]:
            if B[i] != C[i] and A[i] != C[i]:
                return "NO"
            A[i], C[i] = C[i], A[i]
            A[i], B[i] = B[i], A[i]

            if A == B:
                return "YES"

    return "NO"


if __name__ == "__main__":
    n = int(input())
    a = input()
    b = input()
    c = input()
    print(solution(n, a, b, c))
