class Solution:
    def numIslands(self, grid):
        no_of_islands = 0
        visited = [[False for r in row] for row in grid]
        for i in range(len(grid)):
            for j in range(len(grid[i])):

                if grid[i][j] == 0 or visited[i][j]:
                    continue

                no_of_islands += 1
                visited[i][j] = True
                self.helper(i, j, grid, visited)

        return no_of_islands

    def helper(self, i, j, grid, visited):
        directions = [[-1, 0], [0, -1], [1, 0],
                      [0, 1], [1, -1], [-1, 1], [-1, -1], [1, 1]]

        for direction in directions:
            start, end = i + direction[0], j + direction[1]
            if self.checkIsValid(start, end, grid):
                if grid[start][end] == 0 or visited[i][j]:
                    continue

                visited[start][end] = True
                self.helper(start, end, grid)

    def checkIsValid(self, i, j, grid):
        return False if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[i]) else True


if __name__ == '__main__':
    ob = Solution()
    grid = [
        [0, 1],
        [1, 0],
        [1, 1],
        [1, 0]
    ]
    result = ob.numIslands(grid)
    print(result)
