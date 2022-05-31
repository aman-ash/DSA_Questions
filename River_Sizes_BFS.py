import collections


def riverSizes(matrix):
    N, M = len(matrix), len(matrix[0])
    visit = set()
    ans = []

    for i in range(N):
        for j in range(M):
            if matrix[i][j] == 0 or (i, j) in visit:
                continue

            queue = collections.deque([[i, j, 0]])
            while queue:
                r, c, length = queue.popleft()
                if (r, c) in visit or matrix[r][c] == 0:
                    continue

                visit.add((r, c))
                directions = [[0, 1], [1, 0], [-1, 0], [0, -1]]
                for row, col in directions:
                    newR = r + row
                    newC = c + col

                    if newR < 0 or newC < 0 or newR >= N or newC >= M or (newR, newC) in visit:
                        continue
                    queue.append([newR, newC, length + 1])
            ans.append(length)
    return ans


if __name__ == '__main__':
    mat = [
        [1, 0, 0, 1, 0],
        [1, 0, 1, 0, 0],
        [0, 0, 1, 0, 1],
        [1, 0, 1, 0, 1],
        [1, 0, 1, 1, 0]]
    print(riverSizes(mat))
