class Solution:
    def rob(self, nums):
        d = {}
        return self.helper(nums, d, len(nums) - 1)

    def helper(self, nums, d, n):
        if n == 0:
            return nums[n]

        if n < 0:
            return 0

        if n in d:
            return d[n]

        d[n] = max(nums[n] + self.helper(nums,
                   d, n - 2), self.helper(nums, d, n - 1))
        return d[n]


if __name__ == '__main__':
    ob = Solution()
    nums = [1, 2, 3, 1]
    print(ob.rob(nums))
