class Solution:
    def shortestCommonSupersequence(self, s1, s2):
        n, m = len(s1), len(s2)
        return self.topDown(s1, s2)

    def topDown(self, s1, s2):
        n, m = len(s1), len(s2)
        dp = [[0 for _ in range(m+1)] for _ in range(n+1)]
        for i in range(1, n+1):
            for j in range(1, m + 1):
                if s1[i-1] == s2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i][j - 1], dp[i - 1][j])
        return self.printlcs(s1, s2, dp)

    def printlcs(self, s1, s2, dp):
        i, j = len(s1), len(s2)
        ans = ''
        while i > 0 and j > 0:
            if s1[i - 1] == s2[j - 1]:
                ans = s1[i - 1] + ans
                i -= 1
                j -= 1
            else:
                if dp[i][j - 1] > dp[i - 1][j]:
                    j -= 1
                    ans = s2[j] + ans
                else:
                    i -= 1
                    ans = s1[i] + ans

        while i > 0:
            ans = s1[i - 1] + ans
            i -= 1
        while j > 0:
            ans = s2[j - 1] + ans
            j -= 1
        return ans


if __name__ == '__main__':
    ob = Solution()
    s1, s2 = 'abac', 'cab'
    print(ob.shortestCommonSupersequence(s1, s2))
