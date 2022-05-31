memo = {}


class Solution:
    def countWays(self, N, s):
        return self.helper(s, 0, N-1)

    def helper(self, s, i, j, isTrue=True):
        key = str(i) + "." + str(j) + '.' + str(isTrue)

        if i >= j:
            return False if i > j else s[i] == 'T' if isTrue else s[i] == 'F'

        if key in memo:
            return memo[key]

        ans = 0
        for k in range(i+1, j, 2):
            lt = self.helper(s, i, k-1,  True)
            lf = self.helper(s, i, k-1, False)
            rt = self.helper(s, k+1, j, True)
            rf = self.helper(s, k+1, j, False)

            if s[k] == '&':
                if isTrue:
                    ans += (lt * rt)
                else:
                    ans += (lt * rf) + (rt*lf) + (lf*rf)

            elif s[k] == '|':
                if isTrue:
                    ans += (lt * rt) + (lt * rf) + (lf*rt)
                else:
                    ans += (lf * rf)

            elif s[k] == '^':
                if isTrue:
                    ans += (lt * rf) + (lf*rt)
                else:
                    ans += (lt * rt) + (lf * rf)

        memo[key] = ans
        return ans


if __name__ == '__main__':
    ob = Solution()
    s = 'T|F^F&T|F^F^F^T|T&T^T|F^T^F&F^T|T^F'
    print(ob.countWays(len(s), s))
