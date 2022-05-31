class testClass(object):
    def minJumps(self, arr):
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
    
