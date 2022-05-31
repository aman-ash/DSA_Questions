def func(nums):
    visit = set(nums)
    seen = [False for i in range(len(nums) + 1)]
    ans = 0

    for num in nums:
        if seen[num]:
            ans += num
            break
        seen[num] = True

    for i in range(1, len(nums) + 1):
        if i not in visit:
            ans += i
            break

    return ans


if __name__ == '__main__':
    tests = [
        [1, 1, 3, 4],
        [2, 2],
        [4, 3, 3, 1],
        [6, 3, 2, 4, 3, 1],
        [10, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    ]
    for test in tests:
        print(func(test))
