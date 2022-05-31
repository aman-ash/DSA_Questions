def cycleInGraph(edges):
    adj = {i:edges[i] for i in range(len(edges))}
    visit = set()

    def dfs(node):
        if node in visit:
            return True
        if adj[node] == []:
            return False
        visit.add(node)
        for pre in adj[node]:
            if dfs(pre):
                return True
        visit.remove(node)
        return False

    for i in range(len(edges)):
        if dfs(i):
            return True
    return False
	
	
def build(edges):
    d= {}
    for i in range(len(edges)):
        d[i] = edges[i]
    return d


if __name__ == '__main__':
    arr = [ 
           [],
           [0, 3],
           [0],
           [1, 2]]
    print(cycleInGraph(arr))

