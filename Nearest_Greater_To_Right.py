
def solve(arr):
    ans = [-1]
    stack = [arr[-1]]
    for i in reversed(range(len(arr) - 1)):
        flag = False
        while len(stack):
            if stack[-1] > arr[i]:
                ans.append(stack[-1])
                flag = True
                break
            else:
                stack.pop()
        if not flag:
            ans.append(-1)
        stack.append(arr[i])
    ans.reverse()
    return ans


def leftSmaller(self, n, a):
    ans = [-1]
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
            ans.append(-1)
    return ans


def leftGreater(a, n):
    ans = [-1]
    stack = [[a[0], 0]]

    for i in range(1, n):
        cur = a[i]
        flag = False

        while len(stack):
            if stack[-1][0] > cur:
                ans.append(i - stack[-1][1])
                flag = True
                break

            else:
                stack.pop()

        stack.append([cur, i])
        if not flag:
            ans.append(-1)
    return ans


if __name__ == '__main__':
    arr = [1, 3, 2, 4]
    a1 = [100, 80, 60, 70, 60, 75, 85]
    print(solve(a1))
