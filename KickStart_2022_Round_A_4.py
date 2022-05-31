class Solution:
    def func(self, A, B):
        if B < 10:
            return (B - A + 1)

        count = 0
        for i in range(A, B+1):
            prod = self.getProd(i)
            sums = self.getSum(i)
            if prod % sums == 0:
                count += 1

        return count

    def getProd(self, i):
        i = str(i)
        ans = 1
        for j in range(len(i)):
            ans *= int(i[j])
        return ans

    def getSum(self, i):
        ans = 0
        i = str(i)
        for j in range(len(i)):
            ans += int(i[j])
        return ans


def main():
    ob = Solution()
    t = int(input())
    for case in range(t):
        A, B = map(int, input().split())
        print('Case #%d: %s' % (case+1, ob.func(A, B)))


if __name__ == '__main__':
    main()
