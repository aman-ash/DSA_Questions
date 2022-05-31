class Solution:

    def findMaxArea(self, grid):
        visited = [[False for r in row] for row in grid]
        maxArea = float("-inf")

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 0 or visited[i][j]:
                    continue

                maxSoFar = self.foundArea(grid, visited, i, j)
                maxArea = max(maxArea, maxSoFar)
        return maxArea

    def foundArea(self, grid, visited, i, j):
        if grid[i][j] == 0 or visited[i][j]:
            return 0
        visited[i][j] = True
        directions = [[0, 1], [1, 0], [0, -1], [-1, 0],
                      [1, 1], [-1, -1], [1, -1], [-1, 1]]
        size = 1
        for d in directions:
            r, c = i + d[0], j + d[1]
            if r < 0 or c < 0 or r >= len(grid) or c >= len(grid[0]):
                continue
            if visited[r][c] or grid[r][c] == 0:
                continue

            size += self.foundArea(grid, visited, r, c)

        return size


if __name__ == '__main__':
    h, w = map(int, input().split())
    grid = [list(map(int, input().strip().split())) for _ in range(h)]
    ob = Solution()
    result = ob.findMaxArea(grid)
    print(result)
