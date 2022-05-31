class Solution:
    def diffWaysToCompute(self, s):

        def func(i, j):
            if i == j:
                return int(s[i])
            ans = []
            for k in range(i, j, 2):
                t1 = func(i, k)
                t2 = func(k+2, j)
                if s[k + 1] == '+':
                    temp = t1 + t2
                if s[k + 1] == '-':
                    temp = t1 - t2
                if s[k + 1] == '*':
                    temp = t1 * t2
            ans.append(temp)
            print(ans)

            return temp

        return func(0, len(s) - 1)


if __name__ == '__main__':
    ob = Solution()
    s = "2*3-4*5"
    print(ob.diffWaysToCompute(s))
