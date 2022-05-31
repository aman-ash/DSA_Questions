def func(arr):
    N = len(arr)
    adj = {i: [x for x in range(i+1, i+arr[i]+1)] for i in range(N)}
    queue = [[0,0]]
    visit = set()

    while queue:
        current, travel = queue.pop(0)
        if current == N - 1:
            return travel
        if current in visit:
            continue
        visit.add(current)
        travel += 1
        for neighbor in adj[current]:
            queue.append([neighbor, travel])

    return -1


if __name__ == '__main__':
    tests = [[1, 2, 3], [5, 0, 0, 0], [0], [0, 2, 4], [1, 2, 0, 0, 1]]
    for test in tests:
        print(func(test))
