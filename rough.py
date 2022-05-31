class Solution:
    def solve(self, n, s, c):
        ans = 0
        for i in range(0, n//2, 2):
            j = n - i - 2
            a = s[i:i+2]
            b = s[j:j+2]
            res = 0
            res2 = 0

            if a == '' or b == '':
                continue

            if a[0] == b[0] and a[1] == b[1]:
                continue

            elif a[0] == b[0]:
                res += min(c[i+1], c[n-i-1])

            elif a[1] == b[1]:
                res += min(c[i], c[n - i - 2])

            else:
                res += min(c[i+1], c[n-i-1])
                res += min(c[i], c[n-i-2])

            if a[0] == b[1] and a[1] == b[0]:
                continue

            elif a[0] == b[1]:
                res2 += min(c[i+1], c[n-i-2])

            elif a[1] == b[0]:
                res2 += min(c[i], c[n-i-1])

            else:
                res2 += min(c[i+1], c[n-i-2])
                res2 += min(c[i], c[n-i-1])

            ans += min(res, res2)
        return ans


if __name__ == '__main__':
    N = 8
    S = 'abbacaaa'
    C = [1, 2, 3, 4, 2, 3, 0, 1]
    ob = Solution()
    print(ob.solve(N, S, C))
