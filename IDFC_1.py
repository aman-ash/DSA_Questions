from collections import defaultdict


def func(N, M, A, Roards):

    def bfs(i):
        queue = [i]
        curSum = 0
        maxS = 0
        while queue:
            node = queue.pop(0)
            if node in visit:
                continue
            visit.add(node)
            curSum += A[node - 1]
            maxS = max(maxS, A[node - 1])
            for nei in adj[node]:
                queue.append(nei)
        return curSum - maxS

    adj = build(Roards)
    visit = set()
    res = 0
    for i in range(1, N + 1):
        if i in visit:
            continue
        res += bfs(i)

    return res


def build(Roards):
    d = defaultdict(list)
    for u, v in Roards:
        d[u].append(v)
        d[v].append(u)
    return d


if __name__ == '__main__':
    N, M = 9, 6
    A = [12, 7, 15, 9, 13, 15, 15, 13, 15]
    roards = [[1, 2], [1, 9], [3, 7], [3, 9], [4, 5], [7, 8]]
    print(func(N, M, A, roards))
