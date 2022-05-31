def solution(A):
    A.sort()
    answer = A[0]
    for i in range(1, len(A)):
        answer = (A[i] + answer)/2

    return int(answer)


if __name__ == '__main__':
    A = list(map(int, input().strip().split()))
    print(solution(A))
