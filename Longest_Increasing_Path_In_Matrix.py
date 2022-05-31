from collections import deque


class Solution:
    def longestIncreasingPath(self, matrix):
        ROWS, COLS = len(matrix), len(matrix[0])
        ans = float("-inf")
        dp = [[-1 for r in row] for row in matrix]

        def bfs(queue):
            d = 1
            while queue:
                r, c, t = queue.popleft()
                d = max(d, t)
                direc = [[1, 0], [0, 1], [-1, 0], [0, -1]]
                for di in direc:
                    newR, newC = r+di[0], c+di[1]
                    if newR >= 0 and newC >= 0 and newR < ROWS and newC < COLS and matrix[newR][newC] > matrix[r][c]:
                        queue.append([newR, newC, t + 1])
            return d

        for i in range(ROWS):
            for j in range(COLS):
                queue = deque()
                queue.append([i, j, 1])
                temp = bfs(queue)
                ans = max(ans, temp)
                dp[i][j] = temp
        return ans


if __name__ == "__main__":
    mat = [[3, 4, 5], [3, 2, 6], [2, 2, 1]]
    ob = Solution()
    print(ob.longestIncreasingPath(mat))
