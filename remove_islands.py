def removeIslands(matrix):
    n, m = len(matrix), len(matrix[0])
    for i in range(n):
        for j in range(m):
            if i == 0 or j == 0 or i == n - 1 or j == m - 1:
                if matrix[i][j] == 0:
                    continue
                changeColor(i, j, matrix)

    for i in range(n):
        for j in range(m):
            if matrix[i][j] == 1:
                matrix[i][j] = 0
            if matrix[i][j] == 2:
                matrix[i][j] = 1
    return matrix


def changeColor(i, j, matrix):
    n, m = len(matrix), len(matrix[0])
    if matrix[i][j] == 1:
        matrix[i][j] = 2
    else:
        return
    directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
    for d in directions:
        r, c = i + d[0], j + d[1]
        if r > n - 1 or c > m - 1 or r < 0 or c < 0:
            continue
        changeColor(r, c, matrix)


if __name__ == '__main__':
    matrix = [
        [1, 0, 0, 0, 0, 0],
        [0, 0, 0, 1, 1, 1],
        [0, 0, 0, 0, 1, 0],
        [1, 1, 0, 0, 1, 0],
        [1, 0, 0, 0, 0, 0],
        [1, 0, 0, 0, 0, 1]
    ]

    result = removeIslands(matrix)
    print(result)
