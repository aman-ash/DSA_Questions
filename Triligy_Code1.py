class GFG:

    def __init__(self):
        self.R = None
        self.C = None
        self.dir = [[1, 0], [1, 1],
                    [1, -1], [-1, -1], [-1, 1],
                    [0, 1], [0, -1]]

    def search2D(self, grid, row, col, word):

        if grid[row][col] != word[0]:
            return False

        for x, y in self.dir:
            rd, cd = row + x, col + y
            flag = True

            for k in range(1, len(word)):

                if (0 <= rd < self.R and
                    0 <= cd < self.C and
                        word[k] == grid[rd][cd]):

                    rd += x
                    cd += y
                else:
                    flag = False
                    break

            if flag:
                return True
        return False

    def patternSearch(self, grid, word):
        count = 0

        self.R = len(grid)
        self.C = len(grid[0])

        for row in range(self.R):
            for col in range(self.C):
                if self.search2D(grid, row, col, word):
                    count += 1
        return count


def main():
    M, N = map(int, input().split())
    word = str(input('Word to find : '))
    words = [list(map(str, input().split())) for _ in range(M)]
    ob = GFG()
    result = ob.patternSearch(words,  word,)
    print(result)


if __name__ == "__main__":
    word = 'sos'
    N, M = 4, 3
    words = [['s', 'o', 's', 'o'],
             ['s', 'o', 'o', 's'],
             ['s', 's', 's', 's']
             ]

    ob = GFG()
    print(ob.patternSearch(words, word))
