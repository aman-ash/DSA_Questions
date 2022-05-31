class Innovator:

    def func(self, matrix, word):
        if len(word) < 2:
            return self.CheckBaseCase(matrix, word)

        count = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):

                right = matrix[i][j]
                for k in range(j+1, len(matrix[0])):
                    right += matrix[i][k]
                    if self.checkEqual(word, right):
                        count += 1
                        break

                down = matrix[i][j]
                for k in range(i+1, len(matrix)):
                    down += matrix[k][j]
                    if self.checkEqual(word, down):
                        count += 1
                        break

                k, l = i + 1, j + 1
                cross = matrix[i][j]
                while k < len(matrix) and l < len(matrix[0]):
                    cross += matrix[k][l]
                    if self.checkEqual(word, cross):
                        count += 1
                        break
                    k += 1
                    l += 1

        return count

    def checkEqual(self, word, temp):
        return word == temp

    def CheckBaseCase(self, matrix, word):
        count = 0
        for array in matrix:
            for i in range(len(array)):
                if array[i] == word:
                    count += 1
        return count


if __name__ == '__main__':
    word = 'sos'
    matrix = [
        ['s', 'o', 's', 'o'],
        ['s', 'o', 'o', 's'],
        ['s', 's', 's', 's']
    ]
    ob = Innovator()
    result = ob.func(matrix, word)
    print(result)
