class Solution:
    def remove_duplicate(self, A, N):
        i = 1
        while i < N:
            if A[i] == A[i - 1]:
                A.remove(A[i - 1])
            else:
                i += 1

        return len(A)


if __name__ == '__main__':
    ob = Solution()
    A = [2, 2, 2, 2, 2]
    N = 5
    print(ob.remove_duplicate(A, N))
