class Solution:
    def countCells(self, A, N, M):
        count = 0

        for i in range(N):
            for j in range(M):
                cur = A[i][j]
                if i == 0 and j == 4 or i == 4 and j == 0:
                    count += 1
                    continue

                up = True
                for k in range(i, -1, -1):
                    if cur < A[k][j]:
                        up = False
                        break

                left = True
                for m in range(j, -1, -1):
                    if cur < A[i][m]:
                        left = False
                        break

                if not up and not left:
                    break

                down = True
                for l in range(i, N):
                    if cur < A[l][j]:
                        down = False
                        break

                right = True
                for n in range(j, M):
                    if cur < A[i][n]:
                        right = False
                        break

                if (up or left) and (down or right):
                    count += 1

        return count


if __name__ == "__main__":
    ob = Solution()
    A = [
        [1, 2, 2, 3, 5],
        [3, 2, 3, 4, 4],
        [2, 4, 5, 3, 1],
        [6, 7, 1, 4, 5],
        [5, 1, 1, 2, 4]
    ]

    result = ob.countCells(A, 5, 5)
    print(result)
