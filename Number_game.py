class Solution:

    def helper(self, A, li):
        ans = [[] for i in range(A + 1)]

        for i in range(A):
            for num in li:
                Idx = i + num
                if Idx <= A:
                    if len(ans[i]):
                        for element in ans[i]:
                            ans[Idx].append([*element, num])
                    else:
                        ans[Idx] = [[num]]

        i = (len(ans[A]) // 2)
        print(*ans[A], sep="\n")
        return ans[A][i:]

    def reverseIt(self, arr):
        i, j = 0, len(arr) - 1

        while i < j:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
            j -= 1


def main():
    A = int(input())
    ob = Solution()
    li = [x for x in range(1, A)]
    result = ob.helper(A, li)
    ob.reverseIt(result)
    print(*result, sep="\n")
    return


if __name__ == '__main__':
    main()
