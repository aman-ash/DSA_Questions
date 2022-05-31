class Solution:
    def func(self, N, K, trees):
        if N < 4:
            return self.basecase(trees, N, K)

        temp = []
        temp.append(trees[0])
        for i in range(1, N-1):
            temp.append(trees[i] + trees[i+1])
        temp.append(trees[N - 1])
        ans = 0
        i = k = 0
        j = len(temp) - 1

        temp = temp.sort()
        while i < j:
            sums = temp[i] + temp[j]
            ans += 1
            if sums < K:
                i += 1
            elif sums > K:
                j -= 1
            else:
                return ans

        return -1

    def basecase(self, trees, N, K):
        if N < 3:
            if sum(trees) != K:
                return - 1
        for i in range(N - 1):
            for j in range(i+1, N):
                if trees[i] + trees[j] == K:
                    return 2
        return -1


def main():
    ob = Solution()
    t = int(input())
    N, K = map(int, input().strip().split())
    trees = list(map(int, input().strip().split()))
    for case in range(t):
        print('Case #%d: %s' % (case+1, ob.func(N, K, trees)))


if __name__ == '__main__':
    main()
