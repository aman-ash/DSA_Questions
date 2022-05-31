class Solution:

    def func(self, n):
        ways = [[0 for _ in range(n + 1)] for _ in range(n + 1)]

        for i in range(1, n + 1):
            for j in range(1, n + 1):
                if i < j:
                    continue
                elif i == 1 or j == 1:
                    ways[i][j] = 1

                else:
                    ways[i][j] = ways[i - 1][j] + ways[i][j - 1]

        return ways[-1][-1]

    def func2(self, n):
        ways = [[0 for _ in range(n)] for _ in range(n)]

        for i in range(n):
            for j in range(n):
                if i < j:
                    continue
                elif i == 0 or j == 0:
                    ways[i][j] = 1

                else:
                    ways[i][j] = ways[i - 1][j] + ways[i][j - 1]

        return ways[-1][-1]


if __name__ == '__main__':
    ob = Solution()
    n = int(input('n2'))
    result = ob.func2(n)
    print(result)
