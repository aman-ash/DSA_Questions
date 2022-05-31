# Brute Force , Time - O(n2) , space = O(n)
def largestRectangleUnderSkylineBF(arr):
    n = len(arr)
    if n < 2:
        return 0 if n == 0 else arr[0]
    ans = float("-inf")
    for i in range(n):
        cur = arr[i]
        for j in range(i+1, n+1):
            temp = arr[i:j+1]
            ans = max(cur, ans, len(temp)*min(temp))
    return ans


# Optimized Stack Solution , Time - O(n) , space = O(n)
def largestRectangleUnderSkyline(arr):
    n = len(arr)
    left = leftSmaller(arr, n)
    right = rightSmaller(arr, n)
    print(left, right)
    ans = float("-inf")

    for i in range(n):
        cur = arr[i] * (right[i] - left[i]+1)
        ans = max(ans, cur)
    return ans


def rightSmaller(arr, n):
    ans = [n-1]
    stack = [arr[-1]]
    for i in reversed(range(n - 1)):
        flag = False
        while len(stack):
            if stack[-1] < arr[i]:
                ans.append(stack[-1])
                flag = True
                break
            else:
                stack.pop()
        if not flag:
            ans.append(n-1)
        stack.append(arr[i])
    ans.reverse()
    return ans


def leftSmaller(a, n):
    ans = [0]
    stack = [a[0]]

    for i in range(1, n):
        cur = a[i]
        flag = False

        while len(stack):
            if stack[-1] < cur:
                ans.append(stack[-1])
                flag = True
                break

            else:
                stack.pop()

        stack.append(cur)
        if not flag:
            ans.append(0)
    return ans


if __name__ == '__main__':
    arr = [1, 3, 3, 2, 4, 1, 5, 3, 2]
    print(largestRectangleUnderSkyline(arr))
