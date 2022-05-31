def riverSizes(matrix):
    sizes = []
    visited = [[False for value in row] for row in matrix]
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 0 or visited[i][j]:
                continue
            size = traverse_node(i, j, matrix, visited)
            sizes.append(size)
    return sizes


def traverse_node(i, j, grid, visited):
    if visited[i][j] or grid[i][j] == 0:
        return 0
    visited[i][j] = True
    directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
    size = 1
    for d in directions:
        r, c = i + d[0], j + d[1]
        if not inBounds(r, c, grid) or visited[r][c]:
            continue
        size += traverse_node(r, c, grid, visited)
    return size


def inBounds(i, j, grid):
    return False if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]) else True


if __name__ == '__main__':
    grid = [
        [1, 0, 0, 1, 0],
        [1, 0, 1, 0, 0],
        [0, 0, 1, 0, 1],
        [1, 0, 1, 0, 1],
        [1, 0, 1, 1, 0]
    ]
    print(riverSizes(grid))
