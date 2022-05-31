def taskAssignment(k, tasks):
    new = []
    ans = []
    return helper(tasks, new, ans)


def helper(new, tasks, ans):
    new = [[tasks[i], i] for i in range(len(tasks))]
    new = sorted(new, key=lambda x: x[0])

    i = 0
    j = len(new) - 1
    while i < j:
        ans.append([new[i][1], new[j][1]])
        i += 1
        j -= 1
    return ans
