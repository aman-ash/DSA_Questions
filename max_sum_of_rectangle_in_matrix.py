class Solution:
    def maximalRectangle(self, matrix):
        ret = 0
        if not matrix:
            return 0
        count = [0] * len(matrix[0]) + [-1]
        for row in matrix:
            for i in range(len(row)):
                count[i] += 1
                if row[i] == 0:
                    count[i] = 0
            st = [(-1, -1)]
            for index, c in enumerate(count):
                while st[-1][1] > c:
                    ii, cc = st.pop()
                    ret = max(ret, cc * (index - st[-1][0] - 1))
                st.append((index, c))
        return ret


if __name__ == "__main__":
    ob = Solution()
    matrix = [

        [1, 1, 1],
        [0, 1, 1],
        [1, 1, 0]
    ]

    result = ob.maximalRectangle(matrix)
    print(result)
