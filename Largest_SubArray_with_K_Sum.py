class Solution:
    def lenOfLongSubarr(self, A, N, K):
        ans, curSum = float("-inf"), 0
        i = j = 0

        while j < N:

            while curSum > K:
                curSum -= A[i]
                i += 1

            else:
                if curSum == K:
                    ans = max(ans, j - i)

                curSum += A[j]
                j += 1

        return 0 if ans == float("-inf") else ans


if __name__ == "__main__":
    ob = Solution()
    A = [4, 1, 1, 1, 2, 3, 5]
    n, k = len(A), 5
    print(ob.lenOfLongSubarr(A, n, k))
