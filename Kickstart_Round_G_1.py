class Solution:
    def func(self, N, D, C, M, S):
        for i in range(N):
            if S[i] == 'D':
                D -= 1
                C += M
            if S[i] == 'C':
                C -= 1
            if D < 0:
                return "NO"
            if C < 0:
                string = S[i:]
                if 'D' in string:
                    return "NO"
                return "YES"
        return "YES"


def main():
    ob = Solution()
    t = int(input())
    for case in range(t):
        N, D, C, M = map(int, input().strip().split())
        string = str(input())
        print('Case #%d: %s' % (case+1, ob.func(N, D, C, M, string)))


if __name__ == '__main__':
    main()
