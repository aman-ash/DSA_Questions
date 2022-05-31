import heapq


class Solution:
    def swimInWater(self, grid):
        ROWS, COLS = len(grid), len(grid[0])
        minHeap = [(0, 0, 0)]
        visit = set()
        ans = 0

        while minHeap:
            t, i, j = heapq.heappop(minHeap)
            ans = max(t, ans)
            directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]

            if i == ROWS - 1 and j == COLS - 1:
                break
            for d in directions:
                r, c = i + d[0], j + d[1]
                if (r, c) not in visit and r >= 0 and c >= 0 and r < ROWS and c < COLS:
                    heapq.heappush(minHeap, (grid[r][c], r, c))
                    visit.add((r, c))

        return ans


if __name__ == '__main__':
    ob = Solution()
    grid = [[0, 1, 2, 3, 4], [24, 23, 22, 21, 5], [
        12, 13, 14, 15, 16], [11, 17, 18, 19, 20], [10, 9, 8, 7, 6]]
    print(ob.swimInWater(grid))
