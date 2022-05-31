class Solution:
    def maximalRectangle(self, matrix):
        temp = [1 for i in range(len(matrix))]
        ans = float("-inf")
        for i in reversed(range(len(matrix))):
            curMat = matrix[i]
            if i == len(matrix) - 1:
                temp = [int(matrix[-1][x]) for x in range(len(matrix[-1]))]
            else:
                for j in range(len(curMat)):
                    temp[j] = 0 if curMat[j] == '0' else temp[j] + \
                        int(curMat[j])
            ans = max(ans, self.helper(temp))
        return ans

    def helper(self, arr):
        if not len(arr):
            return 0
        left = self.firstleftsmallest(arr)
        right = self.firstrightsmallest(arr)
        ans = float("-inf")
        for i in range(len(arr)):
            temp = (right[i] - left[i] - 1) * arr[i]
            ans = max(ans, temp)
        return ans

    def firstleftsmallest(self, arr):
        ans = []
        left = []

        for i in range(len(arr)):
            cur = arr[i]
            flag = False

            while len(left):
                ele, Idx = left[-1]
                if ele < cur:
                    ans.append(Idx)
                    flag = True
                    left.append([cur, i])
                    break
                else:
                    left.pop()

            if not flag:
                ans.append(-1)
                left.append([cur, i])
        return ans

    def firstrightsmallest(self, arr):
        n = len(arr)
        ans = []
        right = []

        for i in reversed(range(len(arr))):
            cur = arr[i]
            flag = False

            while len(right):
                ele, Idx = right[-1]
                if ele < cur:
                    ans.append(Idx)
                    flag = True
                    right.append([cur, i])
                    break
                else:
                    right.pop()

            if not flag:
                ans.append(n)
                right.append([cur, i])
        ans.reverse()
        return ans


if __name__ == "__main__":
    ob = Solution()
    matrix = [["1", "0", "1", "0", "0"], ["1", "0", "1", "1", "1"],
              ["1", "1", "1", "1", "1"], ["1", "0", "0", "1", "0"]]
    mat1 = [['1', '0'], ['1', '0']]
    mat2 = [['1', '0'], ['0', '1']]
    print(ob.maximalRectangle(matrix))
    print(ob.maximalRectangle(mat1))
    print(ob.maximalRectangle(mat2))
