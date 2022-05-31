class Solution:
    def countWays(self, N, s):
        return self.helper(s, 0, N-1)

    def helper(self, s, i, j, isTrue=True):
        if i > j:
            return False
        if i == j:
            return s[i] == 'T' if isTrue else s[i] == 'F'

        ans = 0
        for k in range(i+1, j, 2):
            lt = self.helper(s, i, k-1, True)
            lf = self.helper(s, i, k-1, False)
            rt = self.helper(s, k+1, j, True)
            rf = self.helper(s, k+1, j, False)

            if s[k] == '&':
                ans += lt * rt if isTrue else lt * rf + rt*lf + lf*rf

            elif s[k] == '|':
                ans += lt * rt + lt * rf + lf * rt if isTrue else lf * rf

            elif s[k] == '^':
                ans += lt * rf + lf * rt if isTrue else lt * rt + lf * rf

        return ans


if __name__ == '__main__':
    ob = Solution()
    s = 'T|F^F&T'
    print(ob.countWays(len(s), s))
