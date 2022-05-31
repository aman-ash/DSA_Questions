def solve(root, res):
    if root is None:
        return 0

    l = solve(root.left, res)
    r = solve(root.right, res)

    temp = max()
    ans = max(temp)
    res[0] = max(res[0], ans)
    return temp


def main(root):
    res = [float("-inf")]
    solve(root, res[0])
    return res[0]
