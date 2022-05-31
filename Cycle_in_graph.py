from collections import deque


class Solution:

    def findCycle(self, arr):
        graph = self.makeGraph(arr)
        visited = [False for edge in arr]
        for i in range(len(arr)):
            if visited[i]:
                continue
            checkForCycle = self.explore(graph, i, visited)
            if checkForCycle:
                return True
        return False

    def explore(self, graph, edge, visited):
        queue = deque([edge])
        while len(queue):
            cur = queue.popleft()
            if visited[cur]:
                if self.check(cur, graph):
                    return True
            visited[cur] = True
            neighbors = graph[cur]
            for neighbor in neighbors:
                queue.append(neighbor)
        return False

    def check(self, edge, graph):
        visited = [False for _ in graph]
        queue = deque([edge])
        while len(queue):
            cur = queue.popleft()
            if visited[cur]:
                return True
            visited[cur] = True
            N = graph[cur]
            for n in N:
                queue.append(n)
        return False

    def makeGraph(self, arr):
        return dict([(key, value) for key, value in enumerate(arr)])


def main():
    ob = Solution()
    arr = [[1],
           [2, 3, 4, 5, 6, 7],
           [],
           [2, 7],
           [5],
           [],
           [4],
           []]
    result = ob.findCycle(arr)
    print(result)

    return


if __name__ == '__main__':
    main()
