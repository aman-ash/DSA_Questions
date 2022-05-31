import heapq
from collections import defaultdict


def getMinimumCost(n, m, connections):
    adj = defaultdict(list)
    for i in range(m):
        u, v, w = connections[i]
        adj[u].append([w, v])
        adj[v].append([w, u])

    mHeap = [[0, connections[0][0]]]
    visit = set()
    res = 0
    while len(visit) < m+1:
        cost, node = heapq.heappop(mHeap)
        if node in visit:
            continue
        res += cost
        visit.add(node)
        for neiCost, nei in adj[node]:
            if nei in visit:
                continue
            heapq.heappush(mHeap, [neiCost, nei])
    return res


if __name__ == '__main__':
    connections = [[1, 2, 4]]
    print(getMinimumCost(3, 1, connections))
