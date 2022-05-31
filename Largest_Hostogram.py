def histogram(arr):
    left = firstleftsmallest(arr)
    right = firstrightsmallest(arr)
    ans = float("-inf")
    for i in range(len(arr)):
        temp = (right[i] - left[i] - 1) * arr[i]
        ans = max(ans, temp)
    return ans


def firstleftsmallest(arr):
    ans = [-1]
    left = [[arr[0], 0]]

    for i in range(1, len(arr)):
        cur = arr[i]
        flag = False

        while len(left):
            ele, Idx = left[-1]
            if ele < cur:
                ans.append(Idx)
                flag = True
                left.append([cur, i])
                break
            else:
                left.pop()

        if not flag:
            ans.append(-1)
            left.append([cur, i])
    return ans


def firstrightsmallest(arr):
    n = len(arr)
    ans = []
    right = []

    for i in reversed(range(len(arr))):
        cur = arr[i]
        flag = False

        while len(right):
            ele, Idx = right[-1]
            if ele < cur:
                ans.append(Idx)
                flag = True
                right.append([cur, i])
                break
            else:
                right.pop()

        if not flag:
            ans.append(n)
            right.append([cur, i])
    ans.reverse()
    return ans


if __name__ == '__main__':
    arr = [1, 3, 3, 2, 4, 1, 5, 3, 2]
    print(histogram(arr))
