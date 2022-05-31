memo = {}


class Solution:
    def isScramble(self, s1, s2):
        if len(s1) != len(s2):
            return False
        if s1 == '':
            return True
        return self.solve(s1, s2)

    def solve(self, a, b):
        n = len(a)
        if a == b:
            return True

        if len(a) <= 1:
            return False

        if n in memo:
            return memo[n]

        flag = False
        for i in range(1, n):
            case1 = self.solve(a[:i], b[:i]) and self.solve(a[i:], b[i:])
            case2 = self.solve(a[:i], b[n-i:]) and self.solve(a[i:], b[:n-i])
            flag = case1 or case2
            if flag:
                break

        memo[n] = flag
        return flag


if __name__ == '__main__':
    ob = Solution()
    s1, s2 = "abcde", "caebd"
    print(ob.isScramble(s1, s2))
