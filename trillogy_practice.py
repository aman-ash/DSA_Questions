def func(word, matrix):
    if len(word) < 2:
        return basecase(word, matrix)
    count = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):

            right = matrix[i][j]
            for k in range(j + 1, len(matrix[i])):
                right += matrix[i][k]
                if right == word:
                    count += 1
                    break

            down = matrix[i][j]
            for k in range(i + 1, len(matrix)):
                down += matrix[k][j]
                if down == word:
                    count += 1
                    break

            cross = matrix[i][j]
            k, l = i+1, j+1
            while k < len(matrix) and l < len(matrix[i]):
                cross += matrix[k][l]
                if cross == word:
                    count += 1
                    break
                k += 1
                l += 1

    return count


def basecase(word, matrix):
    if not word:
        return 0

    count = 0
    for array in matrix:
        for w in array:
            if w == word:
                count += 1
    return count


if __name__ == '__main__':
    word = 'sos'
    matrix = [
        ['s', 'o', 's', 's'],
        ['s', 'o', 'o', 'o'],
        ['s', 'o', 's', 's']
    ]
    print(func(word, matrix))
