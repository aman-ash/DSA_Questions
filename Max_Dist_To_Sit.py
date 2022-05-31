class solution:
    def maxDistance(self, A, N):
        maxSumSoFar = 0
        count = 0
        start = 0
        end = 0
        for i in range(N):
            if A[i] == 1:
                count = 0
                start = i
            else:
                count += 1
            if count > maxSumSoFar:

                end = i
                maxSumSoFar = count
            index = [start, end]

        if maxSumSoFar <= 1:
            return 1

        if maxSumSoFar % 2 == 0:
            answer = maxSumSoFar // 2
        else:
            answer = maxSumSoFar // 2 + 1

        if index[0] == 0 or index[1] == N - 1:
            return answer + (maxSumSoFar // 2)
        return answer


if __name__ == '__main__':
    ob = solution()
    A = list(map(int, input().split()))
    N = len(A)
    print(ob.maxDistance(A, N))
