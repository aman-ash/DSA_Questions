class Solution:
    def findTwoElement(self, arr, n):
        repeating = missing = 0
        dp = [False for _ in range(n+1)]
        for i in arr:
            if dp[i]:
                repeating = i
                break
            dp[i] = True

        arr = set(arr)
        for i in range(1, n+1):
            if i not in arr:
                missing = i
                break

        return [repeating, missing]


if __name__ == '__main__':
    ob = Solution()
    print(ob.findTwoElement([2, 2], 2))
