class Solution:
    def func(self, N, K, trees):
        subset = [[]]
        self.helper(trees, subset)
        subset = sorted(subset, key=lambda x: len(x))
        for s in subset:
            if sum(s) == K:
                return len(s)
        return -1

    def helper(self, trees, subset):
        for element in trees:
            for i in range(len(subset)):
                cur = subset[i]
                if cur + [element] not in subset:
                    subset.append(cur + [element])
        subset.pop(0)
        return subset


def main():
    ob = Solution()
    t = int(input())

    for case in range(t):
        N, K = map(int, input().strip().split())
        trees = list(map(int, input().strip().split()))
        print('Case #%d: %s' % (case+1, ob.func(N, K, trees)))


if __name__ == '__main__':
    main()
