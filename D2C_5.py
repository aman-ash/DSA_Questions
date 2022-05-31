def solution(n, k, array):
    n = int(n)
    k = int(k)
    answer = float("inf")
    for i in range(0, n-k+1):
        current = 0
        for j in range(i, i+k):
            current += abs(array[j])
        if current < answer:
            answer = current
    return answer


if __name__ == '__main__':
    n, k = input().split()
    array = list(map(int, input().strip().split()))
    print(solution(n, k, array))
