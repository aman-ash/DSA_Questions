class Solution:
    def func(self, matrix, size):
        sums = []
        X = size
        Y = len(matrix) // 2 if len(matrix) % size == 0 else (len(matrix) // 2) + 1
        for k in range(Y):
            for r in range(size):
                cur = 0
                for i in range(k, k+X):
                    for j in range(k+r, k+X):
                        temp = matrix[i][j]
                        cur += temp

                sums.append(cur)

        return max(sums)


if __name__ == '__main__':
    matrix = [

        [3, -4, 6, -5, 1],
        [1, -2, 8, -4, -2],
        [3, -8, 9, 3, 1],
        [-7, 3, 4, 2, 7],
        [-3, 7, -5, 7, -6]
    ]
    ob = Solution()
    print(ob.func(matrix, size=3))
