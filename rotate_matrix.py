class Solution:
    def rotate(self, A):
        if len(A) < 2:
            return A

        t1 = 0
        t2 = A[1][0]
        for j in range(len(A)):
            t1 = A[0][j]
            A[0][j] = t2
            t2 = t1

        for i in range(1, len(A)):
            t1 = A[i][len(A) - 1]
            A[i][len(A) - 1] = t2
            t2 = t1

        for i in range(len(A) - 1, -1, -1):
            t1 = A[i][len(A) - 1]
            A[i][len(A) - 1] = t2
            t2 = t1

        for i in range(len(A) - 2, 0, -1):
            t1 = A[i][0]
            A[i][0] = t2
            t2 = t1

        return A


if __name__ == "__main__":
    ob = Solution()
    A = [
        [1, 2],
        [3, 4]
    ]
    ob.rotate(A)
    print(A)
