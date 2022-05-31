class Solution:
    def func(self, n):
        val = int(self.helper(str(n)))
        numList = list(str(n))
        if val == 9:
            return int(str(n) + '0')

        ans = float("inf")
        new = str(9 - val)

        n = str(n)
        for i in range(len(n)):
            temp = str(n)[:i] + new + str(n)[i:]
            ans = min(ans, int(temp))
        return ans

    def checkZeros(self, arr):
        for i in range(1, len(arr)):
            if arr[i] != '0':
                arr[i], arr[0] = arr[0], arr[i]
                break
        return arr

    def helper(self, n):
        if len(n) == 1:
            return n

        t = 0
        for i in range(len(n)):
            t += int(n[i])
        return self.helper(str(t))


def main():
    ob = Solution()
    t = int(input())
    for case in range(t):
        n = int(input())
        print('Case #%d: %s' % (case+1, ob.func(n)))


if __name__ == '__main__':
    main()
